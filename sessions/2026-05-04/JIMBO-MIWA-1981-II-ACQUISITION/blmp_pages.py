"""Read full text of BLMP 2024 pages 24, 25, 26 (sec 4.1 Lax pair) and last refs page."""
from pypdf import PdfReader
pdf_path = r"C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\tex\submitted\control center\literature\g3b_2026-05-03\08_barhoumi_lisovyy_miller_prokhorov_2024_pIII_D6.pdf"
r = PdfReader(pdf_path)
for idx in [23, 24, 25, 26, 70, 71, 72, 73, 74, 75, 76]:
    if idx < len(r.pages):
        t = r.pages[idx].extract_text() or ""
        print(f"\n========== PAGE {idx+1} ==========")
        print(t)
