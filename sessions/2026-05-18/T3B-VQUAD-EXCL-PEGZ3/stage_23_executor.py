#!/usr/bin/env python3
"""
T3B-VQUAD-EXCL-PEGZ3 — Stage 2 + Stage 3 executor.

Pipeline:
  Stage 2 (NUMERIC SWEEP): compute V_quad at 100 dp / 500 dp / 2000 dp via
    backward GCF recurrence with cross-validation depths.
  Stage 3 (PRECISION FILTER): build basis = monomials in {pi, e, G, zeta(3)}
    of total degree <= 3 (35 elements), then run mpmath.pslq on
    [V_quad] + basis at two precision tiers (500 dp and 2050 dp).
    A relation must be stable across both tiers to advance.

Outputs (all written into SLOT_DIR):
  raw_candidates.jsonl        one record per PSLQ tier
  vquad_value_2000dp.txt      the V_quad string at 2000 dp
  basis_enumeration.json      explicit list of basis exponents and labels
  pslq_500dp.json             tier-1 result
  pslq_2050dp.json            tier-2 result
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from itertools import product
from pathlib import Path

import mpmath as mp

SLOT_DIR = Path(__file__).resolve().parent
TASK_ID = "T3B-VQUAD-EXCL-PEGZ3"

# Reference value (from prior workspace work) for sanity gate
VQUAD_REF_50 = "1.197373990688357602448603219937206329704270703231"

# Precision tiers
TIER1_DPS = 100
TIER2_DPS = 500
TIER3_DPS_WORKING = 2200       # gives >= 2000 stable usable digits
TIER3_DPS_TARGET = 2000

# CF depths per tier (convergence ~ k * n^(3/2); empirically safe)
DEPTHS = {
    TIER1_DPS: (400, 600),
    TIER2_DPS: (2000, 2400),
    TIER3_DPS_WORKING: (5000, 6000),
}

# PSLQ parameters
PSLQ_MAXCOEFF = 10**4
PSLQ_TOL_FACTOR_AT_TIER = {
    500: 50,    # tolerance ~ 10^-(500 - 50)
    2050: 80,   # tolerance ~ 10^-(2050 - 80)
}


def compute_vquad(depth: int, dps: int) -> mp.mpf:
    """V_quad = 1 + K_{n>=1} 1/(3n^2+n+1) via backward recurrence."""
    with mp.workdps(dps + 50):
        v = mp.mpf(0)
        for n in range(depth, 0, -1):
            b_n = 3 * n * n + n + 1
            v = mp.mpf(1) / (b_n + v)
        return mp.mpf(1) + v


def agreement_digits(a: mp.mpf, b: mp.mpf, max_dps: int) -> int:
    with mp.workdps(max_dps):
        d = abs(a - b)
        if d == 0:
            return max_dps
        return max(0, int(-float(mp.log10(d))))


def sha256_of_str(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def stage2_numeric_sweep() -> tuple[mp.mpf, dict]:
    log: dict = {"task_id": TASK_ID, "stage": 2, "tiers": []}

    # Tier 1: 100 dp
    print("[Stage 2] Tier 1: V_quad at 100 dp ...", flush=True)
    mp.mp.dps = TIER1_DPS + 50
    t0 = time.time()
    v1a = compute_vquad(DEPTHS[TIER1_DPS][0], TIER1_DPS)
    v1b = compute_vquad(DEPTHS[TIER1_DPS][1], TIER1_DPS)
    agree1 = agreement_digits(v1a, v1b, TIER1_DPS)
    elapsed1 = time.time() - t0

    # Sanity vs reference (50 digits)
    with mp.workdps(100):
        ref = mp.mpf(VQUAD_REF_50)
        ref_diff = abs(v1a - ref)
        ref_agree = 50 if ref_diff == 0 else max(0, int(-float(mp.log10(ref_diff))))

    log["tiers"].append(
        {
            "tier_dps": TIER1_DPS,
            "depths": DEPTHS[TIER1_DPS],
            "agreement_digits": agree1,
            "ref_agreement_digits": ref_agree,
            "wall_seconds": round(elapsed1, 3),
        }
    )
    if ref_agree < 45:
        raise RuntimeError(f"Tier-1 disagreement with reference: only {ref_agree} digits")

    # Tier 2: 500 dp
    print("[Stage 2] Tier 2: V_quad at 500 dp ...", flush=True)
    mp.mp.dps = TIER2_DPS + 50
    t0 = time.time()
    v2a = compute_vquad(DEPTHS[TIER2_DPS][0], TIER2_DPS)
    v2b = compute_vquad(DEPTHS[TIER2_DPS][1], TIER2_DPS)
    agree2 = agreement_digits(v2a, v2b, TIER2_DPS)
    elapsed2 = time.time() - t0
    log["tiers"].append(
        {
            "tier_dps": TIER2_DPS,
            "depths": DEPTHS[TIER2_DPS],
            "agreement_digits": agree2,
            "wall_seconds": round(elapsed2, 3),
        }
    )
    if agree2 < TIER2_DPS:
        raise RuntimeError(f"Tier-2 insufficient agreement: {agree2} < {TIER2_DPS}")

    # Tier 3: 2000 dp (working at 2200)
    print("[Stage 2] Tier 3: V_quad at 2000+ dp ...", flush=True)
    mp.mp.dps = TIER3_DPS_WORKING + 50
    t0 = time.time()
    v3a = compute_vquad(DEPTHS[TIER3_DPS_WORKING][0], TIER3_DPS_WORKING)
    v3b = compute_vquad(DEPTHS[TIER3_DPS_WORKING][1], TIER3_DPS_WORKING)
    agree3 = agreement_digits(v3a, v3b, TIER3_DPS_WORKING)
    elapsed3 = time.time() - t0
    log["tiers"].append(
        {
            "tier_dps_working": TIER3_DPS_WORKING,
            "tier_dps_target": TIER3_DPS_TARGET,
            "depths": DEPTHS[TIER3_DPS_WORKING],
            "agreement_digits": agree3,
            "wall_seconds": round(elapsed3, 3),
        }
    )
    if agree3 < TIER3_DPS_TARGET:
        raise RuntimeError(f"Tier-3 insufficient agreement: {agree3} < {TIER3_DPS_TARGET}")

    # Write canonical 2000-dp string
    with mp.workdps(TIER3_DPS_WORKING):
        v_str = mp.nstr(v3a, TIER3_DPS_TARGET, strip_zeros=False)
    (SLOT_DIR / "vquad_value_2000dp.txt").write_text(v_str + "\n", encoding="utf-8")

    log["vquad_first_64"] = v_str[:66]
    log["vquad_sha256"] = sha256_of_str(v_str)
    log["status"] = "OK"
    return v3a, log


def enumerate_basis() -> list[tuple[tuple[int, int, int, int], str]]:
    """All (a,b,c,d) with a+b+c+d <= 3, in lex order. Labels are pretty strings."""
    names = ["pi", "e", "G", "zeta3"]
    items: list[tuple[tuple[int, int, int, int], str]] = []
    for total in range(0, 4):  # 0..3 inclusive
        for combo in product(range(0, total + 1), repeat=4):
            if sum(combo) != total:
                continue
            parts = []
            for k, exp in zip(names, combo):
                if exp == 0:
                    continue
                parts.append(k if exp == 1 else f"{k}^{exp}")
            label = "1" if not parts else "*".join(parts)
            items.append((combo, label))
    return items


def build_basis_values(dps: int) -> tuple[list[mp.mpf], list[str], list[tuple[int, int, int, int]]]:
    items = enumerate_basis()
    with mp.workdps(dps):
        pi_v = mp.pi
        e_v = mp.e
        G_v = mp.catalan
        z3_v = mp.zeta(3)
        vals: list[mp.mpf] = []
        labels: list[str] = []
        exps: list[tuple[int, int, int, int]] = []
        for combo, label in items:
            a, b, c, d = combo
            val = (pi_v**a) * (e_v**b) * (G_v**c) * (z3_v**d)
            vals.append(val)
            labels.append(label)
            exps.append(combo)
    return vals, labels, exps


def stage3_pslq(v_quad: mp.mpf) -> dict:
    log: dict = {"task_id": TASK_ID, "stage": 3, "tiers": []}

    # ── Build basis once and dump enumeration ──
    items = enumerate_basis()
    expected_size = 35
    if len(items) != expected_size:
        raise RuntimeError(f"Basis enumeration size mismatch: {len(items)} != {expected_size}")
    basis_enum_path = SLOT_DIR / "basis_enumeration.json"
    basis_enum_path.write_text(
        json.dumps(
            {
                "basis_size": len(items),
                "monomial_field": ["pi", "e", "G", "zeta3"],
                "max_total_degree": 3,
                "items": [{"exponents": list(c), "label": lbl} for c, lbl in items],
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    # ── Tier 1 PSLQ: 500 dp ──
    print("[Stage 3] PSLQ at 500 dp ...", flush=True)
    dps_lo = 500
    mp.mp.dps = dps_lo + 30
    with mp.workdps(dps_lo):
        v_lo = mp.mpf(v_quad)  # cast carries enough digits since v_quad has > 2000
        basis_vals, labels, exps = build_basis_values(dps_lo)
        full_lo = [v_lo] + basis_vals
        tol_lo = mp.mpf(10) ** (-(dps_lo - PSLQ_TOL_FACTOR_AT_TIER[500]))
        t0 = time.time()
        try:
            rel_lo = mp.pslq(full_lo, tol=tol_lo, maxcoeff=PSLQ_MAXCOEFF, maxsteps=2000)
        except ValueError as exc:
            rel_lo = None
            err_lo = repr(exc)
        else:
            err_lo = None
        elapsed_lo = time.time() - t0

    tier1 = {
        "tier_dps": dps_lo,
        "tol_exponent": -(dps_lo - PSLQ_TOL_FACTOR_AT_TIER[500]),
        "maxcoeff": PSLQ_MAXCOEFF,
        "basis_size": len(basis_vals),
        "wall_seconds": round(elapsed_lo, 3),
        "result": None if rel_lo is None else [int(c) for c in rel_lo],
        "error": err_lo,
    }
    log["tiers"].append(tier1)
    (SLOT_DIR / "pslq_500dp.json").write_text(json.dumps(tier1, indent=2), encoding="utf-8")
    print(f"  Tier-1 PSLQ result: {tier1['result']}", flush=True)

    # ── Tier 2 PSLQ: 2050 dp ──
    print("[Stage 3] PSLQ at 2050 dp ... (this is the long one)", flush=True)
    dps_hi = 2050
    mp.mp.dps = dps_hi + 30
    with mp.workdps(dps_hi):
        v_hi = mp.mpf(v_quad)
        basis_vals, labels, exps = build_basis_values(dps_hi)
        full_hi = [v_hi] + basis_vals
        tol_hi = mp.mpf(10) ** (-(dps_hi - PSLQ_TOL_FACTOR_AT_TIER[2050]))
        t0 = time.time()
        try:
            rel_hi = mp.pslq(full_hi, tol=tol_hi, maxcoeff=PSLQ_MAXCOEFF, maxsteps=4000)
        except ValueError as exc:
            rel_hi = None
            err_hi = repr(exc)
        else:
            err_hi = None
        elapsed_hi = time.time() - t0

    tier2 = {
        "tier_dps": dps_hi,
        "tol_exponent": -(dps_hi - PSLQ_TOL_FACTOR_AT_TIER[2050]),
        "maxcoeff": PSLQ_MAXCOEFF,
        "basis_size": len(basis_vals),
        "wall_seconds": round(elapsed_hi, 3),
        "result": None if rel_hi is None else [int(c) for c in rel_hi],
        "error": err_hi,
    }
    log["tiers"].append(tier2)
    (SLOT_DIR / "pslq_2050dp.json").write_text(json.dumps(tier2, indent=2), encoding="utf-8")
    print(f"  Tier-2 PSLQ result: {tier2['result']}", flush=True)

    # ── Classification ──
    if tier1["result"] is None and tier2["result"] is None:
        verdict = "NULL"
    elif tier1["result"] is None or tier2["result"] is None:
        verdict = "UNSTABLE_NOISE"
    elif tier1["result"] == tier2["result"]:
        verdict = "STABLE_CANDIDATE"
    else:
        verdict = "UNSTABLE_NOISE"

    log["verdict"] = verdict
    log["status"] = "OK"
    return log


def emit_raw_candidates(stage2_log: dict, stage3_log: dict) -> None:
    path = SLOT_DIR / "raw_candidates.jsonl"
    with path.open("w", encoding="utf-8") as f:
        f.write(json.dumps({"stage": 2, **stage2_log}) + "\n")
        f.write(json.dumps({"stage": 3, **stage3_log}) + "\n")


def main() -> int:
    print(f"=== {TASK_ID} Stages 2+3 executor ===", flush=True)
    print(f"Slot dir: {SLOT_DIR}", flush=True)
    print(f"mpmath version: {mp.__version__}", flush=True)
    print("", flush=True)

    t_start = time.time()
    v_quad, s2_log = stage2_numeric_sweep()
    s3_log = stage3_pslq(v_quad)
    elapsed = time.time() - t_start

    emit_raw_candidates(s2_log, s3_log)
    summary = {
        "task_id": TASK_ID,
        "elapsed_seconds": round(elapsed, 1),
        "stage2_status": s2_log["status"],
        "stage3_status": s3_log["status"],
        "stage3_verdict": s3_log["verdict"],
    }
    (SLOT_DIR / "executor_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print("\n=== DONE ===", flush=True)
    print(json.dumps(summary, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
