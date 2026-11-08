# 第三方素材、署名与更正

**简体中文** | [English](THIRD_PARTY_MEDIA.en.md)

[首页](README.md) · [历史效果](docs/HISTORY.md) · [精选预览](docs/GALLERY.md)

本仓库记录公开可追溯的历史模型输出，不要求用已经不可用的模型重新生成。模型、运行日期和环境按来源记录填写，不代表本库独立核验了生成过程，也不代表模型厂商官方发布或背书。

## 已保存的预览图

本批五张图均为 **Pelican SDF** 原项目生成的 480×270 JPEG 缩略图，来自固定提交 `63190d7e5fb883175b8612374de5e7f094293548`。图片没有裁剪、压缩、重绘或替换；原图中的裁切或空白也照样保留。它们属于独立的 3D SDF 题，不是已有 SVG 动画题的结果。

- 作品整理者与署名：**AzatJalilov / Pelican SDF contributors**。
- 版权声明：**Copyright (c) 2026 Pelican SDF contributors**。
- 使用依据：[上游 MIT 许可证](https://github.com/AzatJalilov/PelicanSdf/blob/63190d7e5fb883175b8612374de5e7f094293548/LICENSE)，完整副本见 [assets/licenses/pelican-sdf-MIT.txt](assets/licenses/pelican-sdf-MIT.txt)。
- 文件：`assets/previews/pelican-sdf/*.jpg`；逐张原图地址、SHA-256、固定提交、运行日期与来源记录见 [data/history.json](data/history.json)。
- 模型记录快照：[data/upstream/pelican-sdf/](data/upstream/pelican-sdf/)，保留原字段，仅格式化 JSON。上游状态为 `unverified`，不改成“实测通过”。

预览涉及 gpt-5.5、claude-haiku-4-5-20251001、google/gemini-3.1-pro-preview、deepseek/deepseek-v4-pro 和 z-ai/glm-5.2。运行日均按上游 `createdAt` 记录为 2026-07-18；这不是模型发布日期或本站发布日期。

## 首页引用的原仓库截图

首页额外引用两张固定提交的原项目截图，图片通过原仓库 URL 展示，未保存到本仓库、裁切或重绘，也不是本库复现的结果。

| 案例 | 原图与版本 | 署名与许可 |
| --- | --- | --- |
| Tidewater | [原图](https://raw.githubusercontent.com/dgreenheck/tidewater/4811ba48d795197de5621985f404e765c0b7c0ef/docs/screenshot.jpg) · `4811ba48d795197de5621985f404e765c0b7c0ef` | Dan Greenheck / DRG Software Solutions LLC · Copyright (c) 2026 DRG Software Solutions LLC · [MIT 完整副本](assets/licenses/tidewater-MIT.txt) · [上游许可](https://github.com/dgreenheck/tidewater/blob/4811ba48d795197de5621985f404e765c0b7c0ef/LICENSE) · [场景素材署名](https://github.com/dgreenheck/tidewater/blob/4811ba48d795197de5621985f404e765c0b7c0ef/CREDITS.md) |
| Between Tokens | [原图](https://raw.githubusercontent.com/chrisjz/between-tokens/93561477667dfc27df77f451e747353a15654f46/assets/screenshot.png) · `93561477667dfc27df77f451e747353a15654f46` | Chris Zaharia · Copyright (c) 2026 Chris Zaharia · [MIT 完整副本](assets/licenses/between-tokens-MIT.txt) · [上游许可](https://github.com/chrisjz/between-tokens/blob/93561477667dfc27df77f451e747353a15654f46/LICENSE) |

首页视频链接回到创作者原帖，未转载或保存视频。X 的完整题面与制作过程未公开部分仍保留在案例说明中，不将发布日期写成运行日期。

## 仅提供链接的历史作品

- **Tom Gally 的 SVG 画廊**：按题号链接到原站及 2025 年 Gemini 2.5 Pro 原 SVG。原站没有提供本次使用所需的明确转载许可，所以不保存或内嵌这些图片。
- **AI 考题博物馆**：链接到题目详情和 Claude Opus 5.5 原始答案。运行日期与环境按原站公开信息记录；其 [服务条款](https://aitestmuseum.com/zh/terms)不作为通用转载许可，不保存其截图、视频或答案代码。

所有仅链接素材仍归相应权利人，并受原站条件约束。仓库的 MIT 许可只覆盖本库原创内容与代码，不将第三方素材重新授权。另附许可的素材按其各自许可处理。

## 以后怎样添加素材？

优先寻找作者原帖、原仓库或原博客。分别记录作者、发布者、模型、运行日期、收录日期和测试环境；未公布的细节留空，不根据画面猜测。视频优先提供原站播放入口。

保存图片前核对具体素材的使用条件，并保留许可或授权依据。外链图片、截图、裁剪或录屏也要核对使用条件。收到允许的素材以后再扩充预览；不拿其他题目的相似图片补位。

## 更正与下架

作者或权利人可以通过 [素材更正 / 下架 Issue](https://github.com/Java4ye/awesome-ai-tests/issues/new?template=media-correction.md) 提供案例编号、原始作品地址、涉及文件及希望如何处理。本仓库会核实并更正署名、更新链接或下架素材。也欢迎反馈错误模型标记和失效链接。

更正或移除时记录涉及的案例与处理说明。
