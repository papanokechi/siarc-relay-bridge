"""Route S of the Appendix A formula pass: re-derive every computational
expression in appendixA.tex from the transcribed page source.

The transcription below is from refs/vdps_p2655.png, folio read off the page
(running head "MODULI FOR DIFFERENTIAL AND PAINLEVE EQUATIONS", folio 2655,
footer "TOME 59 (2009), FASCICULE 7").  It is the input under test: if the
vacuity pre-checks V1/V2/V4 fail, the transcription is wrong and no verdict
here means anything.

Nothing in this script reads the appendix to decide what the answer should be.
Each appendix expression is typed in as a literal and compared.
"""
import sys

import sympy as sp

p, q, t, z = sp.symbols("p q t z")
th0, th1, thi = sp.symbols("theta0 theta1 thetainf")

# ---------------------------------------------------------------------------
# Transcribed from journal page 2655.
# ---------------------------------------------------------------------------
# a(z) = p + 1/2(-2qt + t - theta_inf)(z - q) - 1/2 t (z - q)^2
a = p + sp.Rational(1, 2) * (-2 * q * t + t - thi) * (z - q) \
    - sp.Rational(1, 2) * t * (z - q) ** 2

# c(z) = -(z - q)/(q - 1)
c = -(z - q) / (q - 1)


def b_of(first_bracket):
    """b(z) with its first squared bracket supplied.

    The page prints   -( z*( BRACKET^2 - th1^2/4 + (q-1)(th0^2/4 - th1^2/4
                             - q*thinf^2/4) ) )/q
                      -( (q-1)(p + 1/2((q-1)qt - th0 + q*thinf))
                              (p + 1/2((q-1)qt + th0 + q*thinf)) )/q
    Only the first bracket differs between the printed and corrected readings.
    """
    term1 = -(z * (first_bracket ** 2
                   - th1 ** 2 / 4
                   + (q - 1) * (th0 ** 2 / 4 - th1 ** 2 / 4
                                - q * thi ** 2 / 4))) / q
    term2 = -((q - 1)
              * (p + sp.Rational(1, 2) * ((q - 1) * q * t - th0 + q * thi))
              * (p + sp.Rational(1, 2) * ((q - 1) * q * t + th0 + q * thi))) / q
    return term1 + term2


HALF = sp.Rational(1, 2)
PRINTED = p + HALF * (q - 1) * q                 # as printed, no t
CORRECTED = p + HALF * (q - 1) * q * t           # with the t
BOGUS = {
    "t^2":   p + HALF * (q - 1) * q * t ** 2,
    "t+1":   p + HALF * (q - 1) * q * (t + 1),
    "2t":    p + HALF * (q - 1) * q * (2 * t),
    # drawn from outside the appendix's own list
    "t/2":   p + HALF * (q - 1) * q * (t / 2),
    "t-1":   p + HALF * (q - 1) * q * (t - 1),
}

# B_1 (1,2) entry, transcribed from the same page.  Note the t is present here.
B1_12 = -((CORRECTED ** 2
           - th1 ** 2 / 4
           + (q - 1) * (th0 ** 2 / 4 - th1 ** 2 / 4 - q * thi ** 2 / 4)) / q)


def detA(first_bracket, at):
    """det of [[a, b], [c, -a]] = -a^2 - b c, evaluated at z = at."""
    expr = -a ** 2 - b_of(first_bracket) * c
    return sp.simplify(sp.expand(expr.subs(z, at)))


FAIL = []
OUT = []


def say(s=""):
    OUT.append(s)
    print(s)


def check(name, got, want, note=""):
    r = sp.simplify(sp.expand(sp.together(got - want)))
    ok = r == 0
    say("  %-7s %s%s" % ("MATCHES" if ok else "DIFFERS", name,
                         ("  " + note) if note else ""))
    if not ok:
        say("          residual: %s" % sp.simplify(r))
        FAIL.append(name)
    return ok


# ---------------------------------------------------------------------------
# Vacuity pre-checks, per PREREG section 4.  These run FIRST and halt.
# ---------------------------------------------------------------------------
say("=" * 74)
say("VACUITY PRE-CHECKS (PREREG section 4)")
say("=" * 74)

v1 = sp.simplify(detA(CORRECTED, 1) + th1 ** 2 / 4)
say("  V1 positive  det A(1) + th1^2/4 under CORRECTED reading = %s" % v1)
if v1 != 0:
    say("HALT: V1 failed. The transcription of a, b or c is wrong;")
    say("      no verdict in this script would be meaningful.")
    sys.exit(2)

v2 = sp.simplify(detA(PRINTED, 1) + th1 ** 2 / 4)
say("  V2 negative  same under PRINTED reading             = %s"
    % sp.factor(v2))
if v2 == 0:
    say("HALT: V2 failed. Both readings pass, so the test does not")
    say("      discriminate and the appendix's argument is void.")
    sys.exit(2)

say("  V3 control   %d bogus variants must each be REJECTED (%d of them "
    "drawn from outside the appendix's own list):"
    % (len(BOGUS), 2))
