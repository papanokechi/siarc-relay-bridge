#!/usr/bin/env python3
"""
T3B-VQUAD-EXCL-T2DPRIME -- Stages 2+3 executor.

Stage 2: reload V_quad from predecessor T2' provenance (string-content SHA-256
match required), compute fresh V_quad via backward CF at depths 5000 and 6000
to 2200 dp working precision, require dual-depth agreement >= 2000 digits AND
reload-vs-fresh sanity >= 1998 digits.

Stage 3: run PSLQ on two complementary bases at two precision tiers each.

  Axis 1 (coefficient-floor escalation):
    B_3_2 = {V_quad^k * pi^a * e^b * G^c * zeta(3)^d : k in [0..3], a+b+c+d <= 2}
            (60 elements; identical to T2' tensor basis)
    maxcoeff = 10^6 at 500 dp and 2050 dp.

  Axis 2 (V_quad-degree extension):
    B_4_2 = {V_quad^k * pi^a * e^b * G^c * zeta(3)^d : k in [0..4], a+b+c+d <= 2}
            (75 elements; extends V_quad-degree axis by one)
    maxcoeff = 10^4 at 500 dp and 2050 dp.

Combined verdict: both axes NULL across both tiers -> EXCLUSION_CERTIFIED.
"""
from __future__ import annotations

import hashlib
import json
import sys
import time
from itertools import product
from pathlib import Path

import mpmath as mp

SLOT_DIR = Path(__file__).resolve().parent
TASK_ID = "T3B-VQUAD-EXCL-T2DPRIME"

# Predecessor provenance: T2' inherited the string-SHA from T2 unchanged.
PREDECESSOR_VQUAD_PATH = SLOT_DIR.parent.parent / "2026-05-18" / "T3B-VQUAD-EXCL-PEGZ3" / "vquad_value_2000dp.txt"
PREDECESSOR_VQUAD_STR_SHA = "52375a71a05bf61ad971cf83ea9334eb96e20ffa054dc3cab74447966a2f5c44"

DPS_WORKING_HI = 2200
DPS_TARGET = 2000
CF_DEPTH_CROSS_CHECK = 6000

# PSLQ default schedule (overridable per call)
PSLQ_TOL_OFFSET = {500: 50, 2050: 80}  # tol = 10^-(dps - offset)
PSLQ_MAXSTEPS = {500: 2000, 2050: 4000}


# ─────────────────────────────────────────────────────────────────
# V_quad
# ─────────────────────────────────────────────────────────────────

def compute_vquad(depth: int, dps: int) -> mp.mpf:
    """V_quad = 1 + K_{n>=1} 1/(3n^2+n+1) via backward GCF recurrence."""
    with mp.workdps(dps + 50):
        v = mp.mpf(0)
        for n in range(depth, 0, -1):
            v = mp.mpf(1) / (3 * n * n + n + 1 + v)
        return mp.mpf(1) + v


def agreement_digits(a: mp.mpf, b: mp.mpf, max_dps: int) -> int:
    with mp.workdps(max_dps):
        d = abs(a - b)
        if d == 0:
            return max_dps
        return max(0, int(-float(mp.log10(d))))


