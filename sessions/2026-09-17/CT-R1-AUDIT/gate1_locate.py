"""Gate 1: locate the pages of companion v1.2 holding Remark 2.2 and Conjecture 4.1,
then render them at 3x for reading as page images (P0 citation rule: load-bearing
statements are read from page images, not from the OCR/text layer).

Text extraction here is used ONLY to find the pages. Every quoted string is then
confirmed against the rendered image.
"""
import hashlib
from pathlib import Path
import fitz

D = Path(r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17\CT-R1-AUDIT")
PDF = D / "refs" / "vquad_resurgence_v1.2_zenodo-20481592.pdf"
OUT = D / "coldpackets"


def norm(s):
    return s.replace(chr(0xFB01), "fi").replace(chr(0xFB02), "fl")


print("pdf :", PDF.name)
print("sha256:", hashlib.sha256(PDF.read_bytes()).hexdigest())

doc = fitz.open(PDF)
print("pages:", doc.page_count)

targets = ["Remark 2.2", "Conjecture 4.1", "Remark 2.", "Conjecture 4."]
hits = {}
for i in range(doc.page_count):
    t = norm(doc[i].get_text())
    for s in targets:
        if s in t:
            hits.setdefault(s, []).append(i)

for s in targets:
    print(f"{s!r:18} -> pdf indices {hits.get(s)}")

pages = sorted({i for s in ("Remark 2.2", "Conjecture 4.1") for i in hits.get(s, [])})
print("rendering pdf indices:", pages)
for i in pages:
    p = OUT / f"companion_v12_p{i}.png"
    doc[i].get_pixmap(matrix=fitz.Matrix(3, 3)).save(p)
    print("  wrote", p.name, hashlib.sha256(p.read_bytes()).hexdigest()[:16])

# Dump the surrounding text of each hit so I know what to look for on the image.
for i in pages:
    t = norm(doc[i].get_text())
    print("\n" + "=" * 70, "\nPDF INDEX", i, "\n" + "=" * 70)
    for key in ("Remark 2.2", "Conjecture 4.1"):
        k = t.find(key)
        while k != -1:
            print(f"\n--- context for {key} ---")
            print(t[max(0, k - 400): k + 1400])
            k = t.find(key, k + 1)
