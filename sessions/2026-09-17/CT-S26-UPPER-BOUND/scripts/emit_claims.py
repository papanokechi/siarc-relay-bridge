"""Emit claims.jsonl for CT-S26-UPPER-BOUND.

P0 Amendment B: hashes are taken from DISK, after the outputs are final. This
emitter does not re-run upper_bound.py, so no artefact it hashes can change
underneath it; it asserts the two outputs exist and are non-empty, writes the
claims, then reads them back and re-hashes to confirm nothing moved.

outputs/upper_bound.out.txt      -- the FAIL run (V1 fired). RETAINED, cited.
outputs/upper_bound_rev2.out.txt -- the corrected run, VERDICT OK.
"""

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESSION = HERE.parent
CLAIMS = SESSION / "claims.jsonl"
FAIL_RUN = SESSION / "outputs" / "upper_bound.out.txt"
OK_RUN = SESSION / "outputs" / "upper_bound_rev2.out.txt"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def build(h_fail: str, h_ok: str):
    return [
        {
            "claim_id": "S26-01",
            "task_id": "CT-S26-UPPER-BOUND/proposition-u",
            "claim": (
                "PROPOSITION U (the upper bound on r_infinity), PROVED. Let b be a polynomial "
                "with deg b = d >= 1 and b(n) != 0 for every integer n >= 1 (this is (A1) of "
                "CT-S1-THEOREM/theorem.tex), and suppose IN ADDITION that b(n) > 0 for every "
                "integer n >= 1. With Q_{-1} = 0, Q_0 = 1, Q_n = b(n) Q_{n-1} + Q_{n-2}, "
                "B_n = prod_{k<=n} b(k) and r_n = Q_n / B_n, then for every n >= 1 the EXACT "
                "FINITE-n inequality r_n <= exp( sum_{k=1}^{n-1} 1/(b(k) b(k+1)) ) holds, and "
                "consequently 1 <= r_infinity <= L := exp( sum_{k>=1} 1/(b(k) b(k+1)) ) < "
                "infinity. PROOF, in four steps, written out in full in PROOF.md BEFORE any "
                "numerics were run: (1) prop:positive (S1-02, PROVEN) gives r_n > 0 and "
                "(r_n)_{n>=1} strictly increasing, hence r_{n-2} <= r_{n-1} for every n >= 2 "
                "(at n = 2 because r_0 = r_1 = 1); (2) substituting that into the exact "
                "recurrence r_n = r_{n-1} + r_{n-2}/(b(n-1)b(n)) (theorem.tex eq. rnrec) gives "
                "r_n <= (1 + eps_n) r_{n-1} <= r_{n-1} exp(eps_n) with eps_n = 1/(b(n-1)b(n)) > "
                "0, using 1 + x <= e^x; (3) iterating from n down to r_1 = 1 and re-indexing by "
                "k = m-1 gives the finite-n statement; (4) the series converges by theorem.tex "
                "eq. eps (the same summability prop:exists already uses, restated as Lemma 1 so "
                "PROOF.md is closed), its partial sums increase to the total, and passage to the "
                "limit in a non-strict inequality gives the limit form, with the lower bound "
                "from S1-02. THE PROOF USES NO MINIMAL-SOLUTION, PINCHERLE OR "
                "PERRON-KREUSER INPUT AT ANY STEP, which matters because OUTLINE.md section 2.0 "
                "undertakes that nothing in the paper rests on Birkhoff-Trjitzinsky. DRAFTING "
                "CONSTRAINT: the upper half must NOT be written citing S1-02, which supplies "
                "step (1) and the lower bound only; it carries THIS claim id."
            ),
            "label": "PROVEN",
            "evidence_type": "computation",
            "proof_file": "PROOF.md",
            "dps": None,
            "reproducible": True,
            "script": "scripts/upper_bound.py",
            "output_hash": h_ok,
        },
        {
            "claim_id": "S26-02",
            "task_id": "CT-S26-UPPER-BOUND/numerics",
            "claim": (
                "THE FINITE-n INEQUALITY IS VERIFIED NUMERICALLY, and the arm that says so is "
                "shown capable of reporting a violation. At mpmath dps = 60, for ten polynomials "
                "b positive on n >= 1 of degrees 1, 2 and 3 (b = n, n+1, 2n-1, n/2+1/4, n^2, "
                "n^2+n+1, 3n^2-2n+1, n^3+1, 10n, 100n^2), the quantity "
                "P_{n-1} - log r_n was computed at EVERY n from 2 to 20000, where "
                "P_{n-1} = sum_{k=1}^{n-1} 1/(b(k)b(k+1)). Its minimum over n is non-negative "
                "for all ten, ranging from 3.124947918e-10 (b = 100n^2) to 0.3407296633 "
                "(b = n/2+1/4); the pre-registered falsifier F1 was a minimum below -1e-40, and "
                "did not fire. The finite-n form was tested rather than the limit form "
                "DELIBERATELY: it is exact at every n and needs no tail estimate, which removes "
                "the place where a loose tail bound could manufacture an agreement. ARM V4 (can "
                "the check fail?): the identical test against the WEAKENED bound with the k = 1 "
                "term deleted reports a violation for 10 of 10 families, so the passes above are "
                "informative rather than an inequality that cannot return a negative. ARM V5 "
                "(is the bound informative?): the ratios r_N / exp(P) span 0.4740494076107038 to "
                "0.9999999996117842, a spread of 0.5259505920 against a pre-registered floor of "
                "0.01, so (U-finite) is not being satisfied trivially. For b(n) = n the sum is "
                "sum 1/(k(k+1)) = 1 exactly, so L = e, and r_20000 = 2.2794713259205270753 "
                "against the bound 2.7181459177654179385."
            ),
            "label": "VERIFIED",
            "evidence_type": "computation",
            "dps": 60,
            "reproducible": True,
            "script": "scripts/upper_bound.py",
            "output_hash": h_ok,
        },
        {
            "claim_id": "S26-03",
            "task_id": "CT-S26-UPPER-BOUND/controls",
            "claim": (
                "THE RECURRENCE ENGINE IS CHECKED AGAINST AN INDEPENDENTLY KNOWN SOLUTION, in "
                "both directions. POSITIVE (V1): at z = 2 the modified Bessel identity "
                "I_{v-1}(2) - I_{v+1}(2) = v I_v(2) taken at v = n gives I_{n-1} - I_{n+1} = "
                "n I_n, so y_n = (-1)^n I_{n+1}(2) satisfies y_n = n y_{n-1} + y_{n-2} exactly. "
                "The implemented recurrence reproduces it to a worst-case 60.9069 digits over "
                "n = 2..40 (worst at n = 11), against a pre-registered threshold of 40 digits; "
                "falsifier F2 did not fire. NEGATIVE (V2): perturbing y_7 by a relative 1e-20 "
                "drops the same residual to 20.0 digits of agreement, against a requirement of "
                "below 25, so the residual is not one that returns zero whatever it is fed. The "
                "two arms together test the engine against something other than itself."
            ),
            "label": "VERIFIED",
            "evidence_type": "computation",
            "dps": 60,
            "reproducible": True,
            "script": "scripts/upper_bound.py",
            "output_hash": h_ok,
        },
        {
            "claim_id": "S26-04",
            "task_id": "CT-S26-UPPER-BOUND/controls",
            "claim": (
                "POSITIVITY IS LOAD-BEARING IN PROPOSITION U, NOT DECORATIVE. Arm V6, "
                "pre-registered as a finding and not as a gate, ran the same finite-n test on "
                "six sign-changing b, each with b(n) != 0 at every positive integer n, to "
                "n = 2000. THREE VIOLATE (U-finite): b(n) = 2n-9 (min slack -0.04235066097), "
                "b(n) = 3n-100 (-0.004279784399), and b(n) = n-7/2, where r_n becomes "
                "non-positive so the log-form slack is -infinity outright. Three do not: "
                "b(n) = n^2-7n+3, b(n) = n^2-10n+2 and b(n) = -n^2+5n-1. The hypothesis b > 0 "
                "on n >= 1 therefore cannot be dropped from Proposition U: it is consumed at "
                "step (1) of the proof, where r_{n-2} <= r_{n-1} is needed, and the "
                "counterexamples show the conclusion genuinely fails without it rather than "
                "merely the proof. That three of six do NOT violate is recorded as observed and "
                "is not offered as evidence of anything: no claim is made about which "
                "sign-changing b satisfy the inequality."
            ),
            "label": "VERIFIED",
            "evidence_type": "computation",
            "dps": 60,
            "reproducible": True,
            "script": "scripts/upper_bound.py",
            "output_hash": h_ok,
        },
        {
            "claim_id": "S26-05",
            "task_id": "CT-S26-UPPER-BOUND/addendum",
            "claim": (
                "A REGISTERED FALSIFIER FIRED, AND THE DEFECT WAS IN THE CONTROL, NOT THE "
                "ENGINE. PREREG.md section 5 registered arm V1 as 'y_n = (-1)^n I_n(2) satisfies "
                "y_n = n y_{n-1} + y_{n-2}'. The first run reported 0.30103 digits of agreement "
                "at n = 2 and F2 fired, halting with VERDICT: FAIL "
                "(outputs/upper_bound.out.txt, RETAINED UNCHANGED and cited by this claim). "
                "Substituting that closed form and dividing by (-1)^n requires "
                "I_{n-2} - I_n = n I_{n-1}, whereas the Bessel identity at v = n-1 gives "
                "I_{n-2} - I_n = (n-1) I_{n-1}: the registered closed form was WRONG BY AN INDEX "
                "SHIFT, and 0.30103 = -log10(1/2) is the size of exactly that one-unit "
                "discrepancy at n = 2, not the signature of a broken iteration. The correct "
                "solution, derived in ADDENDUM-1.md section 3, is y_n = (-1)^n I_{n+1}(2). "
                "HANDLING: PREREG.md is LEFT UNEDITED, the correction is recorded in a separate "
                "ADDENDUM-1.md, the 40-digit threshold and every other arm are UNCHANGED, and "
                "the corrected run writes to a NEW path. WHY IT MATTERS: the arm caught a wrong "
                "CONTROL, which is the harder case, because a wrong control that happened to "
                "agree would have certified a broken engine. It is also the third instance in "
                "this run of the same provenance defect -- something derived once, remembered in "
                "compressed form, and reproduced from the compressed memory rather than from the "
                "source (compare S24-12 and S24-13) -- and it recurred INSIDE the session "
                "written to remove exactly that status from the upper bound."
            ),
            "label": "INSPECTED",
            "evidence_type": "file_inspection",
            "dps": None,
            "reproducible": True,
            "script": "scripts/upper_bound.py",
            "output_hash": h_fail,
        },
        {
            "claim_id": "S26-06",
            "task_id": "CT-S26-UPPER-BOUND/proposition-u",
            "claim": (
                "BOTH INEQUALITIES IN 1 <= r_infinity <= L ARE STRICT for every admissible b, so "
                "L is never attained. r_2 = 1 + 1/(b(1)b(2)) > 1 = r_1 gives the left, and "
                "1 + x < e^x is strict for x != 0 with eps_n > 0 for every n >= 2, giving the "
                "right. RECORDED ONLY TO FORESTALL THE READING that L might be attained. "
                "NOTHING USES IT, and it is not to be stated in the paper as if it were part of "
                "the result."
            ),
            "label": "STRUCTURAL",
            "evidence_type": "file_inspection",
            "dps": None,
            "reproducible": True,
            "script": "scripts/upper_bound.py",
            "output_hash": h_ok,
        },
        {
            "claim_id": "S26-07",
            "task_id": "CT-S26-UPPER-BOUND/drafting",
            "claim": (
                "THE OUTLINE'S ONE OPEN DRAFTING ITEM IS CLOSED, and the pre-declared fallback "
                "was NOT taken. OUTLINE.md at revision 5 recorded the upper bound as an "
                "'unfolded drafting addition CARRYING NO CLAIM ID', to be proved at drafting or "
                "else dropped back to the one-sided statement (S24-21(a)); REPORT.md section 5 "
                "of CT-S24-PAPER-OUTLINE carried it as the session's single open item. It now "
                "carries S26-01. CONSEQUENCES FOR DRAFTING: (i) OUTLINE.md section 1 paragraph "
                "2's phrase 'together with a two-sided bound' is now backed and needs no "
                "weakening; (ii) the insertion point is immediately after prop:positive in "
                "CT-S1-THEOREM/theorem.tex, hypothesised identically to it, about fifteen lines "
                "of LaTeX; (iii) theorem.tex is NOT modified here, because it belongs to an "
                "earlier session and this corpus does not edit earlier sessions -- the result "
                "lives in CT-S26-UPPER-BOUND/PROOF.md and the outline references it; (iv) the "
                "upper half must not be written citing S1-02. WHAT IS NOT ESTABLISHED: no "
                "closed form for r_infinity is claimed for any b, and in particular the "
                "numerical value 2.2794713259205270753 computed for b(n) = n at n = 20000 is "
                "reported as a bound check only and is NOT asserted to equal any named constant."
            ),
            "label": "INSPECTED",
            "evidence_type": "file_inspection",
            "dps": None,
            "reproducible": True,
            "script": "scripts/upper_bound.py",
            "output_hash": h_ok,
        },
    ]


