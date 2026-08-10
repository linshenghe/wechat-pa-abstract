# wechat-pa-abstract

Codex skill for producing short Public Administration journal WeChat manuscripts.

It organizes user-provided article information into a fixed bilingual format, creates a Word manuscript, and can generate a cover image from the local PowerPoint cover template workflow.

## Files

- `SKILL.md`: skill instructions
- `references/`: long-summary, cover, Word, and delivery-email workflows
- `scripts/`: deterministic PowerPoint title, short-DOCX build, and DOCX validation helpers
- `assets/封面模板.pptx`: authoritative PowerPoint cover template
- `agents/openai.yaml`: Codex UI metadata

## Install Locally

Copy this folder into:

```text
~/.codex/skills/wechat-pa-abstract
```
