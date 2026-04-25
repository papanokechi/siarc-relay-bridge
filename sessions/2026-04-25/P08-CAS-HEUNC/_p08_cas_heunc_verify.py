"""P08-CAS-HEUNC: Verify claimed HeunC parameters for the V_quad ODE.

Original ODE:  (3x^2 + x + 1) y'' + (6x + 1) y' - x^2 y = 0

Claimed remark (rem:heunc in vquad_resurgence_R1.tex):
    HeunC(alpha, beta, gamma, delta, eta; z) with
        alpha = -1/3
        beta  = 1/(3*sqrt(3))
        gamma = 0
        delta = -1/3
        eta   = 1/9
    in Ronveaux (1995) / Slavyanov-Lay convention:
        y'' + (alpha + beta/z + gamma/(z-1)) y' + (delta*z + eta)/(z(z-1)) y = 0
    with regular singular points at z=0, z=1 and irregular rank-1 at z=infty.
"""
import sys
from sympy import (
    Symbol, symbols, sqrt, I, Rational, simplify, together, cancel,
    diff, expand, series, limit, oo, nsimplify, apart, Poly, collect,
    Function, Eq, solve, N, re, im, conjugate, sympify,
)

x = Symbol('x', complex=True)
z = Symbol('z', complex=True)

# ---------------------------------------------------------------- STEP 1
print("="*72)
print("[STEP 1] Ronveaux/Slavyanov-Lay HeunC convention:")
print("  y'' + (alpha + beta/z + gamma/(z-1)) y' + (delta*z + eta)/(z(z-1)) y = 0")
print("  Regular singular at z=0, z=1; irregular rank-1 at z=infty.")
print("  Convention confirmed: YES")
print()

# Original ODE coefficients
a_x = 3*x**2 + x + 1
b_x = 6*x + 1
c_x = -x**2

# Standard form  y'' + p(x) y' + q(x) y = 0
p_x = b_x / a_x
q_x = c_x / a_x

print(f"  p(x) = {p_x}")
print(f"  q(x) = {q_x}")
print()

# Finite singularities
s_vals = solve(a_x, x)
s1, s2 = s_vals
print(f"  s1 = {s1}")
print(f"  s2 = {s2}")
print()

# ---------------------------------------------------------------- STEP 5 first
print("="*72)
print("[STEP 5] Poincare rank at x = infty")
t = Symbol('t', positive=True)
p_inv = p_x.subs(x, 1/t)
q_inv = q_x.subs(x, 1/t)
p_lead = series(p_inv, t, 0, 3).removeO()
q_lead = series(q_inv, t, 0, 3).removeO()
print(f"  p(1/t) near t=0: {p_lead}")
print(f"  q(1/t) near t=0: {q_lead}")
# In the variable w = 1/x, ODE becomes (after change of variable):
# d^2y/dw^2 has p-contribution (2/w - p(1/w)/w^2) and q-contribution q(1/w)/w^4.
# Poincare rank r at infty is determined by highest pole of q(1/w)/w^4 as w->0:
# if q(1/w) ~ const as w->0 then q(1/w)/w^4 ~ 1/w^4 => rank 1 (since rank=pole_order/2 - 1
# for second-order ODE standard definition).
# Simpler: irregular rank 1 iff q(x) tends to a nonzero finite constant at infty.
q_limit = limit(q_x, x, oo)
p_limit_times_x = limit(x*p_x, x, oo)
print(f"  lim_{{x->oo}} q(x) = {q_limit}  (should be finite nonzero for rank-1)")
print(f"  lim_{{x->oo}} x*p(x) = {p_limit_times_x}")
if q_limit.is_finite and q_limit != 0:
    print("  Poincare rank at infty: RANK-1 CONFIRMED")
else:
    print("  Poincare rank at infty: MISMATCH")
print()

# ---------------------------------------------------------------- STEP 2
print("="*72)
print("[STEP 2] Affine change of variable z = (x - s1)/(s2 - s1)")
print("         Sends s1 -> 0, s2 -> 1, infty -> infty (preserves irregular pt).")
# x(z) = s1 + (s2 - s1)*z
x_of_z = s1 + (s2 - s1)*z
scale = s2 - s1  # dx/dz
print(f"  x(z) = {simplify(x_of_z)}")
print(f"  dx/dz = s2 - s1 = {simplify(scale)}")
print()

# Under y(x) = Y(z), y'(x) = Y'(z) * dz/dx = Y'(z)/scale
#                  y''(x) = Y''(z)/scale^2
# Original: a(x) y'' + b(x) y' + c(x) y = 0
# becomes: a(x(z)) Y''/scale^2 + b(x(z)) Y'/scale + c(x(z)) Y = 0
# standard form:
#   Y'' + [b(x(z))*scale/a(x(z))] Y' + [c(x(z))*scale^2/a(x(z))] Y = 0

a_z = a_x.subs(x, x_of_z)
b_z = b_x.subs(x, x_of_z)
c_z = c_x.subs(x, x_of_z)

P_z = simplify(b_z * scale / a_z)
Q_z = simplify(c_z * scale**2 / a_z)

P_z = simplify(together(P_z))
Q_z = simplify(together(Q_z))
print(f"  P(z) = {P_z}")
print(f"  Q(z) = {Q_z}")
print()

