"""Render source leads separately from editorially indexed challenges."""
from pathlib import Path
from collections import Counter
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
        elif r.get('disposition')!='research_lead':errors.append(tag+': unclassified lead')
    for c in cases:
        if 'evidence_level' in c and c['id'] not in promoted:errors.append(c['id']+': missing research provenance')
    return errors

def slug(s):return re.sub(r'[^\w\u4e00-\u9fff\- ]','',s.lower()).replace(' ','-')

def render_research(cases,sources,records,language):
    en=language=='en';base=Path('docs/en') if en else Path('docs');suffix='_en' if en else ''
    new=[c for c in cases if 'evidence_level' in c]
    leads=[r for r in records if not r.get('included_case_id')]
    x=[r for r in records if r['platform']=='X']
    n=Counter(r['platform'] for r in records)
    lines=['# Community source research' if en else '# 社区出处与本轮新收录','',
        '[简体中文](../RESEARCH.md) | **English**' if en else '**简体中文** | [English](en/RESEARCH.md)','',
        '[Home](../../README.en.md) · [Catalog](INDEX.md) · [Sources](SOURCES.md)' if en else '[首页](../README.md) · [全部案例](INDEX.md) · [来源导航](SOURCES.md)','',
        f'As of 2026-11-08: **{len(new)} additions**, **{len(records)} source records**, including **{len(x)} X posts** and **{len(leads)} remaining leads**. Source records overlap the catalog; do not add these counts together.' if en else f'整理日期：2026-11-08。新增 **{len(new)} 道案例方向**，共整理 **{len(records)} 条来源记录**，其中 **{len(x)} 条 X 帖子**、**{len(leads)} 条尚未纳入正式索引的线索**。来源记录与案例重叠，不能相加算题数。','',
        'This is a bounded research pass, not exhaustive coverage of the internet. Categories follow the project’s visual and interactive coding focus.' if en else '这是本轮有边界的检索结果，不代表穷尽全网。继续围绕视觉、编程与交互测试整理，未将大型学术评测数据集拆成几千道题凑数。','',
        '## How the evidence was checked' if en else '## 来源是怎样核对的','',
        '- GitHub: original prompt files, pinned revisions and output directories were checked. Code links open source, not hosted play sessions.\n- Reddit and Hacker News: author posts and linked projects were read. Claims remain participant-reported.\n- X: original post URLs and IDs were discovered through [Awesome Opus Animation](https://github.com/krillinai/awesome-opus-animation); public FxTwitter metadata was used to match IDs, accounts and text. This is indirect access, not a direct X session or a video review.\n- Official demos: source descriptions were checked. Google AI Studio play/remix links require sign-in and were not run after login.\n- Unknown full prompts, assets, run dates and iteration counts remain unknown. Observation points are our editorial suggestions, not source scoring rules.' if en else '- GitHub：核对作者题面、固定提交和输出目录。代码链接打开源码，不冒充可直接试玩的网页。\n- Reddit / Hacker News：读取发帖者的说明和项目入口；保留“作者报告”的证据性质。\n- X：通过 [Awesome Opus Animation](https://github.com/krillinai/awesome-opus-animation) 发现原帖，再用 FxTwitter 公共元数据核对帖子 ID、账号和文字。这属于间接读取，不是登录 X 直接核验或逐条观看视频。\n- 官方演示：核对官方说明；Google AI Studio 试玩 / Remix 要求登录，本轮未登录运行。\n- 未公开的完整题面、素材来源、运行日期和迭代次数不作推测。观察点是本库编辑建议，不是原站评分规则。','',
        ('Discovery channels: ' if en else '来源渠道：')+' · '.join(f'{k}: {v}' for k,v in n.items()),'',
        '## Newly indexed challenges' if en else '## 已接入索引的新案例','',
        '| Challenge | Material | Prompt | Source / output |' if en else '| 案例 | 资料形态 | 题面 | 出处 / 效果 |','| --- | --- | --- | --- |']
    by_case={r.get('included_case_id'):r for r in records if r.get('included_case_id')}
    for c in new:
        r=by_case[c['id']]
        material=('Work adaptation' if en else '按作品整理') if c['evidence_level']=='public_reader_metadata' else ('Prompt only; no historical output' if en else '仅题面，无历史效果') if c['evidence_level']=='prompt_only' else ('Official demo' if en else '官方演示') if c['source_id'].startswith('google-') else ('Source prompt / work + output' if en else '来源题目 / 作品与效果')
        prompt={'public':('公开','Public'),'partial':('部分 / 示例请求','Partial / example request'),'not_verified':('完整原题未确认','Full prompt unconfirmed')}[c['prompt_availability']][int(en)]
        title=c['title'+suffix]
        links=f'[Source]({c["source_url"]})' if en else f'[出处]({c["source_url"]})'
        if r['demo_urls'] and r['demo_urls'][0]!=c['source_url']:links+=f' · [↗]({r["demo_urls"][0]})'
        lines.append(f'| [{title}](categories/{c["category"]}.md#{slug(title)}) | {material} | {prompt} | {links} |')
    lines.extend(['','## Remaining X leads' if en else '## 待进一步整理的 X 线索','',
        'These posts have retrievable metadata, but prompt completeness, task boundaries, duplicates and asset provenance still need editorial review. They are not counted as new challenges. Titles are discovery labels, not verified original prompt text.' if en else '下面帖子的元数据可读取，但完整题面、任务边界、重复关系和素材来源尚未完成逐项编辑审核，不计入新增题数。标题沿用发现索引的作品名称，不冒充原始提示词。','',
        '| Work / lead | Account | Post | Discovery |' if en else '| 作品线索 | 发布账号 | 原帖 | 发现入口 |','| --- | --- | --- | --- |'])
    for r in leads:lines.append(f'| {r["title"].replace("|","/")} | {r["publisher"]} | [X]({r["source_url"]}) | [Index]({r["discovery_url"]}) |')
    lines.extend(['','## Duplicates and source problems' if en else '## 重复关系与来源问题','',
        '- Pelican animation and browser Minecraft appear again in the X leads; they are not automatically new tasks.\n- The 20-ball heptagon challenge is distinct from the existing single-ball hexagon; its JavaScript adaptation is not another new task.\n- psydox flight and browser OS variants overlap existing themes and are left out of this addition.\n- KCORES snake-pit README mixes a snake prompt with a solar-system rubric and inconsistent board sizes; excluded pending correction.\n- Stock42 HTML links expose code, not hosted demos.\n- Search caches and live Spring Prompt pages disagree on model counts; no dynamic counts or rankings are copied.\n- X video presence does not prove prompt compliance or physical accuracy; no third-party media were copied in this pass.' if en else '- X 线索中再次出现鹈鹕动画和浏览器 Minecraft，不能自动当成新题。\n- 20 球七边形题与已有单球六边形题约束不同；七边形 JavaScript 改写版没有另算一道题。\n- psydox 的飞行模拟和浏览器操作系统题与现有主题重叠，本轮未重复加入。\n- KCORES snake-pit 的 README 将贪吃蛇题面与太阳系评分表混在一起，棋盘尺寸也不一致；暂不收录。\n- Stock42 的 HTML 链接为输出源码，不是托管试玩。\n- Spring Prompt 搜索缓存与实时页模型数量不一致，因此不抄写动态数量或排行榜。\n- X 帖子带视频不等于符合题面或物理正确；本轮未复制第三方图片和视频。','',
        '[Machine-readable source ledger](../../data/research.json)' if en else '[机器可读的来源记录](../data/research.json)',''])
    source_lines=['# Source directory' if en else '# 来源与资源导航','',
        '[简体中文](../SOURCES.md) | **English**' if en else '**简体中文** | [English](en/SOURCES.md)','',
        '[Home](../../README.en.md) · [Catalog](INDEX.md) · [Research](RESEARCH.md)' if en else '[首页](../README.md) · [全部案例](INDEX.md) · [社区出处整理](RESEARCH.md)','',
        f'{len(sources)} source groups. Counts describe this repository’s indexed entries as of 2026-11-08, not all content on the source sites.' if en else f'共 {len(sources)} 个来源组。数量为本库截至 2026-11-08 的收录数，不代表来源网站的全部内容。','']
    for s in sources:
        source_lines.extend([f'## {s["name"+suffix]}','',f'[Source]({s["url"]}) · {s["count"]} entries' if en else f'[来源入口]({s["url"]}) · 本库收录 {s["count"]} 条','',s['note'+suffix],''])
        if s.get('details'+suffix):source_lines.extend([s['details'+suffix],''])
    source_lines.extend(['## Further discovery resources' if en else '## 继续发现案例的资源','',
        '- [Awesome Opus Animation](https://github.com/krillinai/awesome-opus-animation)\n- [Awesome Astra 3D](https://github.com/carpentry-liu/awesome-astra-3d)\n- [Animation2Code](https://anya-ji.github.io/animation2code-website/)\n- [ArtifactsBench](https://artifactsbenchmark.github.io/)','',
        'Some Reddit and CodePen pages reject direct automated HTTP checks (403), although their public text was readable through web search. Google AI Studio links redirect to sign-in. These access limits are not treated as proof that a source was deleted; playback remains unverified.' if en else '部分 Reddit、CodePen 页面会拒绝直接自动 HTTP 检查（403），但可通过网页检索读取公开文字。Google AI Studio 入口跳转登录。这些访问限制不等于来源已删除；本轮未验证实际播放。','',
        'Discovery resources are not a blanket license to copy linked media. Follow each original source; store correction requests through an issue.' if en else '资源索引不代表其链接的第三方素材获得统一转载授权。请继续追溯原作者；来源错误可通过 Issue 更正。',''])
    return {base/'RESEARCH.md':'\n'.join(lines),base/'SOURCES.md':'\n'.join(source_lines)}
