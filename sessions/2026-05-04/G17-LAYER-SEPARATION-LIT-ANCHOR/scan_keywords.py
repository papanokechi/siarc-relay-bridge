"""G17 keyword scan: locate canonical L-equation and isomonodromic-
deformation framing across the extracted JSONs. Emits keyword_hits.json
with (slot, page_idx, snippet)."""
import json
import re
from pathlib import Path

OUT = Path(r"C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge\sessions\2026-05-04\G17-LAYER-SEPARATION-LIT-ANCHOR")

# Patterns relevant to L-equation framing (linear ODE / formal series / wave function)
PAT_L_EQ = [
    r"linear\s+(?:ordinary\s+)?differential\s+equation",
    r"formal\s+(?:power\s+)?series\s+solution",
    r"formal\s+solution",
    r"asymptotic\s+(?:series|expansion|solution)",
    r"sectorial",
    r"Borel\s+(?:sum|summability|summable|transform)",
    r"Stokes\s+(?:phenomenon|line|multiplier|matrix|matrices|constant|data)",
    r"irregular\s+singular(?:ity|\s+point)",
    r"wave\s+function",
    r"resurgent",
]
# Patterns relevant to isomonodromic-deformation framing
PAT_ISO = [
    r"isomonodrom\w*",
    r"monodromy(?:-|\s+)preserving",
    r"Lax\s+pair",
    r"Riemann.Hilbert",
    r"Hamiltonian\s+(?:system|formulation|form)",
    r"compatibility\s+condition",
    r"deformation\s+(?:equation|parameter)",
    r"connection\s+(?:matrix|matrices|problem)",
    r"affine\s+Weyl",
    r"surface\s+of\s+initial",
    r"\bP\s*_*\s*III\b|Painlev[eé]\s+III",
    r"D_?6|D\(6\)|D\^\(1\)_?6",
]

ALL_PATS = [("L", p) for p in PAT_L_EQ] + [("I", p) for p in PAT_ISO]

def scan_file(json_path, max_hits_per_pat=4):
    data = json.loads(json_path.read_text(encoding="utf-8"))
    pages = data["pages"]
    hits = {}
    for kind, pat in ALL_PATS:
        rgx = re.compile(pat, re.IGNORECASE)
        plist = []
        for i, page in enumerate(pages):
            for m in rgx.finditer(page):
                start = max(0, m.start() - 220)
                end = min(len(page), m.end() + 220)
                snip = page[start:end].replace("\n", " ").replace("  ", " ")
                plist.append({"page_idx": i, "match": m.group(0), "snip": snip})
                if len(plist) >= max_hits_per_pat:
                    break
            if len(plist) >= max_hits_per_pat:
                break
        if plist:
            hits[f"{kind}::{pat}"] = plist
    return {"file": data["file"], "sha256_prefix": data["sha256_prefix"], "hits": hits}

result = {}
for jf in sorted(OUT.glob("extract_*.json")):
    if "manifest" in jf.name:
        continue
    tag = jf.stem.replace("extract_", "")
    print(f"Scanning {tag} ...")
    result[tag] = scan_file(jf)

(OUT / "keyword_hits.json").write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

# Summary print
for tag, r in result.items():
    print(f"\n=== {tag} ({r['file']}) ===")
    for k, v in r["hits"].items():
        print(f"  {k}: {len(v)} hits (e.g., page {v[0]['page_idx']})")
