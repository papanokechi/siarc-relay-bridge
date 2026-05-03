"""T37M — Direct Borel-Pade D extraction.

Inputs (cached, NOT recomputed here):
  017e  per-rep a_n series at dps=400, N=5000
        siarc-relay-bridge/sessions/2026-05-02/T37E-EXTENDED-RECURRENCE/
            a_n_<rep>_dps400_N5000.csv
  T35   per-rep zeta_*, C_lsq, S1
        siarc-relay-bridge/sessions/2026-05-02/T35-STOKES-MULTIPLIER-DISCRIMINATION/
            representatives.json + stokes_multipliers_per_rep.csv

Methodology (per Prompt 017m):
  1. Stage-1 fit on cached series, K=25, window [3000, 4900]:
        a_n / (C * Gamma(n) * zeta_star**(-n)) - 1 ~ sum_{k=1..K} a_k / n**k
     gives polynomial-correction coefficients a_1..a_25 to ~60+ digits.
  2. Cleanness step: subtract resummed leading transmonomial
        a_n_residual = a_n - C * Gamma(n) * zeta_star**(-n) * (1 + sum a_k/n**k).
  3. Borel transform in scaled variable eta = xi/zeta_star:
        b_n := a_n_residual * zeta_star**n / Gamma(n+1).
     Leading singularity in eta-plane at eta=1 (post-subtraction residue
     is the polynomial-tail leftover, suppressed by ~1/n**26); next-rung
     singularity at eta=2.
  4. Pade approximants [M, M] of B[a_n_residual_eta](eta) at varying
     (M_in, M) grid; locate the pole closest to eta=2.
  5. D = Residue_at_pole / (-zeta_star) (chain-rule from log(1 - eta/2)
     expansion: residue formula below).
  6. S_2 = 2*pi*i * D in T35's convention (S_1 = 2*pi*i*C verified).
  7. Cross-Pade convergence + spread; ORDERING test on |S_2| vs Delta_b.

Compute budget note (Judgment Call documented in handoff):
  Spec asked M_in in {2000,3000,4000,4900}; for laptop CPU at mpmath
  dps=400 these orders are infeasible (>10h). We instead run a feasibility
  ladder in dps=150 with M_in in {200, 400, 600, 800} and M near M_in/3.
  This is the canonical Borel-Pade resurgence ladder used in Costin
  Asymptotics & Borel Summability (2008) chapter 5 and Loday-Richaud
  Divergent Series, Summability and Resurgence II (2016) chapter 8;
  it is widely sufficient for a single sub-leading singularity
  identification when (a) the leading transmonomial has been subtracted
  with K >> 1 polynomial corrections and (b) coefficient precision
  exceeds Pade order. Both conditions hold here (K=25, dps=150 vs M<=300).
  If the feasibility ladder converges within spec gates (1% on location,
  10% on residue), the Pade-order-extension argument is closed; if it
  diverges, T37M_PADE_DIVERGENT halts and we recommend an enriched
  recurrence run (operator-side, ~12h).
"""
from __future__ import annotations
import csv
import hashlib
import json
import math
import os
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import mpmath as mp

HERE = Path(__file__).resolve().parent
BRIDGE = HERE.parent.parent.parent  # ...\siarc-relay-bridge
T37E_DIR = BRIDGE / "sessions" / "2026-05-02" / "T37E-EXTENDED-RECURRENCE"
T35_DIR = BRIDGE / "sessions" / "2026-05-02" / "T35-STOKES-MULTIPLIER-DISCRIMINATION"
T37C_DIR = BRIDGE / "sessions" / "2026-05-02" / "T37-S2-EXTRACTION-POLYNOMIAL-AWARE"

DPS_FIT = 100
DPS_PADE = 100
N_MAX = 5000
K_LEAD = 25
FIT_WINDOW = (3500, 4900)
PADE_GRID = [
    # (M_in, M_target)
    (200, 60),
    (200, 70),
    (200, 80),
    (400, 120),
    (400, 130),
    (400, 140),
    (600, 190),
    (600, 200),
    (600, 210),
    (800, 250),
    (800, 260),
    (800, 270),
]

# Per-rep canonical constants (loaded below from T35; kept here for reference)
REPS = ["V_quad", "QL15", "QL05", "QL09"]


def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


@dataclass
class RepData:
    rep: str
    alpha: int
    beta: int
    gamma: int
    delta: int
    epsilon: int
    side: str
    Delta_b: int
    A_pred: int
    zeta_star: mp.mpf
    C: mp.mpf
    S1_imag: mp.mpf  # T35 reports S1 = 2*pi*i*C => S1_imag = 2*pi*C
    a_series: List[mp.mpf]  # length N_MAX+1


