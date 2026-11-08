"""Validate provenance for included records and render the source directory."""
from pathlib import Path
from urllib.parse import urlsplit
import re

def check_research(cases, records):
    errors, ids, posts, promoted = [], set(), set(), set()
    by_id={c['id']:c for c in cases}
    for r in records:
        tag='research '+str(r.get('id'))
        if not r.get('id') or r['id'] in ids: errors.append(tag+': duplicate/missing id')
        ids.add(r.get('id'))
        for key in ('source_url','discovery_url'):
            p=urlsplit(r.get(key,''))
            if p.scheme!='https' or not p.netloc:errors.append(tag+': invalid '+key)
        if r.get('rights')!='link_only':errors.append(tag+': unsupported media rights')
        if r.get('platform')=='X':
            if r['source_url'] in posts:errors.append(tag+': duplicate post')
            posts.add(r['source_url'])
            if r.get('verification')=='public_reader_metadata':
                if not re.fullmatch('[a-f0-9]{64}',r.get('source_text_sha256','')):errors.append(tag+': missing evidence hash')
                if not r.get('reader_url','').startswith('https://api.fxtwitter.com/'):errors.append(tag+': missing reader attribution')
        cid=r.get('included_case_id')
        if cid:
            if cid not in by_id:errors.append(tag+': unknown case')
            elif by_id[cid]['source_url']!=r['source_url']:errors.append(tag+': source mismatch')
            if cid in promoted:errors.append(tag+': duplicate promoted case')
            promoted.add(cid)
        else:errors.append(tag+': missing included case')
    for c in cases:
        if 'evidence_level' in c and c['id'] not in promoted:errors.append(c['id']+': missing research provenance')
    return errors

def render_sources(sources, language):
    en=language=='en';base=Path('docs/en') if en else Path('docs');suffix='_en' if en else ''
    source_lines=['# Source directory' if en else '# 来源与资源导航','',
        '[简体中文](../SOURCES.md) | **English**' if en else '**简体中文** | [English](en/SOURCES.md)','',
        '[Home](../../README.md) · [Work index](INDEX.md)' if en else '[首页](../README.zh-CN.md) · [作品索引](INDEX.md)','',
        f'{len(sources)} source groups. Counts are catalog records and include individual works in collections and prompt-only entries.' if en else f'共 {len(sources)} 个来源组。数量按收录记录统计，包含专题内的单件作品和仅有题面的条目。','']
    for s in sources:
        source_lines.extend([f'## {s["name"+suffix]}','',f'[Source]({s["url"]}) · {s["count"]} entries' if en else f'[来源入口]({s["url"]}) · 本库收录 {s["count"]} 条','',s['note'+suffix],''])
        if s.get('details'+suffix):source_lines.extend([s['details'+suffix],''])
    source_lines.extend(['## Further discovery resources' if en else '## 继续发现案例的资源','',
        '- [Awesome Opus Animation](https://github.com/krillinai/awesome-opus-animation)\n- [Awesome Astra 3D](https://github.com/carpentry-liu/awesome-astra-3d)\n- [Animation2Code](https://anya-ji.github.io/animation2code-website/)\n- [ArtifactsBench](https://artifactsbenchmark.github.io/)','',
        'Some Reddit and CodePen pages reject direct automated HTTP checks (403), although their public text was readable through web search. Google AI Studio links redirect to sign-in. X attributions were checked using FxTwitter public metadata. Actual playback may require opening the original source.' if en else '部分 Reddit、CodePen 页面会拒绝直接自动 HTTP 检查（403），但可通过网页检索读取公开文字。Google AI Studio 入口跳转登录。X 帖子的出处通过 FxTwitter 公开元数据核对。实际播放请前往原出处查看。','',
        'Discovery resources are not a blanket license to copy linked media. Follow each original source; store correction requests through an issue.' if en else '资源索引不代表其链接的第三方素材获得统一转载授权。请继续追溯原作者；来源错误可通过 Issue 更正。',''])
    return {base/'SOURCES.md':'\n'.join(source_lines)}
