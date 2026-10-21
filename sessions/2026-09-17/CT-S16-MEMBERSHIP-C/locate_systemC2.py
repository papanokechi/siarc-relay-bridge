"""CT-S16 step 3(a), efficient version.

Same computation as locate_systemC.py, but theta_0 = theta_1 = 0 is imposed
before the scalar reduction and sp.simplify / sp.limit are avoided (they were
the bottleneck).  Only cancel / Poly / factor are used.

theta_0 = theta_1 = 0 is JUSTIFIED, not assumed: the family's projective normal
potential has double-pole coefficient (theta^2 - 1)/4 at z = 0 and z = 1, and
System C's is -1/4 at both (systemC_invariants.py).  That check is redone here
symbolically before the substitution.
"""
import sympy as sp

z, p, q, t, th0, th1, thi = sp.symbols("z p q t theta_0 theta_1 theta_inf")


def build(th0v, th1v):
    a = (p + sp.Rational(1, 2) * (-2 * q * t + t - thi) * (z - q)
         - sp.Rational(1, 2) * t * (z - q) ** 2)
    c = -(z - q) / (q - 1)
    b = (-(z * ((p + sp.Rational(1, 2) * (q - 1) * q * t) ** 2 - th1v**2 / 4
                + (q - 1) * (th0v**2 / 4 - th1v**2 / 4 - q * thi**2 / 4))) / q
         - ((q - 1)
            * (p + sp.Rational(1, 2) * ((q - 1) * q * t - th0v + q * thi))
            * (p + sp.Rational(1, 2) * ((q - 1) * q * t + th0v + q * thi))) / q)
    return sp.cancel(a), sp.cancel(b), sp.cancel(c)


def normal_potential(a, b, c):
    """Projective normal potential of the scalar equation for y_1."""
    D = z * (z - 1)
    # y1'' + P y1' + Q y1 = 0 with
    #   P = (D' + ... ) derived from eliminating y2 by hand to keep it cheap.
    # y2 = (-D y1' - a y1)/b
    # y2' = -(c y1 - a y2)/D
    # => (-D y1' - a y1)'/b - (-D y1' - a y1) b'/b^2 = -(c y1 - a(-D y1' - a y1)/b)/D
    # Multiply by -b^2 D and collect.
    bp = sp.diff(b, z)
    ap = sp.diff(a, z)
    Dp = sp.diff(D, z)
    # LHS*b^2*D :  D*[(-D y1'' - Dp y1' - ap y1 - a y1')*b - (-D y1' - a y1)*bp]
    # RHS*b^2*D : -b^2 c y1 + a b (-D y1' - a y1)
    # Collect coefficients of y1'', y1', y1.
    c2 = D * (-D) * b
    c1 = D * ((-Dp - a) * b + D * bp) + a * b * D
    c0 = D * (-ap * b + a * bp) + b**2 * c + a**2 * b
    c2, c1, c0 = sp.cancel(c2), sp.cancel(c1), sp.cancel(c0)
    P = sp.cancel(c1 / c2)
    Q = sp.cancel(c0 / c2)
    R = sp.cancel(sp.together(P**2 / 4 + sp.diff(P, z) / 2 - Q))
    return P, Q, sp.cancel(R)


# ---------- 1. justify theta_0 = theta_1 = 0 --------------------------------
a_s, b_s, c_s = build(th0, th1)
_, _, R_sym = normal_potential(a_s, b_s, c_s)
num, den = sp.fraction(R_sym)
for pt, th in [(0, th0), (1, th1)]:
    # double-pole coefficient = lim (z-pt)^2 R, computed by series-free algebra
    expr = sp.cancel(((z - pt) ** 2 * R_sym))
    val = sp.cancel(expr.subs(z, pt))
    val = sp.factor(sp.cancel(val))
    print(f"double-pole coeff of R at z={pt}: {val}")
    sol = sp.solve(sp.Eq(val, sp.Rational(-1, 4)), th)
    print(f"   = -1/4  iff  {th} in {sol}")

# ---------- 2. System C's r_z ----------------------------------------------
x = sp.Symbol("x")
sp_root = sp.Rational(-1, 6) + sp.sqrt(11) * sp.I / 6
delta = -sp.sqrt(11) * sp.I / 3
A_c, C_c = 3 * x**2 + x + 1, -x**2
pc, qc = sp.diff(A_c, x) / A_c, C_c / A_c
r_x = sp.cancel(pc**2 / 4 + sp.diff(pc, x) / 2 - qc)
r_z = sp.cancel(sp.expand(delta**2 * r_x.subs(x, sp_root + delta * z)))
print("\nr_z =", sp.factor(sp.numer(r_z)), "/", sp.factor(sp.denom(r_z)))

# ---------- 3. match with theta_0 = theta_1 = 0 -----------------------------
a0, b0, c0_ = build(sp.Integer(0), sp.Integer(0))
b_lin = sp.factor(sp.Poly(sp.numer(sp.cancel(b0)), z).all_coeffs()[0])
print("\nleading (z) coefficient of b(z):", b_lin)
print("must vanish: System C's r_z has no apparent singularity")

_, _, R0 = normal_potential(a0, b0, c0_)
diff = sp.cancel(sp.together(R0 - r_z))
dn = sp.expand(sp.numer(diff))
poly = sp.Poly(dn, z)
print("\nmatching R(z) = r_z(z): numerator is a polynomial in z of degree",
      poly.degree())
eqs = [sp.factor(co) for co in poly.all_coeffs()]
with open("outputs/match_equations.txt", "w", encoding="utf-8") as f:
    for i, e in enumerate(eqs):
        f.write(f"--- coefficient of z^{poly.degree()-i} ---\n{sp.sstr(e)}\n\n")
print("wrote outputs/match_equations.txt  (", len(eqs), "equations )")

sols = sp.solve(eqs + [sp.numer(sp.cancel(b_lin))], [p, q, t, thi], dict=True)
print("\nsolutions:")
for s in sols:
    print("   ", {k: sp.radsimp(sp.simplify(v)) for k, v in s.items()})
