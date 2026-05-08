# Phase B — Static audit of `jimbo_final.py` `S_num` provenance

**Audit input:** `pcf-research/vquad/scripts/jimbo_final.py`
**SHA-256 at audit time:** `E743A49C244CD56E2F9F0CFCD9E9E0D1447742A88BE56A3AC46C1FB5EEEDCE74`
**Last-mod time:** 2026-05-01 12:21:28 (predates 110-EXEC commit by 7 days; unchanged)
**Size:** 14238 B / 349 LC.
**HALT-111-RE-B:** PASS (file present and unmodified since 110-EXEC commit).

---

## §1 `S_num` assignment location

Located at **L26** of `jimbo_final.py`:

```python
S_num = mpf("0.43770528073458")
```

Single assignment in the file. The token `S_num` appears in 9 additional locations (L194-L255: print-statements, root-finding equation residual, PSLQ basis-vector entries, normalisation diagnostic), all as RHS reads — no second assignment redefines it.

---

## §2 RHS classification

| Component | Value |
|---|---|
| Constructor | `mpf(...)` (mpmath arbitrary-precision float) |
| Argument | string literal `"0.43770528073458"` (14 character digits) |
| Upstream computation in this file producing these digits? | **NONE** |
| Imported via `from X import S_num`? | **NO** |

Imports inventory (L14-L20):

```python
import sys, json, time
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import mpmath as mp
from mpmath import (mpf, mpc, pi, sqrt, gamma as G, sin, cos, exp,
                    log, nstr, fabs, re, im, matrix, acos, psi)
```

No project-internal imports; no `from X import S_num` elsewhere. The 14 digits appear ex nihilo as a string literal at L26.

**Classification per STEP B.2:** **(i) HARDCODED_STRING_LITERAL** (RHS is `mpf("0.43770528073458")`; no upstream computation produces the digits).

---

## §3 Companion metadata — precision

Search for `S_precision_digits` near the `S_num` assignment and in the file's emitted JSON output:

**L329** (in the result dict written to `pcf-research/vquad/results/jimbo_piii_final.json`):

```python
"S_precision_digits": 8,
```

This precision claim (8 digits) is internally INCONSISTENT with the literal at L26 (14 character digits in the string). Two readings:
1. The author considers only the first 8 digits as cited-anchor-quality and the remaining 6 as untrusted (truncation risk).
2. The `S_precision_digits: 8` field reflects an upstream measurement noise floor independent of the literal-string accuracy.

In either reading, the file does not document where the digits originated.

---

## §4 Companion metadata — provenance attribution

Search for substrings `Dingle` (case-insensitive), `late-term`, `late_term`, `hyperasymptotic`, `Borel` (case-insensitive), `resurgent` near the `S_num` assignment:

| Substring | Hits in file | Lines | Context |
|---|---|---|---|
| `Dingle` | 2 | L177, L191 | normalisation-formula discussion only |
| `late-term` / `late_term` | 0 | — | not present |
| `hyperasymptotic` | 0 | — | not present |
| `Borel` | 0 | — | not present |
| `resurgent` | 0 | — | not present |

L177 verbatim:
```
#   S_Dingle = |s|/(2*pi) [common normalization]
```

L191 verbatim:
```
# With various normalizations between s and S_Dingle.
```

These two `Dingle` references appear in a comment block (L172-L191) discussing alternative NORMALISATIONS between the connection coefficient `s = 2*sin(pi*sigma)*Gamma(1-sigma)^2/Gamma(1+sigma)^2` and a candidate `S_Dingle`. **NO comment, docstring, or print-statement in the file attributes the actual 14 digits `0.43770528073458` of `S_num` to any computational source.**

Filesystem-inspection telemetry: the result JSON path written by `__main__` is `pcf-research/vquad/results/jimbo_piii_final.json` per L325 — outside the scope of this static audit.

---

## §5 File purpose classification (`__main__` body)

Top-of-file docstring (L2-L11) verbatim:

```
DEFINITIVE: Jimbo 1982 PIII(D6) Connection Formula for V_quad Stokes Constant S.

RESULT: The Jimbo formula does NOT yield S in closed form because S depends
on the accessory parameter q of the CHE, which is transcendental.

This script:
1. Verifies finite monodromies are unipotent (theta_0=theta_inf=0)
2. Computes the connection matrix via high-precision Frobenius series
3. Shows sigma (connection parameter) depends on accessory parameter q
4. Confirms S is not a Gamma-function expression
```

Top-level `__main__` block top-down trace (no `if __name__ == "__main__":` guard; the file is a flat sequential script):

| Block | Line range | Operation |
|---|---|---|
| STEP 1 | L40-L70 | Frobenius indicial-equation verification (`theta_0 = theta_inf = 0`) |
| STEP 2 | L72-L130 | High-precision Frobenius series + connection matrix M |
| STEP 3 | L132-L170 | sigma extraction via tr(M_1 M_2) = 2 cos(2 pi sigma) |
| STEP 4 | L172-L210 | Normalisation analysis (Dingle / sin / Gamma variants) |
| STEP 5 | L239-L270 | Direct PSLQ on `S_num` against 7 candidate basis tuples |
| STEP 6 | L272-L320 | Closed-form attribution attempts (q-dependence) |
| (epilogue) | L320-L349 | JSON output with `match: false`, `closed_form: null` |

**Critical observations:**
- The script reads `S_num` as INPUT and tests whether `S_num` matches `2 sin(pi sigma) Gamma(1-sigma)^2 / Gamma(1+sigma)^2` for various sigma candidates (L211 `return 2*sin(pi*sig)*G(1-sig)**2/G(1+sig)**2 - S_num`).
- The script attempts PSLQ attribution (L249-L255) with `S_num` as one of the basis vectors.
- The result JSON at L325-L334 emits `"match": false`, `"closed_form": null`, `"F2_status": "OPEN"`, `"reason": "S depends transcendentally on accessory parameter q; Jimbo formula relates S to sigma but sigma=g(q) is not closed-form"`, and explicit `"next_steps": ["Push S to 12+ digits for stronger PSLQ", ...]`.
- The script does NOT compute S_num. It treats S_num as a fixed numerical anchor and searches for symbolic/closed-form matches.

**Classification per STEP B.5:** **(i) DIAGNOSTIC_SCRIPT** (PSLQ-style attribution attempts + basis-search + residual reporting; treats `S_num` as INPUT).

---

## §6 Phase B verdict

**`B_VERDICT_S_HARDCODED_STRING_LITERAL_DIAGNOSTIC_SCRIPT`**

Anchors:
- L26 `S_num = mpf("0.43770528073458")` — string-literal `mpf()` constructor.
- No `from X import S_num`; no upstream computation in this file.
- L329 `"S_precision_digits": 8` (precision claim for 14-character literal — inconsistency surfaced as discrepancy D-111-2).
- L172-L211 normalisation-only `Dingle` references; ZERO provenance attribution for the digits themselves.
- Top-level `__main__` is PSLQ + closed-form-search DIAGNOSTIC; emits `"match": false`.
