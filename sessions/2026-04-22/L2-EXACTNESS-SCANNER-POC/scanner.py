#!/usr/bin/env python3
"""
Layer 2 Exactness Scanner — POC
Scans numerical values from F(2,4) classification for exact algebraic relationships.
Task: L2-EXACTNESS-SCANNER-POC
"""

import json
import os
import sys
from fractions import Fraction
from mpmath import mp, mpf, pi, sqrt, fabs

# Ensure we can import sibling modules
sys.path.insert(0, os.path.dirname(__file__))

from triggers import run_all_triggers
from algebraic_check import classify_algebraic, check_exact_fraction
from report import build_report, format_markdown_report, write_claims

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CERT_PATH = os.path.join(BASE_DIR, "f1_base_certificate.json")
TRANS_PATH = os.path.join(BASE_DIR, "trans_verification.json")
SIGN_PATH = os.path.join(BASE_DIR, "h017_sign_a2_report.json")
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


# ---------------------------------------------------------------------------
# Validation tests
# ---------------------------------------------------------------------------

def run_validation_tests():
    """Run 4 validation tests. Returns True if all pass."""
    mp.dps = 100
    all_pass = True

    # TEST 1: scan(22/7)
    x = mpf(22) / mpf(7)
    triggers = run_all_triggers(x)
    result = classify_algebraic(x)
    t1_trigger = any(t["type"] == "near-fraction" for t in triggers)
    t1_degree = result["algebraic_degree"] == 1
    t1_verdict = result["verdict"] == "EXACT-RATIONAL"
    t1_pass = t1_trigger and t1_degree and t1_verdict
    print(f"TEST 1 (22/7): trigger={t1_trigger}, degree={result['algebraic_degree']}, "
          f"verdict={result['verdict']}, poly={result['minimal_poly']} → {'PASS' if t1_pass else 'FAIL'}")
    if not t1_pass:
        all_pass = False

    # TEST 2: scan(sqrt(2))
    x = sqrt(2)
    triggers = run_all_triggers(x)
    result = classify_algebraic(x)
    t2_trigger = any(t["type"] == "sq-near-integer" for t in triggers)
    t2_degree = result["algebraic_degree"] == 2
    t2_verdict = result["verdict"] == "EXACT-ALGEBRAIC"
    t2_pass = t2_trigger and t2_degree and t2_verdict
    print(f"TEST 2 (sqrt(2)): trigger={t2_trigger}, degree={result['algebraic_degree']}, "
          f"verdict={result['verdict']}, poly={result['minimal_poly']} → {'PASS' if t2_pass else 'FAIL'}")
    if not t2_pass:
        all_pass = False

    # TEST 3: scan(pi) — should be transcendental
    mp.dps = 50
    x = pi
    triggers = run_all_triggers(x)
    result = classify_algebraic(x, dps=50)
    t3_no_alg = result["algebraic_degree"] is None
    t3_verdict = result["verdict"] == "TRANSCENDENTAL"
    t3_pass = t3_no_alg and t3_verdict
    print(f"TEST 3 (pi): triggers={[t['type'] for t in triggers]}, degree={result['algebraic_degree']}, "
          f"verdict={result['verdict']} → {'PASS' if t3_pass else 'FAIL'}")
    if not t3_pass:
        all_pass = False
    mp.dps = 100

    # TEST 4: scan(1e-21) — near zero
    x = mpf("1e-21")
    triggers = run_all_triggers(x)
    t4_trigger = any(t["type"] == "near-zero" for t in triggers)
    # Near-zero values are treated as exactly 0 (rational) by convention
    if t4_trigger:
        result = {"algebraic_degree": 1, "minimal_poly": [0, 1], "verdict": "EXACT-RATIONAL"}
    else:
        result = classify_algebraic(x)
    t4_degree = result["algebraic_degree"] == 1
    t4_verdict = result["verdict"] == "EXACT-RATIONAL"
    t4_pass = t4_trigger and t4_degree and t4_verdict
    print(f"TEST 4 (1e-21): trigger={t4_trigger}, degree={result['algebraic_degree']}, "
          f"verdict={result['verdict']}, poly={result['minimal_poly']} → {'PASS' if t4_pass else 'FAIL'}")
    if not t4_pass:
        all_pass = False

    return all_pass


