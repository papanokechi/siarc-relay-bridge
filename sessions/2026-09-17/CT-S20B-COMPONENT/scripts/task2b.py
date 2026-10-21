"""TASK 2b: is thi as given in SS3 consistent with System C's local data at
infinity?

Two earlier attempts of mine were unsound; both are reported in the output,
because each would have produced a wrong answer silently.

Sound method.  At z = oo the system has
    N11 = -a/D -> t/2,  N22 -> -t/2,  N12 = -b/D = O(1/z^k),  N21 = O(1/z),
so the leading matrix is already diagonal with distinct entries +-t/2.  The
branch with rate +t/2 has eigenvector e1 + O(1/z), so its FIRST COMPONENT is
dominant and carries exponent equal to the 1/z-coefficient of N11 exactly --
no shift, and no degeneration, for any thi.  That is the branch to compare
with the b-route scalar equation (whose unknown is the first component).
The other branch has y1 = (N12/(lam_- - lam_+)) y2 (1+...), so its first
component is shifted by -k where k = ord_oo(N12); this predicts, rather than
assumes, the shift there.
"""
import os
from sympy import *

z, lam, TH = symbols('z lam TH')
s3, s11 = sqrt(3), sqrt(11)
s33 = s3 * s11


def head(R):
    """(R0, R1) with R = R0 + R1/z + O(1/z^2), by exact polynomial arithmetic."""
    n, d = fraction(together(R))
    pn, pd = Poly(expand(n), z), Poly(expand(d), z)
    dg = pd.degree()
    assert pn.degree() <= dg, 'not O(1) at infinity'

    def co(P, k):
        return P.coeff_monomial(z**k) if k > 0 else P.coeff_monomial(1)
    R0 = cancel(co(pn, dg) / co(pd, dg))
    R1 = cancel((co(pn, dg - 1) - R0 * co(pd, dg - 1)) / co(pd, dg))
    return R0, R1


p = 5 * I * (-28151758571 * s33 + 48874838016 * s11) / 4086468672
q = Rational(1, 2) + (-457937 * s11 * I + 281700 * s33 * I) / 122408
t = -2 * s33 * I / 9
thi_given = -2 - s3 / 9
th0 = th1 = Integer(0)


def entries(thi):
    D = z * (z - 1)
    a = (p + Rational(1, 2) * (-2 * q * t + t - thi) * (z - q)
         - Rational(1, 2) * t * (z - q)**2)
    b = (-(z * ((p + Rational(1, 2) * (q - 1) * q * t)**2 - th1**2 / 4
                + (q - 1) * (th0**2 / 4 - th1**2 / 4 - q * thi**2 / 4))) / q
         - ((q - 1) * (p + Rational(1, 2) * ((q - 1) * q * t - th0 + q * thi))
            * (p + Rational(1, 2) * ((q - 1) * q * t + th0 + q * thi))) / q)
    c = -(z - q) / (q - 1)
    return a, b, c, D


# ---- System C: scalar data at infinity ------------------------------------
delta = -I * s11 / 3
x = (-1 + I * s11) / 6 + delta * z
P_C = delta * (6 * x + 1) / (3 * x**2 + x + 1)
Q_C = delta**2 * (-x**2) / (3 * x**2 + x + 1)
P0, P1 = head(P_C)
Q0, Q1 = head(Q_C)
muC = {}
for l in solve(Eq(lam**2 + P0 * lam + Q0, 0), lam):
    muC[radsimp(simplify(l))] = radsimp(cancel(-(P1 * l + Q1) / (2 * l + P0)))
rate_dom = radsimp(simplify(t / 2))
rate_sub = radsimp(simplify(-t / 2))
rates_agree = set(muC) == {rate_dom, rate_sub}

# ---- the system with thi symbolic -----------------------------------------
a, b, c, D = entries(TH)
n11_0, n11_1 = head(-a / D)
sols = [radsimp(s) for s in
        solve(Eq(expand(fraction(cancel(n11_1 - muC[rate_dom]))[0]), 0), TH)]
hits = [simplify(s - thi_given) == 0 for s in sols]
nums = [str(N(Abs(N(s - thi_given, 40)), 6)) for s in sols]
consistent = any(hits)

# ---- the subdominant branch: predicted shift ------------------------------
def ord_inf(R):
    n, d = fraction(together(cancel(R)))
    return Poly(expand(d), z).degree() - Poly(expand(n), z).degree()


