# obsidian-knowledge-organizer

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-cjke84%2Fobsidian--knowledge--organizer-blue?logo=github)](https://github.com/cjke84/obsidian-knowledge-organizer)

面向 Obsidian vault 工作流的原生知识整理 skill。

## 适用场景

- 存入知识库
- 整理文章
- 去重后再保存
- 生成标签、摘要和相关文章建议

## 核心能力

- 生成可直接写入 Obsidian 的笔记，包含 frontmatter、wikilinks、embeds 和 block IDs
- 通过 URL、hash、alias 和相似度做分层去重
- 推荐可直接链接的相关文章
- 在写入前校验标签是否符合知识库契约

## 兼容性

- OpenClaw-compatible skill
- Codex-compatible skill
- Obsidian vault workflows

## 结构

- `SKILL.md`：技能契约与工作流
- `scripts/`：运行时辅助脚本
- `tests/`：回归测试
- `references/`：标签体系和支持文档

## 测试

```bash
pytest -q
```

## 使用

```bash
python scripts/check_duplicate.py "新标题" --content "$(cat draft.md)" --json
python scripts/find_related.py alpha beta --title "新标题" --json
```
