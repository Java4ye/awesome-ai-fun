# Usage, data format, and roadmap

[简体中文](../GUIDE.md) | **English**

[← Home](../../README.en.md)

## Why link to prompts instead of copying them?

This is a curated collection intended for continued maintenance. It helps you find a task, understand what it tests, and return to the source for the actual prompt. Sources may change their prompts or execution instructions. Copies can become outdated, and third-party licenses may not allow bulk republication.

## How to test a model

1. Choose a challenge from the [index](INDEX.md) and read the full source instructions.
2. Record `prompt_version`: original, translated, or adapted. Save your own prompt if you changed it, and record its language.
3. Record the model version, tool or client, date, network access, agent mode, and retry allowance.
4. Save your own code, screenshots, and execution instructions. Do not present them as outputs from the source site.
5. Assess correctness, whether it runs, visual quality, and interaction separately. Avoid ranking results obtained under different conditions as if they were directly comparable.

The following is a format example, **not a real test result**:

```yaml
case_id: museum-002
model: "actual model version"
client: "client or API"
date: "YYYY-MM-DD"
prompt_version: "original / translated / adapted"
prompt_language: "actual language used"
agent_mode: false
retries: 0
runs: "your saved code or link"
notes: "observations about collisions, wall penetration, frame rate, etc."
```

## Shared bilingual data

Edit `data/cases.json` for challenges and `data/sources.json` for websites. Both languages share the same IDs, source URLs, item numbers, and type keys.

| Field | Meaning |
| --- | --- |
| `id` | Stable challenge ID; keep it when changing a title |
| `title` / `title_en` | Required Chinese and English titles |
| `category` | `svg`, `animation`, `3d`, `games`, or `applications` |
| `summary` / `summary_en` | Our Chinese and English summaries, not full original prompts |
| `checks` / `checks_en` | Corresponding editorial observation points, not official scoring rules |
| `tags` / `tags_en` | Corresponding tags for abilities spanning multiple types |
| `source_id` | Source website ID: currently `gally` or `museum` |
| `source_item_no` | Item number on the source site |
| `source_url` | Original source URL, shared by both languages |
| `source_credit` / `source_credit_en` | Attribution leads as listed by the source; not necessarily the earliest author |
| `prompt_status` | `source_only`: read the prompt at its source |
| `status` | `collected_not_tested`: not tested by this repository |
| `verified_on` | Date the index information was checked, not the task publication date |

In `sources.json`, `name_en` and `note_en` correspond to the Chinese source name and note. English observation points and tags must have the same number of entries as their Chinese counterparts.

Types are browsing categories rather than mutually exclusive abilities. Choose one primary type and use tags for overlap. A translated prompt can affect model behavior; record its language and version when testing.

## Local maintenance

Python 3.10+ is required. No third-party dependencies are needed.

```bash
python scripts/validate.py
python scripts/build.py
python scripts/build.py --check
python -m unittest discover -s tests -v
```

Rebuild after editing JSON. The generator writes the Chinese index and five category pages, plus their English counterparts under `docs/en/`: 12 pages in total. Edit the JSON rather than generated Markdown.

CI checks the data and generated pages for consistency. Local validation does not contact every external URL; links may become unavailable later. Report broken sources through Issues.

## Roadmap: not implemented yet

- Add more traceable source websites and genuinely new challenges.
- Trace classic tasks to earlier sources and document prompt versions.
- Add contributors' own test results with the necessary execution context.
- Consider GitHub Pages search and filtering if the collection grows substantially.

This version has no automatic model calls, scoring, online previews, or leaderboard.
