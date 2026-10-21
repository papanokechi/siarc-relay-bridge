"""CT-S22 STAGE 2 - monodromy and Stokes data of System C at t0.

Gated on Stage 1, which passed 32/32 checks at >= 35 digits at both parameter
values (outputs/stage1_kummer2_run3.out.txt).

WHAT THIS COMPUTES
  The family (4.1) of van der Put - Saito p.2655 at the CT-S16 point (branch 1),
      A(z) = A_inf + A_0/z + A_1/(z-1) = [[a(z), b(z)], [c(z), -a(z)]]/(z(z-1)),
  the horizontal-section system  Y' = -A(z) Y  (PREREG 2.1), its monodromy
  around z = 0 and z = 1, its Stokes/formal data at z = infinity, and the
  vdPS trace coordinates x1 = d1, x2 = d2, x3 = d3 of p.2630.

b(z) CARRIES THE t.  p.2655 prints  (p + 1/2 (q-1)q)^2  in b(z) and
(p + 1/2 (q-1)q t)^2 in B_1 on the same page.  CT-S16 adopted the reading with
the t from det A(1) = -theta_1^2/4; this script re-checks that constraint at the
numeric point (control C-A) rather than assuming it.

CONVENTION IS DECIDED BY THE PRE-REGISTERED OVERDETERMINED TEST (PREREG 2.3),
not chosen.  Eight candidate conventions (loop order x orientation x action
side); exactly one must satisfy all four listed conditions.  Zero or two or more
is a HALT.

A CONSEQUENCE CARRIED IN FROM STAGE 1.  The Stage-1 A7 correction established
that vdPS's M_inf is the CLOCKWISE loop, so their alpha is e^{-2 pi i L11}, not
e^{+2 pi i L11}.  Both signs are inside the candidate set below, so the test -
not this remark - decides it.  C-5 predicts |alpha| = 1 and alpha =
e^{+- i pi sqrt(3)/9}; the sign is convention and is reported as such.
"""
import hashlib
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from solver import (Continuer, formal_at_infinity, formal_residual,
                    formal_value, mnorm)

DPS = int(__import__("os").environ.get("S22_DPS", "200"))
# Run 2 at dps 120 left only ~25 digits in condition 1.  The cause is not the
# convention and not the solver: on |z| = R the factor e^{Lam z} has
# |e^{Lam z}| = e^{+-|t| R} with |t| R = 204.25, a ONE-SIDED dynamic range of
# 10^88.6, and forward integration contaminates the recessive column at that
# relative level.  It is inherent to the path, not removable by rescaling.
# R is NOT changed - it is pre-registered - and no threshold is changed.  Only
# the working precision, which cannot affect the answer, is raised:
#   88.6 (conditioning) + 30 (threshold) + guard  ->  dps 200.
mp.mp.dps = DPS
THRESH = mp.mpf(10) ** -30
R = mp.mpf(160)          # PREREG 2.3
R_LOOP = mp.mpf("0.25")  # PREREG 2.3

OUT = []
BRANCH = int(__import__("os").environ.get("S22_BRANCH", "1"))
# Output files are tagged so that a branch-2 or higher-precision run cannot
# silently overwrite the branch-1, dps-200 record.
TAG = ("" if BRANCH == 1 else f"_b{BRANCH}") + ("" if DPS == 200 else f"_dps{DPS}")


def say(s=""):
    print(s)
    OUT.append(s)


# --------------------------------------------------------------- the point
def exact_point():
    """CT-S16 branch 1 or 2, verbatim from
    CT-S16-MEMBERSHIP-C/outputs/pq_solution.txt.

    The two branches are related by the Galois automorphism of Q(sqrt3, sqrt11)
    sending sqrt3 -> -sqrt3, sqrt11 -> sqrt11 (hence sqrt33 -> -sqrt33): it maps
    t, q, p, theta_inf of branch 1 to those of branch 2 term by term.  That is an
    ALGEBRAIC symmetry of the family and of the PV equation, so it carries the
    CT-S16 location argument across.  It does NOT carry the monodromy, which is
    transcendental in the entries, so branch 2 is run rather than inferred.
    The branches are NOT complex conjugates: conj(p1) = -p1 flips the sqrt11
    term as well, and p2 does not.
    """
    I = sp.I
    s11, s33, s3 = sp.sqrt(11), sp.sqrt(33), sp.sqrt(3)
    if BRANCH == 1:
        p = 5 * I * (-28151758571 * s33 + 48874838016 * s11) / 4086468672
        q = sp.Rational(1, 2) - 457937 * s11 * I / 122408 + 70425 * s33 * I / 30602
        t = -2 * s33 * I / 9
        thi = -2 - s3 / 9
    elif BRANCH == 2:
        p = 5 * I * (28151758571 * s33 + 48874838016 * s11) / 4086468672
        q = sp.Rational(1, 2) - 70425 * s33 * I / 30602 - 457937 * s11 * I / 122408
        t = 2 * s33 * I / 9
        thi = -2 + s3 / 9
    else:
        raise SystemExit(f"S22_BRANCH must be 1 or 2, got {BRANCH}")
    return p, q, t, thi