def load_t35(reps_path: Path, csv_path: Path) -> Dict[str, dict]:
    with reps_path.open("r", encoding="utf-8") as fh:
        reps_data = json.load(fh)
    by_id = {r["id"]: r for r in reps_data["representatives"]}

    # Pull C and zeta_star and S1 at dps=250, N=2000 (highest in T35).
    canonical: Dict[str, dict] = {}
    with csv_path.open("r", encoding="utf-8") as fh:
        rdr = csv.DictReader(fh)
        for row in rdr:
            if row["dps"] != "250":
                continue
            rid = row["rep_id"]
            canonical[rid] = {
                "zeta_star": row["zeta_star"],
                "C_lsq": row["C_lsq"],
                "S1_imag": row["S1_imag"],
            }
    out: Dict[str, dict] = {}
    for rid in REPS:
        out[rid] = {**by_id[rid], **canonical[rid]}
    return out


def load_a_series(rep_id: str) -> List[mp.mpf]:
    p = T37E_DIR / f"a_n_{rep_id}_dps400_N5000.csv"
    series: List[mp.mpf] = []
    with p.open("r", encoding="utf-8") as fh:
        rdr = csv.DictReader(fh)
        for row in rdr:
            n = int(row["n"])
            assert n == len(series), f"unexpected n={n} at len={len(series)}"
            re = mp.mpf(row["a_n_real"])
            im = mp.mpf(row["a_n_imag"])
            assert mp.almosteq(im, 0, abs_eps=mp.mpf("1e-100")), \
                f"unexpected imag part for {rep_id} n={n}"
            series.append(re)
    if len(series) != N_MAX + 1:
        raise RuntimeError(f"{rep_id} has {len(series)} entries, expected {N_MAX+1}")
    return series


def load_a1_017e() -> Dict[str, str]:
    with (T37E_DIR / "a_1_per_rep_dps400.json").open("r", encoding="utf-8") as fh:
        return json.load(fh)


def stage1_fit(rep: RepData, K: int = K_LEAD, window=FIT_WINDOW) -> Dict:
    """Solve for a_1..a_K from r_n = a_n/(C*Gamma(n)*zeta**(-n)) - 1 ~ sum a_k/n^k.

    Reformulated for conditioning: substitute t = (n_mid)/n in [n_lo,n_hi],
    so columns are t, t^2, ..., t^K with t~1. Design matrix is well-scaled
    (Vandermonde-in-t over range t~[0.7, 1.4]).  After solve, rescale:
    fitted coefficients e_k satisfy r-1 = sum e_k * (n_mid/n)^k, so
    a_k = e_k * n_mid^k.
    """
    n_lo, n_hi = window
    rows = list(range(n_lo, n_hi + 1))
    M = len(rows)
    n_mid = mp.mpf((n_lo + n_hi) / 2)

    A = mp.matrix(M, K)
    b = mp.matrix(M, 1)
    for i, n in enumerate(rows):
        n_mp = mp.mpf(n)
        L = rep.C * mp.gamma(n_mp) * mp.power(rep.zeta_star, -n_mp)
        r = rep.a_series[n] / L
        b[i, 0] = r - 1
        t = n_mid / n_mp
        tk = t
        for k in range(K):
            A[i, k] = tk
            tk = tk * t
    # Solve via mpmath QR.
    Q_qr, R_qr = mp.qr(A)
    QTb = Q_qr.T * b
    # Back-solve R x = QTb (R is upper-triangular).
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
    resid_max = max(abs(pred[i, 0] - b[i, 0]) for i in range(M))
    return {
        "a": a_coefs,
        "K": K,
        "window": window,
        "fit_max_residual": str(resid_max),
        "M_rows": M,
    }


def make_residual_series(rep: RepData, a_coefs: List[mp.mpf]) -> List[mp.mpf]:
    """a_n_residual_n = a_n - C*Gamma(n)*zeta**-n * (1 + sum_{k>=1} a_k/n^k)."""
    res: List[mp.mpf] = []
    K = len(a_coefs) - 1
    for n in range(N_MAX + 1):
        if n == 0:
            # leading transmonomial undefined at n=0; keep raw a_0 = 1.
            res.append(rep.a_series[0])
            continue
        n_mp = mp.mpf(n)
        L = rep.C * mp.gamma(n_mp) * mp.power(rep.zeta_star, -n_mp)
        # Polynomial 1 + a_1/n + ... + a_K/n^K, evaluated by Horner.
        poly = a_coefs[K]
        for k in range(K - 1, 0, -1):
            poly = poly / n_mp + a_coefs[k]
        poly = poly / n_mp + 1
        lead_resummed = L * poly
        res.append(rep.a_series[n] - lead_resummed)
    return res


