# Long-Summary and PDF Workflow

## Contents

- Source gate
- Extraction and cross-validation
- Drafting rules
- Section-specific coverage
- Reviewer audit
- Temporary drafts

## Source Gate

Require the original article PDF for every final long-summary, section-by-section, PDF-verified, or source-sensitive manuscript. A preliminary chat-only translation from pasted text is allowed when explicitly requested, but label it preliminary and do not produce a final Word manuscript or cover until the PDF is verified.

Confirm that the PDF exists, is readable, is not encrypted, and has a plausible page count. If a required extractor is unavailable or source structure remains unresolved, stop and ask the user how to proceed.

## Extraction and Cross-Validation

Use the three extractors for distinct purposes:

1. Convert the PDF with `pdfmd` as the main working text:

   ```bash
   pdfmd "$INPUT_PDF" -o "$TEMP_DIR/article.pdfmd.md" --page-breaks --no-progress --stats
   ```

2. Use `pdftotext -layout` only for structural cross-validation:

   ```bash
   pdftotext -layout "$INPUT_PDF" "$TEMP_DIR/article.pdftotext.txt"
   ```

3. Compare page count, headings, section boundaries, abstract, references boundary, and interpretation-relevant tables or figures. Correct `pdfmd` heading mistakes from the structural extraction and direct PDF reading.
4. Use `pdfplumber` page-by-page only for final content QA. Check the completed manuscript for omitted concepts, section-order errors, mistranslations, and unsupported additions.

Record the methods used and unresolved extraction uncertainty in the final response.

## Drafting Rules

- Follow the article's actual section structure. Do not impose literature/method/results/discussion on theoretical, essay-style, or review articles.
- Format each section as `N. [Chinese section title] [Original English Section Title]`.
- Put Chinese condensed text first, followed directly by matching English condensed text without an intervening heading.
- Usually use two or three Chinese paragraphs per substantive section. Methods and results may be longer when clarity requires it.
- Condense rather than translate in full. Preserve the reasoning chain and major evidence; do not reduce a substantive section to one sentence.
- First understand the source in Chinese, then condense from that understanding.
- Preserve the original reasoning order. Do not reorganize the material into a generic guide.
- Omit references, author-year citations, footnotes, and table numbers from condensed text.
- Preserve research questions, contributions, hypotheses, definitions, findings, limitations, implications, and future research when they occur in the source flow.
- Avoid guide-like transitions such as `文章首先报告`, `本文接下来介绍`, or `下面说明` unless the source uses that framing.
- Make the English condensed text match the Chinese condensed text and stay close to source wording without copying full passages.

## Section-Specific Coverage

- Introduction/background: preserve the problem setting, reasoning flow, research question, object, contribution, importance, and transition into analysis.
- Literature/theory/hypotheses: preserve theoretical lineage, concepts, mechanisms, contrasting views, gap, reasoning before hypotheses, and every formal hypothesis or proposition. Do not invent hypotheses.
- Methods/data/design: preserve setting, object, sample, period, treatment and comparison groups, comparison logic, baseline and observation periods, measures, controls, model, robustness checks, and the reason for the design.
- Results/findings: preserve finding order, baseline and placebo tests, model results, coefficient direction, significance, key numbers, substantive magnitude, and support for hypotheses or expectations. Do not copy complete tables.
- Discussion/conclusion: preserve findings, theoretical relationship, policy or practical implications, mechanisms, limitations, unresolved questions, and future directions.

## Reviewer Audit

For complex, long, theoretical, or terminology-heavy manuscripts, use an independent reviewer agent when multi-agent tools are available. The reviewer must audit rather than rewrite. Provide the original PDF, `pdfmd` output, `pdftotext` structural extraction, and manuscript draft; do not provide hidden reasoning or expected findings.

Ask the reviewer to check:

- fidelity to the article's section structure;
- omitted concepts, mechanisms, distinctions, hypotheses, findings, limitations, or implications;
- terminology consistency across title, abstract, and long summary;
- preservation of source reasoning order and absence of unsupported interpretation;
- correspondence between Chinese and English condensed text;
- preservation of names, citation details, DOI, and the original English abstract.

Verify findings against the PDF before editing. Fix confirmed issues and rerun the affected validation. If no reviewer is used, perform the same audit manually and state that in the final validation summary.

## Temporary Drafts

For work spanning sections or turns, keep a task-local Markdown draft:

- In `/Users/linsheng/Projects/work-pa-wechat-posts`, use `drafts/` for resumable manuscript drafts and `tmp/<safe-title>/` for extraction and QA intermediates.
- In the legacy Social Media For Public Administration workspace, use `tmp/wechat-pa-drafts/`.

Use the same safe title rule as the Word filename. Update the draft after each completed section. If the user insists on pasted sections, request the next functional section without assuming its heading, but still require the original PDF before final delivery.

Use these prompts when they match the article's functional sequence:

- `请给我第 1 部分“引言 / 研究背景”原文。`
- `请给我第 2 部分“文献综述 / 理论与假设”原文；它不一定叫 Literature Review，请给我承担这个功能的那一部分。`
- `请给我第 3 部分“方法 / 数据与研究设计”原文。`
- `请给我第 4 部分“结果 / 发现”原文。`
- `请给我第 5 部分“讨论与结论”原文。`

Adapt the sequence to the article. Do not ask for methods or results sections that a theoretical or review article does not contain.