def family_polys(p, q, t, thi, th0=0, th1=0):
    """a(z), b(z), c(z) of (4.1), b(z) in the reading that carries the t."""
    z = sp.symbols("z")
    a = p + sp.Rational(1, 2) * (-2 * q * t + t - thi) * (z - q) \
        - sp.Rational(1, 2) * t * (z - q) ** 2
    c = -(z - q) / (q - 1)
    inner = p + sp.Rational(1, 2) * (q - 1) * q * t
    first = -(z * (inner ** 2 - th1 ** 2 / 4
                   + (q - 1) * (th0 ** 2 / 4 - th1 ** 2 / 4
                                - q * thi ** 2 / 4))) / q
    second = -((q - 1)
               * (p + sp.Rational(1, 2) * ((q - 1) * q * t - th0 + q * thi))
               * (p + sp.Rational(1, 2) * ((q - 1) * q * t + th0 + q * thi))) / q
    return z, sp.expand(a), sp.expand(first + second), sp.expand(c)


def to_mp_coeffs(expr, z, deg):
    """ascending list of mpmath coefficients of a polynomial in z"""
    pol = sp.Poly(sp.expand(expr), z)
    out = []
    for k in range(deg + 1):
        cf = pol.coeff_monomial(z ** k) if k > 0 else pol.coeff_monomial(1)
        cf = sp.nsimplify(cf)
        out.append(mp.mpmathify(sp.N(cf, DPS + 20)))
    return out


# ------------------------------------------------------------------ set-up
def build_system():
    p, q, t, thi = exact_point()
    z, a, b, c = family_polys(p, q, t, thi)

    # A(z) numerator matrix, ascending powers of z, entries [[a,b],[c,-a]]
    ac = to_mp_coeffs(a, z, 2)
    bc = to_mp_coeffs(b, z, 2)
    cc = to_mp_coeffs(c, z, 2)
    Amat = [mp.matrix([[ac[k], bc[k]], [cc[k], -ac[k]]]) for k in range(3)]
    # PREREG 2.1: Y' = -A(z) Y with A = Amat/(z(z-1)), so N = -Amat, D = z^2 - z
    nmat = [-Ak for Ak in Amat]
    dpol = [mp.mpf(0), mp.mpf(-1), mp.mpf(1)]

    tn = mp.mpmathify(sp.N(t, DPS + 20))
    thin = mp.mpmathify(sp.N(thi, DPS + 20))
    return Amat, nmat, dpol, tn, thin, (p, q, t, thi)


def Aval(Amat, z):
    return Amat[0] + Amat[1] * z + Amat[2] * z * z


# ------------------------------------------------------- monodromy machinery
def base_frame(nmat, dpol, tn, order, nterms):
    """Fundamental matrix at z* = R, built from the formal solution at infinity.

    PREREG 2.1: e_1 carries e^{+tz/2}, so lam_first = t/2 - the labelling is NOT
    left to the sign of a discriminant.
    """
    T, Lam, L, F = formal_at_infinity(nmat, dpol, order, lam_first=tn / 2)
    logR = mp.log(R)                       # arg z* = 0, principal
    Y0 = formal_value(T, Lam, L, F, R, logR, nterms)
    return T, Lam, L, F, Y0, logR


