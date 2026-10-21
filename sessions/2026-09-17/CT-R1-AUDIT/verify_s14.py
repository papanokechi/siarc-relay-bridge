"""Independent re-check of CT-S14-COLDREAD-B's load-bearing computations.

Written without reading CT-S14's scripts; only its REPORT.md conclusions are
being tested. Each item is checked from the primary data (the printed normal
form of object B, and the companion's printed polynomial coefficients).
"""
import sympy as sp

x, z = sp.symbols("x z")

# --- primary data -----------------------------------------------------------
# Object B: the source paper's printed normal form y'' = r_B(z) y.
r_B = (11 * z**4 + 4 * z**2 + 4 * z + 12) / (4 * z**4 * (z**2 + z + 3) ** 2)

# Companion v1.2's printed ODE  A W'' + B W' + C W = 0  (read from page image).
A = 3 * x**2 + x + 1
B = 6 * x + 1
C = -(x**2)

print("=== 0. sanity: B = A' (the exactness identity) ===")
print("  A' =", sp.expand(sp.diff(A, x)), " B =", sp.expand(B),
      " equal:", sp.simplify(sp.diff(A, x) - B) == 0)

# --- 1. inversion of B's normal form ---------------------------------------
# For u'' = r(z) u with z = 1/x one gets u'' + (2/x)u' - r(1/x)/x^4 u = 0,
# whose trace-free normal potential is exactly r(1/x)/x^4 (the 2/x terms cancel).
print("\n=== 1. pullback of B's normal form under z = 1/x ===")
P_pull = sp.Rational(2, 1) / x
Q_pull = -r_B.subs(z, 1 / x) / x**4
r_pull = sp.simplify(sp.diff(P_pull, x) / 2 + P_pull**2 / 4 - Q_pull)
r_pull = sp.cancel(sp.together(r_pull))
print("  r_B(1/x)/x^4 =", sp.simplify(sp.cancel(r_B.subs(z, 1 / x) / x**4)))
print("  normal potential of the pullback =", r_pull)
print("  the 2/x first-order term contributes nothing:",
      sp.simplify(sp.diff(P_pull, x) / 2 + P_pull**2 / 4) == 0)

# --- 2. companion's own trace-free normal potential --------------------------
print("\n=== 2. companion's trace-free normal potential ===")
P_c = sp.cancel(B / A)
Q_c = sp.cancel(C / A)
r_C = sp.cancel(sp.together(sp.diff(P_c, x) / 2 + P_c**2 / 4 - Q_c))
print("  r_C(x) =", r_C)

# --- 3. THE load-bearing identity -------------------------------------------
print("\n=== 3. do B (inverted) and C share a trace-free normal form? ===")
diff = sp.simplify(sp.cancel(r_pull - r_C))
print("  r_pull - r_C =", diff, " -> IDENTICAL:", diff == 0)

# --- 4. is x = 0 (i.e. z = infinity) ordinary? ------------------------------
print("\n=== 4. behaviour at z = infinity (x = 0) ===")
print("  r at x=0 =", sp.simplify(r_pull.subs(x, 0)), " (finite => ordinary point)")
print("  series:", sp.series(r_pull, x, 0, 3))

# --- 5. singular points and their correspondence ----------------------------
print("\n=== 5. finite singular points ===")
roots_B = sp.solve(sp.Eq(z**2 + z + 3, 0), z)
roots_C = sp.solve(sp.Eq(A, 0), x)
print("  B's finite regular singular points (roots of z^2+z+3):", roots_B)
print("  C's finite singular points (roots of A):", roots_C)
print("  image of B's roots under x = 1/z:",
      sorted([sp.nsimplify(sp.simplify(1 / r)) for r in roots_B], key=str))
print("  match:",
      {sp.simplify(1 / r) for r in roots_B} == {sp.simplify(r) for r in roots_C})

# --- 6. exponents at those points, in each presentation ---------------------
print("\n=== 6. local exponents at a finite singular point ===")
beta = roots_C[0]
lam = sp.symbols("lam")
# (a) in the trace-free normal form  U'' = r U
c2 = sp.simplify(sp.limit((x - beta) ** 2 * (-r_C), x, beta))
ind_nf = sp.expand(lam * (lam - 1) + c2)
print("  normal form: lim (x-b)^2 * (-r) =", sp.nsimplify(c2))
print("    indicial =", ind_nf, " roots =", sp.solve(ind_nf, lam))
# (b) in the companion's printed scalar basis  W'' + P W' + Q W = 0
p0 = sp.simplify(sp.limit((x - beta) * P_c, x, beta))
q0 = sp.simplify(sp.limit((x - beta) ** 2 * Q_c, x, beta))
ind_sc = sp.expand(lam * (lam - 1) + p0 * lam + q0)
print("  printed basis: residue(P) =", sp.nsimplify(p0), " lim (x-b)^2 Q =", sp.nsimplify(q0))
print("    indicial =", ind_sc, " roots =", sp.solve(ind_sc, lam))

# --- 7. the twist, and what it does to the trace ----------------------------
print("\n=== 7. the rank-1 twist relating the two presentations ===")
h = A ** sp.Rational(-1, 2)
print("  twist multiplier h =", h)
print("  trace change 2*dlog(h) =", sp.simplify(2 * sp.diff(sp.log(h), x)))
print("  -dlog(A)             =", sp.simplify(-sp.diff(sp.log(A), x)))
print("  nonzero => trace is altered:",
      sp.simplify(2 * sp.diff(sp.log(h), x)) != 0)
print("  companion scalar trace (= P, up to sign convention):", P_c)
print("  B's normal form trace (trace-free by construction): 0")

# --- 8. does the twist restore to trace-free? -------------------------------
print("\n=== 8. re-normalising the twisted operator ===")
print("  U = A^(1/2) W recovers U'' = r U with r =", r_C)
print("  so the row is read off the trace-free normal form, which inversion alone reaches.")
