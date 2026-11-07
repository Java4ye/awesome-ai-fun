# Contributing

[简体中文](CONTRIBUTING.md) | **English**

Help us collect interesting AI challenges with clear sources and reproducible tasks.

## What belongs here?

- A task that clearly explains what the model should do and what to observe.
- A traceable source, ideally an original post, author website, or repository.
- An unusual or engaging challenge that reveals differences in model behavior.
- A clear note when a prompt is adapted rather than original.

Do not submit unsourced screenshots, promotional articles, unsupported claims of model superiority, or copied videos and generated works.

## Recommend a challenge or website

Open an Issue with its source URL, a brief description, and why it is worth collecting. You can write in Chinese or English without providing a full translation first.

## Submit a pull request

1. Add a record to `data/cases.json`. For a new source, also update `data/sources.json`.
2. Write your own Chinese description in `summary` and observation points in `checks`. Include `title_en`, `summary_en`, `checks_en`, `tags_en`, and `source_credit_en`. Sources need `name_en` and `note_en`. Keep both languages equivalent. Do not copy entire articles or full third-party prompts.
3. Use one existing main type: `svg`, `animation`, `3d`, `games`, or `applications`. Use `tags` and `tags_en` for overlapping abilities. Keep shared IDs, type keys, and source URLs consistent.
4. Validate, regenerate both languages, and run the tests:

```bash
python scripts/validate.py
python scripts/build.py
python scripts/build.py --check
python -m unittest discover -s tests -v
```

5. Submit the JSON and generated pages together. Explain what you added, why it belongs here, its original source, and whether you tested it.

Direct JSON contributions need complete bilingual fields to pass validation. If you need translation help, start with an Issue.

## Be precise about evidence and translations

`collected_not_tested` means the task is indexed but has not been tested by this repository. Do not label entries with unsupported scores or claims of successful testing.

Our descriptions and translations are not original prompts or official scoring rules. If you test a translated or adapted prompt, record its language and version. Request corrections or removal through an Issue.

All third-party materials remain subject to their owners' rights. This repository's license does not automatically license linked works, images, code, or prompts.

## Add historical outputs

Add a record to `data/history.json` linked to a case ID. Record the creator or publisher, model version, run period, source, and output URL. Do not confuse a task's originator with the author of a later reproduction. Leave undisclosed dates and parameters unknown. Prefer source-site playback for videos.

Saved previews also need an original image URL, specific license basis, preserved license, fixed revision, SHA-256, and run-record snapshot. Validate and regenerate both languages. See the [media notice](THIRD_PARTY_MEDIA.en.md). Use media feedback Issues for attribution corrections, broken links, or removal requests.