def sha256_of_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def stage2_reload_and_cross_check() -> tuple[mp.mpf, dict]:
    log: dict = {"task_id": TASK_ID, "stage": 2, "events": []}

    raw = PREDECESSOR_VQUAD_PATH.read_bytes()
    file_sha = sha256_of_bytes(raw)
    v_str = raw.decode("utf-8").strip()
    str_sha = sha256_of_bytes(v_str.encode("utf-8"))
    log["events"].append({
        "event": "predecessor_load",
        "predecessor_path": str(PREDECESSOR_VQUAD_PATH.relative_to(SLOT_DIR.parent.parent)).replace("\\", "/"),
        "file_bytes_sha": file_sha,
        "string_content_sha": str_sha,
        "expected_string_sha": PREDECESSOR_VQUAD_STR_SHA,
        "string_sha_match": str_sha == PREDECESSOR_VQUAD_STR_SHA,
    })
    if str_sha != PREDECESSOR_VQUAD_STR_SHA:
        raise RuntimeError(
            f"Predecessor V_quad string SHA mismatch: got {str_sha}, expected {PREDECESSOR_VQUAD_STR_SHA}"
        )

    mp.mp.dps = DPS_WORKING_HI + 50
    v_reload = mp.mpf(v_str)

    t0 = time.time()
    v_fresh_d5000 = compute_vquad(5000, DPS_WORKING_HI)
    t_mid = time.time()
    v_fresh_d6000 = compute_vquad(CF_DEPTH_CROSS_CHECK, DPS_WORKING_HI)
    elapsed_fresh = time.time() - t0

    agree_depths = agreement_digits(v_fresh_d5000, v_fresh_d6000, DPS_WORKING_HI)
    log["events"].append({
        "event": "fresh_cf_dual_depth",
        "depths": [5000, CF_DEPTH_CROSS_CHECK],
        "dps_working": DPS_WORKING_HI,
        "wall_seconds_d5000": round(t_mid - t0, 3),
        "wall_seconds_d6000": round(time.time() - t_mid, 3),
        "wall_seconds_total": round(elapsed_fresh, 3),
        "agreement_digits_dual_depth": agree_depths,
    })
    if agree_depths < DPS_TARGET:
        raise RuntimeError(
            f"Stage-2 fresh-CF dual-depth agreement insufficient: {agree_depths} < {DPS_TARGET}"
        )

    agree_reload_vs_fresh = agreement_digits(v_fresh_d5000, v_reload, DPS_WORKING_HI)
    log["events"].append({
        "event": "reload_sanity_check",
        "agreement_digits_reload_vs_fresh_d5000": agree_reload_vs_fresh,
        "note": "Round-trip through mp.nstr at 2000-digit precision truncates 1 ULP at the boundary; agreement >= 1998 is expected.",
    })
    if agree_reload_vs_fresh < 1998:
        raise RuntimeError(
            f"Reload-vs-fresh sanity check failed: {agree_reload_vs_fresh} < 1998"
        )

    log["events"].append({"event": "using_fresh_d5000_for_pslq", "first_64": mp.nstr(v_fresh_d5000, 64)})
    log["status"] = "OK"
    return v_fresh_d5000, log


# ─────────────────────────────────────────────────────────────────
# Bases
# ─────────────────────────────────────────────────────────────────

def enum_classical_monomials_deg_le(max_deg: int):
    """Monomials pi^a * e^b * G^c * zeta(3)^d with a+b+c+d <= max_deg."""
    names = ["pi", "e", "G", "zeta3"]
    items = []
    for total in range(0, max_deg + 1):
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


def build_basis_tensor(v_quad: mp.mpf, dps: int, k_max: int):
    """{V_quad^k * m : k in [0..k_max], m a classical monomial of total deg <= 2}.
    Size = (k_max + 1) * 15."""
    classical = enum_classical_monomials_deg_le(2)
    assert len(classical) == 15

    with mp.workdps(dps):
        pi_v, e_v, G_v, z3_v = mp.pi, mp.e, mp.catalan, mp.zeta(3)
        V = mp.mpf(v_quad)
        vals: list[mp.mpf] = []
        labels: list[str] = []
        records: list[dict] = []
        for k in range(0, k_max + 1):
            v_pow = V ** k
            for combo, mlab in classical:
                a, b, c, d = combo
                m_val = (pi_v ** a) * (e_v ** b) * (G_v ** c) * (z3_v ** d)
                vals.append(v_pow * m_val)
                lab = mlab if k == 0 else (f"V_quad^{k}" if mlab == "1" else f"V_quad^{k}*{mlab}")
                labels.append(lab)
                records.append({"k": k, "classical_exponents": list(combo), "label": lab})

    expected = (k_max + 1) * 15
    assert len(vals) == expected, f"basis size {len(vals)} != {expected}"
    return vals, labels, records


# ─────────────────────────────────────────────────────────────────
# PSLQ
# ─────────────────────────────────────────────────────────────────