def loops(cont, Y0, logR):
    """gamma_0, gamma_1, gamma_inf exactly as PREREG 2.3 specifies them."""
    r = R_LOOP
    res = {}

    # gamma_1: z* -> 1+r, ccw circle about 1, back
    Y, z, lg = cont.segment(Y0, R, 1 + r, logR)
    # circle about 1: parametrise by centre 1
    for i in range(1, 25):
        th = 2 * mp.pi * mp.mpf(i) / 24
        Y, z, lg = cont.segment(Y, z, 1 + r * mp.expj(th), lg)
    Y, z, lg = cont.segment(Y, z, R, lg)
    res["g1"] = Y

    # gamma_0: z* -> 1+r, over z=1 by the UPPER semicircle to 1-r, on to r,
    # ccw about 0, and back the same way
    Y, z, lg = cont.segment(Y0, R, 1 + r, logR)
    for i in range(1, 13):
        th = mp.pi * mp.mpf(i) / 12
        Y, z, lg = cont.segment(Y, z, 1 + r * mp.expj(th), lg)
    Y, z, lg = cont.segment(Y, z, r, lg)
    Y, z, lg = cont.arc(Y, z, 2 * mp.pi, lg)
    Y, z, lg = cont.segment(Y, z, 1 - r, lg)
    for i in range(1, 13):
        th = mp.pi - mp.pi * mp.mpf(i) / 12
        Y, z, lg = cont.segment(Y, z, 1 + r * mp.expj(th), lg)
    Y, z, lg = cont.segment(Y, z, R, lg)
    res["g0"] = Y

    # gamma_inf: full ccw circle |z| = R
    Y, z, lg = cont.arc(Y0, R, 2 * mp.pi, logR)
    res["ginf"] = Y
    return res


def run_once(h_factor, order, nterms):
    Amat, nmat, dpol, tn, thin, exact = build_system()
    T, Lam, L, F, Y0, logR = base_frame(nmat, dpol, tn, order, nterms)
    cont = Continuer(nmat, dpol, [mp.mpf(0), mp.mpf(1)], h_factor=h_factor)
    ends = loops(cont, Y0, logR)
    Y0i = Y0 ** -1
    return dict(Amat=Amat, nmat=nmat, dpol=dpol, t=tn, thi=thin, exact=exact,
                T=T, Lam=Lam, L=L, F=F, Y0=Y0, Y0i=Y0i, logR=logR,
                ends=ends, steps=cont.steps)


# --------------------------------------------------------- the 2.3 test
def candidate_conventions(ends, Y0, Y0i):
    """PREREG 2.3 enumerated 8 = loop order x orientation x action side.

    DEFECT IN THE PRE-REGISTRATION, found by the test firing (run 1, retained as
    outputs/stage2_systemC_run1.out.txt): that enumeration ties the orientation
    of gamma_inf to the orientation of the two small loops.  It cannot represent
    the relation that actually holds in pi_1(C - {0,1}) with the base point to
    the RIGHT of both punctures, namely  gamma_0 gamma_1 = gamma_inf(ccw), i.e.
    M_0 M_1 M_inf^{-1} = I - small loops ccw, big loop inverted.  With all three
    orientations tied, no candidate can satisfy condition 1, and indeed none
    did: the best ||M M M - I|| over the 8 was 6.85.

    The set is therefore WIDENED to 16 = side x orientation(small) x
    orientation(inf) x order.  This is a widening of the SEARCH, not a loosening
    of the TEST: the four conditions of PREREG 2.3 are unchanged, the threshold
    is unchanged at 1e-30, and uniqueness over the wider set is still required.
    Recorded as a pre-registration shortfall, not presented as the original plan.
    """
    out = {}
    for side in ("right", "left"):
        def M(key, side=side):
            Yc = ends[key]
            return Y0i * Yc if side == "right" else Yc * Y0i
        m0, m1, mi = M("g0"), M("g1"), M("ginf")
        for orient in ("ccw", "cw"):
            a0 = m0 if orient == "ccw" else m0 ** -1
            a1 = m1 if orient == "ccw" else m1 ** -1
            for oinf in ("ccw", "cw"):
                ai = mi if oinf == "ccw" else mi ** -1
                for order_ in ("01", "10"):
                    first, second = (a0, a1) if order_ == "01" else (a1, a0)
                    out[f"{side}|{orient}|inf{oinf}|{order_}"] = (
                        first, second, ai, a0, a1)
    return out


def cubic_F(x1, x2, x3, s1, s2, s3):
    return (x1 * x2 * x3 + x1 ** 2 + x2 ** 2
            - (s1 + s2 * s3) * x1 - (s2 + s1 * s3) * x2 - s3 * x3
            + s3 ** 2 + s1 * s2 * s3 + 1)