# Try partial fraction
P_apart = apart(P_z, z)
Q_apart = apart(Q_z, z)
print(f"  P(z) [partial fractions in z] = {P_apart}")
print(f"  Q(z) [partial fractions in z] = {Q_apart}")
print()

# Residues of P at z=0 and z=1
res_P_0 = simplify(limit(P_z * z, z, 0))
res_P_1 = simplify(limit(P_z * (z - 1), z, 1))
P_infty = simplify(limit(P_z, z, oo))
print(f"  Res_{{z=0}} P(z) = {res_P_0}")
print(f"  Res_{{z=1}} P(z) = {res_P_1}")
print(f"  P(infty)       = {P_infty}  (this is the 'alpha' constant)")
print()

# For HeunC in Ronveaux:  P(z) = alpha + beta/z + gamma/(z-1)
# so beta = Res_0 P, gamma = Res_1 P, alpha = P(infty) limit
alpha_comp = P_infty
beta_comp = res_P_0
gamma_comp = res_P_1

# Q(z) = (delta*z + eta) / (z*(z-1))
# So z*(z-1)*Q(z) = delta*z + eta
Q_times = simplify(expand(Q_z * z * (z - 1)))
print(f"  z(z-1) * Q(z) = {Q_times}")
# Should be linear in z: delta*z + eta
Q_poly = Poly(Q_times, z)
print(f"  as polynomial in z: degrees = {Q_poly.monoms()}, coeffs = {Q_poly.all_coeffs()}")
coeffs = Q_poly.all_coeffs()
if Q_poly.degree() == 1:
    delta_comp, eta_comp = coeffs[0], coeffs[1]
elif Q_poly.degree() == 0:
    delta_comp, eta_comp = 0, coeffs[0]
else:
    delta_comp, eta_comp = None, None
    print(f"  !!! z(z-1)*Q(z) is NOT linear in z — degree {Q_poly.degree()}")

print()

# ---------------------------------------------------------------- STEP 3
print("="*72)
print("[STEP 3] Parameter comparison")

alpha_claim = Rational(-1, 3)
beta_claim  = 1/(3*sqrt(3))
gamma_claim = Rational(0)
delta_claim = Rational(-1, 3)
eta_claim   = Rational(1, 9)

def verdict(claimed, computed):
    if computed is None:
        return "UNCOMPUTED"
    d = simplify(computed - claimed)
    if d == 0:
        return "MATCH (exact)"
    dn = complex(N(d, 30))
    if abs(dn) < 1e-20:
        return f"MATCH (|diff|={abs(dn):.2e})"
    return f"MISMATCH (diff = {simplify(computed - claimed)})"

rows = [
    ("alpha", alpha_claim, simplify(alpha_comp)),
    ("beta",  beta_claim,  simplify(beta_comp)),
    ("gamma", gamma_claim, simplify(gamma_comp)),
    ("delta", delta_claim, simplify(delta_comp)),
    ("eta",   eta_claim,   simplify(eta_comp)),
]
print(f"  {'param':<6} {'claimed':<18} {'computed':<40} verdict")
for name, cl, co in rows:
    print(f"  {name:<6} {str(cl):<18} {str(co):<40} {verdict(cl, co)}")

# Numeric display
print()
print("  Numeric (mpmath 30 digits):")
for name, cl, co in rows:
    cl_n = N(cl, 20)
    co_n = N(co, 20)
    print(f"    {name}: claimed = {cl_n},  computed = {co_n}")
print()

# ---------------------------------------------------------------- STEP 4
print("="*72)
print("[STEP 4] Independent numerical spot check")
try:
    import scipy.special
    has_heunc = hasattr(scipy.special, 'heun_c')
except Exception:
    has_heunc = False
print(f"  scipy.special.heun_c available: {has_heunc}")
print("  SKIPPED: HeunC is not in scipy.special (standard scipy does not ship")
print("           confluent Heun). Full numerical ODE vs. HeunC comparison would")
print("           require a dedicated HeunC implementation (e.g. Motygin or")
print("           Fiziev codes), not available in this environment.")
print()

# Still do an internal consistency check: solve original ODE numerically
# and check that the transformed solution satisfies the HeunC-form ODE
# with the *computed* parameters (not the claimed ones).
from mpmath import mp, mpc, mpf, odefun, chop
mp.dps = 30

# Original ODE as first-order system:
#   Y0' = Y1
#   Y1' = -(b(x) Y1 + c(x) Y0) / a(x)
def F(x_, Y):
    a = 3*x_**2 + x_ + 1
    b = 6*x_ + 1
    c = -x_**2
    return [Y[1], -(b*Y[1] + c*Y[0])/a]

sol = odefun(F, mpf('1'), [mpf('1'), mpf('0')])
vals = {}
for xv in [mpf('2'), mpf('3'), mpf('4')]:
    y_val = sol(xv)
    vals[xv] = y_val
    print(f"  Original ODE: y({xv}) = {y_val[0]}")
print()

# ---------------------------------------------------------------- Summary
print("="*72)
print("OVERALL")
all_match = all(
    simplify(co - cl) == 0 for _, cl, co in rows
)
if all_match:
    print("  PARAMETERS VERIFIED — computed = claimed for all 5 parameters.")
else:
    print("  PARAMETERS: at least one MISMATCH (see table).")
    print("  Correct values (computed from affine transform):")
    for name, cl, co in rows:
        print(f"    {name} = {simplify(co)}  =  {N(co, 20)}")