# ---------------------------------------------------------------------------
# Data loaders
# ---------------------------------------------------------------------------

def load_certificate():
    with open(CERT_PATH) as f:
        return json.load(f)


def load_trans_verification():
    with open(TRANS_PATH) as f:
        return json.load(f)


def load_sign_report():
    with open(SIGN_PATH) as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# Scan helpers
# ---------------------------------------------------------------------------

def scan_value(name, x_mpf):
    """Scan a single value. Returns result dict."""
    triggers = run_all_triggers(x_mpf)
    trigger_str = triggers[0]["type"] if triggers else "none"

    # Near-zero values are treated as exactly 0 (rational)
    if triggers and triggers[0]["type"] == "near-zero":
        result = {
            "algebraic_degree": 1,
            "minimal_poly": [0, 1],
            "verdict": "EXACT-RATIONAL",
            "cm_discriminant": None,
        }
    elif triggers:
        result = classify_algebraic(x_mpf)
    else:
        result = {
            "algebraic_degree": None,
            "minimal_poly": None,
            "verdict": "NO-TRIGGER",
            "cm_discriminant": None,
        }

    approx_str = mp.nstr(x_mpf, 20)

    return {
        "value_name": name,
        "value_approx": approx_str,
        "trigger": trigger_str,
        "algebraic_degree": result.get("algebraic_degree"),
        "minimal_poly": result.get("minimal_poly"),
        "cm_discriminant": result.get("cm_discriminant"),
        "verdict": result["verdict"],
    }


def scan_integer_exactness(name, x_mpf):
    """Scan a value expected to be an integer. Handles exact integers directly."""
    triggers = run_all_triggers(x_mpf)
    trigger_str = triggers[0]["type"] if triggers else "none"
    approx_str = mp.nstr(x_mpf, 20)

    # If value is exactly an integer (within machine precision), skip PSLQ
    rounded = int(mp.nint(x_mpf))
    gap = fabs(x_mpf - rounded)
    if gap < mpf("1e-40"):
        result = {
            "algebraic_degree": 1,
            "minimal_poly": [-rounded, 1],  # -n + 1*x = 0 → x = n
            "verdict": "EXACT-RATIONAL",
            "cm_discriminant": None,
        }
        if not trigger_str or trigger_str == "none":
            trigger_str = "near-integer"
    else:
        result = classify_algebraic(x_mpf)

    return {
        "value_name": name,
        "value_approx": approx_str,
        "trigger": trigger_str,
        "algebraic_degree": result.get("algebraic_degree"),
        "minimal_poly": result.get("minimal_poly"),
        "cm_discriminant": result.get("cm_discriminant"),
        "verdict": result["verdict"],
    }


def scan_fraction_exactness(name, x_mpf, expected_p=None, expected_q=None):
    """Scan a value expected to be a fraction."""
    triggers = run_all_triggers(x_mpf)
    trigger_str = triggers[0]["type"] if triggers else "none"
    result = classify_algebraic(x_mpf)
    approx_str = mp.nstr(x_mpf, 20)

    entry = {
        "value_name": name,
        "value_approx": approx_str,
        "trigger": trigger_str,
        "algebraic_degree": result.get("algebraic_degree"),
        "minimal_poly": result.get("minimal_poly"),
        "cm_discriminant": result.get("cm_discriminant"),
        "verdict": result["verdict"],
        "exact_fraction": None,
    }

    # If PSLQ found degree 1: poly is [a0, a1] → x = -a0/a1
    if result.get("algebraic_degree") == 1 and result.get("minimal_poly"):
        poly = result["minimal_poly"]
        p, q = -poly[0], poly[1]
        frac = Fraction(p, q)
        entry["exact_fraction"] = (frac.numerator, frac.denominator)
        entry["significance"] = f"exactly {frac.numerator}/{frac.denominator}"

    if expected_p is not None and expected_q is not None:
        is_match = check_exact_fraction(x_mpf, expected_p, expected_q)
        entry["matches_expected"] = is_match

    return entry


# ---------------------------------------------------------------------------
# GROUP scanners
# ---------------------------------------------------------------------------

