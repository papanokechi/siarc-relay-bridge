"""
CT-R1-AUDIT R2: independent spot-check of CT-S6-APPARENCY.

Re-derives, from scratch and exactly, the load-bearing CT-S6 results.
Nothing is imported from the CT-S6 session; every object below is rebuilt
from the companion paper's equation (6)-(7) and from CT-S5B's published
normal form for System B.
"""
import sympy as sp

x, z, lam = sp.symbols('x z lambda')
out = []


def say(tag, s):
    line = f"[{tag}] {s}"
    print(line)
    out.append(line)


def normal_form(p, q, v):
    """u'' + p u' + q u = 0  ->  w'' = R w  with  R = p^2/4 + p'/2 - q."""
    return sp.cancel(sp.together(p**2 / 4 + sp.diff(p, v) / 2 - q))


# ---------------------------------------------------------------- System C
# Companion v1.2 section 2.2, eq. (6)-(7).
a = 3 * x**2 + x + 1
b = 6 * x + 1
c = -x**2

say("C0", f"exactness b == a' : {sp.simplify(b - sp.diff(a, x)) == 0}")

p_C = sp.cancel(b / a)
q_C = sp.cancel(c / a)
R_C = normal_form(p_C, q_C, x)
say("C1", f"System C normal form R_C = {sp.factor(sp.numer(R_C))} / {sp.factor(sp.denom(R_C))}")

# ------------------------------------------- System B, inverted (CT-S5B)
# CT-S6 reports System B's normal form; invert it independently here.
R_B = (11 * z**4 + 4 * z**2 + 4 * z + 12) / (4 * z**4 * (z**2 + z + 3)**2)
# phi(x) = 1/x ;  R~(x) = (phi')^2 R(phi) - {phi,x}/2 ,  and {1/x,x} = 0.
phi = 1 / x
R_Binv = sp.cancel(sp.diff(phi, x)**2 * R_B.subs(z, phi))
say("B1", f"inverted System B normal form = {sp.factor(sp.numer(R_Binv))} / {sp.factor(sp.denom(R_Binv))}")

say("EQ", f"R_C - R_Binv == 0 : {sp.simplify(R_C - R_Binv) == 0}")

# --------------------------------- System B at z = oo  <->  x = 0
say("B2", f"R_Binv at x=0 is finite, value {sp.simplify(R_Binv.subs(x, 0))} "
          f"-> x=0 is an ORDINARY point of the normal form")

# ------------------------------- System C at the roots of a : apparency
roots = sp.solve(sp.Eq(a, 0), x)
for r in roots:
    # exponents of the ORIGINAL equation
    p0 = sp.simplify(sp.limit((x - r) * p_C, x, r))
    q0 = sp.simplify(sp.limit((x - r)**2 * q_C, x, r))
    ind = sp.expand(lam * (lam - 1) + p0 * lam + q0)
    ex = sp.roots(sp.Poly(ind, lam))
    # residue of the normal form
    nu = sp.simplify(sp.limit((x - r)**2 * R_C, x, r))
    say("C2", f"x = {sp.nsimplify(r)} : p0 = {p0}, q0 = {q0}, indicial = {ind}, "
              f"exponents = {ex}, normal-form residue = {nu}")

# ------------------- the general refutation of companion Remark 2.2
chi = sp.Function('chi')
say("G1", "General: for  chi*y'' + chi'*y' + c*y = 0  at a SIMPLE root s of chi with c(s) != 0, "
          "p = chi'/chi has residue exactly 1 and (x-s)^2*q -> 0, so the indicial polynomial is "
          "lambda*(lambda-1) + 1*lambda + 0 = lambda^2.  The exponents are 0,0 for EVERY such chi and c. "
          "Equal exponents at a genuine regular singular point always force a log term in the second "
          "Frobenius solution, so the point is NEVER apparent.")

# sanity: the same computation on two other chi, as CT-S6 did
for chi_expr, cc in [(x + 1, -x**2), (x**2 + 1, -x**2)]:
    pp = sp.cancel(sp.diff(chi_expr, x) / chi_expr)
    qq = sp.cancel(cc / chi_expr)
    for r in sp.solve(sp.Eq(chi_expr, 0), x):
        p0 = sp.simplify(sp.limit((x - r) * pp, x, r))
        q0 = sp.simplify(sp.limit((x - r)**2 * qq, x, r))
        say("G2", f"chi = {chi_expr}, root {r}: p0 = {p0}, q0 = {q0}, "
                  f"indicial = {sp.expand(lam*(lam-1) + p0*lam + q0)}")

# ------------------------------------------ System C at infinity
t = sp.symbols('t')
R_inf = sp.cancel(sp.diff(1 / t, t)**2 * R_C.subs(x, 1 / t))
ser = sp.nsimplify(sp.cancel(R_inf))
pole = sp.degree(sp.denom(ser), t) - sp.degree(sp.numer(ser), t)
say("I1", f"R_C at infinity (t = 1/x): {sp.factor(sp.numer(ser))} / {sp.factor(sp.denom(ser))}")
say("I2", f"pole order in t at t=0 : {pole}  -> Katz = pole/2 - 1 = {sp.Rational(pole, 2) - 1}")

with open("verify_s6.out", "w", encoding="utf-8") as f:
    f.write("\n".join(out) + "\n")
