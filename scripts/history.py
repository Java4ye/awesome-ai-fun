"""Validate and render attributed historical outputs without executing them."""
from collections import defaultdict
from datetime import date
from hashlib import sha256
from pathlib import Path
from urllib.parse import urlsplit
import re
import json


def check_history(cases, records, root):
    errors, ids = [], set()
    case_ids = {c['id'] for c in cases}
    root = root.resolve()
    for r in records:
        prefix = f"history {r.get('id', '<missing>')}"
        for key in ('id', 'case_id', 'publisher', 'model', 'run_period', 'run_period_en', 'collected_on', 'source_url', 'output_url', 'context_url', 'kind', 'conditions', 'conditions_en', 'rights'):
            if not isinstance(r.get(key), str) or not r[key].strip():
                errors.append(f'{prefix}: missing {key}')
        if r.get('id') in ids: errors.append(f'{prefix}: duplicate id')
        ids.add(r.get('id'))
        if r.get('case_id') not in case_ids: errors.append(f'{prefix}: unknown case')
        if r.get('kind') not in ('source_run', 'community_run', 'official_demo'): errors.append(f'{prefix}: invalid kind')
        if r.get('rights') not in ('link_only', 'MIT'): errors.append(f'{prefix}: unsupported rights basis')
        for key in ('source_url', 'output_url', 'context_url', 'license_url', 'preview_source_url'):
            value = r.get(key)
            if value is None and key in ('license_url', 'preview_source_url'): continue
            if not isinstance(value, str) or urlsplit(value).scheme != 'https' or not urlsplit(value).netloc:
                errors.append(f'{prefix}: invalid {key}')
        for key in ('run_date', 'published_on', 'collected_on'):
            if r.get(key) is not None:
                try: date.fromisoformat(r[key])
                except (TypeError, ValueError): errors.append(f'{prefix}: invalid {key}')
        if r.get('preview'):
            if r.get('rights') != 'MIT' or not r.get('license_url'): errors.append(f'{prefix}: preview needs a redistribution license')
            for key in ('preview', 'license_file', 'source_snapshot'):
                value = r.get(key)
                if not isinstance(value, str) or not value:
                    errors.append(f'{prefix}: missing {key}')
                    continue
                path = (root / value).resolve()
                if not path.is_relative_to(root) or not path.is_file(): errors.append(f'{prefix}: unsafe or missing {key}')
                elif key == 'preview':
                    if not value.startswith('assets/previews/') or path.suffix.lower() not in ('.jpg', '.png', '.gif', '.webp'): errors.append(f'{prefix}: invalid preview path')
                    if sha256(path.read_bytes()).hexdigest() != r.get('preview_sha256'): errors.append(f'{prefix}: preview checksum mismatch')
                elif key == 'source_snapshot':
                    try:
                        source = json.loads(path.read_text(encoding='utf-8'))
                        if source.get('model') != r.get('model') or source.get('createdAt') != r.get('run_date'):
                            errors.append(f'{prefix}: source snapshot attribution mismatch')
                    except (ValueError, OSError):
                        errors.append(f'{prefix}: invalid source snapshot')
            if not re.fullmatch(r'[0-9a-f]{40}', r.get('source_commit', '')): errors.append(f'{prefix}: missing fixed source commit')
            for key in ('note', 'note_en', 'modifications'):
                if not isinstance(r.get(key), str) or not r[key].strip(): errors.append(f'{prefix}: missing {key}')
    return errors


def group_history(records):
    grouped = defaultdict(list)
    for r in records: grouped[r['case_id']].append(r)
    return grouped


