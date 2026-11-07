# 贡献指南

**简体中文** | [English](CONTRIBUTING.en.md)

谢谢你愿意往这个收藏夹里加题！这里更在意题目的**趣味、清晰的出处和可复现性**，不追求把每一条互联网 AI 新闻都塞进来。

## 什么样的题目适合收录？

- 能让人很快理解“要 AI 做什么”，并且有具体的观察点；
- 最好有原帖、作者网站、仓库或其他可追溯的一手来源；
- 有趣、特别、能够展示模型能力差异；
- 如果是对原题的改写，说明改写缘由；不要把改写版写成原版。

不收录：无来源截图、营销软文、不能核对的“某模型碾压”故事、盗搬的视频和模型生成成果。

## 最轻松的投稿方式

打开本仓库的 **Issues → New issue**，选择“推荐测试题”或“推荐资源网站”，填上来源链接与理由即可。

## 如果希望直接 PR

1. 在 `data/cases.json` 添加一条结构化记录，格式参照已有案例；有新来源时先补 `data/sources.json`。
2. 使用 **自己的描述**写 `summary` 和 `checks`，并补充对应的 `title_en`、`summary_en`、`checks_en`、`tags_en`、`source_credit_en`。来源需有 `name_en`、`note_en`。中英文含义应一致，不要粘贴别人网站的整篇文章或全部 Prompt。
3. 使用已有分类 `svg` / `animation` / `3d` / `games` / `applications`。多个能力可写入 `tags`。
4. 运行以下命令，提交 JSON 及重新生成的 Markdown：

```bash
python scripts/validate.py
python scripts/build.py
python -m unittest discover -s tests -v
```

5. PR 中说明：新增了什么、为什么值得收录、原始来源在哪里、是否实测。

可以用中文或英文提交 Issue 推荐题目，不必先完成双语翻译。直接修改 JSON 的 PR 需要补齐双语字段，以通过校验。

案例 ID、分类键和来源链接由两种语言共用；分类允许交叉，用 `tags` / `tags_en` 标记其他能力。简介和译文不是原始提示词，使用翻译后的 Prompt 测试时请记录语言和版本。

## 保持诚实

`status: collected_not_tested` 表示仅整理资料。本库尚未建立自己的模型测试结果，所以不用“最高分”“实测通过”之类的标签。修改或撤回内容可以通过 Issue 提醒维护者。

所有第三方材料仍归各自权利人所有。本仓库的开源许可不意味着原站作品、图片、代码或提示词自动获得授权。
