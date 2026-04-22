# PCF Exactness Scanner (Layer 2 POC)

## Overview
Layer 2 of the SIARC pipeline: watches numerical output for near-exact algebraic
relationships that would otherwise scroll past unnoticed.

## Usage
```bash
python scanner.py
```

## What it does
For any numerical value x at high precision:
1. **Trigger check** — near-integer, near-fraction, near-zero, |x|² near integer
2. **Algebraic degree test** — PSLQ against polynomial bases up to degree 4
3. **Special value check** — CM discriminant matching for quadratic irrationals
4. **Output** — JSON + Markdown reports with verdicts for each value

## Input data
- `f1_base_certificate.json` — Trans families with coefficients and relations
- `trans_verification.json` — K values at 300 dps
- `h017_sign_a2_report.json` — disc_a and Möbius parameters

## Scan groups
- **A** — K values and Möbius coefficients (expected: transcendental K, integer coeffs)
- **B** — disc_a values (expected: exact integers)
- **C** — Möbius determinants (expected: nonzero integers)
- **D** — a₂/b₁² ratios (KEY CHECK: test if exactly −2/9)
- **E** — PSLQ residuals (expected: precision artifacts, no algebraic structure)

## Output
- `scanner_report.json` — structured results
- `scanner_report.md` — human-readable report
- `claims.jsonl` — AEAL entries for each discovery
