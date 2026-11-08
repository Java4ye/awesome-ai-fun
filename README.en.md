# Awesome AI Tests · A collection of fun AI challenges

[简体中文](README.md) | **English**

> A collection of fun, strange, and imaginative challenges to try with AI models.
> Collect interesting tasks first, with clear sources and useful observation points.

## Categories

[Games (14)](#category-games) · [3D & Spatial Scenes (16)](#category-3d) · [Apps & Interaction (12)](#category-applications) · [Animation & Physics (31)](#category-animation) · [SVG Drawing (32)](#category-svg)

**105 cases** · 3 with inline previews · 102 awaiting previews.

<a id="category-games"></a>

## Games · 14

[↑ Categories](#categories)

<a id="case-x-dangreenheck-2103004432786993341"></a>

### Coastal fishing and trading game

[![Coastal fishing and trading game — Claude Opus 5.5（作者报告 / creator-reported）](https://raw.githubusercontent.com/dgreenheck/tidewater/4811ba48d795197de5621985f404e765c0b7c0ef/docs/screenshot.jpg)](https://dgreenheck.github.io/tidewater/)

Observe: Fishing, selling and equipment purchases form a working loop / Saving and restart preserve sensible state。

**Model:** Claude Opus 5.5（作者报告 / creator-reported） · **Author / publisher:** Dan Greenheck / DRG Software Solutions LLC

Image: Dan Greenheck / DRG Software Solutions LLC · [Original image](https://github.com/dgreenheck/tidewater/blob/4811ba48d795197de5621985f404e765c0b7c0ef/docs/screenshot.jpg) · [MIT license](assets/licenses/tidewater-MIT.txt)

Original project screenshot; an iterative work. Playing requires WebGPU.

[Original source](https://x.com/dangreenheck/status/2103004432786993341) · [Open work](https://dgreenheck.github.io/tidewater/) · [Details](docs/en/categories/games.md#coastal-fishing-and-trading-game) · [▶ Creator video](https://x.com/dangreenheck/status/2103004432786993341)

---

<details>
<summary>Awaiting previews · 13 cases</summary>

Real, reusable previews are still missing. Source output links are retained below; they are not inline previews.

| Case | What to try | Source / output |
| --- | --- | --- |
| <a id="case-museum-006"></a>[One-shot kart racing game](docs/en/categories/games.md#one-shot-kart-racing-game) | Use a short request to generate a single-file 3D kart racing game. | [Source](https://aitestmuseum.com/zh/tests/kart-racer) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/kart-racer/output.html) |
| <a id="case-museum-009"></a>[Flappy Bird in one file](docs/en/categories/games.md#flappy-bird-in-one-file) | Create a playable Flappy Bird-style game in a single web page. | [Source](https://aitestmuseum.com/zh/tests/flappy-bird) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/flappy-bird/output.html) |
| <a id="case-museum-010"></a>[Tetris in one file](docs/en/categories/games.md#tetris-in-one-file) | Generate a Tetris game with rotation, line clearing, and level progression. | [Source](https://aitestmuseum.com/zh/tests/tetris) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/tetris/output.html) |
| <a id="case-museum-015"></a>[3D flight game among skyscrapers](docs/en/categories/games.md#3d-flight-game-among-skyscrapers) | Generate a browser flight game through skyscrapers from a short instruction. | [Source](https://aitestmuseum.com/zh/tests/flight-sim) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/flight-sim/output.html) |
| <a id="case-stock42-tetris-3d"></a>[3D-style Tetris with sound and scores](docs/en/categories/games.md#3d-style-tetris-with-sound-and-scores) | Combine projected visuals, falling-block rules, audio and persistent scores in one file. | [Source](https://github.com/stock42/test-llm-coding/blob/5dd2e8e63f026337ddfa39195d7f1008806bca1d/promptings/tetris-3d.md) · [↗](https://github.com/stock42/test-llm-coding/blob/5dd2e8e63f026337ddfa39195d7f1008806bca1d/codex/gpt-5.5/tetris-3d/index.html) |
| <a id="case-psydox-01"></a>[Single-file raycasting FPS](docs/en/categories/games.md#single-file-raycasting-fps) | Build a constrained first-person map with enemies and shooting. | [Source](https://github.com/psydox/Local-LLM-Coding-Benchmark/blob/061dec9d8918b0b1d302678e070247f866471fa9/01_Browser_FPS_Raycasting_Game_Test.txt) |
| <a id="case-psydox-03"></a>[Memory matching with best scores](docs/en/categories/games.md#memory-matching-with-best-scores) | Test shuffling, card states and saved best scores. | [Source](https://github.com/psydox/Local-LLM-Coding-Benchmark/blob/061dec9d8918b0b1d302678e070247f866471fa9/03_Memory_Card_Matching_Game_Test.txt) |
| <a id="case-psydox-04"></a>[Canvas Breakout](docs/en/categories/games.md#canvas-breakout) | Implement paddle control, bricks, lives and end states. | [Source](https://github.com/psydox/Local-LLM-Coding-Benchmark/blob/061dec9d8918b0b1d302678e070247f866471fa9/04_Breakout_Canvas_Game_Test.txt) |
| <a id="case-psydox-06"></a>[Top-down 2D driving game](docs/en/categories/games.md#top-down-2d-driving-game) | Handle controls, obstacles and completion on a scrolling track. | [Source](https://github.com/psydox/Local-LLM-Coding-Benchmark/blob/061dec9d8918b0b1d302678e070247f866471fa9/06_Top_Down_2D_Driving_Game_Test.txt) |
| <a id="case-google-studio-neon_arena_laser_tag"></a>[Neon Arena multiplayer laser tag](docs/en/categories/games.md#neon-arena-multiplayer-laser-tag) | Combine multiplayer sessions, bot opponents and timed scores. | [Source](https://blog.google/innovation-and-ai/technology/developers-tools/full-stack-vibe-coding-google-ai-studio/) · [↗](https://aistudio.google.com/apps/bundled/neon_arena_laser_tag) |
| <a id="case-google-studio-neon_claw"></a>[Neon Claw physics claw machine](docs/en/categories/games.md#neon-claw-physics-claw-machine) | Combine claw controls, collisions, a timer and scores in 3D. | [Source](https://blog.google/innovation-and-ai/technology/developers-tools/full-stack-vibe-coding-google-ai-studio/) · [↗](https://aistudio.google.com/apps/bundled/neon_claw) |
| <a id="case-x-nachat_dayo-2102773498037023140"></a>[Harpoon fishing game](docs/en/categories/games.md#harpoon-fishing-game) | Observe: Hit detection and scoring agree | [Source](https://x.com/nachat_dayo/status/2102773498037023140) |
| <a id="case-x-oguzthedev-2102476490344730950"></a>[Flower planting and beekeeping game](docs/en/categories/games.md#flower-planting-and-beekeeping-game) | Observe: Flowers, bees and hives interact | [Source](https://x.com/oguzthedev/status/2102476490344730950) |

</details>

<a id="category-3d"></a>

## 3D & Spatial Scenes · 16

[↑ Categories](#categories)

<a id="case-pelican-sdf-001"></a>

### Interactive 3D pelican on a bicycle with SDFs

[![Interactive 3D pelican on a bicycle with SDFs — google/gemini-3.1-pro-preview](assets/previews/pelican-sdf/gemini-3-1-pro-high-run-01.jpg)](https://pelican.vibe-overflow.com/result.html?id=gemini-3-1-pro-high-run-01)

Build a 3D pelican-on-a-bicycle scene with signed distance fields, ray marching, materials, and camera controls. This is a separate 3D extension, not an output for the SVG animation task.

**Model:** google/gemini-3.1-pro-preview · **Author / publisher:** AzatJalilov / Pelican SDF contributors

Image: AzatJalilov / Pelican SDF contributors · [Original image](https://raw.githubusercontent.com/AzatJalilov/PelicanSdf/63190d7e5fb883175b8612374de5e7f094293548/assets/thumbnails/gemini-3-1-pro-high-run-01.jpg) · [MIT license](assets/licenses/pelican-sdf-MIT.txt)

[Source run record](https://github.com/AzatJalilov/PelicanSdf/blob/63190d7e5fb883175b8612374de5e7f094293548/data/results/gemini-3-1-pro-high-run-01.json)

Source-reported run date: 2026-07-18

The bird and bicycle are recognizable; inspect the original for the full interaction requirements.

[Original source](https://github.com/AzatJalilov/PelicanSdf/blob/63190d7e5fb883175b8612374de5e7f094293548/benchmark/prompt.txt) · [Open work](https://pelican.vibe-overflow.com/result.html?id=gemini-3-1-pro-high-run-01) · [Details](docs/en/categories/3d.md#interactive-3d-pelican-on-a-bicycle-with-sdfs)

<details>
<summary>More model outputs</summary>

[![Interactive 3D pelican on a bicycle with SDFs — gpt-5.5](assets/previews/pelican-sdf/gpt-5-5-run-01.jpg)](https://pelican.vibe-overflow.com/result.html?id=gpt-5-5-run-01)

**Model:** gpt-5.5 · **Author / publisher:** AzatJalilov / Pelican SDF contributors

Image: AzatJalilov / Pelican SDF contributors · [Original image](https://raw.githubusercontent.com/AzatJalilov/PelicanSdf/63190d7e5fb883175b8612374de5e7f094293548/assets/thumbnails/gpt-5-5-run-01.jpg) · [MIT license](assets/licenses/pelican-sdf-MIT.txt)

[Source run record](https://github.com/AzatJalilov/PelicanSdf/blob/63190d7e5fb883175b8612374de5e7f094293548/data/results/gpt-5-5-run-01.json)

Source-reported run date: 2026-07-18

Most of the subject lies outside the thumbnail; this framing issue is preserved.

[![Interactive 3D pelican on a bicycle with SDFs — claude-haiku-4-5-20251001](assets/previews/pelican-sdf/claude-haiku-4-5-high-run-01.jpg)](https://pelican.vibe-overflow.com/result.html?id=claude-haiku-4-5-high-run-01)

**Model:** claude-haiku-4-5-20251001 · **Author / publisher:** AzatJalilov / Pelican SDF contributors

Image: AzatJalilov / Pelican SDF contributors · [Original image](https://raw.githubusercontent.com/AzatJalilov/PelicanSdf/63190d7e5fb883175b8612374de5e7f094293548/assets/thumbnails/claude-haiku-4-5-high-run-01.jpg) · [MIT license](assets/licenses/pelican-sdf-MIT.txt)

[Source run record](https://github.com/AzatJalilov/PelicanSdf/blob/63190d7e5fb883175b8612374de5e7f094293548/data/results/claude-haiku-4-5-high-run-01.json)

Source-reported run date: 2026-07-18

The subject is cropped at the top; this still does not establish correct interaction or bicycle structure.

[![Interactive 3D pelican on a bicycle with SDFs — deepseek/deepseek-v4-pro](assets/previews/pelican-sdf/deepseek-v4-pro-high-run-01.jpg)](https://pelican.vibe-overflow.com/result.html?id=deepseek-v4-pro-high-run-01)

**Model:** deepseek/deepseek-v4-pro · **Author / publisher:** AzatJalilov / Pelican SDF contributors

Image: AzatJalilov / Pelican SDF contributors · [Original image](https://raw.githubusercontent.com/AzatJalilov/PelicanSdf/63190d7e5fb883175b8612374de5e7f094293548/assets/thumbnails/deepseek-v4-pro-high-run-01.jpg) · [MIT license](assets/licenses/pelican-sdf-MIT.txt)

[Source run record](https://github.com/AzatJalilov/PelicanSdf/blob/63190d7e5fb883175b8612374de5e7f094293548/data/results/deepseek-v4-pro-high-run-01.json)

Source-reported run date: 2026-07-18

The upstream thumbnail is a flat-colored frame and is retained unchanged; other views are not inferred.

[![Interactive 3D pelican on a bicycle with SDFs — z-ai/glm-5.2](assets/previews/pelican-sdf/glm-5-2-high-run-01.jpg)](https://pelican.vibe-overflow.com/result.html?id=glm-5-2-high-run-01)

**Model:** z-ai/glm-5.2 · **Author / publisher:** AzatJalilov / Pelican SDF contributors

Image: AzatJalilov / Pelican SDF contributors · [Original image](https://raw.githubusercontent.com/AzatJalilov/PelicanSdf/63190d7e5fb883175b8612374de5e7f094293548/assets/thumbnails/glm-5-2-high-run-01.jpg) · [MIT license](assets/licenses/pelican-sdf-MIT.txt)

[Source run record](https://github.com/AzatJalilov/PelicanSdf/blob/63190d7e5fb883175b8612374de5e7f094293548/data/results/glm-5-2-high-run-01.json)

Source-reported run date: 2026-07-18

The scene and bicycle outline are visible; a still cannot establish whether controls work.

</details>

---

<details>
<summary>Awaiting previews · 15 cases</summary>

Real, reusable previews are still missing. Source output links are retained below; they are not inline previews.

| Case | What to try | Source / output |
| --- | --- | --- |
| <a id="case-museum-003"></a>[Voxel pagoda garden](docs/en/categories/3d.md#voxel-pagoda-garden) | Build a colorful voxel pagoda garden with cherry trees from a text description. | [Source](https://aitestmuseum.com/zh/tests/voxel-pagoda) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/voxel-pagoda/output.html) |
| <a id="case-museum-004"></a>[Minecraft in three.js](docs/en/categories/3d.md#minecraft-in-threejs) | Try generating a simplified browser-based Minecraft with a block world in one attempt. | [Source](https://aitestmuseum.com/zh/tests/minecraft-web) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/minecraft-web/output.html) |
| <a id="case-museum-005"></a>[Self-solving Rubik's cube](docs/en/categories/3d.md#self-solving-rubiks-cube) | Build a 3D Rubik's cube that supports scrambling, stepwise turns, and automatic restoration. | [Source](https://aitestmuseum.com/zh/tests/rubiks-cube) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/rubiks-cube/output.html) |
| <a id="case-museum-007"></a>[Meteor hitting a city](docs/en/categories/3d.md#meteor-hitting-a-city) | Generate a browser demo showing a falling meteor, a shock wave, and changes to a city. | [Source](https://aitestmuseum.com/zh/tests/meteor-city) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/meteor-city/output.html) |
| <a id="case-museum-011"></a>[Solar system simulation](docs/en/categories/3d.md#solar-system-simulation) | Use browser animation to show the relationships between the Sun and orbiting planets. | [Source](https://aitestmuseum.com/zh/tests/solar-system) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/solar-system/output.html) |
| <a id="case-museum-020"></a>[Earth-Mars round trip](docs/en/categories/3d.md#earth-mars-round-trip) | Use three.js to animate a trip from Earth to Mars and a return timed to a launch window. | [Source](https://aitestmuseum.com/zh/tests/mars-round-trip) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/mars-round-trip/output.html) |
| <a id="case-electricazimuth-lightshow"></a>[Ray-marched psychedelic metaballs](docs/en/categories/3d.md#ray-marched-psychedelic-metaballs) | Use WebGL and SDF ray marching to show smoothly merging spheres. | [Source](https://github.com/electricazimuth/LocalLLM_VisualCodeTest/blob/7e7004885221fafb8b1de360cacc2b8281cf934a/code_prompts/lightshow.md) · [↗](https://electricazimuth.github.io/LocalLLM_VisualCodeTest/results/2025.04.28/html/GLM-4-32B-0414-F16-Q4_K_M_lightshow_20250425_174301.html) |
| <a id="case-psydox-09"></a>[Python software-rendered 3D game](docs/en/categories/3d.md#python-software-rendered-3d-game) | Implement 3D projection and game states without a graphics engine. | [Source](https://github.com/psydox/Local-LLM-Coding-Benchmark/blob/061dec9d8918b0b1d302678e070247f866471fa9/09_Python_Software_Rendered_3D_Game_Test.txt) |
| <a id="case-reddit-doner-doner"></a>[Rotating doner skewer and gas heater](docs/en/categories/3d.md#rotating-doner-skewer-and-gas-heater) | Render a rotating skewer, heat source and depth in Canvas without external libraries. | [Source](https://www.reddit.com/r/LocalLLaMA/comments/1ua1na0/whats_more_impressive_glm_51_52_or_qwen_35_36/) |
| <a id="case-reddit-thriller-thriller"></a>[Synchronized multi-character Three.js dance](docs/en/categories/3d.md#synchronized-multi-character-threejs-dance) | Combine multiple characters, choreography, lighting and camera work; the source names the requested cast. | [Source](https://www.reddit.com/r/LocalLLaMA/comments/1rqlaw4/new_benchmark_just_dropped/) |
| <a id="case-x-dotey-2102940980379017293"></a>[Explorable Peach Blossom Land](docs/en/categories/3d.md#explorable-peach-blossom-land) | Observe: Text navigation corresponds to scene positions | [Source](https://x.com/dotey/status/2102940980379017293) |
| <a id="case-x-ishuagra02-2102543638689460488"></a>[Photo-to-cel-shaded autumn railway](docs/en/categories/3d.md#photo-to-cel-shaded-autumn-railway) | Observe: Composition corresponds to the reference photo | [Source](https://x.com/ishuagra02/status/2102543638689460488) |
| <a id="case-x-superalesha-2102779758408774104"></a>[From accelerator tunnel to proton collision](docs/en/categories/3d.md#from-accelerator-tunnel-to-proton-collision) | Observe: Tunnel, detector and camera are spatially coherent | [Source](https://x.com/superalesha/status/2102779758408774104) |
| <a id="case-x-techartist_-2102503719762018434"></a>[From line sketch to 3D house](docs/en/categories/3d.md#from-line-sketch-to-3d-house) | Observe: Sketch, massing and detail connect continuously | [Source](https://x.com/techartist_/status/2102503719762018434) |
| <a id="case-x-studio_veco-2102684366996738511"></a>[Word-driven soft-colored village](docs/en/categories/3d.md#word-driven-soft-colored-village) | Observe: Input has a meaningful scene response | [Source](https://x.com/studio_veco/status/2102684366996738511) |

</details>

<a id="category-applications"></a>

## Apps & Interaction · 12

[↑ Categories](#categories)

<a id="case-between-tokens-interactive-story"></a>

### An interactive story where you are the model

[![An interactive story where you are the model — Claude Fable 5（仓库署名 / repository credit）](https://raw.githubusercontent.com/chrisjz/between-tokens/93561477667dfc27df77f451e747353a15654f46/assets/screenshot.png)](https://chrisjz.github.io/between-tokens/)

Let the reader choose candidate replies while exploring temperature, fading context and branching narrative.

**Model:** Claude Fable 5（仓库署名 / repository credit） · **Author / publisher:** Chris Zaharia

Image: Chris Zaharia · [Original image](https://github.com/chrisjz/between-tokens/blob/93561477667dfc27df77f451e747353a15654f46/assets/screenshot.png) · [MIT license](assets/licenses/between-tokens-MIT.txt)

Original project screenshot; candidate text is authored and probabilities are computed.

[Original source](https://news.ycombinator.com/item?id=49311484) · [Open work](https://chrisjz.github.io/between-tokens/) · [Details](docs/en/categories/applications.md#an-interactive-story-where-you-are-the-model)

---

<details>
<summary>Awaiting previews · 11 cases</summary>

Real, reusable previews are still missing. Source output links are retained below; they are not inline previews.

| Case | What to try | Source / output |
| --- | --- | --- |
| <a id="case-museum-012"></a>[An operating system in one HTML file](docs/en/categories/applications.md#an-operating-system-in-one-html-file) | Build a desktop with windows and multiple applications in a single HTML page. | [Source](https://aitestmuseum.com/zh/tests/web-os-desktop) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/web-os-desktop/output.html) |
| <a id="case-museum-014"></a>[Brick builder](docs/en/categories/applications.md#brick-builder) | Create a 3D editor for placing, rotating, recoloring, and deleting bricks. | [Source](https://aitestmuseum.com/zh/tests/brick-builder) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/brick-builder/output.html) |
| <a id="case-psydox-05"></a>[Persistent personal expense tracker](docs/en/categories/applications.md#persistent-personal-expense-tracker) | Implement expense CRUD, filters, summaries and reload persistence. | [Source](https://github.com/psydox/Local-LLM-Coding-Benchmark/blob/061dec9d8918b0b1d302678e070247f866471fa9/05_Personal_Expense_Tracker_App_Test.txt) |
| <a id="case-psydox-07"></a>[Drag-and-drop Kanban board](docs/en/categories/applications.md#drag-and-drop-kanban-board) | Combine task and column management, archive restore, filters and persistence. | [Source](https://github.com/psydox/Local-LLM-Coding-Benchmark/blob/061dec9d8918b0b1d302678e070247f866471fa9/07_Kanban_Board_App_Test.txt) |
| <a id="case-psydox-08"></a>[Python standard-library layered editor](docs/en/categories/applications.md#python-standard-library-layered-editor) | Use Tkinter and a custom raster model for tools, layers, filters and undo. | [Source](https://github.com/psydox/Local-LLM-Coding-Benchmark/blob/061dec9d8918b0b1d302678e070247f866471fa9/08_Python_GUI_Photoshop_Clone_Test.txt) |
| <a id="case-google-studio-cosmic_flow"></a>[Cosmic Flow shared particles](docs/en/categories/applications.md#cosmic-flow-shared-particles) | Multiple users spawn particles with cursors in a shared 3D space. | [Source](https://blog.google/innovation-and-ai/technology/developers-tools/full-stack-vibe-coding-google-ai-studio/) · [↗](https://aistudio.google.com/apps/bundled/cosmic_flow) |
| <a id="case-google-studio-geoseeker"></a>[GeoSeeker map interaction app](docs/en/categories/applications.md#geoseeker-map-interaction-app) | Use the official map app to explore interaction with external data. | [Source](https://blog.google/innovation-and-ai/technology/developers-tools/full-stack-vibe-coding-google-ai-studio/) · [↗](https://aistudio.google.com/apps/bundled/geoseeker) |
| <a id="case-google-studio-heirloom_recipes"></a>[Heirloom Recipes collaborative cookbook](docs/en/categories/applications.md#heirloom-recipes-collaborative-cookbook) | Organize, import and generate recipes with family collaboration. | [Source](https://blog.google/innovation-and-ai/technology/developers-tools/full-stack-vibe-coding-google-ai-studio/) · [↗](https://aistudio.google.com/apps/bundled/heirloom_recipes) |
| <a id="case-x-petergyang-2102849349122470205"></a>[Upload a photo and watch it painted](docs/en/categories/applications.md#upload-a-photo-and-watch-it-painted) | Observe: The uploaded image affects the painting | [Source](https://x.com/petergyang/status/2102849349122470205) |
| <a id="case-x-ryansael-2102591147927654847"></a>[Interactive focus and aperture lab](docs/en/categories/applications.md#interactive-focus-and-aperture-lab) | Observe: Ray paths correspond to the focus plane | [Source](https://x.com/RyanSael/status/2102591147927654847) |
| <a id="case-x-scheemunai-2103059885361598633"></a>[Bedroom bed-placement planner](docs/en/categories/applications.md#bedroom-bed-placement-planner) | Observe: Floor plan and 3D positions agree | [Source](https://x.com/scheemunai/status/2103059885361598633) |

</details>

<a id="category-animation"></a>

## Animation & Physics · 31

[↑ Categories](#categories)

<details>
<summary>Awaiting previews · 31 cases</summary>

Real, reusable previews are still missing. Source output links are retained below; they are not inline previews.

| Case | What to try | Source / output |
| --- | --- | --- |
| <a id="case-museum-001"></a>[Pelican riding a bicycle](docs/en/categories/animation.md#pelican-riding-a-bicycle) | Generate an SVG animation of a pelican riding a bicycle, rather than a static drawing. | [Source](https://aitestmuseum.com/zh/tests/pelican-bicycle) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/pelican-bicycle/output.html) |
| <a id="case-museum-002"></a>[Bouncing ball inside a spinning hexagon](docs/en/categories/animation.md#bouncing-ball-inside-a-spinning-hexagon) | Animate a ball bouncing inside a continuously rotating hexagon under gravity and friction. | [Source](https://aitestmuseum.com/zh/tests/bouncing-ball-hexagon) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/bouncing-ball-hexagon/output.html) |
| <a id="case-museum-008"></a>[Supernova explosion](docs/en/categories/animation.md#supernova-explosion) | Animate a star's evolution into a supernova and its remnant. | [Source](https://aitestmuseum.com/zh/tests/supernova) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/supernova/output.html) |
| <a id="case-museum-013"></a>[Drowned Gothic city shader](docs/en/categories/animation.md#drowned-gothic-city-shader) | Use a shader to draw a partially submerged Gothic city in a storm. | [Source](https://aitestmuseum.com/zh/tests/drowned-gothic-city) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/drowned-gothic-city/output.html) |
| <a id="case-museum-016"></a>[Hand-controlled particles](docs/en/categories/animation.md#hand-controlled-particles) | Use webcam hand gestures to change the shapes of Three.js particles. | [Source](https://aitestmuseum.com/zh/tests/hand-gesture-particles) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/hand-gesture-particles/output.html) |
| <a id="case-museum-017"></a>[Bouncing ball inside a hypercube](docs/en/categories/animation.md#bouncing-ball-inside-a-hypercube) | Animate a bouncing ball inside a rotating four-dimensional hypercube. | [Source](https://aitestmuseum.com/zh/tests/tesseract-ball) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/tesseract-ball/output.html) |
| <a id="case-museum-018"></a>[Starship control panel](docs/en/categories/animation.md#starship-control-panel) | Use p5.js to generate an imaginative futuristic starship control panel. | [Source](https://aitestmuseum.com/zh/tests/starship-control-panel) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/starship-control-panel/output.html) |
| <a id="case-museum-019"></a>[Analog clock showing 10:10](docs/en/categories/animation.md#analog-clock-showing-1010) | Draw an HTML/CSS clock showing 10:10 with a continuously moving second hand. | [Source](https://aitestmuseum.com/zh/tests/ai-world-clock) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/ai-world-clock/output.html) |
| <a id="case-electricazimuth-aquarium"></a>[Autonomous aquarium](docs/en/categories/animation.md#autonomous-aquarium) | Multiple fish wander and turn within a bounded tank. | [Source](https://github.com/electricazimuth/LocalLLM_VisualCodeTest/blob/7e7004885221fafb8b1de360cacc2b8281cf934a/code_prompts/aquarium.md) · [↗](https://electricazimuth.github.io/LocalLLM_VisualCodeTest/results/2025.04.28/html/GLM-4-32B-0414-F16-Q4_K_M_aquarium_20250425_171639.html) |
| <a id="case-electricazimuth-ball_bound"></a>[Many-ball gravity and damping](docs/en/categories/animation.md#many-ball-gravity-and-damping) | Simulate interacting balls and dissipative collisions in a square container. | [Source](https://github.com/electricazimuth/LocalLLM_VisualCodeTest/blob/7e7004885221fafb8b1de360cacc2b8281cf934a/code_prompts/ball_bound.md) · [↗](https://electricazimuth.github.io/LocalLLM_VisualCodeTest/results/2025.04.28/html/GLM-4-32B-0414-F16-Q4_K_M_ball_bound_20250425_172122.html) |
| <a id="case-electricazimuth-chicken"></a>[Wandering and egg-laying chicken](docs/en/categories/animation.md#wandering-and-egg-laying-chicken) | A chicken switches between wandering and laying, leaving eggs behind. | [Source](https://github.com/electricazimuth/LocalLLM_VisualCodeTest/blob/7e7004885221fafb8b1de360cacc2b8281cf934a/code_prompts/chicken.md) · [↗](https://electricazimuth.github.io/LocalLLM_VisualCodeTest/results/2025.04.28/html/GLM-4-32B-0414-F16-Q4_K_M_chicken_20250425_172543.html) |
| <a id="case-electricazimuth-fireworks"></a>[Autonomous fireworks particles](docs/en/categories/animation.md#autonomous-fireworks-particles) | Rockets launch and burst into fading particles affected by gravity. | [Source](https://github.com/electricazimuth/LocalLLM_VisualCodeTest/blob/7e7004885221fafb8b1de360cacc2b8281cf934a/code_prompts/fireworks.md) · [↗](https://electricazimuth.github.io/LocalLLM_VisualCodeTest/results/2025.04.28/html/GLM-4-32B-0414-F16-Q4_K_M_fireworks_20250425_172956.html) |
| <a id="case-electricazimuth-vehicles"></a>[Vehicle collision and restart](docs/en/categories/animation.md#vehicle-collision-and-restart) | Vehicles wrap around the screen, collide, explode and restart. | [Source](https://github.com/electricazimuth/LocalLLM_VisualCodeTest/blob/7e7004885221fafb8b1de360cacc2b8281cf934a/code_prompts/vehicles.md) · [↗](https://electricazimuth.github.io/LocalLLM_VisualCodeTest/results/2025.04.28/html/GLM-4-32B-0414-F16-Q4_K_M_vehicles_20250425_174812.html) |
| <a id="case-stock42-triple-pendulum"></a>[Triple-pendulum chaos painter](docs/en/categories/animation.md#triple-pendulum-chaos-painter) | Explore chaos and numerical stability through the endpoint of a three-link pendulum. | [Source](https://github.com/stock42/test-llm-coding/blob/5dd2e8e63f026337ddfa39195d7f1008806bca1d/promptings/triple-pendulum.md) · [↗](https://github.com/stock42/test-llm-coding/blob/5dd2e8e63f026337ddfa39195d7f1008806bca1d/codex/gpt-5.5/triple-pendulum/index.html) |
| <a id="case-stock42-1kg-block-bounces"></a>[Pi through block collisions](docs/en/categories/animation.md#pi-through-block-collisions) | Compare elastic-collision counts across mass ratios, separating exact results from visual approximations. | [Source](https://github.com/stock42/test-llm-coding/blob/5dd2e8e63f026337ddfa39195d7f1008806bca1d/promptings/1kg-block-bounces.md) · [↗](https://github.com/stock42/test-llm-coding/blob/5dd2e8e63f026337ddfa39195d7f1008806bca1d/codex/gpt-5.5/1kg-block-bounces/index.html) |
| <a id="case-stock42-balls-fall"></a>[Galton board and bell curve](docs/en/categories/animation.md#galton-board-and-bell-curve) | Balls pass through pegs into bins to build a distribution. | [Source](https://github.com/stock42/test-llm-coding/blob/5dd2e8e63f026337ddfa39195d7f1008806bca1d/promptings/balls-fall.md) · [↗](https://github.com/stock42/test-llm-coding/blob/5dd2e8e63f026337ddfa39195d7f1008806bca1d/codex/gpt-5.5/balls-fall/index.html) |
| <a id="case-kcores-ball-bouncing-inside-spinning-heptagon"></a>[20 numbered balls in a spinning heptagon](docs/en/categories/animation.md#20-numbered-balls-in-a-spinning-heptagon) | Simulate ball-ball and rotating-wall collisions with spin and friction; distinct from the existing single-ball hexagon task. | [Source](https://github.com/KCORES/kcores-llm-arena/blob/8f09c63e78189858377a760d03f69fb744b19aa2/benchmark-ball-bouncing-inside-spinning-heptagon/README.md) · [↗](https://github.com/KCORES/kcores-llm-arena/tree/8f09c63e78189858377a760d03f69fb744b19aa2/benchmark-ball-bouncing-inside-spinning-heptagon/src) |
| <a id="case-kcores-mandelbrot-set-meet-libai"></a>[Mandelbrot fractal drawn with Li Bai characters](docs/en/categories/animation.md#mandelbrot-fractal-drawn-with-li-bai-characters) | Combine poem-character processing, fractal zoom and frame-rate reporting in Canvas. | [Source](https://github.com/KCORES/kcores-llm-arena/blob/8f09c63e78189858377a760d03f69fb744b19aa2/benchmark-mandelbrot-set-meet-libai/README.md) · [↗](https://github.com/KCORES/kcores-llm-arena/tree/8f09c63e78189858377a760d03f69fb744b19aa2/benchmark-mandelbrot-set-meet-libai/src) |
| <a id="case-google-sim-fractals"></a>[Interactive fractal visualization](docs/en/categories/animation.md#interactive-fractal-visualization) | Explore zoom and detail through the official fractal demo. | [Source](https://blog.google/innovation-and-ai/products/gemini-app/3d-models-charts/) |
| <a id="case-google-sim-double-slit"></a>[Interactive double-slit interference](docs/en/categories/animation.md#interactive-double-slit-interference) | Use the official double-slit demo to explore parameters and interference patterns. | [Source](https://blog.google/innovation-and-ai/products/gemini-app/3d-models-charts/) |
| <a id="case-google-sim-double-pendulum"></a>[Interactive double-pendulum chaos](docs/en/categories/animation.md#interactive-double-pendulum-chaos) | Explore initial conditions and motion with the official double-pendulum demo. | [Source](https://blog.google/innovation-and-ai/products/gemini-app/3d-models-charts/) |
| <a id="case-reddit-glass-bridge-glass-bridge"></a>[Glass bridge fracture and loading](docs/en/categories/animation.md#glass-bridge-fracture-and-loading) | Show loading, crack propagation, shattering and particles in one file. | [Source](https://www.reddit.com/r/LLMDevs/comments/1urypfg/benchmarking_gpt56_sol_vs_grok_45_pro_with_the/) · [↗](https://x.com/EntelligenceAI/status/2075282696008532097) |
| <a id="case-x-itsolelehmann-2103124033365762215"></a>[Code film of four seasons through a train window](docs/en/categories/animation.md#code-film-of-four-seasons-through-a-train-window) | Observe: Layered parallax produces continuous motion | [Source](https://x.com/itsolelehmann/status/2103124033365762215) |
| <a id="case-x-victormustar-2102707412704919910"></a>[Inverse-kinematics pixel horse](docs/en/categories/animation.md#inverse-kinematics-pixel-horse) | Observe: Leg joints remain connected | [Source](https://x.com/victormustar/status/2102707412704919910) |
| <a id="case-x-chetaslua-2102501773705670994"></a>[Interactive steam-morph stop motion](docs/en/categories/animation.md#interactive-steam-morph-stop-motion) | Observe: Shape transformations remain coherent | [Source](https://x.com/chetaslua/status/2102501773705670994) |
| <a id="case-x-lcslates-2102503027340988559"></a>[Reassembling glass-and-gold mosaic](docs/en/categories/animation.md#reassembling-glass-and-gold-mosaic) | Observe: Tiles move continuously rather than swap images | [Source](https://x.com/LCSlates/status/2102503027340988559) |
| <a id="case-x-riku720720-2102515055116063144"></a>[Autonomous cosmic pixel dash](docs/en/categories/animation.md#autonomous-cosmic-pixel-dash) | Observe: Obstacles and character motion share consistent timing | [Source](https://x.com/riku720720/status/2102515055116063144) |
| <a id="case-x-dotcsv-2102737776219168939"></a>[Pixel animation of neural-network training](docs/en/categories/animation.md#pixel-animation-of-neural-network-training) | Observe: Animation distinguishes prediction from updating | [Source](https://x.com/DotCSV/status/2102737776219168939) |
| <a id="case-x-addyosmani-2103009037164110327"></a>[40-second coded browser explainer](docs/en/categories/animation.md#40-second-coded-browser-explainer) | Observe: Parsing, layout and painting are explained accurately | [Source](https://x.com/addyosmani/status/2103009037164110327) |
| <a id="case-x-alexalbert__-2102458348511879448"></a>[Blender claymation-style animation](docs/en/categories/animation.md#blender-claymation-style-animation) | Observe: Materials and lighting sustain the clay style | [Source](https://x.com/alexalbert__/status/2102458348511879448) |
| <a id="case-x-dadabots-2103039181266338276"></a>[JavaScript music-theory audiovisual](docs/en/categories/animation.md#javascript-music-theory-audiovisual) | Observe: Sound corresponds to note labels | [Source](https://x.com/dadabots/status/2103039181266338276) |

</details>

<a id="category-svg"></a>

## SVG Drawing · 32

[↑ Categories](#categories)

<details>
<summary>Awaiting previews · 32 cases</summary>

Real, reusable previews are still missing. Source output links are retained below; they are not inline previews.

| Case | What to try | Source / output |
| --- | --- | --- |
| <a id="case-svg-001"></a>[An octopus operating a pipe organ](docs/en/categories/svg.md#an-octopus-operating-a-pipe-organ) | An octopus plays a pipe organ, testing both tentacle anatomy and a convincing playing pose. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt1.svg) |
| <a id="case-svg-002"></a>[A giraffe assembling a grandfather clock](docs/en/categories/svg.md#a-giraffe-assembling-a-grandfather-clock) | A giraffe assembles a grandfather clock, combining a long-necked animal with delicate machinery. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt2.svg) |
| <a id="case-svg-003"></a>[A starfish driving a bulldozer](docs/en/categories/svg.md#a-starfish-driving-a-bulldozer) | A starfish sits at the controls of a bulldozer, testing machinery detail and the driving pose. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt3.svg) |
| <a id="case-svg-004"></a>[A moose conducting a carousel](docs/en/categories/svg.md#a-moose-conducting-a-carousel) | A moose conducts a carousel like an orchestra, testing the relationship between two different actions. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt4.svg) |
| <a id="case-svg-005"></a>[A flamingo repairing a telescope](docs/en/categories/svg.md#a-flamingo-repairing-a-telescope) | A flamingo repairs a telescope, combining slender limbs with detailed equipment. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt5.svg) |
| <a id="case-svg-006"></a>[A hedgehog playing an accordion](docs/en/categories/svg.md#a-hedgehog-playing-an-accordion) | A hedgehog plays an accordion, coordinating its body with the bellows and keyboard. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt6.svg) |
| <a id="case-svg-007"></a>[A jellyfish piloting a Ferris wheel](docs/en/categories/svg.md#a-jellyfish-piloting-a-ferris-wheel) | A jellyfish operates a Ferris wheel, connecting tentacles, controls, and a large machine. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt7.svg) |
| <a id="case-svg-008"></a>[An elephant typing on a typewriter](docs/en/categories/svg.md#an-elephant-typing-on-a-typewriter) | An elephant types on a typewriter, testing how its trunk or limbs interact with small keys. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt8.svg) |
| <a id="case-svg-009"></a>[A chameleon tuning a grand piano](docs/en/categories/svg.md#a-chameleon-tuning-a-grand-piano) | A chameleon tunes a grand piano, testing a complex instrument and a precise action. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt9.svg) |
| <a id="case-svg-010"></a>[A penguin juggling chainsaws](docs/en/categories/svg.md#a-penguin-juggling-chainsaws) | A penguin juggles several chainsaws, testing object recognition and implied motion. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt10.svg) |
| <a id="case-svg-011"></a>[A sloth steering an excavator](docs/en/categories/svg.md#a-sloth-steering-an-excavator) | A sloth drives an excavator, linking the animal to the cab and mechanical arm. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt11.svg) |
| <a id="case-svg-012"></a>[A dragonfly balancing a chandelier](docs/en/categories/svg.md#a-dragonfly-balancing-a-chandelier) | A dragonfly balances a large chandelier, combining a delicate creature with an intricate object. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt12.svg) |
| <a id="case-svg-013"></a>[A rhinoceros painting a lighthouse](docs/en/categories/svg.md#a-rhinoceros-painting-a-lighthouse) | A rhinoceros paints a tall lighthouse, testing scale differences and a painting pose. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt13.svg) |
| <a id="case-svg-014"></a>[A seahorse examining a microscope](docs/en/categories/svg.md#a-seahorse-examining-a-microscope) | A seahorse examines a microscope, combining a small animal with a precision instrument. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt14.svg) |
| <a id="case-svg-015"></a>[A peacock spinning a pottery wheel](docs/en/categories/svg.md#a-peacock-spinning-a-pottery-wheel) | A peacock spins a pottery wheel, combining elaborate feathers with a rotating tool. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt15.svg) |
| <a id="case-svg-016"></a>[A kangaroo climbing a radio tower](docs/en/categories/svg.md#a-kangaroo-climbing-a-radio-tower) | A kangaroo climbs a radio tower, testing pose, support points, and tall structures. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt16.svg) |
| <a id="case-svg-017"></a>[A lobster polishing a harp](docs/en/categories/svg.md#a-lobster-polishing-a-harp) | A lobster polishes a harp, testing contact points and instrument details. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt17.svg) |
| <a id="case-svg-018"></a>[A porcupine pushing a lawnmower](docs/en/categories/svg.md#a-porcupine-pushing-a-lawnmower) | A porcupine pushes a lawnmower, combining spines, a handle, and a pushing pose. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt18.svg) |
| <a id="case-svg-019"></a>[A gecko installing a satellite dish](docs/en/categories/svg.md#a-gecko-installing-a-satellite-dish) | A gecko installs a satellite dish on a building, testing attachment and installation poses. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt19.svg) |
| <a id="case-svg-020"></a>[An iguana carving a totem pole](docs/en/categories/svg.md#an-iguana-carving-a-totem-pole) | An iguana carves a wooden totem pole, testing tool use and intricate patterns. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt20.svg) |
| <a id="case-svg-021"></a>[An armadillo lifting a drawbridge](docs/en/categories/svg.md#an-armadillo-lifting-a-drawbridge) | An armadillo raises a drawbridge, testing the lifting mechanism and raised bridge state. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt21.svg) |
| <a id="case-svg-022"></a>[A mantis studying a sextant](docs/en/categories/svg.md#a-mantis-studying-a-sextant) | A mantis studies a sextant, testing recognition of an unfamiliar precision instrument. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt22.svg) |
| <a id="case-svg-023"></a>[An ostrich pulling a rickshaw](docs/en/categories/svg.md#an-ostrich-pulling-a-rickshaw) | An ostrich pulls a rickshaw, testing long legs and the direction of pulling forces. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt23.svg) |
| <a id="case-svg-024"></a>[A squid disassembling a printing press](docs/en/categories/svg.md#a-squid-disassembling-a-printing-press) | A squid takes apart a printing press, testing many mechanical parts and tentacle actions. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt24.svg) |
| <a id="case-svg-025"></a>[A butterfly inspecting a steam engine](docs/en/categories/svg.md#a-butterfly-inspecting-a-steam-engine) | A butterfly inspects a steam engine, combining organic wings with complex machinery. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt25.svg) |
| <a id="case-svg-026"></a>[A crab descending a fire escape](docs/en/categories/svg.md#a-crab-descending-a-fire-escape) | A crab descends an external fire escape, testing spatial direction and gait. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt26.svg) |
| <a id="case-svg-027"></a>[A venus flytrap swallowing a street lamp](docs/en/categories/svg.md#a-venus-flytrap-swallowing-a-street-lamp) | A giant Venus flytrap swallows a street lamp, testing scale and enclosure relationships. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt27.svg) |
| <a id="case-svg-028"></a>[Coral cleaning a ship's wheel](docs/en/categories/svg.md#coral-cleaning-a-ships-wheel) | Coral cleans a ship's wheel, testing how an unusual subject can express an action. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt28.svg) |
| <a id="case-svg-029"></a>[A sea anemone threading a loom](docs/en/categories/svg.md#a-sea-anemone-threading-a-loom) | A sea anemone threads a loom, testing dense thin lines and precise movements. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt29.svg) |
| <a id="case-svg-030"></a>[An orchid supporting a pergola](docs/en/categories/svg.md#an-orchid-supporting-a-pergola) | An orchid supports a garden pergola, testing structural support and plant form. | [Source](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt30.svg) |
| <a id="case-springprompt-unicorn"></a>[Draw a unicorn in SVG](docs/en/categories/svg.md#draw-a-unicorn-in-svg) | Inspect the horn, legs, mane, tail and connected shapes; this is not a direct reproduction of the TikZ version. | [Source](https://springprompt.com/playground/unicorn) |
| <a id="case-reddit-pgn-svg-pgn-svg"></a>[Render the final PGN position as SVG](docs/en/categories/svg.md#render-the-final-pgn-position-as-svg) | Track a specified chess game and highlight its last move in SVG. | [Source](https://www.reddit.com/r/LocalLLaMA/comments/1t53dhp/quality_comparison_between_qwen_36_27b/) · [↗](https://qwen3-6-27b-benchmark.vercel.app/) |

</details>

## Contribute

Share a challenge, an original preview or an attribution correction through [Issues](https://github.com/Java4ye/awesome-ai-tests/issues/new/choose) or a pull request. See the [contribution guide](CONTRIBUTING.en.md).

[Sources](docs/en/SOURCES.md) · [History](docs/en/HISTORY.md) · [Research leads](docs/en/RESEARCH.md) · [Guide](docs/en/GUIDE.md) · [Maintenance](docs/en/MAINTENANCE.md) · [Media credits](THIRD_PARTY_MEDIA.en.md)

Images show source-published works; historical models were not rerun here. Full videos open at creator posts. Original content and code: [MIT](LICENSE). Third-party previews retain their own licenses. Source conditions differ and do not form a standardized ranking.