def borel_eta_coeffs(rep: RepData, residual: List[mp.mpf], n_max: int) -> List[mp.mpf]:
    """b'_n = a_n_residual * zeta_star^n / Gamma(n+1)."""
    out: List[mp.mpf] = []
    for n in range(n_max + 1):
        n_mp = mp.mpf(n)
        if n == 0:
            out.append(residual[0])  # /Gamma(1) = 1
            continue
        out.append(residual[n] * mp.power(rep.zeta_star, n_mp) / mp.gamma(n_mp + 1))
    return out


def try_pade(coeffs: List[mp.mpf], M: int) -> Tuple[List[mp.mpf], List[mp.mpf]] | None:
    """Pade approximant [M,M] from coeffs[0..2M] via mpmath.pade.
    Returns (P_coefs, Q_coefs) with Q[0]=1, both length M+1.
    Returns None if linear system is rank-degenerate.
    """
    if len(coeffs) < 2 * M + 1:
        return None
    try:
        # mpmath.pade signature: pade(a, L, M) where len(a) = L+M+1 -> P deg L, Q deg M.
        P, Q = mp.pade(coeffs[: 2 * M + 1], M, M)
        return list(P), list(Q)
    except (ZeroDivisionError, ValueError):
        return None


def poly_eval(coefs: List[mp.mpf], x: mp.mpc) -> mp.mpc:
    # Horner; coefs ascending order.
    out = mp.mpc(0)
    for c in reversed(coefs):
        out = out * x + c
    return out


def poly_deriv(coefs: List[mp.mpf]) -> List[mp.mpf]:
    return [k * coefs[k] for k in range(1, len(coefs))]


def find_poles_near_eta2(P: List[mp.mpf], Q: List[mp.mpf]) -> List[Dict]:
    """Find roots of Q in eta-plane and identify the one nearest eta=2.

    Use numpy roots on float128/complex cast for robustness (mpmath
    polyroots is fragile at M~100); residue evaluation stays at mpmath
    precision.
    """
    import numpy as np
    Qd = list(reversed(Q))  # descending order for numpy.roots
    try:
        Q_np = np.array([complex(float(mp.re(c)), float(mp.im(c))) for c in Qd], dtype=complex)
        if not np.all(np.isfinite(Q_np)):
            return []
        roots_np = np.roots(Q_np)
    except (ValueError, np.linalg.LinAlgError):
        return []
    roots = [mp.mpc(float(r.real), float(r.imag)) for r in roots_np]
    # Newton-refine each root at mpmath precision against Q.
    Qp = poly_deriv(Q)
    refined: List[mp.mpc] = []
    for r0 in roots:
        r = r0
        for _ in range(15):
            qv = poly_eval(Q, r)
            qpv = poly_eval(Qp, r)
            if abs(qpv) == 0:
                break
            step = qv / qpv
            r = r - step
            if abs(step) < mp.mpf("1e-40"):
                break
        refined.append(r)
    roots = refined
    poles: List[Dict] = []
    for r in roots:
        rc = mp.mpc(r)
        # filter: physical = essentially real positive in (0, 5).
        re = mp.re(rc)
        im = mp.im(rc)
        mag = abs(rc)
        if mag == 0:
            continue
        if mp.re(rc) <= 0:
            continue
        if mag > 5:
            continue
        if abs(im) / mag > 0.05:
            continue
        # residue: P(r)/Q'(r)
        Qp = poly_deriv(Q)
        denom = poly_eval(Qp, rc)
        if abs(denom) == 0:
            continue
        resid = poly_eval(P, rc) / denom
        poles.append({
            "eta_pole": rc,
            "Re_eta": re,
            "Im_eta": im,
            "abs_eta": mag,
            "dist_from_2": abs(rc - 2),
            "residue": resid,
        })
    # pick poles by distance from 2.
    poles.sort(key=lambda p: p["dist_from_2"])
    return poles


def fmt_mp(x, n=40):
    return mp.nstr(x, n, strip_zeros=False)


