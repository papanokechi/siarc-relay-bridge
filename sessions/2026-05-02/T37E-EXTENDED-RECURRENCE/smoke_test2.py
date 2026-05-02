"""Smoke test: optimized grid Stage 1 alpha agrees with slow path."""
import time
import mpmath as mp
mp.mp.dps = 300
from t37e_runner import (
    load_a_csv, build_T_cache, load_rep_params,
    stage1_fit, stage1_qr_max, stage1_alpha_at_K,
)

reps = load_rep_params()
rid = "V_quad"
a = load_a_csv(rid)
T = build_T_cache(a, reps[rid]["zeta_star"])

W1 = (3000, 4900)
print("Building stage1 QR at K_max=120...")
t0 = time.time()
s1 = stage1_qr_max(T, W1, 120)
print(f"  done in {time.time()-t0:.1f}s")

for K in (40, 60, 80):
    alpha_opt, cond_opt = stage1_alpha_at_K(s1, K)
    # slow path
    t0 = time.time()
    alpha_slow, cond_slow = stage1_fit(T, W1[0], W1[1], K)
    print(f"K={K} slow path: {time.time()-t0:.1f}s")
    diff_C = abs(alpha_opt[0] - alpha_slow[0])
    diff_a1 = abs(alpha_opt[1] - alpha_slow[1])
    print(f"  K={K}: |C_opt - C_slow| = {mp.nstr(diff_C, 5)}; |alpha1| = {mp.nstr(diff_a1, 5)}")
    print(f"         a_1 = {mp.nstr(alpha_opt[1] / alpha_opt[0], 30)}")
    print(f"         cond_opt = {mp.nstr(cond_opt, 6)} ; cond_slow = {mp.nstr(cond_slow, 6)}")
