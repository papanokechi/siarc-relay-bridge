#!/usr/bin/env python3
"""
PCF Cross-Family Correlator — SIARC v2.0 Layer 3 POC

Reads a PCF certificate (input.json) and produces an enrichment report
identifying which structural parameters are over/under-represented
in each stratum compared to the full-space prior.

Usage:
    python correlator.py input.json
    python correlator.py --test   # run on synthetic test data
"""

import itertools
import json
import os
import random
import sys
import time
from collections import Counter

from parameters import extract_parameters, CATEGORICAL_PARAMS, CONTINUOUS_PARAMS
from enrichment import (
    compute_enrichment_categorical,
    compute_enrichment_continuous,
    classify_signals,
)
from report import write_reports

COEFF_RANGE = range(-4, 5)  # [-4, 4]
MAX_K = 20  # check a(k)=0 for k in [0, MAX_K]
RAT_SAMPLE = 200   # ~22% of 1000, matching real Rat/Des ratio
DES_SAMPLE = 500


def load_certificate(path):
    """Load the base certificate JSON."""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_desert_certificate(base_dir):
    """Try to load the desert certificate from the same directory or parent."""
    for candidate in [
        os.path.join(base_dir, 'desert_certificate.json'),
        os.path.join(os.path.dirname(base_dir), 'desert_certificate.json'),
    ]:
        if os.path.exists(candidate):
            with open(candidate, 'r', encoding='utf-8') as f:
                return json.load(f)
    return None


def enumerate_structural_rat(sample_size=RAT_SAMPLE):
    """Enumerate structural Rat families from [-4,4]^6.

    A family is structural Rat if a(k) = a2*k^2 + a1*k + a0 = 0
    for some integer k in [0, MAX_K].
    """
    print("  Enumerating structural Rat families from [-4,4]^6...")
    rat_families = []

    for a2, a1, a0 in itertools.product(COEFF_RANGE, repeat=3):
        # Check if a(k)=0 for any k in [0, MAX_K]
        has_root = False
        for k in range(0, MAX_K + 1):
            if a2 * k * k + a1 * k + a0 == 0:
                has_root = True
                break
        if not has_root:
            continue

        # This a-triple produces Rat for any convergent b-triple.
        # Certificate stores [a2, a1, a0] order.
        for b2, b1, b0 in itertools.product(COEFF_RANGE, repeat=3):
            # Skip degenerate b = (0,0,0)
            if b0 == 0 and b1 == 0 and b2 == 0:
                continue
            rat_families.append({
                'a': [a2, a1, a0],
                'b': [b2, b1, b0],
            })

    print("  Found %d structural Rat families" % len(rat_families))

    if len(rat_families) > sample_size:
        random.seed(42)
        rat_families = random.sample(rat_families, sample_size)
        print("  Sampled %d for POC" % sample_size)

    return rat_families


