"""CT-S22 STAGE 3 - the vacuity pre-check, run BEFORE any leaf transport.

PREREG 5, verbatim and unchanged:

  Perturb the point off the leaf: (q,p) -> (q+delta, p) and (q,p) -> (q, p+delta)
  at delta = 1e-6 and delta = 1e-8, holding t = t0 and theta fixed, rebuild A(z)
  from (4.1), and recompute (x1,x2,x3).

  REQUIRED: max_i |Delta x_i| > 1e-15 at delta = 1e-6, and the response must be
  first order: the ratio of max_i|Delta x_i| at 1e-6 to that at 1e-8 must lie in
  [50, 200].

  FIRES IF either (i) max_i|Delta x_i| <= 1e-15 at delta = 1e-6, or (ii) the
  ratio falls outside [50,200].  If it fires the whole test is void and the
  session HALTS.  No Stage 4 number is reported in that case.

The perturbed points remain inside the (0,0,1) family: b(z) is constructed so
that det A(0) = -theta_0^2/4 and det A(1) = -theta_1^2/4 hold IDENTICALLY in
(p,q), so theta_0 = theta_1 = 0 and s1 = s2 = 2 still.  They leave the PV leaf,
which is what the pre-check needs.  This is asserted, not assumed.

The convention is NOT re-derived here.  Stage 2 determined it uniquely as
right|ccw|infcw|10; this script asserts that the same convention still satisfies
all four PREREG 2.3 conditions at every perturbed point, and would halt if a
perturbation silently changed it.

NOTE on what a PASS here does and does not mean.  Stage 2 found
max|grad F| = 21.24 at the point, so the trace coordinates are NOT degenerate on
the cubic - the risk this pre-check exists to catch was already known to be
absent before it ran.  A pass is therefore expected; it is still run, because a
falsifier that is only run when it might fire is not a falsifier.
"""
import hashlib
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import stage2_systemC as S2
from solver import Continuer, formal_at_infinity, formal_value, mnorm

mp.mp.dps = S2.DPS
R = S2.R
CONVENTION = None      # derived from the PREREG 2.3 test at the baseline point
OUT = []


def say(s=""):
    print(s)
    OUT.append(s)


def x_at(p, q, t, thi, order=230):
    """(x1,x2,x3) and the four PREREG 2.3 residuals at an arbitrary (p,q)."""
    z, a, b, c = S2.family_polys(p, q, t, thi)
    ac = S2.to_mp_coeffs(a, z, 2)
    bc = S2.to_mp_coeffs(b, z, 2)
    cc = S2.to_mp_coeffs(c, z, 2)
    Amat = [mp.matrix([[ac[k], bc[k]], [cc[k], -ac[k]]]) for k in range(3)]
    nmat = [-Ak for Ak in Amat]
    dpol = [mp.mpf(0), mp.mpf(-1), mp.mpf(1)]
    tn = mp.mpmathify(sp.N(t, S2.DPS + 20))
    thin = mp.mpmathify(sp.N(thi, S2.DPS + 20))

    # the family constraints must still hold identically in (p,q)
    A0 = -S2.Aval(Amat, mp.mpf(0))
    A1 = S2.Aval(Amat, mp.mpf(1))
    assert abs(mp.det(A0)) < S2.THRESH, "perturbed point left the theta_0 = 0 family"
    assert abs(mp.det(A1)) < S2.THRESH, "perturbed point left the theta_1 = 0 family"

    nterms = int(mp.floor(abs(tn * R)))
    T, Lam, L, F = formal_at_infinity(nmat, dpol, order, lam_first=tn / 2)
    logR = mp.log(R)
    Y0 = formal_value(T, Lam, L, F, R, logR, nterms)
    cont = Continuer(nmat, dpol, [mp.mpf(0), mp.mpf(1)], h_factor=4)
    ends = S2.loops(cont, Y0, logR)
    alpha_pred = mp.e ** (2j * mp.pi * (thin / 2))
    global CONVENTION
    if CONVENTION is None:
        CONVENTION, rep = S2.unique_convention(ends, Y0, alpha_pred)
        return rep["x"], rep
    cands = S2.candidate_conventions(ends, Y0, Y0 ** -1)
    rep = S2.evaluate_convention(CONVENTION, cands[CONVENTION], alpha_pred)
    assert rep["pass"], (
        f"the Stage-2 convention {CONVENTION} no longer satisfies PREREG 2.3 at "
        f"this point: c1={rep['c1']} alpha={rep['alpha_err']} "
        f"shape={rep['shape']} cubic={rep['cubic']}")
    return rep["x"], rep


