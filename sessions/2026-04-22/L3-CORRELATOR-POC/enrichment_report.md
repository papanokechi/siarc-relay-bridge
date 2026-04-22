# PCF Cross-Family Correlator — Enrichment Report

## Summary

- **Strata**: Des (500), Rat (200), Trans (24)
- **Total families**: 724
- **Parameters extracted**: 21 (Groups A-F)
- **Categorical parameters**: 15
- **Continuous parameters**: 6
- **Discovery candidates**: 5
- **Strong signals**: 3
- **Null-result parameters**: 0

## Discovery Candidates (enrichment > 5, p < 0.001)

### degree_profile = (2,1) in Trans

| Metric | Value |
|--------|-------|
| Enrichment ratio | 8.52 |
| p-value | <1e-10 |
| Count in stratum | 24 / 24 |
| Count in full space | 85 / 724 |

**Interpretation**: degree_profile=(2,1) is 8.5x enriched in Trans vs full space (p=<1e-10): Trans families prefer this (a_deg, b_deg) combination.

### b_degree = 1 in Trans

| Metric | Value |
|--------|-------|
| Enrichment ratio | 8.42 |
| p-value | <1e-10 |
| Count in stratum | 24 / 24 |
| Count in full space | 86 / 724 |

**Interpretation**: b_degree=1 is 8.4x enriched in Trans vs full space (p=<1e-10).

### sign_b2 = 0 in Trans

| Metric | Value |
|--------|-------|
| Enrichment ratio | 7.70 |
| p-value | <1e-10 |
| Count in stratum | 24 / 24 |
| Count in full space | 94 / 724 |

**Interpretation**: sign_b2=0 is 7.7x enriched in Trans vs full space (p=<1e-10).

### b2_is_zero = True in Trans

| Metric | Value |
|--------|-------|
| Enrichment ratio | 7.70 |
| p-value | <1e-10 |
| Count in stratum | 24 / 24 |
| Count in full space | 94 / 724 |

**Interpretation**: b2_is_zero=True is 7.7x enriched in Trans vs full space (p=<1e-10): Trans families are strongly concentrated in degree-(a,<=1) b-profiles (linear or constant b).

### sign_a2_b2 = 0 in Trans

| Metric | Value |
|--------|-------|
| Enrichment ratio | 5.79 |
| p-value | <1e-10 |
| Count in stratum | 24 / 24 |
| Count in full space | 125 / 724 |

**Interpretation**: sign_a2_b2=0 is 5.8x enriched in Trans vs full space (p=<1e-10).

## Strong Signals (enrichment 3-5, p < 0.01)

### a0_is_zero = True in Rat

| Metric | Value |
|--------|-------|
| Enrichment ratio | 3.62 |
| p-value | <1e-10 |
| Count in stratum | 111 / 200 |
| Count in full space | 111 / 724 |

**Interpretation**: a0_is_zero=True is 3.6x enriched in Rat vs full space (p=<1e-10).

### a_eval_1_is_zero = True in Rat

| Metric | Value |
|--------|-------|
| Enrichment ratio | 3.62 |
| p-value | <1e-10 |
| Count in stratum | 72 / 200 |
| Count in full space | 72 / 724 |

**Interpretation**: a_eval_1_is_zero=True is 3.6x enriched in Rat vs full space (p=<1e-10): a(1)=0 causes the CF to terminate, yielding rational values (trivial-zero mechanism).

### a_degree = 1 in Rat

| Metric | Value |
|--------|-------|
| Enrichment ratio | 3.02 |
| p-value | 1.2e-10 |
| Count in stratum | 25 / 200 |
| Count in full space | 30 / 724 |

**Interpretation**: a_degree=1 is 3.0x enriched in Rat vs full space (p=1.2e-10).

## Full Enrichment Table

