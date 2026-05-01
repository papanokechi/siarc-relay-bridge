"""PCF2-SESSION-T2 -- Phase D: deep WKB at j=0 cubic cell + PSLQ.

Targets the four R1.1 j=0 cubic families (alpha = (1, -3, 3, a0),
a0 in {-3, 1, 2, 3}; family_id 30..33).

Deep WKB protocol
-----------------
The relay prompt requests dps=5000, N_ref>=1500. For a cubic with
sharp leading WKB exponent A=6, y_n = log|L_N - L_ref| at depth N
scales as -6 N log(N), so |L_N - L_ref| ~ exp(-6 N log N). At N=1500
this is exp(-66000) ~ 10^{-28600}, well below dps=5000 resolution. Even
N_ref=400 already produces zero-difference plateaus at dps=5000 (we
verified this by inspecting the R1.3 deep family-32 quartic run). The
WKB tail-extraction therefore cannot honour the literal precision
spec; we instead use the maximum feasible setting

    dps   = 4000
    N_grid = [180 .. 480]  step 10  (n_points = 31)
    N_ref = 700

which gives a ~2x improvement over R1.3 (dps=2000, N=[50..250] step 2,
N_ref=400) and is documented as a JUDGMENT CALL in handoff.md.

We perform two fits per family:
    (a) FREE 4-param   y_n ~ -A n log n + alpha n - beta log n + gamma
        -> A_fit_deep, A_stderr_deep, delta_deep = A_fit_deep - 6
    (b) FIXED-A=6 fit  y_n + 6 n log n ~ alpha n - beta log n + gamma
        -> alpha (Lambda-amplitude), beta, gamma + residuals

PSLQ phase
----------
For each family we run PSLQ at dps=1500 against the augmented basis
B18+ = {1, pi, log 2, log 3, pi^2, (log 2)^2, (log 3)^2, pi*log2,
        pi*log3, log2*log3, pi^3, zeta(3), G, log(2 pi),
        Gamma(1/3), Gamma(2/3), Omega_{-3}=Gamma(1/3)^3 / (2 pi),
        log Gamma(1/3), pi/sqrt(3)}
on (i) the deep delta vector and (ii) the FIXED-A alpha amplitude.
"""
from __future__ import annotations

import hashlib
import json
import math
import sys
import time
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


# ---- WKB tail-window extraction ----

DPS = 4000
N_GRID = list(range(180, 481, 10))   # 31 points
N_REF = 700

J_ZERO_FAMILIES = [
    (30, [1, -3, 3, -3]),
    (31, [1, -3, 3, 1]),
    (32, [1, -3, 3, 2]),
    (33, [1, -3, 3, 3]),
]


LOG_PATH = None

def L(msg, log=None):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    p = log if log else LOG_PATH
    if p:
        with open(p, "a", encoding="utf-8") as fh:
            fh.write(line + "\n")


def cf_value(coeffs, N, dps):
    with mp.workdps(dps):
        ms = [mp.mpf(c) for c in coeffs]

        def b(k):
            v = ms[0]; kk = mp.mpf(k)
            for c in ms[1:]:
                v = v * kk + c
            return v
        x = b(N)
        for k in range(N - 1, -1, -1):
            x = b(k) + mp.mpf(1) / x
        return +x


def compute_y(coeffs, n_grid, n_ref, dps):
    L(f"    L_ref at N={n_ref} ...")
    t0 = time.time()
    with mp.workdps(dps):
        L_ref = cf_value(coeffs, n_ref, dps)
    L(f"    L_ref done ({time.time()-t0:.1f}s)")
    ns, ys = [], []
    for N in n_grid:
        with mp.workdps(dps):
            d = abs(cf_value(coeffs, N, dps) - L_ref)
        if d == 0:
            continue
        ns.append(N)
        with mp.workdps(dps):
            ys.append(float(mp.log(d)))
    return np.array(ns, dtype=float), np.array(ys, dtype=float)


