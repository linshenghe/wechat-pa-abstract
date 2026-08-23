#!/usr/bin/env python3
"""Run the deterministic final checks for a WeChat PA manuscript."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from docx import Document

from build_docx import REQUIRED_FIELDS, load_long_summary_blocks
from validate_docx import validate_docx


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--docx", required=True, type=Path)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--cover", required=True, type=Path)
    parser.add_argument("--long-summary", type=Path)
    parser.add_argument("--word-pages", required=True, type=int)
    parser.add_argument("--word-words", required=True, type=int)
    return parser.parse_args()


def word_lock_path(docx_path: Path) -> Path:
    return docx_path.with_name(f"~${docx_path.name[2:]}")


def main() -> None:
    args = parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    document_type = str(data.get("document_type", "short")).strip().lower()
    expected = {field: str(data.get(field, "")).strip() for field in REQUIRED_FIELDS}
    intro = f'今天为大家带来的是{expected["authors"]}的研究：《{expected["chinese_title"]}》。'
    expected_opening = [
        expected["english_title"],
        expected["chinese_title"],
        intro,
        "摘要：",
        expected["chinese_abstract"],
        expected["english_abstract"],
        "Citation:",
        expected["citation"],
    ]

    base_result = validate_docx(args.docx, args.input, args.cover)
    document = Document(args.docx)
    nonempty = [paragraph.text for paragraph in document.paragraphs if paragraph.text]
    lock_path = word_lock_path(args.docx)

    checks = dict(base_result["checks"])
    checks["fixed_block_order"] = nonempty[:8] == expected_opening
    checks["file_nonempty"] = args.docx.is_file() and args.docx.stat().st_size > 0
    checks["word_lock_absent"] = not lock_path.exists()

    if document_type == "long":
        if args.long_summary is None:
            raise ValueError("--long-summary is required for document_type=long")
        expected_long = load_long_summary_blocks(args.long_summary)
        checks["markdown_word_alignment"] = nonempty[8:] == ["长摘要："] + expected_long
    else:
        if args.long_summary is not None:
            raise ValueError("--long-summary requires document_type=long")
        checks["markdown_word_alignment"] = True

    checks["word_page_count"] = args.word_pages > 0
    checks["word_word_count"] = args.word_words > 0

    result = {
        "ok": all(checks.values()),
        "checks": checks,
        "metrics": {
            "docx_bytes": args.docx.stat().st_size if args.docx.exists() else 0,
            "word_pages": args.word_pages,
            "word_words": args.word_words,
        },
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))
    if not result["ok"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
