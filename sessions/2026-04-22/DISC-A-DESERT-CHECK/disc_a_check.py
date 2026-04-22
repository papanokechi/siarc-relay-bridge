#!/usr/bin/env python3
"""
DISC-A-DESERT-CHECK — Check whether disc_a < 0 implies Desert in F(2,4).

Enumerates all F(2,4) families, classifies structurally, and computes
the discriminant distribution across strata.
"""

import itertools
import json
from datetime import datetime, timezone

COEFF_RANGE = range(-4, 5)
MAX_K = 100  # check a(k)=0 for k in 0..MAX_K


def is_structural_rat(a2, a1, a0):
    """True if a(k) = a2*k^2 + a1*k + a0 = 0 for some k in [0, MAX_K]."""
    for k in range(0, MAX_K + 1):
        if a2 * k * k + a1 * k + a0 == 0:
            return True
    return False


def main():
    # Load certificate for Trans families and cross-check
    with open('f1_base_certificate.json', 'r') as f:
        cert = json.load(f)

    trans_families = cert['strata']['Trans']['families']
    trans_set = set()
    for entry in trans_families:
        fam = entry['family']
        trans_set.add((tuple(fam['a']), tuple(fam['b'])))

    # Cross-check Trans: all should have disc_a >= 0
    trans_violations = 0
    for entry in trans_families:
        a = entry['family']['a']  # [a2, a1, a0]
        disc_a = a[1] ** 2 - 4 * a[0] * a[2]
        if disc_a < 0:
            trans_violations += 1
            print(f"  TRANS VIOLATION: a={a} disc_a={disc_a}")

    print(f"Trans violations: {trans_violations} / {len(trans_families)}")

    # Enumerate all F(2,4) families
    n_desert_total = 0
    n_disc_neg = 0
    n_disc_zero = 0
    n_disc_pos = 0
    rat_count = 0
    rat_violations = 0

    for a2, a1, a0 in itertools.product(COEFF_RANGE, repeat=3):
        disc_a = a1 * a1 - 4 * a2 * a0
        rat = is_structural_rat(a2, a1, a0)

        for b2, b1, b0 in itertools.product(COEFF_RANGE, repeat=3):
            if b0 == 0 and b1 == 0 and b2 == 0:
                continue

            key = ((a2, a1, a0), (b2, b1, b0))
            is_trans = key in trans_set

            if rat and not is_trans:
                # Structural Rat
                rat_count += 1
                if disc_a < 0:
                    rat_violations += 1
            elif is_trans:
                pass  # already checked above
            else:
                # Desert (non-Rat, non-Trans, and we treat all
                # non-structural as Desert for this check)
                n_desert_total += 1
                if disc_a < 0:
                    n_disc_neg += 1
                elif disc_a == 0:
                    n_disc_zero += 1
                else:
                    n_disc_pos += 1

    fraction_neg = n_disc_neg / n_desert_total if n_desert_total > 0 else 0
    theorem_candidate = (
        fraction_neg > 0.01
        and rat_violations == 0
        and trans_violations == 0
    )

    theorem_statement = None
    if theorem_candidate:
        theorem_statement = (
            f"disc_a < 0 implies Desert in F(2,4): verified for "
            f"{n_disc_neg} families, zero counterexamples in Rat or Trans."
        )

    result = {
        "task_id": "DISC-A-DESERT-CHECK",
        "date": datetime.now(timezone.utc).isoformat(),
        "n_desert_total": n_desert_total,
        "n_disc_neg": n_disc_neg,
        "n_disc_zero": n_disc_zero,
        "n_disc_pos": n_disc_pos,
        "fraction_neg": round(fraction_neg, 6),
        "rat_count": rat_count,
        "rat_violations": rat_violations,
        "trans_violations": trans_violations,
        "theorem_candidate": theorem_candidate,
        "theorem_statement": theorem_statement,
    }

    print(f"\nDesert total: {n_desert_total}")
    print(f"  disc_a < 0: {n_disc_neg} ({fraction_neg:.4%})")
    print(f"  disc_a = 0: {n_disc_zero}")
    print(f"  disc_a > 0: {n_disc_pos}")
    print(f"Rat count: {rat_count}, violations: {rat_violations}")
    print(f"Theorem candidate: {theorem_candidate}")
    if theorem_statement:
        print(f"  {theorem_statement}")

    with open('disc_a_check.json', 'w') as f:
        json.dump(result, f, indent=2)
    print("\nWrote disc_a_check.json")


if __name__ == '__main__':
    main()