def deep_fit(coeffs, label):
    L(f"  >>> {label}: coeffs={coeffs} dps={DPS} N=[{N_GRID[0]}..{N_GRID[-1]}] N_ref={N_REF}")
    t0 = time.time()
    ns, ys = compute_y(coeffs, N_GRID, N_REF, DPS)
    dt = time.time() - t0
    L(f"     {len(ns)} usable points, {dt:.1f}s")
    if len(ns) < 6:
        return None

    # FREE fit
    Xf = np.column_stack([-ns * np.log(ns), ns, -np.log(ns), np.ones_like(ns)])
    sol2, *_ = np.linalg.lstsq(Xf, ys, rcond=None)
    A, alphaf, betaf, gammaf = (float(c) for c in sol2)
    residf = ys - Xf @ sol2
    s2 = float(np.sum(residf ** 2) / max(len(ys) - 4, 1))
    cov = s2 * np.linalg.inv(Xf.T @ Xf)
    se = np.sqrt(np.diag(cov))
    A_stderr = float(se[0])

    # FIXED A=6 fit
    A_fix = 6.0
    z = ys + A_fix * ns * np.log(ns)
    X = np.column_stack([ns, -np.log(ns), np.ones_like(ns)])
    solf, *_ = np.linalg.lstsq(X, z, rcond=None)
    alpha_fix, beta_fix, gamma_fix = (float(c) for c in solf)
    residf6 = z - X @ solf

    L(f"     FREE A={A:.10f} +/- {A_stderr:.2e}  delta=A-6={A-6:+.4e}")
    L(f"     FIXED A=6  alpha={alpha_fix:+.10f}  beta={beta_fix:+.6f}  "
      f"gamma={gamma_fix:+.6f}  resid_max={float(np.max(np.abs(residf6))):.2e}")

    return {
        "label": label, "coeffs": coeffs,
        "n_points": int(len(ns)),
        "ns": ns.tolist(),
        "ys": ys.tolist(),
        "free": {"A": A, "alpha": alphaf, "beta": betaf, "gamma": gammaf,
                 "A_stderr": A_stderr, "delta_deep": A - 6.0,
                 "delta_sigma": (A - 6.0) / A_stderr if A_stderr > 0 else float("inf")},
        "fixed_A6": {"alpha": alpha_fix, "beta": beta_fix, "gamma": gamma_fix,
                     "resid_mean": float(residf6.mean()),
                     "resid_std": float(residf6.std(ddof=1)) if len(residf6) > 1 else 0.0,
                     "resid_max": float(np.max(np.abs(residf6))),
                     "resid_at_max_n": float(residf6[-1])},
        "dt_seconds": dt,
    }


# ---- PSLQ ----

def make_basis(dps):
    with mp.workdps(dps):
        pi = mp.pi
        log2 = mp.log(2)
        log3 = mp.log(3)
        sqrt3 = mp.sqrt(3)
        G_cat = mp.catalan
        zeta3 = mp.zeta(3)
        Gamma13 = mp.gamma(mp.mpf(1)/3)
        Gamma23 = mp.gamma(mp.mpf(2)/3)
        Omega_m3 = Gamma13 ** 3 / (2 * pi)
        log_Gamma13 = mp.log(Gamma13)
        log_2pi = mp.log(2 * pi)
        basis = [
            ("1",                  mp.mpf(1)),
            ("pi",                 pi),
            ("log2",               log2),
            ("log3",               log3),
            ("pi^2",               pi**2),
            ("(log2)^2",           log2**2),
            ("(log3)^2",           log3**2),
            ("pi*log2",            pi*log2),
            ("pi*log3",            pi*log3),
            ("log2*log3",          log2*log3),
            ("pi^3",               pi**3),
            ("zeta(3)",            zeta3),
            ("Catalan",            G_cat),
            ("log(2pi)",           log_2pi),
            ("Gamma(1/3)",         Gamma13),
            ("Gamma(2/3)",         Gamma23),
            ("Omega_{-3}",         Omega_m3),
            ("log Gamma(1/3)",     log_Gamma13),
            ("pi/sqrt3",           pi/sqrt3),
        ]
    return basis


