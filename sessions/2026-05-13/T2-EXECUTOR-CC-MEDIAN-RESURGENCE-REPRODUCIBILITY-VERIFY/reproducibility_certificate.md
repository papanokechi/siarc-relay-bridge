# Reproducibility Certificate — CC-MEDIAN-RESURGENCE-EXECUTE

**Task ID:** T2-EXECUTOR-CC-MEDIAN-RESURGENCE-REPRODUCIBILITY-VERIFY
**Date:** 2026-05-13
**Status:** REPRODUCED (7/8 bit-identical; 1/8 cosmetic-only divergence)

## Source artefact

| Item | Value |
|---|---|
| Original fire | `sessions/2026-05-02/CC-MEDIAN-RESURGENCE-EXECUTE/` |
| Original commit | `ed61428a13795ad1cf3f922959b36c213d7727fb` |
| Original verdict | `H4_EXECUTED_PASS_108_DIGITS` |
| Original script hash | (`median_resurgence.py`, 31284 bytes, mtime 2026-05-02 18:44:41) |
| Determinism claim under test | H4-A8 — "median_resurgence.py is deterministic at dps=250; rerun reproduces Qn_5000_dps250.csv hash bit-for-bit" |

## Re-run environment

| Field | Value |
|---|---|
| OS | Windows_NT (Windows 11) |
| Python | 3.12.10 |
| mpmath | 1.3.0 |
| Wall time (this run) | ~7 min 10 sec (script start 09:01 → last write 09:08:31 JST) |
| Host load | shared interactive PowerShell session; no special isolation |

## Output hash comparison (SHA-256)

| File | 2026-05-02 (first 16) | 2026-05-13 (first 16) | Status |
|---|---|---|---|
| `claims.jsonl` | `0CE079CDCD595D64` | `0CE079CDCD595D64` | **MATCH** |
| `fit_branch_exponent.log` | `A61123D31A98C2AA` | `A61123D31A98C2AA` | **MATCH** |
| `local_germ_crosscheck.log` | `EBFB3FA238226C41` | `EBFB3FA238226C41` | **MATCH** |
| `phaseA_series.log` | `52C7A0A680762948` | (differs) | **COSMETIC-ONLY DIFF** |
| `Qn_5000_dps250.csv` | `0B9E656F08B5B1DA…` | `0B9E656F08B5B1DA…` | **MATCH** (full hash `0b9e656f08b5b1dae67ebaffa5456e3625594b8e4c1904b4d0b2487ab30687cd`) |
| `S_zeta_star_digits.txt` | `4DDCA058CFE2E29F` | `4DDCA058CFE2E29F` | **MATCH** |
| `stokes_extraction.log` | `0807FE74CD755D4F` | `0807FE74CD755D4F` | **MATCH** |
| `verdict.md` | (omitted — verified MATCH in compare) | — | **MATCH** |

**Summary:** 7 of 8 outputs are bit-identical; the 8th (`phaseA_series.log`) differs only in `elapsed=Xs` decoration strings (host-load dependent timing) — all numerical content (a_k magnitudes at every checkpoint k ∈ {500,1000,…,5000}; a_1, a_2, a_5, a_5000 explicit values) reproduces verbatim.

### `phaseA_series.log` divergence detail

Diff in `Compare-Object` shows only timing rows changed:

```
[Phase A] k= 1000 a_k mag~10^2202 elapsed=0.0s    (new run)
[Phase A] k= 1000 a_k mag~10^2202 elapsed=0.1s    (old run)
[Phase A] complete in 0.4s                          (new run)
[Phase A] complete in 0.3s                          (old run)
```

The magnitude column `a_k mag~10^N` matches exactly at every checkpoint; the explicit a_5000 magnitude `10^14505` matches. The 1.3 MB `Qn_5000_dps250.csv` matrix matches bit-for-bit (matching SHA-256 `0b9e656f…b30687cd`), which is the substantive determinism claim.

## Mathematical content reproduced

| Quantity | Value (bit-identical to 2026-05-02) |
|---|---|
| β (branch exponent) | 0 (logarithmic; refinement of H4's "half-integer expected") |
| C (Stokes coefficient) | 8.12733679549507… |
| S_{ζ*} | 0.0 + 51.0655631399546622698316746099456615679204103033…·i |
| Digit-agreement Phase C ↔ Phase D cross-check | 108.39 digits (vs H4 forecast 30–50, central 40) |
| Verdict | `H4_EXECUTED_PASS_108_DIGITS` |

## Conclusion

Claim H4-A8 ("median_resurgence.py is deterministic at dps=250; rerun reproduces Qn_5000_dps250.csv hash bit-for-bit") is **VERIFIED** across an 11-day gap on the same host with a fresh Python interpreter session. All mathematical outputs reproduce. The single non-matching file differs only in non-mathematical timing strings.

This is the n=2 evidence today of the supersession-gate pattern (M-A xi_0 d=3 + M-C median-resurgence): both Tier-1 picks recommended by the 2026-05-12 strategic-landscape review had already been executed on 2026-05-02 and reproduce bit-identically today.
