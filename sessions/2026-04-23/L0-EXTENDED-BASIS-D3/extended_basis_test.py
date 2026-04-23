#!/usr/bin/env python3
"""
Extended Basis Test — re-test d=3 Desert families with larger PSLQ bases.
Task: L0-EXTENDED-BASIS-D3

Two-pass approach:
  Pass 1: Quick scan at dps=80 (fast PSLQ on all 14,714 families)
  Pass 2: Confirm any hits at dps=150, then dps=300

Re-derives the same 14,714 families from L0-SCALE-SELECTOR-POC, then
tests them against:
  T1_ext = {1, K, pi, K*pi, pi^2, K*pi^2, pi^3}
  T2     = {1, K, pi^2, K*pi^2}
"""
import json
import os
import sys
import time
import hashlib
from concurrent.futures import ProcessPoolExecutor, as_completed

import numpy as np
from mpmath import mp, mpf, pi as mp_pi, pslq, fabs, nstr

# Import from the scale selector package
SELECTOR_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                            "pcf-scale-selector")
sys.path.insert(0, SELECTOR_DIR)

from screener import generate_families, apply_screens
from classifier import (compute_K_batch_lentz, rat_prescreen_float,
                         compute_K_mpmath)

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
TASK_ID = "L0-EXTENDED-BASIS-D3"


def _screen_and_filter(a_all, b_all, D):
    """Screen, batch K, rat prescreen. Returns (a_nr, b_nr) non-rat convergent."""
    import gc
    if len(a_all) == 0:
        return np.empty((0, 4), dtype=np.int16), np.empty((0, 4), dtype=np.int16)

    screens = apply_screens(a_all, b_all, D, verbose=False)
    a_cand = a_all[screens['candidate']]
    b_cand = b_all[screens['candidate']]
    del a_all, b_all, screens
    gc.collect()

    if len(a_cand) == 0:
        return np.empty((0, 4), dtype=np.int16), np.empty((0, 4), dtype=np.int16)

    K_float, converged = compute_K_batch_lentz(a_cand, b_cand, N=200)
    a_conv = a_cand[converged]
    b_conv = b_cand[converged]
    K_conv = K_float[converged]
    del a_cand, b_cand, K_float, converged
    gc.collect()

    if len(a_conv) == 0:
        return np.empty((0, 4), dtype=np.int16), np.empty((0, 4), dtype=np.int16)

    likely_rat = rat_prescreen_float(K_conv, max_q=300, tol=1e-4)
    a_nr = a_conv[~likely_rat]
    b_nr = b_conv[~likely_rat]
    del a_conv, b_conv, K_conv, likely_rat
    gc.collect()

    return a_nr, b_nr


def get_pslq_candidates(D, max_pslq, b_deg_max=None):
    """
    Reproduce the exact pipeline from L0-SCALE-SELECTOR-POC to get
    the (a,b) coefficient arrays that were PSLQ-tested.
    Returns arrays a_test, b_test (the families that went to PSLQ).
    
    For D=3 b_deg_max=3 (4.2M families), uses chunked processing
    to avoid memory pressure.
    """
    import gc
    from itertools import product as iprod

    # For the huge D=3/b_deg=3 case, chunk by b3 value
    if D >= 3 and b_deg_max == 3:
        n = 2 * D + 1
        a3_vals = list(range(-D, 0)) + list(range(1, D + 1))
        a_rest = list(iprod(range(-D, D + 1), repeat=3))
        a_list = np.array([(a3,) + r for a3 in a3_vals for r in a_rest],
                          dtype=np.int16)

        all_nr_a = []
        all_nr_b = []
        b3_vals = list(range(-D, 0)) + list(range(1, D + 1))

        for b3 in b3_vals:
            b_chunk = np.array([(b3, b2, b1, b0)
                                for b2 in range(-D, D + 1)
                                for b1 in range(-D, D + 1)
                                for b0 in range(-D, D + 1)],
                               dtype=np.int16)
            n_b = len(b_chunk)
            a_full = np.repeat(a_list, n_b, axis=0)
            b_full = np.tile(b_chunk, (len(a_list), 1))
            del b_chunk

            a_nr, b_nr = _screen_and_filter(a_full, b_full, D)
            del a_full, b_full
            gc.collect()

            if len(a_nr) > 0:
                all_nr_a.append(a_nr)
                all_nr_b.append(b_nr)

        if not all_nr_a:
            return np.empty((0, 4), dtype=np.int16), np.empty((0, 4), dtype=np.int16)

        a_nr = np.concatenate(all_nr_a)
        b_nr = np.concatenate(all_nr_b)
        del all_nr_a, all_nr_b
        gc.collect()
    else:
        a_all, b_all = generate_families(D, b_deg_max=b_deg_max)
        a_nr, b_nr = _screen_and_filter(a_all, b_all, D)

    if len(a_nr) == 0:
        return np.empty((0, 4), dtype=np.int16), np.empty((0, 4), dtype=np.int16)

    # Priority sort by b_deg (ascending) — same as original
    b_deg = np.where(b_nr[:, 0] != 0, 3,
            np.where(b_nr[:, 1] != 0, 2,
            np.where(b_nr[:, 2] != 0, 1, 0)))
    priority = np.argsort(b_deg)

    if len(priority) > max_pslq:
        priority = priority[:max_pslq]

    return a_nr[priority], b_nr[priority]