def main() -> int:
    for p in (FAIL_RUN, OK_RUN):
        assert p.exists(), f"missing artefact {p}"
        assert p.stat().st_size > 0, f"empty artefact {p}"
    h_fail, h_ok = sha256(FAIL_RUN), sha256(OK_RUN)
    print(f"{FAIL_RUN.name}: {h_fail}")
    print(f"{OK_RUN.name}: {h_ok}")
    assert h_fail != h_ok, "the two runs hash the same -- one was overwritten"

    fail_txt = FAIL_RUN.read_text(encoding="utf-8").strip().splitlines()[-1]
    ok_txt = OK_RUN.read_text(encoding="utf-8").strip().splitlines()[-1]
    assert fail_txt == "VERDICT: FAIL", f"FAIL run does not end in FAIL: {fail_txt!r}"
    assert ok_txt == "VERDICT: OK", f"corrected run does not end in OK: {ok_txt!r}"
    print(f"verdicts read back from disk: {fail_txt!r} / {ok_txt!r}")

    if CLAIMS.exists():
        print("claims.jsonl already exists; refusing to overwrite")
        return 2

    rows = build(h_fail, h_ok)
    with open(CLAIMS, "w", encoding="utf-8", newline="\n") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=True) + "\n")

    back = [json.loads(l) for l in CLAIMS.read_text(encoding="utf-8").splitlines() if l.strip()]
    assert len(back) == len(rows), "read-back row count mismatch"
    for r in back:
        assert r["output_hash"] in (h_fail, h_ok), f"{r['claim_id']} bad hash"
        assert not (r["label"] == "PROVEN" and r["evidence_type"] == "file_inspection"), \
            f"{r['claim_id']} violates invariant 1(a)"
    assert sha256(FAIL_RUN) == h_fail and sha256(OK_RUN) == h_ok, "an artefact moved"
    print(f"wrote and read back {len(back)} claims: {', '.join(r['claim_id'] for r in back)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
