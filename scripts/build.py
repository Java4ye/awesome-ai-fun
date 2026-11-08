#!/usr/bin/env python3
"""Generate the browseable Markdown catalog from data/cases.json."""
from pathlib import Path
import argparse
import json
import sys
from history import check_history, group_history, history_lines
from showcase import (
    CATEGORY_NAMES, check_showcase, collection_entries, image_lines,
    render_homepages, resolve_showcase, work_link,
)
from site_catalog import render_site_catalog

ROOT=Path(__file__).resolve().parents[1]


def render(cases, sources, language='zh', history=(), showcase=()):
    english = language == 'en'
    suffix = '_en' if english else ''
    base = Path('docs/en') if english else Path('docs')
    source_names = {s['id']: s['name'+suffix] for s in sources}
    historical = group_history(history)
    covers = resolve_showcase(history,showcase)
    works, groups, prompts = collection_entries(cases)
    by_id = {case['id']: case for case in cases}
    cases=sorted(cases,key=lambda c:(c['source_id'],c['source_item_no']))
    site = 'https://java4ye.github.io/awesome-ai-fun/site/' + ('' if english else '?lang=zh')
    work_categories = {
        key: [c for c in works if c['category'] == key]
        for key in CATEGORY_NAMES
    }
    index = ['# Work index' if english else '# 作品索引', '',
        '[简体中文](../INDEX.md) | **English**' if english else '**简体中文** | [English](en/INDEX.md)', '',
        f'[Home](../../README.md) · [Open the gallery]({site})' if english else f'[首页](../README.zh-CN.md) · [打开作品画廊]({site})', '',
        f'**{len(works)} works and collections.** Open a collection to browse its individual works.' if english else f'**{len(works)} 个作品与专题。** 专题里的作品可点进去逐个查看。', '',
        ' · '.join(
            f'[{CATEGORY_NAMES[key][english]} ({len(entries)})](#category-{key})'
            for key, entries in work_categories.items() if entries
        ), '']
    for key, entries in work_categories.items():
        if not entries:
            continue
        index.extend([f'<a id="category-{key}"></a>', '', f'## {CATEGORY_NAMES[key][english]}', ''])
        for case in entries:
            cid = case['id']
            group = groups.get(cid)
            title = group[3][english] if group else case['title'+suffix]
            link = f'#{cid}' if group else work_link(case, '', suffix)
            index.append(f'- [{title}]({link})')
        index.append('')
    if prompts:
        index.extend([f'[{len(prompts)} hands-on prompts]({site}#prompt-library)' if english else f'[{len(prompts)} 道动手题]({site}#prompt-library)', ''])
    if groups:
        index.extend(['## Work collections' if english else '## 作品专题', ''])
    for cid, group in groups.items():
        index.extend([f'<a id="{cid}"></a>', '', f'### {group[3][english]}', '', group[4][english], ''])
        for member in group[1]:
            case = by_id[member]
            original = covers.get(member, {}).get('output_url') or case['source_url']
            index.append(f'- [{case["title"+suffix]}]({work_link(case, "", suffix)}) · [{"Original work" if english else "原作品"}]({original})')
        index.append('')
    pages={}
    for key,names in CATEGORY_NAMES.items():
        entries=[c for c in cases if c['category']==key and c.get('evidence_level')!='prompt_only']
        if showcase:entries.sort(key=lambda c:c['id'] not in covers)
        lines=[f'# {names[english]}', '',
            f'[简体中文](../../categories/{key}.md) | **English**' if english else f'**简体中文** | [English](../en/categories/{key}.md)', '',
            '[← Home](../../../README.md) · [Work index](../INDEX.md)' if english else '[← 返回首页](../../README.zh-CN.md) · [作品索引](../INDEX.md)', '',
            '> We provide the summaries and viewing notes. Follow the source links for original works and any published prompts.' if english else '> 简介和观赏要点由本库整理，原作品与已公开的题面见出处。', '']
        pending_open=False
        for c in entries:
            if showcase and c['id'] not in covers and not pending_open:
                pending_count=sum(c['id'] not in covers for c in entries)
                lines.extend(['<details>', f'<summary>Awaiting previews · {pending_count} cases</summary>' if english else f'<summary>待补效果 · {pending_count} 条案例</summary>', '',
                    'Real inline previews are not yet available for these cases. Their original descriptions and source-output links are retained below.' if english else '以下案例暂缺可直接展示的真实预览，保留完整介绍和来源方作品入口。',''])
                pending_open=True
            src_name=source_names[c['source_id']]
            lines.extend([f'## {c["title"+suffix]}', '',
                f'**ID**: `{c["id"]}` · **Source**: [{src_name}]({c["source_url"]}) (catalog source position {c["source_item_no"]})' if english else f'**编号**：`{c["id"]}` · **收录来源**：[{src_name}]({c["source_url"]})（本库来源组内序号 {c["source_item_no"]}）', ''])
            if not english:
                lines.extend([f'**英文标题**：{c["title_en"]}', ''])
            if c['id'] in covers and not covers[c['id']].get('preview'):
                lines.extend(image_lines(c,covers[c['id']],language,'../../../' if english else '../../'))
            lines.extend([c['summary'+suffix], '',
                f'**Source credit / attribution lead**: {c["source_credit_en"]}' if english else f'**原站署名 / 来源线索**：{c["source_credit"]}', '',
                '**What to look for**' if english else '**观赏要点**', ''])
            if 'prompt_availability' in c:
                labels = {'public': ('公开题面', 'Public prompt'), 'partial': ('示例请求或部分题面', 'Example request / partial prompt'), 'not_verified': ('完整原题未确认，按作品整理', 'Full prompt unconfirmed; adapted from work')}
                prompt_label = labels[c['prompt_availability']][1 if english else 0]
                lines[-2:-2] = [('**Prompt availability**: ' if english else '**题面情况**：') + prompt_label, '']
            lines.extend(f'- {v}' for v in c['checks'+suffix])
            lines.extend(['', ('**Tags**: ' if english else '**标签**：') + ', '.join('`'+tag+'`' for tag in c['tags'+suffix]), ''])
            if c['source_id']=='gally':
                lines.extend([f'> All Gally challenges share one page. Find source item **{c["source_item_no"]}** after opening it.' if english else f'> 提示：Gally 的题目都在同一页面，进入后按原站编号 **{c["source_item_no"]}** 查找。', ''])
            records=historical[c['id']]
            prefix='../../../' if english else '../../'
            cover=covers.get(c['id'],{})
            if cover.get('preview'):
                selected=[r for r in records if r.get('id')==cover['id']]
                others=[r for r in records if r not in selected]
                lines.extend(history_lines(selected,language,prefix))
                if others:lines.extend(['<details>','<summary>More model outputs</summary>' if english else '<summary>其他模型的效果</summary>','']+history_lines(others,language,prefix)+['</details>',''])
            else:lines.extend(history_lines(records,language,prefix))
            lines.extend(['---',''])
        if pending_open:lines.extend(['</details>',''])
        pages[base/'categories'/f'{key}.md']='\n'.join(lines).rstrip()+'\n'
    pages[base/'INDEX.md']='\n'.join(index).rstrip()+'\n'
    return pages

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true',help='Compare generated content without writing')
    args=ap.parse_args()
    cases=json.loads((ROOT/'data/cases.json').read_text(encoding='utf-8'))
    from validate import check_data
    sources=json.loads((ROOT/'data/sources.json').read_text(encoding='utf-8'))
    problems=check_data(cases,sources)
    history=json.loads((ROOT/'data/history.json').read_text(encoding='utf-8'))
    problems.extend(check_history(cases,history,ROOT))
    from research import check_research, render_sources
    research=json.loads((ROOT/'data/research.json').read_text(encoding='utf-8'))
    problems.extend(check_research(cases,research))
    showcase=json.loads((ROOT/'data/showcase.json').read_text(encoding='utf-8'))
    problems.extend(check_showcase(cases,history,showcase,ROOT))
    if problems:
        print('Catalog invalid: '+ '; '.join(problems));return 1
    pages={**render(cases,sources,history=history,showcase=showcase), **render(cases,sources,'en',history,showcase),
           **render_sources(sources,'zh'), **render_sources(sources,'en'),
           **render_homepages(cases,history,showcase,'zh'),
           **render_homepages(cases,history,showcase,'en'),
           **render_site_catalog(cases,sources,history,showcase)}
    mismatch=[]
    for rel,contents in pages.items():
        path=ROOT/rel
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != contents: mismatch.append(str(rel))
        else:
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text(contents,encoding='utf-8')
    if mismatch:
        print('❌ Outdated generated files: '+', '.join(mismatch))
        print('Run: python scripts/build.py')
        return 1
    print(f'✅ {"Verified" if args.check else "Generated"} {len(pages)} catalog files from {len(cases)} cases')
    return 0
if __name__=='__main__':sys.exit(main())
