# Awesome AI Tests · 有趣的 AI 测试案例收藏夹

**简体中文** | [English](README.en.md)

> 收集互联网上那些好玩、奇怪、让人忍不住想拿去考一考大模型的测试题。  
> **不做模型排行榜，先把值得尝试的题目收集好。**

A curated collection of fun and reproducible AI model challenges — in Chinese and English, with source links.

**📦 首批收录：50 道案例 · 2 个资源网站 · 5 个分类**（后续数量以 [完整索引](docs/INDEX.md) 为准）  
**🗓️ 本次整理：2026-11-07**（来源网站可能继续更新）

[📚 浏览全部 50 道题](docs/INDEX.md) · [🔎 资源网站导航](docs/SOURCES.md) · [🧭 怎么使用](docs/GUIDE.md) · [🤝 贡献新案例](CONTRIBUTING.md)

---

## 🏷️ 按类型找题

| 分类 | 可以测什么 | 入口 |
| --- | --- | --- |
| 🎨 SVG 绘画 | 复杂物体、动作、关系理解 | [进入合集](docs/categories/svg.md) |
| 🎞️ 动画与物理 | 运动逻辑、碰撞、视觉特效 | [进入合集](docs/categories/animation.md) |
| 🧊 3D 与空间 | 空间结构、3D 交互、场景构建 | [进入合集](docs/categories/3d.md) |
| 🎮 游戏开发 | 游戏机制、操控、可玩性 | [进入合集](docs/categories/games.md) |
| 🖥️ 应用与交互 | 窗口管理、编辑器功能、交互设计 | [进入合集](docs/categories/applications.md) |

## ✨ 不知道先玩什么？从这 8 道开始

| 案例 | 有趣在哪 | 看原题 |
| --- | --- | --- |
| 🐙 章鱼演奏管风琴 | 八条触手真的能在“弹琴”吗？ | [Gally 第 1 题](https://gally.net/temp/20260914pelican-alternatives/index.html) |
| 🦒 长颈鹿组装落地钟 | 长脖子与精密机械如何配合？ | [Gally 第 2 题](https://gally.net/temp/20260914pelican-alternatives/index.html) |
| 🦩 鹈鹕骑自行车 | 脚踏、鸟腿和车轮能同步运动吗？ | [AI 考题博物馆](https://aitestmuseum.com/zh/tests/pelican-bicycle) |
| ⚽ 六边形弹跳球 | 旋转的墙壁会怎样改变反弹？ | [AI 考题博物馆](https://aitestmuseum.com/zh/tests/bouncing-ball-hexagon) |
| 🧊 自动还原的魔方 | 打乱之后，模型真的能还原吗？ | [AI 考题博物馆](https://aitestmuseum.com/zh/tests/rubiks-cube) |
| ⛏️ 浏览器 Minecraft | 一次生成能玩的方块世界有多难？ | [AI 考题博物馆](https://aitestmuseum.com/zh/tests/minecraft-web) |
| 🏎️ 卡丁车游戏 | 赛道、对手与操控能否兼顾？ | [AI 考题博物馆](https://aitestmuseum.com/zh/tests/kart-racer) |
| 🖥️ 单文件网页版操作系统 | 看起来像系统，还得真的能用 | [AI 考题博物馆](https://aitestmuseum.com/zh/tests/web-os-desktop) |

## 📚 资源网站

这版先从两个真实存在、可访问的合集开始，不为了凑数添加未经核实的链接。

1. **[Pelican-bicycle alternatives](https://gally.net/temp/20260914pelican-alternatives/index.html)** — 30 个脑洞 SVG 绘画题，重点是生物、机器与意想不到的动作关系。原站提供模型生成结果对比。
2. **[AI 考题博物馆](https://aitestmuseum.com/zh)** — 20 个经典代码与视觉挑战，覆盖动画、3D、小游戏和应用，提供题面与运行作品。

→ [查看来源介绍及原站说明](docs/SOURCES.md)

## 🧪 怎么测试？

1. 从[案例索引](docs/INDEX.md)中选一个感兴趣的题。
2. 点击原站链接，查看**真实题面**和原站说明；不要把本仓库的中文简介当作原 Prompt。
3. 使用你自己的 AI 模型复现，记录模型名称、运行方式、日期，以及是否修改过提示词。
4. 对照每道题的“可以观察什么”做判断：**能运行**和**效果好**是两回事。

注意：这个仓库是**资料索引**，并未跑过这 50 道题；不应把原站不同模型、不同运行环境下的结果当作统一排行榜。查看 [测试记录建议](docs/GUIDE.md)。

## 📁 仓库结构

```text
awesome-ai-tests/
├── README.md                   # 首页与精选入口
├── README.en.md                # English homepage
├── data/
│   ├── cases.json              # 50 道案例的结构化元数据（编辑入口）
│   └── sources.json            # 资源网站元数据
├── docs/
│   ├── INDEX.md                # 自动生成的全部案例索引
│   ├── categories/             # 自动生成的 5 类案例详解
│   ├── SOURCES.md              # 资源网站导航
│   ├── GUIDE.md                # 使用方式、字段与测试建议
│   └── en/                     # 英文索引、分类、来源和使用指南
├── scripts/
│   ├── build.py                # 从 JSON 生成 Markdown
│   └── validate.py             # 数据校验、查重
├── tests/                      # 数据校验的单元测试
├── .github/                    # CI 与投稿 Issue 模板
├── CONTRIBUTING.md
├── CONTRIBUTING.en.md
└── LICENSE
```

**本地维护**（Python 3.10+，无需安装依赖）：

```bash
python scripts/validate.py
python scripts/build.py
python -m unittest discover -s tests -v
```

改完 `data/cases.json` 再运行 `build.py`；生成的 Markdown 文件不要手工改，否则下次生成会覆盖。

## 💬 欢迎补充

欢迎提交有趣的 AI 考题、原始出处、测试重点，尤其是**短小、可以复现、能看出模型差别**的案例。可以通过仓库的 **Issues → New issue** 或 Pull Request 投稿。

**收录原则：** 来源清晰、玩法明确、不编造热度或测试效果；不搬运他人作品和大段原文。详见 [贡献指南](CONTRIBUTING.md)。

---

### 版权与致谢

本仓库只整理原创中英文简介、观察点和来源索引。原站的 Prompt、网页、SVG、模型输出及其权利归相应权利人或按其许可处理。**仓库的 MIT 许可仅覆盖本仓库原创内容与代码，不对第三方内容授予任何许可。**

感谢 [Tom Gally](https://gally.net/temp/20260914pelican-alternatives/index.html) 与 [AI 考题博物馆](https://aitestmuseum.com/zh) 的整理；请访问原站查看完整题面与模型成果。本站与上述项目无官方关联。
