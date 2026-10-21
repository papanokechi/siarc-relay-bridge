"""CT-S25 N1 - is the matching system's solution set exactly two points?

See PREREG.md. The observable is the degree of the quotient ring; the falsifiers
F1-F4 and the vacuity arms V1-V4 are fixed there and are not adjusted here.

Structure, in the order PREREG requires:
  step 1  rebuild the generators (transcribed from locate_final.py)
  step 2  V1/V2 - the recorded solutions satisfy them; a perturbation does not
  step 3  the saturated Groebner computation  (the result)
  step 4  V3 - drop b1 = 0; the degree must move
  step 5  V4 - drop the saturation; record whether it did work
  step 6  the eliminant, against the prediction registered in PREREG
"""

import hashlib
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
SESSION = HERE.parent

OUT = []


def say(s=""):
    OUT.append(str(s))
    print(s)


z, p, q, t, thi, u = sp.symbols("z p q t theta_inf u")

# ---------------------------------------------------------------- step 1 ----
# Transcribed from CT-S16-MEMBERSHIP-C/locate_final.py (copy held in refs/).
# theta_0 = theta_1 = 0.
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

lhs = sp.expand(a**2 + b0 * c - sp.diff(a, z) * D - sp.Rational(1, 4))
E = sp.expand(lhs - Nz_scaled)
poly_z = sp.Poly(E, z)
COEFF_EQS = [sp.expand(sp.numer(sp.cancel(co))) for co in poly_z.all_coeffs()]
B1_EQ = sp.expand(sp.numer(sp.cancel(b1)))

GENS = COEFF_EQS + [B1_EQ]

say("=" * 74)
say("CT-S25-N1-EXHAUSTIVE / n1_exhaustive.py")
say("=" * 74)
say(f"coefficient equations from matching : {len(COEFF_EQS)} (z-degree {poly_z.degree()})")
say(f"plus the no-apparent-singularity condition b1 = 0 -> {len(GENS)} generators")
say(f"unknowns: p, q, t, theta_inf")

# ---------------------------------------------------------------- step 2 ----
# V1 / V2, run BEFORE the result is consulted.
r11, r33, r3 = sp.sqrt(11), sp.sqrt(33), sp.sqrt(3)
SOLS = [
    {p: 5 * sp.I * (-28151758571 * r33 + 48874838016 * r11) / 4086468672,
     q: sp.Rational(1, 2) - 457937 * r11 * sp.I / 122408 + 70425 * r33 * sp.I / 30602,
     t: -2 * r33 * sp.I / 9,
     thi: -2 - r3 / 9},
    {p: 5 * sp.I * (28151758571 * r33 + 48874838016 * r11) / 4086468672,
     q: sp.Rational(1, 2) - 70425 * r33 * sp.I / 30602 - 457937 * r11 * sp.I / 122408,
     t: 2 * r33 * sp.I / 9,
     thi: -2 + r3 / 9},
]

say()
say("-" * 74)
say("V1 (positive control) - the two recorded solutions must satisfy EVERY")
say("generator exactly.  A mistranscribed generator would fail here and would")
say("otherwise have produced a confident and entirely false degree.")
say("-" * 74)
v1_ok = True
for k, s in enumerate(SOLS, 1):
    vals = []
    for j, g in enumerate(GENS):
        r = sp.simplify(sp.expand(g.subs(s)))
        vals.append(r)
        if r != 0:
            v1_ok = False
            say(f"  solution {k}, generator {j}: NONZERO -> {r}")
    say(f"  solution {k}: all {len(GENS)} generators vanish exactly: {all(v == 0 for v in vals)}")
    # q(q-1) != 0 must hold at the recorded points, or saturation would delete them
    sat = sp.simplify(s[q] * (s[q] - 1))
    say(f"    q(q-1) at this point = {sp.nsimplify(sp.N(sat, 30))}  (nonzero: {sp.simplify(sat) != 0})")
say(f"V1: {'PASS' if v1_ok else 'FAIL'}")

