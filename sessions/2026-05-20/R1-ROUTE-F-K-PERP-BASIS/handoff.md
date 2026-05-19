# Handoff -- R1-ROUTE-F-K-PERP-BASIS
**Date:** 2026-05-20
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~55 minutes (single session)
**Status:** COMPLETE

## What was accomplished

Tier-3b cycle 2 of the R1-ROUTE-F three-cycle brief.  With the
cycle-1 canonical Sakai-convention KNY embedding fixed
(`d6_affine_simple_roots_kny()` per KNY 2017 sec.8.2.19 eq (8.101),
under the configuration-independent Pic intersection form per KNY
sec.3.3 eq (3.26)), we constructed an explicit Z-basis of the
rank-9 sublattice `K_X^perp = { v in Pic(X) : <v, -K_X> = 0 }`,
expressed each of the seven KNY simple roots `delta_0,...,delta_6`
as a Z-linear combination of that basis, computed the Smith Normal
Form of the resulting 7x9 integer matrix, and resolved the
saturation question.  Verdict: **SATURATED_AT_RANK_7**.  All seven
elementary divisors equal 1 and the saturation index is 1, so the
KNY embedding is Z-primitive in `K_X^perp`.

## Key numerical findings

(All exact integer computation; no floating point.  `dps = 0`.)

- **Cycle 2 verdict: `SATURATED_AT_RANK_7`.** Script:
  `python -m sakai_d6.saturation --analyze`.
- **Elementary divisors of M = `kny_in_k_perp_coords()` (7x9):**
  `(1, 1, 1, 1, 1, 1, 1)`.  Script:
  `sakai_d6/saturation.py::smith_normal_form_of_kny()` via
  `sympy.matrices.normalforms.smith_normal_form`.
- **Saturation index:** 1 (= product of elementary divisors).
- **Closure generators needed:** 0.
- **Rank of K_X^perp:** 9 (confirmed by determinant of 9x9 free-coord
  minor = +/-1).
- **K_X^perp is Z-primitive in Pic(X).** The Z-basis is
  `b_1 = H_1 - 2 E_1`, `b_2 = H_2 - 2 E_1`,
  `b_{3+k} = E_{2+k} - E_1` for `k = 0..6`.
- **K_anti = -K_X is itself in K_X^perp** (since
  `(-K_X)^2 = 0` for `Bl_8(P^1 x P^1)`).  Explicit decomposition:
  `-K_X = 2 b_1 + 2 b_2 - b_3 - b_4 - b_5 - b_6 - b_7 - b_8 - b_9`.
- **KNY imaginary root identity (NEW cross-cycle pin):**
  `sum_i a_i delta_i = -K_X` with affine D_6^(1) marks
  `a = (1, 1, 2, 2, 2, 1, 1)`.

Pytest summary: 74 passed in 5.14 s
(31 cycle-0 + 17 cycle-1 + 26 cycle-2).

AEAL hash (SHA256 of `python -m sakai_d6.saturation --analyze`
utf-8 stdout):
`fe150ee817030bab070b2fa1c07cfbedb4c6e058e4882875db7a9aba0b371ee4`.

## Judgment calls made

1. **Choice of K_X^perp basis.**  Picked the natural
   parametrisation by free coords `(H_1, H_2, E_2..E_8)` with
   `v_{E_1}` determined.  This makes the integer rank check
   trivial (9x9 minor on free cols is identity, det = +1) and
   makes "express delta_i in K_perp coords" a simple coordinate
   read-off.  Other bases would give the same SNF result; this
   one minimises code.

2. **Reproduce command and AEAL `output_hash_scope`.**  Chose
   `python -m sakai_d6.saturation --analyze` (a focused
   verifier that prints a JSON dictionary with all 11 verification
   flags + the verdict + elementary divisors + index) rather than
   hashing the full `pytest -v` stdout (which depends on
   pytest version and timing).  The full pytest sweep is still in
   the AEAL `script` field as a sanity wrapper but is not the
   hashed scope.

3. **Cycle 1 `COMPLETION_REPORT.md` was overwritten in the
   workspace** with the cycle-2 version.  The cycle-1 version is
   preserved in the bridge at
   `sessions/2026-05-20/R1-ROUTE-F-SAKAI-NONGEN/COMPLETION_REPORT.md`
   (bridge commit `53efe94`).

4. **The verdict matched the canonical-expected outcome.**  We
   reported it as the cycle 2 finding without further drama; the
   `unexpected_finds.json` cycle-2 entry says "no anomaly".  We
   did not search for a non-saturated branch or treat the
   primitive-embedding result as a surprise.

## Anomalies and open questions