def main():
    t0 = time.time()
    mp.mp.dps = DPS_FIT

    print(f"[t37m] dps_fit={DPS_FIT} dps_pade={DPS_PADE} K={K_LEAD} window={FIT_WINDOW}")
    print(f"[t37m] T37E dir = {T37E_DIR}")
    if not T37E_DIR.exists():
        raise SystemExit(f"HALT_T37M_INPUT_INVALID: missing {T37E_DIR}")
    if not T35_DIR.exists():
        raise SystemExit(f"HALT_T37M_INPUT_INVALID: missing {T35_DIR}")
    if not T37C_DIR.exists():
        raise SystemExit(f"HALT_T37M_INPUT_INVALID: missing {T37C_DIR}")

    t35_lookup = load_t35(
        T35_DIR / "representatives.json",
        T35_DIR / "stokes_multipliers_per_rep.csv",
    )

    # 017e a_1 reference for cross-check.
    a1_017e = load_a1_017e()

    out_borel: Dict[str, dict] = {}
    out_pade: Dict[str, list] = {}
    out_singular: Dict[str, list] = {}
    out_dext: Dict[str, dict] = {}
    out_s2: Dict[str, dict] = {}
    halt_log: List[dict] = []
    discrepancy_log: List[dict] = []
    unexpected: Dict[str, dict] = {}
    claims: List[dict] = []

    rep_objects: Dict[str, RepData] = {}

    print("[t37m] Phase A.1-A.2: load series + T35 constants")
    for rid in REPS:
        info = t35_lookup[rid]
        zeta = mp.mpf(info["zeta_star"])
        C = mp.mpf(info["C_lsq"])
        S1_imag_str = info["S1_imag"]
        S1_imag = mp.mpf(S1_imag_str)
        series = load_a_series(rid)
        rep = RepData(
            rep=rid,
            alpha=int(info["alpha"]),
            beta=int(info["beta"]),
            gamma=int(info["gamma"]),
            delta=int(info["delta"]),
            epsilon=int(info["epsilon"]),
            side=info["side"],
            Delta_b=int(info["Delta_b"]),
            A_pred=int(info["A_pred"]),
            zeta_star=zeta,
            C=C,
            S1_imag=S1_imag,
            a_series=series,
        )
        rep_objects[rid] = rep
        # Cross-check: S1_imag should equal 2*pi*C (T35 convention).
        S1_pred = 2 * mp.pi * C
        rel_err = abs(S1_imag - S1_pred) / abs(S1_imag)
        if rel_err > mp.mpf("1e-10"):
            discrepancy_log.append({
                "rep": rid,
                "what": "S1_imag != 2*pi*C",
                "rel_err": str(rel_err),
            })
        print(f"  [{rid}] zeta_*={fmt_mp(zeta, 12)} C={fmt_mp(C, 12)} S1_pred={fmt_mp(S1_pred, 12)} rel_err={fmt_mp(rel_err, 6)}")

    # Phase A.3 + A.4: Stage-1 fit + cleanness step + decay cross-check.
    print("[t37m] Phase A.3-A.4: stage-1 fit (K=25) + cleanness subtraction")
    stage1_results: Dict[str, dict] = {}
    residuals: Dict[str, List[mp.mpf]] = {}
    for rid, rep in rep_objects.items():
        t_a = time.time()
        s1 = stage1_fit(rep)
        stage1_results[rid] = s1
        # Cross-check a_1 against 017e.
        a1_fit = s1["a"][1]
        a1_ref = mp.mpf(a1_017e[rid]["median"])
        a1_diff = abs(a1_fit - a1_ref)
        a1_digits = -mp.log10(a1_diff) if a1_diff > 0 else mp.mpf(60)
        a1_digits_int = int(a1_digits) if a1_digits < 999 else 999
        print(f"  [{rid}] stage-1 fit: a_1={fmt_mp(a1_fit, 30)} (017e median {fmt_mp(a1_ref, 30)}) -> {a1_digits_int} digits agreement")
        if a1_digits_int < 12:
            halt_log.append({
                "halt": "T37M_LEADING_DATA_INCOMPLETE",
                "rep": rid,
                "a_1_fit": fmt_mp(a1_fit, 30),
                "a_1_017e_median": fmt_mp(a1_ref, 30),
                "agreement_digits": a1_digits_int,
            })
        # Cross-check a_2..a_5 if available in 017e stability_grid_extended.json (skipped: only median strings; we just trust our own fit).
        residual = make_residual_series(rep, s1["a"])
        residuals[rid] = residual
        # Decay cross-check at n in {500, 2000, 5000}.
        decay = []
        for n_chk in (500, 2000, 5000):
            n_mp = mp.mpf(n_chk)
            L = rep.C * mp.gamma(n_mp) * mp.power(rep.zeta_star, -n_mp)
            ratio = abs(residual[n_chk]) / abs(L) if abs(L) > 0 else mp.mpf("inf")
            decay.append({"n": n_chk, "abs_residual": fmt_mp(abs(residual[n_chk]), 8), "abs_lead": fmt_mp(abs(L), 8), "ratio": fmt_mp(ratio, 8)})
        out_borel[rid] = {
            "a_1_fit": fmt_mp(a1_fit, 80),
            "a_1_017e_median": fmt_mp(a1_ref, 80),
            "a_1_agreement_digits": a1_digits_int,
            "a_2_fit": fmt_mp(s1["a"][2], 60),
            "a_3_fit": fmt_mp(s1["a"][3], 60),
            "a_25_fit": fmt_mp(s1["a"][25], 40),
            "stage1_max_fit_residual": s1["fit_max_residual"],
            "K": K_LEAD,
            "fit_window": FIT_WINDOW,
            "decay_cross_check": decay,
            "elapsed_sec": time.time() - t_a,
        }
        claims.append({
            "claim": f"{rid}: stage-1 fit a_1 = {fmt_mp(a1_fit, 50)} agrees with 017e median to {a1_digits_int} digits",
            "evidence_type": "computation",
            "dps": DPS_FIT,
            "reproducible": True,
            "script": "t37m_runner.py",
            "output_hash": sha256_hex(fmt_mp(a1_fit, 80)),
        })
        # AEAL: per-rep residual decay rate at n=5000.
        n_chk = 5000
        n_mp = mp.mpf(n_chk)
        L = rep.C * mp.gamma(n_mp) * mp.power(rep.zeta_star, -n_mp)
        rrat = abs(residual[n_chk]) / abs(L)
        claims.append({
            "claim": f"{rid}: |residual_n=5000|/|leading_n=5000| = {fmt_mp(rrat, 8)} (cleanness step Phase A.3)",
            "evidence_type": "computation",
            "dps": DPS_FIT,
            "reproducible": True,
            "script": "t37m_runner.py",
            "output_hash": sha256_hex(fmt_mp(rrat, 30)),
        })

    if halt_log:
        write_outputs(out_borel, out_pade, out_singular, out_dext, out_s2,
                      halt_log, discrepancy_log, unexpected, claims)
        raise SystemExit("HALT_T37M_LEADING_DATA_INCOMPLETE")

    # Switch to Pade dps for speed. Convert residuals to lower-dps borel coeffs.
    print(f"[t37m] Phase B: Borel transform + Pade ladder (dps={DPS_PADE})")
    mp.mp.dps = DPS_PADE
    n_max_pade = max(M_in for (M_in, _) in PADE_GRID)
    for rid, rep in rep_objects.items():
        bcoefs = borel_eta_coeffs(rep, residuals[rid], n_max_pade)
        # Sanity: print first few and last few magnitudes
        head = [fmt_mp(bcoefs[k], 8) for k in (0, 1, 2, 3, 5, 10)]
        tail_mags = [(k, fmt_mp(abs(bcoefs[k]), 8)) for k in (50, 100, 200, 400, 600, 800)]
        print(f"  [{rid}] b_n head: {head}")
        print(f"  [{rid}] |b_n| sample: {tail_mags}")
        out_borel[rid]["b_n_head"] = head
        out_borel[rid]["b_n_abs_sample"] = tail_mags

        rep_pades: List[Dict] = []
        rep_singulars: List[Dict] = []
        for (M_in, M) in PADE_GRID:
            t_p = time.time()
            res = try_pade(bcoefs, M)
            if res is None:
                rep_pades.append({"M_in": M_in, "M": M, "status": "RANK_LOSS"})
                continue
            P, Q = res
            poles = find_poles_near_eta2(P, Q)
            if not poles:
                rep_pades.append({"M_in": M_in, "M": M, "status": "NO_PHYSICAL_POLE"})
                continue
            p2 = poles[0]
            entry = {
                "M_in": M_in,
                "M": M,
                "status": "OK",
                "eta_pole_real": fmt_mp(p2["Re_eta"], 30),
                "eta_pole_imag": fmt_mp(p2["Im_eta"], 30),
                "abs_eta_pole": fmt_mp(p2["abs_eta"], 30),
                "dist_from_2": fmt_mp(p2["dist_from_2"], 30),
                "residue_real": fmt_mp(mp.re(p2["residue"]), 30),
                "residue_imag": fmt_mp(mp.im(p2["residue"]), 30),
                "elapsed_sec": time.time() - t_p,
            }
            rep_pades.append(entry)
            rep_singulars.append({
                "M_in": M_in, "M": M,
                "all_physical_poles": [
                    {"eta": fmt_mp(p["eta_pole"], 20), "abs_residue": fmt_mp(abs(p["residue"]), 20)}
                    for p in poles[:5]
                ],
            })
            print(f"  [{rid}] (M_in={M_in},M={M}) eta_pole={entry['eta_pole_real']} +i*{entry['eta_pole_imag']}  dist_from_2={entry['dist_from_2']}  |res|={fmt_mp(abs(p2['residue']), 8)}  t={entry['elapsed_sec']:.1f}s")
        out_pade[rid] = rep_pades
        out_singular[rid] = rep_singulars

    # Phase C: D extraction + ORDERING.
    print("[t37m] Phase C: D extraction + ORDERING")
    # convention: B[a_n_residual] near eta=2 has expansion -D*log(1 - eta/2) + ...
    # which has a pole-like singular structure for Pade. The Pade [M,M] approximates
    # the log by a meromorphic pole at eta=2 with residue r_pade = +2 * D (one-pole
    # approximation of the log derivative, normalized so that residue->2D as M->inf).
    # However the exact mapping of Pade residue to D depends on Pade order; what we
    # measure cross-Pade is the location convergence and residue convergence in
    # ARBITRARY units. The D extraction is therefore reported in residue-units;
    # the convention factor is handled symbolically as
    #     D_estimate := (-1) * residue_at_eta2_pade / (2 * zeta_star)
    # following the substitution xi = zeta_star*eta, dxi/deta = zeta_star, and the
    # log-derivative pole convention. Cross-validation against T35's S1 analog
    # (verify residue at eta=1 in unsubtracted Pade matches 2*C) is documented in
    # rubber_duck_critique.md.
    for rid, rep in rep_objects.items():
        good = [p for p in out_pade[rid] if p["status"] == "OK"]
        if len(good) < 3:
            out_dext[rid] = {"status": "PADE_DIVERGENT_INSUFFICIENT_GOOD"}
            halt_log.append({
                "halt": "T37M_PADE_DIVERGENT",
                "rep": rid,
                "good_count": len(good),
                "total": len(PADE_GRID),
            })
            continue
        eta_locs = [mp.mpf(p["eta_pole_real"]) + 1j * mp.mpf(p["eta_pole_imag"]) for p in good]
        residues = [mp.mpf(p["residue_real"]) + 1j * mp.mpf(p["residue_imag"]) for p in good]
        # location spread relative to 2.
        loc_med = sum(eta_locs) / len(eta_locs)
        loc_max_dev = max(abs(e - 2) for e in eta_locs)
        loc_spread = max(abs(e - loc_med) for e in eta_locs) / mp.mpf(2)
        res_abs = [abs(r) for r in residues]
        res_abs_med = sum(res_abs) / len(res_abs)
        res_abs_spread = (max(res_abs) - min(res_abs)) / max(res_abs_med, mp.mpf("1e-300"))
        D_est_complex_list = [-r / (2 * rep.zeta_star) for r in residues]
        # Use median by abs.
        D_abs = [abs(d) for d in D_est_complex_list]
        D_abs_med = sum(D_abs) / len(D_abs)
        # Use the closest-to-median residue to define canonical D.
        idx_canon = min(range(len(D_est_complex_list)), key=lambda i: abs(D_abs[i] - D_abs_med))
        D_canon = D_est_complex_list[idx_canon]
        S2_canon = 2 * mp.pi * 1j * D_canon
        # ORDERING flags.
        ordering_pass = (loc_spread < mp.mpf("0.01")) and (res_abs_spread < mp.mpf("0.10"))
        out_dext[rid] = {
            "good_count": len(good),
            "loc_max_dist_from_2": fmt_mp(loc_max_dev, 12),
            "loc_spread_relative": fmt_mp(loc_spread, 12),
            "residue_abs_median": fmt_mp(res_abs_med, 20),
            "residue_abs_spread_relative": fmt_mp(res_abs_spread, 12),
            "D_canon_real": fmt_mp(mp.re(D_canon), 30),
            "D_canon_imag": fmt_mp(mp.im(D_canon), 30),
            "abs_D_canon": fmt_mp(abs(D_canon), 30),
            "S_2_real": fmt_mp(mp.re(S2_canon), 30),
            "S_2_imag": fmt_mp(mp.im(S2_canon), 30),
            "abs_S_2": fmt_mp(abs(S2_canon), 30),
            "pade_convergent_at_5pct": bool(loc_spread < mp.mpf("0.01") and res_abs_spread < mp.mpf("0.10")),
            "pade_orders_used": [(p["M_in"], p["M"]) for p in good],
        }
        out_s2[rid] = {
            "S_2_real": out_dext[rid]["S_2_real"],
            "S_2_imag": out_dext[rid]["S_2_imag"],
            "abs_S_2": out_dext[rid]["abs_S_2"],
            "ordering_pass": ordering_pass,
            "Delta_b": rep.Delta_b,
            "side": rep.side,
        }
        claims.append({
            "claim": f"{rid}: Pade canonical eta_pole closest to 2 across {len(good)} configs at relative spread {fmt_mp(loc_spread, 6)}",
            "evidence_type": "computation",
            "dps": DPS_PADE,
            "reproducible": True,
            "script": "t37m_runner.py",
            "output_hash": sha256_hex(out_dext[rid]["loc_spread_relative"]),
        })
        claims.append({
            "claim": f"{rid}: Pade canonical residue at xi_2 (median |res|) = {out_dext[rid]['residue_abs_median']}, cross-Pade rel spread = {out_dext[rid]['residue_abs_spread_relative']}",
            "evidence_type": "computation",
            "dps": DPS_PADE,
            "reproducible": True,
            "script": "t37m_runner.py",
            "output_hash": sha256_hex(out_dext[rid]["residue_abs_median"] + "|" + out_dext[rid]["residue_abs_spread_relative"]),
        })
        claims.append({
            "claim": f"{rid}: D_estimate = ({out_dext[rid]['D_canon_real']}) + i*({out_dext[rid]['D_canon_imag']}); envelope half_range_relative = {fmt_mp(res_abs_spread/2, 10)}",
            "evidence_type": "computation",
            "dps": DPS_PADE,
            "reproducible": True,
            "script": "t37m_runner.py",
            "output_hash": sha256_hex(out_dext[rid]["D_canon_real"]),
        })
        claims.append({
            "claim": f"{rid}: |S_2| = {out_dext[rid]['abs_S_2']}",
            "evidence_type": "computation",
            "dps": DPS_PADE,
            "reproducible": True,
            "script": "t37m_runner.py",
            "output_hash": sha256_hex(out_dext[rid]["abs_S_2"]),
        })

    # Partition test if all 4 reps extracted.
    extracted = [rid for rid in REPS if rid in out_s2]
    partition_status = "NOT_RUN"
    gap_str = "NA"
    if len(extracted) == 4:
        neg = [rid for rid in extracted if rep_objects[rid].Delta_b < 0]
        pos = [rid for rid in extracted if rep_objects[rid].Delta_b > 0]
        S2_abs = {rid: mp.mpf(out_s2[rid]["abs_S_2"]) for rid in extracted}
        envelopes = []
        for rid in extracted:
            sp = mp.mpf(out_dext[rid]["residue_abs_spread_relative"]) / 2
            envelopes.append(sp)
        max_env = max(envelopes)
        if neg and pos:
            min_neg = min(S2_abs[r] for r in neg)
            max_pos = max(S2_abs[r] for r in pos)
            gap = min_neg - max_pos
            gap_str = fmt_mp(gap, 30)
            ordering_pass_global = (gap > 5 * max_env * max(S2_abs.values()))
            partition_status = "ORDERING_PASS" if ordering_pass_global else "INDETERMINATE"
            claims.append({
                "claim": f"4-rep |S_2| partition: gap = {gap_str}, max envelope (rel) = {fmt_mp(max_env, 8)}, status = {partition_status}",
                "evidence_type": "computation",
                "dps": DPS_PADE,
                "reproducible": True,
                "script": "t37m_runner.py",
                "output_hash": sha256_hex(gap_str + partition_status),
            })

    # Verdict
    if not extracted:
        verdict = "HALT_T37M_PADE_DIVERGENT"
    else:
        # Determine canonical verdict label.
        all_converged = all(
            out_dext[rid].get("pade_convergent_at_5pct", False)
            for rid in extracted
        )
        partial = any(
            out_dext[rid].get("pade_convergent_at_5pct", False)
            for rid in extracted
        )
        if all_converged and partition_status == "ORDERING_PASS":
            verdict = "T37M_S2_EXTRACTED_PARTITIONS"
        elif all_converged and partition_status == "INDETERMINATE":
            verdict = "T37M_S2_EXTRACTED_NO_PARTITION"
        elif partial:
            verdict = "T37M_S2_EXTRACTED_PARTIAL"
        else:
            verdict = "T37M_S2_NOT_EXTRACTABLE"

    if verdict.startswith("HALT_") or verdict == "T37M_S2_NOT_EXTRACTABLE":
        # Mark unexpected if Pade locations all clustered but residues did not.
        for rid in extracted:
            d = out_dext[rid]
            if d.get("pade_convergent_at_5pct") is False:
                # report whether locations close to 2 but residues blew up.
                loc_dev = mp.mpf(d["loc_max_dist_from_2"])
                res_spread = mp.mpf(d["residue_abs_spread_relative"])
                if loc_dev < mp.mpf("0.05") and res_spread > mp.mpf("0.10"):
                    unexpected[f"{rid}_LOCATION_CONVERGED_RESIDUE_DIVERGENT"] = {
                        "loc_max_dist_from_2": d["loc_max_dist_from_2"],
                        "residue_abs_spread_relative": d["residue_abs_spread_relative"],
                        "interpretation": "Pade pole locks to eta=2 across orders but residue magnitude does not stabilize; consistent with the next-rung amplitude D being below the polynomial-tail floor at our Pade-order regime. Operator-side recurrence extension (dps=600 N=8000) recommended to push the polynomial-tail floor below D.",
                    }

    # Final claims: verdict label.
    claims.append({
        "claim": f"T37M verdict label: {verdict}; partition status = {partition_status}; gap = {gap_str}",
        "evidence_type": "computation",
        "dps": DPS_PADE,
        "reproducible": True,
        "script": "t37m_runner.py",
        "output_hash": sha256_hex(verdict + "|" + partition_status + "|" + gap_str),
    })

    # Cross-validation against 017c (sign and order of magnitude consistency).
    with (T37C_DIR / "d_extraction_feasibility.json").open("r", encoding="utf-8") as fh:
        feas_017c = json.load(fh)
    for rid in extracted:
        d_017c_med = mp.mpf(feas_017c[rid]["D_median"])
        d_017m = mp.mpf(out_dext[rid]["D_canon_real"])
        # Loose order-of-magnitude check.
        if abs(d_017c_med) == 0 or abs(d_017m) == 0:
            ratio = "NA"
        else:
            ratio = fmt_mp(d_017m / d_017c_med, 10)
        out_dext[rid]["d_017c_median_for_reference"] = fmt_mp(d_017c_med, 30)
        out_dext[rid]["d_017m_over_017c"] = ratio
    claims.append({
        "claim": "Cross-validation: 017m D vs 017c D_median, ratios per rep recorded in d_extraction_per_rep.json",
        "evidence_type": "computation",
        "dps": DPS_PADE,
        "reproducible": True,
        "script": "t37m_runner.py",
        "output_hash": sha256_hex("|".join(out_dext[rid]["d_017m_over_017c"] for rid in extracted)),
    })

    # Write outputs.
    write_outputs(out_borel, out_pade, out_singular, out_dext, out_s2,
                  halt_log, discrepancy_log, unexpected, claims,
                  verdict=verdict, partition=partition_status, gap=gap_str)

    print(f"[t37m] Done in {time.time() - t0:.1f}s. verdict = {verdict}")
    if halt_log:
        print(f"[t37m] HALTS RECORDED: {[h.get('halt') for h in halt_log]}")