def reconstruct_families(cert, base_dir):
    """Reconstruct flat list of (family, stratum) records from certificate.

    Returns list of dicts: {'family': {'a': [...], 'b': [...]}, 'stratum': str}
    """
    records = []

    # --- Trans families (all 24, explicit in certificate) ---
    trans_data = cert.get('strata', {}).get('Trans', {})
    trans_fams = trans_data.get('families', [])
    for entry in trans_fams:
        fam = entry.get('family', entry)
        records.append({'family': fam, 'stratum': 'Trans'})
    print("  Trans: %d families" % len(trans_fams))

    # --- Desert families (from desert_certificate.json) ---
    des_cert = load_desert_certificate(base_dir)
    des_families = []
    if des_cert:
        sample = des_cert.get('cert_sample_500', [])
        for entry in sample:
            fam = entry.get('family', entry)
            des_families.append(fam)
    # If we don't have enough desert families from certificate, generate some
    # by excluding known Trans and Rat from the coefficient space.
    if len(des_families) < DES_SAMPLE:
        print("  Desert certificate has %d families, supplementing..." %
              len(des_families))
        des_families = _supplement_desert(
            des_families, trans_fams, DES_SAMPLE
        )
    for fam in des_families[:DES_SAMPLE]:
        records.append({'family': fam, 'stratum': 'Des'})
    print("  Des: %d families" % len(des_families[:DES_SAMPLE]))

    # --- Rat families (enumerate structural Rat) ---
    rat_families = enumerate_structural_rat(RAT_SAMPLE)
    for fam in rat_families:
        records.append({'family': fam, 'stratum': 'Rat'})
    print("  Rat: %d families" % len(rat_families))

    # --- Log, Alg (count=0 in this certificate) ---
    for stratum in ['Log', 'Alg']:
        s_data = cert.get('strata', {}).get(stratum, {})
        s_fams = s_data.get('families', [])
        for entry in s_fams:
            fam = entry.get('family', entry)
            records.append({'family': fam, 'stratum': stratum})
        if s_fams:
            print("  %s: %d families" % (stratum, len(s_fams)))

    return records


def _supplement_desert(existing, trans_fams, target):
    """Generate additional Desert-candidate families.

    Families that are NOT structural Rat and NOT Trans are Desert candidates.
    """
    trans_set = set()
    for entry in trans_fams:
        fam = entry.get('family', entry)
        key = (tuple(fam['a']), tuple(fam['b']))
        trans_set.add(key)

    candidates = list(existing)
    existing_set = set(
        (tuple(f['a']), tuple(f['b'])) for f in existing
    )

    random.seed(123)
    # Sample from coefficient space, filtering out structural Rat and Trans
    all_coeffs = list(itertools.product(COEFF_RANGE, repeat=3))
    random.shuffle(all_coeffs)

    for a_tuple in all_coeffs:
        if len(candidates) >= target:
            break
        a2, a1, a0 = a_tuple

        # Skip if structural Rat (a(k)=0 for some k)
        is_rat = False
        for k in range(0, MAX_K + 1):
            if a2 * k * k + a1 * k + a0 == 0:
                is_rat = True
                break
        if is_rat:
            continue

        for b_tuple in all_coeffs:
            if len(candidates) >= target:
                break
            b0, b1, b2 = b_tuple
            if b0 == 0 and b1 == 0 and b2 == 0:
                continue
            key = (a_tuple, b_tuple)
            if key in trans_set or key in existing_set:
                continue

            candidates.append({'a': list(a_tuple), 'b': list(b_tuple)})
            existing_set.add(key)

    return candidates


def run_pipeline(records, output_dir):
    """Run the full correlator pipeline: extract -> enrich -> report."""

    # Step 1: Extract parameters
    print("\n[Step 1] Extracting parameters for %d families..." % len(records))
    t0 = time.time()
    for rec in records:
        rec['params'] = extract_parameters(rec['family'])
    t1 = time.time()
    print("  Done in %.2fs" % (t1 - t0))

    # Collect strata info
    strata_list = sorted(set(r['stratum'] for r in records))
    stratum_counts = Counter(r['stratum'] for r in records)
    print("  Strata: %s" % dict(stratum_counts))

    # Step 2: Enrichment analysis — categorical
    print("\n[Step 2] Computing categorical enrichment...")
    t0 = time.time()
    all_categorical = []
    for param in CATEGORICAL_PARAMS:
        results = compute_enrichment_categorical(records, param, strata_list)
        all_categorical.extend(results)
    t1 = time.time()
    print("  %d enrichment entries in %.2fs" % (len(all_categorical), t1 - t0))

    # Step 3: Enrichment analysis — continuous
    print("\n[Step 3] Computing continuous parameter summaries...")
    t0 = time.time()
    all_continuous = []
    for param in CONTINUOUS_PARAMS:
        results = compute_enrichment_continuous(records, param, strata_list)
        all_continuous.extend(results)
    t1 = time.time()
    print("  %d continuous entries in %.2fs" % (len(all_continuous), t1 - t0))

    # Step 4: Classify signals
    print("\n[Step 4] Classifying signals...")
    discovery, strong, null_params = classify_signals(all_categorical)
    print("  Discovery candidates: %d" % len(discovery))
    print("  Strong signals: %d" % len(strong))
    print("  Null-result parameters: %d" % len(null_params))

    # Step 5: Generate reports
    print("\n[Step 5] Writing reports...")
    md_path, json_path = write_reports(
        discovery, strong, null_params,
        all_categorical, all_continuous,
        stratum_counts, output_dir,
    )
    print("  %s" % md_path)
    print("  %s" % json_path)

    # Validation checks
    _validate(discovery, strong)

    return discovery, strong


