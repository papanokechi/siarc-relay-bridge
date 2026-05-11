"""Build subtracted stability tables and divergence-pattern analysis from
borel_pade_subtracted_results.json (slot 184 U2 quadrant).

Adapted from 092's build_stability_table.py with these augmentations
per slot 184 prompt Phase A.4:
  - top-level meta: `subtraction_order` (= K_LEAD) recorded in header
  - per-cell columns appended: pole-nearest-u=2 distance + residue
    diagnostics already present in 092; here we also surface a fourth
    table: pole_re (the real part of u_pole, to detect u_pole -> 2
    convergence in the subtracted variant)
  - cross-quadrant comparison block: side-by-side with 092 raw-low-order
    medians at the same (rep, N, M) cell index
"""
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "borel_pade_subtracted_results.json"
BRIDGE = HERE.parent.parent.parent
PRIOR_092 = BRIDGE / "sessions" / "2026-05-07" / "T1-017M-BOREL-PADE-S2-092" / "borel_pade_results.json"

with RESULTS.open() as fh:
    d = json.load(fh)

# Optional: load 092 results for side-by-side cross-quadrant compare.
prior = None
if PRIOR_092.exists():
    try:
        with PRIOR_092.open() as fh:
            prior = json.load(fh)
    except (json.JSONDecodeError, OSError):
        prior = None

REPS = ["V_quad", "QL15", "QL05", "QL09"]
NS = d.get("n_grid", [6, 8, 10, 12, 14, 16, 18])
MS = d.get("m_grid", [6, 8, 10, 12, 14, 16, 18])


def fmt(v, w=10, n=4):
    if v is None:
        return " " * (w - 1) + "-"
    if isinstance(v, str):
        return f"{v:>{w}s}"
    return f"{v:>{w}.{n}g}"


lines = []
lines.append("# Subtracted Pade [N/M] Stability Tables -- Relay 184 (U2 quadrant)")
lines.append("")
lines.append(f"task: T2-EXECUTOR-T1-156-A-U2-QUADRANT-SUBTRACTED-PADE-184")
lines.append(f"dps_pade = {d['dps_pade']}  ;  dps_fit = {d['dps_fit']}")
lines.append(f"subtraction_order K_LEAD = {d['subtraction_order']}")
lines.append(f"fit window = {d['fit_window']}")
lines.append(f"N grid = {NS}  ;  M grid = {MS}")
lines.append(f"M8b verdict: **{d['m8b_verdict']}**")
lines.append(f"halt_mode: **{d['halt_mode']}**")
lines.append("")

# Aggregate stats.
total_ok = sum(c["status"] == "OK"
               for rep in REPS
               for c in d["pade_results_per_rep"][rep]["cells"])
total_cells = sum(len(d["pade_results_per_rep"][rep]["cells"]) for rep in REPS)
best_pair_digits = max(d["convergence_per_rep"][rep]["best_digits_agreement"] for rep in REPS)
threshold = d["convergence_per_rep"]["V_quad"]["threshold_digits"]
lines.append(
    f"Aggregate: {total_ok}/{total_cells} OK Pade cells across 4 reps; "
    f"best adjacent-pair digits-of-agreement = {best_pair_digits:.2f} "
    f"(threshold = dps/4 = {threshold:.0f}). "
    f"{'PASS dps/4 gate' if best_pair_digits >= threshold else 'FAIL dps/4 gate'}."
)
lines.append("")

