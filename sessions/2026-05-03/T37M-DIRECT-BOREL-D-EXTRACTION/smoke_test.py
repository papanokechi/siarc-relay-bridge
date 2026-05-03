"""Smoke test: load V_quad series, run stage-1 fit, build Borel coeffs, run one Pade.
Quick sanity check before full t37m_runner run.
"""
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import mpmath as mp
from t37m_runner import (
    load_t35, load_a_series, RepData, stage1_fit, make_residual_series,
    borel_eta_coeffs, try_pade, find_poles_near_eta2,
    T35_DIR, T37E_DIR, fmt_mp, DPS_FIT, DPS_PADE,
)

mp.mp.dps = DPS_FIT
print("Loading T35...")
t35 = load_t35(T35_DIR / "representatives.json", T35_DIR / "stokes_multipliers_per_rep.csv")
rid = "V_quad"
info = t35[rid]
zeta = mp.mpf(info["zeta_star"]); C = mp.mpf(info["C_lsq"])
print(f"V_quad zeta={fmt_mp(zeta,12)} C={fmt_mp(C,12)}")
print("Loading series...")
t0 = time.time()
series = load_a_series(rid)
print(f"  loaded {len(series)} entries in {time.time()-t0:.2f}s, a_1={fmt_mp(series[1],10)}, a_5000 magnitude={fmt_mp(abs(series[5000]),5)}")
rep = RepData(rep=rid, alpha=info["alpha"], beta=info["beta"], gamma=info["gamma"],
              delta=info["delta"], epsilon=info["epsilon"], side=info["side"],
              Delta_b=int(info["Delta_b"]), A_pred=int(info["A_pred"]),
              zeta_star=zeta, C=C, S1_imag=mp.mpf(info["S1_imag"]), a_series=series)

print("Stage-1 fit (K=25)...")
t1 = time.time()
s1 = stage1_fit(rep)
print(f"  done in {time.time()-t1:.1f}s, a_1={fmt_mp(s1['a'][1],30)}, a_2={fmt_mp(s1['a'][2],30)}")
print(f"  expected: a_1=-53/36={fmt_mp(mp.mpf(-53)/36,30)}")

print("Cleanness step...")
t2 = time.time()
res = make_residual_series(rep, s1["a"])
print(f"  done in {time.time()-t2:.1f}s")
for n in (10, 100, 500, 2000, 5000):
    L = C * mp.gamma(n) * mp.power(zeta, -n)
    print(f"  n={n}: |res|/|lead| = {fmt_mp(abs(res[n])/abs(L),8)}")

print("Borel transform (eta)...")
mp.mp.dps = DPS_PADE
t3 = time.time()
b = borel_eta_coeffs(rep, res, 200)
print(f"  done in {time.time()-t3:.1f}s; |b_50|={fmt_mp(abs(b[50]),8)}, |b_100|={fmt_mp(abs(b[100]),8)}, |b_200|={fmt_mp(abs(b[200]),8)}")

print("Pade [60,60] from M_in=200...")
t4 = time.time()
out = try_pade(b, 60)
if out is None:
    print("  RANK_LOSS")
else:
    P, Q = out
    poles = find_poles_near_eta2(P, Q)
    print(f"  done in {time.time()-t4:.1f}s; {len(poles)} physical poles")
    for p in poles[:5]:
        print(f"    eta={fmt_mp(p['Re_eta'],12)}+i*{fmt_mp(p['Im_eta'],12)}  dist_from_2={fmt_mp(p['dist_from_2'],8)}  |res|={fmt_mp(abs(p['residue']),8)}")
