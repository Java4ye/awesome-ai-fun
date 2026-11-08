# Repository maintenance

[简体中文](../MAINTENANCE.md) | **English**

[Home](../../README.md) · [Submissions and feedback](https://github.com/Java4ye/awesome-ai-fun/issues/new/choose)

Collect submissions through Issues. Before adding a work, check for duplicates and distinguish the original creator from a republisher. Leave undisclosed models, run dates, and conditions unknown, and keep the two languages equivalent.

## Editing sources

- `data/cases.json`: bilingual titles, descriptions, categories and observation points.
- `data/sources.json`: source directory.
- `data/history.json`: source-reported historical outputs, models, conditions and licensed local previews.
- `data/showcase.json`: per-case source images, video posters and historical captures, distinguishing open licenses from unverified source references.
- `data/research.json`: community source and verification records for catalog entries. Keep unreviewed leads outside the repository.

The README, work index, and gallery share the same list of works and collections. Each collection has one index entry and lists its individual works below the main index. Prompt-only entries appear separately in the gallery's prompt library. Open `site/index.html` to browse locally. Define collections in `WORK_GROUPS` and keep existing case IDs stable. The playable filter lists works with interactive destinations.

The build also writes `site/catalog.js`. Pushes to `main` validate the catalog and deploy the gallery and its covers to [GitHub Pages](https://java4ye.github.io/awesome-ai-fun/site/). The website uses the same catalog data as the README.

The gallery shows all works by category in English by default. Chinese uses the same layout. Covers keep their aspect ratio and load lazily. Readers can play videos after opening a work.

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

`history.py` checks existing thumbnails and source snapshots. `showcase.py` checks new capture paths, dates, SHA-256 hashes, and external URL fields. Source references must retain `license_status: not_verified` rather than implying permission. See the [media notice](THIRD_PARTY_MEDIA.md).
