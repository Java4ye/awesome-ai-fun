"""Generate a single-column homepage from cases and attributed previews."""
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit
import re

INTRO = {
    'zh': '# Awesome AI Tests · 有趣的 AI 测试案例收藏夹\n\n**简体中文** | [English](README.en.md)\n\n> 收集互联网上那些好玩、奇怪、让人忍不住想拿去考一考大模型的测试题。  \n> **不做模型排行榜，先把值得尝试的题目收集好。**\n\nA curated collection of fun and reproducible AI model challenges — in Chinese and English, with source links.\n',
    'en': '# Awesome AI Tests · A collection of fun AI challenges\n\n[简体中文](README.md) | **English**\n\n> A collection of fun, strange, and imaginative challenges to try with AI models.\n> Collect interesting tasks first, with clear sources and useful observation points.\n',
}

def slug(value):
    return re.sub(r'[^\w\u4e00-\u9fff\- ]','',value.lower()).replace(' ','-')

def check_showcase(cases, history, records, root):
    errors=[];seen=set();by_history={r['id']:r for r in history}
    by_case={c['id']:c for c in cases}
    for p in records:
        cid=p.get('case_id');tag=f'showcase {cid}'
        if cid not in by_case:errors.append(tag+': unknown case')
        if cid in seen:errors.append(tag+': duplicate case')
        seen.add(cid)
        if 'history_id' in p:
            r=by_history.get(p['history_id'])
            if not r or r.get('case_id')!=cid or not r.get('preview'):errors.append(tag+': missing or mismatched historical preview')
            continue
        for key in ('image_url','source_url','output_url','license_url'):
            u=urlsplit(p.get(key,''))
            if u.scheme!='https' or not u.netloc:errors.append(tag+': invalid '+key)
        pin=p.get('source_commit','')
        if not re.fullmatch('[a-f0-9]{40}',pin) or any('/'+pin+'/' not in p.get(k,'') for k in ('image_url','source_url','license_url')):
            errors.append(tag+': preview and license must use the fixed source commit')
        license_path=(root/p.get('license_file','')).resolve()
        if p.get('rights')!='MIT' or not license_path.is_relative_to(root.resolve()) or not license_path.is_file():errors.append(tag+': missing reusable license')
        for k in ('publisher','model','note','note_en'):
            if not isinstance(p.get(k),str) or not p[k].strip():errors.append(tag+': missing '+k)
    return errors

def resolve_showcase(history, records):
    by_history={r['id']:r for r in history}
    return {p['case_id']:dict(by_history[p['history_id']]) if 'history_id' in p else dict(p) for p in records}

def image_lines(case, preview, language, prefix=''):
    en=language=='en';suffix='_en' if en else ''
    src=prefix+preview['preview'] if preview.get('preview') else preview['image_url']
    image_source=preview.get('preview_source_url',preview['source_url'])
    alt=case['title'+suffix]+' — '+preview['model']
    lines=[f'[![{alt}]({src})]({preview["output_url"]})','',
        f'**Model:** {preview["model"]} · **Author / publisher:** {preview["publisher"]}' if en else f'**模型：** {preview["model"]} · **作者 / 发布者：** {preview["publisher"]}','',
        f'Image: {preview["publisher"]} · [Original image]({image_source}) · [MIT license]({prefix}{preview["license_file"]})' if en else f'图片署名：{preview["publisher"]} · [原图出处]({image_source}) · [MIT 许可]({prefix}{preview["license_file"]})','']
    if preview.get('preview'):
        lines.extend([f'[Source run record]({preview["source_url"]})' if en else f'[来源运行记录]({preview["source_url"]})',''])
    if preview.get('run_date'):
        lines.extend([('Source-reported run date: ' if en else '来源方记录的运行日期：')+preview['run_date'], ''])
    if preview.get('note'+suffix):lines.extend([preview['note'+suffix],''])
    return lines

def card_lines(case,preview,history,language,prefix='',docs_prefix='docs/'):
    en=language=='en';suffix='_en' if en else '';title=case['title'+suffix]
    summary=case['summary'+suffix]
    if case.get('evidence_level')=='public_reader_metadata':
        summary=('Observe: ' if en else '观察重点：')+(' / ' if en else '；').join(case['checks'+suffix])+'。'
    media=image_lines(case,preview,language,prefix)
    lines=[f'### {title}','']+media[:2]+[summary,'']+media[2:]
    detail=f'{docs_prefix}categories/{case["category"]}.md#{slug(title)}'
    links=[f'[Original source]({case["source_url"]})' if en else f'[原题 / 来源]({case["source_url"]})',
        f'[Open work]({preview["output_url"]})' if en else f'[打开作品]({preview["output_url"]})',
        f'[Details]({detail})' if en else f'[案例详情]({detail})']
    if urlsplit(case['source_url']).netloc=='x.com':links.append(f'[▶ Creator video]({case["source_url"]})' if en else f'[▶ 作者视频]({case["source_url"]})')
    lines.extend([' · '.join(links),''])
    others=[r for r in history if r['case_id']==case['id'] and r.get('preview') and r.get('preview')!=preview.get('preview')]
    if others:
        lines.extend(['<details>','<summary>More model outputs</summary>' if en else '<summary>其他模型的效果</summary>',''])
        for r in others:lines.extend(image_lines(case,r,language,prefix))
        lines.extend(['</details>',''])
    return lines

