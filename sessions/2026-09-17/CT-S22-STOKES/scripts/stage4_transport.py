"""CT-S22 STAGE 4 - leaf transport along Painleve V.

PREREG / operator packet, unchanged:

  Integrate PV in t from t0 to t1 = t0 + eps, for two values of eps differing by
  a decade.  Rebuild the linear system at t1 from (q(t1), p(t1)) and recompute
  x, y, z.
  PASS: agreement with Stage 2 to >= 30 digits, at both eps, with the residual
  scaling as expected in eps.
  FAIL: anything less.  A failure falsifies THIS construction, not membership in
  general - say so explicitly in the verdict.

THE FLOW, from vdPS (4.2) p.2655, with theta_0 = theta_1 = 0 (the middle term
of dp/dt then vanishes identically and is dropped, not approximated):

  dq/dt = 2p/t
  dp/dt = (2q-1)p^2/((q-1) q t) + (1/4)(q-1)q(2qt - t + 2 theta_inf - 2)

TRANSPORT METHOD: Taylor series in s = t - t0, coefficients from the exact
recurrences below, no finite differences anywhere.

  q:  q'(s) t(s) = 2p  ->  t0 (k+1) q_{k+1} + k q_k = 2 p_k
  p:  clear denominators with 4 G t, G = (q-1)q:
          4 G t p' = 4(2q-1)p^2 + G^2 t H,   H = 2qt - t + 2 theta_inf - 2
      ->  p_{k+1} = [RHS_k - sum_{j=1..k} C_j (k-j+1) p_{k-j+1}] / (C_0 (k+1))
      with C = 4 G t.

CONTROLS, all assertions that can fail:
  C-T1  the mpmath construction of A(z) agrees with the sympy construction of
        Stage 2 at the exact point (the two code paths are independent).
  C-T2  the Taylor series satisfies the PV system at t1: both residuals
        |q'(t1) - 2p/t| and |p'(t1) - RHS| are at the truncation level.
  C-T3  one step of size eps agrees with two steps of size eps/2.
  C-D   DISCRIMINATION.  The same transport run with a deliberately WRONG
        vector field (the (2 theta_inf - 2) term dropped) must MOVE the trace
        coordinates far above the threshold.  Without this, a PASS at Stage 4
        could be a transport that barely moved.
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
KORD = int(__import__("os").environ.get("S22_KORD", "110"))
# PREREG 4/Stage 4 requires two eps a decade apart; that pair is the default.
# A longer list only ADDS measurements - it does not relax the >= 30 digit
# threshold, which is applied to every eps in the list.
EPSLAB = [s.strip() for s in
          __import__("os").environ.get("S22_EPS", "1e-3,1e-4").split(",")]
ETAG = "" if EPSLAB == ["1e-3", "1e-4"] else "_eps" + str(len(EPSLAB))
OUT = []


def say(s=""):
    print(s)
    OUT.append(s)


# ------------------------------------------------- A(z) directly in mpmath
def mp_family(p, q, t, thi):
    """Coefficient matrices of the (4.1) numerator, ascending in z, theta_0 =
    theta_1 = 0.  Expanded by hand from the same expressions Stage 2 feeds to
    sympy; C-T1 checks the two against each other."""
    half = mp.mpf(1) / 2
    A = half * (-2 * q * t + t - thi)
    B = -half * t
    a = [p - A * q + B * q ** 2, A - 2 * B * q, B]
    c = [q / (q - 1), -1 / (q - 1), mp.mpf(0)]
    inner = p + half * (q - 1) * q * t
    b1 = -(inner ** 2 - (q - 1) * q * thi ** 2 / 4) / q
    fac = p + half * ((q - 1) * q * t + q * thi)
    b0 = -((q - 1) / q) * fac ** 2
    b = [b0, b1, mp.mpf(0)]
    return [mp.matrix([[a[k], b[k]], [c[k], -a[k]]]) for k in range(3)]


def x_from_mp(p, q, t, thi, order=230):
    Amat = mp_family(p, q, t, thi)
    nmat = [-Ak for Ak in Amat]
    dpol = [mp.mpf(0), mp.mpf(-1), mp.mpf(1)]
    A0 = -S2.Aval(Amat, mp.mpf(0))
    A1 = S2.Aval(Amat, mp.mpf(1))
    assert abs(mp.det(A0)) < S2.THRESH and abs(mp.det(A1)) < S2.THRESH, \
        "point left the (0,0,1) family"
    nterms = int(mp.floor(abs(t * R)))
    T, Lam, L, F = formal_at_infinity(nmat, dpol, order, lam_first=t / 2)
    logR = mp.log(R)
    Y0 = formal_value(T, Lam, L, F, R, logR, nterms)
    cont = Continuer(nmat, dpol, [mp.mpf(0), mp.mpf(1)], h_factor=4)
    ends = S2.loops(cont, Y0, logR)
    alpha_pred = mp.e ** (2j * mp.pi * (thi / 2))
    global CONVENTION
    if CONVENTION is None:
        CONVENTION, rep = S2.unique_convention(ends, Y0, alpha_pred)
        return rep["x"], rep
    cands = S2.candidate_conventions(ends, Y0, Y0 ** -1)
    rep = S2.evaluate_convention(CONVENTION, cands[CONVENTION], alpha_pred)
    assert rep["pass"], (
        f"the convention {CONVENTION} fails PREREG 2.3 at the transported point")
    return rep["x"], rep


# -------------------------------------------------------- the PV transport
def conv(Aa, Bb, k):
    s = mp.mpf(0)
    for i in range(k + 1):
        if i < len(Aa) and (k - i) < len(Bb):
            s += Aa[i] * Bb[k - i]
    return s


def pv_series(p0, q0, t0, thi, K=KORD, drop_const=False):
    """Taylor coefficients of (q,p) in s = t - t0 for the PV flow (4.2)."""
    q = [q0]
    p = [p0]
    ts = [t0, mp.mpf(1)]
    const = mp.mpf(0) if drop_const else 2 * thi - 2
    for k in range(K):
        n = k + 1
        # series built from what is already known (indices 0..k)
        qm1 = [q[i] - (1 if i == 0 else 0) for i in range(k + 1)]
        G = [conv(qm1, q, i) for i in range(k + 1)]
        Gt = [conv(G, ts, i) for i in range(k + 1)]
        C = [4 * v for v in Gt]
        qt = [conv(q, ts, i) for i in range(k + 1)]
        H = [2 * qt[i] - (ts[i] if i < len(ts) else mp.mpf(0))
             + (const if i == 0 else 0) for i in range(k + 1)]
        G2 = [conv(G, G, i) for i in range(k + 1)]
        G2t = [conv(G2, ts, i) for i in range(k + 1)]
        term2 = conv(G2t, H, k)
        p2 = [conv(p, p, i) for i in range(k + 1)]
        twoq = [2 * q[i] - (1 if i == 0 else 0) for i in range(k + 1)]
        term1 = 4 * conv(twoq, p2, k)
        rhs = term1 + term2
        acc = mp.mpf(0)
        for j in range(1, k + 1):
            acc += C[j] * (k - j + 1) * p[k - j + 1]
        assert abs(C[0]) > mp.mpf(10) ** (-S2.DPS + 20), "PV transport: C_0 = 0"
        p.append((rhs - acc) / (C[0] * n))
        q.append((2 * p[k] - k * q[k]) / (t0 * n))
    return q, p


def evalser(cs, s):
    v = mp.mpf(0)
    sp_ = mp.mpf(1)
    for c in cs:
        v += c * sp_
        sp_ = sp_ * s
    return v


def dser(cs, s):
    v = mp.mpf(0)
    sp_ = mp.mpf(1)
    for k in range(1, len(cs)):
        v += k * cs[k] * sp_
        sp_ = sp_ * s
    return v


def transport(p0, q0, t0, thi, eps, nsteps=1, K=KORD, drop_const=False):
    p_, q_, t_ = p0, q0, t0
    h = eps / nsteps
    for _ in range(nsteps):
        qs, ps = pv_series(p_, q_, t_, thi, K, drop_const)
        q_, p_ = evalser(qs, h), evalser(ps, h)
        t_ = t_ + h
    return p_, q_, t_


def pv_residual(p0, q0, t0, thi, eps, K=KORD):
    qs, ps = pv_series(p0, q0, t0, thi, K)
    s = eps
    q1, p1 = evalser(qs, s), evalser(ps, s)
    t1 = t0 + s
    dq, dp = dser(qs, s), dser(ps, s)
    rq = dq - 2 * p1 / t1
    rp = dp - ((2 * q1 - 1) * p1 ** 2 / ((q1 - 1) * q1 * t1)
               + (q1 - 1) * q1 * (2 * q1 * t1 - t1 + 2 * thi - 2) / 4)
    return abs(rq), abs(rp), q1, p1, t1


def digits(x):
    x = abs(x)
    return mp.inf if x == 0 else -mp.log10(x)


def main():
    say("=" * 74)
    say("CT-S22 STAGE 4 - leaf transport along Painleve V")
    say(f"dps = {S2.DPS}   branch {S2.BRANCH}   Taylor order K = {KORD}")
    say("=" * 74)

    pe, qe, te, thie = S2.exact_point()
    N = S2.DPS + 20
    p0 = mp.mpmathify(sp.N(pe, N))
    q0 = mp.mpmathify(sp.N(qe, N))
    t0 = mp.mpmathify(sp.N(te, N))
    thi = mp.mpmathify(sp.N(thie, N))

    # ---- C-T1 -----------------------------------------------------------
    say("\n--- C-T1  mpmath and sympy constructions of A(z) agree --------------")
    Asym = S2.build_system()[0]
    Amp = mp_family(p0, q0, t0, thi)
    worst = max(mnorm(Asym[k] - Amp[k]) for k in range(3))
    say(f"  max |A_sympy - A_mpmath| = {mp.nstr(worst,6)}   "
        f"({mp.nstr(digits(worst),5)} digits)")
    assert worst < S2.THRESH, "C-T1 failed: the two constructions of A(z) differ"
    say("  [PASS]")

    # ---- baseline --------------------------------------------------------
    x0, rep0 = x_from_mp(p0, q0, t0, thi)
    say("\nbaseline at t0 (recomputed through the mpmath path):")
    say(f"  UNIQUE convention from PREREG 2.3: {CONVENTION}")
    for i, v in enumerate(x0, 1):
        say(f"  x{i} = {mp.nstr(v, 40)}")
    say(f"  [MMM-I {mp.nstr(rep0['c1'],4)}  cubic {mp.nstr(rep0['cubic'],4)}]")

    unit = t0 / abs(t0)
    results = {}
    for elab in EPSLAB:
        eps = mp.mpf(elab) * unit
        say("\n" + "-" * 74)
        say(f"eps = {elab} * t0/|t0|   ->  t1 = t0 + eps")

        rq, rp, q1, p1, t1 = pv_residual(p0, q0, t0, thi, eps)
        say(f"  C-T2 PV residual at t1:  |q' - 2p/t| = {mp.nstr(rq,6)}   "
            f"|p' - RHS| = {mp.nstr(rp,6)}")
        assert rq < S2.THRESH and rp < S2.THRESH, \
            "C-T2 failed: the Taylor series does not satisfy PV at t1"

        p1b, q1b, _ = transport(p0, q0, t0, thi, eps, nsteps=2)
        d12 = max(abs(q1 - q1b), abs(p1 - p1b))
        say(f"  C-T3 one step vs two half-steps: {mp.nstr(d12,6)}   "
            f"({mp.nstr(digits(d12),5)} digits)")
        assert d12 < S2.THRESH, "C-T3 failed: the transport is not converged"

        say(f"  q(t1) = {mp.nstr(q1, 30)}")
        say(f"  p(t1) = {mp.nstr(p1, 30)}")

        x1, rep1 = x_from_mp(p1, q1, t1, thi)
        say(f"  [MMM-I {mp.nstr(rep1['c1'],4)}  alpha {mp.nstr(rep1['alpha_err'],4)}"
            f"  cubic {mp.nstr(rep1['cubic'],4)}]")
        dx = [abs(x1[i] - x0[i]) for i in range(3)]
        for i in range(3):
            say(f"  |x{i+1}(t1) - x{i+1}(t0)| = {mp.nstr(dx[i],8)}   "
                f"({mp.nstr(digits(dx[i]),6)} digits)")
        m = max(dx)
        results[elab] = m
        say(f"  worst coordinate agreement: {mp.nstr(digits(m),6)} digits")

    # ---- C-D  discrimination -------------------------------------------
    say("\n" + "-" * 74)
    say("C-D  discrimination: the same transport with a WRONG vector field")
    say("     (the constant 2 theta_inf - 2 dropped from dp/dt)")
    eps = mp.mpf("1e-3") * unit
    pw, qw, tw = transport(p0, q0, t0, thi, eps, nsteps=1, drop_const=True)
    xw, _ = x_from_mp(pw, qw, tw, thi)
    dw = max(abs(xw[i] - x0[i]) for i in range(3))
    say(f"  max |x(wrong flow) - x(t0)| = {mp.nstr(dw,8)}")
    assert dw > mp.mpf(10) ** -15, \
        "C-D failed: a WRONG vector field also leaves x unmoved - the Stage 4 " \
        "agreement would not be evidence of anything"
    say(f"  [PASS] the wrong flow moves the coordinates by {mp.nstr(dw,6)}, so a")
    say("         30-digit agreement under the right flow is discriminating.")

    # ---- verdict ---------------------------------------------------------
    say("\n" + "=" * 74)
    say("STAGE 4 VERDICT")
    say("=" * 74)
    ok = True
    for elab in EPSLAB:
        d = digits(results[elab])
        good = d >= 30
        ok = ok and good
        say(f"  eps = {elab}:  agreement {mp.nstr(d,6)} digits   "
            f"({'PASS' if good else 'FAIL'}, need >= 30)")
    for i in range(len(EPSLAB) - 1):
        a, b = EPSLAB[i], EPSLAB[i + 1]
        r = results[a] / results[b] if results[b] != 0 else mp.inf
        say(f"  residual ratio ({a})/({b}) = {mp.nstr(r, 8)}")
    say("  ON THE SCALING, stated carefully.  The trace coordinates are constant")
    say("  along the isomonodromic flow, so the residual is error, not signal.")
    say("  A ratio near 10 per decade means the residual is LINEAR in eps.")
    say("  Whether that linear behaviour is meaningful cannot be decided from a")
    say("  single dps: it is decided by whether the SAME numbers reappear when")
    say("  dps changes while the dps-limited controls improve.  That comparison")
    say("  is made across runs, in REPORT.md, not asserted here.")
    say(f"  For that comparison, the dps-INDEPENDENT quantity to watch is the")
    say(f"  alpha residual printed above; dps for this run = {S2.DPS}.")
    if ok:
        say("\n  PASS.  The point transports along PV with the trace coordinates")
        say("  constant to the stated precision.  LABEL: VERIFIED, not PROVEN.")
    else:
        say("\n  FAIL.  Scope, stated explicitly as the packet requires:")
        say("  this falsifies THIS CONSTRUCTION - this transport, at this point,")
        say("  with these conventions - and NOT membership in general.")
    return ok


if __name__ == "__main__":
    ok = main()
    outp = Path(__file__).resolve().parent.parent / "outputs" / f"stage4_transport{S2.TAG}{ETAG}.out.txt"
    text = "\n".join(OUT) + "\n"
    outp.write_text(text, encoding="utf-8")
    back = outp.read_text(encoding="utf-8")
    assert back == text, "read-back of the output file differs from what was written"
    print(f"\nwritten {outp}  sha256 {hashlib.sha256(back.encode()).hexdigest()}")
    sys.exit(0 if ok else 2)
