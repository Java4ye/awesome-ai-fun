"""Generate a single-column homepage from cases and attributed previews."""
from pathlib import Path
from urllib.parse import urlsplit
from hashlib import sha256
from html import escape
import re

INTRO = {
    'zh': '# Awesome AI Fun · 有趣的 AI 作品与玩法合集\n\n**简体中文** | [English](README.md)\n\n> 收集大家用 AI 做出来的好玩作品：能逛的 3D 世界、小游戏、动画，还有各种奇怪的交互点子。\n>\n> 往下看效果，喜欢就去试玩，或者看看作者是怎么做出来的。\n',
    'en': '# Awesome AI Fun · Fun AI creations and things to try\n\n[简体中文](README.zh-CN.md) | **English**\n\n> A collection of fun things people make with AI: 3D worlds to explore, little games, animations, and odd interactive ideas.\n>\n> Browse the previews, try something you like, or see how its creator made it.\n',
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
        if p.get('rights')=='source_reference':
            for key in ('source_url','output_url'):
                u=urlsplit(p.get(key,''))
                if u.scheme!='https' or not u.netloc:errors.append(tag+': invalid '+key)
            if p.get('license_status')!='not_verified':errors.append(tag+': reference must not imply a redistribution license')
            if p.get('capture'):
                capture=(root/p['capture']).resolve()
                if not capture.is_relative_to(root.resolve()) or not p['capture'].startswith('assets/previews/historical/') or not capture.is_file():errors.append(tag+': unsafe or missing capture')
                elif sha256(capture.read_bytes()).hexdigest()!=p.get('capture_sha256'):errors.append(tag+': capture checksum mismatch')
                if not p.get('captured_on'):errors.append(tag+': missing capture date')
            else:
                u=urlsplit(p.get('image_url',''))
                if u.scheme!='https' or not u.netloc:errors.append(tag+': invalid source image')
            if p.get('video_url') and urlsplit(p['video_url']).scheme!='https':errors.append(tag+': invalid video URL')
            for key in ('publisher','model','note','note_en'):
                if not p.get(key):errors.append(tag+': missing '+key)
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
    local=preview.get('preview') or preview.get('capture')
    src=prefix+local if local else preview['image_url']
    image_source=preview.get('preview_source_url') or preview.get('image_url') or preview['output_url']
    target=preview.get('video_url') or preview['output_url']
    alt=case['title'+suffix]+' — '+preview['model']
    width=preview.get('display_width',480 if preview.get('preview') else 720)
    lines=[f'[<img src="{escape(src,quote=True)}" alt="{escape(alt,quote=True)}" width="{width}">]({target})','',
        f'**Model:** {preview["model"]} · **Author / publisher:** {preview["publisher"]}' if en else f'**模型：** {preview["model"]} · **作者 / 发布者：** {preview["publisher"]}','',
        f'Image: {preview["publisher"]} · [Original image / work]({image_source})' if en else f'图片署名：{preview["publisher"]} · [原图 / 作品出处]({image_source})','']
    if preview.get('rights')=='MIT':lines[-2]+=f' · [MIT]({prefix}{preview["license_file"]})'
    else:lines[-2]+=f' · [Media notice]({prefix}docs/en/THIRD_PARTY_MEDIA.md)' if en else f' · [素材说明]({prefix}docs/THIRD_PARTY_MEDIA.md)'
    if preview.get('preview'):
        lines.extend([f'[Source run record]({preview["source_url"]})' if en else f'[来源运行记录]({preview["source_url"]})',''])
    if preview.get('run_date'):
        lines.extend([('Source-reported run date: ' if en else '来源方记录的运行日期：')+preview['run_date'], ''])
    if preview.get('note'+suffix):lines.extend([preview['note'+suffix],''])
    return lines

WORK_GROUPS = (
    ('svg-001', tuple(f'svg-{n:03d}' for n in range(1,31)), ('svg-010','svg-007','svg-003'),
     ('奇怪生物与机械', 'Odd Creatures and Machines'),
     ('同一个 SVG 系列：企鹅抛电锯、水母转摩天轮、海星开推土机，还有 27 个怪点子。',
      'One SVG series: a chainsaw-juggling penguin, a jellyfish at a Ferris wheel, a starfish with a bulldozer, and 27 more odd ideas.')),
    ('museum-010', ('museum-010','stock42-tetris-3d'), ('museum-010',),
     ('俄罗斯方块', 'Tetris'),
     ('从经典单文件版玩起，另有带音效和排行榜的 3D 风格版。',
      'Start with classic single-file Tetris, or try the 3D-style version with sound and high scores.')),
    ('google-sim-double-pendulum', ('google-sim-double-pendulum','stock42-triple-pendulum'), ('stock42-triple-pendulum',),
     ('混沌摆', 'Chaotic Pendulums'),
     ('拖动双摆看轨迹如何变化，或看看三摆如何用末端轨迹作画。',
      'Explore how a double pendulum moves, or watch a triple pendulum draw with its tip.')),
    ('museum-002', ('museum-002','kcores-ball-bouncing-inside-spinning-heptagon','museum-017','electricazimuth-ball_bound'), ('museum-002',),
     ('弹球与碰撞', 'Bouncing Balls and Collisions'),
     ('从旋转六边形里的单球开始，再看多球碰撞、七边形和四维空间。',
      'Start with a ball in a spinning hexagon, then explore multiple balls, a heptagon, and four dimensions.')),
    ('museum-001', ('museum-001','pelican-sdf-001'), ('museum-001','pelican-sdf-001'),
     ('鹈鹕骑自行车', 'Pelican on a Bicycle'),
     ('同一个脑洞，两种做法：SVG 动画和可旋转查看的 3D 场景。',
      'One idea in two forms: an SVG animation and a 3D scene you can rotate.')),
)


def work_link(case,docs,suffix):
    return f'{docs}categories/{case["category"]}.md#{slug(case["title"+suffix])}'


CATEGORY_NAMES = {
    'games': ('游戏', 'Games'),
    '3d': ('3D 与空间', '3D & Spaces'),
    'animation': ('动画与物理', 'Animation & Physics'),
    'applications': ('应用与交互', 'Apps & Interaction'),
    'svg': ('SVG 绘画', 'SVG Art'),
}

PLAY_LINKS = {
    'aidens-revenge': 'https://aidens-revenge.pages.dev/',
    'sac-little-prince': 'https://littleprince.dev/',
    'x-dotey-2102940980379017293': 'https://s.baoyu.io/files/taohuayuan/index.html',
    'x-studio_veco-2102684366996738511': 'https://powapowa.pages.dev/',
    'x-dangreenheck-2103004432786993341': 'https://dgreenheck.github.io/tidewater/',
    'between-tokens-interactive-story': 'https://chrisjz.github.io/between-tokens/',
}


def play_link(cid, output):
    url=urlsplit(output)
    if url.hostname=='aitestmuseum.com' and url.path.startswith('/results/') and url.path.endswith('/output.html'):
        return output
    return PLAY_LINKS.get(cid)


def collection_entries(cases):
    by_id={c['id']:c for c in cases}
    groups={g[0]:g for g in WORK_GROUPS if set(g[1])<=by_id.keys()}
    grouped_away={cid for g in groups.values() for cid in g[1] if cid!=g[0]}
    prompts=[c for c in cases if c.get('evidence_level')=='prompt_only']
    entries=[c for c in cases if c['id'] not in grouped_away and c not in prompts]
    return entries,groups,prompts


def render_homepages(cases,history,records,language):
    en=language=='en';suffix='_en' if en else '';covers=resolve_showcase(history,records)
    works,groups,prompts=collection_entries(cases)
    docs='docs/en/' if en else 'docs/'
    site='https://java4ye.github.io/awesome-ai-fun/site/' + ('' if en else '?lang=zh')
    suggest='https://github.com/Java4ye/awesome-ai-fun/issues/new?template=new-case' + ('-en' if en else '') + '.md'
    lines=[INTRO[language].rstrip(),'',
        f'**[Open the gallery]({site})** · [Suggest a work]({suggest}) · [Work index]({docs}INDEX.md)' if en else
        f'**[打开作品画廊]({site})** · [推荐作品]({suggest}) · [作品索引]({docs}INDEX.md)','',
        f'**{len(works)} works and collections**' if en else f'**{len(works)} 个作品与专题**','',
        '## All works' if en else '## 全部作品','',
        ' · '.join(f'[{names[en]}](#category-{key})' for key,names in CATEGORY_NAMES.items()),'']
    def a(label, url):
        return f'<a href="{escape(url,quote=True)}">{escape(label)}</a>'

    for key,names in CATEGORY_NAMES.items():
        entries=[c for c in works if c['category']==key]
        if not entries:continue
        lines.extend([f'<a id="category-{key}"></a>','',f'### {names[en]} · {len(entries)}','','<table>'])
        for offset in range(0,len(entries),3):
            lines.append('  <tr>')
            for c in entries[offset:offset+3]:
                cid=c['id'];group=groups.get(cid)
                sample=next((m for m in (group[2] if group else (cid,)) if m in covers),None)
                p=covers.get(sample)
                title=group[3][en] if group else c['title'+suffix]
                detail=f'{docs}INDEX.md#{cid}' if group else work_link(c,docs,suffix)
                cell=[]
                if p:
                    src=p.get('preview') or p.get('capture') or p['image_url']
                    width=min(240,round(p.get('display_width',720)/3))
                    target=p.get('video_url') or p['output_url']
                    cell.append(f'<a href="{escape(target,quote=True)}"><img src="{escape(src,quote=True)}" alt="{escape(title,quote=True)}" width="{width}" loading="lazy"></a><br>')
                else:
                    cell.append('<sub>Preview pending</sub><br>' if en else '<sub>画面待补</sub><br>')
                cell.append(f'<strong>{a(title,detail)}</strong><br>')
                play=next((url for m in (group[1] if group else (cid,))
                    if (url:=play_link(m,covers.get(m,{}).get('output_url','')))),None)
                if play:
                    cell.append(a('Play' if en else '试玩',play)+' · ')
                cell.append(a('Source' if en else '原出处',p['source_url'] if p else c['source_url']))
                lines.append(f'    <td width="33%" valign="top">{"".join(cell)}</td>')
            lines.extend(['    <td></td>']*(3-len(entries[offset:offset+3])))
            lines.append('  </tr>')
        lines.extend(['</table>',''])
    lines.extend([f'[{len(prompts)} hands-on prompts]({site}#prompt-library)' if en else
        f'[{len(prompts)} 道动手题]({site}#prompt-library)',''])
    lines.extend(['## Suggest a work' if en else '## 推荐作品','',
        '[Open an Issue](https://github.com/Java4ye/awesome-ai-fun/issues/new/choose) with an original link and a short description. Maintainers check submissions and update the collection. Please use Issues for submissions and corrections.' if en else '欢迎[提交 Issue](https://github.com/Java4ye/awesome-ai-fun/issues/new/choose)，附上原始链接和一句话介绍。维护者核对后统一收录；投稿和更正都走 Issue。','',
        f'[Sources]({docs}SOURCES.md) · [Media credits]({docs}THIRD_PARTY_MEDIA.md)' if en else f'[来源导航]({docs}SOURCES.md) · [素材署名]({docs}THIRD_PARTY_MEDIA.md)','',
        'Previews are credited to their sources. Original content and code: [MIT](LICENSE). Third-party media retain their owners’ rights.' if en else '效果预览附原始出处。仓库原创内容与代码采用 [MIT](LICENSE)，第三方素材的权利归原权利人。',''])
    readme=Path('README.md' if en else 'README.zh-CN.md')
    return {readme:'\n'.join(lines)}
