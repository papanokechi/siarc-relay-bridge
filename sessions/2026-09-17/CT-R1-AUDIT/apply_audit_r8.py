"""CT-R1-AUDIT R8: ruling 2 -- refine the `review` taxonomy.

`cold` now has a type-dependent definition:
  proofs       : an independent party read the argument without its derivation history.
  computations : an independent party reproduced the value by DIFFERENT CODE, ideally a
                 different method, without access to the original script or output.
                 Re-executing the original script stays `self`.
Every `review` value must carry a `review_note` recording the method.
"""
import json
from pathlib import Path

ROOT = Path(r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17")

# Explicit notes for claims already carrying a review value.
NOTES = {
    "S1-03": ("cold", "proof: CT-S7-COLDREAD read theorem.tex part (i) Step 3 with no access to "
                      "CT-R1-AUDIT/, CT-S7's own derivation history, or any REPORT.md. Verdict SOUND."),
    "S1-04": ("cold", "proof: CT-S10-COLDREAD2 read the repaired thm:growth Step 3 / G1 passage with no "
                      "access to CT-R1-AUDIT/, CT-S7-COLDREAD/, or any REPORT.md. Verdict SOUND; its only "
                      "finding was stale bibliography metadata, since corrected."),
    "R1-18": ("cold", "proof: CT-S11-COLDREAD3 read a self-contained packet (coldpackets/PACKET-A) with no "
                      "access to the derivation history, and improved the proof by supplying the explicit "
                      "reduction-of-order argument for the nonzero log coefficient."),
    "R1-43": ("cold", "proof: as R1-18; this claim records the improvement itself."),
    "R1-31": ("cold", "computation: CT-S12-COLDREAD4 re-derived the PV rescaling law from the Painleve V "
                      "equation by direct symbolic substitution in its OWN SymPy script "
                      "(compute_pv_checks.py), with no access to verify_s9.py or verify_s9.out, and "
                      "additionally checked the opposite scaling convention. Different code, same "
                      "conclusion."),
    "R1-32": ("cold", "computation/inspection: CT-S12-COLDREAD4 read the Jimbo page image itself and "
                      "independently rediscovered the (A1)_PV assumption without being prompted to look "
                      "for it. Independent observation of the same primary source, not a re-run."),
    "R1-33": ("cold", "computation: CT-S12-COLDREAD4 recomputed k and t in its own script from the packet "
                      "statement, with no access to verify_s9.py. Verdict SOUND WITH CAVEAT; the caveat "
                      "(the affine identification is an assumption) was raised independently."),
}

# CT-S8's reproduction of K qualifies as a cold computation review of the P3 amplitude claims.
EXTRA = {
    "R1-40": ("cold", "computation: CT-S8-LITCHECK derived K independently from the Gauss multiplication "
                      "formula and verified it numerically at 60 dps, N=4000, for four polynomials "
                      "(d=1,2,3), using its own script (scripts/verify_growth_law.py) with no access to "
                      "P3's derivation, script or output. Different code and an independently motivated "
                      "derivation, so this meets the `cold` bar for computations."),
}

changed = 0
downgraded = []
for fn in ROOT.glob("*/claims.jsonl"):
    rows = [json.loads(l) for l in fn.read_text(encoding="utf-8").splitlines() if l.strip()]
    ch = False
    for r in rows:
        cid = r.get("claim_id")
        if cid in NOTES or cid in EXTRA:
            rev, note = (NOTES.get(cid) or EXTRA[cid])
            r["review"], r["review_note"] = rev, note
            ch = True
            changed += 1
        elif r.get("review") == "cold":
            # any other 'cold' not explicitly justified above is not defensible under the
            # refined definition -> downgrade rather than leave it unsupported.
            r["review"] = "self"
            r["review_note"] = ("Downgraded under the refined R8 definition: no independent party "
                                "reproduced this by different code or read it without its derivation "
                                "history.")
            downgraded.append(cid)
            ch = True
        elif r.get("review") == "self" and "review_note" not in r:
            r["review_note"] = ("self: checked only by the session that produced it. For a computation "
                                "this means no independent reimplementation; re-running the original "
                                "script would not change this.")
            ch = True
    if ch:
        fn.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in rows) + "\n", encoding="utf-8")

print("review values written/updated:", changed)
print("downgraded to self:", downgraded or "none")

import collections
rev = collections.Counter()
missing = []
for p in ROOT.glob("*/claims.jsonl"):
    for l in p.read_text(encoding="utf-8").splitlines():
        if not l.strip():
            continue
        r = json.loads(l)
        if r.get("review"):
            rev[r["review"]] += 1
            if not r.get("review_note"):
                missing.append(r["claim_id"])
print("review tally:", dict(rev))
print("review values lacking review_note:", missing or "none")
