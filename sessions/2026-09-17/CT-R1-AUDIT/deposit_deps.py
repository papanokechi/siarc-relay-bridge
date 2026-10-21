"""Deposit dependency audit for the companion v1.3 notice.

Operator ruling: list every claim the notice depends on and confirm each is
`cold`, or INSPECTED from page images. The mapping from notice item to claim ids
is curated here; the STATUS COLUMNS ARE PULLED FROM THE CORPUS so they cannot
drift from the record.
"""
import json
import glob
import os
from pathlib import Path

ROOT = Path(r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17")

DEPS = {
    "C1 — Remark 2.2 is false (the lemma)": [
        "R1-18", "R1-43", "step-4-log", "c-independence", "sympy-examples",
        "S6-C13", "S6-C14", "S6-C17",
    ],
    "C2 — the PV parameter contradiction": [
        "R1-65", "R1-64", "R1-31", "R1-32", "R1-29", "R1-30", "R1-34",
        "CT-S12-COLDREAD4-Q1-DICT", "CT-S12-COLDREAD4-Q1-EIGEN",
        "CT-S12-COLDREAD4-Q3-C4C5", "CT-S12-COLDREAD4-Q4-C6",
        "CT-S9-PVPARAMS-C003",
    ],
    "C3 — not well-posed as isomonodromy": [
        "R1-33", "CT-S12-COLDREAD4-Q5-C7", "CT-S9-PVPARAMS-C014",
    ],
    "C4 — per-object surface labels": [
        "R1-52", "R1-53", "R1-54", "R1-55", "R1-56", "R1-57",
        "R1-06", "R1-07", "S4-05", "S4-06", "S5B-C4", "S5B-C5", "S5B-C6",
        "S6-C9", "S6-C10", "A4-table", "A5-table",
    ],
    "C5 — downstream passages in v1.2": [
        "R1-66", "R1-63",
    ],
}

rec = {}
for f in glob.glob(str(ROOT / "*" / "claims.jsonl")):
    sess = os.path.basename(os.path.dirname(f))
    for l in open(f, encoding="utf-8"):
        if l.strip():
            r = json.loads(l)
            rec[r["claim_id"]] = (sess, r)

# A claim clears the gate if it is cold-reviewed, or INSPECTED (a file/page fact).
def verdict(r):
    if r.get("review") == "cold":
        return "PASS (cold)"
    if r.get("label") == "INSPECTED":
        return "PASS (INSPECTED)"
    if r.get("label") in ("PROVEN", "VERIFIED", "STRUCTURAL"):
        return "REVIEW — " + (r.get("review") or "no review field")
    return "REVIEW"


lines = []
missing, flagged = [], []
for item, ids in DEPS.items():
    lines.append("\n### " + item + "\n")
    lines.append("| Claim | Session | Label | Review | Gate verdict |")
    lines.append("|---|---|---|---|---|")
    for cid in ids:
        if cid not in rec:
            missing.append(cid)
            lines.append(f"| `{cid}` | **NOT FOUND** | — | — | **MISSING** |")
            continue
        sess, r = rec[cid]
        v = verdict(r)
        if v.startswith("REVIEW"):
            flagged.append((item, cid, r.get("label"), r.get("review")))
        lines.append(f"| `{cid}` | {sess} | {r.get('label')} | {r.get('review') or '—'} | {v} |")

print("\n".join(lines))
print("\n\n=== MISSING:", missing or "none")
print("=== FLAGGED (not cold, not INSPECTED):", len(flagged))
for item, cid, lab, rev in flagged:
    print(f"   {cid:32} {lab:12} review={rev}   [{item}]")

Path(ROOT / "CT-R1-AUDIT" / "_deps_table.md").write_text("\n".join(lines), encoding="utf-8")
