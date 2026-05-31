---
name: wechat-pa-abstract
description: Use when the user provides article metadata, abstract, citation text, or article sections for a Public Administration journal WeChat short-summary or long-summary post, and wants it organized into a fixed bilingual manuscript format, exported as a Word document, or paired with a cover image made from the local PowerPoint cover template.
---

# WeChat PA Abstract

## Purpose

Create short or long WeChat manuscript drafts for the Public Administration journal account from user-provided article information. The user supplies the article title, authors, abstract, DOI/citation, copied website text, or article sections; do not open the article webpage unless the user explicitly asks.

## Default Input Assumption

The user provides pasted article information, usually including:

- English title
- Author names exactly as shown on the website
- Publication date or DOI, if available
- English abstract
- Website citation text, preferably APA

If any essential item is missing, ask only for the missing item. Essential items are English title, authors, abstract, and citation.

## Output Format

For a short-summary manuscript, always use this fixed order and spacing:

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

For a long-summary manuscript, use the same opening blocks as the short-summary manuscript, then add the long-summary body:

```text
[English title]

[Chinese title]

今天为大家带来的是[author names exactly as provided]的研究：《[Chinese title]》。

摘要：

[Chinese abstract]

[English abstract]

Citation:
[APA citation or provided citation]


长摘要：

1. [Chinese section title] [Original English Section Title]

[Chinese condensed text, usually 2-3 paragraphs]

[English condensed text matching the Chinese condensed text]


2. [Chinese section title] [Original English Section Title]

[Chinese condensed text, usually 2-3 paragraphs]

[English condensed text matching the Chinese condensed text]
```

If a cover image is generated, it is part of the final deliverable. Show or list the final PNG path in the response. If a Word manuscript is generated, insert the cover image at the beginning of the document before the English title.

## Translation Rules

- Keep author names in English exactly as provided by the user or website.
- Translate the title directly and academically.
- Translate the abstract directly, keeping academic precision and professional wording.
- Preserve the original English abstract after the Chinese abstract.
- If the article has Chinese authors, ask whether the user has an author-provided Chinese title or Chinese abstract. If provided, learn the authors' terminology choices and keep those translations consistent throughout the manuscript.
- Do not make the wording promotional or casual.
- Do not add interpretation, commentary, keywords, introductions, emojis, or extra sections unless the user asks.
- Citation defaults to APA. If the user provides a citation from the website, preserve it unless it is clearly not APA and the user asked for APA conversion.

## Long Summary Workflow

Use this workflow when the user asks for a long-summary version, extended abstract, long WeChat manuscript, or asks to process an article section by section.

Do not require the user to provide the whole article at once. Process only the section currently provided. At the end of each step, ask for the next specific section by function, not generically:

- After the opening abstract blocks, ask: `请给我第 1 部分“引言 / 研究背景”原文。`
- After the introduction/background section, ask: `请给我第 2 部分“文献综述 / 理论与假设”原文；它不一定叫 Literature Review，请给我承担这个功能的那一部分。`
- After the literature/theory/hypotheses section, ask: `请给我第 3 部分“方法 / 数据与研究设计”原文。`
- After the methods section, ask: `请给我第 4 部分“结果 / 发现”原文。`
- After the results section, ask: `请给我第 5 部分“讨论与结论”原文。`

For every long-summary section:

- Format the section title as `N. [Chinese section title] [Original English Section Title]`.
- Translate the Chinese section title from the original English section title.
- Put the Chinese condensed text first, then the matching English condensed text.
- Do not add a heading between the Chinese condensed text and English condensed text.
- Do not include the original full text.
- Do not include references, author-year citations, footnotes, or table numbers in the condensed text.
- Usually condense the section into 2-3 Chinese paragraphs; methods or results sections may be slightly longer if needed for clarity.
- First understand or translate the original into Chinese, then condense from that Chinese understanding.
- Preserve the original reasoning order. Do not reorganize the section into a generic guide such as background, question, contribution, method, and conclusion.
- Preserve important content when it appears in the original reasoning flow, including research questions, contributions, hypotheses, variable definitions, findings, limitations, policy implications, and future research directions.
- Avoid guide-like transitions such as `文章首先报告`, `本文接下来介绍`, or `下面说明` unless the original text itself uses that framing.
- The English condensed text should match the Chinese condensed text and use wording close to the original where possible. It is not a full copy of the original.

Section-specific rules:

