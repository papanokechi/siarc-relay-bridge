"""CT-S16 step 2 - System C's module invariants in van der Put-Saito normalisation.

Framework (INSPECTED, vdPS p.2637 sec 3.2 and p.2654 sec 4.3, read from page
images): a type-(0,0,1) module is represented by

    d/dz + A_0/z + A_1/(z-1) + A_inf ,   tr A_i = 0,  A_inf = (t/2)diag(-1,1),

with singular points normalised to z = 0, 1, infinity, local exponents
+-theta_0/2, +-theta_1/2, and generalized local exponents +-(t z + theta_inf)/2
at infinity.  So t is the SCALE OF THE IRREGULAR TYPE AT INFINITY, not the
position of a singular point.

System C (companion v1.2):  A W'' + A' W' + C W = 0,
A = 3x^2 + x + 1, C = -x^2.  Its two regular singular points are the roots of A.

Plan: normalise the two finite singular points to 0 and 1 by the affine map
z = (x - s_plus)/(s_minus - s_plus) (affine maps fix infinity, so the irregular
point stays at infinity), then read off theta_0, theta_1, theta_inf and t.

P0: symbolic equality is simplify-to-zero PLUS a high-precision numeric check.
"""
import sympy as sp

x, z = sp.symbols("x z")

A = 3 * x**2 + x + 1
Cc = -x**2

# --- trace-free (projective) normal form  u'' = r u -------------------------
p_coef = sp.diff(A, x) / A
q_coef = Cc / A
r = sp.simplify(p_coef**2 / 4 + sp.diff(p_coef, x) / 2 - q_coef)
r = sp.cancel(sp.together(r))
print("r_C(x) =", sp.factor(sp.numer(r)), "/", sp.factor(sp.denom(r)))

r_known = (12 * x**4 + 4 * x**3 + 4 * x**2 + 11) / (4 * (3 * x**2 + x + 1) ** 2)
d = sp.simplify(sp.together(r - r_known))
print("matches recorded potential (difference simplifies to):", d)
assert d == 0
# numeric confirmation (P0 rule: never rely on symbolic == alone)
import mpmath as mp
mp.mp.dps = 60
f1 = sp.lambdify(x, r, "mpmath")
f2 = sp.lambdify(x, r_known, "mpmath")
worst = max(abs(f1(mp.mpf(v) + mp.mpf("0.3")) - f2(mp.mpf(v) + mp.mpf("0.3")))
            for v in [1, 2, 5, -3, 7])
print("numeric worst |diff| at dps60:", mp.nstr(worst, 5))

# --- singular points --------------------------------------------------------
roots = sp.solve(A, x)
s_p = [rt for rt in roots if sp.im(sp.nsimplify(rt)) > 0][0]
s_m = [rt for rt in roots if sp.im(sp.nsimplify(rt)) < 0][0]
print("\ns_+ =", sp.simplify(s_p), "   s_- =", sp.simplify(s_m))
delta = sp.simplify(s_m - s_p)
print("delta = s_- - s_+ =", delta, " ; delta^2 =", sp.simplify(delta**2))

# --- normalise to z = 0, 1 --------------------------------------------------
# x = s_+ + delta*z  =>  d^2u/dz^2 = delta^2 * r(x(z)) * u
r_z = sp.simplify(delta**2 * r.subs(x, s_p + delta * z))
r_z = sp.cancel(sp.together(sp.expand(r_z)))
num, den = sp.fraction(r_z)
print("\nr_z(z) numerator  =", sp.factor(sp.expand(num)))
print("r_z(z) denominator=", sp.factor(sp.expand(den)))

# --- local data at z = 0 and z = 1 -----------------------------------------
for pt, name in [(0, "0"), (1, "1")]:
    b2 = sp.simplify(sp.limit((z - pt) ** 2 * r_z, z, pt))
    rho = sp.solve(sp.Symbol("R") * (sp.Symbol("R") - 1) - b2, sp.Symbol("R"))
    print(f"\nz = {name}: double-pole coefficient = {b2}")
    print(f"          normal-form exponents rho(rho-1)=coeff -> {rho}")

# --- local data at infinity -------------------------------------------------
w = sp.Symbol("w", positive=True)
ser = sp.series(r_z.subs(z, 1 / w), w, 0, 3).removeO()
ser = sp.expand(ser)
c0 = sp.simplify(ser.subs(w, 0))
c1 = sp.simplify(sp.diff(ser, w).subs(w, 0))
print("\nexpansion of r_z at infinity:  r_z = c0 + c1/z + O(1/z^2)")
print("  c0 =", c0, "   c1 =", c1)

# u ~ exp(+-(t z + theta_inf ln z)/2)  =>  r_z = t^2/4 + t*theta_inf/(2 z) + ...
t_sym = sp.symbols("t")
t_vals = sp.solve(sp.Eq(t_sym**2 / 4, c0), t_sym)
print("\n  t^2/4 = c0  =>  t =", [sp.simplify(v) for v in t_vals])
for tv in t_vals:
    th_inf = sp.simplify(2 * c1 / tv)
    print(f"    for t = {sp.simplify(tv)}:  theta_inf = 2*c1/t = {sp.radsimp(th_inf)}")

companion_t = [sp.simplify(-2 * sp.I * sp.sqrt(33) / 9), sp.simplify(2 * sp.I * sp.sqrt(33) / 9)]
print("\ncompanion's stated t = -+2i*sqrt(33)/9 =", companion_t)
print("computed t set equals companion set:",
      {sp.simplify(v) for v in t_vals} == set(companion_t))
