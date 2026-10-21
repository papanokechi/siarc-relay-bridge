"""
CT-R1-AUDIT R3: apply operator review #3 rulings to the claim corpus.

1. Ruling 1 accepted with an addition: every evidence_type=="proof" claim gains a
   `review` field with value self | cold | lean.  All 12 retagged claims start at
   "self"; nothing has been cold-read or machine-checked yet.
2. Operator correction A: the Remark 2.2 lemma does not need c(s) != 0.
3. Operator correction B: the System B multiset claim must say "up to twist".
"""
import json
from pathlib import Path

ROOT = Path(r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17")

REVIEW_NOTE = ("Operator review #3 ruling 1: evidence_type 'proof' accepted, with a mandatory "
               "`review` field. 'self' = checked only by the agent that wrote it; 'cold' = read "
               "by an independent session without its derivation history; 'lean' = machine-checked "
               "with no sorry on the claim's path. PROVEN may stand on a 'self' claim, but anything "
               "entering a deposit requires 'cold' or 'lean'.")

# --- correction A: the lemma is more general than we stated -------------------
R1_18_NEW = (
    "At every simple root s of chi, the equation chi*y'' + chi'*y' + c*y = 0 has p = chi'/chi with "
    "residue exactly 1 and q = c/chi with at most a simple pole, so (x-s)^2*q -> 0 and the indicial "
    "polynomial is exactly lambda^2 REGARDLESS OF THE VALUE OF c(s). The exponents are therefore 0,0, "
    "equal exponents at a regular singular point always force a log term in the second Frobenius "
    "solution, and the point is never apparent. This refutes companion Remark 2.2 in full generality."
)
R1_18_NOTE = ("Operator review #3, correction A: the hypothesis c(s) != 0 is unnecessary and has been "
              "dropped. Once p has residue 1 and q has at most a simple pole, the indicial polynomial "
              "is lambda^2 whatever c(s) is; equal exponents then force the log term. The lemma is "
              "strictly more general than first recorded.")

# --- correction B: "ordinary after twist" is equivalence up to rank-1 twist ---
R1_20_NEW = (
    "System B's point z=infinity has local exponents differing by exactly 1 and no log term, and "
    "becomes an ordinary point of the normal form (R = 11/4, finite, at x=0 under z=1/x). UP TO A "
    "RANK-1 TWIST it therefore carries no moduli, and System B's effective Katz multiset is (0,0,1) "
    "rather than (1,0,0,0). This is equivalence up to a rank-1 twist, NOT equivalence of the "
    "operators themselves; it is valid for reading van der Put-Saito Table 2.1 because that table "
    "classifies trace-free rank-2 connections, which is exactly the up-to-twist setting. CT-S6 claim "
    "S6-C7 is SUPERSEDED as an artefact of an apparency test that disallows twisting."
)
R1_20_NOTE = ("Operator review #3, correction B: claim text must say 'up to twist'. 'Ordinary after "
              "twist' is equivalence up to a rank-1 twist, not equivalence of the operators "
              "themselves. That is the setting Table 2.1 uses (trace-free rank-2 connections), so "
              "the (0,0,1) reading is valid there.")

REWRITE = {"R1-18": (R1_18_NEW, R1_18_NOTE), "R1-20": (R1_20_NEW, R1_20_NOTE)}

NEW_CLAIMS = [
    ("R1-22",
     "The stale bibitem{Vquad} is in the PERIOD-REP paper, not in Channel Theory. It was ALREADY "
     "CORRECTED in the 2026-06-16 layout-fix cascade: VQUAD-PAPER-CORRECTIONS-001, "
     "VQUAD-PAPER-LAYOUTFIX-001 and VQUAD-REPRO-BUNDLE-002 (both slot-root and run-2) all carry the "
     "actual Zenodo title 'A non-classical Painleve V transcendent from a quadratic polynomial "
     "continued fraction: surface classification and resurgent Stokes data' and the CONCEPT DOI "
     "10.5281/zenodo.20455089. The stale form, citing version DOI 10.5281/zenodo.20455090 with the "
     "old title, survives only in the superseded 2026-06-15 VQUAD-PERIODREP-PAPER-001 draft and in "
     "the superseded VQUAD-REPRO-BUNDLE-001 copy. CT-S4 read the 2026-06-15 draft. The deposit-ready "
     "path VQUAD-REPRO-BUNDLE-002/run-2 is correct, so no fix is required.",
     "INSPECTED", "file_inspection", None),
    ("R1-23",
     "Residual bibliographic gap: the corrected bibitem{Vquad} records the concept DOI and the Zenodo "
     "title but does not name the version read inside the bibitem itself; 'version 1.2' appears only "
     "in section-8 prose ('with the S=2*pi*K calibration in version 1.2'). The operator's specification "
     "asks for concept DOI, version read, and Zenodo title together. Suggested for that paper's next "
     "version; NOT applied here.",
     "INSPECTED", "file_inspection", None),
    ("R1-24",
     "Deposit gate status at the close of review #3: gate 1 (cold review of theorem.tex part (i) Step 3 "
     "and the G1 argument) is DELEGATED to CT-S7-COLDREAD and not yet returned; gate 2 (no "
     "machine-checked claim) is OPEN, since 7 sorry's remain in XiZero.lean, so the note must not "
     "claim formal verification; gate 3 (prior-art check against Perron, Birkhoff-Trjitzinsky, "
     "Wong-Li, Pincherle/Gautschi) is DELEGATED to CT-S8-LITCHECK and not yet returned. No deposit "
     "may proceed until all three are closed.",
     "INSPECTED", "file_inspection", None),
    ("R1-25",
     "Conjecture 4.1's parameter values alpha=1/6, beta=0, gamma=0, delta=-1/2 were derived from the "
     "now-refuted apparency premise and require re-derivation from the correct local data (repeated "
     "exponents [0,0] with log terms at both finite points, i.e. unipotent non-trivial local "
     "monodromy). Delegated to CT-S9-PVPARAMS with the convention required to be quoted from a "
     "fetched source before computing, and an explicit instruction to halt rather than reconstruct "
     "the PV dictionary from memory. Outcome not yet returned.",
     "STRUCTURAL", "computation", None),
]


def load(p):
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


touched, n_review, n_rewrite = [], 0, 0
for p in sorted(ROOT.glob("*/claims.jsonl")):
    rows = load(p)
    changed = False
    for r in rows:
        if r.get("evidence_type") == "proof" and "review" not in r:
            r["review"] = "self"
            r["audit_r3"] = REVIEW_NOTE
            n_review += 1
            changed = True
        if r.get("claim_id") in REWRITE:
            new, note = REWRITE[r["claim_id"]]
            r["claim_before_r3"] = r["claim"]
            r["claim"] = new
            r["audit_r3"] = note
            r["amended_in"] = "CT-R1-AUDIT/R3"
            n_rewrite += 1
            changed = True
    if changed:
        p.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n",
                     encoding="utf-8")
        touched.append(p.parent.name)

