"""
T2A-CMAX2-RATIO-ANALYZE — Step 4 & 5: ratio distribution + Trans-hard
rate per ratio, plus pick 3 ratio!=1 Trans-hard families.
"""
import json
from collections import Counter, defaultdict
from pathlib import Path

results = json.load(open("t2a_cmax2_results.json"))
deep = json.load(open("t2a_cmax2_deep_results.json"))

R = results["results"]
D = {r["limit_dps50"]: r for r in deep["results"]}  # keyed by limit

# Convergent classification distribution by ratio
by_ratio_class = defaultdict(Counter)
for r in R:
    by_ratio_class[r["a4_b2sq_ratio"]][r["classification"]] += 1

print("=== Step 4: ratio distribution among CONVERGENT families ===")
total = sum(sum(v.values()) for v in by_ratio_class.values())
print(f"total convergent: {total}")
print(f"{'ratio':>8} {'total':>8} {'Rat':>8} {'Alg':>8} "
      f"{'Trans':>9} {'ERR':>6} {'pct':>6}")
for ratio in sorted(by_ratio_class):
    c = by_ratio_class[ratio]
    n = sum(c.values())
    print(f"{ratio:>8.3f} {n:>8} {c.get('Rat',0):>8} "
          f"{c.get('Alg',0):>8} {c.get('Trans-candidate',0):>9} "
          f"{c.get('ERR',0):>6} {100*n/total:>5.1f}%")

print()
print("=== Step 4 (Trans only): ratio distribution among "
      "Trans-candidates ===")
trans_total = sum(c.get("Trans-candidate", 0)
                  for c in by_ratio_class.values())
print(f"total Trans-candidate: {trans_total}")
print(f"{'ratio':>8} {'count':>8} {'pct':>6}")
for ratio in sorted(by_ratio_class):
    n = by_ratio_class[ratio].get("Trans-candidate", 0)
    if n == 0: continue
    print(f"{ratio:>8.3f} {n:>8} {100*n/trans_total:>5.1f}%")

print()
print("=== Step 5: Trans-candidate rate per ratio ===")
print(f"{'ratio':>8} {'conv':>8} {'Trans':>9} {'rate':>6}")
for ratio in sorted(by_ratio_class):
    c = by_ratio_class[ratio]
    n = sum(c.values())
    t = c.get("Trans-candidate", 0)
    if n == 0: continue
    print(f"{ratio:>8.3f} {n:>8} {t:>9} {100*t/n:>5.1f}%")

# Step 5b: confirmed Trans-hard from deep sample, by ratio
print()
print("=== Step 5b (deep sample, n=1000): confirmed Trans-hard "
      "by ratio ===")
deep_by_ratio = Counter()
for r in deep["results"]:
    if r["classification"] == "Trans-hard":
        deep_by_ratio[r["a4_b2sq_ratio"]] += 1
for ratio in sorted(deep_by_ratio):
    print(f"  ratio {ratio:>5.3f}: {deep_by_ratio[ratio]:>4} / "
          f"{sum(deep_by_ratio.values())} sampled")

# Step 6: pick 3 Trans-hard families from deep sample with ratio != 1
print()
print("=== Step 6: 3 Trans-hard families with ratio != 1 ===")
non_one = [r for r in deep["results"]
           if r["classification"] == "Trans-hard"
           and r["a4_b2sq_ratio"] != 1.0]
print(f"non-ratio-1 Trans-hard in deep sample: {len(non_one)}")
# spread by magnitude of L
def L_abs(r):
    try: return abs(float(r["L_dps150"][:30]))
    except: return 0.0
non_one.sort(key=L_abs)
n = len(non_one)
if n >= 3:
    picks = [non_one[0], non_one[n//2], non_one[-1]]
else:
    picks = non_one
for p in picks:
    print(f"  ratio={p['a4_b2sq_ratio']}  "
          f"a={p['coeffs_a']} b={p['coeffs_b']}  "
          f"L={p['L_dps150'][:50]}")

# Save picks for Step 6 follow-up
Path("t2a_cmax2_ratio_picks.json").write_text(
    json.dumps(picks, indent=2))
print(f"saved {len(picks)} picks to t2a_cmax2_ratio_picks.json")
