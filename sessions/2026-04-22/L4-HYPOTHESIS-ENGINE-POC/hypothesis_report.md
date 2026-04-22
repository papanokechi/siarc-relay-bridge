# PCF Hypothesis Engine — Layer 4 Report

**Generated:** 2026-04-22 19:13
**Input:** enrichment_report.json from Layer 3 correlator
**Families:** 114,820
**Strata:** {'Trans': 24, 'Des': 500, 'Rat': 114296}

---

## Summary

| Metric | Count |
|--------|-------|
| Total hypotheses | 16 |
| HIGH priority | 8 |
| MEDIUM priority | 7 |
| LOW priority | 1 |
| IMPLICATION type | 4 |
| ASSOCIATION type | 12 |
| THRESHOLD type | 0 |

---

## HIGH Priority Hypotheses (Proof Candidates)

### H001: sign_disc_a=-1 exclusively in Des

- **Type:** IMPLICATION
- **Claim:** disc_a < 0 implies not structural Rat in F(2,4)
- **Mechanism:** disc_a < 0 means a(n) has no real roots, hence no non-negative integer root k with a(k)=0, hence not structural Rat
- **Enrichment ratio:** 9999.0
- **p-value:** 7.148987864706689e-53
- **Falsification:** Enumerate all convergent F(2,4) families; find any with sign_disc_a=-1 NOT in Des
- **If true:** 0 violations across all convergent families
- **If false:** At least 1 family with sign_disc_a=-1 outside Des
- **Script:** `scripts/verify_H001_sign_disc_a.py`

### H002: degree_profile=(1,1) in Rat

- **Type:** IMPLICATION
- **Claim:** degree_profile=(1,1) implies membership in Rat within F(2,4)
- **Mechanism:** Linear a(n) and linear b(n) produce a Gauss-type CF that always converges to a rational value
- **Enrichment ratio:** 9999.0
- **p-value:** 0.000820961077384568
- **Falsification:** Enumerate all convergent F(2,4) families; find any with degree_profile=(1,1) NOT in Rat
- **If true:** 0 violations across all convergent families
- **If false:** At least 1 family with degree_profile=(1,1) outside Rat
- **Script:** `scripts/verify_H002_degree_profile.py`

### H003: a0_is_zero=True in Rat

- **Type:** IMPLICATION
- **Claim:** a0_is_zero=True implies membership in Rat within F(2,4)
- **Mechanism:** a(0)=0 means n=0 is a root of a(n), so a(0)=0 forces the PCF numerator to vanish at n=0, producing a finite continued fraction (structural Rat)
- **Enrichment ratio:** 9999.0
- **p-value:** 2.8141359216879025e-165
- **Falsification:** Enumerate all convergent F(2,4) families; find any with a0_is_zero=True NOT in Rat
- **If true:** 0 violations across all convergent families
- **If false:** At least 1 family with a0_is_zero=True outside Rat
- **Script:** `scripts/verify_H003_a0_is_zero.py`

### H004: a_eval_1_is_zero=True in Rat

- **Type:** IMPLICATION
- **Claim:** a_eval_1_is_zero=True implies membership in Rat within F(2,4)
- **Mechanism:** a(1)=a2+a1+a0=0 means the PCF numerator vanishes at n=1, forcing finite termination (structural Rat)
- **Enrichment ratio:** 9999.0
- **p-value:** 2.8192151658642463e-112
- **Falsification:** Enumerate all convergent F(2,4) families; find any with a_eval_1_is_zero=True NOT in Rat
- **If true:** 0 violations across all convergent families
- **If false:** At least 1 family with a_eval_1_is_zero=True outside Rat
- **Script:** `scripts/verify_H004_a_eval_1_is_zero.py`

### H005: b_degree=1 in Trans

- **Type:** ASSOCIATION
- **Claim:** b_degree=1 is strongly associated with Trans (ratio=10.1×, p=7.78e-25)
- **Mechanism:** OPEN
- **Enrichment ratio:** 10.1151
- **p-value:** 7.781748742044763e-25
- **Falsification:** Recompute enrichment ratio on full F(2,4) enumeration; confirm ratio > 5
- **If true:** Enrichment ratio ≥ 10.1 on full enumeration
- **If false:** Enrichment ratio < 3 on full enumeration
- **Script:** `scripts/verify_H005_b_degree.py`

### H006: degree_profile=(2,1) in Trans

- **Type:** ASSOCIATION
- **Claim:** degree_profile=(2,1) is strongly associated with Trans (ratio=12.0×, p=1.24e-26)
- **Mechanism:** OPEN
- **Enrichment ratio:** 12.0218
- **p-value:** 1.2394955291531704e-26
- **Falsification:** Recompute enrichment ratio on full F(2,4) enumeration; confirm ratio > 5
- **If true:** Enrichment ratio ≥ 12.0 on full enumeration
- **If false:** Enrichment ratio < 3 on full enumeration
- **Script:** `scripts/verify_H006_degree_profile.py`

### H007: sign_b2=0 in Trans