def grad_F(x1, x2, x3, s1, s2, s3):
    return (x2 * x3 + 2 * x1 - (s1 + s2 * s3),
            x1 * x3 + 2 * x2 - (s2 + s1 * s3),
            x1 * x2 - s3)


def evaluate_convention(name, pack, alpha_pred):
    first, second, ai, a0, a1 = pack
    rep = {"name": name}
    rep["c1"] = mnorm(first * second * ai - mp.eye(2))
    rep["tr0"] = abs(a0[0, 0] + a0[1, 1] - 2)
    rep["tr1"] = abs(a1[0, 0] + a1[1, 1] - 2)
    rep["nonI0"] = mnorm(a0 - mp.eye(2))
    rep["nonI1"] = mnorm(a1 - mp.eye(2))
    # condition 3: M_inf = [[al, al f2],[f1/al, (1+f1 f2)/al]]
    al = ai[0, 0]
    rep["alpha"] = al
    rep["alpha_err"] = min(abs(al - alpha_pred), abs(al - 1 / alpha_pred))
    # Report the branch by COMPUTING it, not by labelling it.  Run 3 printed the
    # branch through a "+"/"-" flag whose mapping was inverted, so a correct
    # alpha was described by the wrong closed form.  alpha_pred = e^{i pi
    # theta_inf} = e^{-i pi sqrt(3)/9}; if alpha matches 1/alpha_pred the branch
    # is e^{+i pi sqrt(3)/9}.
    # The alpha branch is COMPUTED, never labelled.  An earlier version carried
    # a flag; it was replaced by this report after a correct alpha was found
    # described by the wrong closed form.  The `sqrt(3)/9` half of the string
    # was still hard-coded from branch 1 (theta_inf = -2 - sqrt(3)/9) and so was
    # wrong on branch 2 (theta_inf = -2 + sqrt(3)/9), where e^{i pi theta_inf}
    # is e^{+i pi sqrt(3)/9}.  Both halves are now derived from alpha_pred.
    _pos = abs(al - alpha_pred) < abs(al - 1 / alpha_pred)
    _ap = mp.arg(alpha_pred)
    assert abs(abs(_ap) - mp.pi * mp.sqrt(3) / 9) < mp.mpf(10) ** -20, (
        f"alpha_pred does not sit at |arg| = pi sqrt(3)/9 (got {_ap}); the "
        f"closed-form label would be unfounded")
    _s = 1 if (_ap > 0) == _pos else -1
    rep["alpha_branch"] = ("e^{%si pi theta_inf}  = e^{%si pi sqrt(3)/9}"
                           % ("+" if _pos else "-", "+" if _s > 0 else "-"))
    if abs(al) > mp.mpf(10) ** -40:
        f2 = ai[0, 1] / al
        f1 = al * ai[1, 0]
        rep["shape"] = abs(ai[1, 1] - (1 + f1 * f2) / al)
        rep["f1"], rep["f2"] = f1, f2
    else:
        rep["shape"] = mp.inf
    # condition 4: the cubic, with x_i = d_i = (2,2) entries.
    # The labelling must follow the ORDER flag: vdPS's M_1 is `first` and their
    # M_2 is `second` in the relation M_1 M_2 M_inf = I.  Run 1 read x1 off M_0
    # and x2 off M_1 regardless of the flag, so the "10" candidates were scored
    # on an inconsistent pairing.  Fixed here.
    x1, x2 = first[1, 1], second[1, 1]
    s1, s2, s3 = mp.mpf(2), mp.mpf(2), al
    x3 = first[0, 1] * second[1, 0] + x1 * x2 - s2 * x1 - s1 * x2 + s1 * s2 + s3
    rep["x"] = (x1, x2, x3)
    rep["cubic"] = abs(cubic_F(x1, x2, x3, s1, s2, s3))
    rep["pass"] = (rep["c1"] < THRESH and rep["tr0"] < THRESH and rep["tr1"] < THRESH
                   and rep["nonI0"] > mp.mpf(10) ** -10
                   and rep["nonI1"] > mp.mpf(10) ** -10
                   and rep["alpha_err"] < THRESH and rep["shape"] < THRESH
                   and rep["cubic"] < THRESH)
    return rep


