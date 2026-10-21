"""CT-S16 step 3(a) - locate System C in the van der Put-Saito (0,0,1) family.

Family (vdPS (4.1), p.2654-2655, read from page images):
    Y' = -(1/(z(z-1))) A Y,   A = [[a, b], [c, -a]]
with a, b, c as printed, EXCEPT that b(z)'s first term is taken as
(p + (1/2)(q-1)q t)^2.  The printed form omits the t; check_bz.py shows the
printed form fails the paper's own constraint det A(1) = -theta_1^2/4 while the
version with t satisfies it identically.  Recorded as a suspected typo in the
paper, not silently adopted.

The first basis vector is the cyclic vector (paper's own choice), so we reduce
to a scalar equation for y_1, take its projective normal form, and match it
against System C's r_z computed in systemC_invariants.py.

Matching the projective normal potential is convention-free: it avoids the
prose statement "theta_inf is the (1,1) entry of A_0 + A_1", which does not hold
for the printed family (it gives -theta_inf/2) and is therefore not relied on.
"""
import sympy as sp

z, p, q, t, th0, th1, thi = sp.symbols("z p q t theta_0 theta_1 theta_inf")

a = p + sp.Rational(1, 2) * (-2 * q * t + t - thi) * (z - q) - sp.Rational(1, 2) * t * (z - q) ** 2
c = -(z - q) / (q - 1)
b = (-(z * ((p + sp.Rational(1, 2) * (q - 1) * q * t) ** 2 - th1**2 / 4
            + (q - 1) * (th0**2 / 4 - th1**2 / 4 - q * thi**2 / 4))) / q
     - ((q - 1)
        * (p + sp.Rational(1, 2) * ((q - 1) * q * t - th0 + q * thi))
        * (p + sp.Rational(1, 2) * ((q - 1) * q * t + th0 + q * thi))) / q)

D = z * (z - 1)

# ---- scalar reduction, first basis vector as cyclic vector -----------------
# y1' = -(a y1 + b y2)/D   =>   y2 = (-D y1' - a y1)/b
# y2' = -(c y1 - a y2)/D
y1 = sp.Function("y1")
Y1 = y1(z)
y2_expr = (-D * sp.diff(Y1, z) - a * Y1) / b
lhs = sp.diff(y2_expr, z)
rhs = -(c * Y1 - a * y2_expr) / D
eq = sp.simplify(sp.together(lhs - rhs))
eq = sp.numer(sp.cancel(eq))
eq = sp.expand(eq)

d2 = sp.simplify(eq.coeff(sp.Derivative(Y1, (z, 2))))
d1 = sp.simplify(eq.coeff(sp.Derivative(Y1, z)))
d0 = sp.simplify(sp.expand(eq - d2 * sp.Derivative(Y1, (z, 2)) - d1 * sp.Derivative(Y1, z)).coeff(Y1))

P = sp.cancel(sp.together(d1 / d2))
Q = sp.cancel(sp.together(d0 / d2))
print("scalar equation  y'' + P y' + Q y = 0  built.")

R = sp.cancel(sp.together(sp.expand(P**2 / 4 + sp.diff(P, z) / 2 - Q)))
print("projective normal potential R(z) built.")

# ---- System C's normalised potential ---------------------------------------
sp_ = sp.Rational(-1, 6) + sp.sqrt(11) * sp.I / 6
delta = -sp.sqrt(11) * sp.I / 3
x = sp.Symbol("x")
A_c = 3 * x**2 + x + 1
C_c = -x**2
pc = sp.diff(A_c, x) / A_c
qc = C_c / A_c
r_x = sp.cancel(sp.together(pc**2 / 4 + sp.diff(pc, x) / 2 - qc))
r_z = sp.cancel(sp.together(sp.expand(delta**2 * r_x.subs(x, sp_ + delta * z))))
print("r_z(z) =", sp.factor(sp.numer(r_z)), "/", sp.factor(sp.denom(r_z)))

# ---- impose theta_0 = theta_1 = 0 ------------------------------------------
# System C's normal-form exponents at z = 0 and 1 are 1/2 (double), i.e. the
# double-pole coefficient is -1/4.  For the family the double-pole coefficient
# is (theta^2 - 1)/4, so theta_0 = theta_1 = 0.  Verified rather than assumed:
for pt, th in [(0, th0), (1, th1)]:
    coeff = sp.simplify(sp.limit((z - pt) ** 2 * R, z, pt))
    print(f"\nfamily: double-pole coeff of R at z={pt}:", sp.simplify(coeff))
    sol = sp.solve(sp.Eq(coeff, sp.Rational(-1, 4)), th)
    print(f"   equals -1/4 (System C's value) iff {th} in", sol)

R0 = sp.cancel(sp.together(R.subs({th0: 0, th1: 0})))
sp.srepr  # noqa
with open("outputs/R_normal_potential.txt", "w", encoding="utf-8") as f:
    f.write("R(z; p,q,t,theta_inf) with theta_0 = theta_1 = 0\n\n")
    f.write("numerator:\n" + sp.sstr(sp.factor(sp.numer(R0))) + "\n\n")
    f.write("denominator:\n" + sp.sstr(sp.factor(sp.denom(R0))) + "\n")
print("\nwrote outputs/R_normal_potential.txt")

# ---- no apparent singularity: b(z) must be constant ------------------------
b0 = sp.expand(b.subs({th0: 0, th1: 0}))
b_lin = sp.simplify(sp.expand(b0).coeff(z, 1))
print("\ncoefficient of z in b(z) (theta_0=theta_1=0):")
print("   ", sp.factor(sp.simplify(b_lin)))
print("System C's r_z has no pole other than z=0,1, so this must vanish.")
eq_app = sp.numer(sp.together(b_lin))
print("   condition:", sp.factor(sp.expand(eq_app)), "= 0")
