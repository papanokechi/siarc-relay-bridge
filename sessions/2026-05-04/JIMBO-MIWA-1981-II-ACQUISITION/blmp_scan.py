"""Extract BLMP 2024 (slot 08) text to scan for Jimbo-Miwa 1981 II references and parameter labeling."""
from pypdf import PdfReader
import re, sys

pdf_path = r"C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\tex\submitted\control center\literature\g3b_2026-05-03\08_barhoumi_lisovyy_miller_prokhorov_2024_pIII_D6.pdf"
r = PdfReader(pdf_path)
pages_text = []
for i, p in enumerate(r.pages):
    try:
        t = p.extract_text() or ""
    except Exception:
        t = ""
    pages_text.append(t)

# Patterns to scan for
patterns = [
    r"Jimbo",
    r"alpha[_ ]?\\?infty",
    r"\\Theta_\\infty|\\Theta_0",
    r"alpha_?0",
    r"beta_?\\?infty",
    r"beta_?0",
    r"\\theta",
    r"Lax\s*pair",
    r"isomonodromic",
    r"4-tuple|four[- ]parameter|four\s*parameters",
    r"after\s+Jimbo",
    r"\(1/6",
    r"D_6|D6|D-six",
    r"resonance",
]

print("=" * 80)
print(f"BLMP 2024 slot 08 SHA: 96C49CDD... pages: {len(pages_text)}")
print("=" * 80)
for i, t in enumerate(pages_text):
    hits = []
    for pat in patterns:
        for m in re.finditer(pat, t, re.IGNORECASE):
            start = max(0, m.start() - 80)
            end = min(len(t), m.end() + 80)
            snippet = t[start:end].replace("\n", " ")
            hits.append((pat, snippet))
    if hits:
        print(f"\n--- Page {i+1} ---")
        seen = set()
        for pat, snip in hits[:8]:
            key = snip[:120]
            if key in seen:
                continue
            seen.add(key)
            print(f"  [{pat}] ...{snip[:280]}...")
