from __future__ import annotations

import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np

mp.mp.dps = 80
ROOT = Path(__file__).resolve().parent
csv_path = ROOT.parent / "PCF2-SESSION-R1.3" / "residualization_d3.csv"
rows = []
with csv_path.open(newline="", encoding="utf-8") as handle:
    for row in csv.DictReader(handle):
        rows.append({
            "family_id": int(row["family_id"]),
            "x": float(mp.mpf(row["log_abs_j"])),
            "y": float(mp.mpf(row["delta_R13_free"])),
        })

x = np.array([r["x"] for r in rows], dtype=float)
y = np.array([r["y"] for r in rows], dtype=float)
family_ids = np.array([r["family_id"] for r in rows], dtype=int)

# R1.3 visual K-set: fourteen smallest absolute leading-exponent residuals.
k_ids = set(family_ids[np.argsort(np.abs(y))[:14]])
j0_ids = set(family_ids[np.isclose(x, 0.0)])

fig, ax = plt.subplots(figsize=(6.2, 4.1), dpi=180)
ax.scatter(x, y, s=34, c="#9a9a9a", edgecolors="white", linewidths=0.5, label="50 cubic families")
mask_k = np.array([fid in k_ids for fid in family_ids])
ax.scatter(x[mask_k], y[mask_k], s=62, c="#f2c94c", edgecolors="black", linewidths=0.6, label="14-family R1.3 K-set")
mask_j0 = np.array([fid in j0_ids for fid in family_ids])
ax.scatter(x[mask_j0], y[mask_j0], s=150, facecolors="none", edgecolors="#d62728", linewidths=1.6, label="j=0 CM cell")

coef = np.polyfit(x, y, 1)
xline = np.linspace(float(x.min()), float(x.max()), 200)
yline = coef[0] * xline + coef[1]
ax.plot(xline, yline, "--", color="#1f77b4", linewidth=1.4, label="Spearman-rank trend guide")

for fid, xi, yi in zip(family_ids, x, y):
    if fid in j0_ids:
        ax.annotate(str(fid), (xi, yi), xytext=(4, 4), textcoords="offset points", fontsize=7, color="#a00000")

ax.axhline(0.0, color="black", linewidth=0.6, alpha=0.45)
ax.set_xlabel("log(|j(E_b)|+1)")
ax.set_ylabel("A_fit - 6")
ax.set_title("d=3 cubic catalogue: rho=-0.5683, Bonferroni p=5.0e-5", fontsize=10)
ax.grid(True, alpha=0.18, linewidth=0.5)
ax.legend(frameon=False, fontsize=8, loc="lower left")
fig.tight_layout()
fig.savefig(ROOT / "j_scatter.png")