- Introduction, background, or problem-setting sections: preserve the background, original reasoning flow, research question, research object, contribution, importance of the problem, and how the text moves into the analysis. Do not extract these into a separate guide-style summary unless the original does so.
- Literature review, theory, or hypotheses sections: preserve the theoretical lineage, core concepts, mechanism logic, contrasts between theoretical views, research gap, reasoning before hypotheses, and formal hypotheses. If `Hypothesis`, `H1`, `Proposition`, or similar formal statements appear, translate them completely and directly. Do not invent hypotheses when none are stated.
- Methods, data, empirical context, measures, models, or research design sections: preserve the empirical setting, research object, sample, time period, treatment and comparison groups, comparison logic, baseline year, observation period, robustness checks, dependent variables, key independent variables, control variables, model choice, and the reason for using the model or design. Do not reduce this to a generic statement that the paper uses regression analysis.
- Results, findings, analysis, or statistical results sections: preserve the main order of findings, baseline tests, placebo tests, main model results, coefficient direction, significance, key numbers, substantive magnitude, and whether the results support the earlier hypotheses, theoretical expectations, or research questions. Do not copy full tables.
- Discussion, conclusion, implications, limitations, or future research sections: preserve the main findings, relationship to theory, policy or practical implications, mechanism interpretation, limitations, unresolved questions, future research directions, and any future moderators or theoretical propositions. Do not turn the section into a promotional summary or a bullet list unless the original does so.

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

## Delivery Email Draft

When the manuscript is complete and the user wants to reply to the assigning professor or sender, provide a short English email draft in the chat. Do not insert the email draft into the Word document or manuscript body.

Use a slightly warm but still concise tone. Do not include the DOI or article link by default unless the user asks.

For an extended translation, use:

```text
Dear Sarah,

I hope you are doing well!

I have completed the extended translation, and the file is attached here.

Please let me know if there is anything you would like me to revise. Thank you!

Best regards,
Linsheng
```

For an abstract-only translation, use:

```text
Dear Sarah,

I hope you are doing well!

I have completed the abstract-only translation, and the file is attached here.

Please let me know if there is anything you would like me to revise. Thank you!

Best regards,
Linsheng
```

## Cover Image Workflow

When the user asks for a cover image, or asks to include the cover in the Word document, use the local PowerPoint template. This workflow applies to both short-summary and long-summary manuscripts:

- Template file: `assets/封面模板.pptx` bundled with this skill.
- Cover output folder: `output/cover/`.
- Final image file name: `WeChat Cover - [English title without unsafe filename characters].png`.
- Use the English title as the only cover text.
- If the English title contains a colon or semicolon (`:`, `;`, `：`, `；`), insert a line break immediately after that punctuation in the cover text, while keeping the manuscript title itself unchanged.
- Preserve the template's original blue-gray PowerPoint appearance.

Reliable procedure:

1. Copy or generate a temporary PPTX from `assets/封面模板.pptx`; never modify the original template.
2. Insert the English title into the first slide title placeholder named `Title 1`.
3. Preserve the placeholder's inherited template style. Do not force a black/white color scheme.
4. Open the temporary PPTX in Microsoft PowerPoint and visually confirm the template is blue-gray, not black and white.
5. Use `screencapture` to capture the PowerPoint screen after permissions are available.
6. Crop the screenshot to the visible slide canvas and save the final PNG in `output/cover/`.
7. If the user requested a Word manuscript too, insert the final PNG at the top of the Word document.
8. Close the temporary PowerPoint file after visual verification and final PNG creation.
9. Delete temporary PPTX files, PowerPoint lock files, full-screen screenshots, Quick Look previews, and extracted media directories. Keep only the final PNG and final Word document unless the user asks to keep more.

Do not use `qlmanage` or Quick Look thumbnails for the final cover image. Quick Look can render this template incorrectly as black and white. Use PowerPoint's actual display plus screenshot/cropping, or another method that has been visually checked against PowerPoint.

Validation checklist:

- PowerPoint view shows the blue-gray template.
- English title is centered in the first slide title area.
- Final PNG contains only the slide canvas, not PowerPoint toolbars, menus, sidebars, or notes.
- Final Word document contains the cover image if requested.
- `output/cover/` contains only the final PNG after cleanup.

## Browser and Computer Use

Only use browser or computer-use tools when the user explicitly wants Codex to fetch from the webpage, click Cite, copy from a site, inspect a local preview, operate PowerPoint, or verify the cover visually. If the user pasted the article information, work directly from the pasted text.