def render_homepages(cases,sources,history,records,categories,language):
    en=language=='en';suffix='_en' if en else '';covers=resolve_showcase(history,records)
    count=Counter(c['category'] for c in cases)
    names={'svg':('SVG 绘画','SVG Drawing'),'animation':('动画与物理','Animation & Physics'),'3d':('3D 与空间','3D & Spatial Scenes'),'games':('游戏开发','Games'),'applications':('应用与交互','Apps & Interaction')}
    # Put categories with visible works first; this is a browsing order, not a ranking.
    order=['games','3d','applications','animation','svg']
    docs='docs/en/' if en else 'docs/'
    lines=[INTRO[language].rstrip(),'','## Categories' if en else '## 分类导航','',
        ' · '.join(f'[{names[k][int(en)]} ({count[k]})](#category-{k})' for k in order),'',
        f'**{len(cases)} cases** · {len(covers)} with inline previews · {len(cases)-len(covers)} awaiting previews.' if en else f'**{len(cases)} 条案例** · {len(covers)} 条已有预览 · {len(cases)-len(covers)} 条待补效果。','']
    for k in order:
        entries=[c for c in cases if c['category']==k]
        shown=[c for c in entries if c['id'] in covers];pending=[c for c in entries if c['id'] not in covers]
        lines.extend([f'<a id="category-{k}"></a>','',f'## {names[k][int(en)]} · {len(entries)}','',
            '[↑ Categories](#categories)' if en else '[↑ 返回分类导航](#分类导航)',''])
        for c in shown:
            lines.extend([f'<a id="case-{c["id"]}"></a>',''])
            lines.extend(card_lines(c,covers[c['id']],history,language,docs_prefix=docs))
            lines.extend(['---',''])
        if pending:
            lines.extend(['<details>',f'<summary>Awaiting previews · {len(pending)} cases</summary>' if en else f'<summary>待补效果 · {len(pending)} 条案例</summary>','',
                'Real, reusable previews are still missing. Source output links are retained below; they are not inline previews.' if en else '这些案例尚缺可直接展示的真实预览。下方保留来源方作品入口，不将链接当成已补齐效果。','',
                '| Case | What to try | Source / output |' if en else '| 案例 | 测试内容 | 来源 / 历史作品 |','| --- | --- | --- |'])
            for c in pending:
                title=c['title'+suffix];summary=c['summary'+suffix].replace('|','/')
                if len(summary)>180:summary=summary[:177]+'…'
                if c.get('evidence_level')=='public_reader_metadata':summary=('Observe: ' if en else '观察：')+c['checks'+suffix][0]
                detail=f'{docs}categories/{k}.md#{slug(title)}'
                original=f'[Source]({c["source_url"]})' if en else f'[来源]({c["source_url"]})'
                h=next((r for r in history if r['case_id']==c['id']),None)
                if h and h['output_url']!=c['source_url']:original+=f' · [↗]({h["output_url"]})'
                lines.append(f'| <a id="case-{c["id"]}"></a>[{title}]({detail}) | {summary} | {original} |')
            lines.extend(['','</details>',''])
    lines.extend(['## Contribute' if en else '## 欢迎补充','',
        f'Share a challenge, an original preview or an attribution correction through [Issues](https://github.com/Java4ye/awesome-ai-tests/issues/new/choose) or a pull request. See the [contribution guide](CONTRIBUTING.en.md).' if en else '欢迎通过 [Issues](https://github.com/Java4ye/awesome-ai-tests/issues/new/choose) 或 Pull Request 补充题目、真实效果和原始出处，或纠正署名。详见[贡献指南](CONTRIBUTING.md)。','',
        f'[Sources]({docs}SOURCES.md) · [History]({docs}HISTORY.md) · [Research leads]({docs}RESEARCH.md) · [Guide]({docs}GUIDE.md) · [Maintenance]({docs}MAINTENANCE.md) · [Media credits](THIRD_PARTY_MEDIA.en.md)' if en else f'[来源导航]({docs}SOURCES.md) · [历史档案]({docs}HISTORY.md) · [社区线索]({docs}RESEARCH.md) · [使用指南]({docs}GUIDE.md) · [维护说明]({docs}MAINTENANCE.md) · [素材署名](THIRD_PARTY_MEDIA.md)','',
        'Images show source-published works; historical models were not rerun here. Full videos open at creator posts. Original content and code: [MIT](LICENSE). Third-party previews retain their own licenses. Source conditions differ and do not form a standardized ranking.' if en else '图片为来源方作品，本库未重新调用历史模型；完整视频通过作者原帖打开。本库原创内容与代码采用 [MIT](LICENSE)，第三方预览按各自许可处理。不同来源的测试条件不构成统一排行榜。',''])
    readme=Path('README.en.md' if en else 'README.md')
    base=Path('docs/en') if en else Path('docs');prefix='../../' if en else '../'
    gallery=['# Preview gallery' if en else '# 案例效果画廊','',
        '[简体中文](../GALLERY.md) | **English**' if en else '**简体中文** | [English](en/GALLERY.md)','',
        '[Home](../../README.en.md) · [All cases](INDEX.md)' if en else '[首页](../README.md) · [全部案例](INDEX.md)','',
        f'{len(covers)} cases with real previews. Additional model outputs are collapsed under the relevant case.' if en else f'目前 {len(covers)} 条案例有真实预览；同题的其他模型结果折叠在对应案例下。','']
    for c in cases:
        if c['id'] in covers:gallery.extend(card_lines(c,covers[c['id']],history,language,prefix=prefix,docs_prefix=''))
    gallery.extend([f'[Media credits]({prefix}THIRD_PARTY_MEDIA.en.md)' if en else f'[素材署名]({prefix}THIRD_PARTY_MEDIA.md)',''])
    return {readme:'\n'.join(lines),base/'GALLERY.md':'\n'.join(gallery)}
