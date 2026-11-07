#!/usr/bin/env python3
"""Generate the browseable Markdown catalog from data/cases.json."""
from pathlib import Path
from collections import Counter
import argparse
import json
import sys

ROOT=Path(__file__).resolve().parents[1]
CATEGORIES=[('svg','SVG 绘画','画出来，更要画得对'),('animation','动画与物理','让画面真正动起来'),('3d','3D 与空间','把空间关系做正确'),('games','游戏开发','不仅能看，还要能玩'),('applications','应用与交互','从好看的界面走向可用的功能')]
EN_CATEGORIES=[('svg','SVG Drawing','Draw recognizable objects and believable relationships'),('animation','Animation & Physics','Make motion and simulation work'),('3d','3D & Spatial Scenes','Build coherent spatial relationships'),('games','Games','Make something playable'),('applications','Apps & Interaction','Turn interfaces into usable features')]


def render(cases, sources, language='zh'):
    english = language == 'en'
    categories = EN_CATEGORIES if english else CATEGORIES
    suffix = '_en' if english else ''
    base = Path('docs/en') if english else Path('docs')
    source_names = {s['id']: s['name'+suffix] for s in sources}
    count=Counter(c['category'] for c in cases)
    order={name:i for i,(name,_,_) in enumerate(CATEGORIES)}
    cases=sorted(cases,key=lambda c:(order[c['category']],c['source_id'],c['source_item_no']))
    index = ['# All challenges' if english else '# 全部测试案例', '',
        '[简体中文](../INDEX.md) | **English**' if english else '**简体中文** | [English](en/INDEX.md)', '',
        f'> **{len(cases)} challenges** from public sources. This is a curated index; this repository has not tested these challenges.' if english else f'> 收录 **{len(cases)} 道**公开来源的 AI 测试案例。这里是导航与整理，不代表已经由本仓库实测。', '',
        ('Browse by type: ' if english else '按类型查看：') + ' · '.join(f'[{label} ({count[key]})](categories/{key}.md)' for key,label,_ in categories), '',
        '| ID | Challenge | Type | Source |' if english else '| 编号 | 案例 | 分类 | 来源 |', '| --- | --- | --- | --- |']
    pages={}
    for key,label,subtitle in categories:
        entries=[c for c in cases if c['category']==key]
        lines=[f'# {label}', '',
            f'[简体中文](../../categories/{key}.md) | **English**' if english else f'**简体中文** | [English](../en/categories/{key}.md)', '',
            f'> {subtitle} · **{len(entries)} challenges**' if english else f'> {subtitle} · 共 **{len(entries)} 道**', '',
            '[← Home](../../../README.en.md) · [All challenges](../INDEX.md)' if english else '[← 返回首页](../../README.md) · [全部案例](../INDEX.md)', '',
            '> The summaries and observation points below are our editorial descriptions, not original prompts or official scoring rules.' if english else '> 下文简介和观察点为本库整理，不是原始提示词或官方评分规则。', '']
        for c in entries:
            src_name=source_names[c['source_id']]
            lines.extend([f'## {c["title"+suffix]}', '',
                f'**ID**: `{c["id"]}` · **Source**: [{src_name}]({c["source_url"]}) (source item {c["source_item_no"]})' if english else f'**编号**：`{c["id"]}` · **收录来源**：[{src_name}]({c["source_url"]})（原站第 {c["source_item_no"]} 题）', ''])
            if not english:
                lines.extend([f'**英文标题**：{c["title_en"]}', ''])
            lines.extend([c['summary'+suffix], '',
                f'**Source credit / attribution lead**: {c["source_credit_en"]}' if english else f'**原站署名 / 来源线索**：{c["source_credit"]}', '',
                '**What to observe**' if english else '**可以观察什么？**', ''])
            lines.extend(f'- {v}' for v in c['checks'+suffix])
            lines.extend(['', ('**Tags**: ' if english else '**标签**：') + ', '.join('`'+tag+'`' for tag in c['tags'+suffix]), '',
                f'**Prompts and outputs**: [View the source]({c["source_url"]}) · **Test status in this repository**: Not tested' if english else f'**提示词与作品**：[前往原站查看]({c["source_url"]}) · **本库测试情况**：未实测', ''])
            if c['source_id']=='gally':
                lines.extend([f'> All Gally challenges share one page. Find source item **{c["source_item_no"]}** after opening it.' if english else f'> 提示：Gally 的题目都在同一页面，进入后按原站编号 **{c["source_item_no"]}** 查找。', ''])
            lines.extend(['---',''])
        pages[base/'categories'/f'{key}.md']='\n'.join(lines).rstrip()+'\n'
        for c in entries:
            title = c['title'+suffix]
            index.append(f'| `{c["id"]}` | [{title}](categories/{key}.md#{slug(title)}) | {label} | [{source_names[c["source_id"]]}]({c["source_url"]}) |')
    pages[base/'INDEX.md']='\n'.join(index)+'\n'
    return pages

# GitHub heading fragment handling for Chinese: GitHub keeps CJK characters and removes punctuation.
def slug(title):
    import re
    return re.sub(r'[^\w\u4e00-\u9fff\- ]','',title.lower()).replace(' ','-')

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true',help='Compare generated content without writing')
    args=ap.parse_args()
    cases=json.loads((ROOT/'data/cases.json').read_text(encoding='utf-8'))
    from validate import check_data
    sources=json.loads((ROOT/'data/sources.json').read_text(encoding='utf-8'))
    problems=check_data(cases,sources)
    if problems:
        print('Catalog invalid: '+ '; '.join(problems));return 1
    pages={**render(cases,sources), **render(cases,sources,'en')}
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
    print(f'✅ {"Verified" if args.check else "Generated"} {len(pages)} Markdown pages from {len(cases)} cases')
    return 0
if __name__=='__main__':sys.exit(main())
