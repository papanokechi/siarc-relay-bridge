"""
CT-R1-AUDIT R5: record (a) the independent check of CT-S9-PVPARAMS and
(b) the closure of deposit gate 1 after the second cold read.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17")
S = ROOT / "CT-R1-AUDIT"
h = hashlib.sha256((S / "verify_s9.out").read_bytes()).hexdigest()

# ---- gate 1 closure: S1-04 reaches review='cold' ---------------------------
S1 = ROOT / "CT-S1-THEOREM" / "claims.jsonl"
rows = [json.loads(l) for l in S1.read_text(encoding="utf-8").splitlines() if l.strip()]
for r in rows:
    if r["claim_id"] == "S1-04":
        r["review"] = "cold"
        r["audit_r5"] = (
            "Gate 1 CLOSED. After the DLMF equation-number repair, CT-S10-COLDREAD2 read the "
            "repaired thm:growth Step 3 passage cold (theorem.tex only; no access to CT-R1-AUDIT, "
            "CT-S7-COLDREAD, or any REPORT.md) and found the algebra, the product/error step, the "
            "hypotheses, the circularity check AND the DLMF equation numbers all sound. Its only "
            "finding was stale bibliography metadata: the file said 'Release 1.2.4' while DLMF is "
            "Version 1.2.8, release date 2026-09-15. Confirmed independently against the live page "
            "(sha256 929045c7b1cd72f35e8d6e2c966340e30d2c3b990245d44e42f5de8c1caea28e) and corrected; "
            "theorem.tex recompiles clean at 7 pages. The mathematical passage is cold-read SOUND.")
S1.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n", encoding="utf-8")

NEW = [
    ("R1-29",
     "The Jimbo PV dictionary quoted by CT-S9 is transcribed EXACTLY from Jimbo, 'Monodromy Problem "
     "and the Boundary Condition for Some Painleve Equations', PRIMS, p.1152: alpha=(1/8)(th0-tht+thinf)^2, "
     "beta=-(1/8)(th0-tht-thinf)^2, gamma=1-th0-tht, delta=-1/2, with eigenvalues of A_nu equal to "
     "+/- th_nu/2 so that the exponent difference at nu is exactly th_nu. Verified by reading the page "
     "image in CT-S9-PVPARAMS/outputs/jimbo_page16-16.png.", "INSPECTED", "file_inspection", None),
    ("R1-30",
     "CT-S9's System C computation reproduces independently: normal form (12x^4+4x^3+4x^2+11)/(4(3x^2+x+1)^2), "
     "residue -1/4 and exponent difference 0 at both s_pm, R->1/3 at infinity with WKB exponentials "
     "exp(+/- sqrt(3)x/3). Hence th0=tht=0 and the Jimbo dictionary gives alpha=thinf^2/8, beta=-alpha, "
     "gamma=1, delta=-1/2.", "PROVEN", "computation", h),
    ("R1-31",
     "The contradiction with the companion's gamma=0 is genuine, not a convention artefact: under the PV "
     "scaling z -> c*z the parameters transform as (alpha,beta,gamma,delta) -> (alpha,beta,c*gamma,c^2*delta), "
     "so holding delta=-1/2 forces c=+/-1 and gamma is fixed up to sign. gamma=1 cannot be rescaled to "
     "gamma=0.", "PROVEN", "computation", h),
    ("R1-32",
     "Jimbo's standing assumption (A1)_PV, 'th0, tht not in Z', stated on the same page immediately below "
     "the dictionary, is VIOLATED by System C's local data, which gives th0=tht=0 in Z. CT-S9 did not flag "
     "this. The dictionary itself precedes (A1)_PV and is unconditional, so the parameter computation "
     "stands; but everything Jimbo derives after that line is outside its stated hypotheses for this case. "
     "Coherence check: integer theta is precisely the resonant case, and resonance is precisely when logs "
     "can appear -- logs were independently found at both finite points.",
     "INSPECTED", "file_inspection", None),
    ("R1-33",
     "The PV time for System C is NOT a free deformation parameter; it is FIXED. Jimbo's system (3.1) "
     "normalises the irregular part at infinity to exp(x*diag(1,0)), whose exponent difference is exactly x. "
     "System C's exponent difference at infinity is 2*sqrt(3)x/3, so the affine scale k=2/sqrt(3) is forced, "
     "and t = k*(s_mp - s_pm) = -/+ 2i*sqrt(33)/9 with |t| = 2*sqrt(33)/9. System C therefore corresponds to "
     "a SINGLE value of the PV time (the two signs differing only by relabelling s+ and s-). A membership "
     "claim would require exhibiting a curve t -> L_t of connections, isomonodromic in t, whose fibre at "
     "t = -/+ 2i*sqrt(33)/9 is System C; such a family was NOT FOUND in the inspected sources by the methods "
     "used.", "STRUCTURAL", "computation", h),
    ("R1-34",
     "Net position on companion Conjecture 4.1 after CT-S9 and its audit: alpha=1/6 UNDETERMINED by local "
     "data (alpha=thinf^2/8 and thinf is not fixed by local scalar data); beta=0 CONTRADICTED jointly with "
     "alpha=1/6 since beta=-alpha identically; gamma=0 CONTRADICTED since gamma=1 and is not rescalable; "
     "delta=-1/2 CONSISTENT as Jimbo's normalisation. The 'right row, wrong reason' position hardens: the "
     "(0,0,1) Katz multiset still matches the van der Put-Saito D5/PV row p.2635, but the parameter tuple "
     "attached to it does not survive the correct local data.", "STRUCTURAL", "computation", h),
    ("R1-35",
     "Deposit gate 1 is CLOSED. Both target passages of theorem.tex have now been cold-read by independent "
     "sessions with no access to their derivation history: thm:radius Step 3 SOUND (CT-S7-COLDREAD), and "
     "thm:growth Step 3 / G1 SOUND after repair (CT-S10-COLDREAD2). Two defects were found and fixed in the "
     "process: a misquoted DLMF equation number and a stale DLMF release string. Claims S1-03 and S1-04 both "
     "now carry review='cold'. Gate 2 (no machine-checked claim) remains OPEN by design: 7 sorry's remain in "
     "XiZero.lean. Gate 3 (prior art) is still delegated to CT-S8-LITCHECK and NOT returned.",
     "INSPECTED", "file_inspection", None),
]
with (S / "claims.jsonl").open("a", encoding="utf-8") as f:
    for cid, claim, label, ev, oh in NEW:
        rec = {"claim_id": cid, "task_id": "CT-R1-AUDIT-R5", "claim": claim, "label": label,
               "evidence_type": ev, "dps": None, "reproducible": True,
               "script": "sessions/2026-09-17/CT-R1-AUDIT/verify_s9.py", "output_hash": oh}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

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
print("verify_s9.out sha256:", h)
print("corpus labels:", dict(lab))
print("proof-claim review states:", dict(rev))
print("rule 1(a) violations:", bad or "none")