| Parameter | Stratum | Value | Count (S) | Count (all) | Enrichment | p-value |
|-----------|---------|-------|-----------|-------------|------------|---------|
| a0_is_zero | Des | False | 500/500 | 613/724 | 1.18 | <1e-10 |
| a0_is_zero | Des | True | 0/500 | 111/724 | 0.00 | <1e-10 |
| a0_is_zero | Rat | False | 89/200 | 613/724 | 0.53 | <1e-10 |
| a0_is_zero | Rat | True | 111/200 | 111/724 | 3.62 | <1e-10 |
| a0_is_zero | Trans | False | 24/24 | 613/724 | 1.18 | 0.0377 |
| a0_is_zero | Trans | True | 0/24 | 111/724 | 0.00 | 0.0377 |
| a1_is_zero | Des | False | 494/500 | 692/724 | 1.03 | 2.6e-09 |
| a1_is_zero | Des | True | 6/500 | 32/724 | 0.27 | 2.6e-09 |
| a1_is_zero | Rat | False | 174/200 | 692/724 | 0.91 | 1.5e-10 |
| a1_is_zero | Rat | True | 26/200 | 32/724 | 2.94 | 1.5e-10 |
| a1_is_zero | Trans | False | 24/24 | 692/724 | 1.05 | 0.6190 |
| a1_is_zero | Trans | True | 0/24 | 32/724 | 0.00 | 0.6190 |
| a2_is_zero | Des | False | 494/500 | 692/724 | 1.03 | 2.6e-09 |
| a2_is_zero | Des | True | 6/500 | 32/724 | 0.27 | 2.6e-09 |
| a2_is_zero | Rat | False | 174/200 | 692/724 | 0.91 | 1.5e-10 |
| a2_is_zero | Rat | True | 26/200 | 32/724 | 2.94 | 1.5e-10 |
| a2_is_zero | Trans | False | 24/24 | 692/724 | 1.05 | 0.6190 |
| a2_is_zero | Trans | True | 0/24 | 32/724 | 0.00 | 0.6190 |
| a_degree | Des | 0 | 1/500 | 2/724 | 0.72 | 0.5234 |
| a_degree | Des | 1 | 5/500 | 30/724 | 0.24 | 2.0e-09 |
| a_degree | Des | 2 | 494/500 | 692/724 | 1.03 | 2.6e-09 |
| a_degree | Rat | 0 | 1/200 | 2/724 | 1.81 | 0.4765 |
| a_degree | Rat | 1 | 25/200 | 30/724 | 3.02 | 1.2e-10 |
| a_degree | Rat | 2 | 174/200 | 692/724 | 0.91 | 1.5e-10 |
| a_degree | Trans | 0 | 0/24 | 2/724 | 0.00 | 1.0000 |
| a_degree | Trans | 1 | 0/24 | 30/724 | 0.00 | 0.6179 |
| a_degree | Trans | 2 | 24/24 | 692/724 | 1.05 | 0.6190 |
| a_eval_1_is_zero | Des | False | 500/500 | 652/724 | 1.11 | <1e-10 |
| a_eval_1_is_zero | Des | True | 0/500 | 72/724 | 0.00 | <1e-10 |
| a_eval_1_is_zero | Rat | False | 128/200 | 652/724 | 0.71 | <1e-10 |
| a_eval_1_is_zero | Rat | True | 72/200 | 72/724 | 3.62 | <1e-10 |
| a_eval_1_is_zero | Trans | False | 24/24 | 652/724 | 1.11 | 0.1576 |
| a_eval_1_is_zero | Trans | True | 0/24 | 72/724 | 0.00 | 0.1576 |
| b0_is_zero | Des | False | 444/500 | 642/724 | 1.00 | 0.8993 |
| b0_is_zero | Des | True | 56/500 | 82/724 | 0.99 | 0.8993 |
| b0_is_zero | Rat | False | 176/200 | 642/724 | 0.99 | 0.6964 |
| b0_is_zero | Rat | True | 24/200 | 82/724 | 1.06 | 0.6964 |
| b0_is_zero | Trans | False | 22/24 | 642/724 | 1.03 | 1.0000 |
| b0_is_zero | Trans | True | 2/24 | 82/724 | 0.74 | 1.0000 |
| b1_is_zero | Des | False | 440/500 | 639/724 | 1.00 | 0.8035 |
| b1_is_zero | Des | True | 60/500 | 85/724 | 1.02 | 0.8035 |
| b1_is_zero | Rat | False | 175/200 | 639/724 | 0.99 | 0.6995 |
| b1_is_zero | Rat | True | 25/200 | 85/724 | 1.06 | 0.6995 |
| b1_is_zero | Trans | False | 24/24 | 639/724 | 1.13 | 0.0990 |
| b1_is_zero | Trans | True | 0/24 | 85/724 | 0.00 | 0.0990 |
| b2_is_zero | Des | False | 449/500 | 630/724 | 1.03 | 0.0012 |
| b2_is_zero | Des | True | 51/500 | 94/724 | 0.79 | 0.0012 |
| b2_is_zero | Rat | False | 181/200 | 630/724 | 1.04 | 0.1073 |
| b2_is_zero | Rat | True | 19/200 | 94/724 | 0.73 | 0.1073 |
| b2_is_zero | Trans | False | 0/24 | 630/724 | 0.00 | <1e-10 |
| b2_is_zero | Trans | True | 24/24 | 94/724 | 7.70 | <1e-10 |
| b_degree | Des | 0 | 6/500 | 8/724 | 1.09 | 1.0000 |
| b_degree | Des | 1 | 45/500 | 86/724 | 0.76 | 7.0e-04 |
| b_degree | Des | 2 | 449/500 | 630/724 | 1.03 | 0.0012 |
| b_degree | Rat | 0 | 2/200 | 8/724 | 0.91 | 1.0000 |
| b_degree | Rat | 1 | 17/200 | 86/724 | 0.72 | 0.0948 |
| b_degree | Rat | 2 | 181/200 | 630/724 | 1.04 | 0.1073 |
| b_degree | Trans | 0 | 0/24 | 8/724 | 0.00 | 1.0000 |
| b_degree | Trans | 1 | 24/24 | 86/724 | 8.42 | <1e-10 |
| b_degree | Trans | 2 | 0/24 | 630/724 | 0.00 | <1e-10 |
| degree_profile | Des | (0,2) | 1/500 | 2/724 | 0.72 | 0.5234 |
| degree_profile | Des | (1,1) | 0/500 | 1/724 | 0.00 | 0.3094 |
| degree_profile | Des | (1,2) | 5/500 | 29/724 | 0.25 | 5.8e-09 |
| degree_profile | Des | (2,0) | 6/500 | 8/724 | 1.09 | 1.0000 |
| degree_profile | Des | (2,1) | 45/500 | 85/724 | 0.77 | 0.0011 |
| degree_profile | Des | (2,2) | 443/500 | 599/724 | 1.07 | 2.3e-09 |
| degree_profile | Rat | (0,2) | 1/200 | 2/724 | 1.81 | 0.4765 |
| degree_profile | Rat | (1,1) | 1/200 | 1/724 | 3.62 | 0.2762 |
| degree_profile | Rat | (1,2) | 24/200 | 29/724 | 3.00 | 4.1e-10 |
| degree_profile | Rat | (2,0) | 2/200 | 8/724 | 0.91 | 1.0000 |
| degree_profile | Rat | (2,1) | 16/200 | 85/724 | 0.68 | 0.0538 |
| degree_profile | Rat | (2,2) | 156/200 | 599/724 | 0.94 | 0.0473 |
| degree_profile | Trans | (0,2) | 0/24 | 2/724 | 0.00 | 1.0000 |
| degree_profile | Trans | (1,1) | 0/24 | 1/724 | 0.00 | 1.0000 |
| degree_profile | Trans | (1,2) | 0/24 | 29/724 | 0.00 | 0.6180 |
| degree_profile | Trans | (2,0) | 0/24 | 8/724 | 0.00 | 1.0000 |
| degree_profile | Trans | (2,1) | 24/24 | 85/724 | 8.52 | <1e-10 |
| degree_profile | Trans | (2,2) | 0/24 | 599/724 | 0.00 | <1e-10 |
| sign_a2 | Des | -1 | 472/500 | 583/724 | 1.17 | <1e-10 |
| sign_a2 | Des | 0 | 6/500 | 32/724 | 0.27 | 2.6e-09 |
| sign_a2 | Des | 1 | 22/500 | 109/724 | 0.29 | <1e-10 |
| sign_a2 | Rat | -1 | 89/200 | 583/724 | 0.55 | <1e-10 |
| sign_a2 | Rat | 0 | 26/200 | 32/724 | 2.94 | 1.5e-10 |
| sign_a2 | Rat | 1 | 85/200 | 109/724 | 2.82 | <1e-10 |
| sign_a2 | Trans | -1 | 22/24 | 583/724 | 1.14 | 0.1976 |
| sign_a2 | Trans | 0 | 0/24 | 32/724 | 0.00 | 0.6190 |
| sign_a2 | Trans | 1 | 2/24 | 109/724 | 0.55 | 0.5602 |
| sign_a2_b2 | Des | -1 | 216/500 | 302/724 | 1.04 | 0.2537 |
| sign_a2_b2 | Des | 0 | 57/500 | 125/724 | 0.66 | 2.3e-09 |
| sign_a2_b2 | Des | 1 | 227/500 | 297/724 | 1.11 | 3.3e-04 |
| sign_a2_b2 | Rat | -1 | 86/200 | 302/724 | 1.03 | 0.6742 |
| sign_a2_b2 | Rat | 0 | 44/200 | 125/724 | 1.27 | 0.0473 |
| sign_a2_b2 | Rat | 1 | 70/200 | 297/724 | 0.85 | 0.0430 |
| sign_a2_b2 | Trans | -1 | 0/24 | 302/724 | 0.00 | 2.1e-06 |
| sign_a2_b2 | Trans | 0 | 24/24 | 125/724 | 5.79 | <1e-10 |
| sign_a2_b2 | Trans | 1 | 0/24 | 297/724 | 0.00 | 4.8e-06 |
| sign_b2 | Des | -1 | 235/500 | 337/724 | 1.01 | 0.7474 |
| sign_b2 | Des | 0 | 51/500 | 94/724 | 0.79 | 0.0012 |
| sign_b2 | Des | 1 | 214/500 | 293/724 | 1.06 | 0.0599 |
| sign_b2 | Rat | -1 | 102/200 | 337/724 | 1.10 | 0.1566 |
| sign_b2 | Rat | 0 | 19/200 | 94/724 | 0.73 | 0.1073 |
| sign_b2 | Rat | 1 | 79/200 | 293/724 | 0.98 | 0.7996 |
| sign_b2 | Trans | -1 | 0/24 | 337/724 | 0.00 | 4.2e-07 |
| sign_b2 | Trans | 0 | 24/24 | 94/724 | 7.70 | <1e-10 |
| sign_b2 | Trans | 1 | 0/24 | 293/724 | 0.00 | 4.8e-06 |
| sign_disc_a | Des | -1 | 22/500 | 22/724 | 1.45 | 5.4e-04 |
| sign_disc_a | Des | 0 | 4/500 | 26/724 | 0.22 | 1.2e-08 |
| sign_disc_a | Des | 1 | 474/500 | 676/724 | 1.02 | 0.0241 |
| sign_disc_a | Rat | -1 | 0/200 | 22/724 | 0.00 | 0.0011 |
| sign_disc_a | Rat | 0 | 20/200 | 26/724 | 2.78 | 1.4e-07 |
| sign_disc_a | Rat | 1 | 180/200 | 676/724 | 0.96 | 0.0297 |
| sign_disc_a | Trans | -1 | 0/24 | 22/724 | 0.00 | 1.0000 |
| sign_disc_a | Trans | 0 | 2/24 | 26/724 | 2.32 | 0.2115 |
| sign_disc_a | Trans | 1 | 22/24 | 676/724 | 0.98 | 0.6692 |
| sign_disc_b | Des | -1 | 164/500 | 229/724 | 1.04 | 0.3419 |
| sign_disc_b | Des | 0 | 26/500 | 34/724 | 1.11 | 0.4475 |
| sign_disc_b | Des | 1 | 310/500 | 461/724 | 0.97 | 0.1811 |
| sign_disc_b | Rat | -1 | 65/200 | 229/724 | 1.03 | 0.7888 |
| sign_disc_b | Rat | 0 | 8/200 | 34/724 | 0.85 | 0.6964 |
| sign_disc_b | Rat | 1 | 127/200 | 461/724 | 1.00 | 1.0000 |
| sign_disc_b | Trans | -1 | 0/24 | 229/724 | 0.00 | 1.6e-04 |
| sign_disc_b | Trans | 0 | 0/24 | 34/724 | 0.00 | 0.6217 |
| sign_disc_b | Trans | 1 | 24/24 | 461/724 | 1.57 | 3.2e-05 |

