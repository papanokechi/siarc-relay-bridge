"""CT-S22 STAGE 1 - known-answer control on Kummer's equation.  SECOND RUN.

The first run (outputs/stage1_kummer.out.txt, retained) fired the falsifier and
found three things.  All three are recorded here rather than quietly fixed.

DEFECT 1 - the system was not trace-free.
  vdPS work throughout in SL_2: all A_i have trace 0, so det Y is constant and
  every monodromy is unimodular.  Kummer's companion system has
  tr B = 1 - b/z != 0, so det M0 = e^{-2 pi i b} != 1 and the vdPS factorisation
  cannot apply to it at all.  Fixed at the SETUP, not at the check, by passing to
  the trace-free gauge  Btilde = B - (1/2) tr(B) I,  i.e.
  Ntilde = N - (1/2) tr(N) I with the same D.  The solutions are related by the
  scalar  phi(z) = exp(z/2) z^{-b/2},  Ytilde = phi^-1 Y, which is why the oracle
  vector below carries that factor.

DEFECT 2 - M_infinity is the CLOCKWISE big circle.
  On the sphere gamma_0 gamma_1 gamma_inf = 1 with each loop positively oriented
  about its OWN point, and the positively oriented loop about infinity is
  clockwise in the z-plane.  The first run compared M0 with the counterclockwise
  circle, which is homotopic to gamma_0 itself, so M0 * M_inf = M0^2.

DEFECT 3 - check A6a was VACUOUS, and this is the important one.
  "M_inf has the shape diag(a,1/a)*[[1,0],[f1,1]]*[[1,f2],[0,1]]" was extracted as
  alpha = M11, f2 = M12/alpha, f1 = alpha*M21 and then verified against
  M22 = (1+f1 f2)/alpha.  For ANY unimodular M with M11 != 0 that identity is an
  algebraic tautology: det M = 1 gives M12 M21 = alpha M22 - 1, hence
  (1 + f1 f2)/alpha = (1 + alpha M22 - 1)/alpha = M22.  The check could not fail.
  It is the CT-S16 S16-11 family again - a step that cannot fail reporting a pass
  - and it was caught only because the surrounding checks failed loudly enough to
  force the algebra to be looked at.
  Replaced by a check with content: the two Stokes matrices are computed
  SEPARATELY, by comparing the sectorial solutions across each singular ray, and
  each is required to be unipotent and triangular in the correct triangle (four
  conditions apiece, none automatic), after which the factorisation
      M_inf,ccw = e^{2 pi i L} S_{2pi} S_{pi}
  is verified as an identity between independently computed matrices.

Falsifier unchanged: below 35 significant digits at either parameter value.
"""
import pathlib
import sys

import mpmath as mp

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import solver as S  # noqa: E402

DPS = 150
R = mp.mpf(110)
DIGITS_REQUIRED = 35
mp.mp.dps = DPS
I = mp.mpc(0, 1)

PARAMS = [
    (mp.mpf(1) / 3, mp.mpf(5) / 7),
    (mp.mpf(2) / 5 + I * mp.mpf(3) / 10, mp.mpf(11) / 10 - I * mp.mpf(1) / 5),
]

failures = []


def digits(err, scale=1):
    err, scale = abs(err), abs(scale) if abs(scale) > 0 else mp.mpf(1)
    return mp.inf if err == 0 else -mp.log10(err / scale)


def check(name, err, scale=1, need=DIGITS_REQUIRED):
    d = digits(err, scale)
    ok = d >= need
    print(f"    [{'PASS' if ok else 'FAIL'}] {name}: {mp.nstr(d, 5)} digits "
          f"(need {need}), residual {mp.nstr(abs(err), 5)}")
    if not ok:
        failures.append(f"{name}: only {mp.nstr(d, 5)} digits")
    return ok


def kummer_tracefree(a, b):
    """Ntilde = N - (1/2) tr(N) I  with  N = [[0,z],[a,z-b]],  D = z."""
    N0 = mp.matrix([[b / 2, 0], [a, -b / 2]])
    N1 = mp.matrix([[-mp.mpf(1) / 2, 1], [0, mp.mpf(1) / 2]])
    for M in (N0, N1):
        assert abs(M[0, 0] + M[1, 1]) < mp.mpf(10) ** (-DPS + 10), "not trace-free"
    return [N0, N1], [mp.mpf(0), mp.mpf(1)]


