"""R11: append the review-#8 / CT-S14 claims, and promote the claims that the
cold read cleared. Idempotent: re-running does not duplicate.
"""
import hashlib
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
CJ = HERE / "claims.jsonl"


def sha(p):
    p = pathlib.Path(p)
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None


OUT = sha(HERE / "verify_s14.out.txt")
ROOTS = sha(HERE / "verify_roots.out.txt")
INV = sha(HERE / "check_invariants.log")
DEPS = sha(HERE / "deposit_deps2.log")

NEW = [
    # --- adoption of CT-S14, each task separately -------------------------
    dict(claim_id="R1-71", task_id="R11-S14",
         claim="Object B's trace-free normal form, pulled back by z=1/x, is EXACTLY equal to the "
               "trace-free normal potential of companion v1.2's printed ODE: both equal "
               "(12x^4+4x^3+4x^2+11)/(4(3x^2+x+1)^2). Symbolic difference is identically zero.",
         label="PROVEN", evidence_type="computation", dps=None, reproducible=True,
         script="verify_s14.py", output_hash=OUT,
         review="cold", review_note="CT-S14-COLDREAD-B derived this independently under isolation; "
                                    "re-derived here from the primary printed data in different code."),
    dict(claim_id="R1-72", task_id="R11-S14",
         claim="Under z=1/x the pullback's first-order term 2/x contributes nothing to the normal "
               "potential, since (2/x)^2/4 + d/dx(2/x)/2 = 1/x^2 - 1/x^2 = 0. Hence inversion ALONE "
               "reaches object B's trace-free normal form; no twist is required for its Table 2.1 row.",
         label="PROVEN", evidence_type="computation", dps=None, reproducible=True,
         script="verify_s14.py", output_hash=OUT,
         review="cold", review_note="implicit in CT-S14 task 2; verified explicitly here."),
    dict(claim_id="R1-73", task_id="R11-S14",
         claim="The inversion x=1/z carries object B's finite singular points (-1 +/- i*sqrt(11))/2 "
               "exactly onto the companion operator's (-1 +/- i*sqrt(11))/6, resolving the "
               "previously unexplained /2 vs /6 discrepancy between the two objects.",
         label="PROVEN", evidence_type="computation", dps=None, reproducible=True,
         script="verify_roots.out.txt", output_hash=ROOTS,
         review="cold", review_note="elementwise check; an earlier set comparison printed False as a "
                                    "SymPy hashing artefact on unevaluated radicals, recorded in VERIFY-S14.md."),
    dict(claim_id="R1-74", task_id="R11-S14",
         claim="z=infinity is an ORDINARY point of object B's trace-free normal form: under x=1/z the "
               "potential is analytic at x=0 with value 11/4 and series 11/4 - 11x/2 - 29x^2/4 + O(x^3). "
               "B therefore has three singular points, not four, and Katz multiset (0,0,1).",
         label="PROVEN", evidence_type="computation", dps=None, reproducible=True,
         script="verify_s14.py", output_hash=OUT,
         review="cold", review_note="CT-S14-COLDREAD-B reached this independently under isolation."),
    dict(claim_id="R1-75", task_id="R11-S14",
         claim="The rank-1 twist h=A^(-1/2) relating the shared normal form to companion v1.2's PRINTED "
               "scalar operator alters the trace by 2*dlog(h) = -dlog(A) = -(6x+1)/(3x^2+x+1) != 0, and so "
               "falls outside the trace-0 class that van der Put-Saito p. 2634 sets up for Table 2.1.",
         label="PROVEN", evidence_type="computation", dps=None, reproducible=True,
         script="verify_s14.py", output_hash=OUT,
         review="cold", review_note="CT-S14-COLDREAD-B task 4, the question the packet was built around."),
    dict(claim_id="R1-76", task_id="R11-S14",
         claim="Object B's Table 2.1 row is UNAFFECTED by R1-75: the row is read from the trace-free "
               "normal form, which inversion alone reaches (R1-72). The twist is a feature of the "
               "companion's printed presentation, not of the classification. The drafted phrase "
               "'up to inversion and twist' was therefore unnecessary and inaccurate, and was removed.",
         label="STRUCTURAL", evidence_type="proof", dps=None, reproducible=True,
         script="verify_s14.py", output_hash=OUT,
         review="cold", review_note="CT-S14 task 5 states the re-normalisation; adopted with the "
                                    "qualification recorded in VERIFY-S14.md that its task-4 phrasing "
                                    "overstated the risk to the row."),
    dict(claim_id="R1-77", task_id="R11-S14",
         claim="At each root of A=3x^2+x+1 the companion's PRINTED scalar operator has residue(P)=1 and "
               "lim (x-b)^2 Q = 0, hence indicial polynomial lambda^2 and exponents [0,0]; in the "
               "trace-free normal form the exponents are [1/2,1/2]. Katz invariant 0 in both "
               "presentations, so no row is affected.",
         label="PROVEN", evidence_type="computation", dps=None, reproducible=True,
         script="verify_s14.py", output_hash=OUT,
         review="cold", review_note="CT-S14 task 3, arithmetic re-verified here."),
    dict(claim_id="R1-78", task_id="R11-S14",
         claim="CORRECTION to CT-S14 task 3: it called those points 'apparent/regular singular'. By the "
               "C1 lemma, residue(P)=1 with Q at most a simple pole forces a log term, so the points are "
               "regular singular and NON-apparent. CT-S14 was isolated from C1 by design and could not "
               "have known; the defect is in adoption, not in the reviewer. Substance ('not ordinary') adopted.",
         label="PROVEN", evidence_type="proof", dps=None, reproducible=True,
         script="verify_s14.py", output_hash=OUT,
         review="self", review_note="follows from C1 plus the verified hypotheses in R1-77; not "
                                    "independently reviewed, but it only tightens a label."),
    # --- record integrity / process ---------------------------------------
    dict(claim_id="R1-79", task_id="R11-INV",
         claim="Per-round invariants pass over the whole corpus: all claim_ids unique, no PROVEN claim "
               "rests on file_inspection, every claim carries exactly one recognised label, every "
               "reviewed claim carries a review_note, and every review value is in {self,cold,lean}.",
         label="VERIFIED", evidence_type="build", dps=None, reproducible=True,
         script="check_invariants.py", output_hash=INV,
         review="self", review_note="mechanical check; re-run at the end of every round."),
    dict(claim_id="R1-80", task_id="R11-DEPS",
         claim="Every route-4 (corroborated) entry in the deposit dependency audit now names the "
               "specific claim_id it was recomputed against, and deposit_deps2.py verifies each named "
               "claim exists in the corpus, reporting BROKEN LINK otherwise. No broken links were found.",
         label="VERIFIED", evidence_type="build", dps=None, reproducible=True,
         script="deposit_deps2.py", output_hash=DEPS,
         review="self", review_note="mechanical check."),
    dict(claim_id="R1-81", task_id="R11-BACKUP",
         claim="Off-repo backup refreshed for round R11: sessions-2026-09-17_20260917-210047.zip, "
               "32.4 MB, sha256 733de3f643a70f8e57e2c1665124586efec564ae3b1b0ae1ae887561f2be887a, with "
               "the hash written to a separate .sha256 file beside the archive, not inside it. "
               "236 session files included; 124116 .lake/__pycache__ paths excluded.",
         label="INSPECTED", evidence_type="file_inspection", dps=None, reproducible=True,
         script="make_backup.py", output_hash=sha(HERE / "make_backup.log"),
         review="self", review_note="filesystem fact at the time of writing."),
]

