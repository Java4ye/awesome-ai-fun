# 使用、数据规范与后续路线

**简体中文** | [English](en/GUIDE.md)

[← 返回首页](../README.md)

## 为什么只收录索引，不直接拷贝 Prompt？

这个仓库的定位是一个**可持续维护的精选合集**：帮你找到题目、看懂“它测什么”、回到原站拿真实题面。原站可能修改过提示词或运行方法，直接复制一份很快会过时；第三方材料的使用许可也不一定允许批量转载。

## 如何拿来测试新模型？

1. 从 [案例列表](INDEX.md) 选择题目，点击原站打开完整说明。
2. 明确记录 `prompt_version`：直接使用原站版本，还是自行改写；如改写应保存自己的提示词。
3. 记录模型、模型版本、工具或客户端、时间、是否联网、是否使用 Agent、是否允许重试。
4. 保存你自己的测试代码、截图和运行说明（不要冒充原站模型输出）。
5. 分开判断：**实现正确性 / 可运行性 / 视觉效果 / 操作体验**。不要把不同条件下的结果直接排排名。

**运行记录示例**（仅为格式示例，非真实结果）：

```yaml
case_id: museum-002
model: "填写实际模型版本"
client: "填写客户端或 API"
date: "YYYY-MM-DD"
prompt_version: "原站 / 翻译 / 自己改写"
prompt_language: "实际使用的语言"
agent_mode: false
retries: 0
runs: "自己保存的代码或链接"
notes: "物理碰撞、边界穿透、动画帧率等观察"
```

## 数据说明

编辑入口：`data/cases.json`（案例），`data/sources.json`（网站）。

| 字段 | 含义 |
| --- | --- |
| `id` | 稳定案例 ID，更新标题时尽量保持不变 |
| `title` / `title_en` | 中文名 / 英文对照，均必填 |
| `category` | `svg`, `animation`, `3d`, `games`, `applications` |
| `summary` | 本库原创中文概述，不是完整原始提示词 |
| `summary_en` | 对应英文概述，不是完整原始提示词 |
| `checks` | 自己建议的观察点，不代表官方评分规则 |
| `checks_en` | 与中文条目一一对应的英文观察点 |
| `tags` | 跨类别检索标签 |
| `tags_en` | 与中文条目一一对应的英文标签 |
| `source_id` | 来源网站：`gally` / `museum` / `pelican-sdf` |
| `source_item_no` | 在原站的题目编号，方便查找 |
| `source_url` | 原站的真实链接 |
| `source_credit` | 原站标注的来源，不保证等同作品最早作者 |
| `source_credit_en` | 对应英文来源线索 |
| `prompt_status` | `source_only` = 提示词只在原站查看 |
| `status` | `collected_not_tested` = 本库尚未实测 |
| `verified_on` | 本库核对索引信息的日期，不是题目发布日期 |

`sources.json` 中的 `name_en` 和 `note_en` 是来源名称、说明的英文对照。两种语言共用案例 ID、来源链接和分类键。

分类是浏览入口，不是严格互斥的能力划分。每题选择一个主要分类，其他能力用标签表示。简介和观察点均为整理文字，不是原始 Prompt；如果测试时翻译或改写题面，应记录语言及版本。

## 本地操作

```bash
# 需要 Python 3.10+，无需 pip install
python scripts/validate.py
python scripts/build.py
python scripts/build.py --check
python -m unittest discover -s tests -v
```

- 每次修改 JSON 后重新执行构建，生成 `docs/INDEX.md`、`docs/categories/*.md` 及 `docs/en/` 中对应的英文页面，加上中英文历史效果档案与预览页，共 16 页。
- CI 会检查 JSON 字段和生成文件是否同步，避免贡献者忘记更新目录。
- 这里只验证数据结构，**不联网检测每个网址是否始终可访问**；源站链接未来可能失效，欢迎提 Issue。

## 下一阶段（尚未实现）

- [ ] 添加更多可追溯的测试资源网站与真正新的测试题
- [ ] 为经典题补充更早的公开出处与题面版本对照
- [ ] 增加用户自己的实测成果示例与必要的运行信息
- [ ] 如果案例增长明显，再考虑使用 GitHub Pages 做搜索与筛选

本版**没有**自动调用模型、自动评分、在线预览或排行榜。

## 历史效果与素材

[历史效果档案](HISTORY.md)从 `data/history.json` 自动生成；首页和[效果画廊](GALLERY.md)结合 `data/showcase.json` 选择代表预览，并保留同题其他模型结果。每条历史记录关联 `case_id`，包括发布者、模型、运行日期或时间范围、收录日期、来源、效果入口和测试条件。`published_on: null` 表示发布时间未公开，不用运行日或收录日代替。补图与生成方式见[维护说明](MAINTENANCE.md)。

仅链接条目使用 `rights: link_only`。保存预览的条目必须包含具体许可依据、许可证副本、固定源提交、原图地址、SHA-256 和原始运行记录快照。当前支持 MIT 许可的本地预览；新增其他许可先补充明确的处理规则。来源方的未验证状态不改为本库实测。

更多说明见[第三方素材与更正](../THIRD_PARTY_MEDIA.md)。
