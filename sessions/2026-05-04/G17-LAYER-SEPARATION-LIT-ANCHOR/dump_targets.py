"""Pull targeted page text for verbatim quotes."""
import json
from pathlib import Path

OUT = Path(r"C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge\sessions\2026-05-04\G17-LAYER-SEPARATION-LIT-ANCHOR")

TARGETS = {
    "01_birkhoff_1930": [0, 1, 2, 3, 4, 5, 23],
    "03_birkhoff_trjitzinsky_1933": [0, 1, 2, 3, 4, 51, 88],
    "06_costin_2008_chap5": [0, 1, 2, 3, 4, 5, 6, 7, 8, 51, 254],
    "07_okamoto_1987": [0, 1, 2, 3, 4, 26, 27],
    "08_barhoumi_lisovyy": [0, 1, 2, 3, 4, 5, 6, 23, 24, 25, 76],
}

for tag, idxs in TARGETS.items():
    data = json.loads((OUT / f"extract_{tag}.json").read_text(encoding="utf-8"))
    print(f"\n{'='*70}\n{tag}  ({data['file']})  sha256[:8]={data['sha256_prefix']}\n{'='*70}")
    for i in idxs:
        if i >= data["n_pages"]:
            continue
        text = data["pages"][i]
        if not text.strip():
            print(f"\n--- page_idx {i}: EMPTY ---")
            continue
        # Show first 1200 chars
        print(f"\n--- page_idx {i} (len={len(text)}) ---")
        print(text[:1200])
