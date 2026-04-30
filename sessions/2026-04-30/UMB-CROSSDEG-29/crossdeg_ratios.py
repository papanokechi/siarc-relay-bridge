"""UMB-CROSSDEG-29 Step 1-3: leading-ratio histogram across T2A deg-(4,2) Trans census.

Coefficient ordering convention (project-wide): leading-first.
  coeffs_a = [a4, a3, a2, a1, a0]
  coeffs_b = [b2, b1, b0]

Leading ratio (deg-(4,2) generalisation of -2/9):  R1 = a4 / b2^2.
Sub-leading ratio (analogue of -1/36 etc.):        R2 = a2 / b1^2  (b1!=0).

We test concentration at -2/9 and at simple rational multiples
{-2/9, -1/9, -4/9, -2/9 * 1/4 = -1/18, +1/4 (Class B), -1/36, 0}.

Outputs:
  ratios.jsonl              one record per Trans candidate (R1, R2, key)
  concentration_table.json  exact-rational counts at flagged ratios
  ratio_histogram_T2A.png   2x1 histograms of R1 and R2
  ratio_topR1.json / ratio_topR2.json  top-3 concentrations (ties broken
    by closeness to flagged ratios)
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CENSUS = ROOT / "t2a_cmax2_results.json"

FLAGGED = {
    "-2/9": Fraction(-2, 9),
    "-1/9": Fraction(-1, 9),
    "-4/9": Fraction(-4, 9),
    "-1/18": Fraction(-1, 18),  # -2/9 * 1/4
    "-1/36": Fraction(-1, 36),  # T2B Log family
    "+1/4": Fraction(1, 4),
    "-1/4": Fraction(-1, 4),
    "0": Fraction(0, 1),
}


def main() -> int:
    print(f"[load] {CENSUS}")
    with CENSUS.open("r", encoding="utf-8") as fh:
        records = json.load(fh)["results"]
    trans = [r for r in records if r["classification"] == "Trans-candidate"]
    print(f"[filter] Trans-candidate count: {len(trans)}")

    # Compute exact rationals.
    out_path = HERE / "ratios.jsonl"
    cnt_R1 = Counter()
    cnt_R2 = Counter()
    cnt_R2_defined = 0
    with out_path.open("w", encoding="utf-8") as fh:
        for rec in trans:
            a = rec["coeffs_a"]
            b = rec["coeffs_b"]
            a4, a2 = int(a[0]), int(a[2])
            b2, b1 = int(b[0]), int(b[1])
            R1 = Fraction(a4, b2 * b2)  # b2!=0 by construction (deg-4,2)
            cnt_R1[R1] += 1
            R2 = None
            if b1 != 0:
                R2 = Fraction(a2, b1 * b1)
                cnt_R2[R2] += 1
                cnt_R2_defined += 1
            fh.write(
                json.dumps(
                    {
                        "a": a,
                        "b": b,
                        "R1_num": R1.numerator,
                        "R1_den": R1.denominator,
                        "R2_num": R2.numerator if R2 is not None else None,
                        "R2_den": R2.denominator if R2 is not None else None,
                        "limit": rec["limit"],
                    }
                )
                + "\n"
            )
    print(f"[write] {out_path}  ({len(trans)} records)")
    print(f"[stats] R2 defined for {cnt_R2_defined} / {len(trans)}")

    # Concentration table.
    conc = {
        "total_trans": len(trans),
        "R2_defined": cnt_R2_defined,
        "flagged_R1": {},
        "flagged_R2": {},
        "top_R1": [],
        "top_R2": [],
    }
    for label, q in FLAGGED.items():
        conc["flagged_R1"][label] = cnt_R1.get(q, 0)
        conc["flagged_R2"][label] = cnt_R2.get(q, 0)

    # Top-K (excluding nothing; values are exact rationals).
    top_R1 = cnt_R1.most_common(20)
    top_R2 = cnt_R2.most_common(20)
    conc["top_R1"] = [
        {"value": f"{q.numerator}/{q.denominator}", "count": c} for q, c in top_R1
    ]
    conc["top_R2"] = [
        {"value": f"{q.numerator}/{q.denominator}", "count": c} for q, c in top_R2
    ]

    # Distinct ratio counts.
    conc["distinct_R1"] = len(cnt_R1)
    conc["distinct_R2"] = len(cnt_R2)

    with (HERE / "concentration_table.json").open("w", encoding="utf-8") as fh:
        json.dump(conc, fh, indent=2)
    print("[write] concentration_table.json")
    print(json.dumps(conc, indent=2))

    # Histograms (clip to a numerically reasonable range; report clipped tails).
    def _to_float_clipped(c, lo, hi):
        xs = []
        clipped = 0
        for q, cnt in c.items():
            v = float(q)
            if v < lo or v > hi:
                clipped += cnt
                continue
            xs.extend([v] * cnt)
        return xs, clipped

    LO, HI = -1.5, 1.5
    xs1, clip1 = _to_float_clipped(cnt_R1, LO, HI)
    xs2, clip2 = _to_float_clipped(cnt_R2, LO, HI)

    fig, axes = plt.subplots(2, 1, figsize=(10, 8))
    axes[0].hist(xs1, bins=300, color="#1f77b4")
    axes[0].set_title(
        f"T2A Trans (n={len(trans)}): R1 = a4 / b2^2  (clipped {clip1} outside [{LO},{HI}])"
    )
    for label, q in FLAGGED.items():
        axes[0].axvline(float(q), linestyle="--", linewidth=0.8, alpha=0.6, color="r")
        axes[0].text(
            float(q),
            axes[0].get_ylim()[1] * 0.95,
            label,
            rotation=90,
            fontsize=7,
            color="r",
            va="top",
        )
    axes[0].set_xlabel("R1")
    axes[0].set_ylabel("count")

    axes[1].hist(xs2, bins=300, color="#2ca02c")
    axes[1].set_title(
        f"T2A Trans (R2 defined n={cnt_R2_defined}): R2 = a2 / b1^2  (clipped {clip2} outside [{LO},{HI}])"
    )
    for label, q in FLAGGED.items():
        axes[1].axvline(float(q), linestyle="--", linewidth=0.8, alpha=0.6, color="r")
        axes[1].text(
            float(q),
            axes[1].get_ylim()[1] * 0.95,
            label,
            rotation=90,
            fontsize=7,
            color="r",
            va="top",
        )
    axes[1].set_xlabel("R2")
    axes[1].set_ylabel("count")

    fig.tight_layout()
    out_png = HERE / "ratio_histogram_T2A.png"
    fig.savefig(out_png, dpi=140)
    print(f"[write] {out_png}")

    # Top-3 picks per ratio: pick simple rationals with biggest counts AND
    # also dump a small candidate subset (one per flagged ratio if present).
    picks = {"R1": [], "R2": []}
    seen = set()
    for q, c in top_R1:
        if c < 100:
            break
        picks["R1"].append({"value": f"{q.numerator}/{q.denominator}", "count": c})
        if len(picks["R1"]) == 3:
            break
    for q, c in top_R2:
        if c < 100:
            break
        picks["R2"].append({"value": f"{q.numerator}/{q.denominator}", "count": c})
        if len(picks["R2"]) == 3:
            break
    with (HERE / "top3_picks.json").open("w", encoding="utf-8") as fh:
        json.dump(picks, fh, indent=2)
    print(f"[write] top3_picks.json -> {picks}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