## Continuous Parameter Summary

| Parameter | Stratum | n | Mean | Std | Min | Max | Global Mean | Deviation (σ) | Flagged |
|-----------|---------|---|------|-----|-----|-----|-------------|---------------|---------|
| a0_over_b0 | Des | 444 | -0.0274 | 1.2692 | -4.0 | 4.0 | -0.0337 | 0.01 | no |
| a0_over_b0 | Rat | 176 | -0.0540 | 1.0989 | -4.0 | 4.0 | -0.0337 | 0.02 | no |
| a0_over_b0 | Trans | 22 | 0.0000 | 1.1323 | -3.0 | 3.0 | -0.0337 | 0.03 | no |
| a1_over_b1 | Des | 440 | 0.2121 | 2.3645 | -4.0 | 4.0 | 0.1166 | 0.04 | no |
| a1_over_b1 | Rat | 175 | -0.1076 | 1.5400 | -4.0 | 4.0 | 0.1166 | 0.11 | no |
| a1_over_b1 | Trans | 24 | 0.0000 | 0.6383 | -1.0 | 1.0 | 0.1166 | 0.05 | no |
| a2_over_b1sq | Des | 440 | -0.3582 | 0.5751 | -4.0 | 3.0 | -0.2539 | 0.12 | no |
| a2_over_b1sq | Rat | 175 | -0.0013 | 1.3226 | -4.0 | 4.0 | -0.2539 | 0.30 | no |
| a2_over_b1sq | Trans | 24 | -0.1829 | 0.1305 | -0.2222222222222222 | 0.25 | -0.2539 | 0.08 | no |
| a_eval_1 | Des | 500 | 0.9160 | 1.5248 | -10 | 10 | 0.5773 | 0.16 | no |
| a_eval_1 | Rat | 200 | -0.1600 | 2.8363 | -8 | 8 | 0.5773 | 0.35 | no |
| a_eval_1 | Trans | 24 | -0.3333 | 2.8964 | -6 | 4 | 0.5773 | 0.44 | no |
| disc_a | Des | 500 | 7.4000 | 10.6692 | -63 | 73 | 9.2486 | 0.15 | no |
| disc_a | Rat | 200 | 12.9500 | 15.6706 | 0 | 64 | 9.2486 | 0.29 | no |
| disc_a | Trans | 24 | 16.9167 | 9.9370 | 0 | 25 | 9.2486 | 0.61 | no |
| disc_b | Des | 500 | 5.9800 | 25.9496 | -64 | 80 | 6.3246 | 0.01 | no |
| disc_b | Rat | 200 | 6.9150 | 26.9603 | -55 | 80 | 6.3246 | 0.02 | no |
| disc_b | Trans | 24 | 8.5833 | 1.3819 | 4 | 9 | 6.3246 | 0.09 | no |

## Null Results

Parameters with enrichment ratio 0.8–1.2 across all strata (no differential signal):

*All parameters show some enrichment variation.*
