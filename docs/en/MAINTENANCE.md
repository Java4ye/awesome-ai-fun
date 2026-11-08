# Repository maintenance

[简体中文](../MAINTENANCE.md) | **English**

[Home](../../README.en.md) · [Contribution guide](../../CONTRIBUTING.en.md)

## Editing sources

- `data/cases.json`: bilingual titles, descriptions, categories and observation points.
- `data/sources.json`: source directory.
- `data/history.json`: source-reported historical outputs, models, conditions and licensed local previews.
- `data/showcase.json`: representative homepage previews, referencing historical records or pinned upstream screenshots with licenses.
- `data/research.json`: community source records and research leads.

The homepage, categories and gallery share preview data. Illustrated cases are expanded; cases without previews are retained in a collapsible section at the end of each category. Adding a preview and rebuilding moves a case to the expanded section without counting it twice.

Python 3.10+, no third-party dependencies:

```bash
python scripts/validate.py
python scripts/build.py
python scripts/build.py --check
python -m unittest discover -s tests -v
```

Do not edit generated READMEs, categories, indexes or gallery pages directly. The project introduction is defined in `INTRO` in `scripts/showcase.py`; change it only when explicitly requested.

## Adding an image or animation

Use an actual output for the corresponding case. Preserve author, model, image source, pinned revision and license. Images and GIFs display inline; full videos link to original playback pages. Cases without media stay pending, without unrelated illustrations or blank placeholder images.

Local preview checksums and historical snapshots are still checked by `history.py`. Remote screenshots use pinned commits. See the [media notice](../../THIRD_PARTY_MEDIA.en.md).
