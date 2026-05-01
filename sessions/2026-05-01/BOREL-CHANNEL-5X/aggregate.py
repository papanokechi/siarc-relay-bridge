"""Aggregate Borel-channel results and generate summary.json + table."""
import json
from pathlib import Path
from mpmath import mpf, mp, log

D = Path(__file__).parent
families = ["V_quad", "QL01", "QL02", "QL06", "QL15", "QL26"]
file_map = {"V_quad": "vquad_result.json",
            "QL01": "ql01_result.json", "QL02": "ql02_result.json",
            "QL06": "ql06_result.json", "QL15": "ql15_result.json",
            "QL26": "ql26_result.json"}

# Theoretical (alpha, A) from log|delta_n| ~ sum log|a_k| - 2 log q_n
# log q_n ~ deg(b)*log(n!) + n*log(c_b)  (c_b = leading coeff of b_n)
# For deg(b)=2: 2 log q_n ~ 4 n log n - 4 n + 2 n log(c_b)
# For a_n = c_a*n + d_a: sum log|a_k| ~ n log(c_a) + log(n!) ~ n log(c_a) + n log n - n
# A and alpha:
#   if a_n constant (V_quad: a=1):  A=4, alpha = 4 - 2 log(c_b)
#   if a_n ~ c_a * n  (QL01,06,15): A=3, alpha = 3 - 2 log(c_b) + log(c_a)
#       (QL01: c_a=1, c_b=1 -> alpha=3+0+0=3
#        QL06: c_a=1, c_b=2 -> alpha=3 - 2*log(2)
#        QL15: c_a=1, c_b=3 -> alpha=3 - 2*log(3))
#   if a_n ~ c_a*n + d_a (QL02: 2n+1, QL26: -3n+1):
#       sum log|a_k| ~ log(prod |a_k|) ~ n log|c_a| + log(n!) for large n
#       (assuming |c_a*k+d_a| ~ |c_a| k); alpha = 3 - 2 log(c_b) + log|c_a|

def theoretical(family):
    # returns (A_pred, alpha_pred) as mpf
    if family == "V_quad": c_a, d_a, c_b = 0, 1, 3      # a=1
    elif family == "QL01": c_a, d_a, c_b = 1, 0, 1
    elif family == "QL02": c_a, d_a, c_b = 2, 1, 1
    elif family == "QL06": c_a, d_a, c_b = 1, 0, 2
    elif family == "QL15": c_a, d_a, c_b = 1, 0, 3
    elif family == "QL26": c_a, d_a, c_b = 3, 1, 4      # |a_n|~3n
    if c_a == 0:
        return mp.mpf(4), mp.mpf(4) - 2 * log(c_b)
    else:
        return mp.mpf(3), mp.mpf(3) - 2 * log(c_b) + log(c_a)

mp.dps = 30
out = {"families": [], "summary_table": [], "K_scan_vquad": None}
for fam in families:
    p = D / file_map[fam]
    if not p.exists():
        out["families"].append({"family": fam, "error": "missing"})
        continue
    with open(p) as f: r = json.load(f)
    A_pred, alpha_pred = theoretical(fam)
    A_obs = mpf(r["trans_series"]["A"])
    alpha_obs = mpf(r["trans_series"]["alpha"])
    A_match = abs(A_obs - A_pred) < mpf("1e-10")
    alpha_match = abs(alpha_obs - alpha_pred) < mpf("1e-6")
    rho = r.get("rho_star", {})
    rho_re = mpf(rho.get("re", "0")); rho_im = mpf(rho.get("im", "0"))
    rho_abs = mpf(rho.get("abs", "0"))
    arg_over_pi = (mp.atan2(rho_im, rho_re) / mp.pi) if rho_abs > 0 else mp.mpf(0)
    # axis classification
    if abs(arg_over_pi - 1) < 1e-3 or abs(arg_over_pi + 1) < 1e-3:
        axis = "negative real (Stokes line)"
    elif abs(arg_over_pi) < 1e-3:
        axis = "positive real"
    elif abs(rho_im) < abs(rho_re) * 0.05:
        axis = "near-real"
    else:
        axis = f"off-axis (arg/pi = {mp.nstr(arg_over_pi, 4)})"
    bc = r["best_cell"]
    out["families"].append({
        "family": fam,
        "Delta": r["Delta"], "CM_field": r["CM_field"], "Heegner": r["Heegner"],
        "trans_series": {
            "A_obs": mp.nstr(A_obs, 14),
            "A_predicted": mp.nstr(A_pred, 6),
            "A_match": A_match,
            "alpha_obs": mp.nstr(alpha_obs, 14),
            "alpha_predicted": mp.nstr(alpha_pred, 14),
            "alpha_match": alpha_match,
            "beta": r["trans_series"]["beta"],
            "gamma": r["trans_series"]["gamma"],
            "ts_residual_max_log_delta": r["trans_series"]["residual_max_log_delta"],
            "h_first6": r["trans_series"]["h"][:6],
        },
        "rho_star": {
            "re": rho.get("re"), "im": rho.get("im"),
            "abs": rho.get("abs"),
            "arg_over_pi": mp.nstr(arg_over_pi, 8),
            "axis_class": axis,
        },
        "pade_poles_first8": r.get("pade_poles", []),
        "best_painleve_fit": {
            "equation": bc["equation"], "residual": bc["residual"],
            "params": bc["params"], "h": bc["h"],
        },
        "verdict": r["verdict"],
    })
    out["summary_table"].append([
        fam, r["Delta"], r["CM_field"], r["Heegner"],
        mp.nstr(A_obs, 4), mp.nstr(alpha_obs, 8), r["trans_series"]["beta"],
        rho.get("abs"), axis,
        bc["equation"], bc["residual"], r["verdict"],
    ])