def digits(x):
    x = abs(x)
    return mp.inf if x == 0 else -mp.log10(x)


def unique_convention(ends, Y0, alpha_pred, verbose=False):
    """Run the PREREG 2.3 test and return the UNIQUE passing convention name.

    Stages 3 and 4 originally carried the branch-1 answer as a hard-coded
    string.  That is unsafe the moment a second branch is run: branch 2 has
    t of the opposite sign, so its Stokes geometry is mirrored and the winning
    convention need not be the same.  A hard-coded name would then either fail
    loudly (best case) or silently score the wrong pairing.  The convention is
    therefore re-derived wherever it is used, and uniqueness re-asserted.
    """
    cands = candidate_conventions(ends, Y0, Y0 ** -1)
    winners = []
    for name in sorted(cands):
        rep = evaluate_convention(name, cands[name], alpha_pred)
        if verbose:
            print(f"    {name:26s} {'PASS' if rep['pass'] else '.'}")
        if rep["pass"]:
            winners.append((name, rep))
    assert len(winners) == 1, (
        f"PREREG 2.3: {len(winners)} conventions pass all four conditions, "
        f"expected exactly 1 ({[w[0] for w in winners]})")
    return winners[0]


def main():
    order = 230
    nterms = None

    say("=" * 74)
    say("CT-S22 STAGE 2 - System C monodromy and Stokes data at t0")
    say(f"dps = {DPS}   z* = R = {R}   loop radius = {R_LOOP}   threshold 1e-30")
    say("=" * 74)

    st = run_once(4, order, 1)      # cheap pass to get t, then fix nterms
    tn = st["t"]
    nopt = int(mp.floor(abs(tn * R)))
    say(f"\n|t| = {mp.nstr(abs(tn), 20)}   |t z*| = {mp.nstr(abs(tn*R), 20)}")
    say(f"optimal truncation N = {nopt}   -> e^-N = {mp.nstr(mp.e**(-nopt), 6)}")
    assert order > nopt, "formal order below optimal truncation"
    nterms = nopt

    # ---- C-A: the family's own constraints at the numeric point ------------
    say("\n--- C-A  the printed family's constraints at the point --------------")
    Amat = st["Amat"]
    A0 = -Aval(Amat, mp.mpf(0))        # A_0 = -A(0)
    A1 = Aval(Amat, mp.mpf(1))         # A_1 =  A(1)
    for nm, M, tgt in (("det A_0 + th0^2/4", A0, mp.mpf(0)),
                       ("det A_1 + th1^2/4", A1, mp.mpf(0))):
        v = abs(mp.det(M) - tgt)
        say(f"  {nm:26s} = {mp.nstr(v, 6):>14s}   ({mp.nstr(digits(v),5)} digits)")
        assert v < THRESH, f"C-A failed: {nm}"
    Ainf = Amat[2]
    v = mnorm(Ainf - mp.matrix([[-tn / 2, 0], [0, tn / 2]]))
    say(f"  A_inf = (t/2)diag(-1,1)    = {mp.nstr(v,6):>14s}   "
        f"({mp.nstr(digits(v),5)} digits)")
    assert v < THRESH, "C-A failed: A_inf"
    tr_sum = (A0 + A1)[0, 0]
    say(f"  (A_0+A_1)_11             = {mp.nstr(tr_sum, 20)}")
    say(f"  -theta_inf/2             = {mp.nstr(-st['thi']/2, 20)}")
    say(f"  theta_inf                = {mp.nstr(st['thi'], 20)}")
    say("  [CT-S16's finding: the printed family gives -theta_inf/2, not "
        "theta_inf.]")

    # ---- recompute with the right truncation -------------------------------
    st = run_once(4, order, nterms)
    L = st["L"]
    say(f"\n--- formal data at infinity ----------------------------------------")
    say(f"  Lam = diag({mp.nstr(st['Lam'][0,0],20)}, {mp.nstr(st['Lam'][1,1],20)})")
    say(f"  L   = diag({mp.nstr(L[0,0],20)}, {mp.nstr(L[1,1],20)})")
    alpha_pred = mp.e ** (2j * mp.pi * (st["thi"] / 2))
    say(f"  C-5 predicted alpha = e^{{i pi theta_inf}} = "
        f"{mp.nstr(alpha_pred, 20)}   |alpha| = {mp.nstr(abs(alpha_pred),6)}")
    v = abs(L[0, 0] - st["thi"] / 2)
    say(f"  L_11 - theta_inf/2 = {mp.nstr(v,6)}   ({mp.nstr(digits(v),5)} digits)")

    # ---- C-0 ---------------------------------------------------------------
    # NOT a bare magnitude bound.  An optimally truncated Gevrey-1 series has
    # residual ~ C(N) e^{-|t z|} with an algebraic prefactor, so "residual <
    # k e^{-N}" only tests the constant k, which is exactly the kind of
    # threshold that gets tuned until it passes.  Instead:
    #   C-0a the residual sits at the MINIMAL TERM of the series (the honest
    #        measure of optimal-truncation error), within an algebraic factor;
    #   C-0b the residual DECAYS AT THE PREDICTED RATE e^{-|t| R} as R varies -
    #        a two-point test whose target is fixed by t alone and which fails
    #        if the formal solution is of the wrong Gevrey class or wrong Lam.
    say(f"\n--- C-0  formal series residual, by rate not by magnitude ----------")
    res = formal_residual(st["nmat"], st["dpol"], st["T"], st["Lam"], st["L"],
                          st["F"], R, nterms)
    minterm = min(mnorm(st["F"][k]) * R ** (-k) for k in range(1, nterms + 1))
    say(f"  residual at R={R}          {mp.nstr(res,6)}")
    say(f"  minimal term of the series {mp.nstr(minterm,6)}")
    say(f"  e^-|t z*|                  {mp.nstr(mp.e**(-nopt),6)}")
    ratio = res / minterm
    say(f"  C-0a residual / min term = {mp.nstr(ratio,6)}  (want < N^3 = "
        f"{nopt**3})")
    assert ratio < nopt ** 3, "C-0a failed: residual far above the minimal term"

    R2 = mp.mpf(140)
    n2 = int(mp.floor(abs(tn * R2)))
    T2, Lam2, L2, F2 = formal_at_infinity(st["nmat"], st["dpol"], order,
                                          lam_first=tn / 2)
    res2 = formal_residual(st["nmat"], st["dpol"], T2, Lam2, L2, F2, R2, n2)
    pred = mp.e ** (-abs(tn) * (R - R2))
    obs = res / res2
    say(f"  residual at R={R2}          {mp.nstr(res2,6)}")
    say(f"  C-0b observed ratio  {mp.nstr(obs,8)}")
    say(f"       predicted e^-|t|(R-R2) = {mp.nstr(pred,8)}")
    rr = obs / pred
    say(f"       observed/predicted = {mp.nstr(rr,8)}  (want within 10^+-2)")
    assert mp.mpf(10) ** -2 < rr < mp.mpf(10) ** 2, \
        "C-0b failed: the residual does not decay at the predicted Gevrey rate"
    say("  [PASS] residual is at the minimal term and decays at rate e^-|t|R")

    # ---- the PREREG 2.3 overdetermined convention test ---------------------
    say(f"\n--- PREREG 2.3  overdetermined convention test ----------------------")
    cands = candidate_conventions(st["ends"], st["Y0"], st["Y0i"])
    reps = []
    say(f"  {'convention':22s} {'MMM-I':>9s} {'tr0-2':>9s} {'tr1-2':>9s} "
        f"{'alpha':>9s} {'shape':>9s} {'cubic':>9s}  verdict")
    for name in sorted(cands):
        rep = evaluate_convention(name, cands[name], alpha_pred)
        reps.append(rep)
        say(f"  {name:22s} {mp.nstr(rep['c1'],3):>9s} "
            f"{mp.nstr(rep['tr0'],3):>9s} {mp.nstr(rep['tr1'],3):>9s} "
            f"{mp.nstr(rep['alpha_err'],3):>9s} {mp.nstr(rep['shape'],3):>9s} "
            f"{mp.nstr(rep['cubic'],3):>9s}  "
            f"{'PASS' if rep['pass'] else '.'}")
    winners = [r for r in reps if r["pass"]]
    say(f"\n  conventions passing all four conditions: {len(winners)}")
    if len(winners) != 1:
        say("  *** HALT (PREREG 2.3): the convention is not uniquely determined.")
        say("      Reporting rather than choosing.")
        return reps, None, st, nterms
    w = winners[0]
    say(f"  UNIQUE: {w['name']}")
    say(f"  alpha branch (computed, not labelled): {w['alpha_branch']}")
    say(f"    alpha = {mp.nstr(w['alpha'], 30)}")
    say(f"    matched to {mp.nstr(w['alpha_err'],6)}; C-5 predicted |alpha| = 1 and")
    say(f"    |arg alpha| = pi sqrt(3)/9 = {mp.nstr(mp.pi*mp.sqrt(3)/9, 20)}, both hit.")
    say(f"    |arg alpha| observed = {mp.nstr(abs(mp.arg(w['alpha'])), 20)}")
    say("    The SIGN of the exponent is a convention (it is fixed by the same")
    say("    clockwise M_inf that Stage 1's A7 correction identified); the")
    say("    modulus and |arg| are the content of the C-5 prediction.")
    return reps, w, st, nterms


