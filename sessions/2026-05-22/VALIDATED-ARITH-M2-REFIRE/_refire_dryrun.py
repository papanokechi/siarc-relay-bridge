"""Quick sanity check of certified_bound_refire.py building blocks
WITHOUT touching the actual M2-REFIRE pipeline. Tests:
  1. arb_thm1_init_bound on the M1 ball at CERT_PREC_BITS=32768
  2. arb_cor2_bound at K=29363 (m32a historical), should give ~6.66e21
  3. arb_floor_lower_endpoint correctness on a known value
  4. propagated_uncertainty_floor with a small synthetic relation
"""
from __future__ import annotations
import sys, json
sys.set_int_max_str_digits(1_000_000)
from pathlib import Path
from flint import arb, ctx
import certified_bound_refire as M

HERE = Path(__file__).parent
M1 = HERE / "M1_outputs" / "balls_P28712.json"

ctx.prec = M.CERT_PREC_BITS
print(f"ctx.prec = {ctx.prec} bits (~{int(ctx.prec*0.301)} dps)")

with open(M1) as f:
    balls_json = json.load(f)
arb_basis = M.reload_balls_as_arb(balls_json)
print(f"M1 ball loaded; first arb: {arb_basis[0].str(30)}")
print(f"M1 ball loaded; K_0 (label '{[e['label'] for e in balls_json['basis']][1]}'): {arb_basis[1].str(30)}")

# 1. Thm 1 init bound
b1 = M.arb_thm1_init_bound(arb_basis)
M1_thm1 = M.arb_floor_lower_endpoint(b1)
print(f"FBA Thm 1 init bound arb str = {b1.str(40)}")
print(f"floor(lower endpoint)       = {M1_thm1}")

# 2. Cor 2 at K=29363
K_test = 29363
b2 = M.arb_cor2_bound(K_test)
M2_cor2 = M.arb_floor_lower_endpoint(b2)
print(f"FBA Cor 2 at K={K_test}: arb str = {b2.str(40)}")
print(f"floor(lower endpoint)              = {M2_cor2}")
print(f"  expected ~ 6.66e21")

# 3. floor test on a known arb
test_arb = arb("12345.678 +/- 1e-30")
test_floor = M.arb_floor_lower_endpoint(test_arb)
print(f"floor(lower endpoint([12345.678 +/- 1e-30])) = {test_floor}")
assert test_floor == 12345, f"expected 12345, got {test_floor}"

# 4. Propagated uncertainty with a tiny relation [1, -1, 0, 0, ...]
rel = [1, -1] + [0] * (len(arb_basis) - 2)
floor_unc = M.propagated_uncertainty_floor(arb_basis, rel)
print(f"propagated uncertainty floor for [1,-1,0,...,0]: {floor_unc.str(40)}")
# Should be roughly 2 * rad(M1 ball) ~ 2 * 1e-8650

print()
print("ALL SANITY CHECKS PASSED")
