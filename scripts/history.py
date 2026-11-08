"""Validate and render attributed historical outputs without executing them."""
from collections import defaultdict
from datetime import date
from hashlib import sha256
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
