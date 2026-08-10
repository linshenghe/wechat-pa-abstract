---
name: wechat-pa-abstract
description: Use when the user provides Public Administration article metadata, an abstract, citation details, article sections, or a PDF and wants a short-summary or long-summary WeChat manuscript, a fixed-format bilingual Word document, or a PowerPoint-template cover. Short summaries may use pasted metadata and abstract alone; long-summary, section-by-section, PDF-verified, and source-sensitive work requires the original PDF.
---

# WeChat PA Abstract

Create bilingual manuscripts for the Public Administration WeChat account. Deliver a Word document with a verified PowerPoint-derived cover by default. Do not open an article webpage unless the user explicitly asks.

When the user explicitly requests text only, a draft only, or no Word document, provide chat text and skip the file and cover workflows.

## Hard Gates

- For a short summary, require the English title, author names, and English abstract. Treat supported publication metadata as sufficient for a minimum citation; do not block only because volume, issue, or pages are absent.
- For a final long summary, section-by-section manuscript, PDF-verified manuscript, or source-sensitive translation, require the original readable PDF in addition to the title, authors, and abstract.
- Preserve author names exactly. Do not infer author order, DOI, year, volume, issue, pages, or other bibliographic facts from memory.
- Use the bundled PowerPoint template and Microsoft PowerPoint's actual display for the cover. Do not substitute Quick Look, Keynote, generated images, HTML, PIL-created covers, or direct OOXML title editing.
- Do not deliver a Word file as complete until Microsoft Word displays the embedded verified cover and the document passes content read-back.
- If a required source, application, permission, write, screenshot, or validation step remains unresolved, stop and ask the user how to proceed. State partial work as partial.

## Load the Relevant Workflow

Read each selected reference completely before acting:

- Short or long Word manuscript, output paths, fonts, metadata, rendering, or document validation: [references/word-workflow.md](references/word-workflow.md)
- Cover creation, PowerPoint object-model title insertion, macOS file permission handling, screenshot capture, or cover validation: [references/cover-workflow.md](references/cover-workflow.md)
- Long summary, PDF extraction, article structure, section condensation, or reviewer audit: [references/long-summary.md](references/long-summary.md)
- Delivery email: [references/email-drafts.md](references/email-drafts.md)

Use the bundled scripts instead of recreating one-off builders:

- `scripts/write_cover_title.applescript`: write and read back the PowerPoint `Title 1` text range.
- `scripts/build_short_docx.py`: build the fixed-format short-summary Word document from a JSON input.
- `scripts/validate_docx.py`: validate required text, one embedded cover, cover hash, fonts, comments, tracked changes, and core metadata.

## Input and Citation Contract

For multiple articles, create separate manuscripts unless the user explicitly asks for a combined document.

Ask only for genuinely missing essential fields. Do not ask the user to paste material already supplied.

When the user does not provide a ready citation but supplies enough supported metadata, create a minimum APA-style citation:

```text
[Author]. ([Supported year]). [Title in sentence case]. Public Administration. [Supported DOI URL]
```

Omit unsupported year or DOI if necessary. Never invent volume, issue, or pages. Ask for citation information only when the available metadata cannot identify the work reliably or when the user requires a complete formal citation.

If the user provides a website citation, preserve it unless the user asks for APA conversion. For conversion, use only supplied information or a source the user explicitly authorized Codex to open.

## Fixed Manuscript Format

For a short summary, use exactly this block order with one manual blank line between blocks:

```text
[English title]

[Chinese title]

今天为大家带来的是[author names exactly as provided]的研究：《[Chinese title]》。

摘要：

[Chinese abstract]

[Complete original English abstract]

Citation:
[APA citation or provided citation]
```

For a long summary, use the same opening blocks, then add:

```text

长摘要：

1. [Chinese section title] [Original English Section Title]

[Chinese condensed text]

[Matching English condensed text]
```

Repeat the section structure from the article itself. Do not force a theoretical, essay-style, or review article into an empirical template.

## Translation Rules

- Translate the title directly and academically.
- Translate the abstract precisely without adding interpretation, commentary, promotional wording, keywords, emojis, or extra sections.
- Keep the complete original English abstract after the Chinese abstract.
- Keep terminology consistent across the title, abstract, and long summary.
- If an official or author-provided Chinese title or abstract is supplied, use it as authoritative wording unless the user asks for polishing.
- For Chinese authors, ask whether an author-provided Chinese title or abstract exists before finalizing terminology.
- Before delivery, audit that author names remain unchanged, the Chinese text adds no unsupported claim, the English abstract is complete, and the citation is present.

## Core Execution Sequence

1. Resolve the output mapping and non-overwrite filename before creating files.
2. Draft and audit the bilingual content.
3. For long or source-sensitive work, complete the PDF workflow before final drafting.
4. Create and verify the cover through PowerPoint.
5. Build the Word manuscript and embed exactly that verified PNG once.
6. Run deterministic document validation.
7. Open the final document in Microsoft Word and verify the cover, Chinese text, spacing, and pagination. Export a temporary Word PDF for page-by-page QA when practical.
8. Deliver only the final Word document and cover PNG. Do not expose QA intermediates unless requested.

## Delivery Checklist

In the final response, state:

- Word document path
- Cover PNG path
- Whether an email draft was provided
- Which source and visual validations completed
- Any unresolved renderer-specific divergence or metadata risk

Do not report LibreOffice rendering as a pass when it drops Chinese glyphs. If Microsoft Word and its PDF export display the intended `Songti SC` text correctly, record the LibreOffice result as a renderer-specific diagnostic divergence rather than changing the required typography solely to satisfy LibreOffice.

## Browser and Computer Use

Work from pasted text when provided. Use browser or computer-use tools only when the user asks Codex to fetch a webpage, operate PowerPoint or Word, or inspect an application display. The required PowerPoint and Word verification for a requested file deliverable counts as authorization to operate those applications, but grant file access only to the specific task-local file and do not broaden access.
