# 仓库维护

**简体中文** | [English](en/MAINTENANCE.md)

[首页](../README.md) · [贡献指南](../CONTRIBUTING.md)

## 编辑入口

- `data/cases.json`：案例的中英文标题、介绍、分类与观察点。
- `data/sources.json`：来源导航。
- `data/history.json`：来源方历史效果、模型与运行条件，以及有许可的本地预览。
- `data/showcase.json`：首页代表预览，引用已有历史记录，或登记固定版本的原仓库截图和许可。
- `data/research.json`：社区出处与待整理线索。

首页、分类页和画廊由同一份数据生成。有可展示预览的案例默认展开，暂缺预览的案例归入各分类末尾的“待补效果”。新增预览后重新生成即可移到展开区域，案例不会因此重复计数。

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

本地缩略图的校验和与历史记录快照仍由 `history.py` 核对。远程截图引用固定提交，使用条件见[素材说明](../THIRD_PARTY_MEDIA.md)。
