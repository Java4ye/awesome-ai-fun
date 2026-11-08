# 应用与交互

**简体中文** | [English](../en/categories/applications.md)

> 从好看的界面走向可用的功能 · 共 **12 道**

[← 返回首页](../../README.zh-CN.md) · [全部案例](../INDEX.md)

> 下文简介和观察点为本库整理，不是原始提示词或官方评分规则。

## 扮演语言模型的交互叙事

**编号**：`between-tokens-interactive-story` · **收录来源**：[Chris Zaharia / Between Tokens](https://news.ycombinator.com/item?id=49311484)（本库来源组内序号 1）

**英文标题**：An interactive story where you are the model

[<img src="https://raw.githubusercontent.com/chrisjz/between-tokens/93561477667dfc27df77f451e747353a15654f46/assets/screenshot.png" alt="扮演语言模型的交互叙事 — Claude Fable 5（仓库署名 / repository credit）" width="720">](https://chrisjz.github.io/between-tokens/)

**模型：** Claude Fable 5（仓库署名 / repository credit） · **作者 / 发布者：** Chris Zaharia

图片署名：Chris Zaharia · [原图 / 作品出处](https://raw.githubusercontent.com/chrisjz/between-tokens/93561477667dfc27df77f451e747353a15654f46/assets/screenshot.png) · [MIT](../../assets/licenses/between-tokens-MIT.txt)

原项目截图；候选文本预写，概率实时计算。

让读者选择候选回复，观察温度滑杆、上下文消退与叙事分支。

**原站署名 / 来源线索**：Chris Zaharia / Between Tokens

**题面情况**：示例请求或部分题面

**可以观察什么？**

- 温度滑杆是否实际改变概率分布
- 是否明确标注预写文本与模拟注意力

**标签**：`交互应用`, `来源整理`

**提示词与作品**：[前往原站查看](https://news.ycombinator.com/item?id=49311484) · **本库测试情况**：未实测

### 历史效果

**Claude Fable 5（仓库署名 / repository credit）** · 运行日期未公开 · Chris Zaharia / chrisjz

[查看效果 / 体验](https://chrisjz.github.io/between-tokens/) · [来源记录](https://news.ycombinator.com/item?id=49311484) · [测试背景](https://github.com/chrisjz/between-tokens)

作者披露有两次移动端修复；候选回复和注意力高亮为预写内容，只有 softmax 概率是实时计算，不是在线模型推理。

---

## Cosmic Flow 多人共享粒子

**编号**：`google-studio-cosmic_flow` · **收录来源**：[Google AI Studio / Build mode](https://blog.google/innovation-and-ai/technology/developers-tools/full-stack-vibe-coding-google-ai-studio/)（本库来源组内序号 2）

**英文标题**：Cosmic Flow shared particles

[<img src="../../assets/previews/historical/google-studio-cosmic_flow.jpg" alt="Cosmic Flow 多人共享粒子 — Google AI Studio agent（未列具体模型 / exact model undisclosed）" width="720">](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/Google_AIS_FSR_CosmicFlow_05_DR.mp4)

**模型：** Google AI Studio agent（未列具体模型 / exact model undisclosed） · **作者 / 发布者：** Google

图片署名：Google · [原图 / 作品出处](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/Google_AIS_FSR_CosmicFlow_05_DR.mp4) · [素材说明](../../THIRD_PARTY_MEDIA.md)

Google 官方演示视频的画面截图，点击播放原视频。

多个用户用光标在共享三维空间中生成粒子。

**原站署名 / 来源线索**：Google AI Studio / Build mode

**题面情况**：示例请求或部分题面

**可以观察什么？**

- 不同客户端是否看到相同交互
- 粒子生命周期和性能是否稳定

**标签**：`交互应用`, `来源整理`

**提示词与作品**：[前往原站查看](https://blog.google/innovation-and-ai/technology/developers-tools/full-stack-vibe-coding-google-ai-studio/) · **本库测试情况**：未实测

### 历史效果

**Google AI Studio agent（未列具体模型 / exact model undisclosed）** · 运行日期未公开 · Google

[查看效果 / 体验](https://aistudio.google.com/apps/bundled/cosmic_flow) · [来源记录](https://blog.google/innovation-and-ai/technology/developers-tools/full-stack-vibe-coding-google-ai-studio/) · [测试背景](https://blog.google/innovation-and-ai/technology/developers-tools/full-stack-vibe-coding-google-ai-studio/)

官方文章介绍并链接的作品；打开 Remix / 试玩需要 Google 登录。本库核对了官方说明和入口，未登录运行，完整原始提示词与迭代过程未公开。

---

## GeoSeeker 地图交互应用

**编号**：`google-studio-geoseeker` · **收录来源**：[Google AI Studio / Build mode](https://blog.google/innovation-and-ai/technology/developers-tools/full-stack-vibe-coding-google-ai-studio/)（本库来源组内序号 4）

**英文标题**：GeoSeeker map interaction app

[<img src="../../assets/previews/historical/google-studio-geoseeker.jpg" alt="GeoSeeker 地图交互应用 — Google AI Studio agent（未列具体模型 / exact model undisclosed）" width="720">](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/Google-AIS-FSR_GeoSeeker_07-DR.mp4)

**模型：** Google AI Studio agent（未列具体模型 / exact model undisclosed） · **作者 / 发布者：** Google

图片署名：Google · [原图 / 作品出处](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/Google-AIS-FSR_GeoSeeker_07-DR.mp4) · [素材说明](../../THIRD_PARTY_MEDIA.md)

Google 官方演示视频的画面截图，点击播放原视频。

以官方地图应用为方向，考察真实外部数据与交互的结合。

**原站署名 / 来源线索**：Google AI Studio / Build mode

**题面情况**：示例请求或部分题面

**可以观察什么？**

- 地图数据是否来自明确接口
- 权限或网络失败时是否可恢复

**标签**：`交互应用`, `来源整理`

**提示词与作品**：[前往原站查看](https://blog.google/innovation-and-ai/technology/developers-tools/full-stack-vibe-coding-google-ai-studio/) · **本库测试情况**：未实测

### 历史效果

**Google AI Studio agent（未列具体模型 / exact model undisclosed）** · 运行日期未公开 · Google

[查看效果 / 体验](https://aistudio.google.com/apps/bundled/geoseeker) · [来源记录](https://blog.google/innovation-and-ai/technology/developers-tools/full-stack-vibe-coding-google-ai-studio/) · [测试背景](https://blog.google/innovation-and-ai/technology/developers-tools/full-stack-vibe-coding-google-ai-studio/)

官方文章介绍并链接的作品；打开 Remix / 试玩需要 Google 登录。本库核对了官方说明和入口，未登录运行，完整原始提示词与迭代过程未公开。

---

## Heirloom Recipes 家庭协作食谱

**编号**：`google-studio-heirloom_recipes` · **收录来源**：[Google AI Studio / Build mode](https://blog.google/innovation-and-ai/technology/developers-tools/full-stack-vibe-coding-google-ai-studio/)（本库来源组内序号 5）

**英文标题**：Heirloom Recipes collaborative cookbook

[<img src="../../assets/previews/historical/google-studio-heirloom_recipes.jpg" alt="Heirloom Recipes 家庭协作食谱 — Google AI Studio agent（未列具体模型 / exact model undisclosed）" width="720">](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/FSR_HeirloomRecipes_010_ss.mp4)

**模型：** Google AI Studio agent（未列具体模型 / exact model undisclosed） · **作者 / 发布者：** Google

图片署名：Google · [原图 / 作品出处](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/FSR_HeirloomRecipes_010_ss.mp4) · [素材说明](../../THIRD_PARTY_MEDIA.md)

Google 官方演示视频的画面截图，点击播放原视频。

组织、导入和生成食谱，并支持家人协作。

**原站署名 / 来源线索**：Google AI Studio / Build mode

**题面情况**：示例请求或部分题面

**可以观察什么？**

- 编辑与保存是否保持一致
- 多人协作时是否正确处理权限

**标签**：`交互应用`, `来源整理`

**提示词与作品**：[前往原站查看](https://blog.google/innovation-and-ai/technology/developers-tools/full-stack-vibe-coding-google-ai-studio/) · **本库测试情况**：未实测

### 历史效果

**Google AI Studio agent（未列具体模型 / exact model undisclosed）** · 运行日期未公开 · Google

[查看效果 / 体验](https://aistudio.google.com/apps/bundled/heirloom_recipes) · [来源记录](https://blog.google/innovation-and-ai/technology/developers-tools/full-stack-vibe-coding-google-ai-studio/) · [测试背景](https://blog.google/innovation-and-ai/technology/developers-tools/full-stack-vibe-coding-google-ai-studio/)

官方文章介绍并链接的作品；打开 Remix / 试玩需要 Google 登录。本库核对了官方说明和入口，未登录运行，完整原始提示词与迭代过程未公开。

---

## 一个 HTML 文件里的操作系统

**编号**：`museum-012` · **收录来源**：[AI 考题博物馆](https://aitestmuseum.com/zh/tests/web-os-desktop)（本库来源组内序号 12）

**英文标题**：An operating system in one HTML file

[<img src="../../assets/previews/historical/museum-012.jpg" alt="一个 HTML 文件里的操作系统 — Claude Opus 5.5" width="720">](https://aitestmuseum.com/results/claude-opus-5-5/web-os-desktop/output.html)

**模型：** Claude Opus 5.5 · **作者 / 发布者：** AI Test Museum

图片署名：AI Test Museum · [原图 / 作品出处](https://aitestmuseum.com/results/claude-opus-5-5/web-os-desktop/output.html) · [素材说明](../../THIRD_PARTY_MEDIA.md)

来源方已发布历史作品的浏览器截图（2026-11-08），不是重新调用模型；静帧不代表功能实测通过。

在单个 HTML 页面中做一个含窗口和多种应用的桌面系统。

**原站署名 / 来源线索**：@chetaslua

**可以观察什么？**

- 窗口拖拽、聚焦与关闭是否正常
- 文本编辑器等功能是否真的可操作
- 能按题目要求运行或交互，不以截图代替验收

**标签**：`应用`, `UI`

**提示词与作品**：[前往原站查看](https://aitestmuseum.com/zh/tests/web-os-desktop) · **本库测试情况**：未实测

### 历史效果

**Claude Opus 5.5** · 2026-10-19 · AI Test Museum

[查看效果 / 体验](https://aitestmuseum.com/results/claude-opus-5-5/web-os-desktop/output.html) · [来源记录](https://aitestmuseum.com/zh/tests/web-os-desktop) · [测试背景](https://aitestmuseum.com/zh#methodology)

原站 Claude Code agent 环境，包含其系统提示词；不等同裸 API。原站说明失败题可能重答，不将页面展示视作统一的一次成功记录。

---

## 积木搭建器

**编号**：`museum-014` · **收录来源**：[AI 考题博物馆](https://aitestmuseum.com/zh/tests/brick-builder)（本库来源组内序号 14）

**英文标题**：Brick builder

[<img src="../../assets/previews/historical/museum-014.jpg" alt="积木搭建器 — Claude Opus 5.5" width="720">](https://aitestmuseum.com/results/claude-opus-5-5/brick-builder/output.html)

**模型：** Claude Opus 5.5 · **作者 / 发布者：** AI Test Museum

图片署名：AI Test Museum · [原图 / 作品出处](https://aitestmuseum.com/results/claude-opus-5-5/brick-builder/output.html) · [素材说明](../../THIRD_PARTY_MEDIA.md)

来源方已发布历史作品的浏览器截图（2026-11-08），不是重新调用模型；静帧不代表功能实测通过。

创建可放置、旋转、改色和删除积木的 3D 编辑器。

**原站署名 / 来源线索**：Pietro Schirano（题面改写）

**可以观察什么？**

- 网格吸附与积木叠放是否合理
- 鼠标拾取和相机控制是否可用
- 能按题目要求运行或交互，不以截图代替验收

**标签**：`应用`, `3D 编辑`

**提示词与作品**：[前往原站查看](https://aitestmuseum.com/zh/tests/brick-builder) · **本库测试情况**：未实测

### 历史效果

**Claude Opus 5.5** · 2026-10-19 · AI Test Museum

[查看效果 / 体验](https://aitestmuseum.com/results/claude-opus-5-5/brick-builder/output.html) · [来源记录](https://aitestmuseum.com/zh/tests/brick-builder) · [测试背景](https://aitestmuseum.com/zh#methodology)

原站 Claude Code agent 环境，包含其系统提示词；不等同裸 API。原站说明失败题可能重答，不将页面展示视作统一的一次成功记录。

---

## 上传照片观看逐笔绘画

**编号**：`x-petergyang-2102849349122470205` · **收录来源**：[@petergyang / X](https://x.com/petergyang/status/2102849349122470205)（本库来源组内序号 1）

**英文标题**：Upload a photo and watch it painted

[<img src="https://pbs.twimg.com/amplify_video_thumb/2102849308903260160/img/Vf5QsGbNkpNJio9_.jpg" alt="上传照片观看逐笔绘画 — Opus 5.5" width="720">](https://video.twimg.com/amplify_video/2102849308903260160/vid/avc1/1920x1080/4O3qKeMgtNrj744w.mp4?tag=16)

**模型：** Opus 5.5 · **作者 / 发布者：** @petergyang

图片署名：@petergyang · [原图 / 作品出处](https://pbs.twimg.com/amplify_video_thumb/2102849308903260160/img/Vf5QsGbNkpNJio9_.jpg) · [素材说明](../../THIRD_PARTY_MEDIA.md)

原帖视频封面，点击封面播放原视频。

由公开作品整理的挑战方向：上传照片观看逐笔绘画。完整题面未逐字确认时，请勿当成原始提示词。

**原站署名 / 来源线索**：@petergyang；发现入口：[Awesome Opus Animation](https://github.com/krillinai/awesome-opus-animation/blob/main/categories/code-animation.md#case-2102849349122470205)；原帖通过公开读取服务核对。

**题面情况**：完整原题未确认，按作品整理

**可以观察什么？**

- 上传图是否影响绘画内容
- 风格切换与绘画进度是否可用

**标签**：`交互应用`, `来源整理`

**提示词与作品**：[前往原站查看](https://x.com/petergyang/status/2102849349122470205) · **本库测试情况**：未实测

### 历史效果

**Opus 5.5** · 运行日期未公开 · @petergyang

[查看效果 / 体验](https://x.com/petergyang/status/2102849349122470205) · [来源记录](https://x.com/petergyang/status/2102849349122470205) · [测试背景](https://claude.ai/artifact/9sZD4wrf1MpWACjg83hK4r)

通过 FxTwitter 公共读取接口核对原帖 ID、账号和文字；未直接登录 X，也未独立运行或验证视频。作品介绍部分参考发现索引；完整题面、素材来源与迭代次数未公开的部分不推测。发布时间不是运行时间。

---

## 可调焦距与光圈的镜头实验室

**编号**：`x-ryansael-2102591147927654847` · **收录来源**：[@RyanSael / X](https://x.com/RyanSael/status/2102591147927654847)（本库来源组内序号 1）

**英文标题**：Interactive focus and aperture lab

[<img src="https://pbs.twimg.com/amplify_video_thumb/2102589341197619200/img/yc_23PO0WRs63QWw.jpg" alt="可调焦距与光圈的镜头实验室 — Opus 5.5" width="720">](https://video.twimg.com/amplify_video/2102589341197619200/vid/avc1/1920x1080/0zt2fNiA4QMgvhkM.mp4?tag=29)

**模型：** Opus 5.5 · **作者 / 发布者：** @RyanSael

图片署名：@RyanSael · [原图 / 作品出处](https://pbs.twimg.com/amplify_video_thumb/2102589341197619200/img/yc_23PO0WRs63QWw.jpg) · [素材说明](../../THIRD_PARTY_MEDIA.md)

原帖视频封面，点击封面播放原视频。

由公开作品整理的挑战方向：可调焦距与光圈的镜头实验室。完整题面未逐字确认时，请勿当成原始提示词。

**原站署名 / 来源线索**：@RyanSael；发现入口：[Awesome Opus Animation](https://github.com/krillinai/awesome-opus-animation/blob/main/categories/explainers.md#case-2102591147927654847)；原帖通过公开读取服务核对。

**题面情况**：完整原题未确认，按作品整理

**可以观察什么？**

- 光路变化是否对应焦平面变化
- 参数和可视化是否保持一致

**标签**：`交互应用`, `来源整理`

**提示词与作品**：[前往原站查看](https://x.com/RyanSael/status/2102591147927654847) · **本库测试情况**：未实测

### 历史效果

**Opus 5.5** · 运行日期未公开 · @RyanSael

[查看效果 / 体验](https://x.com/RyanSael/status/2102591147927654847) · [来源记录](https://x.com/RyanSael/status/2102591147927654847) · [测试背景](https://lens.lab.sael.net)

通过 FxTwitter 公共读取接口核对原帖 ID、账号和文字；未直接登录 X，也未独立运行或验证视频。作品介绍部分参考发现索引；完整题面、素材来源与迭代次数未公开的部分不推测。发布时间不是运行时间。

---

## 卧室新床摆放规划器

**编号**：`x-scheemunai-2103059885361598633` · **收录来源**：[@scheemunai / X](https://x.com/scheemunai/status/2103059885361598633)（本库来源组内序号 1）

**英文标题**：Bedroom bed-placement planner

[<img src="https://pbs.twimg.com/amplify_video_thumb/2103059810547568640/img/yU6y3fQtRO9dTJEm.jpg" alt="卧室新床摆放规划器 — Opus 5.5" width="720">](https://video.twimg.com/amplify_video/2103059810547568640/vid/avc1/1280x720/L0UyvHEuNya7pOzY.mp4?tag=29)

**模型：** Opus 5.5 · **作者 / 发布者：** @scheemunai

图片署名：@scheemunai · [原图 / 作品出处](https://pbs.twimg.com/amplify_video_thumb/2103059810547568640/img/yU6y3fQtRO9dTJEm.jpg) · [素材说明](../../THIRD_PARTY_MEDIA.md)

原帖视频封面，点击封面播放原视频。

由公开作品整理的挑战方向：卧室新床摆放规划器。完整题面未逐字确认时，请勿当成原始提示词。

**原站署名 / 来源线索**：@scheemunai；发现入口：[Awesome Opus Animation](https://github.com/krillinai/awesome-opus-animation/blob/main/categories/3d-scenes.md#case-2103059885361598633)；原帖通过公开读取服务核对。

**题面情况**：完整原题未确认，按作品整理

**可以观察什么？**

- 平面图与三维位置是否对应
- 摆放是否符合尺寸与通行空间

**标签**：`交互应用`, `来源整理`

**提示词与作品**：[前往原站查看](https://x.com/scheemunai/status/2103059885361598633) · **本库测试情况**：未实测

### 历史效果

**Opus 5.5** · 运行日期未公开 · @scheemunai

[查看效果 / 体验](https://x.com/scheemunai/status/2103059885361598633) · [来源记录](https://x.com/scheemunai/status/2103059885361598633) · [测试背景](https://github.com/krillinai/awesome-opus-animation/blob/main/categories/3d-scenes.md#case-2103059885361598633)

通过 FxTwitter 公共读取接口核对原帖 ID、账号和文字；未直接登录 X，也未独立运行或验证视频。作品介绍部分参考发现索引；完整题面、素材来源与迭代次数未公开的部分不推测。发布时间不是运行时间。

---

<details>
<summary>待补效果 · 3 条案例</summary>

以下案例暂缺可直接展示的真实预览，保留完整介绍和来源方作品入口。

## 本地保存的个人记账应用

**编号**：`psydox-05` · **收录来源**：[psydox / Local LLM Coding Benchmark](https://github.com/psydox/Local-LLM-Coding-Benchmark/blob/061dec9d8918b0b1d302678e070247f866471fa9/05_Personal_Expense_Tracker_App_Test.txt)（本库来源组内序号 4）

**英文标题**：Persistent personal expense tracker

实现记录增删改、筛选、汇总与刷新后的持久化。

**原站署名 / 来源线索**：psydox / Local LLM Coding Benchmark

**题面情况**：公开题面

尚未找到历史效果；本条仅提供原始题面，不补造模型输出。

**可以观察什么？**

- 金额和日期是否校验
- 筛选后汇总与保存是否一致

**标签**：`交互应用`, `来源整理`

**提示词与作品**：[前往原站查看](https://github.com/psydox/Local-LLM-Coding-Benchmark/blob/061dec9d8918b0b1d302678e070247f866471fa9/05_Personal_Expense_Tracker_App_Test.txt) · **本库测试情况**：未实测

---

## 可拖拽与归档的任务看板

**编号**：`psydox-07` · **收录来源**：[psydox / Local LLM Coding Benchmark](https://github.com/psydox/Local-LLM-Coding-Benchmark/blob/061dec9d8918b0b1d302678e070247f866471fa9/07_Kanban_Board_App_Test.txt)（本库来源组内序号 6）

**英文标题**：Drag-and-drop Kanban board

结合任务和列管理、归档恢复、组合筛选与持久化。

**原站署名 / 来源线索**：psydox / Local LLM Coding Benchmark

**题面情况**：公开题面

尚未找到历史效果；本条仅提供原始题面，不补造模型输出。

**可以观察什么？**

- 拖拽后任务是否仍属于正确列
- 归档恢复和键盘操作是否可用

**标签**：`交互应用`, `来源整理`

**提示词与作品**：[前往原站查看](https://github.com/psydox/Local-LLM-Coding-Benchmark/blob/061dec9d8918b0b1d302678e070247f866471fa9/07_Kanban_Board_App_Test.txt) · **本库测试情况**：未实测

---

## Python 标准库图层绘图编辑器

**编号**：`psydox-08` · **收录来源**：[psydox / Local LLM Coding Benchmark](https://github.com/psydox/Local-LLM-Coding-Benchmark/blob/061dec9d8918b0b1d302678e070247f866471fa9/08_Python_GUI_Photoshop_Clone_Test.txt)（本库来源组内序号 7）

**英文标题**：Python standard-library layered editor

用 Tkinter 和自建像素数据实现画笔、图层、滤镜与撤销。

**原站署名 / 来源线索**：psydox / Local LLM Coding Benchmark

**题面情况**：公开题面

尚未找到历史效果；本条仅提供原始题面，不补造模型输出。

**可以观察什么？**

- 图层合成与选区是否正确
- 撤销重做和文件保存是否可靠

**标签**：`交互应用`, `来源整理`

**提示词与作品**：[前往原站查看](https://github.com/psydox/Local-LLM-Coding-Benchmark/blob/061dec9d8918b0b1d302678e070247f866471fa9/08_Python_GUI_Photoshop_Clone_Test.txt) · **本库测试情况**：未实测

---

</details>
