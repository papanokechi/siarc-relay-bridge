"""TASK 2b: is thi as given in SS3 consistent with System C's local data at
infinity?

NOTE ON A DEFECT I CAUGHT IN MY OWN FIRST ATTEMPT (reported in the output).
My first method kept thi symbolic inside the *scalar* b-route reduction and
read its head coefficients at z = oo.  That is unsound here: at the printed
thi the coefficient of z in b(z) vanishes, so deg_z b drops from 1 to 0 and
the head coefficients are discontinuous in thi.  The symptom was that the two
symbolic-thi exponents summed to -1 while System C's sum to -2.  This version
works instead with the SYSTEM's eigenvalues at infinity, whose leading term
is -t/2 (t =/= 0) for every thi, so no degree drop occurs.

Method.  N is trace-free, so its eigenvalues are +-sqrt(a^2+bc)/D =: +-E(z).
Write E = E0 + E1/z + O(1/z^2).  The formal solutions at oo are
e^{+-E0 z} z^{+-E1}(1+...), so the exponential rates are +-E0 and the
exponents are +-E1.
For the scalar side, y'' + P y' + Q y = 0 with P = P0 + P1/z + ...,
Q = Q0 + Q1/z + ... gives lam^2 + P0 lam + Q0 = 0, mu = -(P1 lam + Q1)/(2lam+P0).
A scalar reduction differs from the system by a factor z^k common to the two
branches, so the DIFFERENCE mu(+) - mu(-) along matched exponential rates is
the invariant to compare; the rates themselves are compared directly.
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
    co = lambda P, k: (P.coeff_monomial(z**k) if k > 0 else P.coeff_monomial(1)) if k >= 0 else 0
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


# ---- System C, scalar data at infinity ------------------------------------
delta = -I * s11 / 3
x = (-1 + I * s11) / 6 + delta * z
P_C = delta * (6 * x + 1) / (3 * x**2 + x + 1)
Q_C = delta**2 * (-x**2) / (3 * x**2 + x + 1)
P0, P1 = head(P_C)
Q0, Q1 = head(Q_C)
muC = {}
for l in solve(Eq(lam**2 + P0 * lam + Q0, 0), lam):
    muC[radsimp(simplify(l))] = radsimp(cancel(-(P1 * l + Q1) / (2 * l + P0)))
ratesC = sorted(muC, key=str)
dmuC = radsimp(simplify(muC[radsimp(simplify(-t / 2))] - muC[radsimp(simplify(t / 2))]))

# ---- the system, thi symbolic ---------------------------------------------
a, b, c, D = entries(TH)
G0, G1 = head((a**2 + b * c) / D**2)          # E^2 = G, E = sqrt(G)
E0p = radsimp(simplify(sqrt(G0)))             # = +-t/2
E1p = cancel(G1 / (2 * E0p))                  # exponent on the branch E0p
# branch with rate -E0p has exponent -E1p, so the matched difference is:
dmu_sys = cancel((-E1p if simplify(E0p + t / 2) == 0 else E1p)
                 - (E1p if simplify(E0p + t / 2) == 0 else -E1p))
# i.e. exponent(rate = -t/2) - exponent(rate = +t/2)
sols = [radsimp(s) for s in solve(Eq(expand(fraction(cancel(dmu_sys - dmuC))[0]), 0), TH)]
hits = [simplify(s - thi_given) == 0 for s in sols]
nums = [str(N(Abs(N(s - thi_given, 40)), 6)) for s in sols]

# rates
rate_ok = ({radsimp(simplify(E0p)), radsimp(simplify(-E0p))} ==
           {radsimp(simplify(t / 2)), radsimp(simplify(-t / 2))} ==
           set(ratesC))

# ---- corroboration at the printed thi (from task 2's exact equality) ------
a0, b0, c0, D0 = entries(thi_given)
deg_b_generic = Poly(expand(fraction(together(b))[0]), z).degree()
deg_b_at_point = Poly(expand(numer(cancel(b0))), z).degree()
dbdz = cancel(diff(b0, z))

# ---- CONTROLS THAT CAN FAIL -----------------------------------------------
control_sensitive = (cancel(diff(dmu_sys, TH)) != 0)
bad = cancel(dmu_sys.subs(TH, thi_given + 1) - dmuC)
control_discriminates = (bad != 0)

consistent = any(hits)

L = ["# TASK 2b - is thi consistent with System C's local data at infinity?", "",
     "## System C, scalar data at infinity",
     "    P = %s + %s/z + ...,   Q = %s + %s/z + ..." % (P0, P1, radsimp(Q0), radsimp(Q1))]
for l in ratesC:
    L.append("    rate lam = %-18s exponent mu = %s" % (l, muC[l]))
L += ["    invariant  mu(rate -t/2) - mu(rate +t/2) = %s" % dmuC, "",
      "## The SS1 system at the SS3 point, thi symbolic (TH)",
      "    eigenvalues of N are +-E, E = sqrt(a^2+bc)/D = E0 + E1/z + ...",
      "    E0 = %s   (=> rates +-t/2 = +-%s)" % (E0p, radsimp(simplify(t / 2))),
      "    E1 = %s" % E1p,
      "    exponential rates agree with System C's: %s" % rate_ok,
      "    invariant  mu(rate -t/2) - mu(rate +t/2) = %s" % cancel(dmu_sys), "",
      "## Solving the invariant for thi",
      "    TH with invariant equal to System C's : %s" % [str(s) for s in sols],
      "    thi printed in SS3                    : %s" % thi_given,
      "    printed thi is a solution (simplify of the difference; radicals are",
      "      never compared with ==) : %s" % any(hits),
      "    |solution - printed thi| at dps 40 : %s" % nums, "",
      "## Corroboration",
      "    Task 2 showed P_b - P_C = 0 and Q_b - Q_C = 0 exactly with this thi,",
      "    so the b-route reduction of the system built from SS3 IS System C and",
      "    every local datum agrees, at infinity included.", "",
      "## Defect caught in my own first attempt",
      "    First method: keep thi symbolic inside the SCALAR reduction and read",
      "    its heads at z = oo.  Unsound here: deg_z b = %d generically but %d"
      % (deg_b_generic, deg_b_at_point),
      "    at the printed thi (db/dz = %s), so the heads are discontinuous in" % dbdz,
      "    thi exactly at the point of interest.  Symptom: the symbolic-thi",
      "    exponents summed to -1 while System C's sum to -2 = -P1.  Discarded.",
      "", "## Controls that can fail", "",
      "    control_sensitive: fires (PASS=False) if the invariant did not depend",
      "      on TH, making the check unable to tell any thi from any other.",
      "      PASS = %s" % control_sensitive,
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
