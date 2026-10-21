"""CT-S16 step 3(a) - locate System C in the vdPS (0,0,1) family, exact.

The earlier symbolic attempts stalled because the scalar reduction was built as
a quotient of large products.  Reducing it by hand first makes it trivial.

With Y' = -(1/D) A Y, A = [[a,b],[c,-a]], D = z(z-1), and y_1 as cyclic vector:

    y_1'' + P y_1' + Q y_1 = 0,
    P = D'/D - b'/b,
    Q = a'/D - a b'/(D b) - (a^2 + b c)/D^2 .

System C's r_z has no apparent singularity, so b must be constant (b' = 0),
whence P = D'/D and, since P^2/4 + P'/2 = -1/(4 D^2) identically,

    R = (a^2 + b_0 c - a' D - 1/4) / D^2 .

Both R and r_z then have the same denominator D^2 = z^2(z-1)^2, so matching is
just equality of two quartics.  Every step below is checked symbolically.

Parameters carried in: theta_0 = theta_1 = 0, established from the double-pole
coefficient -1/4 via the dictionary verified in probe_family.py.
"""
import sympy as sp

z, p, q, t, thi = sp.symbols("z p q t theta_inf")

# ---- family objects with theta_0 = theta_1 = 0 -----------------------------
a = (p + sp.Rational(1, 2) * (-2 * q * t + t - thi) * (z - q)
     - sp.Rational(1, 2) * t * (z - q) ** 2)
c = -(z - q) / (q - 1)
U = p + sp.Rational(1, 2) * (q - 1) * q * t
V = p + sp.Rational(1, 2) * ((q - 1) * q * t + q * thi)
b1 = sp.cancel(-(U**2 - (q - 1) * q * thi**2 / 4) / q)      # coefficient of z
b0 = sp.cancel(-(q - 1) * V**2 / q)                          # constant term

# sanity: rebuild b and confirm it equals b1*z + b0
b_full = (-(z * (U**2 + (q - 1) * (-q * thi**2 / 4))) / q
          - ((q - 1) * (p + sp.Rational(1, 2) * ((q - 1) * q * t + q * thi))
             * (p + sp.Rational(1, 2) * ((q - 1) * q * t + q * thi))) / q)
print("b = b1*z + b0 :", sp.simplify(sp.expand(b_full - (b1 * z + b0))) == 0)

# ---- verify the closed form for R on a random draw -------------------------
D = z * (z - 1)


def R_general(aa, bb, cc):
    P = sp.diff(D, z) / D - sp.diff(bb, z) / bb
    Q = sp.diff(aa, z) / D - aa * sp.diff(bb, z) / (D * bb) - (aa**2 + bb * cc) / D**2
    return sp.cancel(sp.together(P**2 / 4 + sp.diff(P, z) / 2 - Q))


draw = {p: sp.Rational(2, 3), q: sp.Rational(5, 7), t: sp.Rational(3, 2), thi: sp.Rational(2, 7)}
a_d, b_d, c_d = a.subs(draw), (b1 * z + b0).subs(draw), c.subs(draw)
R_d = R_general(a_d, b_d, c_d)
R_closed_d = sp.cancel((a_d**2 + b_d * c_d - sp.diff(a_d, z) * D
                        - sp.Rational(1, 4) - D * sp.diff(b_d, z) * 0) / D**2)
print("closed form valid when b is NOT constant?",
      sp.simplify(sp.cancel(R_d - R_closed_d)) == 0, "(expected False)")

# with b constant (b1 = 0) the closed form must hold; test on a draw satisfying it
sol_b1 = sp.solve(sp.numer(sp.cancel(b1)), p)
print("\nb1 = 0  =>  p =", [sp.simplify(s) for s in sol_b1])
draw2 = {q: sp.Rational(5, 7), t: sp.Rational(3, 2), thi: sp.Rational(2, 7)}
p_val = sp.simplify(sol_b1[0].subs(draw2))
draw2[p] = p_val
a_d2 = a.subs(draw2)
b_d2 = sp.simplify((b1 * z + b0).subs(draw2))
c_d2 = c.subs(draw2)
print("b constant on this draw?", sp.simplify(sp.diff(b_d2, z)) == 0)
R_d2 = R_general(a_d2, b_d2, c_d2)
R_cl2 = sp.cancel((a_d2**2 + b_d2 * c_d2 - sp.diff(a_d2, z) * D - sp.Rational(1, 4)) / D**2)
print("closed form valid when b IS constant?", sp.simplify(sp.cancel(R_d2 - R_cl2)) == 0)

# ---- System C's r_z --------------------------------------------------------
x = sp.Symbol("x")
s_p = sp.Rational(-1, 6) + sp.sqrt(11) * sp.I / 6
delta = -sp.sqrt(11) * sp.I / 3
A_c, C_c = 3 * x**2 + x + 1, -x**2
pc, qc = sp.diff(A_c, x) / A_c, C_c / A_c
r_x = sp.cancel(pc**2 / 4 + sp.diff(pc, x) / 2 - qc)
r_z = sp.cancel(sp.expand(delta**2 * r_x.subs(x, s_p + delta * z)))
Nz, Dz = sp.fraction(r_z)
print("\nr_z denominator:", sp.factor(Dz))
Nz_scaled = sp.expand(sp.cancel(Nz * D**2 / Dz))
print("r_z numerator over D^2:", sp.expand(Nz_scaled))

# ---- match -----------------------------------------------------------------
lhs = sp.expand(a**2 + b0 * c - sp.diff(a, z) * D - sp.Rational(1, 4))
E = sp.expand(lhs - Nz_scaled)
poly = sp.Poly(E, z)
eqs = [sp.expand(co) for co in poly.all_coeffs()]
print(f"\nmatching gives {len(eqs)} coefficient equations (degree {poly.degree()})")
eqs.append(sp.expand(sp.numer(sp.cancel(b1))))
print("plus the no-apparent-singularity condition b1 = 0")

sols = sp.solve(eqs, [p, q, t, thi], dict=True)
print("\nsolutions:", len(sols))
for s in sols:
    print("  p       =", sp.radsimp(sp.simplify(s.get(p))))
    print("  q       =", sp.radsimp(sp.simplify(s.get(q))))
    print("  t       =", sp.radsimp(sp.simplify(s.get(t))))
    print("  theta_i =", sp.radsimp(sp.simplify(s.get(thi))))
    print()

with open("outputs/pq_solution.txt", "w", encoding="utf-8") as f:
    for s in sols:
        for k in (p, q, t, thi):
            f.write(f"{k} = {sp.sstr(sp.simplify(s.get(k)))}\n")
        f.write("\n")
print("wrote outputs/pq_solution.txt")
