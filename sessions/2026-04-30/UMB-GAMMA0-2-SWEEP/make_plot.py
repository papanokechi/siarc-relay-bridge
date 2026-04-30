"""Cross-group plot: Trans rate vs predicted ratio."""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).parent
data = json.loads((OUT / "results.json").read_text())
rates = data["rates_by_group"]

groups = ["Gamma0(2)", "G_4", "G_5", "G_6", "G_8"]
xs, ys, conv, total = [], [], [], []
labels = []
for g in groups:
    r = rates[g]
    rho = float(eval(r["predicted_ratio"]))  # Fraction str like "-3/16"
    xs.append(rho)
    ys.append(r["trans"])
    conv.append(r["convergent"])
    total.append(r["total"])
    labels.append(f"{g}\nrho={r['predicted_ratio']}\nconv={r['convergent']}")

fig, ax = plt.subplots(figsize=(9, 5))
ax.scatter(xs, ys, s=120, c="crimson", edgecolor="black", zorder=3)
for x, y, lab in zip(xs, ys, labels):
    ax.annotate(lab, (x, y), textcoords="offset points",
                xytext=(8, 8), fontsize=8)
ax.axhline(0, color="gray", lw=0.5)
ax.set_xlabel("Predicted ratio rho = -m(b-m)/b^2")
ax.set_ylabel("Trans count (deep-validated)")
ax.set_title("UMB-GAMMA0-2-SWEEP: Trans rate vs predicted ratio "
             "across non-PSL2(Z) groups\n"
             "(0 Trans at every predicted ratio; HALT_A triggered)")
ax.set_ylim(-0.5, max(1.5, max(ys) + 0.5))
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(OUT / "trans_rate_vs_ratio.png", dpi=140)
print("Wrote trans_rate_vs_ratio.png")

# bar chart of convergent counts vs trans count
fig, ax = plt.subplots(figsize=(9, 5))
import numpy as np
idx = np.arange(len(groups))
width = 0.35
ax.bar(idx - width/2, conv, width, label="convergent", color="steelblue")
ax.bar(idx + width/2, ys, width, label="Trans", color="crimson")
ax.set_xticks(idx)
ax.set_xticklabels([f"{g}\n{rates[g]['predicted_ratio']}" for g in groups])
ax.set_ylabel("Family count")
ax.set_title("UMB-GAMMA0-2-SWEEP: convergent vs Trans per group")
ax.legend()
ax.set_yscale("symlog")
plt.tight_layout()
plt.savefig(OUT / "group_summary.png", dpi=140)
print("Wrote group_summary.png")
