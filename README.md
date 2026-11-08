# Awesome AI Tests · 有趣的 AI 测试案例收藏夹

**简体中文** | [English](README.en.md)

> 收集互联网上那些好玩、奇怪、让人忍不住想拿去考一考大模型的测试题。  
> **不做模型排行榜，先把值得尝试的题目收集好。**

A curated collection of fun and reproducible AI model challenges — in Chinese and English, with source links.

## 分类导航

[游戏开发 (14)](#category-games) · [3D 与空间 (16)](#category-3d) · [应用与交互 (12)](#category-applications) · [动画与物理 (31)](#category-animation) · [SVG 绘画 (32)](#category-svg)

**105 条案例** · 3 条已有预览 · 102 条待补效果。

<a id="category-games"></a>

## 游戏开发 · 14

[↑ 返回分类导航](#分类导航)

<a id="case-x-dangreenheck-2103004432786993341"></a>

### 海岸钓鱼与买卖升级游戏

[![海岸钓鱼与买卖升级游戏 — Claude Opus 5.5（作者报告 / creator-reported）](https://raw.githubusercontent.com/dgreenheck/tidewater/4811ba48d795197de5621985f404e765c0b7c0ef/docs/screenshot.jpg)](https://dgreenheck.github.io/tidewater/)

观察重点：捕鱼卖鱼买装备是否构成闭环；保存与重开是否保持合理状态。

**模型：** Claude Opus 5.5（作者报告 / creator-reported） · **作者 / 发布者：** Dan Greenheck / DRG Software Solutions LLC

图片署名：Dan Greenheck / DRG Software Solutions LLC · [原图出处](https://github.com/dgreenheck/tidewater/blob/4811ba48d795197de5621985f404e765c0b7c0ef/docs/screenshot.jpg) · [MIT 许可](assets/licenses/tidewater-MIT.txt)

原项目截图；多轮迭代作品，试玩需要 WebGPU。

[原题 / 来源](https://x.com/dangreenheck/status/2103004432786993341) · [打开作品](https://dgreenheck.github.io/tidewater/) · [案例详情](docs/categories/games.md#海岸钓鱼与买卖升级游戏) · [▶ 作者视频](https://x.com/dangreenheck/status/2103004432786993341)

---

<details>
<summary>待补效果 · 13 条案例</summary>

这些案例尚缺可直接展示的真实预览。下方保留来源方作品入口，不将链接当成已补齐效果。

| 案例 | 测试内容 | 来源 / 历史作品 |
| --- | --- | --- |
| <a id="case-museum-006"></a>[一次写出卡丁车游戏](docs/categories/games.md#一次写出卡丁车游戏) | 一句话挑战单文件 3D 卡丁车游戏。 | [来源](https://aitestmuseum.com/zh/tests/kart-racer) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/kart-racer/output.html) |
| <a id="case-museum-009"></a>[一个文件写出 Flappy Bird](docs/categories/games.md#一个文件写出-flappy-bird) | 用单文件网页制作可玩的 Flappy Bird 风格游戏。 | [来源](https://aitestmuseum.com/zh/tests/flappy-bird) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/flappy-bird/output.html) |
| <a id="case-museum-010"></a>[一个文件写出俄罗斯方块](docs/categories/games.md#一个文件写出俄罗斯方块) | 让 AI 生成包含旋转、消行和升级机制的俄罗斯方块。 | [来源](https://aitestmuseum.com/zh/tests/tetris) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/tetris/output.html) |
| <a id="case-museum-015"></a>[摩天楼间的 3D 飞行游戏](docs/categories/games.md#摩天楼间的-3d-飞行游戏) | 用很短的指令生成穿越摩天楼的浏览器飞行游戏。 | [来源](https://aitestmuseum.com/zh/tests/flight-sim) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/flight-sim/output.html) |
| <a id="case-stock42-tetris-3d"></a>[带音效与排行榜的 3D 风格俄罗斯方块](docs/categories/games.md#带音效与排行榜的-3d-风格俄罗斯方块) | 把投影展示、落块规则、声音和持久化分数放进单文件游戏。 | [来源](https://github.com/stock42/test-llm-coding/blob/5dd2e8e63f026337ddfa39195d7f1008806bca1d/promptings/tetris-3d.md) · [↗](https://github.com/stock42/test-llm-coding/blob/5dd2e8e63f026337ddfa39195d7f1008806bca1d/codex/gpt-5.5/tetris-3d/index.html) |
| <a id="case-psydox-01"></a>[单文件光线投射 FPS](docs/categories/games.md#单文件光线投射-fps) | 用受限浏览器技术实现第一人称地图、敌人和射击闭环。 | [来源](https://github.com/psydox/Local-LLM-Coding-Benchmark/blob/061dec9d8918b0b1d302678e070247f866471fa9/01_Browser_FPS_Raycasting_Game_Test.txt) |
| <a id="case-psydox-03"></a>[带最佳成绩的记忆翻牌](docs/categories/games.md#带最佳成绩的记忆翻牌) | 考察洗牌、翻牌状态与本地成绩保存。 | [来源](https://github.com/psydox/Local-LLM-Coding-Benchmark/blob/061dec9d8918b0b1d302678e070247f866471fa9/03_Memory_Card_Matching_Game_Test.txt) |
| <a id="case-psydox-04"></a>[Canvas 打砖块](docs/categories/games.md#canvas-打砖块) | 完成球拍、砖块、生命与关卡结束条件。 | [来源](https://github.com/psydox/Local-LLM-Coding-Benchmark/blob/061dec9d8918b0b1d302678e070247f866471fa9/04_Breakout_Canvas_Game_Test.txt) |
| <a id="case-psydox-06"></a>[俯视角 2D 驾驶游戏](docs/categories/games.md#俯视角-2d-驾驶游戏) | 在滚动赛道中处理操控、障碍和终点流程。 | [来源](https://github.com/psydox/Local-LLM-Coding-Benchmark/blob/061dec9d8918b0b1d302678e070247f866471fa9/06_Top_Down_2D_Driving_Game_Test.txt) |
| <a id="case-google-studio-neon_arena_laser_tag"></a>[Neon Arena 多人激光对战](docs/categories/games.md#neon-arena-多人激光对战) | 多人房间、机器人对手与限时计分组成联机游戏闭环。 | [来源](https://blog.google/innovation-and-ai/technology/developers-tools/full-stack-vibe-coding-google-ai-studio/) · [↗](https://aistudio.google.com/apps/bundled/neon_arena_laser_tag) |
| <a id="case-google-studio-neon_claw"></a>[Neon Claw 物理抓娃娃机](docs/categories/games.md#neon-claw-物理抓娃娃机) | 把夹爪控制、碰撞、计时与排行榜结合成三维游戏。 | [来源](https://blog.google/innovation-and-ai/technology/developers-tools/full-stack-vibe-coding-google-ai-studio/) · [↗](https://aistudio.google.com/apps/bundled/neon_claw) |
| <a id="case-x-nachat_dayo-2102773498037023140"></a>[鱼叉捕鱼小游戏](docs/categories/games.md#鱼叉捕鱼小游戏) | 观察：命中与得分判定是否一致 | [来源](https://x.com/nachat_dayo/status/2102773498037023140) |
| <a id="case-x-oguzthedev-2102476490344730950"></a>[种花养蜂与采蜜游戏](docs/categories/games.md#种花养蜂与采蜜游戏) | 观察：花朵蜜蜂蜂箱是否有实际关联 | [来源](https://x.com/oguzthedev/status/2102476490344730950) |

</details>

<a id="category-3d"></a>

## 3D 与空间 · 16

[↑ 返回分类导航](#分类导航)

<a id="case-pelican-sdf-001"></a>

### 用 SDF 构建可交互的 3D 鹈鹕骑车

[![用 SDF 构建可交互的 3D 鹈鹕骑车 — google/gemini-3.1-pro-preview](assets/previews/pelican-sdf/gemini-3-1-pro-high-run-01.jpg)](https://pelican.vibe-overflow.com/result.html?id=gemini-3-1-pro-high-run-01)

用代码定义有符号距离场、光线步进、材质和相机，构建可旋转、缩放检查的 3D 鹈鹕骑车场景。这是独立的 3D 延伸题，不是 SVG 动画题的同题结果。

**模型：** google/gemini-3.1-pro-preview · **作者 / 发布者：** AzatJalilov / Pelican SDF contributors

图片署名：AzatJalilov / Pelican SDF contributors · [原图出处](https://raw.githubusercontent.com/AzatJalilov/PelicanSdf/63190d7e5fb883175b8612374de5e7f094293548/assets/thumbnails/gemini-3-1-pro-high-run-01.jpg) · [MIT 许可](assets/licenses/pelican-sdf-MIT.txt)

[来源运行记录](https://github.com/AzatJalilov/PelicanSdf/blob/63190d7e5fb883175b8612374de5e7f094293548/data/results/gemini-3-1-pro-high-run-01.json)

来源方记录的运行日期：2026-07-18

可辨认鸟和自行车；是否满足全部交互要求请到原页检查。

[原题 / 来源](https://github.com/AzatJalilov/PelicanSdf/blob/63190d7e5fb883175b8612374de5e7f094293548/benchmark/prompt.txt) · [打开作品](https://pelican.vibe-overflow.com/result.html?id=gemini-3-1-pro-high-run-01) · [案例详情](docs/categories/3d.md#用-sdf-构建可交互的-3d-鹈鹕骑车)

<details>
<summary>其他模型的效果</summary>

[![用 SDF 构建可交互的 3D 鹈鹕骑车 — gpt-5.5](assets/previews/pelican-sdf/gpt-5-5-run-01.jpg)](https://pelican.vibe-overflow.com/result.html?id=gpt-5-5-run-01)

**模型：** gpt-5.5 · **作者 / 发布者：** AzatJalilov / Pelican SDF contributors

图片署名：AzatJalilov / Pelican SDF contributors · [原图出处](https://raw.githubusercontent.com/AzatJalilov/PelicanSdf/63190d7e5fb883175b8612374de5e7f094293548/assets/thumbnails/gpt-5-5-run-01.jpg) · [MIT 许可](assets/licenses/pelican-sdf-MIT.txt)

[来源运行记录](https://github.com/AzatJalilov/PelicanSdf/blob/63190d7e5fb883175b8612374de5e7f094293548/data/results/gpt-5-5-run-01.json)

来源方记录的运行日期：2026-07-18

缩略图中主体大部分位于画面之外；保留该构图问题。

[![用 SDF 构建可交互的 3D 鹈鹕骑车 — claude-haiku-4-5-20251001](assets/previews/pelican-sdf/claude-haiku-4-5-high-run-01.jpg)](https://pelican.vibe-overflow.com/result.html?id=claude-haiku-4-5-high-run-01)

**模型：** claude-haiku-4-5-20251001 · **作者 / 发布者：** AzatJalilov / Pelican SDF contributors

图片署名：AzatJalilov / Pelican SDF contributors · [原图出处](https://raw.githubusercontent.com/AzatJalilov/PelicanSdf/63190d7e5fb883175b8612374de5e7f094293548/assets/thumbnails/claude-haiku-4-5-high-run-01.jpg) · [MIT 许可](assets/licenses/pelican-sdf-MIT.txt)

[来源运行记录](https://github.com/AzatJalilov/PelicanSdf/blob/63190d7e5fb883175b8612374de5e7f094293548/data/results/claude-haiku-4-5-high-run-01.json)

来源方记录的运行日期：2026-07-18

缩略图上方有裁切；静态预览不证明交互或自行车结构正确。

[![用 SDF 构建可交互的 3D 鹈鹕骑车 — deepseek/deepseek-v4-pro](assets/previews/pelican-sdf/deepseek-v4-pro-high-run-01.jpg)](https://pelican.vibe-overflow.com/result.html?id=deepseek-v4-pro-high-run-01)

**模型：** deepseek/deepseek-v4-pro · **作者 / 发布者：** AzatJalilov / Pelican SDF contributors

图片署名：AzatJalilov / Pelican SDF contributors · [原图出处](https://raw.githubusercontent.com/AzatJalilov/PelicanSdf/63190d7e5fb883175b8612374de5e7f094293548/assets/thumbnails/deepseek-v4-pro-high-run-01.jpg) · [MIT 许可](assets/licenses/pelican-sdf-MIT.txt)

[来源运行记录](https://github.com/AzatJalilov/PelicanSdf/blob/63190d7e5fb883175b8612374de5e7f094293548/data/results/deepseek-v4-pro-high-run-01.json)

来源方记录的运行日期：2026-07-18

原项目缩略图显示为单色画面，照原样保留；不据此推断所有视角均为空白。

[![用 SDF 构建可交互的 3D 鹈鹕骑车 — z-ai/glm-5.2](assets/previews/pelican-sdf/glm-5-2-high-run-01.jpg)](https://pelican.vibe-overflow.com/result.html?id=glm-5-2-high-run-01)

**模型：** z-ai/glm-5.2 · **作者 / 发布者：** AzatJalilov / Pelican SDF contributors

图片署名：AzatJalilov / Pelican SDF contributors · [原图出处](https://raw.githubusercontent.com/AzatJalilov/PelicanSdf/63190d7e5fb883175b8612374de5e7f094293548/assets/thumbnails/glm-5-2-high-run-01.jpg) · [MIT 许可](assets/licenses/pelican-sdf-MIT.txt)

[来源运行记录](https://github.com/AzatJalilov/PelicanSdf/blob/63190d7e5fb883175b8612374de5e7f094293548/data/results/glm-5-2-high-run-01.json)

来源方记录的运行日期：2026-07-18

可辨认场景与自行车轮廓；静态图不能用于判断控制是否可用。

</details>

---

<details>
<summary>待补效果 · 15 条案例</summary>

这些案例尚缺可直接展示的真实预览。下方保留来源方作品入口，不将链接当成已补齐效果。

| 案例 | 测试内容 | 来源 / 历史作品 |
| --- | --- | --- |
| <a id="case-museum-003"></a>[体素宝塔花园](docs/categories/3d.md#体素宝塔花园) | 只靠文字构建带樱花树的彩色体素宝塔花园。 | [来源](https://aitestmuseum.com/zh/tests/voxel-pagoda) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/voxel-pagoda/output.html) |
| <a id="case-museum-004"></a>[three.js 版 Minecraft](docs/categories/3d.md#threejs-版-minecraft) | 尝试一次性生成带方块世界的浏览器 Minecraft 简化版。 | [来源](https://aitestmuseum.com/zh/tests/minecraft-web) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/minecraft-web/output.html) |
| <a id="case-museum-005"></a>[会自己还原的魔方](docs/categories/3d.md#会自己还原的魔方) | 在 3D 页面实现可打乱、逐步旋转和自动还原的魔方。 | [来源](https://aitestmuseum.com/zh/tests/rubiks-cube) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/rubiks-cube/output.html) |
| <a id="case-museum-007"></a>[陨石撞击城市](docs/categories/3d.md#陨石撞击城市) | 生成包含陨石坠落、冲击波和城市变化的浏览器演示。 | [来源](https://aitestmuseum.com/zh/tests/meteor-city) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/meteor-city/output.html) |
| <a id="case-museum-011"></a>[太阳系模拟](docs/categories/3d.md#太阳系模拟) | 以浏览器动画展示太阳和行星的运行关系。 | [来源](https://aitestmuseum.com/zh/tests/solar-system) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/solar-system/output.html) |
| <a id="case-museum-020"></a>[地球到火星往返](docs/categories/3d.md#地球到火星往返) | 用 three.js 演示从地球到火星、再按发射窗口返回的轨道动画。 | [来源](https://aitestmuseum.com/zh/tests/mars-round-trip) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/mars-round-trip/output.html) |
| <a id="case-electricazimuth-lightshow"></a>[光线步进迷幻融合球](docs/categories/3d.md#光线步进迷幻融合球) | 使用 WebGL 和 SDF 表现移动球体的平滑融合。 | [来源](https://github.com/electricazimuth/LocalLLM_VisualCodeTest/blob/7e7004885221fafb8b1de360cacc2b8281cf934a/code_prompts/lightshow.md) · [↗](https://electricazimuth.github.io/LocalLLM_VisualCodeTest/results/2025.04.28/html/GLM-4-32B-0414-F16-Q4_K_M_lightshow_20250425_174301.html) |
| <a id="case-psydox-09"></a>[Python 软件渲染 3D 游戏](docs/categories/3d.md#python-软件渲染-3d-游戏) | 不用图形引擎，在标准库约束下完成三维投影和游戏状态。 | [来源](https://github.com/psydox/Local-LLM-Coding-Benchmark/blob/061dec9d8918b0b1d302678e070247f866471fa9/09_Python_Software_Rendered_3D_Game_Test.txt) |
| <a id="case-reddit-doner-doner"></a>[旋转烤肉串与燃气加热器](docs/categories/3d.md#旋转烤肉串与燃气加热器) | 不用外部库，在 Canvas 中呈现旋转肉串、热源与立体质感。 | [来源](https://www.reddit.com/r/LocalLLaMA/comments/1ua1na0/whats_more_impressive_glm_51_52_or_qwen_35_36/) |
| <a id="case-reddit-thriller-thriller"></a>[多人角色同步舞蹈 Three.js 场景](docs/categories/3d.md#多人角色同步舞蹈-threejs-场景) | 把多个人物、舞蹈动作、灯光与镜头组合到同一场景；原帖公开了指定角色题面。 | [来源](https://www.reddit.com/r/LocalLLaMA/comments/1rqlaw4/new_benchmark_just_dropped/) |
| <a id="case-x-dotey-2102940980379017293"></a>[可循文探索的桃花源记](docs/categories/3d.md#可循文探索的桃花源记) | 观察：文字与场景位置是否对应 | [来源](https://x.com/dotey/status/2102940980379017293) |
| <a id="case-x-ishuagra02-2102543638689460488"></a>[从照片重建卡通秋日铁路](docs/categories/3d.md#从照片重建卡通秋日铁路) | 观察：构图与参照照片是否对应 | [来源](https://x.com/ishuagra02/status/2102543638689460488) |
| <a id="case-x-superalesha-2102779758408774104"></a>[从加速器隧道到质子碰撞](docs/categories/3d.md#从加速器隧道到质子碰撞) | 观察：隧道探测器与镜头是否空间连续 | [来源](https://x.com/superalesha/status/2102779758408774104) |
| <a id="case-x-techartist_-2102503719762018434"></a>[从线稿逐步长成三维房屋](docs/categories/3d.md#从线稿逐步长成三维房屋) | 观察：线稿体块细节之间是否连续 | [来源](https://x.com/techartist_/status/2102503719762018434) |
| <a id="case-x-studio_veco-2102684366996738511"></a>[可输入词语探索的柔彩村庄](docs/categories/3d.md#可输入词语探索的柔彩村庄) | 观察：输入与场景反馈是否有关系 | [来源](https://x.com/studio_veco/status/2102684366996738511) |

</details>

<a id="category-applications"></a>

## 应用与交互 · 12

[↑ 返回分类导航](#分类导航)

<a id="case-between-tokens-interactive-story"></a>

### 扮演语言模型的交互叙事

[![扮演语言模型的交互叙事 — Claude Fable 5（仓库署名 / repository credit）](https://raw.githubusercontent.com/chrisjz/between-tokens/93561477667dfc27df77f451e747353a15654f46/assets/screenshot.png)](https://chrisjz.github.io/between-tokens/)

让读者选择候选回复，观察温度滑杆、上下文消退与叙事分支。

**模型：** Claude Fable 5（仓库署名 / repository credit） · **作者 / 发布者：** Chris Zaharia

图片署名：Chris Zaharia · [原图出处](https://github.com/chrisjz/between-tokens/blob/93561477667dfc27df77f451e747353a15654f46/assets/screenshot.png) · [MIT 许可](assets/licenses/between-tokens-MIT.txt)

原项目截图；候选文本预写，概率实时计算。

[原题 / 来源](https://news.ycombinator.com/item?id=49311484) · [打开作品](https://chrisjz.github.io/between-tokens/) · [案例详情](docs/categories/applications.md#扮演语言模型的交互叙事)

---

<details>
<summary>待补效果 · 11 条案例</summary>

这些案例尚缺可直接展示的真实预览。下方保留来源方作品入口，不将链接当成已补齐效果。

| 案例 | 测试内容 | 来源 / 历史作品 |
| --- | --- | --- |
| <a id="case-museum-012"></a>[一个 HTML 文件里的操作系统](docs/categories/applications.md#一个-html-文件里的操作系统) | 在单个 HTML 页面中做一个含窗口和多种应用的桌面系统。 | [来源](https://aitestmuseum.com/zh/tests/web-os-desktop) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/web-os-desktop/output.html) |
| <a id="case-museum-014"></a>[积木搭建器](docs/categories/applications.md#积木搭建器) | 创建可放置、旋转、改色和删除积木的 3D 编辑器。 | [来源](https://aitestmuseum.com/zh/tests/brick-builder) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/brick-builder/output.html) |
| <a id="case-psydox-05"></a>[本地保存的个人记账应用](docs/categories/applications.md#本地保存的个人记账应用) | 实现记录增删改、筛选、汇总与刷新后的持久化。 | [来源](https://github.com/psydox/Local-LLM-Coding-Benchmark/blob/061dec9d8918b0b1d302678e070247f866471fa9/05_Personal_Expense_Tracker_App_Test.txt) |
| <a id="case-psydox-07"></a>[可拖拽与归档的任务看板](docs/categories/applications.md#可拖拽与归档的任务看板) | 结合任务和列管理、归档恢复、组合筛选与持久化。 | [来源](https://github.com/psydox/Local-LLM-Coding-Benchmark/blob/061dec9d8918b0b1d302678e070247f866471fa9/07_Kanban_Board_App_Test.txt) |
| <a id="case-psydox-08"></a>[Python 标准库图层绘图编辑器](docs/categories/applications.md#python-标准库图层绘图编辑器) | 用 Tkinter 和自建像素数据实现画笔、图层、滤镜与撤销。 | [来源](https://github.com/psydox/Local-LLM-Coding-Benchmark/blob/061dec9d8918b0b1d302678e070247f866471fa9/08_Python_GUI_Photoshop_Clone_Test.txt) |
| <a id="case-google-studio-cosmic_flow"></a>[Cosmic Flow 多人共享粒子](docs/categories/applications.md#cosmic-flow-多人共享粒子) | 多个用户用光标在共享三维空间中生成粒子。 | [来源](https://blog.google/innovation-and-ai/technology/developers-tools/full-stack-vibe-coding-google-ai-studio/) · [↗](https://aistudio.google.com/apps/bundled/cosmic_flow) |
| <a id="case-google-studio-geoseeker"></a>[GeoSeeker 地图交互应用](docs/categories/applications.md#geoseeker-地图交互应用) | 以官方地图应用为方向，考察真实外部数据与交互的结合。 | [来源](https://blog.google/innovation-and-ai/technology/developers-tools/full-stack-vibe-coding-google-ai-studio/) · [↗](https://aistudio.google.com/apps/bundled/geoseeker) |
| <a id="case-google-studio-heirloom_recipes"></a>[Heirloom Recipes 家庭协作食谱](docs/categories/applications.md#heirloom-recipes-家庭协作食谱) | 组织、导入和生成食谱，并支持家人协作。 | [来源](https://blog.google/innovation-and-ai/technology/developers-tools/full-stack-vibe-coding-google-ai-studio/) · [↗](https://aistudio.google.com/apps/bundled/heirloom_recipes) |
| <a id="case-x-petergyang-2102849349122470205"></a>[上传照片观看逐笔绘画](docs/categories/applications.md#上传照片观看逐笔绘画) | 观察：上传图是否影响绘画内容 | [来源](https://x.com/petergyang/status/2102849349122470205) |
| <a id="case-x-ryansael-2102591147927654847"></a>[可调焦距与光圈的镜头实验室](docs/categories/applications.md#可调焦距与光圈的镜头实验室) | 观察：光路变化是否对应焦平面变化 | [来源](https://x.com/RyanSael/status/2102591147927654847) |
| <a id="case-x-scheemunai-2103059885361598633"></a>[卧室新床摆放规划器](docs/categories/applications.md#卧室新床摆放规划器) | 观察：平面图与三维位置是否对应 | [来源](https://x.com/scheemunai/status/2103059885361598633) |

</details>

<a id="category-animation"></a>

## 动画与物理 · 31

[↑ 返回分类导航](#分类导航)

<details>
<summary>待补效果 · 31 条案例</summary>

这些案例尚缺可直接展示的真实预览。下方保留来源方作品入口，不将链接当成已补齐效果。

| 案例 | 测试内容 | 来源 / 历史作品 |
| --- | --- | --- |
| <a id="case-museum-001"></a>[鹈鹕骑自行车](docs/categories/animation.md#鹈鹕骑自行车) | 使用代码生成鹈鹕骑车的 SVG 动画，不只是静态画面。 | [来源](https://aitestmuseum.com/zh/tests/pelican-bicycle) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/pelican-bicycle/output.html) |
| <a id="case-museum-002"></a>[旋转六边形里的弹跳球](docs/categories/animation.md#旋转六边形里的弹跳球) | 小球在持续旋转的六边形里弹跳，涉及重力与摩擦。 | [来源](https://aitestmuseum.com/zh/tests/bouncing-ball-hexagon) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/bouncing-ball-hexagon/output.html) |
| <a id="case-museum-008"></a>[超新星爆发](docs/categories/animation.md#超新星爆发) | 展示恒星演化到超新星爆发及残骸的动画。 | [来源](https://aitestmuseum.com/zh/tests/supernova) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/supernova/output.html) |
| <a id="case-museum-013"></a>[沉没的哥特城市着色器](docs/categories/animation.md#沉没的哥特城市着色器) | 使用着色器绘制暴风雨中的半淹没哥特城市。 | [来源](https://aitestmuseum.com/zh/tests/drowned-gothic-city) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/drowned-gothic-city/output.html) |
| <a id="case-museum-016"></a>[用双手控制的粒子](docs/categories/animation.md#用双手控制的粒子) | 摄像头双手手势驱动 Three.js 粒子形状变化。 | [来源](https://aitestmuseum.com/zh/tests/hand-gesture-particles) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/hand-gesture-particles/output.html) |
| <a id="case-museum-017"></a>[超立方体里的弹跳球](docs/categories/animation.md#超立方体里的弹跳球) | 旋转四维超立方体里弹跳的小球，挑战高维可视化。 | [来源](https://aitestmuseum.com/zh/tests/tesseract-ball) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/tesseract-ball/output.html) |
| <a id="case-museum-018"></a>[星舰控制台](docs/categories/animation.md#星舰控制台) | 借助 p5.js 生成充满想象力的未来星舰控制台。 | [来源](https://aitestmuseum.com/zh/tests/starship-control-panel) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/starship-control-panel/output.html) |
| <a id="case-museum-019"></a>[指向 10:10 的指针时钟](docs/categories/animation.md#指向-1010-的指针时钟) | 用 HTML/CSS 画出指向 10:10 并持续走秒的时钟。 | [来源](https://aitestmuseum.com/zh/tests/ai-world-clock) · [↗](https://aitestmuseum.com/results/claude-opus-5-5/ai-world-clock/output.html) |
| <a id="case-electricazimuth-aquarium"></a>[自主游动的水族箱](docs/categories/animation.md#自主游动的水族箱) | 多条鱼自主游动，在鱼缸边缘平滑转向。 | [来源](https://github.com/electricazimuth/LocalLLM_VisualCodeTest/blob/7e7004885221fafb8b1de360cacc2b8281cf934a/code_prompts/aquarium.md) · [↗](https://electricazimuth.github.io/LocalLLM_VisualCodeTest/results/2025.04.28/html/GLM-4-32B-0414-F16-Q4_K_M_aquarium_20250425_171639.html) |
| <a id="case-electricazimuth-ball_bound"></a>[多球重力与阻尼碰撞](docs/categories/animation.md#多球重力与阻尼碰撞) | 在方形容器中模拟多球碰撞与能量损耗。 | [来源](https://github.com/electricazimuth/LocalLLM_VisualCodeTest/blob/7e7004885221fafb8b1de360cacc2b8281cf934a/code_prompts/ball_bound.md) · [↗](https://electricazimuth.github.io/LocalLLM_VisualCodeTest/results/2025.04.28/html/GLM-4-32B-0414-F16-Q4_K_M_ball_bound_20250425_172122.html) |
| <a id="case-electricazimuth-chicken"></a>[会散步和下蛋的母鸡](docs/categories/animation.md#会散步和下蛋的母鸡) | 母鸡在散步和下蛋状态间切换，鸡蛋留在产生的位置。 | [来源](https://github.com/electricazimuth/LocalLLM_VisualCodeTest/blob/7e7004885221fafb8b1de360cacc2b8281cf934a/code_prompts/chicken.md) · [↗](https://electricazimuth.github.io/LocalLLM_VisualCodeTest/results/2025.04.28/html/GLM-4-32B-0414-F16-Q4_K_M_chicken_20250425_172543.html) |
| <a id="case-electricazimuth-fireworks"></a>[自动发射的烟花粒子](docs/categories/animation.md#自动发射的烟花粒子) | 火箭升空后爆炸成受重力影响、逐渐消失的粒子。 | [来源](https://github.com/electricazimuth/LocalLLM_VisualCodeTest/blob/7e7004885221fafb8b1de360cacc2b8281cf934a/code_prompts/fireworks.md) · [↗](https://electricazimuth.github.io/LocalLLM_VisualCodeTest/results/2025.04.28/html/GLM-4-32B-0414-F16-Q4_K_M_fireworks_20250425_172956.html) |
| <a id="case-electricazimuth-vehicles"></a>[车辆碰撞爆炸与重新开始](docs/categories/animation.md#车辆碰撞爆炸与重新开始) | 车辆从屏幕另一侧重现，碰撞触发爆炸并重新初始化场景。 | [来源](https://github.com/electricazimuth/LocalLLM_VisualCodeTest/blob/7e7004885221fafb8b1de360cacc2b8281cf934a/code_prompts/vehicles.md) · [↗](https://electricazimuth.github.io/LocalLLM_VisualCodeTest/results/2025.04.28/html/GLM-4-32B-0414-F16-Q4_K_M_vehicles_20250425_174812.html) |
| <a id="case-stock42-triple-pendulum"></a>[三摆混沌轨迹画笔](docs/categories/animation.md#三摆混沌轨迹画笔) | 通过三段摆的末端轨迹观察混沌与数值稳定性。 | [来源](https://github.com/stock42/test-llm-coding/blob/5dd2e8e63f026337ddfa39195d7f1008806bca1d/promptings/triple-pendulum.md) · [↗](https://github.com/stock42/test-llm-coding/blob/5dd2e8e63f026337ddfa39195d7f1008806bca1d/codex/gpt-5.5/triple-pendulum/index.html) |
| <a id="case-stock42-1kg-block-bounces"></a>[用方块碰撞次数观察 π](docs/categories/animation.md#用方块碰撞次数观察-π) | 观察不同质量比例下的弹性碰撞次数，区分精确结论和视觉近似。 | [来源](https://github.com/stock42/test-llm-coding/blob/5dd2e8e63f026337ddfa39195d7f1008806bca1d/promptings/1kg-block-bounces.md) · [↗](https://github.com/stock42/test-llm-coding/blob/5dd2e8e63f026337ddfa39195d7f1008806bca1d/codex/gpt-5.5/1kg-block-bounces/index.html) |
| <a id="case-stock42-balls-fall"></a>[高尔顿板与钟形分布](docs/categories/animation.md#高尔顿板与钟形分布) | 小球穿过钉阵进入统计槽，观察分布逐渐形成。 | [来源](https://github.com/stock42/test-llm-coding/blob/5dd2e8e63f026337ddfa39195d7f1008806bca1d/promptings/balls-fall.md) · [↗](https://github.com/stock42/test-llm-coding/blob/5dd2e8e63f026337ddfa39195d7f1008806bca1d/codex/gpt-5.5/balls-fall/index.html) |
| <a id="case-kcores-ball-bouncing-inside-spinning-heptagon"></a>[旋转七边形中的 20 个编号小球](docs/categories/animation.md#旋转七边形中的-20-个编号小球) | 在旋转七边形中模拟球间碰撞、壁面碰撞和带摩擦自转；与原有单球六边形题不同。 | [来源](https://github.com/KCORES/kcores-llm-arena/blob/8f09c63e78189858377a760d03f69fb744b19aa2/benchmark-ball-bouncing-inside-spinning-heptagon/README.md) · [↗](https://github.com/KCORES/kcores-llm-arena/tree/8f09c63e78189858377a760d03f69fb744b19aa2/benchmark-ball-bouncing-inside-spinning-heptagon/src) |
| <a id="case-kcores-mandelbrot-set-meet-libai"></a>[李白诗句绘制 Mandelbrot 分形](docs/categories/animation.md#李白诗句绘制-mandelbrot-分形) | 将诗句字符处理、分形缩放与帧率统计结合在 Canvas 动画中。 | [来源](https://github.com/KCORES/kcores-llm-arena/blob/8f09c63e78189858377a760d03f69fb744b19aa2/benchmark-mandelbrot-set-meet-libai/README.md) · [↗](https://github.com/KCORES/kcores-llm-arena/tree/8f09c63e78189858377a760d03f69fb744b19aa2/benchmark-mandelbrot-set-meet-libai/src) |
| <a id="case-google-sim-fractals"></a>[交互式分形可视化](docs/categories/animation.md#交互式分形可视化) | 从官方分形演示观察缩放与细节变化。 | [来源](https://blog.google/innovation-and-ai/products/gemini-app/3d-models-charts/) |
| <a id="case-google-sim-double-slit"></a>[双缝干涉交互演示](docs/categories/animation.md#双缝干涉交互演示) | 以官方双缝实验演示为测试方向，观察参数与干涉图样。 | [来源](https://blog.google/innovation-and-ai/products/gemini-app/3d-models-charts/) |
| <a id="case-google-sim-double-pendulum"></a>[双摆混沌交互演示](docs/categories/animation.md#双摆混沌交互演示) | 通过官方双摆演示观察初始条件与运动变化。 | [来源](https://blog.google/innovation-and-ai/products/gemini-app/3d-models-charts/) |
| <a id="case-reddit-glass-bridge-glass-bridge"></a>[玻璃桥破裂与受力演示](docs/categories/animation.md#玻璃桥破裂与受力演示) | 在单文件中表现受力、裂纹扩展、碎裂和粒子效果。 | [来源](https://www.reddit.com/r/LLMDevs/comments/1urypfg/benchmarking_gpt56_sol_vs_grok_45_pro_with_the/) · [↗](https://x.com/EntelligenceAI/status/2075282696008532097) |
| <a id="case-x-itsolelehmann-2103124033365762215"></a>[列车窗外四季变换的代码短片](docs/categories/animation.md#列车窗外四季变换的代码短片) | 观察：层次视差是否形成连续运动 | [来源](https://x.com/itsolelehmann/status/2103124033365762215) |
| <a id="case-x-victormustar-2102707412704919910"></a>[逆运动学像素奔马](docs/categories/animation.md#逆运动学像素奔马) | 观察：关节运动是否保持腿部连接 | [来源](https://x.com/victormustar/status/2102707412704919910) |
| <a id="case-x-chetaslua-2102501773705670994"></a>[蒸汽变形的交互定格动画](docs/categories/animation.md#蒸汽变形的交互定格动画) | 观察：形态变换是否保持连贯 | [来源](https://x.com/chetaslua/status/2102501773705670994) |
| <a id="case-x-lcslates-2102503027340988559"></a>[会翻转重组的玻璃金箔马赛克](docs/categories/animation.md#会翻转重组的玻璃金箔马赛克) | 观察：拼片是否连续移动而非换图 | [来源](https://x.com/LCSlates/status/2102503027340988559) |
| <a id="case-x-riku720720-2102515055116063144"></a>[自动闪避的宇宙像素冲刺](docs/categories/animation.md#自动闪避的宇宙像素冲刺) | 观察：障碍与角色是否保持一致时序 | [来源](https://x.com/riku720720/status/2102515055116063144) |
| <a id="case-x-dotcsv-2102737776219168939"></a>[像素动画解释神经网络训练](docs/categories/animation.md#像素动画解释神经网络训练) | 观察：动画是否正确区分预测与更新 | [来源](https://x.com/DotCSV/status/2102737776219168939) |
| <a id="case-x-addyosmani-2103009037164110327"></a>[40 秒代码动画解释浏览器](docs/categories/animation.md#40-秒代码动画解释浏览器) | 观察：解析布局绘制的关系是否准确 | [来源](https://x.com/addyosmani/status/2103009037164110327) |
| <a id="case-x-alexalbert__-2102458348511879448"></a>[用 Blender 制作黏土风动画](docs/categories/animation.md#用-blender-制作黏土风动画) | 观察：材质与灯光是否保持黏土风格 | [来源](https://x.com/alexalbert__/status/2102458348511879448) |
| <a id="case-x-dadabots-2103039181266338276"></a>[纯 JavaScript 乐理视听实验](docs/categories/animation.md#纯-javascript-乐理视听实验) | 观察：声音与音符标签是否对应 | [来源](https://x.com/dadabots/status/2103039181266338276) |

</details>

<a id="category-svg"></a>

## SVG 绘画 · 32

[↑ 返回分类导航](#分类导航)

<details>
<summary>待补效果 · 32 条案例</summary>

这些案例尚缺可直接展示的真实预览。下方保留来源方作品入口，不将链接当成已补齐效果。

| 案例 | 测试内容 | 来源 / 历史作品 |
| --- | --- | --- |
| <a id="case-svg-001"></a>[章鱼演奏管风琴](docs/categories/svg.md#章鱼演奏管风琴) | 章鱼通过触手操作管风琴，既要画对触手，也要让演奏动作成立。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt1.svg) |
| <a id="case-svg-002"></a>[长颈鹿组装落地钟](docs/categories/svg.md#长颈鹿组装落地钟) | 一只长颈鹿正在组装古典落地钟，关注机械细节与装配动作。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt2.svg) |
| <a id="case-svg-003"></a>[海星驾驶推土机](docs/categories/svg.md#海星驾驶推土机) | 把海星放到推土机驾驶位，看看能否表现复杂的机械结构和姿势。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt3.svg) |
| <a id="case-svg-004"></a>[驼鹿指挥旋转木马](docs/categories/svg.md#驼鹿指挥旋转木马) | 让驼鹿像指挥家一样指挥旋转木马，考察两种动作的关系。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt4.svg) |
| <a id="case-svg-005"></a>[火烈鸟修理望远镜](docs/categories/svg.md#火烈鸟修理望远镜) | 让腿长嘴长的火烈鸟修理望远镜，考察细长肢体与器械细节。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt5.svg) |
| <a id="case-svg-006"></a>[刺猬演奏手风琴](docs/categories/svg.md#刺猬演奏手风琴) | 刺猬拉动手风琴，观察褶箱、琴键与身体部位的配合。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt6.svg) |
| <a id="case-svg-007"></a>[水母操控摩天轮](docs/categories/svg.md#水母操控摩天轮) | 水母操控巨大的摩天轮，重点看触须、操作台与设备的联系。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt7.svg) |
| <a id="case-svg-008"></a>[大象使用打字机](docs/categories/svg.md#大象使用打字机) | 笨重的大象在打字机上输入文字，观察鼻子与按键的互动。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt8.svg) |
| <a id="case-svg-009"></a>[变色龙给三角钢琴调音](docs/categories/svg.md#变色龙给三角钢琴调音) | 变色龙给三角钢琴调音，考察复杂器物的形状和细节。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt9.svg) |
| <a id="case-svg-010"></a>[企鹅玩杂耍抛电锯](docs/categories/svg.md#企鹅玩杂耍抛电锯) | 企鹅同时抛接多把电锯，测试动作轨迹与危险物件的辨识。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt10.svg) |
| <a id="case-svg-011"></a>[树懒驾驶挖掘机](docs/categories/svg.md#树懒驾驶挖掘机) | 树懒开挖掘机，测试驾驶舱、机械臂与主体之间的联系。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt11.svg) |
| <a id="case-svg-012"></a>[蜻蜓平衡枝形吊灯](docs/categories/svg.md#蜻蜓平衡枝形吊灯) | 蜻蜓维持大型吊灯的平衡，考察轻巧主体与复杂吊灯的关系。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt12.svg) |
| <a id="case-svg-013"></a>[犀牛粉刷灯塔](docs/categories/svg.md#犀牛粉刷灯塔) | 犀牛粉刷高耸的灯塔，考察比例差异与涂刷动作。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt13.svg) |
| <a id="case-svg-014"></a>[海马检查显微镜](docs/categories/svg.md#海马检查显微镜) | 海马检查显微镜，观察小型生物和精密仪器的描绘。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt14.svg) |
| <a id="case-svg-015"></a>[孔雀操作陶艺转盘](docs/categories/svg.md#孔雀操作陶艺转盘) | 孔雀转动陶艺转盘，测试复杂尾羽和旋转工具的组合。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt15.svg) |
| <a id="case-svg-016"></a>[袋鼠攀爬无线电塔](docs/categories/svg.md#袋鼠攀爬无线电塔) | 袋鼠攀爬细高的无线电塔，考察姿态、支撑点和高空结构。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt16.svg) |
| <a id="case-svg-017"></a>[龙虾擦亮竖琴](docs/categories/svg.md#龙虾擦亮竖琴) | 龙虾用钳子擦亮竖琴，测试工具、接触点与乐器细节。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt17.svg) |
| <a id="case-svg-018"></a>[豪猪推割草机](docs/categories/svg.md#豪猪推割草机) | 豪猪推动割草机，测试多刺身体、握柄和推行动作。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt18.svg) |
| <a id="case-svg-019"></a>[壁虎安装卫星天线](docs/categories/svg.md#壁虎安装卫星天线) | 壁虎在建筑物上安装卫星天线，测试吸附姿态与安装动作。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt19.svg) |
| <a id="case-svg-020"></a>[鬣蜥雕刻图腾柱](docs/categories/svg.md#鬣蜥雕刻图腾柱) | 鬣蜥雕刻木质图腾柱，考察雕刻痕迹与复杂花纹。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt20.svg) |
| <a id="case-svg-021"></a>[犰狳升起吊桥](docs/categories/svg.md#犰狳升起吊桥) | 犰狳启动吊桥机构，看看能否画出桥梁升起的状态。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt21.svg) |
| <a id="case-svg-022"></a>[螳螂研究六分仪](docs/categories/svg.md#螳螂研究六分仪) | 螳螂研究航海六分仪，挑战陌生精密仪器的识别。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt22.svg) |
| <a id="case-svg-023"></a>[鸵鸟拉人力车](docs/categories/svg.md#鸵鸟拉人力车) | 鸵鸟拖动人力车，考察细长腿与拉车受力方向。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt23.svg) |
| <a id="case-svg-024"></a>[鱿鱼拆卸印刷机](docs/categories/svg.md#鱿鱼拆卸印刷机) | 鱿鱼用触腕拆卸印刷机，挑战多部件机械绘画。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt24.svg) |
| <a id="case-svg-025"></a>[蝴蝶检查蒸汽机](docs/categories/svg.md#蝴蝶检查蒸汽机) | 蝴蝶检查蒸汽机，考察有机翅膀和复杂工业机械的共存。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt25.svg) |
| <a id="case-svg-026"></a>[螃蟹沿消防梯下楼](docs/categories/svg.md#螃蟹沿消防梯下楼) | 螃蟹沿建筑外的消防梯下降，测试空间方向与步态。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt26.svg) |
| <a id="case-svg-027"></a>[捕蝇草吞下路灯](docs/categories/svg.md#捕蝇草吞下路灯) | 巨大的捕蝇草吞噬路灯，测试尺度、植物口器与包覆关系。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt27.svg) |
| <a id="case-svg-028"></a>[珊瑚清洁船舵](docs/categories/svg.md#珊瑚清洁船舵) | 珊瑚清洁轮船舵轮，考察非典型主体的动作表达。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt28.svg) |
| <a id="case-svg-029"></a>[海葵为织布机穿线](docs/categories/svg.md#海葵为织布机穿线) | 海葵将线穿过织布机，挑战密集细线和细微动作。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt29.svg) |
| <a id="case-svg-030"></a>[兰花支撑藤架](docs/categories/svg.md#兰花支撑藤架) | 兰花支撑庭园藤架，测试结构承重关系与植物形态。 | [来源](https://gally.net/temp/20260914pelican-alternatives/index.html) · [↗](https://gally.net/temp/20260914pelican-alternatives/svgs/google_gemini-2.5-pro_prompt30.svg) |
| <a id="case-springprompt-unicorn"></a>[用 SVG 画独角兽](docs/categories/svg.md#用-svg-画独角兽) | 观察角、四肢、鬃毛、尾巴和形状连接；这不是 TikZ 版本的直接复现。 | [来源](https://springprompt.com/playground/unicorn) |
| <a id="case-reddit-pgn-svg-pgn-svg"></a>[从 PGN 棋谱推演并绘制 SVG 棋盘](docs/categories/svg.md#从-pgn-棋谱推演并绘制-svg-棋盘) | 从指定棋谱追踪棋子状态，并在 SVG 中标记最后一步。 | [来源](https://www.reddit.com/r/LocalLLaMA/comments/1t53dhp/quality_comparison_between_qwen_36_27b/) · [↗](https://qwen3-6-27b-benchmark.vercel.app/) |

</details>

## 欢迎补充

欢迎通过 [Issues](https://github.com/Java4ye/awesome-ai-tests/issues/new/choose) 或 Pull Request 补充题目、真实效果和原始出处，或纠正署名。详见[贡献指南](CONTRIBUTING.md)。

[来源导航](docs/SOURCES.md) · [历史档案](docs/HISTORY.md) · [社区线索](docs/RESEARCH.md) · [使用指南](docs/GUIDE.md) · [维护说明](docs/MAINTENANCE.md) · [素材署名](THIRD_PARTY_MEDIA.md)

图片为来源方作品，本库未重新调用历史模型；完整视频通过作者原帖打开。本库原创内容与代码采用 [MIT](LICENSE)，第三方预览按各自许可处理。不同来源的测试条件不构成统一排行榜。
