"""Repair a defect in this session's own AEAL record.

The R8 batch was numbered R1-44..R1-51, but R1-44..R1-49 were already in use by
the R7 batch. Six claim_ids therefore collided, which breaks the traceability
the AEAL record exists to provide. The R8 occurrences are renumbered to
R1-61..R1-66 (R1-60 was the previous maximum); R1-50 and R1-51 were unique and
are left alone. Cross-references in the prose files are updated to match.
"""
import json
import re
from pathlib import Path

D = Path(r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17\CT-R1-AUDIT")
MAP = {"R1-44": "R1-61", "R1-45": "R1-62", "R1-46": "R1-63",
       "R1-47": "R1-64", "R1-48": "R1-65", "R1-49": "R1-66"}

cl = D / "claims.jsonl"
rows = [json.loads(l) for l in cl.read_text(encoding="utf-8").splitlines() if l.strip()]
n = 0
for r in rows:
    if r.get("task_id") == "CT-R1-AUDIT-R8" and r["claim_id"] in MAP:
        old = r["claim_id"]
        r["claim_id"] = MAP[old]
        r["renumbered_from"] = old
        r["renumber_note"] = ("Renumbered during R9. The R8 batch collided with six R7 claim_ids; "
                              "the R7 occurrences keep the original numbers and these R8 "
                              "occurrences were moved to free numbers. No claim content changed.")
        n += 1
cl.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in rows) + "\n", encoding="utf-8")
print("renumbered", n, "claims")

# Cross-references: only the R8/R9 sections of the prose files refer to these as the
# gate-1 / author-request claims. Rewrite the explicit table rows.
PROSE = {
    "REPORT.md": [
        ("| R1-44 | INSPECTED | self | Wong-Li title defect", "| R1-61 | INSPECTED | self | Wong-Li title defect"),
        ("| R1-45 | INSPECTED | self | Identity block", "| R1-62 | INSPECTED | self | Identity block"),
        ("| R1-46 | INSPECTED | self | Gate 1: all 11", "| R1-63 | INSPECTED | self | Gate 1: all 11"),
        ("| R1-47 | INSPECTED | self | v1.2 itself states", "| R1-64 | INSPECTED | self | v1.2 itself states"),
        ("| R1-48 | PROVEN | self |", "| R1-65 | PROVEN | self |"),
        ("| R1-49 | INSPECTED | self | Five downstream", "| R1-66 | INSPECTED | self | Five downstream"),
        ("| R1-50 | INSPECTED | self | Gate 3", "| R1-50 | INSPECTED | self | Gate 3"),
    ],
}
for fn, subs in PROSE.items():
    p = D / fn
    t = p.read_text(encoding="utf-8")
    before = t
    for a, b in subs:
        t = t.replace(a, b)
    if t != before:
        p.write_text(t, encoding="utf-8")
        print("updated cross-references in", fn)

# Re-check uniqueness across the whole session tree.
import glob
seen = {}
dups = []
for f in glob.glob(str(D.parent / "*" / "claims.jsonl")):
    for l in open(f, encoding="utf-8"):
        if not l.strip():
            continue
        cid = json.loads(l)["claim_id"]
        if cid in seen:
            dups.append(cid)
        seen[cid] = f
print("total claim_ids:", len(seen))
print("remaining duplicates:", sorted(set(dups)) or "NONE")
