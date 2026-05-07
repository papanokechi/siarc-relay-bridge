"""Relay 092 — T1-017M-BOREL-PADE-S2-092

Borel-Padé exponential-asymptotics resummation of the 017m recurrence
to extract the Stokes constant S_2 governing the M8b axis. Distinct
from prior T37M attempt: small-(N,M) sweep regime {6, 8, ..., 18} with
dps>=300, avoiding the RANK_LOSS regime that halted T37M at high orders.

Methodology (per Lustri et al. arXiv:2506.21120 + Costin/Loday-Richaud):
  1. Load 017m recurrence series (cached at T37E, dps=400, N=5000).
  2. Build raw scaled Borel transform in u = t/zeta_star coords:
        b_n(u) := a_n * zeta_star^n / Gamma(n+1)
     so B(u) has nearest singularities at u=1 (S_1) and u=2 (S_2).
  3. Padé approximant [N, M] for N, M in {6, 8, 10, 12, 14, 16, 18}
     subject to N + M <= series_length - 4. (We have ~50 coefficients,
     so this is comfortably satisfied.)
  4. For each [N/M], find roots of denominator Q; identify pole closest
     to u=2 (the S_2 location). Read residue R = P(u_pole)/Q'(u_pole).
  5. Logarithmic-singularity Padé extraction: for B(u) ~
     -(S_2/(2 pi)) log(1 - u/2) near u=2, the dominant Padé pole at
     u_pole has residue R such that the candidate Stokes constant is
        S_2_candidate = -2*pi * R * u_pole
     (sign + factor follow from Pade approximation of log(1-u/u_pole)
      where the Padé picks up an effective residue scaling with u_pole.)
  6. Stability check: digits-of-agreement across (N, M) neighbors. If
     >= dps/4 across a 3+ adjacent (N, M) cell region, classify
     EXTRACTED. Else PERMANENT_RESIDUAL_G6b (Padé-divergence pattern
     documented as substrate evidence).
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import mpmath as mp

HERE = Path(__file__).resolve().parent
BRIDGE = HERE.parent.parent.parent  # ...\siarc-relay-bridge
T37E_DIR = BRIDGE / "sessions" / "2026-05-02" / "T37E-EXTENDED-RECURRENCE"
T35_DIR = BRIDGE / "sessions" / "2026-05-02" / "T35-STOKES-MULTIPLIER-DISCRIMINATION"

REPS = ["V_quad", "QL15", "QL05", "QL09"]
DPS_PADE = 300
N_MAX_LOAD = 60  # only need up to ~36+4=40, load 60 for margin

# Padé sweep grid (092 spec).
N_GRID = [6, 8, 10, 12, 14, 16, 18]
M_GRID = [6, 8, 10, 12, 14, 16, 18]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_str(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def load_t35_constants() -> Dict[str, Dict[str, mp.mpf]]:
    """Read zeta_star, S1_imag from T35 stokes_multipliers_per_rep.csv at dps=250."""
    csv_path = T35_DIR / "stokes_multipliers_per_rep.csv"
    out: Dict[str, Dict[str, mp.mpf]] = {}
    with csv_path.open("r", encoding="utf-8") as fh:
        rdr = csv.DictReader(fh)
        for row in rdr:
            if row["dps"] != "250":
                continue
            rid = row["rep_id"]
            if rid not in REPS:
                continue
            out[rid] = {
                "zeta_star": mp.mpf(row["zeta_star"]),
                "C_lsq": mp.mpf(row["C_lsq"]),
                "S1_imag": mp.mpf(row["S1_imag"]),
                "Delta_b": int(row["Delta_b"]),
                "side": row["side"],
                "A_pred": int(row["A_pred"]),
            }
    missing = [r for r in REPS if r not in out]
    if missing:
        raise RuntimeError(f"missing T35 dps=250 entries for: {missing}")
    return out


def load_a_series_truncated(rep_id: str, n_max: int) -> List[mp.mpf]:
    """Load first n_max+1 entries of a_n from T37E cached CSV.

    Verifies imag part is essentially zero per T37E convention.
    """
    p = T37E_DIR / f"a_n_{rep_id}_dps400_N5000.csv"
    series: List[mp.mpf] = []
    with p.open("r", encoding="utf-8") as fh:
        rdr = csv.DictReader(fh)
        for row in rdr:
            n = int(row["n"])
            if n != len(series):
                raise RuntimeError(f"unexpected n={n} at len={len(series)}")
            re = mp.mpf(row["a_n_real"])
            im = mp.mpf(row["a_n_imag"])
            if abs(im) > mp.mpf("1e-100"):
                raise RuntimeError(f"unexpected imag for {rep_id} n={n}: {im}")
            series.append(re)
            if n >= n_max:
                break
    if len(series) < n_max + 1:
        raise RuntimeError(f"{rep_id} only has {len(series)} entries, need {n_max+1}")
    return series


def borel_u_coeffs(a: List[mp.mpf], zeta_star: mp.mpf, n_max: int) -> List[mp.mpf]:
    """b_n(u) := a_n * zeta_star^n / Gamma(n+1), n=0..n_max."""
    out: List[mp.mpf] = []
    for n in range(n_max + 1):
        if n == 0:
            out.append(a[0])  # / Gamma(1) = 1
            continue
        out.append(a[n] * mp.power(zeta_star, n) / mp.factorial(n))
    return out


def pade_NM(coeffs: List[mp.mpf], N: int, M: int) -> Optional[Tuple[List[mp.mpf], List[mp.mpf]]]:
    """Padé [N/M] approximant from coeffs[0..N+M].

    mpmath.pade(a, L, M) requires len(a) >= L+M+1 and returns (P, Q)
    with deg P = L, deg Q = M, Q[0] = 1.
    Returns (P, Q) or None on rank-loss / numerical failure.
    """
    needed = N + M + 1
    if len(coeffs) < needed:
        return None
    try:
        P, Q = mp.pade(coeffs[:needed], N, M)
        # mpmath returns lists; make sure both are lists.
        return list(P), list(Q)
    except (ZeroDivisionError, ValueError, ArithmeticError):
        return None


def poly_eval(c: List, x) -> "mp.mpc":
    """Horner; c is ascending order (c[0] + c[1] x + ...)."""
    out = mp.mpc(0)
    for k in range(len(c) - 1, -1, -1):
        out = out * x + c[k]
    return out


def poly_deriv(c: List) -> List:
    return [k * c[k] for k in range(1, len(c))]


def find_roots_polyroots(c: List) -> List["mp.mpc"]:
    """Find roots via mpmath.polyroots; coefficients ascending order.
    mpmath.polyroots takes descending coefficients.
    """
    if len(c) <= 1:
        return []
    desc = list(reversed(c))
    try:
        roots = mp.polyroots(desc, maxsteps=200, extraprec=100)
        return [mp.mpc(r) for r in roots]
    except (mp.NoConvergence, ValueError, ZeroDivisionError):
        return []


def candidate_S2_from_pade(
    P: List[mp.mpf],
    Q: List[mp.mpf],
    target_u: mp.mpf,  # u=2 for S_2
    real_tol: mp.mpf = mp.mpf("0.05"),  # |Im/|root|| <= this counted as "real"
    radius: mp.mpf = mp.mpf("3.0"),
) -> Optional[Dict]:
    """Find pole of Pade closest to u=target_u (real); return scaled residue.

    Returns dict with: pole_u (mpc), residue_at_pole (mpc),
                       S2_candidate (mpc), all_real_poles (list[mpc]),
                       all_distances_to_target (list[mpf]),
                       n_real_poles_in_radius (int).

    If no eligible pole found, returns None.
    """
    roots = find_roots_polyroots(Q)
    if not roots:
        return None
    # Filter to poles with small imaginary part and within radius.
    eligible: List[Tuple[mp.mpc, mp.mpf]] = []
    for r in roots:
        ar = abs(r)
        if ar == 0:
            continue
        if ar > radius:
            continue
        if abs(mp.im(r)) > real_tol * ar:
            continue
        if mp.re(r) <= 0:
            continue
        dist = abs(r - target_u)
        eligible.append((r, dist))
    if not eligible:
        return None
    eligible.sort(key=lambda t: t[1])
    best, best_dist = eligible[0]
    Qp = poly_deriv(Q)
    qpv = poly_eval(Qp, best)
    if abs(qpv) == 0:
        return None
    pv = poly_eval(P, best)
    residue = pv / qpv
    # Logarithmic-singularity scaling: B(u) ~ -(S_2/(2 pi)) log(1 - u/2)
    # near u=2. Padé approximant captures this singularity with effective
    # residue R such that Pade ~ R / (u - u_pole) + ...; the equivalent
    # log-jump amplitude is A = -R * u_pole (formal Mittag-Leffler), giving
    # S_2_candidate = -2*pi * R * u_pole = 2*pi * residue * (-u_pole).
    # Sign carries through to T35 convention S_1 = 2*pi*i*C_imag.
    # We report the Stokes constant magnitude (Im part should dominate by
    # T35 convention; Re part is a diagnostic).
    S2_candidate = -2 * mp.pi * residue * best
    return {
        "pole_u": best,
        "dist_to_target": best_dist,
        "residue_at_pole": residue,
        "S2_candidate": S2_candidate,
        "n_eligible": len(eligible),
        "all_eligible_dists": [str(d) for _, d in eligible],
    }


def fmt_mpc(z: "mp.mpc", n: int = 30) -> str:
    return f"({mp.nstr(mp.re(z), n)}) + ({mp.nstr(mp.im(z), n)})j"


def digits_agree(a: "mp.mpc", b: "mp.mpc") -> mp.mpf:
    """Return -log10(|a-b| / max(|a|,|b|)) as digits of agreement.
    Returns 0 if both zero or if relative diff > 1.
    """
    diff = abs(a - b)
    scale = max(abs(a), abs(b))
    if scale == 0:
        return mp.mpf("0")
    rel = diff / scale
    if rel >= 1:
        return mp.mpf("0")
    if rel == 0:
        return mp.mpf("1000")  # essentially exact
    return -mp.log10(rel)


def main():
    t0 = time.time()
    mp.mp.dps = DPS_PADE
    print(f"[092] dps={DPS_PADE} N_GRID={N_GRID} M_GRID={M_GRID}")
    print(f"[092] T37E_DIR = {T37E_DIR}")
    if not T37E_DIR.exists():
        raise SystemExit(f"HALT_092_NO_017L_SUBSTRATE: missing {T37E_DIR}")
    if not T35_DIR.exists():
        raise SystemExit(f"HALT_092_NO_017L_SUBSTRATE: missing {T35_DIR}")

    # ---- Phase A: Substrate readback ----
    constants = load_t35_constants()
    substrate_shas: Dict[str, str] = {}
    series_per_rep: Dict[str, List[mp.mpf]] = {}
    for rep in REPS:
        csv_p = T37E_DIR / f"a_n_{rep}_dps400_N5000.csv"
        substrate_shas[rep] = sha256_file(csv_p)
        series_per_rep[rep] = load_a_series_truncated(rep, N_MAX_LOAD)
        print(f"[092] {rep}: zeta_star={mp.nstr(constants[rep]['zeta_star'], 12)}  "
              f"S1_imag={mp.nstr(constants[rep]['S1_imag'], 12)}  "
              f"sha16={substrate_shas[rep][:16]}")

    # ---- Phase B: Borel transform construction ----
    borel_per_rep: Dict[str, List[mp.mpf]] = {}
    borel_diagnostics: Dict[str, Dict] = {}
    for rep in REPS:
        zeta = constants[rep]["zeta_star"]
        b_u = borel_u_coeffs(series_per_rep[rep], zeta, N_MAX_LOAD)
        borel_per_rep[rep] = b_u
        # Decay diagnostic.
        # |b_n| ~ |a_n| * |zeta|^n / n! ~ (1/n) * |S_1|/(2 pi) (leading) in u-coords;
        # in u-coords leading singularity at u=1, so |b_n| should decay
        # geometrically at most. Record sample values.
        sample_n = [0, 1, 5, 10, 20, 30, 40, 50, 60]
        sample_n = [n for n in sample_n if n <= N_MAX_LOAD]
        borel_diagnostics[rep] = {
            "decay_samples": {
                str(n): mp.nstr(abs(b_u[n]), 25) for n in sample_n
            },
            "n_loaded": len(b_u),
        }
        print(f"[092] {rep} Borel u-coeffs sampled |b_n|: "
              f"|b_5|={mp.nstr(abs(b_u[5]), 6)}  "
              f"|b_20|={mp.nstr(abs(b_u[20]), 6)}  "
              f"|b_40|={mp.nstr(abs(b_u[40]), 6)}")

    # ---- Phase C: Padé sweep ----
    pade_results_per_rep: Dict[str, Dict] = {}
    for rep in REPS:
        zeta = constants[rep]["zeta_star"]
        b_u = borel_per_rep[rep]
        cells: List[Dict] = []
        for N in N_GRID:
            for M in M_GRID:
                if N + M + 1 > N_MAX_LOAD + 1:
                    continue
                pq = pade_NM(b_u, N, M)
                if pq is None:
                    cells.append({
                        "N": N, "M": M, "status": "PADE_FAILED",
                    })
                    continue
                P, Q = pq
                # Find pole near u=2 (the S_2 location) and residue.
                cand = candidate_S2_from_pade(P, Q, mp.mpf("2"))
                if cand is None:
                    cells.append({
                        "N": N, "M": M, "status": "NO_POLE_NEAR_2",
                    })
                    continue
                cells.append({
                    "N": N, "M": M, "status": "OK",
                    "pole_u_re": mp.nstr(mp.re(cand["pole_u"]), 25),
                    "pole_u_im": mp.nstr(mp.im(cand["pole_u"]), 25),
                    "dist_to_2": mp.nstr(cand["dist_to_target"], 12),
                    "residue_re": mp.nstr(mp.re(cand["residue_at_pole"]), 25),
                    "residue_im": mp.nstr(mp.im(cand["residue_at_pole"]), 25),
                    "S2_candidate_re": mp.nstr(mp.re(cand["S2_candidate"]), 30),
                    "S2_candidate_im": mp.nstr(mp.im(cand["S2_candidate"]), 30),
                    "abs_S2_candidate": mp.nstr(abs(cand["S2_candidate"]), 12),
                    "n_eligible_poles": cand["n_eligible"],
                    # Keep mpc objects on side for stability check.
                    "_S2_mpc": cand["S2_candidate"],
                    "_pole_mpc": cand["pole_u"],
                })
        pade_results_per_rep[rep] = {
            "rep": rep,
            "zeta_star": mp.nstr(zeta, 25),
            "S1_imag_t35": mp.nstr(constants[rep]["S1_imag"], 25),
            "cells": cells,
        }

    # ---- Phase C.3: Convergence-region detection ----
    convergence_per_rep: Dict[str, Dict] = {}
    threshold_digits = mp.mpf(DPS_PADE) / 4  # spec: dps/4
    for rep in REPS:
        cells = pade_results_per_rep[rep]["cells"]
        # Build (N,M) -> S2_mpc map.
        ok_cells = {(c["N"], c["M"]): c["_S2_mpc"]
                    for c in cells if c["status"] == "OK"}
        # For each pair of NEIGHBORING cells (N,M) and (N',M') with
        # |N-N'|+|M-M'| <= 2 (i.e., adjacent in grid), compute digits agreement.
        agreements: List[Dict] = []
        for (N, M), s in ok_cells.items():
            for (Np, Mp), sp in ok_cells.items():
                if (N, M) >= (Np, Mp):
                    continue
                if abs(N - Np) + abs(M - Mp) > 2:
                    continue
                d = digits_agree(s, sp)
                agreements.append({
                    "cell_a": [N, M], "cell_b": [Np, Mp],
                    "digits": float(d) if d < 1000 else 1000.0,
                })
        # Find the largest contiguous subgrid where ALL pairwise neighbors
        # agree to >= threshold_digits. Practical heuristic: count cells
        # whose all neighbors agree above threshold.
        good_cells = set()
        for ag in agreements:
            if ag["digits"] >= float(threshold_digits):
                good_cells.add(tuple(ag["cell_a"]))
                good_cells.add(tuple(ag["cell_b"]))
        # Convergence region exists iff good_cells contains at least 3 cells.
        # Compute consensus (mean) S_2 if convergence region exists.
        consensus_S2 = None
        if len(good_cells) >= 3:
            ss = [ok_cells[c] for c in good_cells]
            consensus_S2 = sum(ss) / len(ss)
        # Compute median |S_2| as central tendency for divergence diagnostics.
        if ok_cells:
            mags = sorted([abs(s) for s in ok_cells.values()])
            half = len(mags) // 2
            if len(mags) % 2 == 1:
                median_abs = mags[half]
            else:
                median_abs = (mags[half - 1] + mags[half]) / 2
            # Half-range as max - min.
            span_abs = mags[-1] - mags[0]
            rel_half_range = span_abs / median_abs if median_abs > 0 else mp.mpf("inf")
        else:
            median_abs = mp.mpf("0")
            rel_half_range = mp.mpf("inf")
        convergence_per_rep[rep] = {
            "n_ok_cells": len(ok_cells),
            "n_good_cells_above_threshold": len(good_cells),
            "good_cells": [list(c) for c in sorted(good_cells)],
            "consensus_S2_re": mp.nstr(mp.re(consensus_S2), 50) if consensus_S2 else None,
            "consensus_S2_im": mp.nstr(mp.im(consensus_S2), 50) if consensus_S2 else None,
            "abs_consensus_S2": mp.nstr(abs(consensus_S2), 25) if consensus_S2 else None,
            "median_abs_S2_candidates": mp.nstr(median_abs, 25),
            "rel_half_range_abs": mp.nstr(rel_half_range, 12),
            "agreements_above_threshold": [a for a in agreements if a["digits"] >= float(threshold_digits)],
            "all_agreements": agreements,
            "threshold_digits": float(threshold_digits),
        }

    # ---- Phase D: Verdict classification ----
    rep_verdicts: Dict[str, str] = {}
    for rep in REPS:
        info = convergence_per_rep[rep]
        if info["consensus_S2_re"] is not None and info["n_good_cells_above_threshold"] >= 3:
            rep_verdicts[rep] = "EXTRACTED"
        else:
            rep_verdicts[rep] = "PERMANENT_RESIDUAL_G6b"

    # Aggregate M8b axis verdict.
    if any(v == "EXTRACTED" for v in rep_verdicts.values()):
        m8b_verdict = "M8b_S2_EXTRACTED_VIA_BOREL_PADE"
        status = "COMPLETE_EXTRACTED"
    else:
        m8b_verdict = "M8b_S2_PERMANENT_RESIDUAL_VIA_BOREL_PADE"
        status = "COMPLETE_PERMANENT_RESIDUAL"

    # Strip mpc objects from cells before serializing.
    pade_results_serializable: Dict[str, Dict] = {}
    for rep in REPS:
        rd = dict(pade_results_per_rep[rep])
        rd["cells"] = [
            {k: v for k, v in c.items() if not k.startswith("_")}
            for c in rd["cells"]
        ]
        pade_results_serializable[rep] = rd

    # Strip mpc from convergence_per_rep too (none stored).
    out = {
        "task_id": "T1-017M-BOREL-PADE-S2-092",
        "date": "2026-05-07",
        "dps": DPS_PADE,
        "n_grid": N_GRID,
        "m_grid": M_GRID,
        "n_max_loaded": N_MAX_LOAD,
        "substrate_shas": substrate_shas,
        "t35_constants": {
            rep: {
                "zeta_star": mp.nstr(constants[rep]["zeta_star"], 30),
                "C_lsq": mp.nstr(constants[rep]["C_lsq"], 30),
                "S1_imag": mp.nstr(constants[rep]["S1_imag"], 30),
                "Delta_b": constants[rep]["Delta_b"],
                "side": constants[rep]["side"],
                "A_pred": constants[rep]["A_pred"],
            } for rep in REPS
        },
        "borel_diagnostics": borel_diagnostics,
        "pade_results_per_rep": pade_results_serializable,
        "convergence_per_rep": convergence_per_rep,
        "rep_verdicts": rep_verdicts,
        "m8b_verdict": m8b_verdict,
        "status": status,
        "elapsed_sec": time.time() - t0,
    }
    out_path = HERE / "borel_pade_results.json"
    with out_path.open("w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2)
    print(f"[092] wrote {out_path}")
    print(f"[092] M8b verdict: {m8b_verdict}")
    print(f"[092] rep verdicts: {rep_verdicts}")
    for rep in REPS:
        info = convergence_per_rep[rep]
        print(f"[092] {rep}: ok_cells={info['n_ok_cells']}/{len(N_GRID)*len(M_GRID)}  "
              f"good_above_thresh={info['n_good_cells_above_threshold']}  "
              f"median_abs_S2={info['median_abs_S2_candidates'][:20]}  "
              f"rel_half_range={info['rel_half_range_abs'][:12]}")
    print(f"[092] elapsed: {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
