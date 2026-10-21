"""CT-S22 Stage 0 - locate van der Put-Saito's monodromy-space / trace-coordinate
convention for the (0,0,1) row, so PREREG fixes x,y,z from the paper rather than
from my own choice.

Read-only.  Prints PDF page numbers (journal page = PDF page + 2609, established
in CT-S16 from the running heads) and the matching lines, so the hits can then be
read BY LOOKING at the rendered image, per the CT-S16 S16-17 rule.
"""
import hashlib
import pathlib
import re
import sys

import fitz

PDF = pathlib.Path(__file__).resolve().parents[1] / "refs" / "vdPS-arXiv-0902.1702v5.pdf"
assert PDF.exists(), f"missing {PDF}"

PATTERNS = [
    r"\(0,\s*0,\s*1\)",
    r"Stokes",
    r"formal monodromy",
    r"trace",
    r"x_?1\s*x_?2\s*x_?3|x1x2x3",
    r"monodromy space",
]

doc = fitz.open(PDF)
print(f"pdf pages: {doc.page_count}")
print(f"sha256(pdf): {hashlib.sha256(PDF.read_bytes()).hexdigest()}")

hits = {}
for i in range(doc.page_count):
    txt = doc[i].get_text()
    for pat in PATTERNS:
        for m in re.finditer(pat, txt, re.I):
            lo = max(0, m.start() - 90)
            hi = min(len(txt), m.end() + 90)
            frag = " ".join(txt[lo:hi].split())
            hits.setdefault(pat, []).append((i, i + 2609, frag))

for pat in PATTERNS:
    hs = hits.get(pat, [])
    pages = sorted({h[1] for h in hs})
    print(f"\n=== {pat!r}: {len(hs)} hit(s) on journal pages {pages}")
    for pdfp, jp, frag in hs[:14]:
        print(f"  [pdf {pdfp} / journal {jp}] ...{frag}...")
    if len(hs) > 14:
        print(f"  ... {len(hs) - 14} more")

doc.close()
