# Awesome AI Tests · A collection of fun AI challenges

[简体中文](README.md) | **English**

> A collection of fun, strange, and imaginative challenges to try with AI models.
> Collect interesting tasks first, with clear sources and useful observation points.

**Initial collection: 50 challenges · 2 source websites · 5 types.** See the [full index](docs/en/INDEX.md) for the current list.

**Collection date: 2026-11-07.** Source websites may continue to change.

[Browse all 50 challenges](docs/en/INDEX.md) · [Source directory](docs/en/SOURCES.md) · [How to use](docs/en/GUIDE.md) · [Contribute](CONTRIBUTING.en.md)

## Browse by type

| Type | What to observe | Collection |
| --- | --- | --- |
| SVG Drawing | Complex objects, actions, and relationships | [Browse](docs/en/categories/svg.md) |
| Animation & Physics | Motion, collisions, and visual effects | [Browse](docs/en/categories/animation.md) |
| 3D & Spatial Scenes | Spatial structure, 3D interaction, and scene building | [Browse](docs/en/categories/3d.md) |
| Games | Mechanics, controls, and playability | [Browse](docs/en/categories/games.md) |
| Apps & Interaction | Window management, editor features, and interaction design | [Browse](docs/en/categories/applications.md) |

Types are browsing categories. Use tags to find abilities that span more than one type.

## Start with these eight

| Challenge | What makes it interesting? | Original source |
| --- | --- | --- |
| Octopus playing a pipe organ | Do the tentacles actually appear to play? | [Gally, item 1](https://gally.net/temp/20260914pelican-alternatives/index.html) |
| Giraffe assembling a grandfather clock | Can a long-necked animal handle delicate machinery? | [Gally, item 2](https://gally.net/temp/20260914pelican-alternatives/index.html) |
| Pelican riding a bicycle | Can pedals, legs, and wheels move together? | [AI Test Museum](https://aitestmuseum.com/zh/tests/pelican-bicycle) |
| Bouncing ball in a hexagon | How do rotating walls affect a rebound? | [AI Test Museum](https://aitestmuseum.com/zh/tests/bouncing-ball-hexagon) |
| Self-solving Rubik's cube | Can the model restore the cube after scrambling? | [AI Test Museum](https://aitestmuseum.com/zh/tests/rubiks-cube) |
| Browser Minecraft | How much of a playable block world can one attempt produce? | [AI Test Museum](https://aitestmuseum.com/zh/tests/minecraft-web) |
| Kart racing game | Can the track, opponents, and controls work together? | [AI Test Museum](https://aitestmuseum.com/zh/tests/kart-racer) |
| Single-file web desktop | Does it work as well as it looks? | [AI Test Museum](https://aitestmuseum.com/zh/tests/web-os-desktop) |

## Source websites

- [Pelican-bicycle alternatives](https://gally.net/temp/20260914pelican-alternatives/index.html): 30 imaginative SVG drawing tasks involving living things, machinery, and unexpected actions. The source compares model-generated outputs.
- [AI Test Museum](https://aitestmuseum.com/zh): 20 classic coding and visual challenges covering animation, 3D, games, and applications, with prompts and runnable outputs.

See the [source directory](docs/en/SOURCES.md) for attribution and context. Source links retain their original URLs; some pages are in Chinese.

## How to try a challenge

1. Pick a task from the [index](docs/en/INDEX.md).
2. Open the source to read the actual prompt and instructions. Our summaries and translations are editorial descriptions, not original prompts.
3. Run it with your own model. Record the model version, tool, date, prompt language, and any changes to the prompt.
4. Use the observation points to distinguish whether the result runs, works correctly, looks good, and feels usable.

This repository is a **curated source index**. We have not run these 50 challenges ourselves. Results from different models and environments on the source websites do not form a standardized leaderboard. See the [testing guide](docs/en/GUIDE.md).

## Repository structure

```text
awesome-ai-tests/
├── README.md / README.en.md       # Homepages
├── data/
│   ├── cases.json                 # Shared bilingual challenge metadata
│   └── sources.json               # Shared source metadata
├── docs/
│   ├── INDEX.md                   # Generated Chinese index
│   ├── categories/                # Generated Chinese details
│   ├── SOURCES.md / GUIDE.md      # Chinese source directory and guide
│   └── en/                       # English index, details, sources, and guide
├── scripts/                       # Validation and Markdown generation
├── tests/                         # Catalog tests
├── .github/                       # CI and contribution issue templates
├── CONTRIBUTING.md / CONTRIBUTING.en.md
├── CHANGELOG.md / CHANGELOG.en.md
└── LICENSE
```

Local maintenance requires Python 3.10+ and no third-party dependencies:

```bash
python scripts/validate.py
python scripts/build.py
python scripts/build.py --check
python -m unittest discover -s tests -v
```

Edit the shared JSON, then rebuild both languages. Changes made directly to generated Markdown will be overwritten.

## Contributions

Recommend an interesting task, correct an attribution, or improve a translation through Issues or pull requests. Chinese and English contributions are welcome. See the [contribution guide](CONTRIBUTING.en.md).

We value clear sources, understandable tasks, and reproducible setups. Do not invent popularity or test results, or copy third-party works and long passages.

## Copyright and thanks

We provide our own Chinese and English descriptions, observation points, and source index. Original prompts, websites, SVGs, model outputs, and other third-party materials remain subject to their owners' rights and licenses. **The MIT license covers only this repository's original content and code. It grants no rights to third-party material.**

Thanks to [Tom Gally](https://gally.net/temp/20260914pelican-alternatives/index.html) and [AI Test Museum](https://aitestmuseum.com/zh). Visit their sites for full prompts and outputs. This repository is not officially affiliated with those projects.