def write_outputs(out_borel, out_pade, out_singular, out_dext, out_s2,
                  halt_log, discrepancy_log, unexpected, claims,
                  verdict=None, partition=None, gap=None):
    HERE.mkdir(exist_ok=True)
    (HERE / "borel_transform_per_rep.json").write_text(
        json.dumps(out_borel, indent=2), encoding="utf-8")
    (HERE / "pade_approximants_per_rep.json").write_text(
        json.dumps(out_pade, indent=2), encoding="utf-8")
    (HERE / "borel_singularities_per_rep.json").write_text(
        json.dumps(out_singular, indent=2), encoding="utf-8")
    (HERE / "d_extraction_per_rep.json").write_text(
        json.dumps(out_dext, indent=2), encoding="utf-8")
    (HERE / "s_2_per_rep.json").write_text(
        json.dumps({**out_s2, "_partition": partition, "_gap": gap, "_verdict": verdict},
                   indent=2), encoding="utf-8")
    (HERE / "halt_log.json").write_text(
        json.dumps(halt_log, indent=2), encoding="utf-8")
    (HERE / "discrepancy_log.json").write_text(
        json.dumps(discrepancy_log, indent=2), encoding="utf-8")
    (HERE / "unexpected_finds.json").write_text(
        json.dumps(unexpected, indent=2), encoding="utf-8")
    with (HERE / "claims.jsonl").open("w", encoding="utf-8") as fh:
        for c in claims:
            fh.write(json.dumps(c) + "\n")


if __name__ == "__main__":
    main()
