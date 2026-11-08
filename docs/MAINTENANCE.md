# 仓库维护

**简体中文** | [English](en/MAINTENANCE.md)

[首页](../README.zh-CN.md) · [投稿与反馈](https://github.com/Java4ye/awesome-ai-fun/issues/new/choose)

投稿从 Issue 收集。入库前先检查是否重复，并区分原作者与转发者。未披露的模型、运行日期或条件保持未知；中英文描述应表达同一事实。

## 编辑入口

- `data/cases.json`：案例的中英文标题、介绍、分类与观察点。
- `data/sources.json`：来源导航。
- `data/history.json`：来源方历史效果、模型与运行条件，以及有许可的本地预览。
- `data/showcase.json`：逐案例预览，引用历史记录、原图 / 视频封面，或登记历史作品截图及出处；区分开放许可与未核实授权的来源引用。
- `data/research.json`：已收录条目的社区出处和核对记录。待筛选线索单独保存在仓库外。

README、作品索引与网站画廊共用同一份作品和专题清单。专题在索引中占一个入口，子项在索引下方展开。只有题面的条目在网站动手题库单独展示。可直接打开 `site/index.html` 本地预览。专题定义在 `scripts/showcase.py` 的 `WORK_GROUPS`，入库后的案例编号应保持稳定。「可试玩」对应有交互页面的作品。

生成脚本也会更新 `site/catalog.js`。`main` 分支推送后，GitHub Actions 会校验目录并把画廊和预览图发布到 [GitHub Pages](https://java4ye.github.io/awesome-ai-fun/site/?lang=zh)。无需单独维护网站数据。

画廊默认以英文按分类展示全部作品，中文使用同一布局。封面保持原比例并延迟加载，视频由读者打开作品后播放。

维护需要 Python 3.10+，无第三方依赖：

```bash
python scripts/validate.py
python scripts/build.py
python scripts/build.py --check
python -m unittest discover -s tests -v
```

不要手工修改自动生成的 README、分类页、索引和画廊。项目简介位于 `scripts/showcase.py` 的 `INTRO` 中；修改简介前应明确确认需求。

## 添加图片或动图

使用对应案例的真实作品，保留作者、模型、原图、固定版本和许可信息。图片或 GIF 可以直接预览；完整视频保留原帖播放入口。没有素材时保留待补状态，不使用相似配图或空白占位图代替。

`history.py` 核对原有缩略图与历史快照；`showcase.py` 核对新增本地截图的路径、日期与 SHA-256，以及外链字段。`source_reference` 记录必须保持 `license_status: not_verified`，不能冒称已获授权。使用条件见[素材说明](THIRD_PARTY_MEDIA.md)。
