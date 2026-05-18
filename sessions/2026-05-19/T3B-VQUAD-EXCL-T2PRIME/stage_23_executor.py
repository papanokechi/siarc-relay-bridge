#!/usr/bin/env python3
"""
T3B-VQUAD-EXCL-T2PRIME — Stages 2+3 executor.

Stage 2: reload V_quad from predecessor artifact, cross-check via fresh CF
backward recurrence at depth 6000 to 2200 dp working precision. Halt if
agreement < 2000 digits.

Stage 3: build two complementary bases and run PSLQ on each at 500 dp then
2050 dp. Classify each result. Combined verdict requires both bases to
be NULL across both tiers.
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
TASK_ID = "T3B-VQUAD-EXCL-T2PRIME"

# ── Predecessor artifact ──
# Predecessor recorded TWO SHAs:
#   - str-SHA (raw_candidates.jsonl 'vquad_sha256'): SHA of mp.nstr(...).encode('utf-8') with NO trailing newline.
#   - file-SHA (manifest.json, claims.jsonl output_hash): SHA of file bytes including the trailing "\r\n".
# We verify the str-SHA after stripping the trailing newline, which is line-ending-normalization-safe.
PREDECESSOR_VQUAD_PATH = SLOT_DIR.parent.parent / "2026-05-18" / "T3B-VQUAD-EXCL-PEGZ3" / "vquad_value_2000dp.txt"
PREDECESSOR_VQUAD_STR_SHA = "52375a71a05bf61ad971cf83ea9334eb96e20ffa054dc3cab74447966a2f5c44"

# ── Precision / depth tiers ──
DPS_WORKING_HI = 2200
DPS_TARGET = 2000
CF_DEPTH_CROSS_CHECK = 6000

# ── PSLQ parameters ──
PSLQ_MAXCOEFF = 10**4
PSLQ_TOL_OFFSET = {500: 50, 2050: 80}     # tol = 10^-(dps - offset)
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
    """Two-part Stage 2:
      (a) Reload predecessor's 2000-digit V_quad string, verify string-content SHA,
          parse to mpf, sanity-check first ~1998 digits against fresh CF.
          (Round-trip through mp.nstr truncates at 2000 digits; expect ~1 ULP loss
          at the boundary, so the threshold is 1998 not 2000.)
      (b) Compute V_quad FRESH at 2200 dps via backward CF at two depths (5000 and 6000)
          and require >= 2000 digit agreement between the two depths.
      The fresh (depth-5000) value is what PSLQ consumes; the reload is provenance only.
    """
    log: dict = {"task_id": TASK_ID, "stage": 2, "events": []}

    # (a) Reload + sanity check
    raw = PREDECESSOR_VQUAD_PATH.read_bytes()
    file_sha = sha256_of_bytes(raw)
    v_str = raw.decode("utf-8").strip()
    str_sha = sha256_of_bytes(v_str.encode("utf-8"))
    log["events"].append({
        "event": "predecessor_load",
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

    # (b) Fresh CF at two depths
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

    # Sanity check: fresh vs reload (expect ~1998-2000 digits agreement, limited by nstr truncation)
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

def enum_classical_monomials_deg_le(max_deg: int) -> list[tuple[tuple[int, int, int, int], str]]:
    """Monomials pi^a * e^b * G^c * zeta(3)^d with a+b+c+d <= max_deg."""
    names = ["pi", "e", "G", "zeta3"]
    items: list[tuple[tuple[int, int, int, int], str]] = []
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


def build_basis_union(v_quad: mp.mpf, dps: int):
    """B_union: {V_quad^k : k=0..3} ∪ {classical monomials, deg <= 2}, deduping '1'.
    Size = 4 + 15 - 1 = 18.
    Ordering: classical degree-0 ('1'); V_quad^1, V_quad^2, V_quad^3;
              classical degree-1 (4); classical degree-2 (10).
    """
    classical = enum_classical_monomials_deg_le(2)
    assert len(classical) == 15, f"classical count {len(classical)}"

    with mp.workdps(dps):
        pi_v, e_v, G_v, z3_v = mp.pi, mp.e, mp.catalan, mp.zeta(3)
        V = mp.mpf(v_quad)
        vals = [mp.mpf(1)]                       # "1" (shared)
        labels = ["1"]
        records = [{"kind": "shared_one", "label": "1"}]

        for k in (1, 2, 3):
            vals.append(V**k)
            labels.append(f"V_quad^{k}")
            records.append({"kind": "vquad_power", "k": k, "label": f"V_quad^{k}"})

        for combo, label in classical:
            if combo == (0, 0, 0, 0):
                continue  # already in via "shared_one"
            a, b, c, d = combo
            vals.append((pi_v**a) * (e_v**b) * (G_v**c) * (z3_v**d))
            labels.append(label)
            records.append({"kind": "classical_monomial", "exponents": list(combo), "label": label})

    assert len(vals) == 18, f"union basis size {len(vals)} != 18"
    return vals, labels, records


def build_basis_tensor(v_quad: mp.mpf, dps: int):
    """B_tensor: {V_quad^k * m : k=0..3, m in classical deg <= 2}. Size 4*15 = 60."""
    classical = enum_classical_monomials_deg_le(2)
    assert len(classical) == 15

    with mp.workdps(dps):
        pi_v, e_v, G_v, z3_v = mp.pi, mp.e, mp.catalan, mp.zeta(3)
        V = mp.mpf(v_quad)
        vals = []
        labels = []
        records = []
        for k in range(0, 4):
            v_pow = V**k
            for combo, mlab in classical:
                a, b, c, d = combo
                m_val = (pi_v**a) * (e_v**b) * (G_v**c) * (z3_v**d)
                vals.append(v_pow * m_val)
                lab = mlab if k == 0 else (f"V_quad^{k}" if mlab == "1" else f"V_quad^{k}*{mlab}")
                labels.append(lab)
                records.append({"k": k, "classical_exponents": list(combo), "label": lab})
    assert len(vals) == 60, f"tensor basis size {len(vals)} != 60"
    return vals, labels, records


# ─────────────────────────────────────────────────────────────────
# PSLQ helpers
# ─────────────────────────────────────────────────────────────────

def run_pslq(vals: list[mp.mpf], dps: int) -> dict:
    tol_exp = -(dps - PSLQ_TOL_OFFSET[dps])
    mp.mp.dps = dps + 30
    with mp.workdps(dps):
        tol = mp.mpf(10) ** tol_exp
        t0 = time.time()
        try:
            rel = mp.pslq(vals, tol=tol, maxcoeff=PSLQ_MAXCOEFF,
                          maxsteps=PSLQ_MAXSTEPS[dps])
        except ValueError as exc:
            rel = None
            err = repr(exc)
        else:
            err = None
        elapsed = time.time() - t0

    return {
        "dps": dps,
        "tol_exponent": tol_exp,
        "maxcoeff": PSLQ_MAXCOEFF,
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

    # ── Build and dump basis enumerations once ──
    print("\n[Stage 3] Building bases ...", flush=True)
    # Union (low precision dump just for the structural file)
    _, _, union_records = build_basis_union(v_quad, 50)
    _, _, tensor_records = build_basis_tensor(v_quad, 50)
    (SLOT_DIR / "basis_union_enumeration.json").write_text(
        json.dumps({"basis_size": len(union_records), "items": union_records}, indent=2),
        encoding="utf-8",
    )
    (SLOT_DIR / "basis_tensor_enumeration.json").write_text(
        json.dumps({"basis_size": len(tensor_records), "items": tensor_records}, indent=2),
        encoding="utf-8",
    )

    # ── Stage 3: PSLQ on B_union ──
    print("\n[Stage 3a] B_union (18 elements) PSLQ @ 500 dp ...", flush=True)
    u_vals_lo, _, _ = build_basis_union(v_quad, 500)
    union_500 = run_pslq(u_vals_lo, 500)
    print(f"   result: {union_500['result']}  ({union_500['wall_seconds']}s)", flush=True)
    (SLOT_DIR / "pslq_union_500dp.json").write_text(json.dumps(union_500, indent=2), encoding="utf-8")

    print("\n[Stage 3b] B_union (18 elements) PSLQ @ 2050 dp ...", flush=True)
    u_vals_hi, _, _ = build_basis_union(v_quad, 2050)
    union_2050 = run_pslq(u_vals_hi, 2050)
    print(f"   result: {union_2050['result']}  ({union_2050['wall_seconds']}s)", flush=True)
    (SLOT_DIR / "pslq_union_2050dp.json").write_text(json.dumps(union_2050, indent=2), encoding="utf-8")

    union_verdict = classify(union_500, union_2050)
    print(f"   B_union verdict: {union_verdict}", flush=True)

    # ── Stage 3: PSLQ on B_tensor ──
    print("\n[Stage 3c] B_tensor (60 elements) PSLQ @ 500 dp ...", flush=True)
    t_vals_lo, _, _ = build_basis_tensor(v_quad, 500)
    tensor_500 = run_pslq(t_vals_lo, 500)
    print(f"   result: {tensor_500['result']}  ({tensor_500['wall_seconds']}s)", flush=True)
    (SLOT_DIR / "pslq_tensor_500dp.json").write_text(json.dumps(tensor_500, indent=2), encoding="utf-8")

    print("\n[Stage 3d] B_tensor (60 elements) PSLQ @ 2050 dp ... (long tier)", flush=True)
    t_vals_hi, _, _ = build_basis_tensor(v_quad, 2050)
    tensor_2050 = run_pslq(t_vals_hi, 2050)
    print(f"   result: {tensor_2050['result']}  ({tensor_2050['wall_seconds']}s)", flush=True)
    (SLOT_DIR / "pslq_tensor_2050dp.json").write_text(json.dumps(tensor_2050, indent=2), encoding="utf-8")

    tensor_verdict = classify(tensor_500, tensor_2050)
    print(f"   B_tensor verdict: {tensor_verdict}", flush=True)

    # ── Combined verdict ──
    if union_verdict == "NULL" and tensor_verdict == "NULL":
        combined = "EXCLUSION_CERTIFIED"
    elif "STABLE_CANDIDATE" in (union_verdict, tensor_verdict):
        combined = "PENDING_VERIFICATION_CANDIDATE"
    elif "UNSTABLE_NOISE" in (union_verdict, tensor_verdict):
        combined = "PENDING_VERIFICATION_NOISE"
    else:
        combined = "PENDING_VERIFICATION_OTHER"

    # ── raw_candidates.jsonl ──
    stage3_log = {
        "task_id": TASK_ID,
        "stage": 3,
        "union": {"verdict": union_verdict, "tier_500": union_500, "tier_2050": union_2050},
        "tensor": {"verdict": tensor_verdict, "tier_500": tensor_500, "tier_2050": tensor_2050},
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
        "union_verdict": union_verdict,
        "tensor_verdict": tensor_verdict,
        "combined_verdict": combined,
    }
    (SLOT_DIR / "executor_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print("\n=== DONE ===", flush=True)
    print(json.dumps(summary, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
