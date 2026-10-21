"""CT-S26-UPPER-BOUND -- numerical check of Proposition U.

Checks the FINITE-n inequality (U-finite) of PROOF.md,

    r_n <= exp( sum_{k=1}^{n-1} 1/(b(k) b(k+1)) ),

which is exact at every n and needs no tail estimate.  The proof is in
PROOF.md and was written before this script was run; this is a check on the
proof and its transcription, not evidence for it.

Arms V1..V6 are as registered in PREREG.md section 5.  Every arm is an
assertion that can fail.  Thresholds are those of PREREG.md section 4 and are
not adjustable here.
"""

import sys
from pathlib import Path

from mpmath import mp

HERE = Path(__file__).resolve().parent
SESSION = HERE.parent
OUT = SESSION / "outputs" / "upper_bound_rev2.out.txt"

DPS = 60
N = 20000
TOL = mp.mpf(10) ** -40          # F1 threshold
V1_DIGITS = 40                   # F2 threshold
V5_SPREAD = mp.mpf("0.01")       # F4 threshold

mp.dps = DPS

_lines = []


def say(s=""):
    print(s)
    _lines.append(s)


def poly(coeffs):
    """coeffs in DESCENDING order; returns b(n) as an mpf callable."""
    cs = [mp.mpf(c) for c in coeffs]

    def b(n):
        acc = mp.mpf(0)
        for c in cs:
            acc = acc * n + c
        return acc

    return b


# ---------------------------------------------------------------- test family
POSITIVE = [
    ("b(n) = n",             [1, 0]),
    ("b(n) = n + 1",         [1, 1]),
    ("b(n) = 2n - 1",        [2, -1]),
    ("b(n) = n/2 + 1/4",     [mp.mpf(1) / 2, mp.mpf(1) / 4]),
    ("b(n) = n^2",           [1, 0, 0]),
    ("b(n) = n^2 + n + 1",   [1, 1, 1]),
    ("b(n) = 3n^2 - 2n + 1", [3, -2, 1]),
    ("b(n) = n^3 + 1",       [1, 0, 0, 1]),
    ("b(n) = 10n",           [10, 0]),
    ("b(n) = 100 n^2",       [100, 0, 0]),
]

# sign-changing, all with b(n) != 0 at every positive integer n
SIGNED = [
    ("b(n) = 2n - 9",          [2, -9]),
    ("b(n) = n - 7/2",         [1, -mp.mpf(7) / 2]),
    ("b(n) = n^2 - 7n + 3",    [1, -7, 3]),
    ("b(n) = n^2 - 10n + 2",   [1, -10, 2]),
    ("b(n) = 3n - 100",        [3, -100]),
    ("b(n) = -n^2 + 5n - 1",   [-1, 5, -1]),
]

CHECKPOINTS = [2, 3, 5, 10, 100, 1000, N]


def run_family(name, coeffs, n_max, require_positive, drop_first_term=False):
    """Iterate (3) of PROOF.md and test (U-finite) in log space.

    Returns (min_log_slack, ratio, checkpoint_rows, n_positive_failures).
    """
    b = poly(coeffs)
    bs = [None] + [b(mp.mpf(k)) for k in range(1, n_max + 2)]

    npos_fail = 0
    for k in range(1, n_max + 2):
        if bs[k] == 0:
            raise AssertionError(f"{name}: b({k}) = 0, violates (A1)")
        if require_positive and bs[k] <= 0:
            npos_fail += 1

    r_prev2 = mp.mpf(1)          # r_0
    r_prev1 = mp.mpf(1)          # r_1
    P = mp.mpf(0)                # sum_{k=1}^{n-1} 1/(b(k)b(k+1)) for n = 1
    min_slack = None
    rows = []
    for n in range(2, n_max + 1):
        eps = 1 / (bs[n - 1] * bs[n])
        P += eps
        if drop_first_term and n == 2:
            P -= eps             # delete the k = 1 term: the V4 weakening
        r = r_prev1 + eps * r_prev2
        if r <= 0:
            slack = None         # log undefined; recorded as a violation below
            min_slack = mp.mpf(-1) * mp.inf
        else:
            slack = P - mp.log(r)
            if min_slack is None or slack < min_slack:
                min_slack = slack
        if n in CHECKPOINTS:
            rows.append((n, r, mp.exp(P), (mp.exp(P) - r) if r > 0 else None))
        r_prev2, r_prev1 = r_prev1, r

    ratio = r_prev1 / mp.exp(P) if r_prev1 > 0 else None
    return min_slack, ratio, rows, npos_fail


