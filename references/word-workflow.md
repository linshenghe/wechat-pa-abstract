# Word Manuscript Workflow

## Output Mapping

Resolve paths before writing:

- In `/Users/linsheng/Projects/work-pa-wechat-posts`: Word files go to `posts/`, cover PNGs to `covers/`, resumable drafts to `drafts/`, and task intermediates to `tmp/<safe-title>/`.
- In `/Users/linsheng/Desktop/Academic/PhD/Social Media For Public Administration`: Word files go to `output/doc/`, cover PNGs to `output/cover/`, and long-summary drafts to `tmp/wechat-pa-drafts/`.
- Elsewhere, use existing project instructions; if none exist, ask before creating a new output structure.

Use `WeChat Page Manuscript For "[safe English title]".docx`. Remove unsafe filename characters and limit the title component to 100 characters while preserving the full title inside the manuscript. If the target exists, use ` (Updated)` unless the user explicitly authorizes overwrite.

The current working directory may be a project directory, a Work scratch directory, or a Codex worktree. Resolve the project output root from the applicable project instructions and resolve the skill bundle root separately. In all commands below, `<SKILL_ROOT>` means the absolute directory containing this skill's `SKILL.md`; do not rely on a relative `scripts/` path. The angle-bracket values in the command examples are explanatory placeholders: replace them with the resolved skill path and the Python runtime available in the current environment.

## Office Preflight and Target-Window Control

Before opening the DOCX:

1. Check for existing Word processes/windows, the exact target DOCX, its task-local lock, blank startup documents, and modal dialogs.
2. If a previous task-local DOCX window is open, close only that exact document without saving. Do not quit Word or batch-kill Office processes.
3. Open through the macOS standard application path (`open -a` or the equivalent application object model). Do not launch the Word executable directly as a fallback.
4. If the current task is cloud-hosted or Microsoft Word/computer-use access is unavailable, do not attempt local Office commands. Finish only the non-Office stages that the user requested and report the visual check as pending or blocked.
5. If the standard local opening path fails, inspect the visible error or permission state once and resolve only a narrow, explicit permission issue for the exact task-local file. If it remains unavailable, stop and report the visual check as blocked.

Before `Cmd+End`, reading status-bar metrics, or taking a screenshot, confirm all of the following:

- exactly one relevant target DOCX window is present;
- the frontmost title matches the target filename;
- the document object/window resolves to the same target file;
- no blank startup document, modal dialog, or unrelated application is frontmost.

If target identity cannot be established, do not use a broad shortcut or capture a screenshot.

## Deterministic Manuscript Build

Use the bundled builder rather than recreating document code. Prepare UTF-8 JSON:

```json
{
  "english_title": "...",
  "chinese_title": "...",
  "authors": "...",
  "chinese_abstract": "...",
  "english_abstract": "...",
  "citation": "..."
}
```

Use the canonical builder for new work:

```bash
<available-python> <SKILL_ROOT>/scripts/build_docx.py \
  --input manuscript.json \
  --cover verified-cover.png \
  --output final.docx
```

For a long summary, set `"document_type": "long"` in the JSON and pass the audited Markdown directly:

```bash
<available-python> <SKILL_ROOT>/scripts/build_docx.py \
  --input manuscript.json \
  --long-summary long-summary.md \
  --cover verified-cover.png \
  --output final.docx
```

The canonical builder must refuse overwrite, insert the cover once before the English title, preserve the fixed opening order, and append the long-summary Markdown after `长摘要：`. Keep `build_short_docx.py` only as a backward-compatible short-summary entrypoint.

## Typography and Layout

- Use 12 pt for all manuscript text.
- Set western `ascii` and `hAnsi` fonts to `Times New Roman`.
- On macOS, set the OOXML East Asian font to `Songti SC`, the Microsoft Word name for the required Songti/宋体 family. Do not use the localized string `宋体` as the OOXML font name on macOS.
- Left-align every paragraph, use single line spacing, and set paragraph spacing to 0 pt before and after.
- Insert one real blank paragraph between content blocks.
- Use Letter portrait with 1-inch margins unless an existing authoritative manuscript template requires otherwise.
- Clear generated-document author and last-modified-by core properties. Do not remove metadata from a pre-existing user file unless requested.

## Deterministic Validation

Run the one-command final check:

```bash
<available-python> <SKILL_ROOT>/scripts/final_check.py \
  --docx final.docx \
  --input manuscript.json \
  --cover verified-cover.png \
  --long-summary long-summary.md \
  --word-pages 8 \
  --word-words 4591
```

Replace the example metrics with the values displayed by Microsoft Word during the visual pass. Omit `--long-summary` for a short manuscript. Require all checks to pass: fixed bilingual block order, exact Markdown–Word alignment for long summaries, complete DOI or citation, plausible paragraph count, exactly one inline image, embedded-image hash matching the verified PNG, `Songti SC` East Asian font mapping, no comments, no tracked changes, blank author metadata, non-empty file size, positive recorded Microsoft Word page and word counts, and no task-document lock file. The script must not open or control Office.

`validate_docx.py` remains available as the lower-level structural validator; invoke it from `<SKILL_ROOT>/scripts/` when needed. `final_check.py` is the required delivery gate.

## Visual Validation Authority

Use only Microsoft Word for visual validation. Do not run LibreOffice or a generic DOCX renderer.

1. Open the final DOCX in Microsoft Word.
2. Inspect the first page and confirm the verified cover, English title, Chinese title, opening, and Chinese abstract display correctly.
3. Jump to every numbered section heading and inspect the Chinese–English transition around each section boundary.
4. Use `Cmd+End` and confirm the status bar reports the expected final page and total page count.
5. Record the total page count and Word word count for `final_check.py`, then close the document without further edits so no task-document lock remains.
6. Inspect the final page for clipping, unexpected overflow, or missing text.
7. Export a temporary PDF from Microsoft Word only when page-by-page images are needed.

Confirm that the cover is not clipped, stretched, or substituted and matches the verified PNG. Microsoft Word and, when used, its own PDF export are the only visual authorities.

Classify the result explicitly:

- **Complete:** first page and actual final page were visually checked in Word, the cover (if applicable) was visually checked in PowerPoint, and `final_check.py` passed with no task-local lock remaining.
- **Partial:** structural/semantic checks passed, but one or more required visual views were not checked.
- **Blocked:** Office opening, permissions, dialogs, or target-window control prevented the required visual check.

Do not claim complete visual validation from `final_check.py` alone. Do not delete a lock file to force a pass; after a controlled close, report any remaining lock as unresolved.

## Temporary Files

Keep intermediates isolated under the task-local temporary directory. Delete only files created in the current run when project policy permits deletion. If local instructions prohibit deletion, leave the isolated directory intact and report it; never broaden cleanup to existing deliverables or require the entire output folder to contain only one file.