audit = ROOT / "CT-R1-AUDIT" / "claims.jsonl"
with audit.open("a", encoding="utf-8") as f:
    for cid, claim, label, ev, dps in NEW_CLAIMS:
        f.write(json.dumps({
            "claim_id": cid, "task_id": "CT-R1-AUDIT-R3", "claim": claim, "label": label,
            "evidence_type": ev, "dps": dps, "reproducible": True,
            "script": "sessions/2026-09-17/CT-R1-AUDIT/apply_audit_r3.py",
            "output_hash": None,
        }, ensure_ascii=False) + "\n")

print("amended sessions:", ", ".join(touched))
print(f"proof claims given review='self' : {n_review}")
print(f"claim texts rewritten            : {n_rewrite}")
print(f"new R3 claims appended           : {len(NEW_CLAIMS)}")

import collections
lab, rev, bad = collections.Counter(), collections.Counter(), []
for p in ROOT.glob("*/claims.jsonl"):
    for r in load(p):
        lab[r.get("label")] += 1
        if r.get("evidence_type") == "proof":
            rev[r.get("review")] += 1
        if r.get("evidence_type") == "file_inspection" and r.get("label") == "PROVEN":
            bad.append(r["claim_id"])
print("\ncorpus labels:", dict(lab))
print("proof-claim review states:", dict(rev))
print("rule 1(a) violations:", bad or "none")
print("deposit-eligible proof claims (cold|lean):", rev.get("cold", 0) + rev.get("lean", 0))
