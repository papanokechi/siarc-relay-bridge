"""Emit claims.jsonl for CT-S26-CTV17-DRAFT.

P0 Amendment B: hashes are taken from DISK after the artefact is final. This
emitter does not re-run verify_notice.py; it asserts the output exists, ends in
VERDICT: OK, reports zero failures and zero broken checks, then writes the
claims and re-hashes to confirm nothing moved underneath it.

No computation was run in this session, so every claim is INSPECTED or
STRUCTURAL. There is no PREREG.md and its absence is stated rather than
back-filled (precedent: CT-S3A-ZETA-AUDIT, CT-S24-PAPER-OUTLINE).
"""

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESSION = HERE.parent
CLAIMS = SESSION / "claims.jsonl"
NOTICE = SESSION / "NOTICE-v1.7.md"
OUT = SESSION / "outputs" / "verify_notice.out.txt"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def build(h_out: str, h_notice: str):
    return [
        {
            "claim_id": "S26C-01",
            "task_id": "CT-S26-CTV17-DRAFT/draft",
            "claim": (
                "THE v1.7 VERSION NOTICE IS DRAFTED, and every content guard on it is a check "
                "that can fail. NOTICE-v1.7.md carries the five commissioned items in order "
                "(attribution, the exponent and its priority position, K and r_infinity, the "
                "vacuity explanation, the Borel material), opens with a current-state section "
                "before any history, and places the erratum stack below it. "
                "scripts/verify_notice.py runs 14 checks against the drafted text and then runs "
                "each check a second time against a MUTANT of the notice in which exactly the "
                "thing that check guards has been removed; a check that still passes on its own "
                "mutant is reported as BROKEN and fails the run. Result: 14 of 14 checks pass, "
                "14 of 14 controls fire, 0 broken. DRAFT ONLY: nothing is deposited, no metadata "
                "is edited, and the notice says so on its first line."
            ),
            "label": "INSPECTED",
            "evidence_type": "file_inspection",
            "dps": None,
            "reproducible": True,
            "script": "scripts/verify_notice.py",
            "output_hash": h_out,
        },
        {
            "claim_id": "S26C-02",
            "task_id": "CT-S26-CTV17-DRAFT/doi",
            "claim": (
                "EVERY ZENODO DOI PRINTED BY THE NOTICE IS READ FROM A HELD SOURCE, NOT FROM "
                "THE PROMPT OR FROM MEMORY. The concept DOI 10.5281/zenodo.19941678 and the "
                "version DOIs 10.5281/zenodo.19941679 (v1.1) and 10.5281/zenodo.19951331 (v1.2) "
                "all occur in sessions/2026-05-02/CHANNEL-THEORY-V13-RELEASE/"
                "zenodo_description_v1.3.txt, which states 'This outline is a top-level posting "
                "(concept DOI 10.5281/zenodo.19941678, preserved across versions)'. The checker "
                "enforces the converse as well: any Zenodo DOI appearing in the notice that does "
                "NOT appear in the held description fails the run, and the control confirms this "
                "by substituting a fabricated DOI and being rejected. This matters because a "
                "concept DOI is a distinct object from a version DOI and is not the record "
                "number."
            ),
            "label": "INSPECTED",
            "evidence_type": "file_inspection",
            "dps": None,
            "reproducible": True,
            "script": "scripts/verify_notice.py",
            "output_hash": h_out,
        },
        {
            "claim_id": "S26C-03",
            "task_id": "CT-S26-CTV17-DRAFT/erratum-stack",
            "claim": (
                "THE ERRATUM STACK IS INCOMPLETE BY DECLARATION, NOT BY OMISSION, AND NO TEXT "
                "WAS INVENTED FOR THE MISSING VERSIONS. Channel Theory v1.4, v1.5 and v1.6 are "
                "ABSENT from this repository: the newest in-repo source is v1.3.1 at "
                "sessions/2026-05-08/T1-OPERATOR-CT-V131-3.5.1-R1A-AMENDMENT-VQUAD-CAVEAT-117/"
                "channel_theory_outline_v131_with_r1a_caveat.tex, and the v1.3.1 claims record "
                "points at pcf-research/channel/..., which does not exist on this machine "
                "(CT-S0-INVENTORY/REPORT.md section 2). Two consequences are stated in the "
                "notice rather than papered over: (i) the text and label of rem:d3-vacuous, "
                "which item 4 of the commission says the one-line vacuity explanation REPLACES, "
                "could not be read, so the replacement is stated on its own terms and the "
                "operator must check the replaced wording against the live source; (ii) the v1.5 "
                "halving notice could not be read, and the halving is therefore cited to the "
                "code (CC-PIPELINE-G/vquad_recovery.py L70-79) rather than to the notice. "
                "Separately, op:xi0-singularity-type has ZERO occurrences in this repository and "
                "is NOT cited; the open problem it would have named is stated without a tag and "
                "flagged for the operator to assign one."
            ),
            "label": "INSPECTED",
            "evidence_type": "file_inspection",
            "dps": None,
            "reproducible": True,
            "script": "scripts/verify_notice.py",
            "output_hash": h_out,
        },
        {
            "claim_id": "S26C-04",
            "task_id": "CT-S26-CTV17-DRAFT/vacuity",
            "claim": (
                "THE VACUITY EXPLANATION IS STRUCTURAL AND REPLACES AN EMPIRICAL SWEEP. xi_0 = "
                "d/|beta_d|^(1/d) reads ONLY beta_d (S1-03, PROVEN), and rho = -(d+1)/2 - "
                "beta_{d-1}/beta_d reads ONLY beta_d and beta_{d-1} (S1-04, PROVEN), so any two "
                "families sharing their top two coefficients share both invariants EXACTLY and "
                "no test built on xi_0 and rho alone can separate them. This is a one-line "
                "consequence of two proved statements; it does not depend on degree, on the "
                "discriminant, or on which representatives were sampled, and it therefore needs "
                "no coefficient sweep. It accounts without a sweep for the two phenomena the "
                "earlier versions recorded empirically: the K-SCAN coincidence between V_quad "
                "and QL15 (both beta_2 = 3, hence both xi_0 = 2/sqrt3 to 200 digits, Remark "
                "3.3.C) and the non-injectivity of Proposition 3.3.B (QL01 and QL02 share xi_0 = "
                "2 and rho = -5/2 and split only at a_2). CONSEQUENCE STATED IN THE NOTICE: a B1 "
                "witness is by construction the weakest tier and cannot be strengthened by more "
                "xi_0 data at any precision; separation requires a coordinate reading below "
                "beta_{d-1}. The two phenomena are quoted from the held v1.3 release "
                "description, not from memory."
            ),
            "label": "STRUCTURAL",
            "evidence_type": "file_inspection",
            "dps": None,
            "reproducible": True,
            "script": "scripts/verify_notice.py",
            "output_hash": h_out,
        },
        {
            "claim_id": "S26C-05",
            "task_id": "CT-S26-CTV17-DRAFT/transit",
            "claim": (
                "BOTH REQUIRED CARRY-OVERS ARRIVED, AND EACH IS GUARDED BY A CHECK THAT CAN "
                "FAIL. OUTLINE.md section 3.4's TRANSIT MANIFEST names two items that travel "
                "with the Borel material and that no claim id carries automatically, because "
                "they are METHOD rather than result. (1) THE PSLQ BASIS IS PRINTED IN FULL: the "
                "notice prints the 6-vector [log C, log 2, log 3, log pi, log Gamma(1/3), 1] "
                "with the full relation, the bounds |coeff| <= 1e6, 1 <= |m| <= 12, dps 120, "
                "D_trust = 100 and cost <= 0.40 * D_trust = 40, and the checker rejects the "
                "notice if an ellipsis appears in that block, if the cost rule is deleted, or if "
                "Gamma(1/6) reappears in it -- three separate mutants, all rejected. A printed "
                "basis is what lets a reader check it for internal degeneracy; an elided one is "
                "what hid the degeneracy the first time. (2) THE NAMING PROHIBITION IS STATED AS "
                "A PROHIBITION: K is the amplitude at xi_0 = 2/sqrt3, S_{zeta*} is the Stokes "
                "constant at zeta* = 2 xi_0 = 4/sqrt3, a factor of two apart in the ACTION, and "
                "neither name may ever be used for the other in prose, code or output filenames."
            ),
            "label": "INSPECTED",
            "evidence_type": "file_inspection",
            "dps": None,
            "reproducible": True,
            "script": "scripts/verify_notice.py",
            "output_hash": h_out,
        },
        {
            "claim_id": "S26C-06",
            "task_id": "CT-S26-CTV17-DRAFT/open-problem",
            "claim": (
                "op:cc-median-resurgence-execute IS RESTATED WITH ITS SERIES NAMED AND ITS "
                "PAINLEVE TARGET MARKED STALE. The v1.3 statement, read verbatim from the held "
                "release description, says only 'the V_quad formal coefficient series' and "
                "asserts that executing it 'would conditionally close the V_quad -> P_III(D6) "
                "correspondence at the Stokes-data level under a documented normalisation map'. "
                "The restatement names the series exactly -- S(u) = 1 + sum_{k>=1} a_k u^k, "
                "obtained from the Birkhoff formal solution f_+(u) = exp(c/u) u^rho S(u) of the "
                "order-2 ODE for f(z) = sum_n Q_n z^n at z = 0, in the uniformiser u = sqrt(z), "
                "after stripping exp(c/u) and u^rho, with Borel transform sum_k a_k zeta^k/k!, "
                "normalisation Gamma(k+1), Borel variable zeta conjugate to k -- and records TWO "
                "obstructions together: the normalisation map is OPEN, and the P_III(D6) target "
                "is SUPERSEDED, V_quad having been reclassified in sessions/2026-05-29/"
                "T1-SYNTH-VQ-N1-VQUAD-RECLASSIFICATION-APPLY with the disposition recorded in "
                "sessions/2026-05-02/VQUAD-PIII-NORMALIZATION-MAP/SUPERSEDED_BY_VQ-N1.json. The "
                "notice states that any restatement keeping the P_III(D6) wording without that "
                "pointer repeats a superseded premise, and it does not itself assert any "
                "Painleve label for V_quad. The H4 forecast attached to the problem is recorded "
                "as a theoretical prediction, never an executed measurement."
            ),
            "label": "INSPECTED",
            "evidence_type": "file_inspection",
            "dps": None,
            "reproducible": True,
            "script": "scripts/verify_notice.py",
            "output_hash": h_out,
        },
        {
            "claim_id": "S26C-07",
            "task_id": "CT-S26-CTV17-DRAFT/checker-defect",
            "claim": (
                "A CHECKER DEFECT WAS CAUGHT THAT REPORTED A CONTENT OMISSION WHERE NONE "
                "EXISTED, AND THE TWO ARE INDISTINGUISHABLE FROM THE VERDICT LINE ALONE. "
                "verify_notice.py's main() read the notice in BINARY and decoded it, then "
                "matched fenced blocks with the pattern '```\\n(.*?)```'. The file on disk has "
                "CRLF line endings, so the pattern matched nothing and the PSLQ check reported "
                "'no fenced block containing the basis was found' -- verbally identical to what "
                "it would report if the basis had actually been omitted from the notice, which "
                "is precisely the failure the TRANSIT MANIFEST exists to prevent. It was caught "
                "only because a second, independent read of the same function in TEXT mode "
                "returned the block and passed, i.e. two reads of one file disagreed. Repair: "
                "normalise CRLF to LF immediately after decoding, in ONE place. GENERAL FORM: a "
                "check that reports ABSENCE cannot distinguish 'the content is missing' from 'my "
                "reader could not see it', so an absence report must be confirmed by a second "
                "reader before it is believed -- and the mutant controls do not catch this, "
                "because a broken reader rejects the mutant too, for the same wrong reason."
            ),
            "label": "INSPECTED",
            "evidence_type": "file_inspection",
            "dps": None,
            "reproducible": True,
            "script": "scripts/verify_notice.py",
            "output_hash": h_out,
        },
        {
            "claim_id": "S26C-08",
            "task_id": "CT-S26-CTV17-DRAFT/labels",
            "claim": (
                "NO LABEL IS UPGRADED IN PROSE, AND THE NINE LOAD-BEARING LABELS IN THE NOTICE "
                "ARE CHECKED AGAINST THE CORPUS RECORD RATHER THAN ASSERTED. verify_notice.py "
                "reads every claims.jsonl under sessions/2026-09-17/ (497 claims) and asserts "
                "S1-03 PROVEN, S1-04 PROVEN, S1-05 STRUCTURAL, S3B-04 STRUCTURAL, S3B-05 "
                "VERIFIED, S21-76 INSPECTED, S22-21 PROVEN, S22-22 VERIFIED, S26-01 PROVEN; all "
                "22 claim ids cited anywhere in the notice resolve. Three separate checks guard "
                "the labels that are easiest to inflate: K carries 'VERIFIED, never PROVEN' and "
                "is never labelled PROVEN; the seven remaining Lean 'sorry's are stated and the "
                "notice explicitly denies claiming formal verification, with every occurrence of "
                "'machine-checked' required to sit inside a negation; and Ibrahim-Salvy is "
                "quoted only in its weaker printed form ('do not know how to compute'), the "
                "stronger reading appearing solely as the one excluded. The notice's sha256 is "
                "recorded in the checker output so that any later edit invalidates this claim's "
                "evidence rather than silently outliving it."
            ),
            "label": "INSPECTED",
            "evidence_type": "file_inspection",
            "dps": None,
            "reproducible": True,
            "script": "scripts/verify_notice.py",
            "output_hash": h_out,
            "notice_sha256": h_notice,
        },
    ]


