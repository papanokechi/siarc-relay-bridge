# Handoff — BSD-RATIO-RANK2-N10000-C1
**Date:** 2026-04-25
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~10 minutes
**Status:** HALTED (tool gap + LMFDB reCAPTCHA + LMFDB precision ceiling)

## What was accomplished
The relay asked for a 200-dp BSD-ratio sweep over all 2388 rank-2 elliptic curves with conductor ≤ 10,000. The session HALTED before any curve was processed: the active Windows venv lacks an L-function engine (no Sage, no cypari2, no PARI/gp on PATH), the LMFDB bulk API is currently gated by Google reCAPTCHA which prevents retrieval of the 2388-curve list, and LMFDB's cached `special_value` for sample curve 389.a1 is stored at only ~40 dp (prec=133 bits) — fundamentally below the 200-dp target. A skeleton `bsd_ratio_sweep.py` was written so a follow-up session with a real L-engine can complete the sweep.

## Key numerical findings
- No BSD ratios were computed (L-engine unavailable).
- 389.a1 cached `special_value` precision = 133 bits ≈ 40 dp (independently_verified, single-record API call).
- LMFDB bulk API returns reCAPTCHA HTML for `?rank=i2&_format=json` (independently_verified, 2026-04-25).

## Judgment calls made
- **Halted instead of degrading the precision target silently.** The relay specified 200 dp; the cached LMFDB precision ceiling is ~40 dp, so even a "best-effort" sweep using LMFDB's `special_value` would not satisfy claim C2 ("R(E) computed to 200 dp for all N curves"). Halting and surfacing the tool gap is more honest than producing a spuriously labeled 200-dp result file.
- **Did not attempt a from-scratch Dokchitser implementation in mpmath.** Building an a_p oracle plus approximate-functional-equation summation to 200 dp for 2388 curves is far beyond a single session's budget; per standing instructions, brute-forcing was avoided.
- **Did not retry the LMFDB API after the reCAPTCHA gate appeared.** Single-record GETs (`?lmfdb_label=389.a1`) still succeed, suggesting the gate is rate/pattern-triggered. Retrying repeatedly would risk a longer ban.

## Anomalies and open questions
- **LMFDB reCAPTCHA gate:** the public API for `ec_curvedata` is now serving a Google reCAPTCHA challenge for paginated queries. This is new behavior versus prior SIARC sessions and may affect any future LMFDB-bulk-fetch relay. Worth reporting to LMFDB or switching to the Postgres dump / `beta.lmfdb.org` mirror for bulk work.
- **Precision ceiling mismatch:** the relay asks for 200 dp, but LMFDB caches L-special values at 100–133 bits. Any future BSD-ratio relay needs to either (a) install a local L-engine, or (b) re-scope the precision target to ~30 dp. Claude should clarify which.
- **No L-engine in venv:** this is a recurring constraint (cf. memory `t4-lean-iter27-integration-2026-04-21.md` referencing Lean tooling but not an L-engine). A one-time install of `cypari2` (pip-available with prebuilt wheels for some Python versions) or WSL-Sage would unblock a large class of relays.
- **Python 3.14 in venv:** several scientific wheels (cypari2, sage) do not yet ship Py3.14 builds, so simply `pip install cypari2` may not work without falling back to a 3.11/3.12 interpreter.

## What would have been asked (if bidirectional)
1. "Is 30 dp acceptable as a fallback if no local L-engine is installable?"
2. "Should we proceed in WSL with Sage, or install PARI Windows binaries?"
3. "Is the LMFDB reCAPTCHA gate observable in your environment too, or did it only trip on this venv's IP?"

## Recommended next step
Open a small bootstrap relay (e.g. `BSD-LENGINE-BOOTSTRAP-C1`) to either (a) install cypari2 against a Python 3.12 venv and verify `pari.ellL1(E)` works, or (b) provision a WSL Sage env. Once the engine is in place, re-issue `BSD-RATIO-RANK2-N10000-C2` with either confirmed 200 dp via the engine or an explicit, agreed precision (~30 dp) using LMFDB cache.

## Files committed
- `halt_log.json` — three-blocker halt record (no L-engine, LMFDB reCAPTCHA, LMFDB precision ceiling)
- `discrepancy_log.json` — empty `{}` (no curves processed)
- `unexpected_finds.json` — empty `{}` (PSLQ pass not run)
- `bsd_curves_rank2.json` — empty `[]` (bulk fetch blocked)
- `bsd_results.jsonl` — empty (sweep not run)
- `bsd_ratio_sweep.py` — skeleton, NOT executed; ready for a follow-up session with an L-engine
- `claims.jsonl` — three `independently_verified` claims documenting the tool gap, reCAPTCHA gate, and precision ceiling
- `handoff.md` — this file

## AEAL claim count
3 entries written to claims.jsonl this session. All three are `independently_verified` claims about the session's own infrastructure constraints; no BSD numerical-identity claims were generated.
