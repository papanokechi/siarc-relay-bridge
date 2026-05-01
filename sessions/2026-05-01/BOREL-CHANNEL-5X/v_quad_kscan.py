"""V_quad K-extension: scan K, M_pade to test whether the Painleve fit
residual scales with truncation order (real signal) or stays at ~1e-3
(Pade-truncation noise).  If real, residual should drop substantially
as K, M grow."""
import json, sys
from pathlib import Path
from mpmath import mpf
sys.path.insert(0, str(Path(__file__).resolve().parent))
from borel_channel import borel_probe

def a_fn(n):  return mpf(1)
def b_fn(n):  return mpf(3)*n*n + n + mpf(1)

spec_vq = {"family": "V_quad", "recurrence": {"a_n": "1", "b_n": "3 n^2 + n + 1"},
           "Delta": -11, "CM_field": "Q(sqrt(-11))", "Heegner": True,
           "a_fn": a_fn, "b_fn": b_fn}

if __name__ == "__main__":
    grid = [
        # (depth, dps, K, M, n_lo, n_hi)
        (200, 2200, 12, 5,  15, 120),
        (240, 3000, 16, 7,  15, 150),
        (280, 4000, 20, 9,  15, 170),
        (320, 5000, 24, 11, 15, 190),
    ]
    summary = []
    for (depth, dps, K, M, n_lo, n_hi) in grid:
        print("\n" + "#"*80)
        print(f"# K={K}, M={M}, depth={depth}, dps={dps}, n=[{n_lo},{n_hi}]")
        print("#"*80)
        res = borel_probe(spec_vq, depth=depth, dps=dps, K=K, M_pade=M,
                          n_lo=n_lo, n_hi=n_hi)
        bc = res.get("best_cell", {})
        summary.append({
            "K": K, "M": M, "depth": depth, "dps": dps,
            "best_eq": bc.get("equation"),
            "residual": bc.get("residual"),
            "params": bc.get("params"),
            "ts_residual": res.get("trans_series", {}).get("residual_max_log_delta"),
            "rho_star_re": res.get("rho_star", {}).get("re"),
            "rho_star_im": res.get("rho_star", {}).get("im"),
            "rho_star_abs": res.get("rho_star", {}).get("abs"),
        })
    out = Path(__file__).parent / "vquad_kscan.json"
    with open(out, "w") as f: json.dump(summary, f, indent=2)
    print(f"\nWrote {out}")
    print("\nK-scan summary (V_quad):")
    print(f"{'K':>3} {'M':>3} {'depth':>5} {'dps':>5} {'best_eq':>7} {'residual':>14} "
          f"{'rho_star_abs':>16}")
    for r in summary:
        print(f"{r['K']:>3} {r['M']:>3} {r['depth']:>5} {r['dps']:>5} "
              f"{r['best_eq']:>7} {r['residual']:>14} {r['rho_star_abs']:>16}")