def _test_one_family(args):
    """Worker function for parallel PSLQ testing."""
    idx, a_i, b_i, scan_dps = args
    a_i = list(a_i)
    b_i = list(b_i)

    # Compute K
    K = compute_K_mpmath(a_i, b_i, N=300 if scan_dps <= 80 else 500, dps=scan_dps)
    if K is None:
        return idx, None

    mp.dps = scan_dps
    results = {}

    # T1_ext = {1, K, pi, K*pi, pi^2, K*pi^2, pi^3}
    try:
        basis = [mpf(1), K, mp_pi, K * mp_pi,
                 mp_pi**2, K * mp_pi**2, mp_pi**3]
        rel = pslq(basis, maxcoeff=10**8)
    except Exception:
        rel = None

    if rel is not None:
        residual = fabs(sum(r * v for r, v in zip(rel, basis)))
        if residual < mpf(10)**(-20):  # relaxed threshold for pass 1
            results['T1_ext'] = {
                'hit': True,
                'relation': list(rel),
                'residual': float(residual),
            }

    # T2 = {1, K, pi^2, K*pi^2}
    try:
        basis2 = [mpf(1), K, mp_pi**2, K * mp_pi**2]
        rel2 = pslq(basis2, maxcoeff=10**8)
    except Exception:
        rel2 = None

    if rel2 is not None:
        residual2 = fabs(sum(r * v for r, v in zip(rel2, basis2)))
        if residual2 < mpf(10)**(-20):
            results['T2'] = {
                'hit': True,
                'relation': list(rel2),
                'residual': float(residual2),
            }

    return idx, results


def confirm_hit(a_coeffs, b_coeffs, basis_name, dps=150):
    """Confirm a PSLQ hit at higher precision."""
    K = compute_K_mpmath(a_coeffs, b_coeffs, N=500, dps=dps)
    if K is None:
        return None

    mp.dps = dps
    if basis_name == 'T1_ext':
        basis = [mpf(1), K, mp_pi, K * mp_pi,
                 mp_pi**2, K * mp_pi**2, mp_pi**3]
    elif basis_name == 'T2':
        basis = [mpf(1), K, mp_pi**2, K * mp_pi**2]
    else:
        return None

    try:
        rel = pslq(basis, maxcoeff=10**8)
    except Exception:
        return None

    if rel is not None:
        residual = fabs(sum(r * v for r, v in zip(rel, basis)))
        thresh = mpf(10)**(-30) if dps >= 150 else mpf(10)**(-20)
        if residual < thresh:
            return {'relation': list(rel), 'residual': float(residual),
                    'confirmed': True, 'dps': dps}
    return {'confirmed': False}


