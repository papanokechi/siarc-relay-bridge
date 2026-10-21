"""CT-S22 STAGE 1 - known-answer control on Kummer's equation.

PREREG section 4.3.  The solver is validated against closed forms and against an
INDEPENDENT implementation (mpmath's hyperu / hyp1f1) BEFORE System C is touched.
Falsifier: agreement below 35 significant digits at either parameter value.
On failure the session does not proceed to Stage 2.

Kummer:  z w'' + (b - z) w' - a w = 0
companion system for Y = (w, w')^T:

    Y' = [[0, 1], [a/z, 1 - b/z]] Y = N(z)/D(z) Y,
    N(z) = [[0, z], [a, z - b]],  D(z) = z.

Local structure: z = 0 regular singular with exponents 0 and 1 - b; z = infinity
irregular of Katz rank 1 with Lam = diag(0, 1) and L = diag(-a, a - b).
Exponential difference q(z) = -z, so the SINGULAR directions are arg z = 0, pi
and the anti-Stokes (regular) directions are arg z = +-pi/2.  The base point is
therefore taken on arg z = +pi/2, not on the real axis.

AMENDMENT TO PREREG 4.3, recorded BEFORE any result was seen
------------------------------------------------------------
PREREG promised the individual Stokes multipliers from a connection formula
"verified in-session against mpmath.hyperu".  mpmath's hyperu evaluates a single
branch, so it cannot by itself be continued across the singular ray arg z = 0,
and that particular cross-check is not implementable with it.  Substituted, and
strictly stronger on the machinery actually under test:

  A3  my optimally truncated sectorial solution's RECESSIVE column is compared
      directly with mpmath's (U(a,b,z), U'(a,b,z)) - the unique solution with
      that asymptotic in |arg z| < 3pi/2 - at several points on BOTH rays
      arg z = +pi/2 and arg z = -pi/2, the continuation between them crossing
      the singular ray arg z = 0.  This tests the formal series, the optimal
      truncation, the continuation and the continuous log at once, against code
      that shares nothing with this session.

The joint closed form for the Stokes multipliers, f1*f2 (A7), is retained and is
exact.  The Gamma-quotient closed forms for f1 and f2 separately are computed and
REPORTED, explicitly labelled as recalled-then-tested, and gate nothing.
"""
import hashlib
import pathlib
import sys

import mpmath as mp

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import solver as S  # noqa: E402

DPS = 150
R = mp.mpf(110)          # |q(z*)| = 110  =>  optimal-truncation error ~ e^-110 = 1.7e-48
DIGITS_REQUIRED = 35     # PREREG 4.3 falsifier
mp.mp.dps = DPS

PARAMS = [
    (mp.mpf(1) / 3, mp.mpf(5) / 7),
    (mp.mpf(2) / 5 + mp.mpc(0, 1) * mp.mpf(3) / 10,
     mp.mpf(11) / 10 - mp.mpc(0, 1) * mp.mpf(1) / 5),
]

failures = []


def digits(err, scale=1):
    err = abs(err)
    scale = abs(scale) if abs(scale) > 0 else mp.mpf(1)
    if err == 0:
        return mp.inf
    return -mp.log10(err / scale)


def check(name, err, scale=1, need=DIGITS_REQUIRED):
    d = digits(err, scale)
    ok = d >= need
    print(f"    [{'PASS' if ok else 'FAIL'}] {name}: {mp.nstr(d, 5)} digits "
          f"(need {need}), residual {mp.nstr(abs(err), 5)}")
    if not ok:
        failures.append(f"{name}: only {mp.nstr(d, 5)} digits")
    return ok


def kummer_system(a, b):
    N0 = mp.matrix([[0, 0], [a, -b]])
    N1 = mp.matrix([[0, 1], [0, 1]])
    return [N0, N1], [mp.mpf(0), mp.mpf(1)]


