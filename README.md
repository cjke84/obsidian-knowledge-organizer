# obsidian-knowledge-organizer

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-cjke84%2Fobsidian--knowledge--organizer-blue?logo=github)](https://github.com/cjke84/obsidian-knowledge-organizer)

Obsidian-native knowledge organizer / Obsidian 原生知识整理工具

## What it does / 功能

- Obsidian-native note shaping with frontmatter, wikilinks, embeds, and block IDs
- Layered duplicate detection and related-note discovery
- Tag-contract validation for Obsidian vault workflows

## Repository Layout / 仓库结构

- `SKILL.md`: skill contract and workflow
- `scripts/`: runtime helpers
- `tests/`: regression tests
- `references/`: tag system and supporting docs

## Testing / 测试

Run the full suite:

```bash
pytest -q
```

## Usage Examples / 使用示例

Check whether a draft duplicates an existing note:

```bash
python scripts/check_duplicate.py "New Title" --content "$(cat draft.md)" --json
```

Find related notes for a new article:

```bash
python scripts/find_related.py alpha beta --title "New Title" --json
```

检测草稿是否与现有笔记重复：

```bash
python scripts/check_duplicate.py "新标题" --content "$(cat draft.md)" --json
```

为新文章查找相关文章：

```bash
python scripts/find_related.py alpha beta --title "新标题" --json
```
