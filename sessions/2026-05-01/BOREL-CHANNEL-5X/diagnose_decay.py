"""Diagnostic: empirical decay law of delta_n = L_n - L* for V_quad."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from mpmath import mp, mpf
from borel_channel import compute_convergents

def a_fn(n):  return mpf(1)
def b_fn(n):  return mpf(3)*n*n + n + mpf(1)

mp.dps = 1200
L_arr, n_arr, stab = compute_convergents(a_fn, b_fn, depth=200, dps=1100, record_from=2)
print(f"stab={stab:.1f}, samples={len(L_arr)}")
L_star = L_arr[-1]
for n_target in [5, 10, 20, 30, 40, 50, 60, 80, 100, 120, 140, 160, 180]:
    i = n_arr.index(n_target) if n_target in n_arr else None
    if i is None: continue
    d = L_arr[i] - L_star
    if d == 0: continue
    print(f"n={n_target:4d}  log|d|={float(mp.log(abs(d))):>10.4f}  "
          f"log|d|/n={float(mp.log(abs(d))/n_target):>8.4f}  "
          f"log|d|/sqrt(n)={float(mp.log(abs(d))/mp.sqrt(n_target)):>8.4f}  "
          f"log|d|/(n log n)={float(mp.log(abs(d))/(n_target*mp.log(n_target))):>8.4f}")