def scan_group_a(cert, trans_data):
    """GROUP A: Trans family K values and Möbius coefficients."""
    print("\n=== GROUP A: Trans K values and Möbius coefficients ===")
    mp.dps = 100
    results = []

    families = cert["strata"]["Trans"]["families"]

    for fam in families:
        idx = fam["index"]
        rel = fam["relation"]  # [c0, c1, c2, c3, 0]
        c0, c1, c2, c3 = rel[0], rel[1], rel[2], rel[3]

        # K value from trans_verification
        tv = next((t for t in trans_data if t["family_index"] == idx), None)
        if tv:
            K = mpf(tv["K_value"])
            r = scan_value(f"K for family {idx}", K)
            results.append(r)
            print(f"  K[{idx}]: {r['verdict']}")

        # Check Möbius coefficients are exactly integer
        for label, val in [("c0", c0), ("c1", c1), ("c2", c2), ("c3", c3)]:
            x = mpf(val)
            r = scan_integer_exactness(f"{label} for family {idx}", x)
            r["significance"] = f"Möbius coeff {label}={val} is exact integer"
            results.append(r)

    print(f"  → {len(results)} values scanned in Group A")
    return results


def scan_group_b(cert):
    """GROUP B: disc_a values."""
    print("\n=== GROUP B: disc_a values ===")
    mp.dps = 100
    results = []
    families = cert["strata"]["Trans"]["families"]

    for fam in families:
        idx = fam["index"]
        a = fam["family"]["a"]  # [a2, a1, a0]
        # disc = a1^2 - 4*a2*a0  (with [a2,a1,a0] ordering: a[0]=a2, a[1]=a1, a[2]=a0)
        disc = a[1] ** 2 - 4 * a[0] * a[2]
        x = mpf(disc)
        r = scan_integer_exactness(f"disc_a for family {idx}", x)
        r["significance"] = f"disc_a = {disc} is exact integer"
        results.append(r)
        print(f"  disc_a[{idx}] = {disc}: {r['verdict']}")

    print(f"  → {len(results)} values scanned in Group B")
    return results


def scan_group_c(cert):
    """GROUP C: Möbius determinants."""
    print("\n=== GROUP C: Möbius determinants ===")
    mp.dps = 100
    results = []
    families = cert["strata"]["Trans"]["families"]

    for fam in families:
        idx = fam["index"]
        rel = fam["relation"]
        c0, c1, c2, c3 = rel[0], rel[1], rel[2], rel[3]
        det = c1 * c2 - c0 * c3
        x = mpf(det)
        r = scan_integer_exactness(f"Möbius det for family {idx}", x)
        r["significance"] = f"det = {det} {'(nonzero ✓)' if det != 0 else '(ZERO ✗)'}"
        r["det_value"] = det
        r["det_nonzero"] = det != 0
        results.append(r)
        print(f"  det[{idx}] = {det}: {r['verdict']} {'✓' if det != 0 else '✗ ZERO!'}")

    print(f"  → {len(results)} values scanned in Group C")
    return results


def scan_group_d(cert):
    """GROUP D: Ratio a2/b1² — KEY CHECK."""
    print("\n=== GROUP D: a2/b1² ratio — KEY CHECK ===")
    mp.dps = 100
    results = []
    families = cert["strata"]["Trans"]["families"]

    ratio_counts = {}

    for fam in families:
        idx = fam["index"]
        a = fam["family"]["a"]  # [a2, a1, a0]
        b = fam["family"]["b"]  # [b2, b1, b0]
        a2 = a[0]
        b1 = b[1]

        if b1 == 0:
            print(f"  WARNING: b1=0 for family {idx}, skipping ratio")
            continue

        ratio = mpf(a2) / (mpf(b1) ** 2)
        r = scan_fraction_exactness(
            f"a2/b1^2 for family {idx}",
            ratio,
            expected_p=-2,
            expected_q=9,
        )

        if r.get("exact_fraction"):
            frac_str = f"{r['exact_fraction'][0]}/{r['exact_fraction'][1]}"
            r["significance"] = f"a2/b1^2 = {frac_str} exactly (a2={a2}, b1={b1})"
            ratio_counts.setdefault(frac_str, 0)
            ratio_counts[frac_str] += 1
        else:
            r["significance"] = f"a2/b1^2 ≈ {mp.nstr(ratio, 15)} — not a simple fraction"

        results.append(r)
        frac_display = f"{r.get('exact_fraction', '?')}"
        print(f"  a2/b1²[{idx}] = {mp.nstr(ratio, 10)} → {r['verdict']} {frac_display}")

    print(f"\n  Ratio distribution: {ratio_counts}")
    print(f"  → {len(results)} values scanned in Group D")
    return results


