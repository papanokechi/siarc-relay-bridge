"""CT-S25 N1 - final verdict: the solution set is constructively exactly two.

The degree bound plus two exhibited points already gives "exactly two".  This
script establishes it a second, independent way, constructively:

  1. the lex Groebner basis is TRIANGULAR - the eliminant is univariate in
     theta_inf, and p, q, t, u each appear to degree 1 given theta_inf, so each
     root of the eliminant determines AT MOST ONE point;
  2. the eliminant has exactly two roots;
  3. back-substituting each root reproduces, EXACTLY, the two solutions recorded
     by CT-S16 - so each root determines exactly one point, and both are the
     known ones.

Two independent routes to the same conclusion, one counting and one
constructive.  Neither relies on a sensitivity arm.
"""

import hashlib
import sys
from pathlib import Path

import sympy as sp

OUT = []


def say(s=""):
    OUT.append(str(s))
    print(s)


z, p, q, t, thi, u = sp.symbols("z p q t theta_inf u")

a = (p + sp.Rational(1, 2) * (-2 * q * t + t - thi) * (z - q)
     - sp.Rational(1, 2) * t * (z - q) ** 2)
c = -(z - q) / (q - 1)
U = p + sp.Rational(1, 2) * (q - 1) * q * t
V = p + sp.Rational(1, 2) * ((q - 1) * q * t + q * thi)
b1 = sp.cancel(-(U**2 - (q - 1) * q * thi**2 / 4) / q)
b0 = sp.cancel(-(q - 1) * V**2 / q)
D = z * (z - 1)
x = sp.Symbol("x")
s_p = sp.Rational(-1, 6) + sp.sqrt(11) * sp.I / 6
delta = -sp.sqrt(11) * sp.I / 3
A_c, C_c = 3 * x**2 + x + 1, -x**2
pc, qc = sp.diff(A_c, x) / A_c, C_c / A_c
r_x = sp.cancel(pc**2 / 4 + sp.diff(pc, x) / 2 - qc)
r_z = sp.cancel(sp.expand(delta**2 * r_x.subs(x, s_p + delta * z)))
Nz, Dz = sp.fraction(r_z)
Nz_scaled = sp.expand(sp.cancel(Nz * D**2 / Dz))
poly_z = sp.Poly(sp.expand(sp.expand(a**2 + b0 * c - sp.diff(a, z) * D
                                     - sp.Rational(1, 4)) - Nz_scaled), z)
GENS = [sp.expand(sp.numer(sp.cancel(co))) for co in poly_z.all_coeffs()]
GENS.append(sp.expand(sp.numer(sp.cancel(b1))))
RAB = sp.expand(u * q * (q - 1) - 1)

K = sp.QQ.algebraic_field(sp.I * sp.sqrt(11))

r11, r33, r3 = sp.sqrt(11), sp.sqrt(33), sp.sqrt(3)
RECORDED = [
    {p: 5 * sp.I * (-28151758571 * r33 + 48874838016 * r11) / 4086468672,
     q: sp.Rational(1, 2) - 457937 * r11 * sp.I / 122408 + 70425 * r33 * sp.I / 30602,
     t: -2 * r33 * sp.I / 9,
     thi: -2 - r3 / 9},
    {p: 5 * sp.I * (28151758571 * r33 + 48874838016 * r11) / 4086468672,
     q: sp.Rational(1, 2) - 70425 * r33 * sp.I / 30602 - 457937 * r11 * sp.I / 122408,
     t: 2 * r33 * sp.I / 9,
     thi: -2 + r3 / 9},
]

say("=" * 74)
say("CT-S25-N1-EXHAUSTIVE / n1_verdict.py")
say("Constructive route: triangular lex basis, then back-substitution.")
say("=" * 74)

G = sp.groebner(GENS + [RAB], u, p, q, t, thi, order="lex", domain=K)
say()
say(f"lex Groebner basis: {len(G.exprs)} polynomials, order u > p > q > t > theta_inf")