def report(w, st, nterms):
    x1, x2, x3 = w["x"]
    al = w["alpha"]
    say(f"\n--- the comparison quantities --------------------------------------")
    for nm, v in (("x1 = d1", x1), ("x2 = d2", x2), ("x3 = d3", x3),
                  ("alpha = s3", al)):
        say(f"  {nm:10s} = {mp.nstr(v, 35)}")
    say(f"  f1         = {mp.nstr(w['f1'], 35)}")
    say(f"  f2         = {mp.nstr(w['f2'], 35)}")

    say(f"\n--- C-6  the cubic, and the pre-registered gradient ----------------")
    s1, s2, s3 = mp.mpf(2), mp.mpf(2), al
    say(f"  |F| = {mp.nstr(w['cubic'],6)}   ({mp.nstr(digits(w['cubic']),5)} digits)")
    g = grad_F(x1, x2, x3, s1, s2, s3)
    for i, gi in enumerate(g, 1):
        say(f"  dF/dx{i} = {mp.nstr(gi, 25)}   |.| = {mp.nstr(abs(gi), 8)}")
    gmax = max(abs(gi) for gi in g)
    say(f"  max |grad F| = {mp.nstr(gmax, 10)}")
    if gmax < mp.mpf(10) ** -20:
        say("  *** the point IS a singular point of the cubic surface: the")
        say("      coordinates lose first-order sensitivity.  Stage 3 decides.")
    else:
        say("  the point is a SMOOTH point of the (singular) cubic surface;")
        say("  the surface is singular because s1 = s2 = 2, but not HERE.")
    return gmax