def run(a, b, h_factor=4):
    nmat, dpol = kummer_system(a, b)
    nterms = int(R)                       # optimal truncation N ~ |q(z)|
    T, Lam, L, F = S.formal_at_infinity(nmat, dpol, nterms + 4, lam_first=mp.mpf(0))

    res = {}
    # ---- A2  L = diag(-a, a-b), closed form -------------------------------
    res["L_err"] = max(abs(L[0, 0] - (-a)), abs(L[1, 1] - (a - b)))
    res["Lam"] = (Lam[0, 0], Lam[1, 1])

    # ---- A1 / C-0  formal residual ----------------------------------------
    zc = R * mp.mpc(0, 1)
    res["C0"] = S.formal_residual(nmat, dpol, T, Lam, L, F, zc, nterms)

    # ---- build the sectorial solution on the ray arg z = +pi/2 ------------
    zstar = R * mp.mpc(0, 1)
    logzstar = mp.log(R) + mp.mpc(0, 1) * mp.pi / 2
    Y0 = S.formal_value(T, Lam, L, F, zstar, logzstar, nterms)
    res["Y0"] = Y0

    # ---- A3  oracle: recessive column vs mpmath's U ------------------------
    # verify the derivative identity U'(a,b,z) = -a U(a+1,b+1,z) numerically
    with mp.workdps(50):
        ztest = mp.mpc(3, 2)
        num = mp.diff(lambda zz: mp.hyperu(a, b, zz), ztest)
        idt = -a * mp.hyperu(a + 1, b + 1, ztest)
        res["Uprime_identity"] = abs(num - idt) / abs(idt)

    def Uvec(z):
        return mp.matrix([mp.hyperu(a, b, z), -a * mp.hyperu(a + 1, b + 1, z)])

    ratios = []
    for frac in (mp.mpf(1), mp.mpf("0.93"), mp.mpf("0.87")):
        z = R * frac * mp.mpc(0, 1)
        logz = mp.log(R * frac) + mp.mpc(0, 1) * mp.pi / 2
        Yv = S.formal_value(T, Lam, L, F, z, logz, int(R * frac))
        u = Uvec(z)
        ratios.append((Yv[0, 0] / u[0], Yv[1, 0] / u[1]))
    # all six ratios must be the same constant
    r0 = ratios[0][0]
    res["A3_upper"] = max(abs(r - r0) for pair in ratios for r in pair) / abs(r0)

    # continue the sectorial solution from +pi/2 to -pi/2 ACROSS the singular
    # ray arg z = 0, and compare the recessive column with the same U there
    cont = S.Continuer(nmat, dpol, sings=[mp.mpf(0)], h_factor=h_factor)
    Ym, zm, logzm = cont.arc(mp.matrix(Y0), zstar, -mp.pi, logzstar)
    assert abs(zm - (-R * mp.mpc(0, 1))) < mp.mpf(10) ** (-DPS + 30), "arc endpoint"
    u = Uvec(zm)
    rl = [Ym[0, 0] / u[0], Ym[1, 0] / u[1]]
    res["A3_lower"] = max(abs(r - r0) for r in rl) / abs(r0)

    # ---- A4  monodromy about z = 0 via the small-circle lasso -------------
    r_small = mp.mpf(1) / 4
    Y, z, logz = cont.segment(mp.matrix(Y0), zstar, r_small * mp.mpc(0, 1), logzstar)
    Y, z, logz = cont.arc(Y, z, 2 * mp.pi, logz)
    Y, z, logz = cont.segment(Y, z, zstar, logz)
    M0 = Y0 ** -1 * Y
    res["M0"] = M0
    res["trM0_err"] = abs((M0[0, 0] + M0[1, 1]) - (1 + mp.e ** (-2 * mp.pi * mp.mpc(0, 1) * b)))
    res["detM0_err"] = abs(mp.det(M0) - mp.e ** (-2 * mp.pi * mp.mpc(0, 1) * b))

    # ---- A5  M_infty via the big circle; M0 M_inf = I ---------------------
    Y, z, logz = cont.arc(mp.matrix(Y0), zstar, 2 * mp.pi, logzstar)
    Minf = Y0 ** -1 * Y
    res["Minf"] = Minf
    res["MM_err"] = S.mnorm(M0 * Minf - mp.eye(2))

    # ---- A6  shape of M_infty and alpha in closed form --------------------
    alpha = Minf[0, 0]
    f2 = Minf[0, 1] / alpha
    f1 = alpha * Minf[1, 0]
    res["alpha"], res["f1"], res["f2"] = alpha, f1, f2
    res["shape_err"] = abs(Minf[1, 1] - (1 + f1 * f2) / alpha)
    res["alpha_err"] = abs(alpha - mp.e ** (-2 * mp.pi * mp.mpc(0, 1) * a))

    # ---- A7  f1*f2 in closed form -----------------------------------------
    al = mp.e ** (-2 * mp.pi * mp.mpc(0, 1) * a)
    target = al * (1 + mp.e ** (2 * mp.pi * mp.mpc(0, 1) * b)) - al ** 2 - 1
    res["f1f2_err"] = abs(f1 * f2 - target)
    res["f1f2_target"] = target

    # ---- A8  report-only: Gamma-quotient candidates -----------------------
    i = mp.mpc(0, 1)
    cand = {
        "2pi i / (Gamma(a) Gamma(a-b+1))": 2 * mp.pi * i / (mp.gamma(a) * mp.gamma(a - b + 1)),
        "2pi i / (Gamma(b-a) Gamma(1-a))": 2 * mp.pi * i / (mp.gamma(b - a) * mp.gamma(1 - a)),
    }
    res["cand"] = cand
    return res