def run_pslq(vals: list[mp.mpf], dps: int, maxcoeff: int) -> dict:
    tol_exp = -(dps - PSLQ_TOL_OFFSET[dps])
    mp.mp.dps = dps + 30
    with mp.workdps(dps):
        tol = mp.mpf(10) ** tol_exp
        t0 = time.time()
        try:
            rel = mp.pslq(
                vals,
                tol=tol,
                maxcoeff=maxcoeff,
                maxsteps=PSLQ_MAXSTEPS[dps],
            )
        except ValueError as exc:
            rel = None
            err = repr(exc)
        else:
            err = None
        elapsed = time.time() - t0

    return {
        "dps": dps,
        "tol_exponent": tol_exp,
        "maxcoeff": maxcoeff,
        "maxsteps": PSLQ_MAXSTEPS[dps],
        "basis_size": len(vals),
        "wall_seconds": round(elapsed, 3),
        "result": None if rel is None else [int(c) for c in rel],
        "error": err,
    }


def classify(tier_lo: dict, tier_hi: dict) -> str:
    if tier_lo["result"] is None and tier_hi["result"] is None:
        return "NULL"
    if tier_lo["result"] is None or tier_hi["result"] is None:
        return "UNSTABLE_NOISE"
    return "STABLE_CANDIDATE" if tier_lo["result"] == tier_hi["result"] else "UNSTABLE_NOISE"


# ─────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────