# Per-rep tables.
for rep in REPS:
    info = d["convergence_per_rep"][rep]
    cells = d["pade_results_per_rep"][rep]["cells"]
    cells_by_nm = {(c["N"], c["M"]): c for c in cells}
    constants = d["t35_constants"][rep]

    lines.append(f"## {rep}")
    lines.append("")
    lines.append(f"- T35 zeta_star = {constants['zeta_star'][:20]}")
    lines.append(f"- T35 C_lsq = {constants['C_lsq'][:20]}")
    lines.append(f"- T35 S_1 (imag, T35 conv) = {constants['S1_imag'][:20]}")
    s1 = d["stage1_fit_per_rep"][rep]
    lines.append(f"- stage-1 fit: a_1 = {s1['a_1']}  a_25 = {s1['a_25']}  max_resid = {s1['fit_max_residual']}")
    diag_samples = d["residual_diagnostics"][rep]["samples"]
    target_n = 40
    sample_at_40 = next((s for s in diag_samples if s["n"] == target_n), None)
    if sample_at_40:
        lines.append(f"- subtracted-residual decay at n={target_n}: |residual|/|leading| = {sample_at_40['ratio_residual_over_lead']}")
    lines.append(f"- median |S_2 candidate| = {info['median_abs_S2_candidates'][:22]}")
    lines.append(f"- relative half-range of |S_2| = {info['rel_half_range_abs'][:12]}")
    lines.append(
        f"- best digits-of-agreement across {info['n_pairs_total']} adjacent (N,M) pairs: "
        f"{info['best_digits_agreement']:.3f}"
    )
    lines.append(
        f"- threshold for EXTRACTED = dps/4 = {info['threshold_digits']:.0f}; "
        f"achieved {len(info['agreements_above_threshold'])}/{info['n_pairs_total']} pairs"
    )
    lines.append(f"- verdict: **{d['rep_verdicts'][rep]}**")
    if info["consensus_S2_re"] is not None:
        lines.append(f"- consensus S_2 (re, im) = ({info['consensus_S2_re'][:30]}, {info['consensus_S2_im'][:30]})")
    lines.append("")

    # |S_2 candidate| table
    lines.append("### |S_2 candidate| (subtracted) stability table")
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
    lines.append("### subtracted_pade_pole_nearest_u2_distance")
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

    # residue at nearest pole magnitude
    lines.append("### subtracted_pade_residue_at_nearest_pole (|residue|)")
    lines.append("")
    lines.append(header)
    lines.append(sep)
    for n in NS:
        row = []
        for m in MS:
            cell = cells_by_nm.get((n, m))
            if cell and cell["status"] == "OK":
                rre = float(cell["residue_re"])
                rim = float(cell["residue_im"])
                v = (rre * rre + rim * rim) ** 0.5
            else:
                v = None
            row.append(fmt(v, w=10, n=4))
        lines.append(f"|   {n}   | " + " | ".join(row) + " |")
    lines.append("")

    # u_pole real part
    lines.append("### u_pole (real part of nearest-to-u=2 pole)")
    lines.append("")
    lines.append(header)
    lines.append(sep)
    for n in NS:
        row = []
        for m in MS:
            cell = cells_by_nm.get((n, m))
            v = float(cell["pole_u_re"]) if cell and cell["status"] == "OK" else None
            row.append(fmt(v, w=10, n=4))
        lines.append(f"|   {n}   | " + " | ".join(row) + " |")
    lines.append("")
    lines.append("---")
    lines.append("")

# Divergence-pattern analysis
lines.append("## Divergence-pattern diagnostic (per slot 184 Phase B halt-mode)")
lines.append("")
for rep in REPS:
    info = d["convergence_per_rep"][rep]
    cells = d["pade_results_per_rep"][rep]["cells"]
    abs_vals = sorted([float(c["abs_S2_candidate"]) for c in cells if c["status"] == "OK"])
    if not abs_vals:
        continue
    span_orders = abs_vals[-1] / abs_vals[0] if abs_vals[0] > 0 else float("inf")

    fixed_M = 18
    seq_N = [next((float(c["abs_S2_candidate"]) for c in cells
                   if c["N"] == n and c["M"] == fixed_M and c["status"] == "OK"), None)
             for n in NS]
    seq_N_clean = [v for v in seq_N if v is not None]
    monotone_in_N = "monotonic-increase" if seq_N_clean == sorted(seq_N_clean) else (
        "monotonic-decrease" if seq_N_clean == sorted(seq_N_clean, reverse=True) else "non-monotonic"
    )
    fixed_N = 18
    seq_M = [next((float(c["abs_S2_candidate"]) for c in cells
                   if c["N"] == fixed_N and c["M"] == m and c["status"] == "OK"), None)
             for m in MS]
    seq_M_clean = [v for v in seq_M if v is not None]
    monotone_in_M = "monotonic-increase" if seq_M_clean == sorted(seq_M_clean) else (
        "monotonic-decrease" if seq_M_clean == sorted(seq_M_clean, reverse=True) else "non-monotonic"
    )
    ims = [float(c["S2_candidate_im"]) for c in cells if c["status"] == "OK"]
    n_pos = sum(1 for v in ims if v > 0)
    n_neg = sum(1 for v in ims if v < 0)
    sign_coherence = "coherent_pos" if n_neg == 0 else (
        "coherent_neg" if n_pos == 0 else f"mixed ({n_pos}+/{n_neg}-)"
    )
    dists = [float(c["dist_to_2"]) for c in cells if c["status"] == "OK"]
    # Pole-distance shrinkage check: is min(dist) achieved at large (N+M)?
    cells_ok = [c for c in cells if c["status"] == "OK"]
    if cells_ok:
        min_dist = min(float(c["dist_to_2"]) for c in cells_ok)
        cell_at_min = next(c for c in cells_ok if float(c["dist_to_2"]) == min_dist)
        max_NM = max(c["N"] + c["M"] for c in cells_ok)
        cell_at_max_NM = next(c for c in cells_ok if c["N"] + c["M"] == max_NM)
        max_NM_dist = float(cell_at_max_NM["dist_to_2"])
        pole_shrinks = "YES" if cell_at_min["N"] + cell_at_min["M"] >= max_NM - 4 else "NO"
    else:
        min_dist = None
        pole_shrinks = "n/a"
    log10_span = int(math.log10(span_orders)) if span_orders > 1 else 0
    lines.append(f"### {rep}")
    lines.append(f"- |S_2| span (max/min): {span_orders:.4g}x (~{log10_span} orders of magnitude)")
    lines.append(f"- |S_2| at fixed M=18, N varying: {monotone_in_N}")
    lines.append(f"- |S_2| at fixed N=18, M varying: {monotone_in_M}")
    lines.append(f"- sign of Im(S_2 candidate) across cells: {sign_coherence}")
    if dists:
        lines.append(f"- nearest pole distances to u=2: min={min(dists):.4g}, max={max(dists):.4g}")
        lines.append(f"- min-distance achieved near max(N+M)? {pole_shrinks}")
    lines.append("")

