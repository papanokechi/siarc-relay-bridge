"""G17 literature extraction: pull L-equation and isomonodromic-
deformation framing from slots 04 (Wasow), 06 (Costin),
07 (Okamoto), 08 (Barhoumi-Lisovyy-Miller-Prokhorov), plus
slots 01 (Birkhoff 1930) and 03 (Birkhoff-Trjitzinsky 1933).

Strategy: pypdf full-text extraction per file; dump page-indexed
text to JSON; targeted keyword scan for canonical definitions.
"""
import json
import re
import hashlib
from pathlib import Path

LIT = Path(r"C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\tex\submitted\control center\literature\g3b_2026-05-03")
OUT = Path(r"C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge\sessions\2026-05-04\G17-LAYER-SEPARATION-LIT-ANCHOR")
OUT.mkdir(parents=True, exist_ok=True)

SLOTS = {
    "01_birkhoff_1930": "01_birkhoff_1930_acta54.pdf",
    "03_birkhoff_trjitzinsky_1933": "03_birkhoff_trjitzinsky_1933_acta60.pdf",
    "04_wasow_1965": "04_wasow_1965_dover.pdf",
    "06_costin_2008_chap5": "06_costin_2008_chap5.pdf",
    "07_okamoto_1987": "07_okamoto_1987_painleve_III_FE30.pdf",
    "08_barhoumi_lisovyy": "08_barhoumi_lisovyy_miller_prokhorov_2024_pIII_D6.pdf",
}

try:
    from pypdf import PdfReader
except ImportError:
    from PyPDF2 import PdfReader  # fallback

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

manifest = {}
for tag, fname in SLOTS.items():
    p = LIT / fname
    if not p.exists():
        manifest[tag] = {"status": "MISSING", "path": str(p)}
        continue
    try:
        reader = PdfReader(str(p))
        n = len(reader.pages)
        pages = []
        for i in range(n):
            try:
                t = reader.pages[i].extract_text() or ""
            except Exception as e:
                t = f"[EXTRACT_FAIL: {e}]"
            pages.append(t)
        out_json = OUT / f"extract_{tag}.json"
        out_json.write_text(json.dumps({
            "file": fname,
            "sha256_prefix": sha256(p)[:8],
            "n_pages": n,
            "pages": pages,
        }, ensure_ascii=False), encoding="utf-8")
        manifest[tag] = {
            "status": "OK",
            "n_pages": n,
            "sha256_prefix": sha256(p)[:8],
            "size": p.stat().st_size,
            "json": out_json.name,
        }
        print(f"OK {tag}: {n} pages -> {out_json.name}")
    except Exception as e:
        manifest[tag] = {"status": "FAIL", "error": str(e)}
        print(f"FAIL {tag}: {e}")

(OUT / "extract_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
print("\nManifest written.")