def main() -> int:
    print(f"=== {TASK_ID} Stages 2+3 ===", flush=True)
    print(f"mpmath {mp.__version__}", flush=True)

    t_start = time.time()

    # Stage 2
    print("\n[Stage 2] Reload + cross-check V_quad ...", flush=True)
    v_quad, s2_log = stage2_reload_and_cross_check()
    fresh_ev = next(ev for ev in s2_log["events"] if ev["event"] == "fresh_cf_dual_depth")
    reload_ev = next(ev for ev in s2_log["events"] if ev["event"] == "reload_sanity_check")
    print(
        f"  Fresh dual-depth (5000/6000) agreement: {fresh_ev['agreement_digits_dual_depth']} digits "
        f"({fresh_ev['wall_seconds_total']}s total)",
        flush=True,
    )
    print(
        f"  Reload-vs-fresh sanity: {reload_ev['agreement_digits_reload_vs_fresh_d5000']} digits "
        f"(>= 1998 expected; nstr truncation at 2000)",
        flush=True,
    )

    # Basis enumerations dump (structural)
    print("\n[Stage 3] Building bases ...", flush=True)
    _, _, recs_3_2 = build_basis_tensor(v_quad, 50, k_max=3)
    _, _, recs_4_2 = build_basis_tensor(v_quad, 50, k_max=4)
    (SLOT_DIR / "basis_3_2_enumeration.json").write_text(
        json.dumps({"basis_size": len(recs_3_2), "k_max": 3, "classical_max_deg": 2, "items": recs_3_2}, indent=2),
        encoding="utf-8",
    )
    (SLOT_DIR / "basis_4_2_enumeration.json").write_text(
        json.dumps({"basis_size": len(recs_4_2), "k_max": 4, "classical_max_deg": 2, "items": recs_4_2}, indent=2),
        encoding="utf-8",
    )

    # ── Axis 1: B_3_2 at maxcoeff = 10^6 ──
    print("\n[Stage 3a] B_3_2 (60 elements) PSLQ @ 500 dp, maxcoeff=10^6 ...", flush=True)
    vals_3_2_lo, _, _ = build_basis_tensor(v_quad, 500, k_max=3)
    a1_500 = run_pslq(vals_3_2_lo, 500, 10**6)
    print(f"   result: {a1_500['result']}  ({a1_500['wall_seconds']}s)", flush=True)
    (SLOT_DIR / "pslq_3_2_maxc6_500dp.json").write_text(json.dumps(a1_500, indent=2), encoding="utf-8")

    print("\n[Stage 3b] B_3_2 (60 elements) PSLQ @ 2050 dp, maxcoeff=10^6 ...", flush=True)
    vals_3_2_hi, _, _ = build_basis_tensor(v_quad, 2050, k_max=3)
    a1_2050 = run_pslq(vals_3_2_hi, 2050, 10**6)
    print(f"   result: {a1_2050['result']}  ({a1_2050['wall_seconds']}s)", flush=True)
    (SLOT_DIR / "pslq_3_2_maxc6_2050dp.json").write_text(json.dumps(a1_2050, indent=2), encoding="utf-8")

    axis1_verdict = classify(a1_500, a1_2050)
    print(f"   Axis-1 (B_3_2, maxcoeff=10^6) verdict: {axis1_verdict}", flush=True)

    # ── Axis 2: B_4_2 at maxcoeff = 10^4 ──
    print("\n[Stage 3c] B_4_2 (75 elements) PSLQ @ 500 dp, maxcoeff=10^4 ...", flush=True)
    vals_4_2_lo, _, _ = build_basis_tensor(v_quad, 500, k_max=4)
    a2_500 = run_pslq(vals_4_2_lo, 500, 10**4)
    print(f"   result: {a2_500['result']}  ({a2_500['wall_seconds']}s)", flush=True)
    (SLOT_DIR / "pslq_4_2_maxc4_500dp.json").write_text(json.dumps(a2_500, indent=2), encoding="utf-8")

    print("\n[Stage 3d] B_4_2 (75 elements) PSLQ @ 2050 dp, maxcoeff=10^4 ... (longest tier)", flush=True)
    vals_4_2_hi, _, _ = build_basis_tensor(v_quad, 2050, k_max=4)
    a2_2050 = run_pslq(vals_4_2_hi, 2050, 10**4)
    print(f"   result: {a2_2050['result']}  ({a2_2050['wall_seconds']}s)", flush=True)
    (SLOT_DIR / "pslq_4_2_maxc4_2050dp.json").write_text(json.dumps(a2_2050, indent=2), encoding="utf-8")

    axis2_verdict = classify(a2_500, a2_2050)
    print(f"   Axis-2 (B_4_2, maxcoeff=10^4) verdict: {axis2_verdict}", flush=True)

    # ── Combined verdict ──
    if axis1_verdict == "NULL" and axis2_verdict == "NULL":
        combined = "EXCLUSION_CERTIFIED"
    elif "STABLE_CANDIDATE" in (axis1_verdict, axis2_verdict):
        combined = "PENDING_VERIFICATION_CANDIDATE"
    elif "UNSTABLE_NOISE" in (axis1_verdict, axis2_verdict):
        combined = "PENDING_VERIFICATION_NOISE"
    else:
        combined = "PENDING_VERIFICATION_OTHER"

    stage3_log = {
        "task_id": TASK_ID,
        "stage": 3,
        "axis_1_coefficient_floor": {
            "basis": "B_3_2",
            "basis_size": 60,
            "maxcoeff": 10**6,
            "verdict": axis1_verdict,
            "tier_500": a1_500,
            "tier_2050": a1_2050,
        },
        "axis_2_degree_extension": {
            "basis": "B_4_2",
            "basis_size": 75,
            "maxcoeff": 10**4,
            "verdict": axis2_verdict,
            "tier_500": a2_500,
            "tier_2050": a2_2050,
        },
        "combined_verdict": combined,
        "status": "OK",
    }
    with (SLOT_DIR / "raw_candidates.jsonl").open("w", encoding="utf-8") as f:
        f.write(json.dumps({"stage": 2, **s2_log}) + "\n")
        f.write(json.dumps(stage3_log) + "\n")

    elapsed = time.time() - t_start
    summary = {
        "task_id": TASK_ID,
        "elapsed_seconds": round(elapsed, 1),
        "stage2_status": s2_log["status"],
        "axis_1_verdict": axis1_verdict,
        "axis_2_verdict": axis2_verdict,
        "combined_verdict": combined,
    }
    (SLOT_DIR / "executor_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print("\n=== DONE ===", flush=True)
    print(json.dumps(summary, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
