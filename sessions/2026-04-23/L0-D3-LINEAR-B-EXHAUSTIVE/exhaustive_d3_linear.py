#!/usr/bin/env python3
"""
Exhaustive degree-(3,1) search — classify ALL families with cubic a(n), linear b(n).
Task: L0-D3-LINEAR-B-EXHAUSTIVE

a(n) = a3*n^3 + a2*n^2 + a1*n + a0
  a3 in {-4,...,4} \ {0}  (8 choices)
  a2,a1,a0 in {-4,...,4}  (9 choices each)
  Total a-polynomials: 8 * 9^3 = 5,832

b(n) = b1*n + b0
  b1 in {-4,...,4} \ {0}  (8 choices)
  b0 in {-4,...,4}         (9 choices)
  Total b-polynomials: 72

Total families: 5,832 * 72 = 419,904

Pipeline per family:
  1. Structural Rat screen: a(k)=0 for k in {0,...,12}
  2. Convergence: batch Lentz N=300
  3. Rationality pre-screen: float64 q-scan
  4. PSLQ T1={1,K,pi,K*pi,pi^2} at dps=80
  5. Confirm any Trans hits at dps=150, then dps=300
"""
import json
import os
import sys
import time
import hashlib
import gc
from datetime import datetime, timezone

import numpy as np
from mpmath import mp, mpf, pi as mp_pi, pslq, fabs, nstr

# Import classifier utilities
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from classifier import (compute_K_batch_lentz, rat_prescreen_float,
                         compute_K_mpmath)

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
TASK_ID = "L0-D3-LINEAR-B-EXHAUSTIVE"
D = 4  # coefficient range {-4,...,4}


# ---------------------------------------------------------------------------
# Family enumeration
# ---------------------------------------------------------------------------

def enumerate_d3_linear_b():
    """
    Generate ALL degree-(3,1) families.
    a(n) = a3*n^3 + a2*n^2 + a1*n + a0 with a3 != 0
    b(n) = b1*n + b0 with b1 != 0
    Coefficients stored as [c3, c2, c1, c0] (leading first).
    For b: [0, 0, b1, b0].

    Returns a_coeffs (N,4), b_coeffs (N,4) as int16 arrays.
    """
    a3_vals = list(range(-D, 0)) + list(range(1, D + 1))  # 8 values
    a_rest_vals = list(range(-D, D + 1))  # 9 values each

    b1_vals = list(range(-D, 0)) + list(range(1, D + 1))  # 8 values
    b0_vals = list(range(-D, D + 1))  # 9 values

    n_a = len(a3_vals) * len(a_rest_vals)**3  # 8*729 = 5832
    n_b = len(b1_vals) * len(b0_vals)          # 8*9 = 72
    total = n_a * n_b                           # 419904

    # Build a-poly array
    a_list = np.empty((n_a, 4), dtype=np.int16)
    idx = 0
    for a3 in a3_vals:
        for a2 in a_rest_vals:
            for a1 in a_rest_vals:
                for a0 in a_rest_vals:
                    a_list[idx] = [a3, a2, a1, a0]
                    idx += 1

    # Build b-poly array (linear: b3=b2=0)
    b_list = np.empty((n_b, 4), dtype=np.int16)
    idx = 0
    for b1 in b1_vals:
        for b0 in b0_vals:
            b_list[idx] = [0, 0, b1, b0]
            idx += 1

    # Cross product
    a_full = np.repeat(a_list, n_b, axis=0)
    b_full = np.tile(b_list, (n_a, 1))
    assert len(a_full) == total
    return a_full, b_full


# ---------------------------------------------------------------------------
# Screen 1: structural Rat — a(k) = 0 for k in {0,...,12}
# ---------------------------------------------------------------------------

