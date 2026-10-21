"""CT-S25 N1 - adjudicate the V3 failure.

V3 as written in PREREG.md section 5 fired: dropping b1 = 0 left the degree at 2.
PREREG says halt on that, and the main script did halt.

V3 is ILL-POSED, and this script establishes that rather than asserting it.
Its stated reasoning was:

    "the system without it is a strictly weaker condition, so a degree that does
     not move would show the observable cannot see that equation"

That inference is invalid. A strictly weaker generating set can define the SAME
variety, if the dropped polynomial already lies in the radical of the ideal the
others generate. V3 therefore conflates two causes with opposite meanings:

  (R) REDUNDANCY - b1 = 0 is implied by the five coefficient equations on the
      saturated locus.  A mathematical fact about the system.  The instrument is
      working; the arm asked the wrong question.
  (I) INSENSITIVITY - the degree genuinely cannot see a generator being
      dropped.  The instrument is broken and every degree it reports is void.

This is the same defect class as S23-07: an arm written assuming one outcome,
unable to distinguish an insensitive instrument from a legitimate agreement.

Two discriminating tests, pre-declared in PREREG-ADDENDUM.md before running:

  V3a  radical ideal membership.  Is b1 in sqrt(<coefficient eqs, Rabinowitsch>)?
       Decided exactly, by testing whether adjoining 1 - v*b1 gives the unit
       ideal.  YES => cause (R).
  V3b  positive sensitivity control.  Drop each coefficient equation in turn and
       recompute the degree.  If the degree moves for some drop, the observable
       demonstrably CAN see a generator being removed, which excludes cause (I).

VERDICT RULE, fixed before running: cause (R) is established only if V3a says
YES *and* V3b moves for at least one drop.  Either alone is insufficient.
"""

import hashlib
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

OUT = []


def say(s=""):
    OUT.append(str(s))
    print(s)


z, p, q, t, thi, u, v = sp.symbols("z p q t theta_inf u v")

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
poly_z = sp.Poly(sp.expand(lhs - Nz_scaled), z)
COEFF_EQS = [sp.expand(sp.numer(sp.cancel(co))) for co in poly_z.all_coeffs()]
B1_EQ = sp.expand(sp.numer(sp.cancel(b1)))
RAB = sp.expand(u * q * (q - 1) - 1)

K = sp.QQ.algebraic_field(sp.I * sp.sqrt(11))
VARS = (p, q, t, thi, u)

say("=" * 74)
say("CT-S25-N1-EXHAUSTIVE / n1_v3_adjudicate.py")
say("Adjudicating the V3 failure: redundancy (R) or insensitivity (I)?")
say("=" * 74)


def degree_of(gens, variables, label):
    t0 = time.time()
    G = sp.groebner(gens, *variables, order="grevlex", domain=K)
    zd = G.is_zero_dimensional
    if not zd:
        say(f"  [{label}] NOT zero-dimensional ({time.time()-t0:.1f}s)")
        return None
    lead_exp = [tuple(sp.Poly(g, *variables, domain=K).LM(order="grevlex").exponents)
                for g in G.exprs]
    bounds = []
    for i in range(len(variables)):
        pure = [e[i] for e in lead_exp
                if all(e[j] == 0 for j in range(len(variables)) if j != i)]
        if not pure:
            return None
        bounds.append(min(pure))
    import itertools
    count = sum(
        1 for expo in itertools.product(*[range(b) for b in bounds])
        if not any(all(expo[i] >= le[i] for i in range(len(variables))) for le in lead_exp)
    )
    say(f"  [{label}] degree {count}   ({time.time()-t0:.1f}s)")
    return count


# ------------------------------------------------------------------ V3a ----
say()
say("-" * 74)
say("V3a  Is b1 in the RADICAL of <5 coefficient equations, Rabinowitsch>?")
say("     Decided exactly: b1 is in the radical iff adjoining 1 - v*b1")
say("     produces the UNIT ideal.  This is a yes/no algebraic fact.")
say("-" * 74)

I_coeff = COEFF_EQS + [RAB]

G0 = sp.groebner(I_coeff, *VARS, order="grevlex", domain=K)
rem = G0.reduce(B1_EQ)[1]
say(f"  plain ideal membership: b1 reduces to {sp.expand(rem)}")
plain_member = sp.expand(rem) == 0
say(f"  b1 in the ideal itself                : {plain_member}")

t0 = time.time()
G_rad = sp.groebner(I_coeff + [sp.expand(1 - v * B1_EQ)], v, *VARS,
                    order="grevlex", domain=K)
