"""Extract text from Wasow chap X and Birkhoff 1930 PDFs for Phase C.1/C.2."""
from pypdf import PdfReader
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]  # workspace root
LIT  = ROOT / "tex" / "submitted" / "control center" / "literature" / "g3b_2026-05-03"
OUT  = Path(__file__).parent

for name, alias in [("wasow_1965_chap_X.pdf", "wasow.txt"),
                    ("birkhoff_1930.pdf",      "birkhoff.txt")]:
    pdf = LIT / name
    r = PdfReader(str(pdf))
    out = OUT / alias
    with out.open("w", encoding="utf-8") as f:
        for i, p in enumerate(r.pages):
            f.write(f"\n===== PAGE {i+1} =====\n")
            t = p.extract_text() or "<empty>"
            f.write(t)
            f.write("\n")
    print(f"WROTE {out} ({len(r.pages)} pages)")
