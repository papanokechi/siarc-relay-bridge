"""Render the CT-S16 step-1 pages as images for direct reading.

P0: a load-bearing statement is read by LOOKING at the rendered page. OCR is a
text layer and does not satisfy the rule.

Journal page = PDF page + 2609 (verified from the running headers).
"""
import fitz

PDF = r"..\CT-R1-AUDIT\refs\vanderPut-Saito-AIF-2009-59-7-2611.pdf"
OFFSET = 2609
WANT = [26, 28, 29, 30, 42, 45, 46, 47]

doc = fitz.open(PDF)
mat = fitz.Matrix(3.0, 3.0)
for p in WANT:
    page = doc[p - 1]
    pix = page.get_pixmap(matrix=mat)
    out = f"pages\\vdps_p{OFFSET + p}.png"
    pix.save(out)
    print(f"PDF p.{p} -> journal p.{OFFSET + p}  {out}  {pix.width}x{pix.height}")
