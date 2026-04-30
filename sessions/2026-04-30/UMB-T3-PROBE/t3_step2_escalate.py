"""UMB-T3-PROBE  --  step 2: curate top-5 + dps=3000 escalation + plot.

Pulls full results from t3_probe_full.json, picks 5 diverse candidates
(R1 + 3 trans_hard + 1 irr_482), re-computes their limits at dps=3000
and re-runs the 5-tier strong PSLQ + weak PSLQ probe.  Records final
mu_slope at the extended dps grid {500, 1000, 1500, 3000} and emits
mu_slope_plot.png.
"""
from __future__ import annotations
import json, math, time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp

import t3_probe as tp  # local module

HERE = Path(__file__).resolve().parent

FULL = json.loads((HERE / "t3_probe_full.json").read_text(encoding="utf-8"))
results = FULL["results"]


def find(idstr):
    for r in results:
        if r["id"] == idstr:
            return r
    raise KeyError(idstr)


# Hand-picked diverse top-5 (with rationale per relay prompt §5)
PICKS = [
    "T2A_R1",                                    # the named R1 (deg 4,2)
    "TH_a1_-1_-1_-1_-1_b-1_-1_-1",               # smallest |L| trans_hard, a-shape A
    "TH_a1_-1_-1_-1_-1_b-1_0_1",                 # alt b, same a-shape A
    "TH_a1_-1_-1_-1_0_b-1_-1_-1",                # alt a-shape B
    "IRR482_277",                                # strongest 482 NULL
]

EXT_DPS = 3000

def escalate(rec):
    """Re-run the family at dps=3000 and append a probe point."""
    a = rec["a"]; b = rec["b"]
    print(f"\n[escalate {rec['id']}]  a={a}  b={b}", flush=True)
    t0 = time.time()
    L = tp.pcf_limit(a, b, EXT_DPS)
    L = mp.mpf(str(L))
    print(f"  dps={EXT_DPS}  L={mp.nstr(L, 30)}  ({time.time()-t0:.1f}s)", flush=True)

    mp.mp.dps = EXT_DPS + 60
    tiers_ext = tp.build_tiers(EXT_DPS)
    # 5-tier strong PSLQ
    tier_results_ext = []
    for tname, basis in tiers_ext:
        rel, res, names, mxc = tp.pslq_probe(L, basis, EXT_DPS)
        tier_results_ext.append({
            "tier": tname, "basis_size": len(basis),
            "hit": rel is not None,
            "relation": [int(x) for x in rel] if rel else None,
            "residual_log10": math.log10(res) if res > 0 else -10000,
            "max_coef": mxc,
        })
        print(f"  {tname}  hit={rel is not None}  res=10^{tier_results_ext[-1]['residual_log10']:.1f}", flush=True)
    # weak PSLQ at extended dps
    _, res_w, mxc_w = tp.pslq_probe_weak(L, tiers_ext[-1][1], EXT_DPS)
    weak_pt = {
        "dps": EXT_DPS,
        "log10_res": math.log10(res_w) if res_w > 0 else -10000,
        "log10_max_coef": math.log10(mxc_w) if mxc_w and mxc_w > 0 else 0,
    }
    print(f"  weak dps={EXT_DPS}  log10|res|={weak_pt['log10_res']:.2f}  log10(max_coef)={weak_pt['log10_max_coef']:.2f}", flush=True)

    rec_ext = dict(rec)
    rec_ext["L_dps_ext"] = {EXT_DPS: mp.nstr(L, 80)}
    rec_ext["tiers_ext_dps3000"] = tier_results_ext
    rec_ext["mu_probe_ext"] = list(rec.get("mu_probe", [])) + [weak_pt]
    rec_ext["all_null_ext"] = all(not t["hit"] for t in tier_results_ext)
    return rec_ext


def main():
    t0 = time.time()
    picks = [find(p) for p in PICKS]
    extended = []
    for p in picks:
        ext = escalate(p)
        extended.append(ext)

    out = {
        "task": "UMB-T3-PROBE-step2",
        "dps_extended": EXT_DPS,
        "n_candidates": len(extended),
        "candidates": extended,
        "elapsed_sec": round(time.time() - t0, 1),
    }
    (HERE / "t3_candidates.json").write_text(
        json.dumps(out, indent=2), encoding="utf-8")

    # mu_slope plot: log10|residual| AND log10(max_coef) vs dps for each
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    for ext in extended:
        pts = ext["mu_probe_ext"]
        xs = [p["dps"] for p in pts]
        ys_r = [p["log10_res"] for p in pts]
        ys_c = [p["log10_max_coef"] for p in pts]
        label = ext["id"]
        axes[0].plot(xs, ys_r, "o-", label=label)
        axes[1].plot(xs, ys_c, "o-", label=label)
    axes[0].set_xlabel("dps"); axes[0].set_ylabel("log10 |residual| (weak PSLQ, T5)")
    axes[0].set_title("Residual decay vs dps")
    axes[0].grid(alpha=0.3); axes[0].legend(fontsize=7, loc="best")
    axes[1].set_xlabel("dps"); axes[1].set_ylabel("log10 max|coef|")
    axes[1].set_title("PSLQ coef magnitude growth (mu-coef)")
    axes[1].grid(alpha=0.3); axes[1].legend(fontsize=7, loc="best")
    fig.suptitle(f"UMB-T3-PROBE  --  T3 candidates, dps in [500, 1000, 1500, {EXT_DPS}]")
    fig.tight_layout()
    plot_path = HERE / "mu_slope_plot.png"
    fig.savefig(plot_path, dpi=140)
    print(f"\nWrote {plot_path}")

    # Summary
    n_persist = sum(1 for e in extended if e["all_null_ext"])
    print(f"\n=== STEP-2 SUMMARY ===")
    print(f"Candidates escalated to dps={EXT_DPS}: {len(extended)}")
    print(f"All-NULL persists at dps={EXT_DPS}    : {n_persist}/{len(extended)}")
    print(f"Elapsed (step 2): {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