say()
say("-" * 74)
say("V2 (negative control) - a perturbed point must NOT satisfy the generators.")
say("Guards against a generator set that is identically zero.")
say("-" * 74)
pert = dict(SOLS[0])
pert[thi] = pert[thi] + sp.Rational(1, 1000)
nz = [j for j, g in enumerate(GENS) if sp.simplify(sp.expand(g.subs(pert))) != 0]
say(f"  perturbed theta_inf by 1/1000: generators that are now NONZERO: {nz}")
v2_ok = len(nz) > 0
say(f"V2: {'PASS' if v2_ok else 'FAIL - generators vanish identically'}")

if not (v1_ok and v2_ok):
    say()
    say("HALT: vacuity pre-check failed.  Per PREREG F4 this indicts the")
    say("construction, not the claim.  No degree is reported.")
    Path(sys.argv[1]).write_text("\n".join(OUT) + "\n", encoding="utf-8")
    sys.exit(2)

# ---------------------------------------------------------------- step 3 ----
K = sp.QQ.algebraic_field(sp.I * sp.sqrt(11))
say()
say("-" * 74)
say(f"Groebner computation over K = Q(i*sqrt(11))   domain: {K}")
say("Saturated at q(q-1) != 0 by the Rabinowitsch variable u: u*q*(q-1) - 1 = 0.")
say("-" * 74)

RAB = sp.expand(u * q * (q - 1) - 1)


def degree_of(gens, variables, label, with_basis=False):
    """Return (dim0, degree, groebner) for the ideal, or (None, None, None)."""
    t0 = time.time()
    try:
        G = sp.groebner(gens, *variables, order="grevlex", domain=K)
    except Exception as exc:  # noqa: BLE001
        say(f"  [{label}] groebner raised {type(exc).__name__}: {exc}")
        return None, None, None
    dt = time.time() - t0
    zd = G.is_zero_dimensional
    say(f"  [{label}] basis of {len(G.exprs)} polys in {dt:.1f}s; zero-dimensional: {zd}")
    if not zd:
        return False, None, G
    # count standard monomials = monomials not divisible by any leading monomial
    lead = [sp.Poly(g, *variables, domain=K).LM(order="grevlex") for g in G.exprs]
    lead_exp = [tuple(m.exponents) for m in lead]
    bounds = []
    for i in range(len(variables)):
        pure = [e[i] for e in lead_exp if all(e[j] == 0 for j in range(len(variables)) if j != i)]
        if not pure:
            say(f"  [{label}] no pure power of {variables[i]} in the leading ideal")
            return False, None, G
        bounds.append(min(pure))
    import itertools
    count = 0
    for expo in itertools.product(*[range(b) for b in bounds]):
        if not any(all(expo[i] >= le[i] for i in range(len(variables))) for le in lead_exp):
            count += 1
    say(f"  [{label}] standard monomials (degree of the quotient ring): {count}")
    return True, count, G


VARS_SAT = (p, q, t, thi, u)
zd_main, deg_main, G_main = degree_of(GENS + [RAB], VARS_SAT, "MAIN saturated")

# ---------------------------------------------------------------- step 4 ----
say()
say("-" * 74)
say("V3 (sensitivity) - drop the b1 = 0 equation.  The degree MUST move.")
say("A degree that does not move would show the observable cannot see that")
say("equation, and the whole computation would be void.")
say("-" * 74)
zd_v3, deg_v3, _ = degree_of(COEFF_EQS + [RAB], VARS_SAT, "V3 without b1=0")
if zd_v3 is False:
    say("  [V3] not zero-dimensional -> the observable DID move (from a finite")
    say("       count to a positive-dimensional family).")
v3_moved = (zd_v3 is not True) or (deg_v3 != deg_main)
say(f"V3: {'PASS (observable moved)' if v3_moved else 'FAIL - observable is blind to b1=0'}")

# ---------------------------------------------------------------- step 5 ----
say()
say("-" * 74)
say("V4 (does saturation do work?) - same ideal without the Rabinowitsch")
say("variable.  Recorded as a finding either way, not used as a gate.")
say("-" * 74)
zd_v4, deg_v4, _ = degree_of(GENS, (p, q, t, thi), "V4 unsaturated")