def _validate(discovery, strong):
    """Check that known enrichment patterns are recovered."""
    print("\n[Validation] Checking known structural results...")
    all_signals = discovery + strong

    # Check 1: b2_is_zero enriched in Trans
    b2_trans = [r for r in all_signals
                if r['parameter'] == 'b2_is_zero'
                and r['value'] is True
                and r['stratum'] == 'Trans']
    if b2_trans:
        print("  PASS: b2_is_zero=True enriched in Trans (ratio=%.1f)" %
              b2_trans[0]['enrichment_ratio'])
    else:
        print("  WARN: b2_is_zero=True NOT flagged in Trans — check data")

    # Check 2: a_eval_1_is_zero enriched in Rat
    ae1_rat = [r for r in all_signals
               if r['parameter'] == 'a_eval_1_is_zero'
               and r['value'] is True
               and r['stratum'] == 'Rat']
    if ae1_rat:
        print("  PASS: a_eval_1_is_zero=True enriched in Rat (ratio=%.1f)" %
              ae1_rat[0]['enrichment_ratio'])
    else:
        print("  WARN: a_eval_1_is_zero=True NOT flagged in Rat — check data")

    # Check 3: degree_profile (2,1) enriched in Trans
    dp_trans = [r for r in all_signals
                if r['parameter'] == 'degree_profile'
                and r['value'] == '(2,1)'
                and r['stratum'] == 'Trans']
    if dp_trans:
        print("  PASS: degree_profile=(2,1) enriched in Trans (ratio=%.1f)" %
              dp_trans[0]['enrichment_ratio'])
    else:
        print("  WARN: degree_profile=(2,1) NOT flagged in Trans — check data")


def main():
    if len(sys.argv) < 2:
        print("Usage: python correlator.py input.json")
        print("       python correlator.py --test")
        sys.exit(1)

    output_dir = os.path.dirname(os.path.abspath(__file__))
    t_start = time.time()

    if sys.argv[1] == '--test':
        print("=" * 60)
        print("PCF Cross-Family Correlator — TEST MODE")
        print("=" * 60)
        from test_data import make_test_data
        records = make_test_data()
    else:
        input_path = sys.argv[1]
        if not os.path.exists(input_path):
            print("ERROR: %s not found" % input_path)
            sys.exit(1)

        print("=" * 60)
        print("PCF Cross-Family Correlator — SIARC v2.0 Layer 3 POC")
        print("=" * 60)
        print("\nLoading certificate: %s" % input_path)
        cert = load_certificate(input_path)
        base_dir = os.path.dirname(os.path.abspath(input_path))

        print("\n[Step 0] Reconstructing family list from certificate...")
        records = reconstruct_families(cert, base_dir)

    print("\nTotal records: %d" % len(records))
    discovery, strong = run_pipeline(records, output_dir)

    t_end = time.time()
    print("\n" + "=" * 60)
    print("Correlator finished in %.1fs" % (t_end - t_start))
    print("Discovery candidates: %d" % len(discovery))
    print("Strong signals: %d" % len(strong))
    print("=" * 60)


if __name__ == '__main__':
    main()