def history_lines(records, language, prefix):
    if not records: return []
    en = language == 'en'
    lines = ['### Historical outputs' if en else '### 历史效果', '']
    for r in records:
        lines.extend([f'**{r["model"]}** · {r["run_period_en" if en else "run_period"]} · {r["publisher"]}', '',
            f'[View output / demo]({r["output_url"]}) · [Source record]({r["source_url"]}) · [Test context]({r["context_url"]})' if en else f'[查看效果 / 体验]({r["output_url"]}) · [来源记录]({r["source_url"]}) · [测试背景]({r["context_url"]})', '', r['conditions_en' if en else 'conditions'], ''])
        if r.get('preview'):
            lines.extend([f'[![{r["model"]} — Pelican SDF]({prefix}{r["preview"]})]({r["output_url"]})', '', r['note_en' if en else 'note'], '',
                f'Preview: {r["publisher"]} · [MIT license]({r["license_url"]}) · [Original image]({r["preview_source_url"]}) · Unmodified upstream thumbnail.' if en else f'图片出处：{r["publisher"]} · [MIT 许可]({r["license_url"]}) · [原图]({r["preview_source_url"]}) · 原项目缩略图，未修改。', ''])
    return lines


def slug(title):
    return re.sub(r'[^\w\u4e00-\u9fff\- ]', '', title.lower()).replace(' ', '-')


def render_history(cases, records, language):
    en = language == 'en'
    base, suffix, prefix = (Path('docs/en'), '_en', '../../') if en else (Path('docs'), '', '../')
    grouped = group_history(records)
    lines = ['# Historical outputs' if en else '# 历史效果档案', '',
        '[简体中文](../HISTORY.md) | **English**' if en else '**简体中文** | [English](en/HISTORY.md)', '',
        '[Home](../../README.en.md) · [All challenges](INDEX.md) · [Preview gallery](GALLERY.md)' if en else '[首页](../README.md) · [全部案例](INDEX.md) · [精选预览](GALLERY.md)', '',
        f'> {len(records)} records covering {len(grouped)} challenges. Source-reported historical outputs, not our reproductions or a ranking.' if en else f'> {len(records)} 条效果记录，覆盖 {len(grouped)} 道题。这里记录来源方的历史输出，不代表本库复现或模型排名。', '',
        'Dates describe runs, not model releases. Publication dates are unknown unless recorded separately. Click a challenge for attribution and conditions.' if en else '日期指运行时间，不是模型发布日期；未单独公开的发布时间不作推测。点击题名查看出处及测试条件。', '',
        '| Challenge | Model | Run period | Output | Source |' if en else '| 案例 | 模型 | 运行时间 | 效果 | 来源 |', '| --- | --- | --- | --- | --- |']
    for c in cases:
        for r in grouped[c['id']]:
            lines.append(f'| [{c["title"+suffix]}](categories/{c["category"]}.md#{slug(c["title"+suffix])}) | {r["model"]} | {r["run_period"+suffix]} | [↗]({r["output_url"]}) | [{r["publisher"]}]({r["source_url"]}) |')
    notice = '[Media credits and corrections](../../THIRD_PARTY_MEDIA.en.md)' if en else '[素材署名与更正说明](../THIRD_PARTY_MEDIA.md)'
    lines.extend(['', notice, ''])
    previews = [r for r in records if r.get('preview')]
    gallery = ['# Selected previews' if en else '# 精选效果预览', '',
        '[简体中文](../GALLERY.md) | **English**' if en else '**简体中文** | [English](en/GALLERY.md)', '',
        '[Home](../../README.en.md) · [History](HISTORY.md)' if en else '[首页](../README.md) · [历史效果档案](HISTORY.md)', '',
        f'> {len(previews)} unchanged upstream thumbnails from one separate 3D SDF task. These are not SVG animation outputs or a ranking.' if en else f'> {len(previews)} 张原项目缩略图，均来自独立的 3D SDF 题，不是 SVG 动画题的结果，也不构成排名。', '',
        'Some frames are cropped or blank and are retained to show limitations. A still cannot verify interaction. Upstream records are marked unverified; we have not reproduced them.' if en else '部分画面有裁切或空白，按原样保留以展示局限。静态图不能验证交互；原项目记录为 unverified，本库未独立复现。', '']
    by_id = {c['id']: c for c in cases}
    for r in previews:
        c = by_id[r['case_id']]
        gallery.extend([f'## {r["model"]}', '', f'[{c["title"+suffix]}](categories/{c["category"]}.md#{slug(c["title"+suffix])})', ''])
        gallery.extend(history_lines([r], language, prefix)[2:])
    gallery.extend([notice, ''])
    return {base/'HISTORY.md': '\n'.join(lines), base/'GALLERY.md': '\n'.join(gallery)}
