"""CT-S22 - emit claims.jsonl.

Every numerical claim traces to a script in this session folder and to a hashed
output file.  The hash is computed HERE from the file on disk; no hash is typed
in by hand.  The file is read back and re-parsed after writing.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTD = ROOT / "outputs"


def h(name):
    p = OUTD / name
    assert p.exists(), f"missing output file: {p}"
    return hashlib.sha256(p.read_bytes()).hexdigest()


S1 = "stage1_kummer2_run3.out.txt"
S1A = "stage1_kummer.out.txt"
S2 = "stage2_systemC.out.txt"
S2R1 = "stage2_systemC_run1.out.txt"
S3 = "stage3_vacuity.out.txt"
S4 = "stage4_transport.out.txt"
ALG = "algebra_checks.out.txt"
S4D = "stage4_transport_dps320.out.txt"
S4E = "stage4_transport_eps3.out.txt"
S2B = "stage2_systemC_b2.out.txt"
S3B = "stage3_vacuity_b2.out.txt"
S4B = "stage4_transport_b2.out.txt"
BR  = "branch_relation.out.txt"
G16 = "gamma16_identity.out.txt"
P5B = "stage5b_pslq.out.txt"
PSY = "branch_symmetry.out.txt"

C = [
    ("S22-01", "stage1", "The solver reproduces Kummer's monodromy, formal and "
     "Stokes data against closed forms: 32 of 32 checks pass at >= 35 digits "
     "(44-151 observed) at both pre-registered parameter values.",
     "computation", 150, "scripts/stage1_kummer2.py", S1, "VERIFIED"),
    ("S22-02", "stage1", "Kummer's companion system is not trace-free "
     "(tr B = 1 - b/z), so det M_0 = e^{-2 pi i b} != 1 and the vdPS SL2 "
     "factorisation requires the trace-free gauge.",
     "computation", 150, "scripts/stage1_kummer.py", S1A, "STRUCTURAL"),
    ("S22-03", "stage1", "The counterclockwise circle at infinity is homotopic "
     "to gamma_0; vdPS's M_inf is the CLOCKWISE loop, hence their alpha is "
     "e^{-2 pi i L_11}.",
     "computation", 150, "scripts/stage1_kummer2.py", S1, "STRUCTURAL"),
    ("S22-04", "stage1", "Check A6a as first written was algebraically vacuous: "
     "(1 + f1 f2)/alpha = M_22 equals (1 - det M)/m11 and so vanishes "
     "identically for any unimodular M with M_11 != 0, so it could not fail. "
     "Proved by simplify-to-zero plus an independent numeric arm.",
     "computation", 50, "scripts/algebra_checks.py", ALG, "PROVEN"),
    ("S22-05", "stage1", "Check A7 as first written used vdPS's "
     "diag*lower*upper ordering (trace alpha + (1+f1 f2)/alpha) against a "
     "computed diag*upper*lower factorisation (trace alpha(1+f1 f2) + "
     "1/alpha); the two differ by (alpha - 1/alpha) f1 f2. At the Stage-1 "
     "values the wrong ordering misses 2cos(pi b) by 0.9612 while the "
     "corrected one holds to 1.15e-29, reproducing the observed O(1) failure. "
     "The corrected identity is a DEPENDENT restatement of A4a+A5+A6e, not "
     "independent evidence.",
     "computation", 50, "scripts/algebra_checks.py", ALG, "PROVEN"),
    ("S22-06", "stage2", "At the CT-S16 point the printed (4.1) family satisfies "
     "det A_0 = det A_1 = 0 exactly and A_inf = (t/2) diag(-1,1) to 121 digits.",
     "computation", 200, "scripts/stage2_systemC.py", S2, "VERIFIED"),
    ("S22-07", "stage2", "(A_0 + A_1)_11 = -theta_inf/2, contradicting the prose "
     "of vdPS p.2629 which states it is theta_inf. CT-S16's finding, "
     "reconfirmed at the numeric point and relied on nowhere.",
     "computation", 200, "scripts/stage2_systemC.py", S2, "VERIFIED"),
    ("S22-08", "stage2", "L_11 = theta_inf/2 exactly, hence alpha = "
     "e^{+- i pi theta_inf} in closed form with |alpha| = 1 and |arg alpha| = "
     "pi sqrt(3)/9 = 0.60459978807807261686; both predicted before the run and "
     "both hit.",
     "computation", 200, "scripts/stage2_systemC.py", S2, "VERIFIED"),
    ("S22-09", "stage2", "The truncated formal series' residual sits at the "
     "minimal term of the series (ratio 1.29, bound N^3) and decays at the "
     "predicted Gevrey rate e^{-|t| R} between R = 160 and R = 140 "
     "(observed/predicted 1.259).",
     "computation", 200, "scripts/stage2_systemC.py", S2, "VERIFIED"),
    ("S22-10", "stage2", "PREREG 2.3's 8-element candidate set tied the "
     "orientation of gamma_inf to that of the small loops and so could not "
     "represent gamma_0 gamma_1 = gamma_inf; none of the 8 passed (best "
     "||MMM-I|| = 6.85). Widened to 16 with the four conditions and the 1e-30 "
     "threshold unchanged.",
     "computation", 120, "scripts/stage2_systemC.py", S2R1, "STRUCTURAL"),
    ("S22-11", "stage2", "Over the 16 candidate conventions EXACTLY ONE "
     "satisfies all four PREREG 2.3 conditions: right action, small loops ccw, "
     "M_inf clockwise, vdPS M_1 = gamma_1. ||M_0 M_1 M_inf - I|| = 2.44e-105; "
     "the other 15 fail, several on alpha alone (0.327, 2.27, 2.34).",
     "computation", 200, "scripts/stage2_systemC.py", S2, "VERIFIED"),
    ("S22-12", "stage2", "Trace coordinates of System C at t0: x1 = "
     "-3.4791908904110720783362611334763347 - "
     "1.085013570276491408740290278433511 i; x2 = "
     "5.0274753770206575050513601616191382 + "
     "2.3656209874946766465307178962989066 i; x3 = "
     "1.9725752524636335304002661101339216; alpha = "
     "0.82272965712005465178275844880452679 + "
     "0.56843285557321306726020179279562511 i. Error bar 8.49e-105 from step "
     "halving h = rho/4 vs rho/8 (273 vs 487 steps), not from a single run.",
     "computation", 200, "scripts/stage2_systemC.py", S2, "VERIFIED"),
    ("S22-13", "stage2", "The point is a SMOOTH point of the singular cubic "
     "fibre: the fibre is singular because s1 = s2 = 2 puts it on two resonance "
     "divisors, but grad F = (1.523094, 1.5231748, 21.240405) in modulus is "
     "non-zero there, so the coordinates retain first-order sensitivity.",
     "computation", 200, "scripts/stage2_systemC.py", S2, "VERIFIED"),
    ("S22-14", "stage3", "The observable is sensitive to leaf membership: "
     "max|dx_i| = 8.686e-6 (direction q) and 2.639e-5 (direction p) at "
     "delta = 1e-6, against a 1e-15 floor, with first-order ratios 99.99978 and "
     "99.99956 inside the pre-registered [50,200].",
     "computation", 200, "scripts/stage3_vacuity.py", S3, "VERIFIED"),
    ("S22-15", "stage4", "System C's point transports along Painleve V with the "
     "trace coordinates x1, x2, x3 constant to 90.81 digits at eps = 1e-3 and "
     "91.83 digits at eps = 1e-4, against a 30-digit threshold. Gap S16-15 "
     "closed NUMERICALLY. This is a numerical agreement at one point along one "
     "direction in t; it is not a proof of leaf membership.",
     "computation", 200, "scripts/stage4_transport.py", S4, "VERIFIED"),
    ("S22-16", "stage4", "The Stage-4 test discriminates: the same transport "
     "run with a deliberately wrong vector field (the constant 2 theta_inf - 2 "
     "dropped from dp/dt) moves the trace coordinates by 3.83e-2.",
     "computation", 200, "scripts/stage4_transport.py", S4, "VERIFIED"),
    ("S22-17", "stage4", "Raising dps from 200 to 320 leaves the Stage-4 "
     "agreement and its ratio unchanged to every printed figure (90.8118, "
     "91.8301, ratio 10.429999) while every dps-limited control improves by "
     "about 120 digits (MMM-I 1.20e-105 -> 5.57e-225; cubic 3.96e-112 -> "
     "7.13e-232; |x3(t1)-x3(t0)| 2.35e-113 -> 3.30e-233), and the alpha "
     "residual stays at 1.834e-91. Over eps = 1e-3, 1e-4, 1e-5 the ratios are "
     "10.430 and 10.034. The residual is therefore a systematic O(eps) error, "
     "not round-off; it is floored by the optimal-truncation level e^-|t|R = "
     "1e-88.7 set by the PRE-REGISTERED R, which no dps can reduce.",
     "computation", 320, "scripts/stage4_transport.py", S4D, "VERIFIED"),
    ("S22-18", "branch2", "Branch 2 of the CT-S16 sign pair (t = +2 sqrt(33) "
     "i/9) passes Stages 2, 3 and 4 independently: the PREREG 2.3 test selects "
     "exactly one convention of 16, right|cw|infccw|01; Stage 3 ratios 99.9952 "
     "and 99.9998; Stage 4 agreement 90.82 and 91.84 digits against the "
     "30-digit threshold. Branch 2 was RUN, not inferred.",
     "computation", 200, "scripts/stage4_transport.py", S4B, "VERIFIED"),
    ("S22-19", "branch2", "Branches 1 and 2 are related by the Galois "
     "automorphism sigma of Q(sqrt3, sqrt11) with sigma(sqrt3) = -sqrt3 and "
     "sigma(sqrt11) = +sqrt11, which maps t, theta_inf, q and p term by term, "
     "each difference simplifying to exactly 0 with an independent numeric arm. "
     "They are NOT complex conjugates. sigma is an automorphism of a number "
     "field and does not act on analytic continuation, so it transfers the "
     "CT-S16 location argument but carries NO monodromy information - which is "
     "why branch 2 had to be run.",
     "computation", 40, "scripts/branch_relation.py", BR, "PROVEN"),
    ("S22-20", "branch2", "The two branches yield the same point of the "
     "character variety up to relabelling: x1 and x2 are interchanged, x3 and "
     "alpha are identical, and the selected conventions are exact mirrors "
     "(right|ccw|infcw|10 vs right|cw|infccw|01). The mirrored convention is a "
     "RESULT of the branch-2 PREREG 2.3 test, not an assumption carried over.",
     "file_inspection", 200, "scripts/branch_relation.py", BR, "VERIFIED"),
    ("S22-21", "stage5", "The PREREG-STAGE5 section 3 search space was "
     "DEGENERATE: Gamma(1/6) = 2^(2/3) sqrt3 Gamma(1/3)^2 / (2 sqrt(pi)) by "
     "Legendre duplication at z=1/6 and reflection at 1/3, so PSLQ returned "
     "that identity with coefficient ZERO on log C, for C and for all three "
     "decoys alike, and the search never tested C. Stage 5A is VOID, not "
     "negative, and its NOT FOUND line is withdrawn. The Stage-5A vacuity "
     "pre-check reported the required 3-decoys-rejected/1-control-accepted "
     "outcome but passed FOR THE WRONG REASON.",
     "computation", 80, "scripts/gamma16_identity.py", G16, "PROVEN"),
    ("S22-22", "stage5", "In the corrected space of PREREG-STAGE5B - the "
     "6-vector over {2, 3, pi, Gamma(1/3)}, first shown independent by a "
     "degeneracy pre-check that returned no relation at any bound - NO "
     "multiplicative relation C = +/- 2^a 3^b pi^c Gamma(1/3)^d e^f exists "
     "with |coeff| <= 1e6, 1 <= |m| <= 12 and digit cost <= 40, against C = "
     "8.1273367954950723671... known to 100 decimal digits; no candidate was "
     "returned at any bound. All three decoys were rejected on their own "
     "merits and the positive control 4 pi^2/(3 Gamma(1/3)) was recognised at "
     "cost 1.51. This EXCLUDES THAT SPACE and is not evidence that C has no "
     "closed form. C is in V_quad NATIVE normalisation; the V_quad -> "
     "P-III(D6) map remains OPEN, so this is not comparable with the Stage 1-4 "
     "quantities of this session.",
     "computation", 120, "scripts/stage5b_pslq.py", P5B, "VERIFIED"),
    # HISTORICAL NOTE, retained deliberately.  A provisional S22-18 once
    # carried the label "NOT DONE".  That is a STATUS, not an epistemic label,
    # and check_invariants.py 2 correctly refused it.  The entry was removed
    # rather than relabelled.  The identifier was later REUSED for the branch-2
    # Stage-4 result above, which carries a real label; Stage 5 was
    # subsequently pre-registered and run (S22-22).
    ("S22-23", "S22-20-structural",
     "For the System C family at both CT-S16 branches the denominator "
     "D(z) = z^2 - z is exactly invariant under phi(z) = 1 - z, so phi fixes "
     "the singular set {0, 1, infinity} setwise and exchanges the two finite "
     "punctures. With theta_0 = theta_1 = 0 the local data at 0 and 1 are "
     "interchangeable, so phi is the only candidate involution that could "
     "produce the observed x1 <-> x2 swap with x3 and alpha fixed.",
     "computation", None, "scripts/branch_symmetry.py", PSY, "PROVEN"),
    ("S22-24", "S22-20-structural",
     "There is NO analytic equivalence between the two CT-S16 branches of the "
     "form A_2(z) = -G A_1(phi(z)) G^{-1} with G a CONSTANT gauge, for any of "
     "the four candidate maps phi in {identity, z -> 1-z, coefficient "
     "conjugation, coefficient conjugation composed with z -> 1-z}. A is "
     "traceless, so det is the only gauge invariant; the necessary scalar "
     "condition P_2(z) = P_1(phi(z)) with P = a^2 + b c FAILS for all four, "
     "with max |coefficient| 3.83, 0.416, 0.416 and 3.83 respectively. The "
     "positive control sigma(P_1) - P_2 returns exactly 0 through the same "
     "radicals, so the negative is informative and not a simplification "
     "failure. CONSEQUENCE: the proposed structural route to S22-20 does not "
     "close, and S22-20 REMAINS VERIFIED-NUMERICAL (two independent runs), "
     "not STRUCTURAL. This refutes the simplest form of the argument only; a "
     "z-dependent gauge is untested and remains open.",
     "computation", None, "scripts/branch_symmetry.py", PSY, "PROVEN"),
]

lines = []
for cid, task, claim, ev, dps, script, out, label in C:
    rec = {
        "claim_id": cid,
        "task_id": f"CT-S22-STOKES/{task}",
        "claim": claim,
        "label": label,
        "evidence_type": ev,
        "dps": dps,
        "reproducible": True,
        "script": script,
        "output_hash": h(out) if out else None,
    }
    lines.append(json.dumps(rec, ensure_ascii=True))

path = ROOT / "claims.jsonl"
text = "\n".join(lines) + "\n"
path.write_text(text, encoding="utf-8")

back = path.read_text(encoding="utf-8")
assert back == text, "read-back differs from what was written"
parsed = [json.loads(l) for l in back.splitlines()]
assert len(parsed) == len(C), "claim count changed on read-back"
labels = sorted({r["label"] for r in parsed})
assert set(labels) <= {"PROVEN", "VERIFIED", "STRUCTURAL",
                       "CONJECTURED"}, f"unknown label in {labels}"
for r in parsed:
    assert r["claim_id"].startswith("S22-"), "wrong id prefix"
    if r["output_hash"]:
        assert len(r["output_hash"]) == 64, "bad sha256"
print(f"wrote {len(parsed)} claims to {path}")
print("labels present:", labels)
for r in parsed:
    print(f"  {r['claim_id']}  {r['label']:<11s} {r['script']}")
