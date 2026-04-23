#!/usr/bin/env python3
"""
Layer 0 Scale Selector — POC
Search F(3,D) for Trans-stratum families.
Task: L0-SCALE-SELECTOR-POC
"""
import json
import os
import sys
import time

import numpy as np
from mpmath import mp, nstr

sys.path.insert(0, os.path.dirname(__file__))

from screener import generate_families, apply_screens
from classifier import (
    compute_K_batch_lentz, rat_prescreen_float,
    compute_K_mpmath, classify_single, confirm_classification,
)
from report import (
    structural_check_family, build_structural_comparison,
    build_report, format_markdown, write_claims,
)

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
TASK_ID = "L0-SCALE-SELECTOR-POC"

# ---------------------------------------------------------------------------
# Search at a single D
# ---------------------------------------------------------------------------

def search_profile(a_coeffs, b_coeffs, D, profile_name, max_pslq=3000):
    """
    Run the full pipeline for a batch of families at a given D.
    Returns (trans_list, stats_dict).
    """
    n_total = len(a_coeffs)
    if n_total == 0:
        return [], {'enumerated': 0, 'screened': 0, 'pslq': 0}

    print(f"    [{profile_name}] {n_total:,} families")

    # Screen 1: structural Rat
    screens = apply_screens(a_coeffs, b_coeffs, D, verbose=True)
    cand_mask = screens['candidate']
    n_cand = int(cand_mask.sum())

    if n_cand == 0:
        print(f"    [{profile_name}] No candidates after screening")
        return [], {'enumerated': n_total, 'screened': n_cand, 'pslq': 0}

    a_cand = a_coeffs[cand_mask]
    b_cand = b_coeffs[cand_mask]

    # Float64 batch K + convergence
    print(f"    [{profile_name}] Computing K (float64, N=200)...")
    K_float, converged = compute_K_batch_lentz(a_cand, b_cand, N=200)
    n_conv = int(converged.sum())
    print(f"    [{profile_name}] {n_conv:,} converged")

    if n_conv == 0:
        return [], {'enumerated': n_total, 'screened': n_cand, 'pslq': 0}

    a_conv = a_cand[converged]
    b_conv = b_cand[converged]
    K_conv = K_float[converged]

    # Float64 Rat prescreen
    likely_rat = rat_prescreen_float(K_conv, max_q=300, tol=1e-4)
    non_rat_mask = ~likely_rat
    n_nonrat = int(non_rat_mask.sum())
    print(f"    [{profile_name}] {n_nonrat:,} non-rational after float prescreen")

    if n_nonrat == 0:
        return [], {'enumerated': n_total, 'screened': n_cand, 'pslq': 0}

    a_nr = a_conv[non_rat_mask]
    b_nr = b_conv[non_rat_mask]
    K_nr = K_conv[non_rat_mask]

    # Prioritize by degree profile: b_deg < a_deg first
    b_deg = np.where(b_nr[:, 0] != 0, 3,
            np.where(b_nr[:, 1] != 0, 2,
            np.where(b_nr[:, 2] != 0, 1, 0)))
    priority = np.argsort(b_deg)  # lower b_deg first

    # Limit PSLQ candidates
    if n_nonrat > max_pslq:
        print(f"    [{profile_name}] Limiting to {max_pslq} candidates (from {n_nonrat})")
        priority = priority[:max_pslq]

    n_pslq = len(priority)
    print(f"    [{profile_name}] Running PSLQ on {n_pslq} candidates...")

    trans_found = []
    n_rat_pslq = 0
    n_desert = 0

    for i, idx in enumerate(priority):
        if (i + 1) % 200 == 0:
            print(f"      ... {i+1}/{n_pslq} ({len(trans_found)} Trans, "
                  f"{n_rat_pslq} Rat, {n_desert} Desert)")

        a_i = a_nr[idx]
        b_i = b_nr[idx]

        # High-precision K
        K_hp = compute_K_mpmath(a_i, b_i, N=500, dps=150)
        if K_hp is None:
            n_desert += 1
            continue

        # PSLQ
        result = classify_single(K_hp, dps=150)

        if result['stratum'] == 'Rat':
            n_rat_pslq += 1
        elif result['stratum'] == 'Trans':
            # Confirm at dps=300
            confirm = confirm_classification(a_i, b_i, result, dps=300)
            if confirm and confirm['stratum'] == 'Trans':
                K_str = nstr(K_hp, 20)
                sc = structural_check_family(a_i, b_i, K_str, confirm)
                trans_found.append({
                    'D': D,
                    'a': list(int(c) for c in a_i),
                    'b': list(int(c) for c in b_i),
                    'K_approx': nstr(K_hp, 50),
                    'pslq_relation': confirm['relation'],
                    'residual': confirm['residual'],
                    'structural': sc,
                    'basis': confirm['basis'],
                })
                print(f"      *** TRANS FOUND: a={list(a_i)} b={list(b_i)} "
                      f"K~{nstr(K_hp, 12)} ***")
            elif confirm and confirm['stratum'] == 'Log':
                # Unexpected: log hit
                print(f"      !!! UNEXPECTED LOG HIT: a={list(a_i)} b={list(b_i)} "
                      f"basis={confirm['basis']}")
                # Write to unexpected_finds
                write_unexpected(a_i, b_i, K_hp, confirm)
            else:
                n_desert += 1
        elif result['stratum'] == 'Log':
            print(f"      !!! UNEXPECTED LOG HIT: a={list(a_i)} b={list(b_i)}")
            write_unexpected(a_i, b_i, K_hp, result)
        else:
            n_desert += 1

    print(f"    [{profile_name}] Done: {len(trans_found)} Trans, "
          f"{n_rat_pslq} Rat, {n_desert} Desert")

    return trans_found, {
        'enumerated': n_total,
        'screened': n_cand,
        'pslq': n_pslq,
    }