def run(a, b, h_factor=4):
    nmat, dpol = kummer_tracefree(a, b)
    nterms = int(R)
    # e_1 is the algebraic (z^{-a}) solution: eigenvalue 0 ungauged, -1/2 gauged
    T, Lam, L, F = S.formal_at_infinity(nmat, dpol, nterms + 4,
                                        lam_first=-mp.mpf(1) / 2)
    r = {"Lam": (Lam[0, 0], Lam[1, 1]), "L": (L[0, 0], L[1, 1])}
    r["L_err"] = max(abs(L[0, 0] - (b / 2 - a)), abs(L[1, 1] - (a - b / 2)))

    zc = R * I
    r["C0"] = S.formal_residual(nmat, dpol, T, Lam, L, F, zc, nterms)

    zA, lgA = R * I, mp.log(R) + I * mp.pi / 2              # ray arg z = +pi/2
    YA = S.formal_value(T, Lam, L, F, zA, lgA, nterms)
    zB, lgB = -R * I, mp.log(R) + I * 3 * mp.pi / 2         # ray arg z = 3pi/2
    YB = S.formal_value(T, Lam, L, F, zB, lgB, nterms)

    cont = S.Continuer(nmat, dpol, sings=[mp.mpf(0)], h_factor=h_factor)

    # ---- A3  oracle: recessive column vs mpmath's U, gauge-corrected -------
    with mp.workdps(50):
        zt = mp.mpc(3, 2)
        r["Uprime_identity"] = abs(mp.diff(lambda zz: mp.hyperu(a, b, zz), zt)
                                   - (-a * mp.hyperu(a + 1, b + 1, zt))) \
            / abs(a * mp.hyperu(a + 1, b + 1, zt))

    def Utilde(z, logz):
        """phi^-1 (U, U') with phi = exp(z/2) z^{-b/2}, log z supplied."""
        ph = mp.e ** (-z / 2) * mp.e ** (b / 2 * logz)
        return mp.matrix([ph * mp.hyperu(a, b, z),
                          ph * (-a) * mp.hyperu(a + 1, b + 1, z)])

    ratios = []
    for frac in (mp.mpf(1), mp.mpf("0.93"), mp.mpf("0.87")):
        z, lg = R * frac * I, mp.log(R * frac) + I * mp.pi / 2
        Yv = S.formal_value(T, Lam, L, F, z, lg, int(R * frac))
        u = Utilde(z, lg)
        ratios.append((Yv[0, 0] / u[0], Yv[1, 0] / u[1]))
    r0 = ratios[0][0]
    r["A3_upper"] = max(abs(x - r0) for pr in ratios for x in pr) / abs(r0)

    # continue across the singular ray arg z = 0, down to arg z = -pi/2
    Ym, zm, lgm = cont.arc(mp.matrix(YA), zA, -mp.pi, lgA)
    u = Utilde(zm, lgm)
    r["A3_lower"] = max(abs(Ym[0, 0] / u[0] - r0), abs(Ym[1, 0] / u[1] - r0)) / abs(r0)

    # ---- A4  monodromy about z = 0, lasso down to a small circle ----------
    Y, z, lg = cont.segment(mp.matrix(YA), zA, mp.mpf(1) / 4 * I, lgA)
    Y, z, lg = cont.arc(Y, z, 2 * mp.pi, lg)
    Y, z, lg = cont.segment(Y, z, zA, lg)
    M0 = YA ** -1 * Y
    r["M0"] = M0
    r["trM0_err"] = abs((M0[0, 0] + M0[1, 1]) - 2 * mp.cos(mp.pi * b))
    r["detM0_err"] = abs(mp.det(M0) - 1)

    # ---- A5  M_inf = CLOCKWISE big circle;  M0 * M_inf = I ----------------
    Y, z, lg = cont.arc(mp.matrix(YA), zA, -2 * mp.pi, lgA)
    Minf = YA ** -1 * Y
    r["Minf"] = Minf
    r["MM_err"] = S.mnorm(M0 * Minf - mp.eye(2))

    # ---- A6  the two Stokes matrices, computed SEPARATELY -----------------
    # S_pi : cross the singular ray arg z = pi, going ccw from +pi/2 to 3pi/2
    Yc, zc2, lgc = cont.arc(mp.matrix(YA), zA, mp.pi, lgA)
    Spi = YB ** -1 * Yc
    # S_2pi : cross the singular ray arg z = 2pi, ccw from 3pi/2 to 5pi/2
    Yd, zd, lgd = cont.arc(mp.matrix(YB), zB, mp.pi, lgB)
    e2piL = mp.matrix([[mp.e ** (2 * mp.pi * I * L[0, 0]), 0],
                       [0, mp.e ** (2 * mp.pi * I * L[1, 1])]])
    S2pi = (YA * e2piL) ** -1 * Yd
    r["Spi"], r["S2pi"] = Spi, S2pi
    # unipotent + triangular, in OPPOSITE triangles: four conditions each,
    # none of them automatic
    r["Spi_unip"] = max(abs(Spi[0, 0] - 1), abs(Spi[1, 1] - 1))
    r["S2pi_unip"] = max(abs(S2pi[0, 0] - 1), abs(S2pi[1, 1] - 1))
    r["Spi_tri"] = min(abs(Spi[0, 1]), abs(Spi[1, 0]))
    r["S2pi_tri"] = min(abs(S2pi[0, 1]), abs(S2pi[1, 0]))
    r["Spi_which"] = "lower" if abs(Spi[0, 1]) < abs(Spi[1, 0]) else "upper"
    r["S2pi_which"] = "lower" if abs(S2pi[0, 1]) < abs(S2pi[1, 0]) else "upper"
    r["opposite"] = r["Spi_which"] != r["S2pi_which"]
    # factorisation of the ccw monodromy at infinity
    r["fact_err"] = S.mnorm(e2piL * S2pi * Spi - Minf ** -1)

    alpha = mp.e ** (2 * mp.pi * I * L[0, 0])
    r["alpha"] = alpha
    r["alpha_err"] = abs(alpha - mp.e ** (I * mp.pi * b - 2 * mp.pi * I * a))

    # ---- A7  f1 f2 in closed form ----------------------------------------
    # CORRECTED AFTER RUN 2, and the correction is forced, not fitted.
    # vdPS write M_inf = diag(a,1/a) * LOWER * UPPER.  The factorisation this
    # script computes is  M_inf,ccw = e^{2 pi i L} * S_2pi(UPPER) * S_pi(LOWER),
    # i.e. diag * UPPER * LOWER - the other order.  Multiplying it out,
    #     diag(al,1/al)[[1,g2],[0,1]][[1,0],[g1,1]]
    #        = [[al(1+g1 g2), al g2], [g1/al, 1/al]],
    # so the trace is al(1+g1 g2) + 1/al, not al + (1+f1 f2)/al.  Run 2 used the
    # vdPS ordering against the computed one and failed by O(1).  The TARGET
    # trace 2 cos(pi b) is unchanged and was already verified at 99 digits by
    # A4a+A5+A6e; A7 is therefore a DEPENDENT restatement of those and is not
    # independent evidence.  It is kept because an ordering error of exactly this
    # kind is what it detects.
    #
    # Consequence carried to Stage 2: vdPS's alpha is e^{-2 pi i L11}, not
    # e^{+2 pi i L11}, because their M_inf is the CLOCKWISE loop.  Conjugating
    # M_inf,ccw^-1 = S_pi^-1 S_2pi^-1 e^{-2 pi i L} by the diagonal puts it in
    # exactly their diag * lower * upper shape with their alpha = 1/alpha here.
    f1 = Spi[1, 0] + Spi[0, 1]      # the single off-diagonal entry, whichever it is
    f2 = S2pi[1, 0] + S2pi[0, 1]
    r["f1"], r["f2"] = f1, f2
    tr_target = 2 * mp.cos(mp.pi * b)
    r["f1f2_err"] = abs(f1 * f2 - ((tr_target - 1 / alpha) / alpha - 1))
    r["alpha_vdps"] = 1 / alpha
    return r


