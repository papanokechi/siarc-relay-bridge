"""Generate trans_rate_vs_b1.png (log-log) from CSV."""
import csv
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).parent
rows = []
with (OUT / "trans_rate_vs_b1.csv").open() as f:
    rdr = csv.DictReader(f)
    for r in rdr:
        rows.append(r)

b = [int(r["b1_pos"]) for r in rows]
conv = [int(r["convergent"]) for r in rows]
trans = [int(r["trans"]) for r in rows]
# log-log can't show 0; plot trans_rate as 1/N upper-bound (Wilson-style 0 marker)
# We plot two series: convergent count vs b1 and trans count vs b1.
fig, ax = plt.subplots(1, 2, figsize=(11, 4.5))

ax[0].loglog(b, [c if c > 0 else 0.5 for c in conv], "o-", label="convergent")
ax[0].set_xlabel("b1")
ax[0].set_ylabel("count")
ax[0].set_title("Convergent families at ratio -2/9 vs b1\n(H=5; b1 in {8,10,20} have 0 since 3 does not divide b1)")
ax[0].grid(True, which="both", ls=":")
ax[0].legend()

# Right panel: Trans rate (with 0 plotted at upper bound 1/N; show as marker)
upper = [1.0 / c if c > 0 else None for c in conv]
ax[1].loglog([bi for bi, u in zip(b, upper) if u is not None],
             [u for u in upper if u is not None], "rv",
             label="upper bound 1/N (since 0 Trans)")
# annotate
for bi, t, c in zip(b, trans, conv):
    if c > 0:
        ax[1].annotate(f"b1={bi}\n0/{c}", (bi, 1.0/c),
                       textcoords="offset points", xytext=(6, 6),
                       fontsize=8)
ax[1].set_xlabel("b1")
ax[1].set_ylabel("Trans rate (upper bound = 1/N_convergent)")
ax[1].set_title("Trans rate at -2/9 (HALT: zero across b1 in {9,12,15,30})")
ax[1].grid(True, which="both", ls=":")
ax[1].legend()

plt.tight_layout()
fig.savefig(OUT / "trans_rate_vs_b1.png", dpi=130)
print(f"Wrote {OUT/'trans_rate_vs_b1.png'}")