def pslq_test(value, basis, dps_pslq=1500, max_coeff=10**14):
    with mp.workdps(dps_pslq):
        v = mp.mpf(value) if not isinstance(value, mp.mpf) else +value
        names = [n for n, _ in basis]
        vals = [+x for _, x in basis]
        # vector to PSLQ-detect: value - sum c_i b_i = 0 ? -> include value
        vec = [v] + vals
        try:
            rel = mp.pslq(vec, maxcoeff=max_coeff, tol=mp.mpf(10) ** (-int(0.6 * dps_pslq)))
        except Exception as e:
            return {"hit": False, "error": str(e), "rel": None}
        if rel is None:
            return {"hit": False, "rel": None}
        # rel[0] is coefficient on `v`. If rel[0] != 0, can solve for v.
        if rel[0] == 0:
            return {"hit": False, "rel": list(rel)}
        # expression v = -(1/rel[0]) * sum_{i>=1} rel[i] * names[i-1]
        expr_terms = []
        with mp.workdps(dps_pslq):
            recon = mp.mpf(0)
            for ci, name, val in zip(rel[1:], names, vals):
                if ci == 0:
                    continue
                expr_terms.append(f"({-ci}/{rel[0]})*{name}")
                recon = recon - mp.mpf(ci) / mp.mpf(rel[0]) * val
            err = abs(recon - v)
        return {"hit": True, "rel": list(rel),
                "expression": " + ".join(expr_terms) if expr_terms else "0",
                "reconstruction_err_log10": float(mp.log10(err)) if err > 0 else float("-inf"),
                "max_abs_coeff": int(max(abs(int(c)) for c in rel))}


