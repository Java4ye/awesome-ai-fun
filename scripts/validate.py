#!/usr/bin/env python3
"""Validate the hand-curated source index (Python standard library only)."""
from pathlib import Path
from collections import Counter
from urllib.parse import urlparse
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {"svg", "animation", "3d", "games", "applications"}
REQUIRED = {"id", "title", "category", "summary", "checks", "tags", "source_id", "source_item_no", "source_url", "source_credit", "prompt_status", "status", "verified_on"}
REQUIRED |= {'title_en', 'summary_en', 'checks_en', 'tags_en', 'source_credit_en'}

def check_data(cases, sources):
    errors=[]
    source_ids = {s.get('id') for s in sources}
    counts = Counter()
    case_ids = set()
    source_items = set()
    for idx,c in enumerate(cases,1):
        prefix = f"case #{idx} ({c.get('id', 'no id')})"
        missing = REQUIRED - set(c)
        if missing: errors.append(f"{prefix}: missing fields {sorted(missing)}")
        if not isinstance(c.get('id'),str) or not c.get('id'): errors.append(f"{prefix}: invalid id")
        elif c['id'] in case_ids: errors.append(f"{prefix}: duplicate id")
        else: case_ids.add(c['id'])
        if c.get('category') not in CATEGORIES: errors.append(f"{prefix}: invalid category")
        if c.get('source_id') not in source_ids: errors.append(f"{prefix}: unknown source")
        if not isinstance(c.get('source_item_no'),int) or c['source_item_no'] < 1: errors.append(f"{prefix}: invalid source item number")
        else:
            pair = (c.get('source_id'), c['source_item_no'])
            if pair in source_items: errors.append(f"{prefix}: duplicate source item {pair}")
            source_items.add(pair)
        if not isinstance(c.get('title'), str) or not c['title'].strip(): errors.append(f"{prefix}: empty title")
        if not isinstance(c.get('summary'), str) or not c['summary'].strip(): errors.append(f"{prefix}: empty summary")
        if not isinstance(c.get('checks'), list) or len(c['checks']) < 2: errors.append(f"{prefix}: need two checkpoints")
        if not isinstance(c.get('tags'), list) or not c['tags']: errors.append(f"{prefix}: missing tags")
        for field in ('title_en', 'summary_en', 'source_credit_en'):
            if not isinstance(c.get(field), str) or not c[field].strip(): errors.append(f"{prefix}: empty {field}")
        for field in ('checks_en', 'tags_en'):
            values = c.get(field)
            minimum = 2 if field == 'checks_en' else 1
            if not isinstance(values, list) or len(values) < minimum or any(not isinstance(v, str) or not v.strip() for v in values):
                errors.append(f"{prefix}: invalid {field}")
            elif len(values) != len(c.get(field.removesuffix('_en'), [])):
                errors.append(f"{prefix}: translation count mismatch for {field}")
        url = c.get('source_url','')
        try:
            p = urlparse(url)
            if p.scheme != 'https' or not p.netloc: errors.append(f"{prefix}: invalid source_url")
        except Exception:
            errors.append(f"{prefix}: invalid source_url")
        if c.get('prompt_status') != 'source_only': errors.append(f"{prefix}: prompt should be linked, not copied")
        if c.get('status') != 'collected_not_tested': errors.append(f"{prefix}: no unverified test claims")
        counts[c.get('source_id')]+=1
    for s in sources:
        for field in ('name_en', 'note_en'):
            if not isinstance(s.get(field), str) or not s[field].strip(): errors.append(f"source {s['id']}: empty {field}")
        if counts[s['id']] != s['count']: errors.append(f"source {s['id']}: advertised {s['count']}, actual {counts[s['id']]}")
    return errors

def main():
    cases=json.loads((ROOT/'data/cases.json').read_text(encoding='utf8'))
    sources=json.loads((ROOT/'data/sources.json').read_text(encoding='utf8'))
    errors=check_data(cases,sources)
    if errors:
        print("❌ Catalog validation failed:\n" + "\n".join(f" - {e}" for e in errors))
        return 1
    print(f"✅ {len(cases)} cases, {len(sources)} verified source indexes, no duplicate IDs/source positions")
    return 0
if __name__=='__main__': sys.exit(main())
