"""Relay 184 -- T2-EXECUTOR-T1-156-A-U2-QUADRANT-SUBTRACTED-PADE.

U2 quadrant Borel-Pade survey for M8b axis sub-leading Stokes constant.
Combines T37M's K_LEAD=25 leading-transmonomial subtraction (per UF-092-U2
forward-pointer significance) with 092's small-(N,M) in {6..18}^2 Pade
sweep at dps=300, completing the four-quadrant Pade methodology survey:

    +-----------+---------------------+----------------------+
    |           | raw                  | subtracted (K=25)    |
    +-----------+---------------------+----------------------+
    | small (N,M) <= 18 | 092 (this work's reference)  | THIS RUN (slot 184)  |
    | large M_in {200..800} | (n/a)                | T37M                  |
    +-----------+---------------------+----------------------+

Spec source: slot 156 verdict 607f9e8 Q3d Pathway A; UF-092-U2.
Subtraction methodology: T37M runner at 0dbebdd, K_LEAD = 25 with
fit window [3500, 4900] over 017m's cached a_n series at dps=400, N=5000.

Output schema mirrors 092's borel_pade_results.json + adds
`subtraction_order` field recording K_LEAD = 25.

Performance optimization vs T37M: stage-1 fit uses Gamma-by-recurrence
Gamma(n+1) = n*Gamma(n) instead of mp.gamma per-n, reducing per-rep fit
cost from ~28 min (T37M @ dps=200) to ~30 sec.
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
PRIOR_092_DIR = BRIDGE / "sessions" / "2026-05-07" / "T1-017M-BOREL-PADE-S2-092"

REPS = ["V_quad", "QL15", "QL05", "QL09"]

# 092 spec settings (preserved verbatim per slot 184 prompt directive).
N_MAX_LOAD = 60  # only need up to ~40 for Pade [N+M <= 36]
N_GRID = [6, 8, 10, 12, 14, 16, 18]
M_GRID = [6, 8, 10, 12, 14, 16, 18]
DPS_PADE = 300

# T37M spec settings adopted verbatim (per slot 184 prompt: "K_LEAD value
# should match T37M's choice for direct A<->T37M comparison").
K_LEAD = 25
FIT_WINDOW = (3500, 4900)
DPS_FIT = 200  # escalated from T37M's runtime-cut dps=100 for cleanness
               # at dps/4 = 75-digit Pade-convergence threshold detection.


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_str(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def load_t35_constants() -> Dict[str, Dict[str, mp.mpf]]:
    """Read zeta_star, C_lsq, S1_imag from T35 stokes_multipliers_per_rep.csv
    at dps=250. Same as 092 (matches T37M's load_t35 + C field)."""
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
    """Load first n_max+1 a_n's only (092's narrow-load pattern)."""
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


def load_a_series_window(rep_id: str, n_lo: int, n_hi: int) -> List[mp.mpf]:
    """Load a_n only for n in [n_lo, n_hi] (used by stage-1 fit only)."""
    p = T37E_DIR / f"a_n_{rep_id}_dps400_N5000.csv"
    series: Dict[int, mp.mpf] = {}
    with p.open("r", encoding="utf-8") as fh:
        rdr = csv.DictReader(fh)
        for row in rdr:
            n = int(row["n"])
            if n < n_lo:
                continue
            if n > n_hi:
                break
            re = mp.mpf(row["a_n_real"])
            im = mp.mpf(row["a_n_imag"])
            if abs(im) > mp.mpf("1e-100"):
                raise RuntimeError(f"unexpected imag for {rep_id} n={n}: {im}")
            series[n] = re
    out = [series[n] for n in range(n_lo, n_hi + 1)]
    if len(out) != n_hi - n_lo + 1:
        raise RuntimeError(f"{rep_id} window load missing entries: got {len(out)}, want {n_hi-n_lo+1}")
    return out


def stage1_fit_recurrence(
    a_window: List[mp.mpf],
    n_lo: int,
    n_hi: int,
    C: mp.mpf,
    zeta_star: mp.mpf,
    K: int,
) -> Tuple[List[mp.mpf], Dict]:
    """T37M's stage-1 polynomial-correction fit, with Gamma-by-recurrence.

    Solve for a_1..a_K in:
        r_n := a_n / (C * Gamma(n) * zeta_star**(-n)) - 1 ~ sum_{k=1..K} a_k/n^k

    Reformulation for conditioning: t = n_mid/n in [n_lo, n_hi], so columns
    are t, t^2, ..., t^K with t~1. After QR-solve for e_k, rescale:
        a_k = e_k * n_mid^k.

    Returns (a_coefs[0..K], diagnostics-dict). a_coefs[0] = 0 placeholder.
    """
    M_rows = n_hi - n_lo + 1
    assert len(a_window) == M_rows, "a_window length mismatch"

    # --- Gamma(n) and zeta_star^(-n) by recurrence ---
    # Gamma(n_lo) computed once; then Gamma(n+1) = n * Gamma(n).
    # zeta_star^(-n_lo) once; then divide by zeta_star at each step.
    n_lo_mp = mp.mpf(n_lo)
    gamma_n = mp.gamma(n_lo_mp)
    zeta_inv_n = mp.power(zeta_star, -n_lo_mp)
    zeta_inv = 1 / zeta_star
    n_mid = mp.mpf((n_lo + n_hi) / 2)

    A = mp.matrix(M_rows, K)
    b = mp.matrix(M_rows, 1)
    for i in range(M_rows):
        n_int = n_lo + i
        n_mp = mp.mpf(n_int)
        L = C * gamma_n * zeta_inv_n
        r = a_window[i] / L
        b[i, 0] = r - 1
        t = n_mid / n_mp
        tk = t
        for k in range(K):
            A[i, k] = tk
            tk = tk * t
        # advance recurrence: Gamma(n+1) = n*Gamma(n); zeta^(-(n+1)) = zeta^-n * zeta^-1
        gamma_n = gamma_n * n_mp
        zeta_inv_n = zeta_inv_n * zeta_inv

    # --- QR-solve A x = b ---
    Q_qr, R_qr = mp.qr(A)
    QTb = Q_qr.T * b
    x = mp.matrix(K, 1)
    for k in range(K - 1, -1, -1):
        s = QTb[k, 0]
        for j in range(k + 1, K):
            s -= R_qr[k, j] * x[j, 0]
        x[k, 0] = s / R_qr[k, k]

    # Rescale: a_k = e_k * n_mid^k.
    a_coefs = [mp.mpf(0)]
    for k in range(K):
        a_coefs.append(x[k, 0] * mp.power(n_mid, k + 1))

    # Residual stats.
    pred = A * x
    resid_max = max(abs(pred[i, 0] - b[i, 0]) for i in range(M_rows))

    diag = {
        "K": K,
        "window": [n_lo, n_hi],
        "M_rows": M_rows,
        "fit_max_residual": mp.nstr(resid_max, 12),
        "a_1": mp.nstr(a_coefs[1], 30),
        "a_2": mp.nstr(a_coefs[2], 30),
        "a_3": mp.nstr(a_coefs[3], 30),
        "a_25": mp.nstr(a_coefs[25], 20),
    }
    return a_coefs, diag


def make_residual_series_small(
    a_full_small: List[mp.mpf],
    a_coefs: List[mp.mpf],
    C: mp.mpf,
    zeta_star: mp.mpf,
    n_max: int,
) -> List[mp.mpf]:
    """Compute a_n - C*Gamma(n)*zeta_star^(-n)*(1 + sum_{k=1..K} a_k/n^k) for n=0..n_max.

    a_full_small is a_n loaded for n=0..n_max.

    At n=0 the leading transmonomial is singular (Gamma(0) divergent); we
    keep a_0 verbatim (matches T37M convention).
    """
    K = len(a_coefs) - 1
    res: List[mp.mpf] = []
    for n in range(n_max + 1):
        if n == 0:
            res.append(a_full_small[0])
            continue
        n_mp = mp.mpf(n)
        L = C * mp.gamma(n_mp) * mp.power(zeta_star, -n_mp)
        # Horner-evaluate 1 + a_1/n + a_2/n^2 + ... + a_K/n^K.
        poly = a_coefs[K]
        for k in range(K - 1, 0, -1):
            poly = poly / n_mp + a_coefs[k]
        poly = poly / n_mp + 1
        lead_resummed = L * poly
        res.append(a_full_small[n] - lead_resummed)
    return res


def borel_u_coeffs(residual: List[mp.mpf], zeta_star: mp.mpf, n_max: int) -> List[mp.mpf]:
    """b_n(u) := a_n_residual * zeta_star^n / Gamma(n+1), n=0..n_max.

    Same Borel-transform convention as 092. At n=0, b_0 = a_0_residual /
    Gamma(1) = a_0. Note 092 used a_n (un-subtracted); here we use the
    K_LEAD-subtracted residual.
    """
    out: List[mp.mpf] = []
    for n in range(n_max + 1):
        if n == 0:
            out.append(residual[0])
            continue
        out.append(residual[n] * mp.power(zeta_star, n) / mp.factorial(n))
    return out


def pade_NM(coeffs: List[mp.mpf], N: int, M: int) -> Optional[Tuple[List[mp.mpf], List[mp.mpf]]]:
    """mpmath.pade(a, L, M) requires len(a) >= L+M+1 and returns P, Q
    with deg P = L, deg Q = M, Q[0] = 1. Same shape as 092."""
    needed = N + M + 1
    if len(coeffs) < needed:
        return None
    try:
        P, Q = mp.pade(coeffs[:needed], N, M)
        return list(P), list(Q)
    except (ZeroDivisionError, ValueError, ArithmeticError):
        return None


def poly_eval(c: List, x) -> "mp.mpc":
    out = mp.mpc(0)
    for k in range(len(c) - 1, -1, -1):
        out = out * x + c[k]
    return out


def poly_deriv(c: List) -> List:
    return [k * c[k] for k in range(1, len(c))]


def find_roots_polyroots(c: List) -> List["mp.mpc"]:
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
    target_u: mp.mpf,
    real_tol: mp.mpf = mp.mpf("0.05"),
    radius: mp.mpf = mp.mpf("3.0"),
) -> Optional[Dict]:
    """Find pole of Pade nearest u=target_u (092 convention)."""
    roots = find_roots_polyroots(Q)
    if not roots:
        return None
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
    S2_candidate = -2 * mp.pi * residue * best
    return {
        "pole_u": best,
        "dist_to_target": best_dist,
        "residue_at_pole": residue,
        "S2_candidate": S2_candidate,
        "n_eligible": len(eligible),
        "all_eligible_dists": [str(d) for _, d in eligible],
    }