THIS IS THE MOST IMPORTANT SECTION.  Read carefully.

1. **No halt condition fired.**  All five pre-registered halt
   conditions (`K_PERP_RANK_MISMATCH`, `KNY_NOT_IN_K_PERP`,
   `SATURATION_AMBIGUOUS`, `UNEXPECTED_INDEX`, `SNF_RANK_DEFICIT`)
   evaluated to false.  `halt_log.json` stays `{}`.
   `discrepancy_log.json` stays `{}`.

2. **No literature anomaly.**  The result
   "KNY simple roots are saturated in K_X^perp" is the standard
   canonical algebraic-geometry expectation for the PIII(D_6)
   Sakai surface; it is not a contradiction, surprise, or new
   positive result.  Recording for completeness, not for review.

3. **Cycle 3 (effectivity classification) is NOT started.**  Per
   the SIARC sequential-cycle-dispatch convention, cycle 3 will be
   relayed by Claude after review of this cycle.

4. **Quotient `K_X^perp / L_delta` is free of rank 2.**  This is
   the two-parameter "transcendental" Halphen-pencil dimension
   for PIII(D_6).  Cycle 3 may want to identify the specific
   rank-2 lattice (likely span by an elliptic fibre class F and
   `-K_X`, but the precise structure under the restricted Picard
   form is open).  Flagged as a candidate cycle-3 sub-question;
   not pursued here.

5. **Pre-existing test name misnomer (cycle 0).**
   `test_self_intersection_is_eight` in `test_root_system.py`
   actually asserts the value 0 with an inline-comment correction.
   We did NOT rename it (out-of-scope refactor).  Cycle 2 adds a
   clearly-named cross-consistency test
   `test_anti_canonical_self_intersection_is_zero` in
   `test_k_perp_basis.py` to make the actual asserted value
   discoverable by name.  Synthesizer may want to flag this for a
   future hygiene pass.

6. **Closure-generator code path (`saturation_closure_generators`)
   is implemented but not exercised by the run** because the
   verdict was SATURATED.  It is wired to
   `sympy.matrices.normalforms.smith_normal_decomp`.  Code is
   complete; a synthetic-input regression test would be needed to
   exercise it.  Not added here (out of scope).

## What would have been asked (if bidirectional)

- "If the verdict were `NOT_SATURATED_WITH_INDEX_k`, should the
  generator output be canonicalised in any particular form
  (e.g. with non-negative E-coefficients, or with a fixed
  ordering)?"  Moot since `SATURATED_AT_RANK_7`.
- "Should `test_self_intersection_is_eight` be renamed during this
  cycle (a one-line hygiene fix) or left for a separate pass?"
  Chose to leave it untouched (out of scope).
- "Is the rank-2 quotient identification a cycle-3 deliverable, or
  should cycle 3 be strictly the effectivity classification of
  `delta_i` themselves?"  Deferred to the cycle-3 dispatch.

## Recommended next step

Dispatch cycle 3: effectivity classification of the seven KNY
simple roots `delta_0, ..., delta_6` (which of them are effective
divisor classes on the PIII(D_6) Sakai surface, and what are their
explicit representatives in the Halphen pencil setup).  Use the
canonical Sakai-convention KNY embedding from cycle 1 and the
saturated-rank-7 result from cycle 2 as locked substrate.
Optionally include "identify the rank-2 lattice
`K_X^perp / L_delta`" as a sub-question (open item 4 above).

## Files committed

Under `sessions/2026-05-20/R1-ROUTE-F-K-PERP-BASIS/`:

- `sakai_d6/saturation.py`               (new cycle-2 module)
- `sakai_d6/tests/test_k_perp_basis.py`  (26 cycle-2 tests, 5 classes)
- `claims/claim-r1-k-perp-basis-001.json` (pre-registered AEAL claim, now filled)
- `claims.jsonl`                         (2 lines: cycle 1 + cycle 2)
- `k_perp_basis.json`                    (9x10 Z-basis of K_X^perp)
- `kny_in_k_perp_coords.json`            (7x9 matrix M)
- `saturation_verdict.json`              (verdict + SNF + index)
- `COMPLETION_REPORT.md`                 (cycle-2 report)
- `halt_log.json`                        ({} -- no halt fired)
- `discrepancy_log.json`                 ({} -- no discrepancy)
- `unexpected_finds.json`                (cycles 1+2 entries)
- `handoff.md`                           (this file)

## AEAL claim count

1 entry written to `claims.jsonl` this session (cycle 2).
Cumulative `claims.jsonl` line count for R1-ROUTE-F = 2 (cycle 1 + cycle 2).