# ---------------------------------------------------------------- step 6 ----
say()
say("-" * 74)
say("The eliminant in theta_inf, against the prediction registered in PREREG.")
say("-" * 74)
elim = None
try:
    t0 = time.time()
    Gl = sp.groebner(GENS + [RAB], u, p, q, t, thi, order="lex", domain=K)
    say(f"  lex basis of {len(Gl.exprs)} polys in {time.time() - t0:.1f}s")
    for g in Gl.exprs:
        if g.free_symbols <= {thi}:
            elim = sp.Poly(g, thi)
            break
except Exception as exc:  # noqa: BLE001
    say(f"  lex groebner raised {type(exc).__name__}: {exc}")

PREDICTED = sp.Poly(27 * thi**2 + 108 * thi + 107, thi)
if elim is not None:
    say(f"  eliminant: {sp.expand(elim.as_expr())}")
    say(f"  degree in theta_inf: {elim.degree()}")
    monic_e = sp.Poly(sp.expand(elim.as_expr() / elim.LC()), thi)
    monic_p = sp.Poly(sp.expand(PREDICTED.as_expr() / PREDICTED.LC()), thi)
    matches = sp.simplify(monic_e.as_expr() - monic_p.as_expr()) == 0
    say(f"  predicted (monic): {monic_p.as_expr()}")
    say(f"  matches prediction registered before computing: {matches}")
    roots = sp.solve(elim.as_expr(), thi)
    say(f"  roots: {[sp.radsimp(sp.simplify(r)) for r in roots]}")
else:
    matches = False
    say("  no univariate eliminant in theta_inf found in the lex basis")

# ---------------------------------------------------------------- verdict ---
say()
say("=" * 74)
say("VERDICT")
say("=" * 74)
say(f"  V1 positive control          : {'PASS' if v1_ok else 'FAIL'}")
say(f"  V2 negative control          : {'PASS' if v2_ok else 'FAIL'}")
say(f"  V3 sensitivity to b1=0       : {'PASS' if v3_moved else 'FAIL'}")
say(f"  V4 saturation did work       : {'YES' if deg_v4 != deg_main else 'NO (recorded, not a gate)'}"
    f"   [saturated {deg_main} vs unsaturated {deg_v4}]")
say(f"  zero-dimensional             : {zd_main}")
say(f"  degree of the quotient ring  : {deg_main}")
say(f"  eliminant matches prediction : {matches}")
say()
if zd_main and deg_main == 2 and v1_ok and v2_ok and v3_moved:
    say("  H HOLDS.  The saturated ideal is zero-dimensional of degree 2 over")
    say("  K = Q(i*sqrt(11)), so the variety has AT MOST two points counted with")
    say("  multiplicity.  Two distinct points are exhibited and verified by V1.")
    say("  Therefore the solution set is EXACTLY those two points, and S16-12's")
    say("  'for both sign branches' is exhaustive.")
    rc = 0
elif zd_main and deg_main is not None and deg_main > 2:
    say(f"  F3 FIRED: degree {deg_main} > 2.  Additional solutions exist and")
    say("  S16-12 is WRONG.  Reported as found; not explained away.")
    rc = 1
elif zd_main is False:
    say("  F2 FIRED: the saturated ideal is NOT zero-dimensional.")
    rc = 1
else:
    say("  NOT CLOSED.  Take the PREREG section 6 fallback.")
    rc = 1
say("=" * 74)

path = Path(sys.argv[1])
path.write_text("\n".join(OUT) + "\n", encoding="utf-8")
# read back what was written
back = path.read_text(encoding="utf-8")
assert "VERDICT" in back and back.strip().endswith("=" * 74), "read-back failed"
print(f"\nwrote {path.name} ({len(back)} chars, sha256 "
      f"{hashlib.sha256(path.read_bytes()).hexdigest()})")
sys.exit(rc)