def main():
    start_time = time.time()

    print("=" * 60)
    print("EXTENDED BASIS TEST — d=3 Desert families")
    print(f"Task: {TASK_ID}")
    print("Two-pass: dps=80 scan -> dps=150/300 confirmation")
    print("=" * 60)

    # Reproduce the exact same families from L0-SCALE-SELECTOR-POC
    print("\n--- Phase 1: Reproducing PSLQ candidate sets ---")

    batches = [
        # (D, max_pslq, b_deg_max, label)
        (1, 3000, None, "D=1 full"),
        (2, 3000, None, "D=2 full"),
        (3, 3000, 1, "D=3 b_deg<=1"),
        (3, 3000, 2, "D=3 b_deg=2"),
        (3, 1000, 3, "D=3 b_deg=3"),
        (4, 2000, 1, "D=4 b_deg<=1"),
    ]

    all_a = []
    all_b = []
    all_labels = []

    for D, max_pslq, b_deg_max, label in batches:
        print(f"  {label}: ", end="", flush=True)
        a_test, b_test = get_pslq_candidates(D, max_pslq, b_deg_max)
        print(f"{len(a_test)} families")
        all_a.append(a_test)
        all_b.append(b_test)
        all_labels.extend([label] * len(a_test))

    a_all = np.concatenate(all_a)
    b_all = np.concatenate(all_b)
    n_total = len(a_all)
    del all_a, all_b
    print(f"\n  Total families to retest: {n_total}")

    # Phase 2: Quick scan at dps=80
    print(f"\n--- Phase 2: Quick PSLQ scan (dps=80, {n_total} families) ---")
    scan_dps = 80

    pass1_t1_hits = []
    pass1_t2_hits = []
    n_tested = 0

    for i in range(n_total):
        if (i + 1) % 500 == 0:
            elapsed = time.time() - start_time
            rate = (i + 1) / elapsed if elapsed > 0 else 0
            eta = (n_total - i - 1) / rate if rate > 0 else 0
            print(f"  ... {i+1}/{n_total} ({elapsed:.0f}s, ~{eta:.0f}s left, "
                  f"T1_ext={len(pass1_t1_hits)}, T2={len(pass1_t2_hits)})")

        a_i = a_all[i]
        b_i = b_all[i]

        K = compute_K_mpmath(a_i, b_i, N=300, dps=scan_dps)
        if K is None:
            continue

        n_tested += 1
        mp.dps = scan_dps

        # T1_ext
        try:
            basis = [mpf(1), K, mp_pi, K * mp_pi,
                     mp_pi**2, K * mp_pi**2, mp_pi**3]
            rel = pslq(basis, maxcoeff=10**8)
        except Exception:
            rel = None

        if rel is not None:
            residual = fabs(sum(r * v for r, v in zip(rel, basis)))
            if residual < mpf(10)**(-20):
                pass1_t1_hits.append({
                    'idx': i,
                    'a': list(int(c) for c in a_i),
                    'b': list(int(c) for c in b_i),
                    'relation': list(rel),
                    'residual': float(residual),
                })
                print(f"  ** T1_ext candidate at dps=80: a={list(a_i)} "
                      f"b={list(b_i)} K~{nstr(K, 12)}")

        # T2
        try:
            basis2 = [mpf(1), K, mp_pi**2, K * mp_pi**2]
            rel2 = pslq(basis2, maxcoeff=10**8)
        except Exception:
            rel2 = None

        if rel2 is not None:
            residual2 = fabs(sum(r * v for r, v in zip(rel2, basis2)))
            if residual2 < mpf(10)**(-20):
                pass1_t2_hits.append({
                    'idx': i,
                    'a': list(int(c) for c in a_i),
                    'b': list(int(c) for c in b_i),
                    'relation': list(rel2),
                    'residual': float(residual2),
                })
                print(f"  ** T2 candidate at dps=80: a={list(a_i)} "
                      f"b={list(b_i)} K~{nstr(K, 12)}")

    scan_time = time.time() - start_time
    print(f"\n  Pass 1 complete: {n_tested} tested in {scan_time:.0f}s")
    print(f"  T1_ext candidates: {len(pass1_t1_hits)}")
    print(f"  T2 candidates: {len(pass1_t2_hits)}")

    # Phase 3: Confirm hits at dps=150 then dps=300
    t1_ext_confirmed = []
    t2_confirmed = []

    if pass1_t1_hits or pass1_t2_hits:
        print(f"\n--- Phase 3: Confirmation at dps=150/300 ---")

        for hit in pass1_t1_hits:
            conf150 = confirm_hit(hit['a'], hit['b'], 'T1_ext', dps=150)
            if conf150 and conf150.get('confirmed'):
                conf300 = confirm_hit(hit['a'], hit['b'], 'T1_ext', dps=300)
                if conf300 and conf300.get('confirmed'):
                    entry = {
                        'a': hit['a'],
                        'b': hit['b'],
                        'K_approx': nstr(compute_K_mpmath(hit['a'], hit['b'],
                                         N=500, dps=150), 30),
                        'basis': 'T1_ext',
                        'relation': conf300['relation'],
                        'residual': conf300['residual'],
                        'source': all_labels[hit['idx']],
                    }
                    t1_ext_confirmed.append(entry)
                    print(f"  *** T1_ext CONFIRMED: a={entry['a']} "
                          f"b={entry['b']} ***")

        for hit in pass1_t2_hits:
            conf150 = confirm_hit(hit['a'], hit['b'], 'T2', dps=150)
            if conf150 and conf150.get('confirmed'):
                conf300 = confirm_hit(hit['a'], hit['b'], 'T2', dps=300)
                if conf300 and conf300.get('confirmed'):
                    entry = {
                        'a': hit['a'],
                        'b': hit['b'],
                        'K_approx': nstr(compute_K_mpmath(hit['a'], hit['b'],
                                         N=500, dps=150), 30),
                        'basis': 'T2',
                        'relation': conf300['relation'],
                        'residual': conf300['residual'],
                        'source': all_labels[hit['idx']],
                    }
                    t2_confirmed.append(entry)
                    print(f"  *** T2 CONFIRMED: a={entry['a']} "
                          f"b={entry['b']} ***")
    else:
        print("\n  No candidates to confirm — skipping Phase 3.")

    runtime = time.time() - start_time

    # Build results
    new_trans = len(t1_ext_confirmed) + len(t2_confirmed)
    verdict = "TRANS-FOUND" if new_trans > 0 else "NULL"

    report = {
        "task_id": TASK_ID,
        "date": __import__('datetime').datetime.now(
            __import__('datetime').timezone.utc).isoformat(),
        "families_retested": n_tested,
        "families_reproduced": n_total,
        "scan_dps": scan_dps,
        "confirm_dps": [150, 300],
        "T1_ext_candidates_pass1": len(pass1_t1_hits),
        "T1_ext_confirmed": len(t1_ext_confirmed),
        "T1_ext_details": t1_ext_confirmed,
        "T2_candidates_pass1": len(pass1_t2_hits),
        "T2_confirmed": len(t2_confirmed),
        "T2_details": t2_confirmed,
        "new_trans_found": new_trans,
        "verdict": verdict,
        "runtime_seconds": round(runtime, 1),
        "bases_tested": {
            "T1_ext": "{1, K, pi, K*pi, pi^2, K*pi^2, pi^3}",
            "T2": "{1, K, pi^2, K*pi^2}",
        },
        "method": "Two-pass: dps=80 scan then dps=150/300 confirmation",
    }

    # Write report
    report_path = os.path.join(OUT_DIR, "extended_basis_results.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\n  Written: extended_basis_results.json")

    # Write AEAL claim
    report_hash = hashlib.sha256(json.dumps(report).encode()).hexdigest()
    claim = {
        "claim": (f"Extended basis test on {n_tested} d=3 families: "
                  f"T1_ext confirmed={len(t1_ext_confirmed)}, "
                  f"T2 confirmed={len(t2_confirmed)}, "
                  f"verdict={verdict}"),
        "evidence_type": "computation",
        "dps": 80,
        "confirmation_dps": 300,
        "reproducible": True,
        "script": "extended_basis_test.py",
        "output_hash": report_hash,
    }
    claims_path = os.path.join(OUT_DIR, "claims.jsonl")
    with open(claims_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(claim) + "\n")
    print(f"  Written: claims.jsonl")

    # Summary
    print(f"\n{'='*60}")
    print("EXTENDED BASIS TEST COMPLETE")
    print(f"  Families retested: {n_tested}")
    print(f"  Pass 1 (dps=80):  T1_ext={len(pass1_t1_hits)}, T2={len(pass1_t2_hits)}")
    print(f"  Confirmed (300):  T1_ext={len(t1_ext_confirmed)}, T2={len(t2_confirmed)}")
    print(f"  New Trans found: {new_trans}")
    print(f"  Verdict: {verdict}")
    print(f"  Runtime: {runtime:.0f}s")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