# Cross-quadrant comparison vs 092 raw-low-order.
if prior is not None:
    lines.append("## Cross-quadrant comparison: subtracted (slot 184) vs raw (slot 092)")
    lines.append("")
    lines.append(
        "Both runs use identical (N, M) in {6..18}^2, dps=300 (Pade), 4 reps. "
        "Only the Borel-coefficient series differs: 092 uses raw a_n; 184 uses "
        "K_LEAD = 25 -subtracted a_n_residual. Comparison at the per-rep level:"
    )
    lines.append("")
    lines.append("| rep | (092) median |S_2| | (184) median |S_2| | (092) rel_half_range | (184) rel_half_range | (092) best_pair_digits | (184) best_pair_digits |")
    lines.append("|---|---|---|---|---|---|---|")
    for rep in REPS:
        info_184 = d["convergence_per_rep"][rep]
        info_092 = prior.get("convergence_per_rep", {}).get(rep, {})
        # 092 best-pair-digits: derive from agreements list
        all_092 = info_092.get("all_agreements", [])
        best_092 = max((a["digits"] for a in all_092), default=0.0) if all_092 else 0.0
        lines.append(
            f"| {rep} | {info_092.get('median_abs_S2_candidates', '?')[:12]} | "
            f"{info_184['median_abs_S2_candidates'][:12]} | "
            f"{info_092.get('rel_half_range_abs', '?')[:10]} | "
            f"{info_184['rel_half_range_abs'][:10]} | "
            f"{best_092:.2f} | "
            f"{info_184['best_digits_agreement']:.2f} |"
        )
    lines.append("")

# Aggregate interpretation
lines.append("## Aggregate interpretation -- halt-mode rationale")
lines.append("")
hm = d["halt_mode"]
if hm == "HALT_A_RESIDUAL_PATTERN_REPRODUCED":
    lines.append(
        "The K_LEAD = 25 -subtracted Pade approximant at small (N, M) in {6..18}^2 "
        "exhibits the same PERMANENT_RESIDUAL signature as 092's raw-low-order "
        "approach: no adjacent-cell pair achieves the dps/4 = 75-digit Pade-"
        "convergence threshold, and the pole-nearest-u=2 distance does not "
        "exhibit systematic shrinkage with increasing (N + M)."
    )
    lines.append("")
    lines.append(
        "**Cross-quadrant closure.** Combined with 092 (raw small-(N,M)) and T37M "
        "(subtracted large-M_in), the M8b axis sub-leading Stokes constant is "
        "now established as PERMANENT_RESIDUAL across all four corners of the "
        "Pade-stability quadrant grid: subtraction does not help at small order, "
        "and order-extension does not help at any subtraction order. This is the "
        "strictly-stronger negative-result substrate envisioned by slot 156 verdict's "
        "V0+(defended) target."
    )
elif hm == "HALT_A_DPS_THRESHOLD_REACHED":
    lines.append(
        "**Unexpected positive result.** The subtracted small-(N, M) variant has "
        "achieved >= dps/4 = 75 -digit agreement between at least one pair of "
        "adjacent (N, M) cells, indicating Pade-convergence to a stable S_2 "
        "candidate. This was assigned ~15% prior probability by slot 156 verdict. "
        "Triggers M8b V0 amendment cascade per 130R sec 6.3."
    )
elif hm == "HALT_A_NUMERICAL_INSTABILITY":
    lines.append(
        "**Numerical-instability halt.** Subtraction at small (N, M) exposes "
        "Hankel-system pathologies (poles at distance < 1e-10 from u=2 with "
        "diverging residues). Closure-by-methodology-limit: subtraction at "
        "this regime is numerically intractable. Less informative than "
        "RESIDUAL_PATTERN_REPRODUCED but still M-axis-relevant."
    )
lines.append("")

OUT = HERE / "stability_table_subtracted.md"
OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"wrote {OUT} ({len(lines)} lines)")