a0, b0, c0, D0 = entries(thi_given)
k_gen = ord_inf(-b / D)
k_pt = ord_inf(-b0 / D0)
n22_1 = head(a0 / D0)[1]
pred_sub = cancel(n22_1 - k_pt)
obs_sub = muC[rate_sub]
shift_ok = simplify(pred_sub - obs_sub) == 0
shift_num = str(N(Abs(N(pred_sub - obs_sub, 40)), 6))

# ---- CONTROLS THAT CAN FAIL -----------------------------------------------
control_sensitive = (cancel(diff(n11_1, TH)) != 0)
bad = cancel(n11_1.subs(TH, thi_given + 1) - muC[rate_dom])
control_discriminates = (bad != 0)

L = ["# TASK 2b - is thi consistent with System C's local data at infinity?", "",
     "## System C, scalar data at infinity",
     "    P = %s + %s/z + ... ,  Q = %s + %s/z + ..." % (P0, P1, radsimp(Q0), radsimp(Q1))]
for r in sorted(muC, key=str):
    L.append("    rate %-18s exponent mu = %s" % (r, muC[r]))
L += ["    rates coincide with +-t/2 = +-%s : %s" % (rate_dom, rates_agree), "",
      "## The system at the SS3 point, thi symbolic (TH)",
      "    N11 = -a/D = %s + (%s)/z + O(1/z^2)" % (n11_0, n11_1),
      "    leading matrix diag(t/2, -t/2), distinct, so the rate +t/2 branch has",
      "    eigenvector e1 + O(1/z): its first component carries exponent N11_1",
      "    exactly, for every thi.", "",
      "## Test on the dominant branch (rate %s)" % rate_dom,
      "    exponent demanded by System C : %s" % muC[rate_dom],
      "    exponent from the system      : %s" % n11_1,
      "    TH solving the two            : %s" % [str(s) for s in sols],
      "    thi printed in SS3            : %s" % thi_given,
      "    printed thi is a solution (simplify of the difference; radicals are",
      "      never compared with ==) : %s" % any(hits),
      "    |solution - printed thi| at dps 40 : %s" % nums, "",
      "## Subdominant branch (rate %s): shift predicted, not assumed" % rate_sub,
      "    ord_oo(N12) = %d generically in thi, %d at the printed thi" % (k_gen, k_pt),
      "    y1 = N12/(lam_- - lam_+) * y2 * (1+...) => exponent = N22_1 - ord",
      "    predicted %s ;  System C gives %s ;  equal: %s" % (pred_sub, obs_sub, shift_ok),
      "    |predicted - observed| at dps 40 : %s" % shift_num, "",
      "## Two unsound attempts of my own, recorded",
      "    (1) thi symbolic inside the SCALAR reduction, heads read at oo.",
      "        Unsound: deg_z b drops from 1 to 0 at the printed thi, so the",
      "        heads are discontinuous in thi exactly there.  Symptom: the",
      "        symbolic-thi exponents summed to -1, System C's sum to -2 = -P1.",
      "    (2) comparing the gauge-'invariant' difference mu(+) - mu(-) between",
      "        system and scalar.  Unsound: the two branches do NOT share a",
      "        common power of z here -- their shifts are 0 and %d -- so the" % (-k_pt),
      "        difference is not invariant.  It returned thi = sqrt(3)/9, i.e.",
      "        it was wrong by exactly the shift, 2.",
      "    Both are discarded; neither is used above.", "",
      "## Controls that can fail", "",
      "    control_sensitive: fires (PASS=False) if the system-side exponent did",
      "      not depend on TH, making the test unable to tell any thi from any",
      "      other.  PASS = %s" % control_sensitive,
      "    control_discriminates: fires (PASS=False) if the same test also",
      "      accepted thi + 1.  PASS = %s   (residual %s)" % (control_discriminates, bad),
      "", "## Verdict",
      "    thi as printed in SS3 is consistent with System C's local data at",
      "    infinity: %s" % consistent, ""]

out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   'outputs', 'task2b.md')
with open(out, 'w', encoding='utf-8') as f:
    f.write("\n".join(L) + "\n")
with open(out, encoding='utf-8') as f:
    back = f.read()
assert 'Verdict' in back and 'control_discriminates' in back, 'WRITE-BACK FAILED'
print(back)
print('READBACK OK', out, len(back))
