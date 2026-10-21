"""Numeric confirmation of the B-C projective equivalence, per the P0 rule
adopted at operator review #9: symbolic equality is established by simplifying
the difference to zero AND by a high-precision numeric check at several sample
points.

The symbolic half is in verify_s14.py (difference simplifies to exactly 0).
This script supplies the numeric half.
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 60

x, z = sp.symbols("x z")
r_B = (11 * z**4 + 4 * z**2 + 4 * z + 12) / (4 * z**4 * (z**2 + z + 3) ** 2)
A = 3 * x**2 + x + 1
P_c = sp.cancel(sp.diff(A, x) / A)
Q_c = sp.cancel(-(x**2) / A)
r_C = sp.cancel(sp.together(sp.diff(P_c, x) / 2 + P_c**2 / 4 - Q_c))

f_pull = sp.lambdify(x, r_B.subs(z, 1 / x) / x**4, "mpmath")
f_C = sp.lambdify(x, r_C, "mpmath")

print(f"dps = {mp.mp.dps}")
print("checking  r_B(1/x)/x^4  ==  r_C(x)  at sample points off the real axis\n")

pts = [mp.mpf("0.37"), mp.mpf("-1.9"), mp.mpf("2.5"),
       mp.mpc("0.4", "0.9"), mp.mpc("-0.7", "1.3"), mp.mpc("3.1", "-2.2"),
       mp.mpf("1") / 1000, mp.mpf(7)]

worst = mp.mpf(0)
for p in pts:
    a, b = f_pull(p), f_C(p)
    scale = max(abs(a), abs(b), mp.mpf(1))
    rel = abs(a - b) / scale
    worst = max(worst, rel)
    print(f"  x = {mp.nstr(p, 8):>22}   rel. residual = {mp.nstr(rel, 5)}")

print(f"\nworst relative residual over {len(pts)} points: {mp.nstr(worst, 5)}")
print(f"threshold 1e-50: {'PASS' if worst < mp.mpf('1e-50') else 'FAIL'}")

# The root correspondence, numerically as well as elementwise-symbolically.
print("\nroot correspondence under x = 1/z:")
rB = sp.solve(z**2 + z + 3, z)
rC = sp.solve(A, x)
for r in rB:
    img = complex(sp.N(1 / r, 50))
    near = min(rC, key=lambda c: abs(complex(sp.N(c, 50)) - img))
    d = abs(complex(sp.N(near, 50)) - img)
    print(f"  1/({r}) = {img:.15g}   nearest C root {near}   |diff| = {d:.3e}")