def main() -> int:
    say("CT-S26-UPPER-BOUND  --  Proposition U, numerical check")
    say(f"mpmath dps = {mp.dps}   N = {N}   F1 tolerance = 1e-40 (relative)")
    say("Arms as registered in PREREG.md section 5.  Proof: PROOF.md.")
    say("=" * 78)

    failures = []

    # ----------------------------------------------------- V1 known-answer (+)
    say()
    say("V1  known-answer, POSITIVE.  y_n = (-1)^n I_{n+1}(2) solves")
    say("    y_n = n y_{n-1} + y_{n-2},  because I_{v-1}(2) - I_{v+1}(2) = v I_v(2)")
    say("    at v = n gives I_{n-1} - I_{n+1} = n I_n.")
    say("    NOTE: PREREG.md registered this control with y_n = (-1)^n I_n(2),")
    say("    which is wrong by an index shift.  The arm FIRED on the first run")
    say("    (0.30103 digits at n = 2; outputs/upper_bound.out.txt, VERDICT FAIL)")
    say("    and the defect was in the CONTROL, not the engine.  See ADDENDUM-1.md.")
    say("    Threshold UNCHANGED: >= 40 digits for n = 2..40.  (F2 below that.)")
    y = [(-1) ** n * mp.besseli(n + 1, 2) for n in range(0, 41)]
    worst = mp.inf
    worst_n = None
    for n in range(2, 41):
        res = y[n] - (n * y[n - 1] + y[n - 2])
        scale = max(abs(y[n]), abs(n * y[n - 1]), abs(y[n - 2]))
        dig = mp.inf if res == 0 else -mp.log10(abs(res) / scale)
        if dig < worst:
            worst, worst_n = dig, n
    say(f"    worst agreement: {mp.nstr(worst, 6)} digits at n = {worst_n}")
    if worst < V1_DIGITS:
        failures.append("F2: V1 below 40 digits -- engine wrong, no result reported")
        say("    V1 FAIL")
    else:
        say("    V1 PASS")

    # ----------------------------------------------------- V2 known-answer (-)
    say()
    say("V2  known-answer, NEGATIVE.  Perturb y_7 by a relative 1e-20; the same")
    say("    residual must then be LARGE.  Guards a residual that is zero")
    say("    whatever it is fed.  Requires < 25 digits somewhere in n = 7..9.")
    yp = list(y)
    yp[7] = yp[7] * (1 + mp.mpf(10) ** -20)
    best = mp.inf
    for n in (7, 8, 9):
        res = yp[n] - (n * yp[n - 1] + yp[n - 2])
        scale = max(abs(yp[n]), abs(n * yp[n - 1]), abs(yp[n - 2]))
        dig = mp.inf if res == 0 else -mp.log10(abs(res) / scale)
        best = min(best, dig)
    say(f"    best agreement under perturbation: {mp.nstr(best, 6)} digits")
    if best >= 25:
        failures.append("V2: perturbation not detected -- the residual cannot fail")
        say("    V2 FAIL")
    else:
        say("    V2 PASS  (the check can return a negative)")

    # ------------------------------------------------------------- V3 main arm
    say()
    say("V3  MAIN ARM.  (U-finite) at every n <= N, tested in log space as")
    say("    P_{n-1} - log r_n >= 0.  F1 fires below -1e-40.")
    say()
    say(f"    {'b':<22} {'min_n (P - log r_n)':>26}   {'r_N / exp(P)':>22}")
    say("    " + "-" * 74)
    ratios = []
    per_b = {}
    for name, cs in POSITIVE:
        ms, ratio, rows, npos = run_family(name, cs, N, require_positive=True)
        per_b[name] = (ms, ratio, rows)
        ratios.append(ratio)
        if npos:
            failures.append(f"{name}: b(n) <= 0 at {npos} points -- outside Proposition U")
        flag = "" if ms >= -TOL else "   <-- F1"
        if ms < -TOL:
            failures.append(f"F1: {name} violates (U-finite), min slack {mp.nstr(ms, 8)}")
        say(f"    {name:<22} {mp.nstr(ms, 10):>26}   {mp.nstr(ratio, 16):>22}{flag}")
    say()
    say("    All min slacks >= 0: " + ("YES" if all(per_b[n][0] >= -TOL for n, _ in POSITIVE) else "NO"))

    say()
    say("    Checkpoints for b(n) = n:   n,  r_n,  exp(P_{n-1}),  slack")
    for n, r, bd, sl in per_b["b(n) = n"][2]:
        say(f"      n = {n:>6}   r_n = {mp.nstr(r, 20):<24} bound = {mp.nstr(bd, 20):<24} slack = {mp.nstr(sl, 10)}")
    say("    (For b(n) = n the sum is sum 1/(k(k+1)) = 1 exactly, so the")
    say("     limiting bound is L = e = " + mp.nstr(mp.e, 25) + ".)")

    # --------------------------------------------- V4 can the check fail at all
    say()
    say("V4  CAN THE CHECK FAIL?  Re-run V3 against the WEAKENED bound with the")
    say("    k = 1 term deleted.  r_2 = 1 + 1/(b(1)b(2)) > 1 = exp(0), so a")
    say("    correct checker MUST report a violation.  F3 fires if none does.")
    n_viol = 0
    for name, cs in POSITIVE:
        ms, _, _, _ = run_family(name, cs, 200, require_positive=True, drop_first_term=True)
        if ms < -TOL:
            n_viol += 1
    say(f"    families violating the weakened bound: {n_viol} of {len(POSITIVE)}")
    if n_viol == 0:
        failures.append("F3: the inequality check found no violation even when the bound is false")
        say("    V4 FAIL -- V3's passes are uninformative")
    else:
        say("    V4 PASS  (V3's passes are informative: the arm can return a negative)")

    # --------------------------------------------- V5 is the bound informative?
    say()
    say("V5  IS THE BOUND INFORMATIVE?  The ratios r_N / exp(P) must span a")
    say("    range; all-equal-to-1 would mean (U-finite) holds for reasons")
    say("    unrelated to the argument.  F4 fires if the spread is < 0.01.")
    spread = max(ratios) - min(ratios)
    say(f"    min ratio = {mp.nstr(min(ratios), 16)}   max ratio = {mp.nstr(max(ratios), 16)}")
    say(f"    spread    = {mp.nstr(spread, 10)}")
    if spread < V5_SPREAD:
        failures.append("F4: ratio spread below 0.01 -- numerics are weak, say so")
        say("    V5 FAIL")
    else:
        say("    V5 PASS")

    # ------------------------------------------- V6 is positivity load-bearing?
    say()
    say("V6  IS POSITIVITY LOAD-BEARING?  NOT A GATE.  Sign-changing b, all with")
    say("    b(n) != 0 for n >= 1.  A violation shows the hypothesis b > 0 is")
    say("    necessary; no violation is reported as NOT ESTABLISHED, and is NOT")
    say("    evidence that the hypothesis can be dropped.")
    signed_viol = []
    for name, cs in SIGNED:
        ms, ratio, _, _ = run_family(name, cs, 2000, require_positive=False)
        viol = ms < -TOL
        if viol:
            signed_viol.append(name)
        say(f"    {name:<22} min slack = {mp.nstr(ms, 10):>24}   {'VIOLATED' if viol else 'holds'}")
    say()
    if signed_viol:
        say(f"    V6 RESULT: (U-finite) FAILS without positivity, at {len(signed_viol)} of")
        say(f"    {len(SIGNED)} sign-changing b: {', '.join(signed_viol)}.")
        say("    The hypothesis b > 0 is therefore LOAD-BEARING, not decorative.")
    else:
        say(f"    V6 RESULT: no violation found among {len(SIGNED)} sign-changing b.")
        say("    NOT ESTABLISHED that positivity is necessary.  This is recorded as")
        say("    a null search, NOT as licence to drop the hypothesis: Step 1 of")
        say("    PROOF.md consumes positivity and no proof without it is offered.")

    # ------------------------------------------------------------------ verdict
    say()
    say("=" * 78)
    if failures:
        for f in failures:
            say("DEFECT: " + f)
        say("VERDICT: FAIL")
    else:
        say("All registered arms pass at their pre-registered thresholds.")
        say("(U-finite) holds for every tested b at every n <= %d, and V4 shows" % N)
        say("the arm that says so is capable of reporting a violation.")
        say("VERDICT: OK")

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(_lines) + "\n", encoding="utf-8", newline="\n")

    # read back what was written
    back = OUT.read_text(encoding="utf-8").splitlines()
    assert back[-1] == _lines[-1], "read-back mismatch on the verdict line"
    assert len(back) == len(_lines), "read-back mismatch on line count"
    print(f"\n[wrote and read back {OUT} : {len(back)} lines, last = {back[-1]!r}]")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