print("=" * 78)
print("CT-S22 STAGE 1 - Kummer known-answer control")
print(f"dps = {DPS}   R = {mp.nstr(R, 10)}   optimal truncation N = {int(R)}")
print(f"optimal-truncation error ~ e^-{int(R)} = {mp.nstr(mp.e ** (-R), 5)}")
print(f"falsifier: below {DIGITS_REQUIRED} significant digits")
print("=" * 78)

for idx, (a, b) in enumerate(PARAMS, 1):
    print(f"\n--- parameter value {idx}:  a = {mp.nstr(a, 20)}   b = {mp.nstr(b, 20)}")
    assert abs(b - mp.nint(mp.re(b))) > mp.mpf("1e-6") or abs(mp.im(b)) > mp.mpf("1e-6"), \
        "b must not be an integer"
    r4 = run(a, b, h_factor=4)
    r8 = run(a, b, h_factor=8)

    print(f"  Lam = diag({mp.nstr(r4['Lam'][0], 5)}, {mp.nstr(r4['Lam'][1], 5)})"
          f"   (expected diag(0,1))")
    check("A2  L = diag(-a, a-b)", r4["L_err"], need=DPS - 20)
    check("A1  C-0 formal series residual is below the truncation error",
          r4["C0"], scale=mp.e ** (-R), need=0)
    print(f"        (C-0 residual {mp.nstr(r4['C0'], 5)} vs truncation error "
          f"{mp.nstr(mp.e ** (-R), 5)})")
    check("A3a U'(a,b,z) = -a U(a+1,b+1,z) [mpmath identity]",
          r4["Uprime_identity"], need=30)
    check("A3b recessive column vs mpmath U on ray +pi/2", r4["A3_upper"])
    check("A3c recessive column vs mpmath U on ray -pi/2 (crossing arg z = 0)",
          r4["A3_lower"])
    check("A4a tr M0 = 1 + e^{-2 pi i b}", r4["trM0_err"])
    check("A4b det M0 = e^{-2 pi i b}", r4["detM0_err"])
    check("A5  M0 M_inf = I", r4["MM_err"])
    check("A6a M_inf has the vdPS triangular x diagonal shape", r4["shape_err"])
    check("A6b alpha = e^{-2 pi i a}", r4["alpha_err"])
    check("A7  f1 f2 = alpha(1+e^{2 pi i b}) - alpha^2 - 1", r4["f1f2_err"])
    check("C-7 step halving (h_factor 4 vs 8) agreement",
          S.mnorm(r4["M0"] - r8["M0"]))

    print(f"    f1 = {mp.nstr(r4['f1'], 30)}")
    print(f"    f2 = {mp.nstr(r4['f2'], 30)}")
    print("    A8 (REPORT ONLY - recalled candidates, gate nothing):")
    for k, v in r4["cand"].items():
        print(f"       {k} = {mp.nstr(v, 20)}")
        for nm, got in (("f1", r4["f1"]), ("f2", r4["f2"])):
            for sgn, lab in ((1, "+"), (-1, "-")):
                if abs(got - sgn * v) / max(abs(got), mp.mpf(1)) < mp.mpf(10) ** -30:
                    print(f"          -> matches {lab}{nm} to >=30 digits")

print("\n" + "=" * 78)
if failures:
    print("STAGE 1 FALSIFIER FIRED - the session does NOT proceed to Stage 2")
    for f in failures:
        print("   ", f)
    sys.exit(1)
print("STAGE 1 PASSED - all closed-form targets met at >= "
      f"{DIGITS_REQUIRED} digits, at both parameter values")
print("=" * 78)
