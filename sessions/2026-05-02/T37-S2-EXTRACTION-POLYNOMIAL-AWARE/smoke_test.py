"""Smoke test: verify infrastructure on V_quad with one config."""
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import mpmath as mp
import t37_runner as R

mp.mp.dps = 200

t0 = time.time()
print("Loading V_quad series...")
a = R.load_series("V_quad")
print(f"  N={len(a)-1}, a_0={a[0]}, a_1900={mp.nstr(a[1900], 6)}")

stokes = R.load_stokes_at_dps("V_quad", 250)
C_T35 = stokes["C_T35"]
zeta = stokes["zeta_star"]
print(f"  C_T35={mp.nstr(C_T35, 20)}, zeta*={mp.nstr(zeta, 12)}")

print("Computing T array...")
T = R.compute_T_array(a, zeta, 2000)
print(f"  T_1900={mp.nstr(T[1900], 12)}, T_100={mp.nstr(T[100], 12)}")
print(f"  (Should be ~ C_T35 + corrections; C_T35={mp.nstr(C_T35, 12)})")

print(f"\nStage 1 fit: K_lead=25, [800, 1900]...")
ts1 = time.time()
s1 = R.stage1_fit(T, 800, 1900, 25)
print(f"  done in {time.time()-ts1:.1f}s")
print(f"  C_fit = {mp.nstr(s1['C_fit'], 30)}")
print(f"  C_T35 = {mp.nstr(C_T35, 30)}")
print(f"  |diff| = {mp.nstr(abs(s1['C_fit'] - C_T35), 6)}")
print(f"  a_1 = {mp.nstr(s1['a_coeff'][1], 10)}")
print(f"  a_2 = {mp.nstr(s1['a_coeff'][2], 10)}")
print(f"  residual_inf = {mp.nstr(s1['residual_inf'], 6)}")
print(f"  cond_A = {mp.nstr(s1['cond_A'], 6)}")
print(f"  effective_rank = {s1['effective_rank']} / {41}")

# Show how stage1 behaves at low n
print("\nStage 1 polynomial extrapolation to low n:")
for n in [40, 60, 80, 100, 200, 500]:
    pred = R.stage1_predict(s1, n)
    print(f"  n={n:4d}: T_n_lead_pred = {mp.nstr(pred, 12)}, T_n_data = {mp.nstr(T[n], 12)}, diff = {mp.nstr(T[n] - pred, 6)}")

print(f"\nStage 2 fit: K_next=6, [40, 100]...")
ts2 = time.time()
s2 = R.stage2_fit(T, s1, 40, 100, 6)
print(f"  done in {time.time()-ts2:.1f}s")
print(f"  D_fit = {mp.nstr(s2['D_fit'], 12)}")
print(f"  b_1 = {mp.nstr(s2['b_coeff'][1], 8)}")
print(f"  residual_inf = {mp.nstr(s2['residual_inf'], 6)}")
print(f"  r_data_max = {mp.nstr(s2['r_data_max'], 6)}")
print(f"  cond_A = {mp.nstr(s2['cond_A'], 6)}")

print(f"\nTotal smoke-test time: {time.time()-t0:.1f}s")