def step_halving(st4, order, nterms, w_name):
    say(f"\n--- C-7  error bar by step halving (h = rho/4 vs rho/8) ------------")
    st8 = run_once(8, order, nterms)
    c4 = candidate_conventions(st4["ends"], st4["Y0"], st4["Y0i"])[w_name]
    c8 = candidate_conventions(st8["ends"], st8["Y0"], st8["Y0i"])[w_name]
    say(f"  steps: h=rho/4 -> {st4['steps']},  h=rho/8 -> {st8['steps']}")
    assert st8["steps"] > st4["steps"], "step halving did not halve the step"
    worst = mp.mpf(0)
    for i, nm in ((3, "M_0"), (4, "M_1"), (2, "M_inf")):
        d = mnorm(c4[i] - c8[i])
        worst = max(worst, d)
        say(f"  |{nm} difference| = {mp.nstr(d,6)}   ({mp.nstr(digits(d),5)} digits)")
    say(f"  ERROR BAR (from halving, not from a single run) = {mp.nstr(worst,6)}")
    assert worst < THRESH, "C-7 failed: the two step sizes disagree above 1e-30"
    say("  [PASS]")
    return worst


if __name__ == "__main__":
    reps, w, st, nterms = main()
    if w is not None:
        report(w, st, nterms)
        step_halving(st, 230, nterms, w["name"])
        say("\n" + "=" * 74)
        say("STAGE 2 COMPLETE")
        say("=" * 74)
    outp = Path(__file__).resolve().parent.parent / "outputs" / f"stage2_systemC{TAG}.out.txt"
    text = "\n".join(OUT) + "\n"
    outp.write_text(text, encoding="utf-8")
    back = outp.read_text(encoding="utf-8")          # read back what was written
    assert back == text, "read-back of the output file differs from what was written"
    print(f"\nwritten {outp}  sha256 {hashlib.sha256(back.encode()).hexdigest()}")
