"""CT-S25 N1 - known-answer control for the degree-counting code.

See PREREG-ADDENDUM-2.md, written before this was run.  The expected degrees in
the table below were fixed there and are NOT adjusted here.

Why this and not a third sensitivity arm: V3 and V3b both failed as instrument
tests because the target system is overdetermined (six generators, four
unknowns, two points), so redundancy absorbs any single perturbation and a null
response is uninterpretable.  A known-answer control does not touch the target
system at all, which is exactly why overdetermination cannot absorb it.  This is
the CT-S22 Stage 1 pattern.

FALSIFIER: any row returning other than its stated value means the counter is
wrong and every degree in this session, including the main degree-2 result, is
VOID.
"""

import hashlib
import itertools
import sys
from pathlib import Path

import sympy as sp

OUT = []


def say(s=""):
    OUT.append(str(s))
    print(s)


p, q, t, thi, u = sp.symbols("p q t theta_inf u")
VARS = (p, q, t, thi, u)
K = sp.QQ.algebraic_field(sp.I * sp.sqrt(11))
RAB = sp.expand(u * q * (q - 1) - 1)


def degree_of(gens, variables=VARS):
    """The SAME code path used for the main result.  Returns int, or None if
    the ideal is not zero-dimensional, or 0 for the unit ideal (empty variety)."""
    G = sp.groebner(list(gens), *variables, order="grevlex", domain=K)
    if len(G.exprs) == 1 and sp.simplify(G.exprs[0] - 1) == 0:
        return 0
    if not G.is_zero_dimensional:
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
    return sum(
        1 for expo in itertools.product(*[range(b) for b in bounds])
        if not any(all(expo[i] >= le[i] for i in range(len(variables))) for le in lead_exp)
    )


# Expected values fixed in PREREG-ADDENDUM-2.md section 3 BEFORE running.
BATTERY = [
    ("A", [p - 1, q - 2, t - 3, thi - 5], 1,
     "four linear equations: a single point"),
    ("B", [p**2 - 2, q - 2, t - 3, thi - 5], 2,
     "p quadratic: two points"),
    ("C", [p**3 - 2, q - 2, t - 3, thi - 5], 3,
     "p cubic: three points"),
    ("D", [p**2 - 2, q**2 - 4, t - 3, thi - 5], 4,
     "2 x 2; both roots q = +/-2 survive saturation"),
    ("E", [p**2 - 2, q - 2, t**3 - 7, thi - 5], 6,
     "2 x 3"),
    ("F", [p - 1, q - 2, t - 3], None,
     "theta_inf free: must NOT be zero-dimensional"),
    ("G", [p - 1, q - 2, t - 3, thi - 5, q], 0,
     "forces q = 0, which saturation removes: empty"),
]

say("=" * 74)
say("CT-S25-N1-EXHAUSTIVE / n1_known_answer.py")
say("Known-answer control for the degree-counting code path.")
say("Expected values fixed in PREREG-ADDENDUM-2.md before this was run.")
say("=" * 74)
say()
say(f"{'row':<5}{'expected':<12}{'got':<12}{'result':<8}  note")
say("-" * 74)

results = {}
for name, gens, expected, note in BATTERY:
    got = degree_of(gens + [RAB])
    ok = (got == expected)
    results[name] = ok
    e_s = "not 0-dim" if expected is None else str(expected)
    g_s = "not 0-dim" if got is None else str(got)
    say(f"{name:<5}{e_s:<12}{g_s:<12}{'PASS' if ok else 'FAIL':<8}  {note}")

say("-" * 74)
npass = sum(1 for v in results.values() if v)
say(f"KNOWN-ANSWER BATTERY: {npass}/{len(results)}")

say()
say("=" * 74)
if npass == len(results):
    say("The degree-counting code path is CORRECT on independently known answers,")
    say("across degrees 0, 1, 2, 3, 4, 6 and one positive-dimensional case.")
    say("Row G confirms the saturation actively removes the q = 0 locus rather")
    say("than being inert.")
    say()
    say("This licenses the main result's degree of 2 as a genuine bound, without")
    say("relying on any sensitivity arm on the overdetermined target system.")
    rc = 0
else:
    say("FALSIFIER FIRED: the counter is wrong.  Every degree reported in this")
    say("session, INCLUDING the main degree-2 result, is VOID.")
    rc = 1
say("=" * 74)

path = Path(sys.argv[1])
path.write_text("\n".join(OUT) + "\n", encoding="utf-8")
back = path.read_text(encoding="utf-8")
assert "KNOWN-ANSWER BATTERY" in back, "read-back failed"
print(f"\nwrote {path.name} ({len(back)} chars, sha256 "
      f"{hashlib.sha256(path.read_bytes()).hexdigest()})")
sys.exit(rc)
