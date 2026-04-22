# PCF Cross-Family Correlator — SIARC v2.0 Layer 3 POC

## Overview

Standalone cross-family correlator that takes classified PCF families from the
F1-BASE-d2D4 certificate and produces an enrichment table showing which
structural parameters are over/under-represented in each stratum compared to
the full-space prior.

## Directory Structure

```
pcf-correlator/
  correlator.py      # main entry point
  parameters.py      # parameter extractor (Groups A-F, 21 parameters)
  enrichment.py      # statistical analysis (Fisher exact, z-score)
  report.py          # output formatter (markdown + JSON)
  test_data.py       # minimal synthetic test fixture
  input.json         # copy of f1_base_certificate.json
  desert_certificate.json  # desert family sample
  enrichment_report.md     # output: human-readable report
  enrichment_report.json   # output: machine-readable report
  README.md
```

## Usage

```bash
# Full run on certificate data
python correlator.py input.json

# Test mode with synthetic data
python correlator.py --test
```

## Dependencies

- Python 3.8+
- scipy (Fisher exact test)
- Standard library: json, itertools, collections, math, os, sys, time, random

No dependencies on existing pipeline files (f1_base_computation.py etc.).

## Input Format

Reads `f1_base_certificate.json` format. Coefficient arrays use
`[a2, a1, a0]` ordering (leading coefficient first):
- `a(n) = a2*n^2 + a1*n + a0`
- `b(n) = b2*n^2 + b1*n + b0`

The correlator reconstructs a flat family list from the certificate's
stratified sections:
- **Trans**: 24 families (explicit in certificate)
- **Rat**: 200 sampled structural Rat (enumerated from coefficient space)
- **Des**: 500 families (50 from desert certificate + 450 supplemented)

## Parameters Extracted

| Group | ID | Parameter | Type |
|-------|----|-----------|------|
| A | P01-P03 | a_degree, b_degree, degree_profile | Categorical |
| B | P04-P06 | sign(a2), sign(b2), sign(a2)*sign(b2) | Categorical |
| C | P07-P12 | a0/a1/a2/b0/b1/b2 _is_zero | Categorical |
| D | P13-P15 | a2/b1^2, a1/b1, a0/b0 ratios | Continuous |
| E | P16-P19 | disc_a, disc_b, sign(disc_a), sign(disc_b) | Mixed |
| F | P20-P21 | a_eval_1, a_eval_1_is_zero | Mixed |

## Enrichment Method

For categorical parameters: Fisher exact test on 2x2 contingency tables.
- **Discovery candidate**: enrichment > 5.0 AND p < 0.001
- **Strong signal**: enrichment > 3.0 AND p < 0.01

For continuous parameters: z-score deviation from full-space mean.
- Flagged if stratum mean deviates > 2σ from global mean.

## Validation — Known Structural Results

The correlator successfully rediscovers all three known enrichment patterns:

### 1. b2_is_zero enriched in Trans ✓

```
b2_is_zero=True: 7.7x enriched in Trans (p < 1e-10)
Count: 24/24 Trans families vs 94/724 overall
```

All 24 Trans families have b2=0 (linear b-polynomial). This is the
signature structural constraint of the Trans stratum in the d2D4 search.

### 2. a_eval_1_is_zero enriched in Rat ✓

```
a_eval_1_is_zero=True: 3.6x enriched in Rat (p < 1e-10)
Count: 72/200 Rat families vs 72/724 overall
```

When a(1)=0, the continued fraction terminates at n=1, forcing a
rational value. This is the trivial-zero mechanism.

### 3. degree_profile (2,1) enriched in Trans ✓

```
degree_profile=(2,1): 8.5x enriched in Trans (p < 1e-10)
Count: 24/24 Trans families vs 85/724 overall
```

All Trans families have quadratic a(n) and linear b(n), confirming
the degree-(2,1) structural requirement.

## Results Summary

| Category | Count |
|----------|-------|
| Discovery candidates (enrichment > 5, p < 0.001) | 5 |
| Strong signals (enrichment 3-5, p < 0.01) | 3 |
| Null-result parameters | 0 |
| Total families analyzed | 724 |
| Runtime | < 1 second |

## POC Scope Limits

- Desert sample: 500 families (50 from certificate + 450 supplemented)
- Rat sample: 200 structural Rat families
- No visualization (text output only)
- No parameters beyond Groups A-F
- Runtime: ~0.5s (well under 60s target)