def digits_agree(a: "mp.mpc", b: "mp.mpc") -> mp.mpf:
    diff = abs(a - b)
    scale = max(abs(a), abs(b))
    if scale == 0:
        return mp.mpf("0")
    rel = diff / scale
    if rel >= 1:
        return mp.mpf("0")
    if rel == 0:
        return mp.mpf("1000")
    return -mp.log10(rel)


def log(msg: str, fh=None):
    s = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(s, flush=True)
    if fh is not None:
        fh.write(s + "\n")
        fh.flush()


def main():
    t0 = time.time()
    out_path = HERE / "borel_pade_subtracted_results.json"
    run_log_path = HERE / "run.log"
    fit_cache_path = HERE / "stage1_fit_cache.json"

    with run_log_path.open("w", encoding="utf-8") as run_fh:
        log(f"[184] dps_fit={DPS_FIT} dps_pade={DPS_PADE} K_LEAD={K_LEAD}", run_fh)
        log(f"[184] N_GRID={N_GRID} M_GRID={M_GRID}", run_fh)
        log(f"[184] FIT_WINDOW={FIT_WINDOW}", run_fh)
        log(f"[184] BRIDGE={BRIDGE}", run_fh)
        log(f"[184] T37E_DIR={T37E_DIR}", run_fh)
        if not T37E_DIR.exists():
            raise SystemExit(f"HALT_184_NO_T37E_SUBSTRATE: missing {T37E_DIR}")
        if not T35_DIR.exists():
            raise SystemExit(f"HALT_184_NO_T35_SUBSTRATE: missing {T35_DIR}")

        # ---- Phase A.0: load T35 + substrate SHAs ----
        constants = load_t35_constants()
        substrate_shas: Dict[str, str] = {}
        for rep in REPS:
            csv_p = T37E_DIR / f"a_n_{rep}_dps400_N5000.csv"
            substrate_shas[rep] = sha256_file(csv_p)
            log(
                f"[184] {rep}: zeta_star={mp.nstr(constants[rep]['zeta_star'], 12)} "
                f"C_lsq={mp.nstr(constants[rep]['C_lsq'], 12)} "
                f"S1_imag={mp.nstr(constants[rep]['S1_imag'], 12)} "
                f"sha16={substrate_shas[rep][:16]}",
                run_fh,
            )

        # ---- Phase A.1: stage-1 fits at DPS_FIT (with cache) ----
        if fit_cache_path.exists():
            log(f"[184] Phase A.1: loading cached stage-1 fit from {fit_cache_path.name}", run_fh)
            with fit_cache_path.open("r", encoding="utf-8") as fh:
                fit_cache = json.load(fh)
            stage1_per_rep: Dict[str, Dict] = {}
            a_coefs_per_rep: Dict[str, List[mp.mpf]] = {}
            for rep in REPS:
                if rep not in fit_cache:
                    log(f"[184] cache missing {rep}; will recompute all reps", run_fh)
                    stage1_per_rep = {}
                    a_coefs_per_rep = {}
                    break
                stage1_per_rep[rep] = fit_cache[rep]["diag"]
                a_coefs_per_rep[rep] = [mp.mpf(s) for s in fit_cache[rep]["a_coefs"]]
            if stage1_per_rep:
                log("[184] cache load OK", run_fh)

        if not (fit_cache_path.exists() and stage1_per_rep):
            stage1_per_rep = {}
            a_coefs_per_rep = {}
            mp.mp.dps = DPS_FIT
            log(f"[184] Phase A.1: stage-1 polynomial-correction fits @ dps={DPS_FIT}, K={K_LEAD}", run_fh)
            n_lo, n_hi = FIT_WINDOW
            for rep in REPS:
                t_a = time.time()
                a_window = load_a_series_window(rep, n_lo, n_hi)
                a_coefs, diag = stage1_fit_recurrence(
                    a_window, n_lo, n_hi,
                    constants[rep]["C_lsq"], constants[rep]["zeta_star"], K_LEAD,
                )
                elapsed = time.time() - t_a
                diag["elapsed_sec"] = elapsed
                stage1_per_rep[rep] = diag
                a_coefs_per_rep[rep] = a_coefs
                log(
                    f"[184]   {rep}: a_1={diag['a_1']}  a_25={diag['a_25']}  "
                    f"fit_max_resid={diag['fit_max_residual']}  t={elapsed:.1f}s",
                    run_fh,
                )
            # cache to disk for restartability
            cache_out = {
                rep: {
                    "a_coefs": [mp.nstr(c, DPS_FIT) for c in a_coefs_per_rep[rep]],
                    "diag": stage1_per_rep[rep],
                }
                for rep in REPS
            }
            with fit_cache_path.open("w", encoding="utf-8") as fh:
                json.dump(cache_out, fh, indent=2)
            log(f"[184] stage-1 fit cache written: {fit_cache_path.name}", run_fh)

        # ---- Phase A.2: residual series at small n + decay diagnostics ----
        # We need a_n for n=0..N_MAX_LOAD = 60. Load these once per rep.
        mp.mp.dps = max(DPS_FIT, DPS_PADE)  # use highest precision for downstream
        a_small_per_rep: Dict[str, List[mp.mpf]] = {}
        residuals_per_rep: Dict[str, List[mp.mpf]] = {}
        residual_diag_per_rep: Dict[str, Dict] = {}
        log(f"[184] Phase A.2: residual series construction at small n (0..{N_MAX_LOAD})", run_fh)
        for rep in REPS:
            t_b = time.time()
            a_small = load_a_series_truncated(rep, N_MAX_LOAD)
            a_small_per_rep[rep] = a_small
            residual = make_residual_series_small(
                a_small, a_coefs_per_rep[rep],
                constants[rep]["C_lsq"], constants[rep]["zeta_star"],
                N_MAX_LOAD,
            )
            residuals_per_rep[rep] = residual
            # decay diagnostics at sample n values
            samples = [1, 2, 5, 10, 20, 30, 40, 50, 60]
            diag_samples = []
            for n_chk in samples:
                if n_chk > N_MAX_LOAD:
                    continue
                n_mp = mp.mpf(n_chk)
                L = constants[rep]["C_lsq"] * mp.gamma(n_mp) * mp.power(constants[rep]["zeta_star"], -n_mp)
                rrat = abs(residual[n_chk]) / abs(L) if abs(L) > 0 else mp.mpf("inf")
                diag_samples.append({
                    "n": n_chk,
                    "abs_a_n": mp.nstr(abs(a_small[n_chk]), 8),
                    "abs_residual_n": mp.nstr(abs(residual[n_chk]), 8),
                    "abs_lead_n": mp.nstr(abs(L), 8),
                    "ratio_residual_over_lead": mp.nstr(rrat, 8),
                })
            residual_diag_per_rep[rep] = {
                "samples": diag_samples,
                "elapsed_sec": time.time() - t_b,
            }
            log(f"[184]   {rep}: residual decay at n=40: ratio={diag_samples[6]['ratio_residual_over_lead']}  t={time.time()-t_b:.1f}s", run_fh)

        # ---- Phase B: Borel + Pade [N/M] sweep at small (N,M) ----
        mp.mp.dps = DPS_PADE
        log(f"[184] Phase B: small-(N,M) Pade sweep @ dps={DPS_PADE}, K_LEAD-subtracted Borel", run_fh)
        borel_diag_per_rep: Dict[str, Dict] = {}
        pade_results_per_rep: Dict[str, Dict] = {}
        for rep in REPS:
            t_c = time.time()
            zeta = constants[rep]["zeta_star"]
            b_u = borel_u_coeffs(residuals_per_rep[rep], zeta, N_MAX_LOAD)
            sample_n = [0, 1, 5, 10, 20, 30, 40, 50, 60]
            sample_n = [n for n in sample_n if n <= N_MAX_LOAD]
            borel_diag_per_rep[rep] = {
                "n_loaded": len(b_u),
                "decay_samples": {str(n): mp.nstr(abs(b_u[n]), 25) for n in sample_n},
            }
            cells: List[Dict] = []
            for N in N_GRID:
                for M in M_GRID:
                    if N + M + 1 > N_MAX_LOAD + 1:
                        continue
                    t_cell = time.time()
                    pq = pade_NM(b_u, N, M)
                    if pq is None:
                        cells.append({"N": N, "M": M, "status": "PADE_FAILED"})
                        log(f"[184]   {rep} [{N}/{M}]: PADE_FAILED", run_fh)
                        continue
                    P, Q = pq
                    cand = candidate_S2_from_pade(P, Q, mp.mpf("2"))
                    if cand is None:
                        cells.append({"N": N, "M": M, "status": "NO_POLE_NEAR_2"})
                        log(f"[184]   {rep} [{N}/{M}]: NO_POLE_NEAR_2", run_fh)
                        continue
                    cell = {
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
                        "_S2_mpc": cand["S2_candidate"],
                        "_pole_mpc": cand["pole_u"],
                        "elapsed_sec": time.time() - t_cell,
                    }
                    cells.append(cell)
                    log(f"[184]   {rep} [{N}/{M}]: OK dist_to_2={cell['dist_to_2']}  |S_2|={cell['abs_S2_candidate']}", run_fh)
            pade_results_per_rep[rep] = {
                "rep": rep,
                "zeta_star": mp.nstr(zeta, 25),
                "S1_imag_t35": mp.nstr(constants[rep]["S1_imag"], 25),
                "cells": cells,
                "elapsed_sec": time.time() - t_c,
            }
            log(f"[184] {rep}: Pade sweep done in {time.time()-t_c:.1f}s", run_fh)

        # ---- Phase B.3: Convergence-region detection ----
        log(f"[184] Phase B.3: convergence-region detection (dps/4 threshold = {DPS_PADE//4} digits)", run_fh)
        convergence_per_rep: Dict[str, Dict] = {}
        threshold_digits = mp.mpf(DPS_PADE) / 4
        for rep in REPS:
            cells = pade_results_per_rep[rep]["cells"]
            ok_cells = {(c["N"], c["M"]): c["_S2_mpc"]
                        for c in cells if c["status"] == "OK"}
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
            good_cells = set()
            for ag in agreements:
                if ag["digits"] >= float(threshold_digits):
                    good_cells.add(tuple(ag["cell_a"]))
                    good_cells.add(tuple(ag["cell_b"]))
            consensus_S2 = None
            if len(good_cells) >= 3:
                ss = [ok_cells[c] for c in good_cells]
                consensus_S2 = sum(ss) / len(ss)
            if ok_cells:
                mags = sorted([abs(s) for s in ok_cells.values()])
                half = len(mags) // 2
                if len(mags) % 2 == 1:
                    median_abs = mags[half]
                else:
                    median_abs = (mags[half - 1] + mags[half]) / 2
                span_abs = mags[-1] - mags[0]
                rel_half_range = span_abs / median_abs if median_abs > 0 else mp.mpf("inf")
            else:
                median_abs = mp.mpf("0")
                rel_half_range = mp.mpf("inf")
            best_digits = max((a["digits"] for a in agreements), default=0.0)
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
                "n_pairs_total": len(agreements),
                "best_digits_agreement": best_digits,
                "threshold_digits": float(threshold_digits),
            }
            log(
                f"[184]   {rep}: ok={len(ok_cells)}/{len(N_GRID)*len(M_GRID)}  "
                f"good_above_thresh={len(good_cells)}  "
                f"best_pair_digits={best_digits:.2f}  "
                f"median_abs_S2={mp.nstr(median_abs, 12)}",
                run_fh,
            )

        # ---- Phase C: numerical-instability scan ----
        # HALT_A_NUMERICAL_INSTABILITY trigger: any cell has pole within 1e-10 of u=2
        # with |residue| > 1e10 (unphysical-divergence pattern).
        unstable_cells: List[Dict] = []
        for rep in REPS:
            cells = pade_results_per_rep[rep]["cells"]
            for c in cells:
                if c["status"] != "OK":
                    continue
                dist = mp.mpf(c["dist_to_2"])
                if dist < mp.mpf("1e-10"):
                    res_mag = mp.sqrt(mp.mpf(c["residue_re"])**2 + mp.mpf(c["residue_im"])**2)
                    if res_mag > mp.mpf("1e10"):
                        unstable_cells.append({
                            "rep": rep, "N": c["N"], "M": c["M"],
                            "dist_to_2": c["dist_to_2"],
                            "residue_mag": mp.nstr(res_mag, 12),
                        })

        # ---- Phase D: verdict classification ----
        rep_verdicts: Dict[str, str] = {}
        for rep in REPS:
            info = convergence_per_rep[rep]
            if info["consensus_S2_re"] is not None and info["n_good_cells_above_threshold"] >= 3:
                rep_verdicts[rep] = "EXTRACTED"
            else:
                rep_verdicts[rep] = "PERMANENT_RESIDUAL_G6b_SUBTRACTED"

        # Aggregate halt-mode classification per slot 184 spec.
        if unstable_cells:
            halt_mode = "HALT_A_NUMERICAL_INSTABILITY"
            m8b_verdict = "M8b_S2_NUMERICAL_INSTABILITY_VIA_SUBTRACTED_BOREL_PADE"
            status = "COMPLETE_NUMERICAL_INSTABILITY"
        elif any(v == "EXTRACTED" for v in rep_verdicts.values()):
            halt_mode = "HALT_A_DPS_THRESHOLD_REACHED"
            m8b_verdict = "M8b_S2_EXTRACTED_VIA_SUBTRACTED_BOREL_PADE"
            status = "COMPLETE_EXTRACTED"
        else:
            halt_mode = "HALT_A_RESIDUAL_PATTERN_REPRODUCED"
            m8b_verdict = "M8b_S2_PERMANENT_RESIDUAL_VIA_SUBTRACTED_BOREL_PADE"
            status = "COMPLETE_PERMANENT_RESIDUAL_SUBTRACTED"

        # ---- Serialize and write ----
        pade_results_serializable: Dict[str, Dict] = {}
        for rep in REPS:
            rd = dict(pade_results_per_rep[rep])
            rd["cells"] = [
                {k: v for k, v in c.items() if not k.startswith("_")}
                for c in rd["cells"]
            ]
            pade_results_serializable[rep] = rd

        out = {
            "task_id": "T2-EXECUTOR-T1-156-A-U2-QUADRANT-SUBTRACTED-PADE-184",
            "date": "2026-05-11",
            "dps_pade": DPS_PADE,
            "dps_fit": DPS_FIT,
            "subtraction_order": K_LEAD,
            "fit_window": list(FIT_WINDOW),
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
            "stage1_fit_per_rep": stage1_per_rep,
            "residual_diagnostics": residual_diag_per_rep,
            "borel_diagnostics": borel_diag_per_rep,
            "pade_results_per_rep": pade_results_serializable,
            "convergence_per_rep": convergence_per_rep,
            "unstable_cells": unstable_cells,
            "rep_verdicts": rep_verdicts,
            "m8b_verdict": m8b_verdict,
            "halt_mode": halt_mode,
            "status": status,
            "elapsed_sec": time.time() - t0,
        }
        with out_path.open("w", encoding="utf-8") as fh:
            json.dump(out, fh, indent=2)
        log(f"[184] wrote {out_path.name}", run_fh)
        log(f"[184] M8b verdict: {m8b_verdict}", run_fh)
        log(f"[184] halt_mode: {halt_mode}", run_fh)
        log(f"[184] rep verdicts: {rep_verdicts}", run_fh)
        for rep in REPS:
            info = convergence_per_rep[rep]
            log(
                f"[184] {rep}: ok={info['n_ok_cells']}/{len(N_GRID)*len(M_GRID)}  "
                f"good_above_thresh={info['n_good_cells_above_threshold']}  "
                f"best_pair_digits={info['best_digits_agreement']:.2f}  "
                f"median_abs_S2={info['median_abs_S2_candidates'][:20]}  "
                f"rel_half_range={info['rel_half_range_abs'][:12]}",
                run_fh,
            )
        log(f"[184] total elapsed: {time.time()-t0:.1f}s", run_fh)


if __name__ == "__main__":
    main()
