"""Locate candidate pages in van der Put-Saito for step 1 of CT-S16.

IMPORTANT: the text layer is used ONLY to find page numbers. Every load-bearing
statement is afterwards read from a rendered page image, per the P0 rule.
"""
import fitz

PDF = r"..\CT-R1-AUDIT\refs\vanderPut-Saito-AIF-2009-59-7-2611.pdf"
doc = fitz.open(PDF)
print(f"pages: {doc.page_count}")

TERMS = [
    "moduli space",
    "isomonodrom",
    "foliation",
    "Painlev\u00e9 V",
    "PV",
    "family of",
    "semisimple",
    "resonan",
    "irreducib",
    "unipotent",
    "logarithm",
    "Riemann-Hilbert",
    "Riemann\u2013Hilbert",
    "(0,0,1)",
    "0,0,1",
]

hits = {t: [] for t in TERMS}
for i in range(doc.page_count):
    txt = doc[i].get_text()
    low = txt.lower()
    for t in TERMS:
        if t.lower() in low:
            hits[t].append(i + 1)  # 1-based PDF page index

for t in TERMS:
    pages = hits[t]
    shown = pages[:25]
    print(f"\n{t!r}: {len(pages)} pages")
    print("   ", shown, ("..." if len(pages) > 25 else ""))
