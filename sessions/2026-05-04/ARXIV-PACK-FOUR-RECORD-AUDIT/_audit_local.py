"""Local PDF audit: SHA-256, MD5, page count for each cached zenodo.pdf
   and rebuilt local PDF in pack/. Compare to Zenodo API md5 and expected page count.
"""
import hashlib, json, os, sys
from pathlib import Path
try:
    from pypdf import PdfReader
except ImportError:
    from PyPDF2 import PdfReader  # fallback

BASE = Path(r"C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge\sessions\2026-05-02\ARXIV-MIRROR-RUNBOOK")

PACKS = [
    {"name":"siarc_umbrella_v2.0","record":"19965041","pdf":"main.pdf",
     "api_md5":"d633699fbfe698dae08d510e8e165320","api_size":455178,"expected_pages":12},
    {"name":"pcf2_v1.3","record":"19963298","pdf":"pcf2_program_statement.pdf",
     "api_md5":"cdd628911f3fd95cec8ed916c1958c51","api_size":558153,"expected_pages":22},
    {"name":"ct_v1.3","record":"19972394","pdf":"channel_theory_outline.pdf",
     "api_md5":"e58951de5cbf1be7cdd26f335bc359af","api_size":581459,"expected_pages":17},
    {"name":"t2b_v3.0","record":"19915689","pdf":"t2b_paper_draft_v5_withauthor.pdf",
     "api_md5":"d245be3b2b60cf04c5210f3859ad7394","api_size":331769,"expected_pages":8},
]

def hashes(p):
    h_sha = hashlib.sha256(); h_md = hashlib.md5()
    with open(p,'rb') as f:
        for chunk in iter(lambda: f.read(1<<20), b''):
            h_sha.update(chunk); h_md.update(chunk)
    return h_sha.hexdigest(), h_md.hexdigest(), os.path.getsize(p)

def pages(p):
    try: return len(PdfReader(str(p)).pages)
    except Exception as e: return f"ERR:{e}"

results = []
for p in PACKS:
    pack_dir = BASE / f"arxiv_pack_{p['name']}"
    zpdf = pack_dir / "zenodo.pdf"
    lpdf = pack_dir / "pack" / p["name"] / p["pdf"]
    rec = {"name": p["name"], "record": p["record"]}
    if zpdf.exists():
        sha, md5, size = hashes(zpdf)
        rec["zenodo_pdf"] = {"sha256": sha, "md5": md5, "size": size,
                             "pages": pages(zpdf),
                             "md5_match_api": md5 == p["api_md5"],
                             "size_match_api": size == p["api_size"]}
    else:
        rec["zenodo_pdf"] = {"missing": True}
    if lpdf.exists():
        sha, md5, size = hashes(lpdf)
        rec["local_pdf"] = {"path": str(lpdf.relative_to(BASE)), "sha256": sha, "md5": md5,
                            "size": size, "pages": pages(lpdf)}
    else:
        # try alternative locations
        candidates = list((pack_dir/"pack").rglob("*.pdf"))
        rec["local_pdf"] = {"missing": True, "rglob_pdfs": [str(c.relative_to(BASE)) for c in candidates]}
    rec["expected_pages"] = p["expected_pages"]
    results.append(rec)

print(json.dumps(results, indent=2))
out = Path(r"C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge\sessions\2026-05-04\ARXIV-PACK-FOUR-RECORD-AUDIT\local_pdf_audit.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(results, indent=2))