existing = set()
lines = []
if CJ.exists():
    for line in CJ.read_text(encoding="utf-8").splitlines():
        if line.strip():
            lines.append(line)
            existing.add(json.loads(line)["claim_id"])

added = [c for c in NEW if c["claim_id"] not in existing]
with CJ.open("a", encoding="utf-8") as f:
    for c in added:
        f.write(json.dumps(c, ensure_ascii=False) + "\n")
print(f"appended {len(added)} new claims ({len(NEW) - len(added)} already present)")

# --- promote R1-20: cold-confirmed by CT-S14 on its central assertion -------
text = CJ.read_text(encoding="utf-8").splitlines()
out, promoted = [], 0
for line in text:
    if not line.strip():
        continue
    c = json.loads(line)
    if c["claim_id"] == "R1-20" and c.get("review") != "cold":
        c["review"] = "cold"
        c["review_note"] = ("cold-confirmed by CT-S14-COLDREAD-B on its central assertion, that "
                            "z=infinity is not a genuine extra singular point and the tuple is (0,0,1) "
                            "(see R1-74); CT-S14 reached it independently under isolation.")
        promoted += 1
    out.append(json.dumps(c, ensure_ascii=False))
CJ.write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"promoted {promoted} claim(s) to review=cold")
print(f"corpus now: {len(out)} claims")