for nm, br in BOGUS.items():
    r = sp.simplify(detA(br, 1) + th1 ** 2 / 4)
    verdict = "REJECTED" if r != 0 else "ACCEPTED  <-- control failed"
    say("                 %-5s %s" % (nm, verdict))
    if r == 0:
        FAIL.append("V3 control %s accepted" % nm)

v4a = sp.simplify(detA(CORRECTED, 0) + th0 ** 2 / 4)
v4b = sp.simplify(detA(PRINTED, 0) + th0 ** 2 / 4)
say("  V4 reader    det A(0) + th0^2/4: corrected = %s, printed = %s"
    % (v4a, v4b))
if not (v4a == 0 and v4b == 0):
    say("HALT: V4 failed. The appendix states det A(0) does not discriminate;")
    say("      in this transcription it does, so A(z) is mis-transcribed.")
    sys.exit(2)
say()

# ---------------------------------------------------------------------------
# Route S: the appendix's computational displays, typed in as literals.
# ---------------------------------------------------------------------------
say("=" * 74)
say("ROUTE S -- appendix displays re-derived symbolically")
say("=" * 74)

# E7  S16-20: the det A(1) residual under the printed reading
E7 = -sp.Rational(1, 4) * (q - 1) * (t - 1) * (4 * p + q ** 2 * t + q ** 2
                                               - q * t - q)
say("E7  S16-20 det A(1) residual, printed reading")
check("E7", E7, v2)

# E8  S16-20: its value at the stated exact rational point
PT = {p: sp.Rational(2, 7), q: sp.Rational(5, 3), t: sp.Rational(11, 4),
      th0: 0, th1: 0, thi: sp.Rational(3, 5)}
got8 = sp.nsimplify(v2.subs(PT))
say("E8  S16-20 residual at p=2/7, q=5/3, t=11/4, th0=th1=0, thinf=3/5")
say("      appendix says -223/144;  re-derived = %s" % sp.Rational(got8))
if sp.Rational(got8) != sp.Rational(-223, 144):
    FAIL.append("E8")
    say("  DIFFERS E8")
else:
    say("  MATCHES E8")

# E10 S16-R18-02: corrected first term of b(z) equals z * B1[1,2]
first_corr = -(z * (CORRECTED ** 2 - th1 ** 2 / 4
                    + (q - 1) * (th0 ** 2 / 4 - th1 ** 2 / 4
                                 - q * thi ** 2 / 4))) / q
say("E10 S16-R18-02 corrected first term of b(z) == z * B1[1,2]")
check("E10", first_corr, z * B1_12)

# E11 S16-R18-02: the unfactored difference
first_prin = -(z * (PRINTED ** 2 - th1 ** 2 / 4
                    + (q - 1) * (th0 ** 2 / 4 - th1 ** 2 / 4
                                 - q * thi ** 2 / 4))) / q
true_diff = sp.simplify(sp.expand(first_prin - z * B1_12))

E11 = sp.Rational(1, 4) * z * (4 * p * q * t - 4 * p * q - 4 * p * t + 4 * p
                               + q ** 3 * t ** 2 - q ** 3
                               - 2 * q ** 2 * t ** 2 + 2 * q ** 2
                               + q * t ** 2 - q)
say("E11 S16-R18-02 difference, unfactored")
check("E11", E11, true_diff)

# E12 S16-R18-02: the difference, factored -- PREREG F4 predicts a sign error
E12 = -sp.Rational(1, 4) * z * (q - 1) * (t - 1) * (4 * p + q ** 2 * t
                                                    + q ** 2 - q * t - q)
say("E12 S16-R18-02 difference, factored  [PREREG F4 predicts sign error]")
check("E12", E12, true_diff)
say("      true factorisation: %s" % sp.factor(true_diff))

# E13 the two factored forms must carry the SAME factor, per the appendix's
# claim that "the two independent tests agree on the correction term for term"
say("E13 do the det A(1) residual and the difference carry the same factor?")
ratio = sp.simplify(sp.factor(true_diff) / sp.factor(v2))
say("      difference / detA(1)-residual = %s" % ratio)
if ratio.has(p) or ratio.has(th0) or ratio.has(th1) or ratio.has(thi):
    say("  DIFFERS E13  (not a bare multiple: the factor is not shared)")
    FAIL.append("E13")
else:
    say("  MATCHES E13  (shared factor; ratio is %s)" % ratio)

# E14 S16-21: the residual vanishes precisely at t = 1
say("E14 S16-21 printed residual vanishes at t=1")
check("E14", sp.simplify(v2.subs(t, 1)), sp.Integer(0))

# E15 S16-21: the two readings coincide at t = 1
say("E15 S16-21 the two readings coincide at t=1")
check("E15", sp.simplify((PRINTED - CORRECTED).subs(t, 1)), sp.Integer(0))

# E16 S16-18: c(0) = q/(q-1)
say("E16 S16-18 c(0) = q/(q-1)")
check("E16", sp.simplify(c.subs(z, 0)), q / (q - 1))

say()
say("=" * 74)
if FAIL:
    say("ROUTE S: %d of the checked displays DIFFER: %s"
        % (len(FAIL), ", ".join(FAIL)))
else:
    say("ROUTE S: all checked displays match")
say("=" * 74)

with open("outputs/route_s.out.txt", "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT) + "\n")

sys.exit(1 if FAIL else 0)
