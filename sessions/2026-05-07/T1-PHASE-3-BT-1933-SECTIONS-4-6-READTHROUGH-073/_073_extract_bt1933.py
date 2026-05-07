"""073 Phase A.5: extract BT 1933 page-by-page text via pypdf.

Working artefact only (per relay 073 spec; not committed).
Outputs:
  - bt_1933_pypdf_text.txt (page-anchored linear text)
  - prints page count + extraction success rate to stdout

Usage:
  python _073_extract_bt1933.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import pypdf

BT_PDF = Path("tex/submitted/control center/literature/g3b_2026-05-03/03_birkhoff_trjitzinsky_1933_acta60.pdf")
OUT_TXT = Path("siarc-relay-bridge/sessions/2026-05-07/T1-PHASE-3-BT-1933-SECTIONS-4-6-READTHROUGH-073/bt_1933_pypdf_text.txt")


def main() -> int:
    if not BT_PDF.exists():
        print(f"ERROR: BT PDF not found at {BT_PDF}", file=sys.stderr)
        return 1
    OUT_TXT.parent.mkdir(parents=True, exist_ok=True)

    reader = pypdf.PdfReader(str(BT_PDF))
    n = len(reader.pages)
    empty_pages: list[int] = []
    char_counts: list[int] = []

    with OUT_TXT.open("w", encoding="utf-8") as fh:
        fh.write(f"# BT 1933 pypdf text extraction (Phase A.5)\n")
        fh.write(f"# Source: {BT_PDF}\n")
        fh.write(f"# Total pages (PDF): {n}\n")
        fh.write(f"# pypdf version: {pypdf.__version__}\n")
        fh.write(f"# Page anchors: '====== PDF PAGE NN ======' separator lines\n")
        fh.write(f"# (PDF page index is 1-based here; physical paper page may differ\n")
        fh.write(f"#  per BT 1933 paginated to Acta 60 pp. 1-89.)\n\n")
        for i in range(n):
            try:
                txt = reader.pages[i].extract_text() or ""
            except Exception as e:  # pragma: no cover
                txt = ""
                print(f"  page {i+1}: extract_text raised {e!r}", file=sys.stderr)
            char_counts.append(len(txt))
            if not txt.strip():
                empty_pages.append(i + 1)
            fh.write(f"\n====== PDF PAGE {i+1:03d} ======\n")
            fh.write(txt)
            fh.write("\n")

    print(f"BT 1933 PDF total pages: {n}")
    print(f"Pages with non-empty extraction: {n - len(empty_pages)}")
    print(f"Pages with empty extraction: {len(empty_pages)}")
    if empty_pages:
        print(f"  empty page numbers: {empty_pages}")
    print(f"Total extracted characters: {sum(char_counts)}")
    print(f"Mean chars/page: {sum(char_counts) / max(n, 1):.1f}")
    print(f"Min chars/page: {min(char_counts) if char_counts else 0}")
    print(f"Max chars/page: {max(char_counts) if char_counts else 0}")
    print(f"Output: {OUT_TXT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
