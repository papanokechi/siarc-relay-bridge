"""Re-verify the K=8783 candidate relation at FULL M1 precision in Arb.

M1 balls have intrinsic radii ~10^-8650. To distinguish a true relation
from a precision-limited noise hit, we need Arb working precision >= M1
precision. ctx.prec = 32768 bits ~= 9863 dps > 8650 dps M1 floor.
"""
from __future__ import annotations
import sys, json
sys.set_int_max_str_digits(1_000_000)
from flint import arb, ctx
from pathlib import Path

# Use high enough precision to exceed M1 intrinsic precision.
ctx.prec = 32768  # ~9863 dps; well above M1 P=28712 bits

HERE = Path(__file__).parent
M1 = HERE / "M1_outputs" / "balls_P28712.json"

candidate = [15179948790500973246422, -6603394654578507390303, 6565294395350690323962, -10957173281012461161178, -5983495785540015769527, 16807627033953227217868, -5585247812062988178128, -7703456228348489266797, 20450190096676615809901, 15433720835932586713928, -21000395339540999557086, -38861446070259165830566, 10419220659249660832096, -2099160064932962436366, 3447828390839822348588]

print(f"Arb working precision: {ctx.prec} bits (~{int(ctx.prec*0.301)} dps)")
print(f"M1 ball precision:     28712 bits (~8643 dps)")
print()

with open(M1) as f:
    balls = json.load(f)

xs = [arb(e["arb_repr"]) for e in balls["basis"]]
labels = [e["label"] for e in balls["basis"]]

S = arb(0)
for m, x in zip(candidate, xs):
    S = S + arb(m) * x

# Arb str of the enclosure (heavily truncated; we just want order-of-mag).
s = S.str(40)
print(f"sum_i m_i * x_i (Arb) = {s}")
print()

# Decision criteria
contains_zero = S.contains(arb(0))
print(f"  contains_zero (Arb): {contains_zero}")

# Get the radius and midpoint for direct inspection.
# arb.rad() returns an arf; convert to mpf-like display via str.
# The Arb .str(20) shows "[mid +/- rad]"; we already see it above.

# Crucially: a TRUE relation should give |sum| ~ 0 with radius ~ propagated
# uncertainty (= sum |m_i| * rad(x_i)). Compute that bound:
total_prop_rad = arb(0)
for m, x in zip(candidate, xs):
    # rad(x) as arb, multiplied by |m| (exact int)
    total_prop_rad = total_prop_rad + arb(abs(m)) * arb(0, x.rad())
print(f"  Propagated uncertainty bound: sum |m_i| * rad(x_i)")
print(f"     = {total_prop_rad.str(30)}")
print()

# Order-of-magnitude of |sum|: we want to know whether midpoint dominates radius
abs_S = abs(S)
print(f"  |sum| (Arb enclosure of absolute value): {abs_S.str(30)}")
print()

# Final verdict
if contains_zero:
    print("VERDICT: Arb enclosure of sum CONTAINS ZERO at high precision.")
    print("        Candidate relation is CONSISTENT with M1 balls at this precision.")
    print("        Likely a TRUE integer relation.")
else:
    print("VERDICT: Arb enclosure of sum DOES NOT contain zero.")
    print("        Candidate relation is REJECTED as a spurious mpmath artifact.")