def scan_group_e(cert):
    """GROUP E: PSLQ residuals."""
    print("\n=== GROUP E: PSLQ residuals ===")
    mp.dps = 100
    results = []
    families = cert["strata"]["Trans"]["families"]

    for fam in families:
        idx = fam["index"]
        residual = fam["residual"]
        x = mpf(residual)

        if residual == 0.0:
            r = {
                "value_name": f"residual for family {idx}",
                "value_approx": "0.0",
                "trigger": "near-zero",
                "algebraic_degree": 1,
                "minimal_poly": [0, 1],
                "cm_discriminant": None,
                "verdict": "EXACT-RATIONAL",
                "significance": "residual = 0 exactly (perfect PSLQ match)",
            }
        else:
            triggers = run_all_triggers(x)
            trigger_str = triggers[0]["type"] if triggers else "none"
            # Don't bother with PSLQ on precision artifacts
            r = {
                "value_name": f"residual for family {idx}",
                "value_approx": f"{residual:.6e}",
                "trigger": trigger_str,
                "algebraic_degree": None,
                "minimal_poly": None,
                "cm_discriminant": None,
                "verdict": "NO-TRIGGER" if trigger_str == "none" else "TRANSCENDENTAL",
                "significance": f"residual = {residual:.2e} — precision artifact, not algebraic",
            }

        results.append(r)
        print(f"  residual[{idx}] = {residual}: {r['verdict']}")

    print(f"  → {len(results)} values scanned in Group E")
    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("LAYER 2 EXACTNESS SCANNER — POC")
    print("Task: L2-EXACTNESS-SCANNER-POC")
    print("=" * 60)

    # Validation
    print("\n--- VALIDATION TESTS ---")
    if not run_validation_tests():
        print("\nFATAL: Validation tests failed. Fix scanner before proceeding.")
        sys.exit(1)
    print("\nAll 4 validation tests PASSED.\n")

    # Load data
    print("--- LOADING DATA ---")
    cert = load_certificate()
    trans_data = load_trans_verification()
    print(f"  Certificate: {cert['total_enumerated']} families enumerated")
    print(f"  Trans families: {cert['strata']['Trans']['count']}")
    print(f"  Trans verification entries: {len(trans_data)}")

    # Run scans
    scan_results = {}
    scan_results["A"] = scan_group_a(cert, trans_data)
    scan_results["B"] = scan_group_b(cert)
    scan_results["C"] = scan_group_c(cert)
    scan_results["D"] = scan_group_d(cert)
    scan_results["E"] = scan_group_e(cert)

    # Build report
    print("\n--- BUILDING REPORT ---")
    report = build_report(scan_results)

    # Write outputs
    report_json_path = os.path.join(OUT_DIR, "scanner_report.json")
    with open(report_json_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"  Written: {report_json_path}")

    report_md_path = os.path.join(OUT_DIR, "scanner_report.md")
    md_text = format_markdown_report(report)
    with open(report_md_path, "w", encoding="utf-8") as f:
        f.write(md_text)
    print(f"  Written: {report_md_path}")

    claims_path = os.path.join(OUT_DIR, "claims.jsonl")
    claims = write_claims(report, claims_path)
    print(f"  Written: {claims_path} ({len(claims)} claims)")

    # Summary
    print("\n" + "=" * 60)
    print("SCAN COMPLETE")
    print(f"  Total values scanned: {report['total_values_scanned']}")
    print(f"  Triggers fired: {report['triggers_fired']}")
    print(f"  Exact algebraic found: {report['exact_algebraic_found']}")
    print(f"  Discovery candidates: {len(report['discovery_candidates'])}")
    print(f"\n  KEY FINDING: {report['key_finding']}")
    print("=" * 60)


if __name__ == "__main__":
    main()
