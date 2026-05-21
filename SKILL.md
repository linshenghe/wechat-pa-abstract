---
name: wechat-pa-abstract
description: Use when the user provides article metadata, abstract, and citation text for a Public Administration journal WeChat short-summary post, and wants it organized into a fixed bilingual manuscript format, exported as a Word document, or paired with a cover image made from the local PowerPoint cover template.
---

# WeChat PA Abstract

## Purpose

Create short WeChat manuscript drafts for the Public Administration journal account from user-provided article information. The user supplies the article title, authors, abstract, DOI/citation, or copied website text; do not open the article webpage unless the user explicitly asks.

## Default Input Assumption

The user provides pasted article information, usually including:

- English title
- Author names exactly as shown on the website
- Publication date or DOI, if available
- English abstract
- Website citation text, preferably APA

If any essential item is missing, ask only for the missing item. Essential items are English title, authors, abstract, and citation.

## Output Format

Always use this fixed order and spacing:

```text
[English title]

[Chinese title]

今天为大家带来的是[author names exactly as provided]的研究：《[Chinese title]》。

摘要：

[Chinese abstract]

[English abstract]

Citation:
[APA citation or provided citation]
```

## Translation Rules

- Keep author names in English exactly as provided by the user or website.
- Translate the title directly and academically.
- Translate the abstract directly, keeping academic precision and professional wording.
- Preserve the original English abstract after the Chinese abstract.
- Do not make the wording promotional or casual.
- Do not add interpretation, commentary, keywords, introductions, emojis, or extra sections unless the user asks.
- Citation defaults to APA. If the user provides a citation from the website, preserve it unless it is clearly not APA and the user asked for APA conversion.

## Word Document Workflow

When the user asks for a Word document, use the `doc` skill and create a `.docx` manuscript with these rules:

- File name: `WeChat Page Manuscript For "[English title]".docx`
- Preferred output folder in this workspace: `output/doc/`
- Font: Chinese text uses Songti/宋体; English text uses Times New Roman.
- Font size: 12 pt for all text.
- Alignment: left aligned for all paragraphs.
- Paragraph spacing: 0 before and 0 after.
- Line spacing: single line.
- Insert one manual blank line between every content block in the fixed output format.
- If a cover image has been generated, insert it at the beginning of the Word document before the English title.

For mixed Chinese and English in Word, set the western font to Times New Roman and the East Asian font to 宋体. After creating the document, verify by reading the `.docx` back and checking that the expected title, Chinese title, intro sentence, Citation label, and DOI or citation text are present.

## Cover Image Workflow

When the user asks for a cover image, or asks to include the cover in the Word document, use the local PowerPoint template:

- Template file: `封面模板.pptx` in the current workspace.
- Cover output folder: `output/cover/`.
- Final image file name: `WeChat Cover - [English title without unsafe filename characters].png`.
- Use the English title as the only cover text.
- Preserve the template's original blue-gray PowerPoint appearance.

Reliable procedure:

1. Copy or generate a temporary PPTX from `封面模板.pptx`; never modify the original template.
2. Insert the English title into the first slide title placeholder named `Title 1`.
3. Preserve the placeholder's inherited template style. Do not force a black/white color scheme.
4. Open the temporary PPTX in Microsoft PowerPoint and visually confirm the template is blue-gray, not black and white.
5. Use `screencapture` to capture the PowerPoint screen after permissions are available.
6. Crop the screenshot to the visible slide canvas and save the final PNG in `output/cover/`.
7. If the user requested a Word manuscript too, insert the final PNG at the top of the Word document.
8. Delete temporary PPTX files, PowerPoint lock files, full-screen screenshots, Quick Look previews, and extracted media directories. Keep only the final PNG and final Word document unless the user asks to keep more.

Do not use `qlmanage` or Quick Look thumbnails for the final cover image. Quick Look can render this template incorrectly as black and white. Use PowerPoint's actual display plus screenshot/cropping, or another method that has been visually checked against PowerPoint.

Validation checklist:

- PowerPoint view shows the blue-gray template.
- English title is centered in the first slide title area.
- Final PNG contains only the slide canvas, not PowerPoint toolbars, menus, sidebars, or notes.
- Final Word document contains the cover image if requested.
- `output/cover/` contains only the final PNG after cleanup.

## Browser and Computer Use

Only use browser or computer-use tools when the user explicitly wants Codex to fetch from the webpage, click Cite, copy from a site, inspect a local preview, operate PowerPoint, or verify the cover visually. If the user pasted the article information, work directly from the pasted text.
