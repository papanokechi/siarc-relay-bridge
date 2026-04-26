"""Analyze T2B-F25 results: ratio distribution for Trans families."""
import json
from fractions import Fraction
from collections import Counter
from pathlib import Path

p = Path("t2b_f25_results.json")
data = json.loads(p.read_text())

print(f"Counts: {data['counts']}")
print(f"Total convergent: {data['stage_a_convergent']}")
print(f"Trans count: {data['trans_count']}")
print(f"Log count: {data['log_count']}")
print()

trans = data['trans_records']
ratios = Counter()
for r in trans:
    a2 = r['coeffs'][0]; b1 = r['coeffs'][3]
    rat = Fraction(a2, b1*b1)
    ratios[rat] += 1

print("=== Trans ratio distribution ===")
for r, c in sorted(ratios.items(), key=lambda x: float(x[0])):
    in_neg = Fraction(-1,4) < r < 0
    region = "neg-int" if in_neg else ("pos-int" if 0 < r < Fraction(1,4) else "outside/boundary")
    print(f"  {str(r):>10s}  ({float(r):+.5f})  count={c:3d}  [{region}]")

print()
print(f"Distinct ratios in Trans: {len(ratios)}")
print(f"-2/9 count: {ratios.get(Fraction(-2,9), 0)}")
print(f"-2/9 fraction of Trans: {ratios.get(Fraction(-2,9), 0)/len(trans):.3f}")

# New ratios at D=5 (not present at D=4)
D4_neg_int = {Fraction(-2,9), Fraction(-3,16), Fraction(-1,8), Fraction(-1,9), Fraction(-1,16)}
new_ratios_observed = [r for r in ratios if r not in D4_neg_int]
print()
print(f"=== Ratios beyond F(2,4)'s set ({len(D4_neg_int)} were available at D=4) ===")
new_neg_int = [r for r in new_ratios_observed if Fraction(-1,4) < r < 0]
print(f"NEW negative Worpitzky-interior ratios in Trans: {len(new_neg_int)}")
for r in sorted(new_neg_int, key=float):
    print(f"  {str(r):>10s}  count={ratios[r]}")

other_new = [r for r in new_ratios_observed if not (Fraction(-1,4) < r < 0)]
print(f"\nOther new ratios in Trans (positive or outside Worpitzky-interior):")
for r in sorted(other_new, key=float):
    print(f"  {str(r):>10s}  ({float(r):+.5f})  count={ratios[r]}")

# Save digest for handoff
digest = {
    "trans_count": len(trans),
    "log_count": data['log_count'],
    "distinct_ratios_in_trans": len(ratios),
    "ratio_distribution": {str(r): c for r, c in sorted(ratios.items(), key=lambda x: float(x[0]))},
    "minus_2_9_count": ratios.get(Fraction(-2,9), 0),
    "minus_2_9_fraction": ratios.get(Fraction(-2,9), 0)/len(trans) if trans else 0,
    "new_negative_worpitzky_interior": [str(r) for r in sorted(new_neg_int, key=float)],
    "other_new": [str(r) for r in sorted(other_new, key=float)],
    "D4_baseline_neg_int": [str(r) for r in sorted(D4_neg_int, key=float)],
}
Path("_t2b_f25_digest.json").write_text(json.dumps(digest, indent=2))
print("\nWrote _t2b_f25_digest.json")