- **Type:** ASSOCIATION
- **Claim:** sign_b2=0 is strongly associated with Trans (ratio=9.1×, p=9.75e-24)
- **Mechanism:** OPEN
- **Enrichment ratio:** 9.1028
- **p-value:** 9.748465280606756e-24
- **Falsification:** Recompute enrichment ratio on full F(2,4) enumeration; confirm ratio > 5
- **If true:** Enrichment ratio ≥ 9.1 on full enumeration
- **If false:** Enrichment ratio < 3 on full enumeration
- **Script:** `scripts/verify_H007_sign_b2.py`

### H008: b2_is_zero=True in Trans

- **Type:** ASSOCIATION
- **Claim:** b2_is_zero=True is strongly associated with Trans (ratio=9.1×, p=9.75e-24)
- **Mechanism:** OPEN
- **Enrichment ratio:** 9.1028
- **p-value:** 9.748465280606756e-24
- **Falsification:** Recompute enrichment ratio on full F(2,4) enumeration; confirm ratio > 5
- **If true:** Enrichment ratio ≥ 9.1 on full enumeration
- **If false:** Enrichment ratio < 3 on full enumeration
- **Script:** `scripts/verify_H008_b2_is_zero.py`

## MEDIUM Priority Hypotheses (Statistical Associations)

### H009: a_degree=1 in Rat

- **Type:** ASSOCIATION
- **Claim:** a_degree=1 is strongly associated with Rat (ratio=16.0×, p=3.33e-30)
- **Enrichment ratio:** 16.0204
- **p-value:** 3.3333057875081194e-30

### H010: degree_profile=(1,2) in Rat

- **Type:** ASSOCIATION
- **Claim:** degree_profile=(1,2) is strongly associated with Rat (ratio=14.3×, p=4.80e-26)
- **Enrichment ratio:** 14.2599
- **p-value:** 4.796476035489946e-26

### H011: sign_a2=0 in Rat

- **Type:** ASSOCIATION
- **Claim:** sign_a2=0 is strongly associated with Rat (ratio=13.9×, p=9.84e-31)
- **Enrichment ratio:** 13.9066
- **p-value:** 9.835568803909872e-31

### H012: sign_a2=1 in Rat

- **Type:** ASSOCIATION
- **Claim:** sign_a2=1 is strongly associated with Rat (ratio=9.2×, p=2.49e-86)
- **Enrichment ratio:** 9.1783
- **p-value:** 2.4918166910602896e-86

### H013: a1_is_zero=True in Rat

- **Type:** ASSOCIATION
- **Claim:** a1_is_zero=True is strongly associated with Rat (ratio=10.6×, p=1.95e-21)
- **Enrichment ratio:** 10.569
- **p-value:** 1.945047946349875e-21

### H014: a2_is_zero=True in Rat

- **Type:** ASSOCIATION
- **Claim:** a2_is_zero=True is strongly associated with Rat (ratio=13.9×, p=9.84e-31)
- **Enrichment ratio:** 13.9066
- **p-value:** 9.835568803909872e-31

### H015: sign_disc_a=0 in Rat

- **Type:** ASSOCIATION
- **Claim:** sign_disc_a=0 is strongly associated with Rat (ratio=8.3×, p=1.55e-15)
- **Enrichment ratio:** 8.3439
- **p-value:** 1.5487117107480669e-15

## LOW Priority Hypotheses

### H016: sign_a2_b2=0 in Trans

- **Type:** ASSOCIATION
- **Claim:** sign_a2_b2=0 is strongly associated with Trans (ratio=4.0×, p=3.95e-15)
- **Enrichment ratio:** 3.9836

---

## Mathematical Agenda

### Immediate (provable from certificate data)

1. **H001 — disc_a < 0 → Desert:** The discriminant of `a(n)` being negative means `a(n)` has no real roots, hence no non-negative integer root where `a(k)=0`. Without such a root, the PCF cannot terminate finitely, ruling out structural rationality. This is a clean implication provable by exhaustive check over F(2,4).

2. **a(0)=0 → Rat:** If the constant term of `a(n)` is zero, then `a(0)=0`, and the PCF numerator vanishes at `n=0`, forcing a finite continued fraction. All 58,968 such families are Rat.

3. **a(1)=0 → Rat:** If `a2+a1+a0=0`, the PCF terminates at `n=1`. All 44,408 such families are Rat.

### Medium-term (require deeper analysis)

4. **Trans requires degree profile (2,1):** All 24 Trans families have quadratic `a(n)` and linear `b(n)`. Is this a theorem of the arithmetic theory of PCFs, or an artifact of the small coefficient range?

5. **Trans requires b2=0:** All Trans families have `b(n)` with leading coefficient zero (effectively linear). Combined with the degree profile, this constrains `b(n)` to be exactly linear.

### Open questions

6. Why is `sign_a2=-1` enriched 2.17× in Trans (22 of 24)? Is there a structural reason negative leading coefficient in `a(n)` favors transcendental limits?

7. The `sign_a2_b2=0` signal (all 24 Trans) — is this just a restatement of `b2=0` combined with `a2≠0`, or does it carry independent information?
