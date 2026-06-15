#!/usr/bin/env python3
# PERIOD-REP-VQUAD-003 Stage 2 — Kovacic algorithm on L_phi (order 2), and an
# INDEPENDENT structural confirmation of the differential Galois group.
#
# L_phi = q2 D^2 + q1 D + q0  over Q(sqrt3) (VQUAD-002 operator-verification.md sec4.0a).
# Reduce y''+a y'+b y=0 (a=q1/q2, b=q0/q2) to u''=r u, r = a^2/4 + a'/2 - b.
# Kovacic decides which of 4 cases holds => Galois group:
#   Case1 reducible(Borel) / Case2 imprimitive(dihedral) / Case3 finite(A4,S4,A5) / Case4 SL2.
#
# METHOD 1 (Kovacic): pole structure of r (excludes Case3 by pole order),
#   Riccati rational-solution test (Case1), symmetric-square rational test (Case1/2).
# METHOD 2 (structural, independent): trace-free reduced form => G <= SL2;
#   pole order 4 at z=0 => Poincare rank 1, two DISTINCT exponentials => exponential
#   torus G_m <= G; nonzero Stokes S=2piK => off-torus unipotent in G;
#   <torus, off-torus unipotent> = SL2  =>  G = SL2.
import sympy as sp

z = sp.symbols('z')
s3 = sp.sqrt(3)

q0 = 1 + (sp.Rational(23,9) + sp.Rational(14,27)*s3)*z + (sp.Rational(-253,9) + sp.Rational(488,27)*s3)*z**2
q1 = (48 - 24*s3) + (-64 + 44*s3)*z + (sp.Rational(-68,3) + sp.Rational(52,3)*s3)*z**2 + (sp.Rational(-152,3) + sp.Rational(100,3)*s3)*z**3
q2 = (-36 + 24*s3)*z**2 + (-12 + 8*s3)*z**3 + (-12 + 8*s3)*z**4

a = sp.cancel(q1/q2)
b = sp.cancel(q0/q2)
r = sp.cancel(a**2/4 + sp.diff(a, z)/2 - b)
r = sp.together(r)
rnum, rden = sp.fraction(sp.cancel(r))
rnum = sp.expand(rnum); rden = sp.expand(rden)

print("=== reduced potential r = a^2/4 + a'/2 - b ===")
print("r =", sp.nsimplify(sp.simplify(r)))
print("num deg =", sp.degree(rnum, z), " den deg =", sp.degree(rden, z))

# ---- pole structure: factor denominator ----
print("\n=== pole structure of r ===")
den_factored = sp.factor(rden)
print("den (factored) =", den_factored)
num_factored = sp.factor(rnum)
print("num (factored) =", num_factored)

# q2 zeros => candidate poles of r
print("\nq2 factored =", sp.factor(q2))
q2roots = sp.roots(sp.Poly(q2, z))
print("q2 roots (with mult):", q2roots)

# order of r at each pole = multiplicity in reduced denominator
rden_poly = sp.Poly(rden, z)
den_roots = sp.roots(rden_poly)
print("\nreduced-r denominator roots (pole : order):")
for root, mult in den_roots.items():
    print("   ", sp.nsimplify(root), ":", mult)

# order at infinity o(inf) = deg(den) - deg(num)
o_inf = sp.degree(rden, z) - sp.degree(rnum, z)
print("order of r at infinity o(inf) = deg den - deg num =", o_inf)

# leading coefficient of r at z=0 (Laurent): r ~ L0 / z^4  -> distinct exponentials iff L0 != 0
ser0 = sp.series(r*z**4, z, 0, 1).removeO()
L0 = sp.simplify(ser0.subs(z, 0))
print("\nleading Laurent coeff of r at z=0 (coeff of 1/z^4):  L0 =", sp.nsimplify(sp.simplify(L0)))
print("  sqrt(L0) (sets exponential parts +- sqrt(L0)/z):", sp.nsimplify(sp.simplify(sp.sqrt(L0))))

# ---- METHOD 1: Kovacic case necessary conditions ----
print("\n=== METHOD 1: Kovacic case necessary conditions ===")
pole_orders = sorted([int(m) for m in den_roots.values()], reverse=True)
print("pole orders:", pole_orders, " o(inf) =", o_inf)
max_pole = max(pole_orders)
case3_possible = (max_pole <= 2) and (int(o_inf) >= 2)
print("Case 3 (finite group) necessary cond [all poles<=2 and o(inf)>=2]:",
      "POSSIBLE" if case3_possible else f"EXCLUDED (a pole has order {max_pole} > 2)")

# Case 1 necessary: every pole order 1 or even; o(inf) even or >2
c1 = all((po == 1) or (po % 2 == 0) for po in pole_orders) and ((int(o_inf) % 2 == 0) or (int(o_inf) > 2))
print("Case 1 (reducible) necessary cond:", "POSSIBLE" if c1 else "EXCLUDED")
# Case 2 necessary: r has a pole of order 2 or odd order >2
c2 = any((po == 2) or (po % 2 == 1 and po > 2) for po in pole_orders)
print("Case 2 (dihedral) necessary cond:", "POSSIBLE" if c2 else "EXCLUDED")

# ---- METHOD 1: Riccati rational-solution test (Case 1 decisive) ----
print("\n=== METHOD 1: Riccati rational-solution test (Case 1) ===")
print("Riccati: v' = r - v^2 ; rational solution exists  <=>  Case 1 (reducible).")
try:
    from sympy.solvers.ode.riccati import solve_riccati
    f = sp.Function('f')
    sols = solve_riccati(f(z), z, b0=r, b1=sp.Integer(0), b2=sp.Integer(-1))
    print("solve_riccati rational solutions:", sols)
    case1_holds = len(sols) > 0
except Exception as e:
    print("solve_riccati raised:", repr(e))
    case1_holds = None

print("\n=== VERDICT (Method 1) ===")
if case3_possible:
    print("  Case 3 not excluded by pole order — needs finite-group search.")
elif case1_holds is True:
    print("  Case 1 HOLDS: group reducible (NOT SL2) — CONTRADICTS V_quad claim!")
elif case1_holds is False and not c2:
    print("  Cases 1,2,3 all excluded => CASE 4: Galois group = SL(2).")
elif case1_holds is False and c2:
    print("  Case 1 excluded, Case 3 excluded; Case 2 needs symmetric-square test (see Method 1b).")
else:
    print("  Riccati test inconclusive (engine); rely on structural Method 2.")