def screen_rat_structural(a_coeffs):
    """Returns bool mask: True = Rat (skip)."""
    N = len(a_coeffs)
    rat = np.zeros(N, dtype=bool)
    a = a_coeffs.astype(np.int64)
    for k in range(0, 13):
        if k == 0:
            a_k = a[:, 3]  # a(0) = a0
        else:
            k2, k3 = k * k, k * k * k
            a_k = a[:, 0] * k3 + a[:, 1] * k2 + a[:, 2] * k + a[:, 3]
        rat |= (a_k == 0)
    return rat


# ---------------------------------------------------------------------------
# PSLQ at specified dps
# ---------------------------------------------------------------------------

def pslq_scan_single(a_row, b_row, dps=80, maxcoeff=10**8):
    """
    Compute K at dps precision, then run PSLQ against T1.
    Returns dict or None.
    """
    mp.dps = dps + 50
    a3, a2, a1, a0 = [mpf(int(c)) for c in a_row]
    b3, b2, b1, b0 = [mpf(int(c)) for c in b_row]

    # Euler-Wallis recurrence
    Pp, Pc = mpf(1), b0
    Qp, Qc = mpf(0), mpf(1)
    N = 500 if dps >= 150 else 300
    for n in range(1, N + 1):
        nn = mpf(n)
        an = a3 * nn**3 + a2 * nn**2 + a1 * nn + a0
        bn = b1 * nn + b0  # b3=b2=0 for linear b
        Pn = bn * Pc + an * Pp
        Qn = bn * Qc + an * Qp
        Pp, Pc = Pc, Pn
        Qp, Qc = Qc, Qn
        if n % 50 == 0 and Qc != 0:
            s = abs(Qc)
            if s > mpf(10)**20:
                Pc /= s; Pp /= s; Qc /= s; Qp /= s

    if Qc == 0:
        return None
    mp.dps = dps
    K = +(Pc / Qc)

    # Rational check
    try:
        rel = pslq([mpf(1), K], maxcoeff=10**6)
    except Exception:
        rel = None
    if rel is not None:
        residual = fabs(rel[0] + rel[1] * K)
        if residual < mpf(10)**(-20 if dps == 80 else -40):
            return {'stratum': 'Rat', 'basis': 'R', 'relation': list(rel),
                    'residual': float(residual)}

    # T1 PSLQ: {1, K, pi, K*pi, pi^2}
    try:
        basis_vals = [mpf(1), K, mp_pi, K * mp_pi, mp_pi**2]
        rel = pslq(basis_vals, maxcoeff=maxcoeff)
    except Exception:
        rel = None
    if rel is not None:
        residual = fabs(sum(r * v for r, v in zip(rel, basis_vals)))
        threshold = mpf(10)**(-20 if dps == 80 else -30)
        if residual < threshold:
            return {'stratum': 'Trans', 'basis': 'T1', 'relation': list(rel),
                    'residual': float(residual), 'K': float(K)}

    return {'stratum': 'Desert', 'basis': None}


