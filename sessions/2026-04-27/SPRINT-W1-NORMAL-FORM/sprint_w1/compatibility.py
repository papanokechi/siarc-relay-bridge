"""
SPRINT-W1-NORMAL-FORM — Part D
Compatibility condition C and integer-grid sample check.

The compatibility condition for indicial pair {1/3, 2/3} in
degree-(2,1) PCFs (a_n = a2 n^2 + a1 n + a0,  b_n = b1 n + b0) is:

    C1 :  a1 - 2 a2                                  = 0
    C2 :  a2 + 9 b0^2 - 27 b0 b1 + 20 b1^2           = 0

(a0 does not appear at the leading two-term Birkhoff balance.)

Equivalently:    a1 = 2 a2          and   a2 / b1^2 = -9 r^2 + 27 r - 20
                                                where r = b0/b1.

Empirically, the conjectured Trans-class fingerprint is
    a2 / b1^2 = -2/9 .

This is recovered by C only when r solves  -9 r^2 + 27 r - 20 = -2/9 ,
i.e.  r = (27 +/- sqrt(17)) / 18  -- irrational.

Hence:  no integer Trans family can satisfy C exactly; equivalently,
the empirical -2/9 fingerprint does NOT arise from a forced indicial
pair {1/3, 2/3}.

Below we (1) write C explicitly, (2) parameterise the C-locus
symbolically, (3) enumerate small integer (a2, a1, a0, b0, b1)
satisfying both empirical Trans ratio (a2 / b1^2 = -2/9) and
indicial pair {1/3, 2/3} (i.e. C), and verify the predicted
emptiness over Z.
"""

import json
import sympy as sp
from sympy import Rational, sqrt, simplify

a0, a1, a2, b0, b1 = sp.symbols("a0 a1 a2 b0 b1", real=True)
r = sp.symbols("r", real=True)

print("="*68)
print("PART D — Compatibility condition C")
print("="*68)
C1 = a1 - 2*a2
C2 = a2 + 9*b0**2 - 27*b0*b1 + 20*b1**2
print(f"  C1 := {C1}  = 0")
print(f"  C2 := {C2}  = 0")
print()
print("  Symbolic ratio in r = b0/b1 (after C1 imposed):")
ratio_in_r = sp.simplify(-9*r**2 + 27*r - 20)
print(f"      a2 / b1^2  =  {ratio_in_r}")
print()
target = Rational(-2, 9)
print(f"  Solving  a2 / b1^2 = {target}  for r:")
sols = sp.solve(sp.Eq(ratio_in_r, target), r)
for s in sols:
    print(f"      r = {s}    ~= {sp.N(s, 12)}")

print()
print("="*68)
print("Integer-grid sample check")
print("="*68)
print("Enumerate (a2, b0, b1) with |b1| <= 30, |b0| <= 30, |a2| <= 200,")
print("checking both:")
print("  (E)   a2 / b1^2 = -2/9              (empirical Trans ratio)")
print("  (C)   C1=0 AND C2=0                 (forces indicial {1/3, 2/3})")
print()

both_count = 0
e_only_count = 0
c_only_count = 0
samples_E = []
samples_C = []
samples_both = []

for B1 in range(1, 31):
    for B0 in range(-30, 31):
        for A2 in range(-200, 201):
            # E test:  9 a2 + 2 b1^2 = 0
            E_ok = (9*A2 + 2*B1*B1 == 0)
            # C2 test (a2 + 9 b0^2 - 27 b0 b1 + 20 b1^2 = 0)
            C2_ok = (A2 + 9*B0*B0 - 27*B0*B1 + 20*B1*B1 == 0)
            if E_ok and C2_ok:
                both_count += 1
                if len(samples_both) < 5:
                    samples_both.append((A2, B0, B1))
            elif E_ok:
                e_only_count += 1
                if len(samples_E) < 5:
                    samples_E.append((A2, B0, B1))
            elif C2_ok:
                c_only_count += 1
                if len(samples_C) < 5:
                    samples_C.append((A2, B0, B1))

print(f"  matches BOTH (E and C):    {both_count}    (predicted: 0)")
print(f"  matches E only:            {e_only_count}")
print(f"  matches C only:            {c_only_count}")
print()
print("  Sample E-only triples (a2, b0, b1)  [a2/b1^2 = -2/9 holds]:")
for s in samples_E:
    A2, B0, B1 = s
    val_C2 = A2 + 9*B0*B0 - 27*B0*B1 + 20*B1*B1
    print(f"      a2={A2:5d}  b0={B0:3d}  b1={B1:3d}    "
          f"C2 residual = {val_C2}")
print()
print("  Sample C-only triples (a2, b0, b1)  [indicial pair {1/3, 2/3}, integer]:")
for s in samples_C:
    A2, B0, B1 = s
    val_E_num = 9*A2 + 2*B1*B1
    print(f"      a2={A2:5d}  b0={B0:3d}  b1={B1:3d}    "
          f"E residual (9 a2 + 2 b1^2) = {val_E_num}")
print()

if both_count == 0:
    verdict = (
        "VERIFIED: over the searched integer grid, no PCF simultaneously "
        "satisfies the empirical Trans ratio a2/b1^2 = -2/9 AND the "
        "indicial pair {1/3, 2/3}.  This matches the symbolic prediction "
        "(b0/b1 must be irrational)."
    )
else:
    verdict = (
        "WARNING: integer solutions to E AND C found.  This contradicts "
        "the symbolic analysis and must be investigated."
    )
print(verdict)

# Dump a small summary JSON for the report
summary = {
    "C1":  "a1 - 2*a2",
    "C2":  "a2 + 9*b0^2 - 27*b0*b1 + 20*b1^2",
    "empirical_E":   "9*a2 + 2*b1^2 = 0",
    "search_bounds": {"abs_a2": 200, "abs_b0": 30, "b1_min": 1, "b1_max": 30},
    "matches_E_and_C":  both_count,
    "matches_E_only":   e_only_count,
    "matches_C_only":   c_only_count,
    "sample_E_only":    samples_E,
    "sample_C_only":    samples_C,
    "verdict":          verdict,
}
with open("compatibility_summary.json", "w") as f:
    json.dump(summary, f, indent=2)
print("\nWrote compatibility_summary.json")
