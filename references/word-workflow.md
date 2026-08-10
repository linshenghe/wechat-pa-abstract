# Word Manuscript Workflow

## Output Mapping

Resolve paths before writing:

- In `/Users/linsheng/Projects/work-pa-wechat-posts`: Word files go to `posts/`, cover PNGs to `covers/`, resumable drafts to `drafts/`, and task intermediates to `tmp/<safe-title>/`.
- In `/Users/linsheng/Desktop/Academic/PhD/Social Media For Public Administration`: Word files go to `output/doc/`, cover PNGs to `output/cover/`, and long-summary drafts to `tmp/wechat-pa-drafts/`.
- Elsewhere, use existing project instructions; if none exist, ask before creating a new output structure.

Use `WeChat Page Manuscript For "[safe English title]".docx`. Remove unsafe filename characters and limit the title component to 100 characters while preserving the full title inside the manuscript. If the target exists, use ` (Updated)` unless the user explicitly authorizes overwrite.

## Deterministic Short-Summary Build

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

Run:

```bash
python scripts/build_short_docx.py \
  --input manuscript.json \
  --cover verified-cover.png \
  --output final.docx
```

The script must refuse overwrite, insert the cover once before the English title, and preserve the fixed block order.

## Typography and Layout

- Use 12 pt for all manuscript text.
- Set western `ascii` and `hAnsi` fonts to `Times New Roman`.
- On macOS, set the OOXML East Asian font to `Songti SC`, the Microsoft Word name for the required Songti/宋体 family. Do not use the localized string `宋体` as the OOXML font name on macOS.
- Left-align every paragraph, use single line spacing, and set paragraph spacing to 0 pt before and after.
- Insert one real blank paragraph between content blocks.
- Use Letter portrait with 1-inch margins unless an existing authoritative manuscript template requires otherwise.
- Clear generated-document author and last-modified-by core properties. Do not remove metadata from a pre-existing user file unless requested.

## Deterministic Validation

Run:

```bash
python scripts/validate_docx.py \
  --docx final.docx \
  --input manuscript.json \
  --cover verified-cover.png
```

Require all checks to pass: expected text, complete DOI or citation, plausible paragraph count, exactly one inline image, embedded-image hash matching the verified PNG, `Songti SC` East Asian font mapping, no comments, no tracked changes, and blank author metadata.

For a long manuscript, add `"document_type": "long"` and an `"expected_additional_text"` array containing representative long-summary headings or required claims to the validation JSON. The validator then requires `长摘要：`, additional paragraphs, and every supplied representative string while retaining the same cover, font, revision, comment, and metadata checks.

## Visual Validation Authority

Use the available document skill to render the DOCX and inspect every page. Treat this as a diagnostic pass, not permission to ignore the project-required Microsoft Word check.

On macOS, LibreOffice may omit Chinese glyphs even when the OOXML correctly specifies `Songti SC`. If that occurs:

1. Record the LibreOffice result as a renderer-specific failure; do not call it a pass.
2. Do not change required typography solely to satisfy LibreOffice.
3. Open the final DOCX in Microsoft Word.
4. Verify the cover, Chinese glyphs, font, fixed block order, spacing, and pagination.
5. Export a temporary PDF from Microsoft Word and inspect every page when practical.
6. Treat Microsoft Word plus its PDF export as the final visual authority for this macOS workflow, while disclosing the LibreOffice divergence.

Confirm in Microsoft Word that the cover is not clipped, stretched, or substituted and matches the verified PNG.

## Temporary Files

Keep intermediates isolated under the task-local temporary directory. Delete only files created in the current run when project policy permits deletion. If local instructions prohibit deletion, leave the isolated directory intact and report it; never broaden cleanup to existing deliverables or require the entire output folder to contain only one file.