def confirm_hit(a_row, b_row, dps=150):
    """Confirm a PSLQ hit at higher precision."""
    return pslq_scan_single(a_row, b_row, dps=dps, maxcoeff=10**8)


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()
    print("=" * 70)
    print(f"EXHAUSTIVE DEGREE-(3,1) SEARCH — {TASK_ID}")
    print(f"Coefficient range: [-{D}, {D}]")
    print("Pipeline: Struct screen -> Lentz convergence -> Rat prescreen -> PSLQ T1")
    print("=" * 70)

    # --- Phase 0: Enumerate ---
    print("\n--- Phase 0: Enumerating families ---")
    a_all, b_all = enumerate_d3_linear_b()
    total = len(a_all)
    print(f"  Total families: {total}")
    assert total == 419904, f"Expected 419904, got {total}"

    # --- Phase 1: Structural Rat screen ---
    print("\n--- Phase 1: Structural Rat screen (a(k)=0, k=0..12) ---")
    rat_mask = screen_rat_structural(a_all)
    n_rat_struct = int(rat_mask.sum())
    a_pass1 = a_all[~rat_mask]
    b_pass1 = b_all[~rat_mask]
    del a_all, b_all
    gc.collect()
    print(f"  Structural Rat: {n_rat_struct}")
    print(f"  Remaining: {len(a_pass1)}")

    # --- Phase 2: Convergence check (batch Lentz, N=300) ---
    print("\n--- Phase 2: Convergence check (Lentz N=300) ---")
    K_float, conv_mask = compute_K_batch_lentz(a_pass1, b_pass1, N=300)
    n_divergent = int((~conv_mask).sum())
    a_pass2 = a_pass1[conv_mask]
    b_pass2 = b_pass1[conv_mask]
    K_pass2 = K_float[conv_mask]
    del a_pass1, b_pass1, K_float, conv_mask
    gc.collect()
    print(f"  Divergent: {n_divergent}")
    print(f"  Convergent: {len(a_pass2)}")

    # --- Phase 3: Rationality pre-screen ---
    print("\n--- Phase 3: Rationality pre-screen (float64, max_q=300) ---")
    rat_float = rat_prescreen_float(K_pass2, max_q=300, tol=1e-4)
    n_rat_float = int(rat_float.sum())
    a_pass3 = a_pass2[~rat_float]
    b_pass3 = b_pass2[~rat_float]
    del a_pass2, b_pass2, K_pass2, rat_float
    gc.collect()
    print(f"  Likely rational: {n_rat_float}")
    print(f"  PSLQ candidates: {len(a_pass3)}")

    # --- Phase 4: PSLQ scan at dps=80 ---
    n_pslq = len(a_pass3)
    print(f"\n--- Phase 4: PSLQ scan (dps=80, {n_pslq} families) ---")
    trans_candidates = []  # (index, a_row, b_row, result)
    rat_pslq = 0
    desert_pslq = 0

    for i in range(n_pslq):
        a_row = a_pass3[i]
        b_row = b_pass3[i]
        result = pslq_scan_single(a_row, b_row, dps=80)
        if result is None:
            desert_pslq += 1
        elif result['stratum'] == 'Trans':
            trans_candidates.append((i, a_row.tolist(), b_row.tolist(), result))
            print(f"  ** TRANS HIT at index {i}: a={a_row.tolist()}, b={b_row.tolist()}")
            print(f"     relation={result['relation']}, residual={result['residual']:.2e}")
        elif result['stratum'] == 'Rat':
            rat_pslq += 1
        else:
            desert_pslq += 1

        if (i + 1) % 500 == 0:
            elapsed = time.time() - t0
            rate = (i + 1) / elapsed
            eta = (n_pslq - i - 1) / rate if rate > 0 else 0
            print(f"  ... {i+1}/{n_pslq} ({elapsed:.0f}s, ~{eta:.0f}s left, "
                  f"Trans={len(trans_candidates)}, Rat={rat_pslq}, Desert={desert_pslq})")

    elapsed_p4 = time.time() - t0
    print(f"\n  Pass 1 complete: {n_pslq} tested in {elapsed_p4:.0f}s")
    print(f"  Trans candidates: {len(trans_candidates)}")
    print(f"  Rat (PSLQ): {rat_pslq}")
    print(f"  Desert: {desert_pslq}")

    # --- Phase 5: Confirmation at dps=150 then dps=300 ---
    confirmed_trans = []
    if trans_candidates:
        print(f"\n--- Phase 5: Confirming {len(trans_candidates)} Trans candidates ---")
        for idx, a_row, b_row, p1_result in trans_candidates:
            print(f"  Confirming a={a_row}, b={b_row}...")
            # dps=150 first
            r150 = confirm_hit(np.array(a_row, dtype=np.int16),
                               np.array(b_row, dtype=np.int16), dps=150)
            if r150 is None or r150['stratum'] != 'Trans':
                print(f"    FAILED at dps=150: {r150}")
                continue
            print(f"    dps=150 OK, residual={r150['residual']:.2e}")
            # dps=300
            r300 = confirm_hit(np.array(a_row, dtype=np.int16),
                               np.array(b_row, dtype=np.int16), dps=300)
            if r300 is None or r300['stratum'] != 'Trans':
                print(f"    FAILED at dps=300: {r300}")
                continue
            print(f"    dps=300 OK, residual={r300['residual']:.2e}")
            confirmed_trans.append({
                'a_coeffs': a_row,
                'b_coeffs': b_row,
                'pass1_relation': p1_result['relation'],
                'pass1_residual': p1_result['residual'],
                'dps150_relation': r150['relation'],
                'dps150_residual': r150['residual'],
                'dps300_relation': r300['relation'],
                'dps300_residual': r300['residual'],
                'K_float': p1_result.get('K'),
            })
            print(f"    ** CONFIRMED TRANS: a={a_row}, b={b_row}")
            print(f"       relation={r300['relation']}")
    else:
        print("\n  No Trans candidates to confirm — skipping Phase 5.")

    # --- Write results ---
    total_time = time.time() - t0
    total_rat = n_rat_struct + n_rat_float + rat_pslq

    results = {
        'task_id': TASK_ID,
        'date': datetime.now(timezone.utc).isoformat(),
        'coefficient_range': D,
        'total_families': total,
        'a_degree': 3,
        'b_degree': 1,
        'phase1_rat_structural': n_rat_struct,
        'phase2_divergent': n_divergent,
        'phase3_rat_float': n_rat_float,
        'phase4_pslq_tested': n_pslq,
        'phase4_rat_pslq': rat_pslq,
        'phase4_trans_candidates': len(trans_candidates),
        'phase4_desert': desert_pslq,
        'confirmed_trans_count': len(confirmed_trans),
        'confirmed_trans': confirmed_trans,
        'total_rat': total_rat,
        'total_desert': desert_pslq,
        'verdict': 'TRANS_FOUND' if confirmed_trans else 'NULL',
        'runtime_seconds': round(total_time, 1),
    }

    results_path = os.path.join(OUT_DIR, 'exhaustive_d3_linear_results.json')
    with open(results_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\n  Written: exhaustive_d3_linear_results.json")

    # AEAL claim
    claim_str = json.dumps(results, sort_keys=True, ensure_ascii=False)
    claim_hash = hashlib.sha256(claim_str.encode()).hexdigest()
    claim = {
        'claim': (f"Exhaustive degree-(3,1) search in F(3,{D}): "
                  f"{total} families, {n_pslq} PSLQ-tested, "
                  f"confirmed_trans={len(confirmed_trans)}, "
                  f"verdict={'TRANS_FOUND' if confirmed_trans else 'NULL'}"),
        'evidence_type': 'computation',
        'dps': 80,
        'confirmation_dps': 300,
        'reproducible': True,
        'script': 'exhaustive_d3_linear.py',
        'output_hash': claim_hash,
    }
    claims_path = os.path.join(OUT_DIR, 'claims_exhaustive.jsonl')
    with open(claims_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(claim, ensure_ascii=False) + '\n')
    print(f"  Written: claims_exhaustive.jsonl")

    # --- Summary ---
    print("\n" + "=" * 70)
    print(f"EXHAUSTIVE DEGREE-(3,1) SEARCH COMPLETE")
    print(f"  Total families: {total}")
    print(f"  Structural Rat: {n_rat_struct}")
    print(f"  Divergent:      {n_divergent}")
    print(f"  Rat (float):    {n_rat_float}")
    print(f"  PSLQ tested:    {n_pslq}")
    print(f"  Rat (PSLQ):     {rat_pslq}")
    print(f"  Trans candidates: {len(trans_candidates)}")
    print(f"  CONFIRMED Trans:  {len(confirmed_trans)}")
    print(f"  Desert:         {desert_pslq}")
    print(f"  Verdict: {'TRANS_FOUND' if confirmed_trans else 'NULL'}")
    print(f"  Runtime: {total_time:.0f}s")
    print("=" * 70)


if __name__ == '__main__':
    main()