# Append K-scan
ks = D / "vquad_kscan.json"
if ks.exists():
    with open(ks) as f: out["K_scan_vquad"] = json.load(f)

# Counts of verdicts
counts = {"CANDIDATE": 0, "MARGINAL": 0, "NO_FIT": 0}
for fr in out["families"]:
    v = fr.get("verdict")
    if v in counts: counts[v] += 1
out["verdict_counts"] = counts

n_explicit = counts["CANDIDATE"]
n_marginal = counts["MARGINAL"]
if n_explicit == 5 and out["families"][0]["verdict"] == "CANDIDATE":
    flag = "BOREL CHANNEL UNIVERSAL"
elif n_explicit >= 3:
    flag = "BOREL CHANNEL PARTIAL"
else:
    flag = "BOREL CHANNEL ANOMALOUS"
# but per V_quad gate failure (residual ~10^-3 vs required 10^-20),
# even MARGINAL hits cannot be trusted - they are likely Pade noise.
out["flag"] = flag
out["v_quad_gate_failed"] = True
out["v_quad_gate_evidence"] = {
    "required_residual": "1e-20",
    "best_residual_observed": out["families"][0]["best_painleve_fit"]["residual"],
    "K_scan_residual_trend": "non-converging: 7.2e-3 (K=12) -> 5.0e-3 (K=16) -> 1.0e-2 (K=20) -> 9.9e-2 (K=24)",
    "Pade_pole_radius_trend": "non-converging: 2.17 (K=12) -> 3.00 -> 3.65 -> 4.59 (no finite-radius Borel singularity)",
    "interpretation": ("Trans-series 1/n coefficients h_k are stable to 14 digits "
                       "across K, but Pade approximants of B(zeta) = sum h_k zeta^{k-1}/(k-1)! "
                       "do not converge to any finite-radius singularity.  This indicates "
                       "the Borel transform has either no finite-radius singularity (i.e. the "
                       "1/n series is convergent or super-Gevrey-1 divergent), or the "
                       "singularities lie at infinity in the zeta plane.  The Painleve "
                       "ansatz fits via this channel are therefore Pade artefacts, not real "
                       "Borel-channel reductions.")
}

with open(D / "summary.json", "w") as f:
    json.dump(out, f, indent=2)
print("Wrote summary.json")
print("\nFlag matrix counts:", counts)
print("FLAG:", flag)
print("V_quad gate:", "FAILED" if out["v_quad_gate_failed"] else "PASSED")

# Pretty-print table
print("\n5-row table for paper:")
print(f"{'Family':>7}  {'Delta':>5}  {'CM':>14}  {'A':>4}  {'alpha':>9}  "
      f"{'|rho*|':>8}  {'axis':>30}  {'best PE':>8}  {'residual':>14}  {'verdict':>10}")
for row in out["summary_table"]:
    fam, D_, cm, heg, A, a, b, ra, ax, eq, res, v = row
    print(f"{fam:>7}  {D_:>5}  {cm:>14}  {A:>4}  {a:>9}  {ra:>8}  {ax:>30}  "
          f"{eq:>8}  {res:>14}  {v:>10}")
