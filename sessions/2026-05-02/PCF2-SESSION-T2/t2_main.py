"""PCF2-SESSION-T2 -- Phase A/B/C/E driver.

Phase A: tau_b reduction to F + Eisenstein E_4, E_6, Delta, eta evaluation
         on all 50 R1.1 cubic families; cross-check j(tau) vs j_invariant.
Phase B: Spearman correlations of A_fit-deltas with each modular predictor,
         using both R1.1 free-A delta and R1.3 deep-residualised delta.
Phase C: Residual-after-best-Eisenstein-predictor, secondary correlations.
Phase E: verdict + paragraph + AEAL claims.

Phase D (deep WKB + PSLQ at j=0 cell) is a separate script (phase_d_pslq.py).
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import sys
import time
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy import stats

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from t2_helpers.eisenstein import (
    tau_from_j, j_of_tau, eisenstein_q, in_fundamental_domain,
)

R11 = HERE.parent.parent / "2026-05-01" / "PCF2-SESSION-R1.1" / "assembled_data_v2.csv"
R13 = HERE.parent.parent / "2026-05-01" / "PCF2-SESSION-R1.3" / "residualization_d3.csv"

DPS = 200
QN = 200       # q-series truncation; |q| <= exp(-pi*sqrt(3)) ~ 4.3e-3 in F


def log_line(path, msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")


def load_inputs():
    r11 = {}
    with open(R11, newline="") as fh:
        for row in csv.DictReader(fh):
            r11[int(row["family_id"])] = row
    r13 = {}
    with open(R13, newline="") as fh:
        for row in csv.DictReader(fh):
            r13[int(row["family_id"])] = row
    return r11, r13


# -------------------- Phase A --------------------

def phase_A(log):
    log("PHASE A: tau_b reduction + Eisenstein evaluation")
    r11, r13 = load_inputs()
    ids = sorted(set(r11) & set(r13))
    log(f"  {len(ids)} cubic families with both R1.1 and R1.3 records")

    rows = []
    reduction_trace = {}
    j_max_relerr = mp.mpf(0)
    for fid in ids:
        rec = r11[fid]
        j_csv = mp.mpf(rec["j_invariant"])
        tau, branch, niter, res = tau_from_j(j_csv, N=QN, dps=DPS)
        if not in_fundamental_domain(tau):
            raise RuntimeError(
                f"family {fid}: tau_b not in F: {complex(tau)}")
        E4, E6, Delta = eisenstein_q(tau, N=QN)
        # j cross-check
        j_recomputed = (E4 ** 3) / Delta
        relerr = abs(j_recomputed - j_csv) / max(abs(j_csv), mp.mpf(1))
        if relerr > j_max_relerr:
            j_max_relerr = relerr
        if relerr > mp.mpf("1e-6") and abs(j_csv) > mp.mpf("1e-6"):
            log(f"  WARNING fid={fid}: j relerr={float(relerr):.3e}")

        abs_E4 = abs(E4)
        abs_E6 = abs(E6)
        abs_Delta = abs(Delta)
        # Petersson height ||Delta|| = (Im tau)^6 |Delta| * |eta|^? .
        # Standard: ||Delta(tau)|| = (Im tau)^12 |Delta(tau)|^2 (weight 12)
        # The relay prompt asks (Im tau)^6 |eta|^24 which equals
        # (Im tau)^6 |Delta|. Provide both.
        log_abs_Delta_petersson_w6 = float(
            6 * mp.log(tau.imag) + mp.log(abs_Delta))
        log_abs_Delta_petersson_w12 = float(
            12 * mp.log(tau.imag) + 2 * mp.log(abs_Delta))
        log_eta_norm = float(mp.log(tau.imag) / 2 + mp.log(abs_Delta) / 24)

        # j - 1728 (use mp arithmetic to keep precision)
        j_minus_1728 = j_csv - 1728

        rows.append({
            "family_id": fid,
            "alpha_3": int(rec["alpha_3"]),
            "alpha_2": int(rec["alpha_2"]),
            "alpha_1": int(rec["alpha_1"]),
            "alpha_0": int(rec["alpha_0"]),
            "j_invariant": float(j_csv),
            "log_abs_j": float(rec["log_abs_j"]) if rec["log_abs_j"] else float("nan"),
            "tau_re": float(tau.real),
            "tau_im": float(tau.imag),
            "branch": branch,
            "newton_iters": niter,
            "newton_residual": float(abs(res)) if res is not None else 0.0,
            "j_csv_vs_recomputed_relerr": float(relerr),
            "abs_E4": float(abs_E4),
            "log_abs_E4": float(mp.log(abs_E4)) if abs_E4 > 0 else float("-inf"),
            "abs_E6": float(abs_E6),
            "log_abs_E6": float(mp.log(abs_E6)) if abs_E6 > 0 else float("-inf"),
            "abs_Delta": float(abs_Delta),
            "log_abs_Delta_petersson_w6": log_abs_Delta_petersson_w6,
            "log_abs_Delta_petersson_w12": log_abs_Delta_petersson_w12,
            "log_eta_norm": log_eta_norm,
            "log_imtau": float(mp.log(tau.imag)),
            "log_abs_E4_cube": float(3 * mp.log(abs_E4)) if abs_E4 > 0 else float("-inf"),
            "log_abs_j_minus_1728": float(mp.log(abs(j_minus_1728))) if j_minus_1728 != 0 else float("-inf"),
            "delta_R11_free": float(rec["delta"]),
            "A_stderr_R11": float(rec["A_stderr"]),
            "delta_R13_free": float(r13[fid]["delta_R13_free"]),
            "A_stderr_R13": float(r13[fid]["A_stderr_R13_free"]),
            "alpha_fixedA_R13": float(r13[fid]["alpha_fixedA"]),
            "beta_fixedA_R13": float(r13[fid]["beta_fixedA"]),
            "gamma_fixedA_R13": float(r13[fid]["gamma_fixedA"]),
        })
        reduction_trace[fid] = {
            "branch": branch,
            "newton_iters": niter,
            "newton_residual": str(res),
            "tau": [str(tau.real), str(tau.imag)],
            "j_csv_vs_recomputed_relerr": str(relerr),
        }

    # write CSV
    csv_path = HERE / "phase_A_eisenstein_table.csv"
    fieldnames = list(rows[0].keys())
    with open(csv_path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    log(f"  wrote {csv_path.name} ({len(rows)} rows)")

    trace_path = HERE / "phase_A_tau_b_reduction.json"
    with open(trace_path, "w") as fh:
        json.dump({"max_j_relerr": str(j_max_relerr),
                   "n_families": len(rows),
                   "reduction_trace": reduction_trace}, fh, indent=2)
    log(f"  wrote {trace_path.name}; max j relerr = {float(j_max_relerr):.3e}")

    return rows, float(j_max_relerr)


# -------------------- Phase B --------------------

HYPOTHESES = [
    ("H_baseline",       "log_abs_j",                  "R1.1 baseline"),
    ("H_E4",             "log_abs_E4",                 "H2 main mechanism"),
    ("H_Delta_w6",       "log_abs_Delta_petersson_w6", "H2 next-residual (weight 6)"),
    ("H_Delta_w12",      "log_abs_Delta_petersson_w12","H2 next-residual (weight 12)"),
    ("H_E6",             "log_abs_E6",                 "H2 j=1728 probe"),
    ("H_j_minus_1728",   "log_abs_j_minus_1728",       "H2 order-2 elliptic point"),
    ("H_eta",            "log_eta_norm",               "implied by Delta=eta^24"),
    ("H_imtau",          "log_imtau",                  "drift coordinate"),
    ("H_E4_cube",        "log_abs_E4_cube",            "sanity ~ baseline + log Delta"),
    # Heights / class-number rows are sparse: we omit them rather than
    # fabricate placeholders; that drops K from 14 toward 9.  We retain
    # K = 14 in the Bonferroni denominator to match R1.1's stated K and
    # to be conservative (the surviving signals get penalised harder).
]
K_BONF = 14


def spearman(x, y):
    res = stats.spearmanr(x, y, nan_policy="omit")
    return float(res.correlation), float(res.pvalue)


def phase_B(rows, log):
    log("PHASE B: correlation map (R1.1 vs R1.3)")
    table = []
    n = len(rows)
    for hname, col, descr in HYPOTHESES:
        x = np.array([r[col] for r in rows], dtype=float)
        # filter -inf
        mask = np.isfinite(x)
        if not mask.all():
            log(f"  {hname}: dropping {(~mask).sum()} non-finite")
        d11 = np.array([r["delta_R11_free"] for r in rows], dtype=float)
        d13 = np.array([r["delta_R13_free"] for r in rows], dtype=float)
        rho11, p11 = spearman(x[mask], d11[mask])
        rho13, p13 = spearman(x[mask], d13[mask])
        p11_b = min(1.0, p11 * K_BONF)
        p13_b = min(1.0, p13 * K_BONF)
        table.append({
            "hypothesis": hname,
            "predictor": col,
            "description": descr,
            "n": int(mask.sum()),
            "rho_R11": rho11, "p_raw_R11": p11, "p_bonf_R11": p11_b,
            "rho_R13": rho13, "p_raw_R13": p13, "p_bonf_R13": p13_b,
        })
        log(f"  {hname:18s} rho_R11={rho11:+.3f} (Bonf p={p11_b:.2e})  "
            f"rho_R13={rho13:+.3f} (Bonf p={p13_b:.2e})")

    # write JSON + LaTeX
    json_path = HERE / "phase_B_correlation_table.json"
    with open(json_path, "w") as fh:
        json.dump({"K_bonferroni": K_BONF, "n_families": n, "table": table},
                  fh, indent=2)

    tex_lines = []
    tex_lines.append("% phase_B_correlation_table.tex --- generated by t2_main.py")
    tex_lines.append("\\begin{tabular}{lrrrrrrr}")
    tex_lines.append("\\hline")
    tex_lines.append("Hypothesis & Predictor & $n$ & $\\rho_{\\rm R1.1}$ & "
                     "$p_{\\rm Bonf}^{\\rm R1.1}$ & $\\rho_{\\rm R1.3}$ & "
                     "$p_{\\rm Bonf}^{\\rm R1.3}$ \\\\")
    tex_lines.append("\\hline")
    for t in table:
        pred = t["predictor"].replace("_", "\\_")
        tex_lines.append(
            f"{t['hypothesis'].replace('_', '\\_')} & "
            f"\\texttt{{{pred}}} & {t['n']} & "
            f"{t['rho_R11']:+.3f} & {t['p_bonf_R11']:.2e} & "
            f"{t['rho_R13']:+.3f} & {t['p_bonf_R13']:.2e} \\\\")
    tex_lines.append("\\hline")
    tex_lines.append("\\end{tabular}")
    tex_path = HERE / "phase_B_correlation_table.tex"
    with open(tex_path, "w") as fh:
        fh.write("\n".join(tex_lines) + "\n")
    log(f"  wrote {json_path.name} and {tex_path.name}")
    return table


# -------------------- Phase C --------------------

def phase_C(rows, table, log):
    log("PHASE C: residual after best-Eisenstein predictor")

    # Choose 'winner' among Eisenstein-grounded predictors as the predictor
    # with smallest p_bonf_R13 (deep-precision delta) restricted to E4-
    # related coordinates.
    eisenstein_keys = {"H_E4", "H_Delta_w6", "H_Delta_w12", "H_eta", "H_E4_cube"}
    cand = [t for t in table if t["hypothesis"] in eisenstein_keys
            and math.isfinite(t["rho_R13"])]
    cand.sort(key=lambda t: t["p_bonf_R13"])
    winner = cand[0]
    log(f"  winner = {winner['hypothesis']} ({winner['predictor']}) "
        f"rho_R13={winner['rho_R13']:+.3f} p_bonf={winner['p_bonf_R13']:.2e}")

    # Compare to bare baseline
    baseline = next(t for t in table if t["hypothesis"] == "H_baseline")
    log(f"  baseline H_baseline rho_R13={baseline['rho_R13']:+.3f} "
        f"p_bonf={baseline['p_bonf_R13']:.2e}")

    e4_beats_baseline = (winner["p_bonf_R13"] <= baseline["p_bonf_R13"])
    log(f"  E4-grounded predictor beats baseline at deep precision? "
        f"{e4_beats_baseline}")

    # OLS fit delta_R13 = c0 + c1 * predictor
    pred_col = winner["predictor"]
    x = np.array([r[pred_col] for r in rows], dtype=float)
    y = np.array([r["delta_R13_free"] for r in rows], dtype=float)
    finite = np.isfinite(x) & np.isfinite(y)
    x = x[finite]; y = y[finite]
    X = np.column_stack([np.ones_like(x), x])
    sol, *_ = np.linalg.lstsq(X, y, rcond=None)
    c0, c1 = (float(s) for s in sol)
    yhat = X @ sol
    resid = y - yhat
    log(f"  OLS  delta = {c0:+.4e} + ({c1:+.4e}) * {pred_col}")
    log(f"  RMS resid = {float(resid.std(ddof=1)):.4e}")

    # Secondary correlations on resid against Petersson, j-1728, E6, eta
    secondary = []
    for col in ("log_abs_Delta_petersson_w6", "log_abs_Delta_petersson_w12",
                "log_abs_j_minus_1728", "log_abs_E6", "log_eta_norm",
                "log_imtau"):
        z = np.array([r[col] for r in rows], dtype=float)[finite]
        m = np.isfinite(z)
        rho, p = spearman(z[m], resid[m])
        p_b = min(1.0, p * 4)  # K=4 secondary tests
        secondary.append({"predictor": col, "rho": rho, "p_raw": p,
                          "p_bonf_K4": p_b, "n": int(m.sum())})
        log(f"  resid vs {col}: rho={rho:+.3f} p_bonf(K=4)={p_b:.2e}")

    # Save
    out = {
        "winner_hypothesis": winner["hypothesis"],
        "winner_predictor": pred_col,
        "winner_metrics_R13": {"rho": winner["rho_R13"],
                               "p_bonf": winner["p_bonf_R13"]},
        "baseline_metrics_R13": {"rho": baseline["rho_R13"],
                                 "p_bonf": baseline["p_bonf_R13"]},
        "e4_beats_baseline": e4_beats_baseline,
        "ols_fit": {"c0": c0, "c1": c1, "resid_std": float(resid.std(ddof=1)),
                    "resid_mean": float(resid.mean())},
        "secondary_correlations": secondary,
    }
    json_path = HERE / "phase_C_residual.json"
    with open(json_path, "w") as fh:
        json.dump(out, fh, indent=2)
    log(f"  wrote {json_path.name}")

    # diagnostics PNG
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, axs = plt.subplots(2, 2, figsize=(11, 9))
        axs[0,0].scatter(x, y, s=18); axs[0,0].plot(np.sort(x),
            c0 + c1*np.sort(x), "r-", lw=1)
        axs[0,0].set_xlabel(pred_col); axs[0,0].set_ylabel("delta_R13_free")
        axs[0,0].set_title(f"OLS fit (winner={winner['hypothesis']})")
        for ax, col in zip([axs[0,1], axs[1,0], axs[1,1]],
                           ["log_abs_Delta_petersson_w6",
                            "log_abs_j_minus_1728", "log_abs_E6"]):
            z = np.array([r[col] for r in rows], dtype=float)[finite]
            m = np.isfinite(z)
            ax.scatter(z[m], resid[m], s=14)
            ax.axhline(0, color="grey", lw=0.5)
            ax.set_xlabel(col); ax.set_ylabel("residual")
        plt.tight_layout()
        png = HERE / "phase_C_diagnostics.png"
        plt.savefig(png, dpi=110)
        plt.close()
        log(f"  wrote {png.name}")
    except Exception as e:
        log(f"  WARN: png skipped ({e})")

    return out, winner, baseline, e4_beats_baseline


# -------------------- main --------------------

def main():
    LOG = HERE / "t2_main.log"
    if LOG.exists():
        LOG.unlink()
    def log(m): log_line(LOG, m)

    t0 = time.time()
    rows, j_relerr_max = phase_A(log)
    table = phase_B(rows, log)
    cres, winner, baseline, beats = phase_C(rows, table, log)
    log(f"DONE Phase A/B/C in {time.time()-t0:.1f}s")

    # write a small summary
    summary = {
        "n_families": len(rows),
        "phase_A": {"max_j_relerr": j_relerr_max},
        "phase_B_top_R13": sorted(
            [(t["hypothesis"], t["rho_R13"], t["p_bonf_R13"]) for t in table],
            key=lambda x: x[2])[:5],
        "phase_C": {"winner": winner["hypothesis"],
                    "winner_predictor": winner["predictor"],
                    "e4_beats_baseline": beats,
                    "winner_p_bonf": winner["p_bonf_R13"],
                    "baseline_p_bonf": baseline["p_bonf_R13"]},
    }
    with open(HERE / "phase_ABC_summary.json", "w") as fh:
        json.dump(summary, fh, indent=2)
    log(f"summary -> phase_ABC_summary.json")


if __name__ == "__main__":
    main()
