import hashlib, os
from pathlib import Path
from pypdf import PdfReader

BASE = Path(r"C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge\sessions\2026-05-02\ARXIV-MIRROR-RUNBOOK")
PACKS = [
    ("siarc_umbrella_v2.0", "main.pdf"),
    ("pcf2_v1.3", "pcf2_program_statement.pdf"),
    ("ct_v1.3", "channel_theory_outline.pdf"),
    ("t2b_v3.0", "t2b_paper_draft_v5_withauthor.pdf"),
]
for name, fn in PACKS:
    p = BASE / f"arxiv_pack_{name}" / "pack" / fn
    if not p.exists():
        print(f"{name}: MISSING")
        continue
    h_sha = hashlib.sha256(); h_md = hashlib.md5()
    with open(p,'rb') as f:
        for c in iter(lambda: f.read(1<<20), b''):
            h_sha.update(c); h_md.update(c)
    pgs = len(PdfReader(str(p)).pages)
    print(f"{name}: local_sha256={h_sha.hexdigest()} local_md5={h_md.hexdigest()} size={p.stat().st_size} pages={pgs}")