def main():
    say("=" * 74)
    say("CT-S22 STAGE 3 - vacuity pre-check (PREREG 5), run before Stage 4")
    say(f"dps = {S2.DPS}   branch {S2.BRANCH}   convention: derived below by the "
        f"PREREG 2.3 test")
    say("=" * 74)

    p0, q0, t, thi = S2.exact_point()
    x0, rep0 = x_at(p0, q0, t, thi)
    say("\nbaseline (on the leaf):")
    say(f"  UNIQUE convention from PREREG 2.3: {CONVENTION}")
    for i, v in enumerate(x0, 1):
        say(f"  x{i} = {mp.nstr(v, 30)}")
    say(f"  [convention residuals: MMM-I {mp.nstr(rep0['c1'],4)}, "
        f"alpha {mp.nstr(rep0['alpha_err'],4)}, cubic {mp.nstr(rep0['cubic'],4)}]")

    results = {}
    for dlabel, dexp in (("1e-6", 6), ("1e-8", 8)):
        d = sp.Rational(1, 10 ** dexp)
        for vname, pp, qq in (("q", p0, q0 + d), ("p", p0 + d, q0)):
            x, _ = x_at(pp, qq, t, thi)
            dx = [abs(x[i] - x0[i]) for i in range(3)]
            m = max(dx)
            results[(vname, dlabel)] = m
            say(f"\nperturb {vname} by {dlabel}:")
            for i in range(3):
                say(f"  |dx{i+1}| = {mp.nstr(dx[i], 12)}")
            say(f"  max |dx| = {mp.nstr(m, 12)}")

    say("\n" + "-" * 74)
    say("PREREG 5 verdict")
    say("-" * 74)
    fired = False
    for vname in ("q", "p"):
        m6 = results[(vname, "1e-6")]
        m8 = results[(vname, "1e-8")]
        ratio = m6 / m8
        ok_size = m6 > mp.mpf(10) ** -15
        ok_ratio = mp.mpf(50) <= ratio <= mp.mpf(200)
        say(f"  direction {vname}:  max|dx| at 1e-6 = {mp.nstr(m6,10)}  "
            f"(> 1e-15 ? {'YES' if ok_size else 'NO'})")
        say(f"               ratio (1e-6)/(1e-8) = {mp.nstr(ratio,12)}  "
            f"(in [50,200] ? {'YES' if ok_ratio else 'NO'})")
        if not (ok_size and ok_ratio):
            fired = True
    if fired:
        say("\n  *** THE VACUITY PRE-CHECK FIRED.  The observable cannot see the")
        say("      perturbation, so a 30-digit agreement in Stage 4 would be")
        say("      agreement about nothing.  HALT: no Stage 4 number is reported.")
    else:
        say("\n  [PASS] the observable responds at first order and far above the")
        say("         threshold.  Stage 4 may proceed.")
        say("  Scope: this establishes SENSITIVITY of (x1,x2,x3) to (q,p) at t0.")
        say("  It does not establish that the Stage-4 agreement, if obtained, is")
        say("  evidence of leaf membership in general - only that the test is")
        say("  not vacuous at this point.")
    return not fired


if __name__ == "__main__":
    ok = main()
    outp = Path(__file__).resolve().parent.parent / "outputs" / f"stage3_vacuity{S2.TAG}.out.txt"
    text = "\n".join(OUT) + "\n"
    outp.write_text(text, encoding="utf-8")
    back = outp.read_text(encoding="utf-8")
    assert back == text, "read-back of the output file differs from what was written"
    print(f"\nwritten {outp}  sha256 {hashlib.sha256(back.encode()).hexdigest()}")
    sys.exit(0 if ok else 2)