is_unit = list(G_rad.exprs) == [sp.Integer(1)] or (
    len(G_rad.exprs) == 1 and sp.simplify(G_rad.exprs[0] - 1) == 0)
say(f"  Rabinowitsch ideal basis: {G_rad.exprs if len(G_rad.exprs) < 4 else str(len(G_rad.exprs)) + ' polys'}"
    f"   ({time.time()-t0:.1f}s)")
say(f"  unit ideal  =>  b1 in the RADICAL      : {is_unit}")

# control for V3a: a polynomial that is NOT in the radical must be detected.
# theta_inf itself vanishes nowhere on the variety (roots are -2 +/- sqrt3/9),
# so it must NOT be in the radical.
G_ctrl = sp.groebner(I_coeff + [sp.expand(1 - v * thi)], v, *VARS,
                     order="grevlex", domain=K)
ctrl_unit = len(G_ctrl.exprs) == 1 and sp.simplify(G_ctrl.exprs[0] - 1) == 0
say(f"  [control] theta_inf in the radical?    : {ctrl_unit}  (must be False;")
say(f"            theta_inf vanishes nowhere on the variety, so a test that")
say(f"            returned True here would be accepting everything)")
v3a_ok = is_unit and not ctrl_unit
say(f"V3a: {'b1 IS in the radical -> cause (R) supported' if v3a_ok else 'INCONCLUSIVE'}")

# ------------------------------------------------------------------ V3b ----
say()
say("-" * 74)
say("V3b  Positive sensitivity control.  Drop each coefficient equation in")
say("     turn, keeping b1 = 0.  If the degree moves for ANY drop, the")
say("     observable demonstrably CAN see a generator being removed, which")
say("     excludes cause (I).")
say("-" * 74)
base = degree_of(COEFF_EQS + [B1_EQ, RAB], VARS, "full system")
moved = []
for i in range(len(COEFF_EQS)):
    sub = [e for j, e in enumerate(COEFF_EQS) if j != i] + [B1_EQ, RAB]
    d = degree_of(sub, VARS, f"drop coefficient eq {i}")
    if d != base:
        moved.append((i, d))
say(f"  drops that moved the degree from {base}: {moved if moved else 'NONE'}")
v3b_ok = len(moved) > 0
say(f"V3b: {'PASS - the observable can see a dropped generator' if v3b_ok else 'FAIL - observable is blind to every drop'}")

# -------------------------------------------------------------- verdict ----
say()
say("=" * 74)
say("V3 ADJUDICATION")
say("=" * 74)
say(f"  V3a  b1 in the radical of the other generators : {is_unit}")
say(f"  V3a  control (must be False)                   : {ctrl_unit}")
say(f"  V3b  degree moves on some other drop           : {v3b_ok}  {moved}")
say()
if v3a_ok and v3b_ok:
    say("  CAUSE (R) - REDUNDANCY, established, not assumed.")
    say()
    say("  b1 lies in the radical of the ideal generated by the five coefficient")
    say("  equations on the saturated locus, so dropping it cannot change the")
    say("  variety.  The instrument is NOT insensitive: V3b shows the degree does")
    say("  move when a genuinely independent generator is removed.")
    say()
    say("  Therefore V3's halt condition was triggered by an ill-posed arm, not")
    say("  by a defect in the computation.  V3 is WITHDRAWN AS ILL-POSED and")
    say("  left unedited in PREREG.md, per the handling used for Stage 5A.")
    say()
    say("  MATHEMATICAL CONTENT, worth stating in its own right: the quartic")
    say("  coefficient matching ALREADY FORCES the no-apparent-singularity")
    say("  condition b1 = 0.  It did not have to be imposed separately.")
    rc = 0
elif not v3b_ok:
    say("  CAUSE (I) - INSENSITIVITY.  The observable cannot see any generator")
    say("  being dropped.  Every degree reported by this instrument is VOID.")
    rc = 2
else:
    say("  INCONCLUSIVE.  Neither cause established; take the fallback.")
    rc = 1
say("=" * 74)

path = Path(sys.argv[1])
path.write_text("\n".join(OUT) + "\n", encoding="utf-8")
back = path.read_text(encoding="utf-8")
assert "V3 ADJUDICATION" in back, "read-back failed"
print(f"\nwrote {path.name} ({len(back)} chars, sha256 "
      f"{hashlib.sha256(path.read_bytes()).hexdigest()})")
sys.exit(rc)