def search_at_D(D):
    """
    Search F(3,D) for Trans families.
    Uses profile-based generation for D >= 3.
    """
    print(f"\n  Searching F(3,{D})...")
    all_trans = []
    stats = {'enumerated': 0, 'screened': 0, 'pslq': 0}

    if D <= 2:
        # Full enumeration
        a_all, b_all = generate_families(D)
        trans, st = search_profile(a_all, b_all, D, f"full-D{D}")
        all_trans.extend(trans)
        for k in st:
            stats[k] += st[k]
    else:
        # Profile-based: (3,<=1) then (3,2) then (3,3)
        for b_deg_max, name in [(1, "b_deg<=1"), (2, "b_deg=2"), (3, "b_deg=3")]:
            if all_trans:
                print(f"    Skipping {name} — Trans already found")
                break
            a_p, b_p = generate_families(D, b_deg_max=b_deg_max)
            trans, st = search_profile(a_p, b_p, D, name,
                                       max_pslq=3000 if b_deg_max <= 2 else 1000)
            all_trans.extend(trans)
            for k in st:
                stats[k] += st[k]
            del a_p, b_p  # free memory

    return all_trans, stats


def write_unexpected(a_coeffs, b_coeffs, K, result):
    """Write unexpected find to unexpected_finds.json."""
    path = os.path.join(OUT_DIR, "unexpected_finds.json")
    try:
        with open(path) as f:
            data = json.load(f)
            if isinstance(data, dict) and not data:
                data = []
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    data.append({
        'a': list(int(c) for c in a_coeffs),
        'b': list(int(c) for c in b_coeffs),
        'K_approx': nstr(K, 20),
        'stratum': result['stratum'],
        'basis': result['basis'],
        'relation': result['relation'],
    })
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    start_time = time.time()

    print("=" * 60)
    print("LAYER 0 SCALE SELECTOR — POC")
    print("Task: L0-SCALE-SELECTOR-POC")
    print("Target: Trans-stratum families at d=3")
    print("=" * 60)

    D_searched = []
    D_min = None
    all_trans = []
    families_enum = {}
    families_screened = {}
    families_pslq = {}

    for D in [1, 2, 3]:
        elapsed = time.time() - start_time
        print(f"\n{'='*60}")
        print(f"D = {D}  (elapsed: {elapsed:.0f}s)")
        print(f"{'='*60}")

        D_searched.append(D)
        trans, stats = search_at_D(D)

        D_str = f"D={D}"
        families_enum[D_str] = stats['enumerated']
        families_screened[D_str] = stats['screened']
        families_pslq[D_str] = stats['pslq']

        if trans:
            all_trans.extend(trans)
            D_min = D
            print(f"\n*** {len(trans)} TRANS FAMILIES FOUND AT D={D}! ***")

            if D == 1:
                # HALT: unexpected
                print("!!! HALT: Trans at D=1 is unexpected !!!")
                halt_data = {
                    "reason": "Trans found at D=1 — unexpectedly small",
                    "families": [{'a': t['a'], 'b': t['b']} for t in trans],
                }
                with open(os.path.join(OUT_DIR, "halt_log.json"), "w",
                          encoding="utf-8") as f:
                    json.dump(halt_data, f, indent=2)
            break
        else:
            print(f"\n  No Trans at D={D}.")

        # Check runtime for D=3+
        if D >= 3 and (time.time() - start_time) > 600:
            print("  Runtime limit reached (>10min). Stopping.")
            break

    # --- D=4 sampling if nothing found ---
    if D_min is None and max(D_searched) >= 3:
        elapsed = time.time() - start_time
        if elapsed < 1800:  # still have time
            D = 4
            print(f"\n{'='*60}")
            print(f"D = {D} (sampling mode, elapsed: {elapsed:.0f}s)")
            print(f"{'='*60}")
            D_searched.append(D)
            # Only check (3,<=1) profile at D=4
            a_p, b_p = generate_families(D, b_deg_max=1)
            trans, stats = search_profile(a_p, b_p, D, "b_deg<=1-sample",
                                          max_pslq=2000)
            D_str = f"D={D}"
            families_enum[D_str] = stats['enumerated']
            families_screened[D_str] = stats['screened']
            families_pslq[D_str] = stats['pslq']
            if trans:
                all_trans.extend(trans)
                D_min = D
                print(f"\n*** {len(trans)} TRANS FOUND AT D={D}! ***")

    # --- Build reports ---
    runtime = time.time() - start_time
    print(f"\n{'='*60}")
    print(f"BUILDING REPORTS (total runtime: {runtime:.0f}s)")
    print(f"{'='*60}")

    structural_comp = build_structural_comparison(all_trans)

    report = build_report(
        task_id=TASK_ID,
        D_searched=D_searched,
        D_min=D_min,
        trans_families=all_trans,
        families_enumerated=families_enum,
        families_screened=families_screened,
        families_pslq=families_pslq,
        structural_comparison=structural_comp,
        runtime=runtime,
    )

    # Write outputs
    report_path = os.path.join(OUT_DIR, "scale_selector_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"  Written: scale_selector_report.json")

    md_path = os.path.join(OUT_DIR, "scale_selector_report.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(format_markdown(report))
    print(f"  Written: scale_selector_report.md")

    sc_path = os.path.join(OUT_DIR, "structural_comparison.json")
    with open(sc_path, "w", encoding="utf-8") as f:
        json.dump(structural_comp, f, indent=2, ensure_ascii=False)
    print(f"  Written: structural_comparison.json")

    claims_path = os.path.join(OUT_DIR, "claims.jsonl")
    claims = write_claims(report, claims_path)
    print(f"  Written: claims.jsonl ({len(claims)} claims)")

    # Empty log files if not created
    for fname in ["halt_log.json", "discrepancy_log.json", "unexpected_finds.json"]:
        fpath = os.path.join(OUT_DIR, fname)
        if not os.path.exists(fpath):
            with open(fpath, "w", encoding="utf-8") as f:
                json.dump({}, f)

    # Summary
    print(f"\n{'='*60}")
    print("SEARCH COMPLETE")
    print(f"  D values searched: {D_searched}")
    print(f"  D_min: {D_min or 'NOT FOUND'}")
    print(f"  Trans found: {len(all_trans)}")
    print(f"  Runtime: {runtime:.0f}s")
    print(f"\n  KEY FINDING: {report['key_finding']}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
