#!/usr/bin/env python3
# PERIOD-REP-VQUAD-003 Stage 0.2 — canonical-form check on L_V coefficients,
# in a second engine (sympy exact rationals), independent of VQUAD-002.
#
# Checks:
#  (1) the hand-transcribed L_V (from operator-verification.md) matches the parent
#      machine artifact operator_verification_results.json EXACTLY (md<->json drift);
#  (2) every coefficient pair (p,q) for p+q*sqrt3 is a reduced fraction;
#  (3) denominators are exactly {1, 431, 418501} with 418501 = 431*971 (971 prime);
#  (4) clearing to the primitive Z[sqrt3] form (x418501) gives integer coeffs whose
#      overall content (gcd of all p,q numerators) is 1 -> no common factor remains.
import json
from fractions import Fraction as F
import sympy as sp
from stage0_residual_check import LV   # reuse the hand-transcribed operator

PARENT = (r"C:\LocalWork\siarc-relay-bridge\sessions\2026-06-15"
          r"\PERIOD-REP-VQUAD-002\scripts\operator_verification_results.json")

def check_matches_parent():
    d = json.load(open(PARENT, encoding="utf-8"))
    coeffs = d["L_V_operator"]["coeffs"]   # list over k of list over i of [p,q] strings
    mism = []
    for k in range(5):
        row = coeffs[k]
        for i in range(len(row)):
            pj = F(row[i][0]); qj = F(row[i][1])
            # my hardcoded value (pad missing high-degree entries with 0)
            pm, qm = (LV[k][i] if i < len(LV[k]) else (F(0), F(0)))
            if pj != pm or qj != qm:
                mism.append((k, i, (str(pm), str(qm)), (row[i][0], row[i][1])))
    return mism

def all_reduced():
    bad = []
    for k in LV:
        for i, (p, q) in enumerate(LV[k]):
            # Fraction is always normalized; re-derive to be safe and assert gcd==1
            for name, val in (("p", p), ("q", q)):
                if val != 0:
                    g = abs(F(val.numerator, val.denominator).denominator)
                    from math import gcd
                    if gcd(abs(val.numerator), val.denominator) != 1:
                        bad.append((k, i, name, str(val)))
    return bad

def denominators():
    dens = set()
    for k in LV:
        for (p, q) in LV[k]:
            for v in (p, q):
                if v != 0:
                    dens.add(v.denominator)
                else:
                    dens.add(1)
    return sorted(dens)

def primitive_content():
    # multiply all coeffs by 418501 -> should be integers; gcd of all = content
    M = 418501
    ints = []
    for k in LV:
        for (p, q) in LV[k]:
            for v in (p, q):
                x = v * M
                assert x.denominator == 1, f"not integer after x{M}: {x}"
                ints.append(int(x))
    from math import gcd
    g = 0
    for x in ints:
        g = gcd(g, abs(x))
    return g, len(ints)

def main():
    out = {}

    mism = check_matches_parent()
    out["md_vs_json_mismatches"] = mism
    out["md_matches_parent_json"] = (len(mism) == 0)
    print("[1] md<->json match:", out["md_matches_parent_json"],
          "" if not mism else f"({len(mism)} mismatches!)")

    bad = all_reduced()
    out["unreduced_fractions"] = bad
    out["all_fractions_reduced"] = (len(bad) == 0)
    print("[2] all (p,q) reduced:", out["all_fractions_reduced"])

    dens = denominators()
    out["distinct_denominators"] = dens
    fac = sp.factorint(418501)
    out["factor_418501"] = {str(p): e for p, e in fac.items()}
    is_431x971 = (fac == {431: 1, 971: 1}) and sp.isprime(431) and sp.isprime(971)
    out["418501_eq_431x971_both_prime"] = bool(is_431x971)
    dens_ok = set(dens).issubset({1, 431, 418501})
    out["denominators_in_expected_set"] = bool(dens_ok)
    print("[3] denominators", dens, "| 418501 =", out["factor_418501"],
          "| both prime:", bool(is_431x971), "| set ok:", bool(dens_ok))

    g, ncoef = primitive_content()
    out["primitive_content_gcd"] = g
    out["n_integer_coeffs"] = ncoef
    out["primitive_no_common_factor"] = (g == 1)
    print(f"[4] primitive Z[sqrt3] content gcd = {g} over {ncoef} integers "
          f"-> no common factor: {g == 1}")

    out["verdict"] = "CANONICAL-OK" if (out["md_matches_parent_json"]
                                        and out["all_fractions_reduced"]
                                        and out["denominators_in_expected_set"]
                                        and out["418501_eq_431x971_both_prime"]
                                        and out["primitive_no_common_factor"]) else "ISSUE"
    path = (r"C:\LocalWork\siarc-relay-bridge\sessions\2026-06-15"
            r"\PERIOD-REP-VQUAD-003\scripts\stage0_canonical_results.json")
    json.dump(out, open(path, "w", encoding="utf-8"), indent=2)
    print("\n[verdict]", out["verdict"])
    print("[wrote]", path)

if __name__ == "__main__":
    main()
