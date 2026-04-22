# Exactness Scanner Report
**Task:** L2-EXACTNESS-SCANNER-POC
**Date:** 2026-04-22T11:22:08.244220+00:00

## Summary
- **Values scanned:** 216
- **Triggers fired:** 192
- **Exact algebraic found:** 176
- **Groups:** A, B, C, D, E

## Key Finding
> a2/b1^2 ratio takes exact values: -2/9: 22 families; 1/4: 2 families. Not a universal -2/9 but a small finite set of exact fractions.

## Discovery Candidates (Group D: a2/b1^2 ratios)

| Family | Value | Fraction | Verdict |
|--------|-------|----------|---------|
| a2/b1^2 for family 116433 | -0.22222222222222222222 | a2/b1^2 = -2/9 exactly (a2=-2, b1=-3) | EXACT-RATIONAL |
| a2/b1^2 for family 116447 | -0.22222222222222222222 | a2/b1^2 = -2/9 exactly (a2=-2, b1=3) | EXACT-RATIONAL |
| a2/b1^2 for family 118473 | -0.22222222222222222222 | a2/b1^2 = -2/9 exactly (a2=-2, b1=-3) | EXACT-RATIONAL |
| a2/b1^2 for family 118474 | -0.22222222222222222222 | a2/b1^2 = -2/9 exactly (a2=-2, b1=-3) | EXACT-RATIONAL |
| a2/b1^2 for family 118486 | -0.22222222222222222222 | a2/b1^2 = -2/9 exactly (a2=-2, b1=3) | EXACT-RATIONAL |
| a2/b1^2 for family 118487 | -0.22222222222222222222 | a2/b1^2 = -2/9 exactly (a2=-2, b1=3) | EXACT-RATIONAL |
| a2/b1^2 for family 130100 | -0.22222222222222222222 | a2/b1^2 = -2/9 exactly (a2=-2, b1=-3) | EXACT-RATIONAL |
| a2/b1^2 for family 130101 | -0.22222222222222222222 | a2/b1^2 = -2/9 exactly (a2=-2, b1=-3) | EXACT-RATIONAL |
| a2/b1^2 for family 130102 | -0.22222222222222222222 | a2/b1^2 = -2/9 exactly (a2=-2, b1=-3) | EXACT-RATIONAL |
| a2/b1^2 for family 130116 | -0.22222222222222222222 | a2/b1^2 = -2/9 exactly (a2=-2, b1=3) | EXACT-RATIONAL |
| a2/b1^2 for family 130117 | -0.22222222222222222222 | a2/b1^2 = -2/9 exactly (a2=-2, b1=3) | EXACT-RATIONAL |
| a2/b1^2 for family 130118 | -0.22222222222222222222 | a2/b1^2 = -2/9 exactly (a2=-2, b1=3) | EXACT-RATIONAL |
| a2/b1^2 for family 143930 | -0.22222222222222222222 | a2/b1^2 = -2/9 exactly (a2=-2, b1=-3) | EXACT-RATIONAL |
| a2/b1^2 for family 143931 | -0.22222222222222222222 | a2/b1^2 = -2/9 exactly (a2=-2, b1=-3) | EXACT-RATIONAL |
| a2/b1^2 for family 143932 | -0.22222222222222222222 | a2/b1^2 = -2/9 exactly (a2=-2, b1=-3) | EXACT-RATIONAL |
| a2/b1^2 for family 143933 | -0.22222222222222222222 | a2/b1^2 = -2/9 exactly (a2=-2, b1=-3) | EXACT-RATIONAL |
| a2/b1^2 for family 143934 | -0.22222222222222222222 | a2/b1^2 = -2/9 exactly (a2=-2, b1=-3) | EXACT-RATIONAL |
| a2/b1^2 for family 143948 | -0.22222222222222222222 | a2/b1^2 = -2/9 exactly (a2=-2, b1=3) | EXACT-RATIONAL |
| a2/b1^2 for family 143949 | -0.22222222222222222222 | a2/b1^2 = -2/9 exactly (a2=-2, b1=3) | EXACT-RATIONAL |
| a2/b1^2 for family 143950 | -0.22222222222222222222 | a2/b1^2 = -2/9 exactly (a2=-2, b1=3) | EXACT-RATIONAL |
| a2/b1^2 for family 143951 | -0.22222222222222222222 | a2/b1^2 = -2/9 exactly (a2=-2, b1=3) | EXACT-RATIONAL |
| a2/b1^2 for family 143952 | -0.22222222222222222222 | a2/b1^2 = -2/9 exactly (a2=-2, b1=3) | EXACT-RATIONAL |
| a2/b1^2 for family 321561 | 0.25 | a2/b1^2 = 1/4 exactly (a2=1, b1=-2) | EXACT-RATIONAL |
| a2/b1^2 for family 321601 | 0.25 | a2/b1^2 = 1/4 exactly (a2=1, b1=2) | EXACT-RATIONAL |

## Expected Confirmations

- **Group A:** 96 values confirmed exact (as expected)
- **Group B:** 24 values confirmed exact (as expected)
- **Group C:** 24 values confirmed exact (as expected)
- **Group E:** 8 values confirmed exact (as expected)

## Null Results

- **Group A:** 24 values showed no trigger (expected transcendental) (n=120)
- **Group E:** 16 values are transcendental as expected (n=24)
