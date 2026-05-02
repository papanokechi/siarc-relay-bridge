"""Probe: stage1 fit with various K_lead, see extrapolation behavior."""
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import mpmath as mp
import t37_runner as R

# Disable SVD truncation for this probe (set threshold absurdly low)
R._SVD_TRUNC_LOG10 = mp.mpf("1e-100")

mp.mp.dps = 200
a = R.load_series("V_quad")
stokes = R.load_stokes_at_dps("V_quad", 250)
zeta = stokes["zeta_star"]
C_T35 = stokes["C_T35"]
T = R.compute_T_array(a, zeta, 2000)

print("K_lead | C-C_T35       | a_1          | resid_inf  | T_lead(40)    | T_lead(100)   | T_lead(200)   | T_data(40)=", mp.nstr(T[40], 10), "T_data(100)=", mp.nstr(T[100], 10))
for K in [10, 15, 20, 25, 30, 35, 40]:
    s = R.stage1_fit(T, 800, 1900, K)
    p40 = R.stage1_predict(s, 40)
    p100 = R.stage1_predict(s, 100)
    p200 = R.stage1_predict(s, 200)
    print(f"K={K:2d} | {mp.nstr(s['C_fit']-C_T35, 4):>14s} | {mp.nstr(s['a_coeff'][1], 8):>13s} | {mp.nstr(s['residual_inf'], 4):>10s} | {mp.nstr(p40, 8):>13s} | {mp.nstr(p100, 8):>13s} | {mp.nstr(p200, 8):>13s} | rank={s['effective_rank']}")
