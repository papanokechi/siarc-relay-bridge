"""Post-hoc trimmed-grid ORDERING diagnostic.

The full 216-grid half-range envelope is dominated by K_lead=120
configurations where cond(A) ~ 10^120 and Stage 1 alpha_k for high
k carries numerical noise of order |alpha_k| * cond * 10^-300.
The mantissa noise is harmless inside the W1=[2500,4900] training
window but blows up when extrapolating to small n.

This script re-runs the aggregation restricted to K_lead in
{60, 70, 80, 90} (excluding 100 and 120) and reports the trimmed
ORDERING test.

Output: trimmed_ordering.json
"""
from __future__ import annotations

import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 300

HERE = Path(__file__).resolve().parent
SIDE = {"V_quad": "neg", "QL15": "neg", "QL05": "pos", "QL09": "pos"}
REP_NAMES = ["V_quad", "QL15", "QL05", "QL09"]


def median_halfrange(vals):
    if not vals:
        return None, None
    s = sorted(vals, key=lambda x: float(x))
    n = len(s)
    med = s[n // 2] if n % 2 == 1 else (s[n // 2 - 1] + s[n // 2]) / 2
    hr = (s[-1] - s[0]) / 2
    return med, hr


def main():
    with (HERE / "stability_grid_extended.json").open("r") as fh:
        grid = json.load(fh)

    K_KEEP = {60, 70, 80, 90}

    out = {"K_lead_kept": sorted(K_KEEP), "per_rep": {}}
    a1_by_rep = {}
    for rid in REP_NAMES:
        configs = grid[rid]["configs"]
        kept = [c for c in configs if "error" not in c
                and c.get("K_lead") in K_KEEP and c.get("a_1") is not None]
        a1s = [mp.mpf(c["a_1"]) for c in kept]
        Cs = [mp.mpf(c["C"]) for c in kept]
        Ds = [mp.mpf(c["D"]) for c in kept]
        a1_med, a1_hr = median_halfrange(a1s)
        C_med, C_hr = median_halfrange(Cs)
        D_med, D_hr = median_halfrange(Ds)
        out["per_rep"][rid] = {
            "kept_count": len(kept),
            "a_1_median": mp.nstr(a1_med, 50),
            "a_1_half_range": mp.nstr(a1_hr, 30),
            "a_1_rel_half_range": mp.nstr(a1_hr / max(abs(a1_med), mp.mpf(1)), 10),
            "C_median": mp.nstr(C_med, 50),
            "C_rel_half_range": mp.nstr(C_hr / max(abs(C_med), mp.mpf(1)), 10),
            "D_median": mp.nstr(D_med, 30),
            "D_rel_half_range": mp.nstr(D_hr / max(abs(D_med), mp.mpf(1)), 10),
        }
        a1_by_rep[rid] = (a1_med, a1_hr)

    # ORDERING test (4-rep + 3-rep) on trimmed grid
    def ordering(reps):
        neg = [(r, *a1_by_rep[r]) for r in reps if SIDE[r] == "neg"]
        pos = [(r, *a1_by_rep[r]) for r in reps if SIDE[r] == "pos"]
        neg_max_med = max(n[1] for n in neg)
        neg_max_env = max(n[2] for n in neg)
        pos_min_med = min(p[1] for p in pos)
        pos_min_env = max(p[2] for p in pos)
        neg_upper = neg_max_med + neg_max_env
        pos_lower = pos_min_med - pos_min_env
        return {
            "passes": bool(neg_upper < pos_lower),
            "neg_upper": mp.nstr(neg_upper, 30),
            "pos_lower": mp.nstr(pos_lower, 30),
            "gap": mp.nstr(pos_lower - neg_upper, 30),
        }

    out["ordering_4rep"] = ordering(REP_NAMES)
    out["ordering_3rep_exclude_QL09"] = ordering([r for r in REP_NAMES if r != "QL09"])

    with (HERE / "trimmed_ordering.json").open("w") as fh:
        json.dump(out, fh, indent=2)
    print(json.dumps({"4rep": out["ordering_4rep"],
                      "3rep": out["ordering_3rep_exclude_QL09"],
                      "per_rep_a1_rel_half_range":
                          {r: out["per_rep"][r]["a_1_rel_half_range"] for r in REP_NAMES}},
                     indent=2))


if __name__ == "__main__":
    main()
