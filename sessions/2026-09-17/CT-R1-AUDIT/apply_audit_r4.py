"""
CT-R1-AUDIT R4: record the outcome of gate 1 (the CT-S7-COLDREAD cold review).

Verdicts returned by CT-S7:
  thm:radius Step 3 (multinomial sandwich)  -> SOUND
  thm:growth Step 3 / G1                    -> ERROR (DLMF equation misquoted)

The error was independently confirmed against dlmf.nist.gov and repaired in
theorem.tex, which recompiles clean at 7 pages.
"""
import json
from pathlib import Path

ROOT = Path(r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17")
S1 = ROOT / "CT-S1-THEOREM" / "claims.jsonl"
AUDIT = ROOT / "CT-R1-AUDIT" / "claims.jsonl"

COLD_OK = ("Gate 1 (operator review #3): COLD-READ by CT-S7-COLDREAD, which read theorem.tex alone "
           "with no access to CT-R1-AUDIT or any REPORT.md. Verdict SOUND: the multinomial-sandwich "
           "argument of thm:radius Step 3, including the exchange-argument maximality sub-lemma "
           "added in round R1, is complete and correct as written.")

COLD_ERR = ("Gate 1 (operator review #3): COLD-READ by CT-S7-COLDREAD returned verdict ERROR on "
            "thm:growth Step 3 / G1 -- DLMF (5.11.12) was misquoted as the full G_k expansion. "
            "Independently confirmed against dlmf.nist.gov (page sha256 "
            "929045c7b1cd72f35e8d6e2c966340e30d2c3b990245d44e42f5de8c1caea28e): 5.11.12 is the plain "
            "ratio Gamma(z+a)/Gamma(z+b) ~ z^(a-b); the G_k expansion is 5.11.13 and G_0(a,b)=1 is "
            "5.11.15. REPAIRED in theorem.tex at five sites; the document recompiles clean at 7 pages. "
            "The mathematical content is unaffected -- 5.11.12 alone is exactly what the proof needs -- "
            "but the REPAIR HAS NOT ITSELF BEEN COLD-READ, so review stays 'self'.")

updates = {"S1-03": ("cold", COLD_OK), "S1-04": ("self", COLD_ERR)}

rows = [json.loads(l) for l in S1.read_text(encoding="utf-8").splitlines() if l.strip()]
for r in rows:
    if r["claim_id"] in updates:
        rev, note = updates[r["claim_id"]]
        r["review"] = rev
        r["audit_r4"] = note
S1.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n", encoding="utf-8")

NEW = [
    ("R1-26",
     "Gate 1 partial result: CT-S7-COLDREAD, reading theorem.tex alone without its derivation "
     "history, returned SOUND on thm:radius Step 3 (the multinomial sandwich and its exchange-argument "
     "maximality sub-lemma). Claim S1-03 is therefore the first claim in the corpus to reach "
     "review='cold'.", "INSPECTED", "file_inspection"),
    ("R1-27",
     "Gate 1 found a real defect: DLMF (5.11.12) was misquoted in theorem.tex as the full G_k "
     "expansion. Verified independently against dlmf.nist.gov: (5.11.12) is Gamma(z+a)/Gamma(z+b) ~ "
     "z^(a-b) for |ph z| <= pi - delta; the expansion with G_k(a,b) is (5.11.13); G_0(a,b)=1 is "
     "(5.11.15). The proof only ever needed (5.11.12), so the mathematics is unaffected and the "
     "citation was corrected at five sites in theorem.tex; the document recompiles clean at 7 pages.",
     "INSPECTED", "file_inspection"),
    ("R1-28",
     "Gate 1 is NOT yet closed. thm:radius Step 3 is cold-read SOUND, but the repaired DLMF passage "
     "in thm:growth Step 3 has not itself been cold-read, so claim S1-04 remains review='self' and is "
     "not deposit-eligible. A re-read of the repaired passage is required before deposit.",
     "INSPECTED", "file_inspection"),
]
with AUDIT.open("a", encoding="utf-8") as f:
    for cid, claim, label, ev in NEW:
        f.write(json.dumps({
            "claim_id": cid, "task_id": "CT-R1-AUDIT-R4-GATE1", "claim": claim, "label": label,
            "evidence_type": ev, "dps": None, "reproducible": True,
            "script": "sessions/2026-09-17/CT-R1-AUDIT/apply_audit_r4.py", "output_hash": None,
        }, ensure_ascii=False) + "\n")

import collections
lab, rev, bad = collections.Counter(), collections.Counter(), []
for p in ROOT.glob("*/claims.jsonl"):
    for l in p.read_text(encoding="utf-8").splitlines():
        if not l.strip():
            continue
        r = json.loads(l)
        lab[r.get("label")] += 1
        if r.get("evidence_type") == "proof":
            rev[r.get("review")] += 1
        if r.get("evidence_type") == "file_inspection" and r.get("label") == "PROVEN":
            bad.append(r["claim_id"])
print("corpus labels:", dict(lab))
print("proof-claim review states:", dict(rev))
print("rule 1(a) violations:", bad or "none")
print("deposit-eligible proof claims (cold|lean):", rev.get("cold", 0) + rev.get("lean", 0))
