"""Smoke test single fit to estimate timing."""
import time
import mpmath as mp
mp.mp.dps = 300
from t37e_runner import load_a_csv, build_T_cache, load_rep_params, run_full_fit

reps = load_rep_params()
rid = "V_quad"

print("Loading a_n...")
t0 = time.time()
a = load_a_csv(rid)
print(f"  loaded in {time.time()-t0:.1f}s")

print("Building T_n cache...")
t0 = time.time()
T = build_T_cache(a, reps[rid]["zeta_star"])
print(f"  built in {time.time()-t0:.1f}s")

for K_lead in (40, 80):
    print(f"Single fit K_lead={K_lead}, K_next=12, W1=(3000,4900), W2=(60,200)...")
    t0 = time.time()
    cfg = run_full_fit(T, K_lead, 12, (3000, 4900), (60, 200))
    print(f"  fit in {time.time()-t0:.1f}s")
    print(f"  C = {mp.nstr(cfg['C'], 30)}")
    print(f"  a_1 = {mp.nstr(cfg['a_k'][0], 30)}")
    print(f"  D = {mp.nstr(cfg['D'], 30)}")
    print(f"  cond1 = {mp.nstr(cfg['cond1'], 6)}; cond2 = {mp.nstr(cfg['cond2'], 6)}")
    print(f"  |R_n@W2_hi| = {mp.nstr(abs(cfg['R_n_at_W2_hi']), 10)}")