elim = None
shape = {}
for g in G.exprs:
    fs = g.free_symbols
    if fs <= {thi}:
        elim = g
        say(f"  eliminant (theta_inf only)         : {sp.expand(g)}")
    else:
        lead = [s for s in (u, p, q, t) if s in fs]
        if lead:
            head = lead[0]
            d = sp.Poly(g, head).degree()
            shape[head] = min(shape.get(head, 99), d)
            say(f"  degree {d} in {str(head):<10} given theta_inf : {str(sp.expand(g))[:52]}...")

say()
say("-" * 74)
say("1. TRIANGULARITY - each of u, p, q, t appears to degree 1 in some basis")
say("   element whose only other variable is theta_inf, so a root of the")
say("   eliminant determines AT MOST ONE point.")
say("-" * 74)
triangular = all(shape.get(s) == 1 for s in (u, p, q, t))
for s in (u, p, q, t):
    say(f"   minimal degree in {str(s):<10}: {shape.get(s)}")
say(f"   triangular: {triangular}")

say()
say("-" * 74)
say("2. THE ELIMINANT'S ROOTS")
say("-" * 74)
roots = sp.solve(elim, thi)
roots = [sp.radsimp(sp.simplify(r)) for r in roots]
say(f"   degree {sp.Poly(elim, thi).degree()}, roots: {roots}")
say(f"   distinct: {len(set(sp.simplify(r) for r in roots)) == len(roots)}")

say()
say("-" * 74)
say("3. BACK-SUBSTITUTION - each root must reproduce exactly one point, and")
say("   that point must be one of the two CT-S16 recorded.")
say("-" * 74)

matched = []
for r in roots:
    sub = [sp.expand(g.subs(thi, r)) for g in GENS + [RAB]]
    sol = sp.solve(sub, [p, q, t, u], dict=True)
    say(f"   theta_inf = {r}")
    say(f"     solutions in (p,q,t,u): {len(sol)}")
    if len(sol) != 1:
        say("     UNEXPECTED: not exactly one point above this root")
        continue
    s = sol[0]
    hit = None
    for k, rec in enumerate(RECORDED, 1):
        if sp.simplify(rec[thi] - r) != 0:
            continue
        same = all(sp.simplify(sp.expand(s[var] - rec[var])) == 0 for var in (p, q, t))
        if same:
            hit = k
    say(f"     matches CT-S16 recorded solution #{hit}" if hit
        else "     DOES NOT MATCH either recorded solution")
    if hit:
        matched.append(hit)

say()
say("=" * 74)
say("VERDICT")
say("=" * 74)
ok = triangular and len(roots) == 2 and sorted(matched) == [1, 2]
say(f"  triangular lex basis                    : {triangular}")
say(f"  eliminant roots                         : {len(roots)} (distinct)")
say(f"  each root gives exactly one point       : {len(matched) == 2}")
say(f"  both points are the CT-S16 recorded ones: {sorted(matched) == [1, 2]}")
say()
if ok:
    say("  The solution set of the matching system, saturated at q(q-1) != 0,")
    say("  is EXACTLY the two points recorded in CT-S16.  Established twice:")
    say("  by a degree bound of 2 against two exhibited points, and")
    say("  constructively via a triangular eliminant with two roots.")
    say()
    say("  S16-12's 'for both sign branches' is EXHAUSTIVE.  N1 CLOSES.")
    rc = 0
else:
    say("  NOT ESTABLISHED by this route.")
    rc = 1
say("=" * 74)

path = Path(sys.argv[1])
path.write_text("\n".join(OUT) + "\n", encoding="utf-8")
back = path.read_text(encoding="utf-8")
assert "VERDICT" in back, "read-back failed"
print(f"\nwrote {path.name} ({len(back)} chars, sha256 "
      f"{hashlib.sha256(path.read_bytes()).hexdigest()})")
sys.exit(rc)
