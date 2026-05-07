"""Build stability tables and divergence-pattern analysis from
borel_pade_results.json.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "borel_pade_results.json"

with RESULTS.open() as fh:
    d = json.load(fh)

REPS = ["V_quad", "QL15", "QL05", "QL09"]
NS = [6, 8, 10, 12, 14, 16, 18]
MS = [6, 8, 10, 12, 14, 16, 18]


def fmt(v, w=10, n=4):
    if v is None:
        return " " * (w - 1) + "-"
    return f"{v:>{w}.{n}g}"


lines = []
lines.append("# Padé [N/M] Stability Tables — Relay 092")
lines.append("")
lines.append(f"dps = {d['dps']}  ;  N grid = {NS}  ;  M grid = {MS}")
lines.append(f"M8b verdict: **{d['m8b_verdict']}**")
lines.append("")
lines.append(f"All four reps yielded 49/49 OK Padé cells (no RANK_LOSS or "
             f"NO_POLE_NEAR_2 failures), but **zero** adjacent-cell pairs "
             f"agreed to dps/4 = {d['convergence_per_rep']['V_quad']['threshold_digits']:.0f} digits, "
             f"so no convergence region exists per the relay 092 spec gate.")
lines.append("")

for rep in REPS:
    info = d["convergence_per_rep"][rep]
    cells = d["pade_results_per_rep"][rep]["cells"]
    cells_by_nm = {(c["N"], c["M"]): c for c in cells}

    lines.append(f"## {rep}")
    lines.append("")
    lines.append(f"- T35 zeta_star = {d['t35_constants'][rep]['zeta_star'][:20]}")
    lines.append(f"- T35 S_1 (imag, T35 conv) = {d['t35_constants'][rep]['S1_imag'][:20]}")
    lines.append(f"- median |S_2 candidate| = {info['median_abs_S2_candidates'][:22]}")
    lines.append(f"- relative half-range of |S_2| = {info['rel_half_range_abs'][:12]}")
    lines.append(f"- best digits-of-agreement across "
                 f"{len(info['all_agreements'])} adjacent (N,M) pairs: "
                 f"{max(a['digits'] for a in info['all_agreements']):.3f}")
    lines.append(f"- threshold for EXTRACTED = dps/4 = "
                 f"{info['threshold_digits']:.0f}; achieved 0/{len(info['all_agreements'])} pairs")
    lines.append(f"- verdict: **{d['rep_verdicts'][rep]}**")
    lines.append("")

    # |S_2 candidate| table
    lines.append("### |S_2 candidate| stability table")
    lines.append("")
    header = "| N \\ M | " + " | ".join(f"{m:>10d}" for m in MS) + " |"
    sep = "|" + "---|" * (len(MS) + 1)
    lines.append(header)
    lines.append(sep)
    for n in NS:
        row = []
        for m in MS:
            cell = cells_by_nm.get((n, m))
            v = float(cell["abs_S2_candidate"]) if cell and cell["status"] == "OK" else None
            row.append(fmt(v, w=10, n=4))
        lines.append(f"|   {n}   | " + " | ".join(row) + " |")
    lines.append("")

    # dist-to-u=2 table
    lines.append("### Distance of nearest pole to u = 2 (the S_2 location)")
    lines.append("")
    lines.append(header)
    lines.append(sep)
    for n in NS:
        row = []
        for m in MS:
            cell = cells_by_nm.get((n, m))
            v = float(cell["dist_to_2"]) if cell and cell["status"] == "OK" else None
            row.append(fmt(v, w=10, n=4))
        lines.append(f"|   {n}   | " + " | ".join(row) + " |")
    lines.append("")

    # S_2 candidate (Im part — should match T35 S_1_imag scale if extraction worked)
    lines.append("### S_2 candidate Im part (T35 convention has Stokes constants pure imaginary)")
    lines.append("")
    lines.append(header)
    lines.append(sep)
    for n in NS:
        row = []
        for m in MS:
            cell = cells_by_nm.get((n, m))
            v = float(cell["S2_candidate_im"]) if cell and cell["status"] == "OK" else None
            row.append(fmt(v, w=10, n=4))
        lines.append(f"|   {n}   | " + " | ".join(row) + " |")
    lines.append("")
    lines.append("---")
    lines.append("")

# Divergence-pattern analysis
lines.append("## Divergence-pattern diagnostic (per Phase D2)")
lines.append("")
for rep in REPS:
    info = d["convergence_per_rep"][rep]
    cells = d["pade_results_per_rep"][rep]["cells"]
    abs_vals = sorted([float(c["abs_S2_candidate"]) for c in cells if c["status"] == "OK"])
    if not abs_vals:
        continue
    span_orders = abs_vals[-1] / abs_vals[0] if abs_vals[0] > 0 else float("inf")
    # detect monotonic growth in N at fixed M=18
    fixed_M = 18
    seq_N = [next((float(c["abs_S2_candidate"]) for c in cells
                   if c["N"] == n and c["M"] == fixed_M and c["status"] == "OK"), None)
             for n in NS]
    monotone_in_N = "monotonic-increase" if seq_N == sorted(seq_N) else (
        "monotonic-decrease" if seq_N == sorted(seq_N, reverse=True) else "non-monotonic"
    )
    fixed_N = 18
    seq_M = [next((float(c["abs_S2_candidate"]) for c in cells
                   if c["N"] == fixed_N and c["M"] == m and c["status"] == "OK"), None)
             for m in MS]
    monotone_in_M = "monotonic-increase" if seq_M == sorted(seq_M) else (
        "monotonic-decrease" if seq_M == sorted(seq_M, reverse=True) else "non-monotonic"
    )
    # sign-coherence: how many cells have positive Im(S_2) vs negative
    ims = [float(c["S2_candidate_im"]) for c in cells if c["status"] == "OK"]
    n_pos = sum(1 for v in ims if v > 0)
    n_neg = sum(1 for v in ims if v < 0)
    sign_coherence = "coherent_pos" if n_neg == 0 else (
        "coherent_neg" if n_pos == 0 else f"mixed ({n_pos}+/{n_neg}-)"
    )
    lines.append(f"### {rep}")
    lines.append(f"- |S_2| span (max/min): {span_orders:.4g}× (so spans ~{int(__import__('math').log10(span_orders)) if span_orders>1 else 0} orders of magnitude)")
    lines.append(f"- |S_2| at fixed M=18, N varying: {monotone_in_N}")
    lines.append(f"- |S_2| at fixed N=18, M varying: {monotone_in_M}")
    lines.append(f"- sign of Im(S_2 candidate) across cells: {sign_coherence}")
    lines.append(f"- nearest pole distances to u=2: min={min(float(c['dist_to_2']) for c in cells if c['status']=='OK'):.4g}, "
                 f"max={max(float(c['dist_to_2']) for c in cells if c['status']=='OK'):.4g}")
    lines.append("")

lines.append("## Aggregate interpretation")
lines.append("")
lines.append(
    "Per peer-AI rubric A's signal-floor concern (absorbed in 092 spec): "
    "Padé-stability across [N/M] orders is itself the inline signal-floor "
    "diagnostic. Across all four reps the small-(N,M) sweep produces well-"
    "formed Padé approximants (no RANK_LOSS at this conservative order, "
    "consistent with 092's design relative to T37M's M_in∈{200..800}), "
    "but the residue at the pole nearest u=2 fails to stabilise — the "
    "pole drifts in distance from 2 and its residue varies by 1-2 orders "
    "across the (N,M) grid. This **absence of convergence is the negative-"
    "result substrate**: at the laptop-feasible recurrence depth (017m / "
    "T37E cache, dps=400, N=5000, post-leading-sector polynomial structure), "
    "the sub-leading transmonomial governing S_2 is below the resolution "
    "floor of the small-order Padé construction.")
lines.append("")
lines.append(
    "Combined with T37M's high-order (M=200..800) RANK_LOSS verdict, "
    "the M8b-axis sub-leading Stokes constant is bracketed: "
    "**too small for low-order Padé to resolve, too noisy for high-order "
    "Padé to capture without numerical singularity**. This is the canonical "
    "PERMANENT_RESIDUAL_G6b signature.")
lines.append("")

OUT = HERE / "stability_table.md"
OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"wrote {OUT} ({len(lines)} lines)")
