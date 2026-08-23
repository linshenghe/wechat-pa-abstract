# PowerPoint Cover Workflow

## Contents

- Contract
- Title insertion
- macOS file-access permission
- Screenshot capture
- Visual validation
- Stop conditions

## Contract

Use `assets/封面模板.pptx`. Copy it to a task-local temporary PPTX and never modify the original. Resolve the final cover directory from `word-workflow.md` and use `WeChat Cover - [safe English title].png`, limiting the title component to 100 characters.

Use the complete uppercased English title as the only cover text. Keep manuscript title capitalization unchanged. Insert a PowerPoint soft line break immediately after every colon or semicolon, including Chinese variants, using character 11 rather than a paragraph break.

Preserve the template's blue-gray design, blue uppercase bold sans-serif title, horizontal and vertical centering, and lower-right circular mark.

## Title Insertion

Start from a clean PowerPoint state when possible. If an existing PowerPoint state is ambiguous or the object-model bridge hangs, inspect the application before retrying.

Run the bundled script:

```bash
osascript scripts/write_cover_title.applescript "$TEMP_PPTX" "$UPPERCASED_TITLE"
```

The script must:

- open the temporary PPTX in Microsoft PowerPoint;
- address `shape "Title 1" -> text frame -> text range -> content` directly;
- insert soft breaks without creating extra paragraphs;
- save the presentation;
- read the same text range back;
- fail nonzero when read-back differs from the intended title.

Do not enumerate shapes unless direct addressing fails and a reliable fallback can be verified. Do not use `python-pptx`, `shape.text`, direct OOXML editing, clipboard paste, or simulated typing for title insertion.

After the script returns, independently inspect `ppt/slides/slide1.xml`. Confirm that the exact title text is present, the placeholder is gone, and each required punctuation break appears as `<a:br>`. Do not treat a zero exit code alone as success.

## macOS File-Access Permission

PowerPoint may show `授予文件访问权限` the first time it opens the temporary copy. A stalled AppleScript or an empty presentation count can be caused by this dialog even when the shell command eventually exits without useful output.

Do not request file access proactively. First attempt to open the exact task-local PPTX in PowerPoint. If it opens normally, continue without a permission step. If `授予文件访问权限` actually appears, resolve only that prompt before running the title script.

When the user requested the Word/cover deliverable, resolve this prompt narrowly:

1. Bring PowerPoint to the foreground and inspect the visible dialog.
2. Select `选择...` and grant access only to the exact task-local temporary PPTX, not its parent directory or the project.
3. Do not accept unrelated login, purchase, account, or broad permission prompts.
4. Close any empty or ambiguous presentation, then run `write_cover_title.applescript` after access is granted.
5. Repeat both object-model read-back and package inspection.

If the exact temporary file cannot be granted or verified, stop and ask the user.

## Screenshot Capture

Use PowerPoint's actual display. Bring PowerPoint to the foreground, resolve overlays, and run the slide show. Capture a candidate screenshot only after the slide is fully displayed.

PowerPoint slide-show controls may appear at the lower left immediately after launch. Wait for them to disappear, then recapture. Treat the first screenshot as a candidate, not the final image.

Prefer a full-screen slide show that covers the display. Otherwise capture only the PowerPoint slide-show window and crop to the visible slide canvas. Do not retain unrelated desktop or application content in the final PNG or persistent QA screenshots.

Inspect the candidate at original resolution. Recapture if it contains a cursor, playback controls, toolbar, menu, thumbnails, sidebar, notes, window chrome, account prompt, modal overlay, blank area outside the slide canvas, or any other application content.

Crop only the actual PowerPoint screenshot; do not recreate or export a substitute rendering. Never use Quick Look or `qlmanage` because this template can render incorrectly in black and white.

## Visual Validation

Compare with the most recent correct cover in the resolved cover directory when one exists. Confirm:

- blue-gray template appearance;
- blue uppercase bold sans-serif title;
- correct soft-break placement without paragraph spacing;
- title scale and centering;
- no clipping or overflow;
- unchanged background placement and lower-right circular mark;
- final PNG contains only the slide canvas.

Insert exactly that PNG into the Word manuscript. Compare the embedded media hash with the final PNG, then open the completed document in Microsoft Word and confirm the same image is displayed without clipping, stretching, or substitution.

## Stop Conditions

Stop and ask the user if any of these remain unresolved:

- template missing, unreadable, or lacking `Title 1`;
- PowerPoint unavailable or cannot open the temporary file;
- direct object-model addressing or read-back fails;
- title package inspection fails or soft breaks are wrong;
- file-access permission cannot be granted narrowly;
- screenshot permission, foreground control, or slide-show capture fails;
- an overlay cannot be resolved;
- screenshot contains UI or captures the wrong app/window;
- title is black, serif, mixed case, left-aligned, clipped, or off-center;
- final PNG differs materially from the template or cannot be inspected;
- Word cannot embed and display the verified PNG.
