"""Verify the candidate relation found by mpmath at K=8783 against the M1
certified Arb balls.

For the candidate to be a GENUINE integer relation, the Arb-enclosed value
of sum_i m_i * x_i must CONTAIN ZERO. If it does NOT contain zero, the
candidate is a spurious mpmath artifact (precision-limited noise).

This is the operator's halt-time arbitration check, not a discovery
oracle: it uses ONLY M1 certified Arb balls and exact integer arithmetic.
"""
from __future__ import annotations
import sys, json, hashlib
sys.set_int_max_str_digits(1_000_000)
from flint import arb, ctx, fmpz
from pathlib import Path

ctx.prec = 1024

HERE = Path(__file__).parent
M1 = HERE / "M1_outputs" / "balls_P28712.json"

candidate_top = [15179948790500973246422, -6603394654578507390303, 6565294395350690323962, -10957173281012461161178, -5983495785540015769527, 16807627033953227217868, -5585247812062988178128, -7703456228348489266797, 20450190096676615809901, 15433720835932586713928, -21000395339540999557086, -38861446070259165830566, 10419220659249660832096, -2099160064932962436366, 3447828390839822348588]

print("M_certified verification of candidate relation from mpmath @ K=8783")
print()

with open(M1) as f:
    balls = json.load(f)

xs = [arb(e["arb_repr"]) for e in balls["basis"]]
labels = [e["label"] for e in balls["basis"]]

print(f"n = {len(xs)}, |relation| = {len(candidate_top)}")
print()
print("Per-term contributions (m_i * x_i):")
S = arb(0)
for i, (m, x, lbl) in enumerate(zip(candidate_top, xs, labels)):
    term = arb(m) * x
    S = S + term
    print(f"  i={i:2d}  {lbl:12s}  m={m:>25d}  m*x ~ {term.str(20)}")
print()
print(f"sum_i m_i * x_i (Arb enclosure) = {S.str(50)}")
print()
print(f"  midpoint     ~ {S.mid().str(40)}")
print(f"  abs rad approx{S.rad_lower()}")
print(f"  contains zero: {S.contains(arb(0))}")
print(f"  Euclidean norm |m|_2 (approx) = {(sum(m*m for m in candidate_top))**0.5:.3e}")
print(f"  Euclidean norm |m|_2 (exact, sqrt of int):")
norm_sq = sum(m*m for m in candidate_top)
print(f"     |m|_2^2 = {norm_sq}")
print(f"     |m|_2 ~= 10^{(len(str(norm_sq))-1)/2:.2f}")
print()

# Estimate the threshold below which |sum| would be consistent with zero given M1 ball radii.
# Each x_i has radius rad_i; total uncertainty in sum = sum_i |m_i| * rad_i.
total_unc = arb(0)
for m, x in zip(candidate_top, xs):
    total_unc = total_unc + arb(abs(m)) * arb(0, x.rad())
print(f"  Propagated uncertainty bound (sum |m_i| * rad(x_i)):")
print(f"  {total_unc.str(30)}")
print()
# Is |sum| << total_unc? That would mean the relation is consistent with M1 precision.
# Is |sum| >> total_unc? That would mean the relation is REJECTED.
abs_sum = abs(S)
print(f"  |sum| ~= {abs_sum.str(30)}")
print(f"  log10 |sum| approx {abs_sum.str(5)}")
