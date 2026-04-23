# PCF Scale Selector (Layer 0 POC)

## Overview
Layer 0 of the SIARC pipeline: given a phenomenon observed at (d=2, D=4),
find the smallest (d, D) at which the same phenomenon appears at d=3.

Target: Trans-stratum families with Mobius-of-pi limits.

## Usage
```bash
python scale_selector.py
```

## Search procedure
For each D in {1, 2, 3, ...}:
1. Enumerate F(3,D) — all PCFs with degree-3 numerator/denominator polynomials
2. Pre-screen: structural Rat check (a(k)=0), degree profile, ratio check
3. Float64 batch convergence check (modified Lentz algorithm)
4. Float64 rationality pre-screen
5. mpmath PSLQ classification on surviving candidates
6. Stop when first Trans family found

## Pre-screening protocol
- **Screen 1**: a(k)=0 for k in {1,...,3D} → Rat structural
- **Screen 2**: a_lead/b_sublead^2 ratio check (heuristic from d=2)
- **Screen 3**: Degree profile priority: b_deg < a_deg preferred

## Output
- `scale_selector_report.json` — structured results
- `scale_selector_report.md` — human-readable report
- `structural_comparison.json` — d=2 vs d=3 signature comparison
- `claims.jsonl` — AEAL entries