def main() -> int:
    for p in (NOTICE, OUT):
        assert p.exists(), f"missing artefact {p}"
        assert p.stat().st_size > 0, f"empty artefact {p}"
    h_out, h_notice = sha256(OUT), sha256(NOTICE)
    print(f"{OUT.name}: {h_out}")
    print(f"{NOTICE.name}: {h_notice}")

    txt = OUT.read_text(encoding="utf-8")
    lines = [l.strip() for l in txt.strip().splitlines() if l.strip()]
    assert lines[-1].startswith("="), f"output does not end in a rule: {lines[-1]!r}"
    assert "VERDICT: OK" in lines, "the checker run did not end OK"
    assert "checks failed       : 0" in txt, "the checker reported failures"
    assert "broken checks       : 0" in txt, "the checker reported broken checks"
    assert "controls fired      : 14 of 14" in txt, "not all controls fired"
    # the output must be the output for THIS notice, not a stale one
    assert h_notice in txt, "the checker output does not carry the current notice hash"
    print("read back from disk: VERDICT OK, 0 failed, 0 broken, 14/14 controls, hash matches")

    if CLAIMS.exists():
        print("claims.jsonl already exists; refusing to overwrite")
        return 2

    rows = build(h_out, h_notice)
    with open(CLAIMS, "w", encoding="utf-8", newline="\n") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=True) + "\n")

    back = [json.loads(l) for l in CLAIMS.read_text(encoding="utf-8").splitlines() if l.strip()]
    assert len(back) == len(rows), "read-back row count mismatch"
    for r in back:
        assert r["output_hash"] == h_out, f"{r['claim_id']} bad hash"
        assert r["label"] in ("PROVEN", "VERIFIED", "STRUCTURAL", "INSPECTED", "CONJECTURED"), \
            f"{r['claim_id']} bad label"
        assert not (r["label"] == "PROVEN" and r["evidence_type"] == "file_inspection"), \
            f"{r['claim_id']} violates invariant 1(a)"
    assert sha256(OUT) == h_out and sha256(NOTICE) == h_notice, "an artefact moved"
    print(f"wrote and read back {len(back)} claims: {', '.join(r['claim_id'] for r in back)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
