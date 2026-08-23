# Long-Summary and PDF Workflow

## Contents

- Source gate
- Extraction and cross-validation
- Drafting rules
- Section-specific coverage
- Reviewer audit
- Temporary drafts

## Source Gate

Classify the supplied source before extraction:

1. **PDF only:** require a readable, unencrypted PDF with a plausible page count and run the full three-stage PDF workflow.
2. **Complete OA text plus PDF:** use the OA text as the main working source. Use the PDF only to verify metadata, section boundaries, tables or figures, and interpretation-relevant numbers. Do not run all extractors unless a discrepancy remains.
3. **Pasted text without PDF:** check that the text includes the title and authors, abstract, complete body through the conclusion, and enough metadata for citation. Produce a final long summary when the text is complete and internally coherent. Request the PDF only when the text is incomplete or source-sensitive structure, notes, tables, figures, or numerical evidence remains unresolved.

State the selected source mode in the validation summary. Do not describe a pasted-text manuscript as PDF-verified.

## Extraction and Cross-Validation

For PDF-only work, use the three extractors for distinct purposes:

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

For complete OA text plus PDF, perform only targeted PDF checks. Record the source mode, checks used, and unresolved uncertainty in the final response.

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

For complex, long, theoretical, or terminology-heavy manuscripts, use an independent reviewer agent when multi-agent tools are available. The reviewer must audit rather than rewrite. Provide the available source artifacts for the selected source mode and the manuscript draft; do not provide hidden reasoning or expected findings. For PDF-only work, include the PDF, `pdfmd`, and `pdftotext` outputs. For complete OA text, include that text and only the targeted PDF evidence used.

Ask the reviewer to check:

- fidelity to the article's section structure;
- omitted concepts, mechanisms, distinctions, hypotheses, findings, limitations, or implications;
- terminology consistency across title, abstract, and long summary;
- preservation of source reasoning order and absence of unsupported interpretation;
- correspondence between Chinese and English condensed text;
- preservation of names, citation details, DOI, and the original English abstract.

Verify findings against the authoritative source for the selected mode before editing. Fix confirmed issues and rerun the affected validation. If no reviewer is used, perform the same audit manually and state that in the final validation summary.

## Temporary Drafts

For work spanning sections or turns, keep a task-local Markdown draft:

- In `/Users/linsheng/Projects/work-pa-wechat-posts`, use `drafts/` for resumable manuscript drafts and `tmp/<safe-title>/` for extraction and QA intermediates.
- In the legacy Social Media For Public Administration workspace, use `tmp/wechat-pa-drafts/`.

Use the same safe title rule as the Word filename. Update the draft after each completed section. If pasted sections are incomplete, request the next functional section without assuming its heading; request the original PDF only when completeness or source-sensitive evidence cannot otherwise be resolved.

Use these prompts when they match the article's functional sequence:

- `请给我第 1 部分“引言 / 研究背景”原文。`
- `请给我第 2 部分“文献综述 / 理论与假设”原文；它不一定叫 Literature Review，请给我承担这个功能的那一部分。`
- `请给我第 3 部分“方法 / 数据与研究设计”原文。`
- `请给我第 4 部分“结果 / 发现”原文。`
- `请给我第 5 部分“讨论与结论”原文。`

Adapt the sequence to the article. Do not ask for methods or results sections that a theoretical or review article does not contain.