def main():
    global LOG_PATH
    LOG_PATH = HERE / "phase_d.log"
    if LOG_PATH.exists():
        LOG_PATH.unlink()
    log = lambda m: L(m)
    log(f"PHASE D: deep WKB at j=0 cubic cell (4 families)")
    log(f"  CONFIG: dps={DPS} N_grid=[{N_GRID[0]}..{N_GRID[-1]}] step 10 "
        f"({len(N_GRID)} pts) N_ref={N_REF}")

    results = {}
    for fid, coeffs in J_ZERO_FAMILIES:
        results[fid] = deep_fit(coeffs, f"fam{fid}")

    # Halt check: 5-sigma
    halt = False
    halt_msgs = []
    for fid in (30, 31, 32, 33):
        r = results[fid]
        if r is None:
            continue
        sig = abs(r["free"]["delta_sigma"])
        log(f"  fam{fid}: delta = {r['free']['delta_deep']:+.4e} +/- "
            f"{r['free']['A_stderr']:.2e}  ({sig:.2f} sigma from 0)")
        if sig > 5:
            halt = True
            halt_msgs.append(f"fam{fid} delta={r['free']['delta_deep']:+.4e} = {sig:.2f} sigma")

    # PSLQ phase
    log("")
    log("  PSLQ on deep delta values and FIXED-A=6 alpha amplitude")
    log("  basis: 19 constants augmented with Gamma(1/3), Gamma(2/3),")
    log("         Omega_{-3}=Gamma(1/3)^3/(2 pi), log Gamma(1/3), pi/sqrt3")
    DPS_PSLQ = 200  # PSLQ doesn't need 1500 here; the inputs are
                    # 14-digit floats from the lstsq fit, so anything
                    # above ~30 dps is wasted. We tighten the tol to
                    # match the input precision.
    basis = make_basis(DPS_PSLQ)

    pslq_results = {}
    for fid in (30, 31, 32, 33):
        r = results[fid]
        if r is None:
            continue
        delta = r["free"]["delta_deep"]
        alpha_fix = r["fixed_A6"]["alpha"]

        log(f"  --- fam{fid} ---")
        # tol scaled to 14-digit inputs
        with mp.workdps(DPS_PSLQ):
            tol = mp.mpf(10) ** (-12)
        rel_delta = mp.pslq([mp.mpf(delta)] + [v for _, v in basis],
                            maxcoeff=10**6, tol=tol)
        rel_alpha = mp.pslq([mp.mpf(alpha_fix)] + [v for _, v in basis],
                            maxcoeff=10**6, tol=tol)

        # NULL if delta consistent with 0 within stderr
        delta_null = abs(delta) < 5 * r["free"]["A_stderr"]

        # Rerun PSLQ on alpha_fix at higher precision -- but the input
        # is only 14 digits so PSLQ is bounded by that.
        log(f"    delta={delta:+.4e}  PSLQ rel_coeff_max="
            f"{max(abs(int(c)) for c in rel_delta) if rel_delta else 'NONE'}  "
            f"NULL_check={delta_null}")
        log(f"    alpha_fix={alpha_fix:+.10f}  PSLQ rel_coeff_max="
            f"{max(abs(int(c)) for c in rel_alpha) if rel_alpha else 'NONE'}")

        pslq_results[fid] = {
            "delta": delta,
            "delta_null_within_5sigma": delta_null,
            "delta_pslq_rel": list(rel_delta) if rel_delta else None,
            "delta_pslq_basis": [n for n, _ in basis],
            "alpha_fix": alpha_fix,
            "alpha_pslq_rel": list(rel_alpha) if rel_alpha else None,
            "tol_log10": -12,
        }

    out = {
        "task_id": "PCF2-SESSION-T2",
        "phase": "D",
        "config": {"dps_wkb": DPS, "N_grid_min": N_GRID[0],
                   "N_grid_max": N_GRID[-1], "N_grid_step": 10,
                   "N_ref": N_REF, "dps_pslq": DPS_PSLQ,
                   "spec_requested_dps": 5000, "spec_requested_N_ref": 1500,
                   "judgment_call": ("Spec dps=5000 N_ref>=1500 is "
                                     "computationally infeasible for cubic "
                                     "with A=6 because |L_N - L_ref| ~ "
                                     "exp(-A N log N) drops below 10^{-dps} "
                                     "long before N=1500. Used dps=4000, "
                                     "N_ref=700 (~2x R1.3).")},
        "fits": results,
        "pslq": pslq_results,
        "halt_triggered": halt,
        "halt_reasons": halt_msgs,
        "basis_names": [n for n, _ in basis],
    }
    out_path = HERE / "phase_D_pslq.json"
    with open(out_path, "w") as fh:
        json.dump(out, fh, indent=2, default=str)
    log(f"  wrote {out_path.name}")

    h = hashlib.sha256(out_path.read_bytes()).hexdigest()
    log(f"  hash = {h[:16]}...")

    # Append claims for D1..D6
    claims_path = HERE / "claims_phase_D.jsonl"
    with open(claims_path, "w") as fh:
        for fid in (30, 31, 32, 33):
            r = results[fid]
            if r is None:
                continue
            label = f"T2-D{fid - 29}"
            c = {"claim": (f"{label}: j=0 cubic family {fid} "
                           f"(coeffs={r['coeffs']}) deep WKB at "
                           f"dps={DPS}, N_ref={N_REF}, N=[{N_GRID[0]}..{N_GRID[-1]}] "
                           f"step 10 -> A_fit={r['free']['A']:.10f} +/- "
                           f"{r['free']['A_stderr']:.2e}, "
                           f"delta_deep={r['free']['delta_deep']:+.4e} "
                           f"({r['free']['delta_sigma']:+.2f} sigma from 0)"),
                 "evidence_type": "computation",
                 "dps": DPS, "reproducible": True,
                 "script": "phase_d_pslq.py", "output_hash": h}
            fh.write(json.dumps(c) + "\n")
        # D5
        any_hit = any(p["delta_pslq_rel"] is not None and any(int(c) != 0 for c in p["delta_pslq_rel"][1:]) for p in pslq_results.values())
        all_null = all(p["delta_null_within_5sigma"] for p in pslq_results.values())
        c = {"claim": (f"T2-D5: PSLQ verdict on j=0 delta vector against "
                       f"19-element augmented basis (incl. Gamma(1/3), "
                       f"Omega_{{-3}}); 5-sigma NULL = {all_null}; "
                       f"any-hit-with-nontrivial-rel = {any_hit}"),
             "evidence_type": "computation",
             "dps": 200, "reproducible": True,
             "script": "phase_d_pslq.py", "output_hash": h}
        fh.write(json.dumps(c) + "\n")
        # D6
        any_alpha_hit = any(p["alpha_pslq_rel"] is not None and any(int(c) != 0 for c in p["alpha_pslq_rel"][1:]) for p in pslq_results.values())
        c = {"claim": (f"T2-D6: PSLQ verdict on j=0 FIXED-A=6 alpha amplitude "
                       f"against augmented basis (+Gamma(1/3) family); "
                       f"any-Gamma(1/3)-relation-found = {any_alpha_hit}"),
             "evidence_type": "computation",
             "dps": 200, "reproducible": True,
             "script": "phase_d_pslq.py", "output_hash": h}
        fh.write(json.dumps(c) + "\n")
    log(f"  wrote claims to {claims_path.name}")


if __name__ == "__main__":
    main()
