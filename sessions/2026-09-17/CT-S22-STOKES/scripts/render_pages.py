"""CT-S22 Stage 0 - render the pages carrying the (0,0,1) monodromy space so they
can be read BY LOOKING (CT-S16 S16-17: the text layer of this PDF mangles
matrices, and an image that never displayed must not be quoted).

Journal page = PDF page + 2609.
"""
import hashlib
import pathlib

import fitz

ROOT = pathlib.Path(__file__).resolve().parents[1]
PDF = ROOT / "refs" / "vdPS-arXiv-0902.1702v5.pdf"
OUT = ROOT / "pages"
OUT.mkdir(exist_ok=True)

WANT = [20, 21, 22]  # journal 2629, 2630, 2631

doc = fitz.open(PDF)
for i in WANT:
    pix = doc[i].get_pixmap(dpi=200)
    path = OUT / f"vdps_p{i + 2609}.png"
    pix.save(path)
    b = path.read_bytes()
    print(f"journal {i + 2609}  pdf {i}  ->  {path.name}  "
          f"{len(b)} B  sha256 {hashlib.sha256(b).hexdigest()[:16]}")
doc.close()
print("rendered", len(WANT), "page(s)")
