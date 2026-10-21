"""Print short locating snippets (NOT for quotation) to choose which pages to
render as images. Every quoted statement is later read from the image."""
import re
import fitz

PDF = r"..\CT-R1-AUDIT\refs\vanderPut-Saito-AIF-2009-59-7-2611.pdf"
doc = fitz.open(PDF)

WANT = [24, 26, 27, 31, 32, 41, 42, 45, 46, 47, 48]
KEYS = ["foliation", "isomonodrom", "resonan", "irreducib", "moduli", "Painlev"]

for p in WANT:
    txt = doc[p - 1].get_text()
    flat = re.sub(r"\s+", " ", txt)
    print(f"\n===== PDF p.{p}  (journal p.{2610 + p}) =====")
    for k in KEYS:
        for m in re.finditer(k, flat, re.I):
            a = max(0, m.start() - 110)
            print(f"  [{k}] ...{flat[a:m.start() + 150]}...")
            break
