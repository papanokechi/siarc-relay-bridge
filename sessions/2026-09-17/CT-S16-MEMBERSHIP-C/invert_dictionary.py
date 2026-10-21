"""CT-S16 - invert the vdPS dictionary for System C and locate its point (p,q).

Dictionary established by probe_family.py on three independent exact draws:

    double-pole coeff of R at z=0 :  (theta_0^2 - 1)/4     [3/3 draws]
    double-pole coeff of R at z=1 :  (theta_1^2 - 1)/4     [3/3 draws]
    R(infinity)                   :  t^2/4                 [3/3 draws]
    1/z coefficient at infinity   :  t*(theta_inf + 1)/2    <- the +1 is the
        scalar-reduction shift; the naive t*theta_inf/2 failed all three draws
        and the corrected form is re-tested here on the same draws.

Those draws also serve as the step-2 vacuity pre-check for H-a: they carry
theta_0 != 0 and the observable reports it, so the test is not vacuous.
"""
import sympy as sp

z = sp.Symbol("z")
p, q = sp.symbols("p q")


def family(pv, qv, tv, t0, t1, ti):
    a = (pv + sp.Rational(1, 2) * (-2 * qv * tv + tv - ti) * (z - qv)
         - sp.Rational(1, 2) * tv * (z - qv) ** 2)
    c = -(z - qv) / (qv - 1)
    b = (-(z * ((pv + sp.Rational(1, 2) * (qv - 1) * qv * tv) ** 2 - t1**2 / 4
                + (qv - 1) * (t0**2 / 4 - t1**2 / 4 - qv * ti**2 / 4))) / qv
         - ((qv - 1)
            * (pv + sp.Rational(1, 2) * ((qv - 1) * qv * tv - t0 + qv * ti))
            * (pv + sp.Rational(1, 2) * ((qv - 1) * qv * tv + t0 + qv * ti))) / qv)
    return sp.cancel(a), sp.cancel(b), sp.cancel(c)


def normal_potential(a, b, c):
    D = z * (z - 1)
    bp, ap, Dp = sp.diff(b, z), sp.diff(a, z), sp.diff(D, z)
    c2 = sp.cancel(D * (-D) * b)
    c1 = sp.cancel(D * ((-Dp - a) * b + D * bp) + a * b * D)
    c0 = sp.cancel(D * (-ap * b + a * bp) + b**2 * c + a**2 * b)
    P, Q = sp.cancel(c1 / c2), sp.cancel(c0 / c2)
    return sp.cancel(sp.together(P**2 / 4 + sp.diff(P, z) / 2 - Q))


# ---- re-test the corrected infinity entry on the same three draws ----------
DRAWS = [
    (sp.Rational(2, 3), sp.Rational(5, 7), sp.Rational(3, 2), sp.Rational(1, 5), sp.Rational(4, 3), sp.Rational(2, 7)),
    (sp.Rational(-1, 2), sp.Rational(3, 4), sp.Rational(-5, 3), sp.Rational(7, 2), sp.Rational(-1, 3), sp.Rational(5, 6)),
    (sp.Integer(3), sp.Rational(-2, 5), sp.Rational(1, 4), sp.Rational(-2, 3), sp.Rational(1, 2), sp.Rational(-3, 4)),
]
w = sp.Symbol("w")
print("re-test of  1/z coefficient == t*(theta_inf + 1)/2 :")
for i, (pv, qv, tv, t0, t1, ti) in enumerate(DRAWS, 1):
    R = normal_potential(*family(pv, qv, tv, t0, t1, ti))
    ser = sp.series(R.subs(z, 1 / w), w, 0, 2).removeO()
    e1 = sp.cancel(sp.diff(sp.expand(ser), w).subs(w, 0))
    ok = sp.simplify(e1 - tv * (ti + 1) / 2) == 0
    print(f"   draw {i}: e1={e1}  predicted {tv*(ti+1)/2}  ok={ok}")
    assert ok

# ---- System C's invariants (from systemC_invariants.py) --------------------
c0_inf = sp.Rational(-11, 27)          # R(infinity)
c1_inf = sp.sqrt(11) * sp.I / 27       # 1/z coefficient
dpole = sp.Rational(-1, 4)             # double-pole coeff at z=0 and z=1

th0 = sp.solve(sp.Eq((sp.Symbol("T") ** 2 - 1) / 4, dpole), sp.Symbol("T"))
print("\nSystem C: theta_0 and theta_1 from double-pole coeff -1/4 ->", th0)

t_branches = sp.solve(sp.Eq(sp.Symbol("T") ** 2 / 4, c0_inf), sp.Symbol("T"))
print("t branches:", t_branches)
for tv in t_branches:
    ti = sp.radsimp(sp.simplify(2 * c1_inf / tv - 1))
    print(f"   t = {tv}  ->  theta_inf = 2*c1/t - 1 = {sp.nsimplify(sp.radsimp(ti))}")

# ---- solve for (p,q) on the branch t = -2i sqrt(33)/9 ----------------------
tv = sp.simplify(-2 * sp.I * sp.sqrt(33) / 9)
ti = sp.simplify(-1 - sp.sqrt(3) / 9)
print(f"\nworking branch: t = {tv},  theta_inf = {ti},  theta_0 = theta_1 = 0")

a, b, c = family(p, q, tv, sp.Integer(0), sp.Integer(0), ti)
b_poly = sp.Poly(sp.expand(sp.numer(sp.cancel(b))), z)
b_lin = sp.expand(b_poly.all_coeffs()[0]) if b_poly.degree() >= 1 else sp.Integer(0)
print("\ncondition 'no apparent singularity'  (coeff of z in b) = 0:")
print("   ", sp.factor(b_lin), "= 0")

# System C's r_z
x = sp.Symbol("x")
s_p = sp.Rational(-1, 6) + sp.sqrt(11) * sp.I / 6
delta = -sp.sqrt(11) * sp.I / 3
A_c, C_c = 3 * x**2 + x + 1, -x**2
pc, qc = sp.diff(A_c, x) / A_c, C_c / A_c
r_x = sp.cancel(pc**2 / 4 + sp.diff(pc, x) / 2 - qc)
r_z = sp.cancel(sp.expand(delta**2 * r_x.subs(x, s_p + delta * z)))

# residue of r_z at z = 0 (simple-pole coefficient)
res_target = sp.cancel(sp.diff(sp.cancel(z**2 * r_z), z).subs(z, 0))
print("\nSystem C: simple-pole coefficient of r_z at z=0 =", sp.radsimp(res_target))

R = normal_potential(a, b, c)
res_family = sp.cancel(sp.diff(sp.cancel(z**2 * R), z).subs(z, 0))
print("family: same coefficient computed as a function of (p,q).")

eq1 = sp.numer(sp.cancel(b_lin))
eq2 = sp.numer(sp.cancel(sp.together(res_family - res_target)))
print("\nsolving the two conditions for (p,q) ...")
sols = sp.solve([eq1, eq2], [p, q], dict=True)
print("candidate solutions:", len(sols))
for s in sols:
    print("   p =", sp.radsimp(sp.simplify(s[p])), "   q =", sp.radsimp(sp.simplify(s[q])))

with open("outputs/pq_candidates.txt", "w", encoding="utf-8") as f:
    for s in sols:
        f.write(f"p = {sp.sstr(sp.simplify(s[p]))}\nq = {sp.sstr(sp.simplify(s[q]))}\n\n")
print("wrote outputs/pq_candidates.txt")
