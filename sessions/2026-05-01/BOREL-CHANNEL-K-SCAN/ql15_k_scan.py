"""QL15 K-extension scan: scan (K, M_pade, depth, dps) at the same
grid as the V_quad K-scan in BOREL-CHANNEL-5X to determine whether
the K=12 marginal P-V hit (residual 9.08e-5) is a genuine
Borel-channel Painleve reduction or a Pade-truncation artefact.

Family: a_n = n, b_n = 3 n^2 - 2 n + 2, Delta = -20, Q(sqrt(-5)).

Uses borel_channel.py from BOREL-CHANNEL-5X verbatim.
"""
import json
import sys
import time
from pathlib import Path

from mpmath import mp, mpf

# Reuse the v3 pipeline from the parent session.
PARENT = Path(__file__).resolve().parent.parent / "BOREL-CHANNEL-5X"
sys.path.insert(0, str(PARENT))
from borel_channel import borel_probe  # type: ignore  # noqa: E402


def a_fn(n):
    return n


def b_fn(n):
    return mpf(3) * n * n - mpf(2) * n + mpf(2)


SPEC = {
    "family": "QL15",
    "recurrence": {"a_n": "n", "b_n": "3 n^2 - 2 n + 2"},
    "Delta": -20,
    "CM_field": "Q(sqrt(-5))",
    "Heegner": False,
    "a_fn": a_fn,
    "b_fn": b_fn,
}


GRID = [
    # (depth, dps, K, M_pade, n_lo, n_hi)
    (200, 2200, 12, 5, 15, 120),
    (240, 3000, 16, 7, 15, 150),
    (280, 4000, 20, 9, 15, 170),
    (320, 5000, 24, 11, 15, 190),
]


def main():
    summary = []
    t_total = time.time()
    for depth, dps, K, M, n_lo, n_hi in GRID:
        print("\n" + "#" * 80)
        print(f"# QL15  K={K}, M={M}, depth={depth}, dps={dps}, n=[{n_lo},{n_hi}]")
        print("#" * 80)
        t0 = time.time()
        res = borel_probe(SPEC, depth=depth, dps=dps, K=K, M_pade=M,
                          n_lo=n_lo, n_hi=n_hi)
        elapsed = time.time() - t0
        bc = res.get("best_cell", {})
        rho = res.get("rho_star", {})
        ts = res.get("trans_series", {})
        summary.append({
            "K": K,
            "M": M,
            "depth": depth,
            "dps": dps,
            "best_eq": bc.get("equation"),
            "residual": bc.get("residual"),
            "params": bc.get("params"),
            "ts_residual": ts.get("residual_max_log_delta"),
            "A_obs": ts.get("A"),
            "alpha_obs": ts.get("alpha"),
            "rho_star_re": rho.get("re"),
            "rho_star_im": rho.get("im"),
            "rho_star_abs": rho.get("abs"),
            "verdict_K": res.get("verdict"),
            "elapsed_s": round(elapsed, 1),
        })

    # h cross-check at K=24 (h in {0.1, 0.05, 0.025} are already inside
    # borel_probe; record fit_results for the K=24 cell to confirm
    # h-independence of the design-block step size).
    print("\n" + "#" * 80)
    print("# QL15  h cross-check at K=24 (re-run, capture full fit_results)")
    print("#" * 80)
    res_h = borel_probe(SPEC, depth=320, dps=5000, K=24, M_pade=11,
                        n_lo=15, n_hi=190)
    h_cross = {h: {eq: row[eq]["residual_validate"]
                   for eq in row if isinstance(row, dict) and eq in row
                   and "residual_validate" in row[eq]}
               for h, row in res_h.get("fit_results", {}).items()
               if isinstance(row, dict) and "error" not in row}

    out = Path(__file__).parent / "ql15_k_scan.json"
    with open(out, "w") as f:
        json.dump({"family": "QL15", "grid": summary,
                   "h_cross_check_K24": h_cross,
                   "total_elapsed_s": round(time.time() - t_total, 1)},
                  f, indent=2)
    print(f"\nWrote {out}")

    print("\nK-scan summary (QL15):")
    print(f"{'K':>3} {'M':>3} {'depth':>5} {'dps':>5} {'best_eq':>7} "
          f"{'residual':>14} {'rho_star_abs':>16} {'verdict':>10}")
    for r in summary:
        print(f"{r['K']:>3} {r['M']:>3} {r['depth']:>5} {r['dps']:>5} "
              f"{str(r['best_eq']):>7} {str(r['residual']):>14} "
              f"{str(r['rho_star_abs']):>16} {str(r['verdict_K']):>10}")


if __name__ == "__main__":
    main()