print("=" * 78)
print("CT-S22 STAGE 1 (2nd run) - Kummer known-answer control, trace-free gauge")
print(f"dps = {DPS}   R = {mp.nstr(R, 10)}   truncation N = {int(R)}   "
      f"error ~ e^-{int(R)} = {mp.nstr(mp.e ** (-R), 5)}")
print(f"falsifier: below {DIGITS_REQUIRED} significant digits")
print("=" * 78)

for idx, (a, b) in enumerate(PARAMS, 1):
    print(f"\n--- parameter value {idx}:  a = {mp.nstr(a, 20)}   b = {mp.nstr(b, 20)}")
    r4, r8 = run(a, b, 4), run(a, b, 8)
    print(f"  Lam = diag({mp.nstr(r4['Lam'][0], 5)}, {mp.nstr(r4['Lam'][1], 5)})"
          f"   L = diag({mp.nstr(r4['L'][0], 12)}, {mp.nstr(r4['L'][1], 12)})"
          f"   expected diag(b/2-a, a-b/2) = "
          f"diag({mp.nstr(b / 2 - a, 12)}, {mp.nstr(a - b / 2, 12)})")
    check("A2  L = diag(b/2-a, a-b/2) [closed form]", r4["L_err"], need=DPS - 20)
    print(f"    [info] A1 C-0 formal residual {mp.nstr(r4['C0'], 5)} vs "
          f"truncation error {mp.nstr(mp.e ** (-R), 5)}")
    check("A1  C-0 formal residual at or below the truncation error",
          r4["C0"], scale=mp.e ** (-R), need=0)
    check("A3a U'(a,b,z) = -a U(a+1,b+1,z) [mpmath]", r4["Uprime_identity"], need=30)
    check("A3b recessive column vs mpmath U, ray +pi/2", r4["A3_upper"])
    check("A3c recessive column vs mpmath U, ray -pi/2 (crosses arg z = 0)",
          r4["A3_lower"])
    check("A4a tr M0 = 2 cos(pi b) [closed form]", r4["trM0_err"])
    check("A4b det M0 = 1 [trace-free gauge]", r4["detM0_err"])
    check("A5  M0 * M_inf(cw) = I", r4["MM_err"])
    print(f"    [info] S_pi is {r4['Spi_which']} triangular, "
          f"S_2pi is {r4['S2pi_which']} triangular, opposite = {r4['opposite']}")
    assert r4["opposite"], "the two Stokes matrices are in the SAME triangle"
    check("A6a S_pi unipotent (diag = 1)", r4["Spi_unip"])
    check("A6b S_pi triangular (one off-diagonal = 0)", r4["Spi_tri"])
    check("A6c S_2pi unipotent (diag = 1)", r4["S2pi_unip"])
    check("A6d S_2pi triangular (one off-diagonal = 0)", r4["S2pi_tri"])
    check("A6e M_inf,ccw = e^{2 pi i L} S_2pi S_pi", r4["fact_err"])
    check("A6f alpha = e^{i pi b - 2 pi i a} [closed form]", r4["alpha_err"])
    check("A7  f1 f2 = (2cos(pi b) - 1/alpha)/alpha - 1 [DEPENDENT on A4a/A6e]",
          r4["f1f2_err"])
    check("C-7 step halving (h_factor 4 vs 8)", S.mnorm(r4["M0"] - r8["M0"]))
    print(f"    f1 = {mp.nstr(r4['f1'], 30)}")
    print(f"    f2 = {mp.nstr(r4['f2'], 30)}")

print("\n" + "=" * 78)
if failures:
    print("STAGE 1 FALSIFIER FIRED - the session does NOT proceed to Stage 2")
    for f in failures:
        print("   ", f)
    sys.exit(1)
print(f"STAGE 1 PASSED - every closed-form target met at >= {DIGITS_REQUIRED} "
      "digits, at both parameter values")
print("=" * 78)
