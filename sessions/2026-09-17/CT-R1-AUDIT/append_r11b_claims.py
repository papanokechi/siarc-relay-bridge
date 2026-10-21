"""R11b: repair the three claims that append_r11_claims.py silently dropped.

append_r11_claims.py deduplicated by claim_id and skipped anything already
present. R1-71/72/73 had already been used in round R10, so three genuinely new
claims -- the ones carrying the central CT-S14 result -- were discarded without
an error. This script re-appends them under fresh IDs and ABORTS on any
collision rather than skipping, which is what the first script should have done.
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
CJ = HERE / "claims.jsonl"


def sha(p):
    p = pathlib.Path(p)
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None


OUT = sha(HERE / "verify_s14.out.txt")
ROOTS = sha(HERE / "verify_roots.out.txt")

NEW = [
    dict(claim_id="R1-82", task_id="R11-S14",
         claim="Object B's trace-free normal form, pulled back by z=1/x, is EXACTLY equal to the "
               "trace-free normal potential of companion v1.2's printed ODE: both equal "
               "(12x^4+4x^3+4x^2+11)/(4(3x^2+x+1)^2). Symbolic difference is identically zero. "
               "Objects B and C are therefore the same object in different presentations.",
         label="PROVEN", evidence_type="computation", dps=None, reproducible=True,
         script="verify_s14.py", output_hash=OUT,
         review="cold", review_note="CT-S14-COLDREAD-B derived this independently under isolation; "
                                    "re-derived here from the primary printed data in different code."),
    dict(claim_id="R1-83", task_id="R11-S14",
         claim="Under z=1/x the pullback's first-order term 2/x contributes nothing to the normal "
               "potential, since (2/x)^2/4 + d/dx(2/x)/2 = 1/x^2 - 1/x^2 = 0. Hence inversion ALONE "
               "reaches object B's trace-free normal form; no twist is required for its Table 2.1 row.",
         label="PROVEN", evidence_type="computation", dps=None, reproducible=True,
         script="verify_s14.py", output_hash=OUT,
         review="cold", review_note="implicit in CT-S14 task 2; verified explicitly here."),
    dict(claim_id="R1-84", task_id="R11-S14",
         claim="The inversion x=1/z carries object B's finite singular points (-1 +/- i*sqrt(11))/2 "
               "exactly onto the companion operator's (-1 +/- i*sqrt(11))/6, resolving the "
               "previously unexplained /2 vs /6 discrepancy between the two objects.",
         label="PROVEN", evidence_type="computation", dps=None, reproducible=True,
         script="verify_roots.out.txt", output_hash=ROOTS,
         review="cold", review_note="elementwise check; an earlier set comparison printed False as a "
                                    "SymPy hashing artefact on unevaluated radicals, recorded in VERIFY-S14.md."),
    dict(claim_id="R1-85", task_id="R11-PROCESS",
         claim="PROCESS DEFECT, self-reported: append_r11_claims.py deduplicated by claim_id and "
               "silently skipped 3 of 11 claims whose IDs (R1-71/72/73) had been used in round R10. "
               "The dropped claims were the central CT-S14 results. Detected only because the script "
               "printed a count. Append scripts must ABORT on collision, never skip.",
         label="INSPECTED", evidence_type="file_inspection", dps=None, reproducible=True,
         script="append_r11b_claims.py", output_hash=None,
         review="self", review_note="self-reported defect in this session's own tooling."),
]

rec = {}
for line in CJ.read_text(encoding="utf-8").splitlines():
    if line.strip():
        c = json.loads(line)
        rec[c["claim_id"]] = c

collide = [c["claim_id"] for c in NEW if c["claim_id"] in rec]
if collide:
    sys.exit(f"ABORT: claim_id collision, nothing written: {collide}")

with CJ.open("a", encoding="utf-8") as f:
    for c in NEW:
        f.write(json.dumps(c, ensure_ascii=False) + "\n")
print(f"appended {len(NEW)} claims: {[c['claim_id'] for c in NEW]}")

# --- repair the dangling cross-reference in R1-76 ---------------------------
lines, fixed = [], 0
for line in CJ.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    c = json.loads(line)
    if c["claim_id"] == "R1-76" and "(R1-72)" in c["claim"]:
        c["claim"] = c["claim"].replace("(R1-72)", "(R1-83)")
        fixed += 1
    lines.append(json.dumps(c, ensure_ascii=False))
CJ.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"repaired {fixed} dangling cross-reference(s) in R1-76 -> R1-83")
print(f"corpus now: {len(lines)} claims in this file")
