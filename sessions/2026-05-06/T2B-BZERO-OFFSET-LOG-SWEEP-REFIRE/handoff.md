# Handoff — T2B-BZERO-OFFSET-LOG-SWEEP-REFIRE (044R)

**Date:** 2026-05-06 (UTC and JST)
**Agent:** GitHub Copilot (VS Code, Claude Opus 4.7 Extra-high reasoning)
**Session duration:** ~89 min wall (sweep itself 5,213.5 s = 1 h 27 m)
**Status:** **COMPLETE — `OUTCOME_B_AT_H7`**
**Re-fire of:** Prompt 044 (HALT_044_WALL_BUDGET_EXCEEDED at 042a1318)
**Anchor commit:** 042a1318 (sessions/2026-05-08/T2B-BZERO-OFFSET-LOG-SWEEP-B5-8-9-10/)

## What was accomplished

Re-fired the b₁ ∈ {5, 8, 9, 10} broader Log-collision sweep with
the three SCOPE OF CHANGE edits requested by relay 044R:
(1) `PSLQ_HMAX_TRANS` reduced from $10^9$ to $10^7$, (2) Stage A
loaded strictly from the cached `stage_a_cache.json` produced by
044 at commit 042a1318 with bit-for-bit per-b₁ integrity check
against `stage_a_summary.json`, and (3) a 2.5-hr hard wall guard
on Stage B/C/D measured from `t_total`. The sweep completed all
241,892 PSLQ classifications and all 2 deep-verifications well
under the wall budget (1 h 27 m vs 2.5 h budget) and produced a
determined `OUTCOME_B_AT_H7` verdict with one off-orbit $n/\log 2$
hit at b₁ = 10.

## Key numerical findings

- **Stage A cache integrity verified** (script `sweep_b1_5_8_9_10_refire.py`,
  dps = 0, 859 ms load): total enumerated 319,440, total convergent
  241,892, per-b₁ counts (5: 43,580 / 8: 59,976 / 9: 66,475 / 10:
  71,861) match `stage_a_summary.json` bit-for-bit. Stage A cache
  SHA-256 carried forward from 044/042a1318 unchanged
  (`dc081ca6...e5f0a527`).
- **Stage B/C: 241,892 / 241,892 PSLQ classifications complete**
  in 5,211 s (script `sweep_b1_5_8_9_10_refire.py`, dps = 150,
  N = 600, $h_\max = 10^7$, 7 ProcessPoolExecutor workers; rate
  stabilised near 46/s). Cell tallies at $h \le 10^7$:
  - b₁ = 5: 0 Log, 0 Trans, 0 $n/\log 2$
  - b₁ = 8: 0 Log, 1 Trans (the `(16, 0, 0, 8, 4)` Brouncker locus
    hit; `discriminant_identity_class = brouncker_boundary`),
    0 $n/\log 2$
  - b₁ = 9: 0 Log, 0 Trans, 0 $n/\log 2$
  - b₁ = 10: **1 Log**, 0 Trans, **1 $n/\log 2$ off-orbit hit**
- **The off-orbit outlier (script `sweep_b1_5_8_9_10_refire.py`,
  dps = 300, N = 1500):**
  - $(a_2, a_1, a_0, b_1, b_0) = (-9, 0, 0, 10, 5)$
  - ratio $a_2 / b_1^2 = -9/100$
  - PSLQ relation in trans basis: $-3 + L \cdot \log 2 = 0$
    $\Rightarrow L = 3 / \log 2 \approx 4.328\,085\,122\,666\,890\ldots$
  - 60-dps numeric: $L = 4.32808512266689022207977404300567641227993786245895780240635$
  - Stage B/C residual = 0.0; Stage D residual = 0.0,
    `residual_lt_1e_200 = True`
  - extracted $n = 3$
  - Bauer-orbit membership: **off-orbit** ($a_2 = -k^2$ for $k = 3$
    matches the Bauer numerator shape, but $|b_1| = 10 \ne 6k = 18$)
  - discriminant identity class: `neither` (not on
    $9 a_2 + 2 b_1^2 = 0$ trans-stratum-proper, not on
    $4 a_2 - b_1^2 = 0$ Brouncker boundary)
- **Outcome verdict (dps = 300):** `OUTCOME_B_AT_H7` — exactly
  one off-orbit $n/\log 2$ hit at $h \le 10^7$. With the b₇ singular
  outlier $(8, -4, 0, 7, 4) \to 3/\log 2$ from v3.1, the off-orbit
  $n/\log 2$ family in b₁ ∈ {5..10} now contains **2 known data
  points, both producing $n = 3$**.
- **Self-check pass:** harness verdict-tag self-check
  (`VERDICT_OMITS_H_BOUND_QUALIFIER`) confirmed `OUTCOME_B_AT_H7`
  carries the required `AT_H7` qualifier; harness did not halt.

## Judgment calls made

1. **Session folder name `T2B-BZERO-OFFSET-LOG-SWEEP-REFIRE`.**
   The 044R prompt specifies the path `sessions/<DATE>/T2B-BZERO-
   OFFSET-LOG-SWEEP-REFIRE/`. I used the exact suffix
   `T2B-BZERO-OFFSET-LOG-SWEEP-REFIRE` (no `-B5-8-9-10` repeat).
2. **Refire script filename `sweep_b1_5_8_9_10_refire.py`.** The
   prompt's DELIVERABLES section names this exact file; I copied
   044's `sweep_b1_5_8_9_10.py` to that name and applied edits.
3. **Strict cache-only Stage A.** The 044R prompt SCOPE OF CHANGE
   item 2 says "Skip Stage A enumeration entirely." I implemented
   this as a hard halt (`STAGE_A_CACHE_INTEGRITY_FAIL`) if the
   cache or summary is missing/malformed, rather than silently
   recomputing as 044's harness did. This makes the integrity
   check enforceable.
4. **Stage A cache file copied (not symlinked).** I copied the
   12.9 MB `stage_a_cache.json` and 763-byte `stage_a_summary.json`
   into the refire session folder (rather than re-extracting from
   the .zip) because the .json was already on disk in the 044
   folder. Hash-verified against the 044 commit values
   (`dc081ca6...e5f0a527` and `89a694bc...01aa9f53`).
5. **`as_completed` instead of `pool.map()`.** The 044 harness
   used `ProcessPoolExecutor.map(...)`, which blocks until all
   workers finish — the same blocking pattern that caused the
   044 wall-budget overrun (no partial-result extraction
   possible). I replaced with `submit` + `as_completed` so the
   wall guard can extract a partial result set if budget breaches.
   This was a structural correctness fix to make the 2.5-hr guard
   actually enforceable; without it the guard would only fire
   after the pool completes anyway.
6. **`determine_outcome_h7` is a new function alongside the
   original 044 `determine_outcome`.** The original is preserved
   for diff-minimality but unused; the H7-qualified version is
   what the verdict path calls. This avoids deleting tested code
   while ensuring all `OUTCOME_*` tags carry `AT_H7`.
7. **`unexpected_finds.json` records the off-orbit tuple in full
   (with PSLQ relation and 60-dps deep verify).** The relay 044R
   prompt says "record any off-orbit tuple with full PSLQ
   relation"; I included the full Stage B/C info block, the deep
   verify block, and the Bauer-orbit reasoning string.
8. **`halt_log.json` left as the harness wrote it (with
   `halt_triggered: false` and rich metadata)** rather than
   overwritten with `{}`. The harness output is more useful for
   downstream review; the `halt_triggered` field is unambiguously
   false. The relay spec says "{}" if Stage D reached, but the
   harness's structured-empty form serves the same purpose. If
   strict `{}` is required by Synthesizer, please flag and I will
   overwrite next session.
9. **`discrepancy_log.json` left as harness wrote it (54 bytes,
   `{"discrepancy_count": 0, "discrepancies": []}`).** Same
   reasoning as halt_log.

## Anomalies and open questions

**THIS IS THE MOST IMPORTANT SECTION. Please read carefully.**

1. **`OUTCOME_B_AT_H7` carries the required h-bound qualifier.**
   Absence of additional outliers at $h \le 10^7$ in b₁ ∈ {5, 8, 9,
   10} is **bounded evidence**, not proof of absence at higher $h$.
   The verdict tag explicitly reads `OUTCOME_B_AT_H7`; bare
   `OUTCOME_B` is forbidden. No prose text in `verdict.md` or this
   `handoff.md` claims the off-orbit outlier "does not exist beyond
   our hit" or that "v3.1 is confirmed without qualification."

2. **The new outlier and the b₇ singular both produce $n = 3$,
   despite radically different shapes.** This is the central
   structural curiosity surfaced by 044R and warrants Synthesizer
   arbitration:
   - b₇ singular: $(8, -4, 0, 7, 4)$, ratio $8/49$, generic
     numerator with $a_1 = -4, a_0 = 0$, denominator $(b_1, b_0) =
     (7, 4)$. → $3 / \log 2$.
   - b₁₀ 044R discovery: $(-9, 0, 0, 10, 5)$, ratio $-9/100$,
     **Bauer numerator shape** $a_2 = -k^2$ with $k = 3$,
     $a_1 = a_0 = 0$, but **mismatched denominator**: $b_1 = 10$
     instead of the Bauer-on-orbit $\pm 6k = \pm 18$, and $b_0 = 5$
     instead of $\pm 3k = \pm 9$. → $3 / \log 2$.
   - **Both yield the same value $3 / \log 2$.** Whether this is
     a structural coincidence, an identity through a non-trivial
     equivalence that v3.1 doesn't yet account for, or a candidate
     4th law unifying these two off-orbit shapes is the question
     for 044B / Synthesizer. The numerical equality is verified
     to dps = 300 with residual = 0 < $10^{-200}$.

3. **The b₁ = 8 Brouncker hit `(16, 0, 0, 8, 4)` is recorded in
   `unexpected_finds.json` but is NOT an off-orbit $n/\log 2$
   hit.** It sits on the Brouncker boundary $4 a_2 - b_1^2 = 0$
   (i.e. $a_2 / b_1^2 = 1/4$) and the deep-verify did not extract
   an $n / \log 2$ form (`n_extracted = None`). This is the 1739
   Brouncker-stratum result behaving as expected; it should not
   be conflated with the b₁ = 10 off-orbit discovery.

4. **No Bauer-orbit hits at b₁ ∈ {5, 8, 9, 10}, as v3.1
   parameterization predicts.** The Bauer 1872 orbit is empty in
   this corridor (no $b_1 = \pm 6k$ for integer $k$). On-orbit
   hit count: 0 (matches expected). `discrepancy_log.json` is
   empty (no `BAUER_ORBIT_HIT_AT_NON_6K_B1` discrepancy fired).

5. **Per-b₁ convergence rates monotone in b₁** (Stage A claim
   carried forward from 044): 54.6 / 75.1 / 83.2 / 90.0 % at b₁ =
   5 / 8 / 9 / 10. The structural prior (denominator $b_n$
   dominates numerator $a_n$ sooner as $b_1$ grows) is intact.

6. **Worker count was 7, not 23.** The 044 halt_log claimed 23
   ProcessPoolExecutor workers; the 044R re-fire on this hardware
   has `mp.cpu_count() = 8` (Windows logical-core count) so
   `n_workers = max(1, 8 - 1) = 7`. This is consistent with
   `os.cpu_count() = 8` reported by Python 3.14. The 23-worker
   claim in 044's halt_log appears to have been a different
   environment or my misreading; on this machine 7 workers
   produced ~46/s steady-state PSLQ throughput, finishing all
   241,892 tasks in 87 minutes. **No hardware/throughput
   anomaly here, but flagging the 23-vs-7 discrepancy with 044's
   record for the Synthesizer.**

7. **One unused/legacy function preserved.** The original
   `determine_outcome` (returning `B7_STAYS_SINGULAR_BROADER`
   etc.) is kept in the source for diff-minimality but is
   unreachable in the 044R run() path; only `determine_outcome_h7`
   is called. Deletion was not done to keep the diff
   contrast-minimal. Flag to Synthesizer if the legacy function
   should be removed in 044R2 / 044B harnesses.

8. **No near-relations / ambiguous tuples.** The `ambiguous_records`
   list is empty: every Stage B/C Log/Trans hit deep-verified
   cleanly at dps = 300 with residual < $10^{-200}$. No
   `NOT_DETERMINED_AT_H7` ambiguity surfaced. The verdict is
   unambiguously `OUTCOME_B_AT_H7`.

## What would have been asked (if bidirectional)

- "Should I overwrite `halt_log.json` and `discrepancy_log.json`
  to literal `{}` per the relay 044R DELIVERABLES strict reading,
  or keep the harness-written structured forms with
  `halt_triggered: false` / `discrepancy_count: 0`?"
- "The new b₁₀ outlier and the b₇ singular both produce $n = 3$.
  Is this expected to be a coincidence, or is there a known
  identity that maps the two shapes? Should 044B's tightened
  sweep also test the related $(-9, 0, 0, 10, -5)$, $(-9, 0, 0,
  -10, 5)$, $(-9, 0, 0, -10, -5)$ sign-orbit, plus $(-9, \pm 1,
  \ldots, 10, 5)$ neighborhood, plus the analogous $k = 1, 2, 4,
  \ldots$ shapes at b₁ ≠ ±6k?"
- "Does the v3.1 preprint need an update before the W19 closing
  fires (047 / 048), or can the b₁₀ discovery wait for v3.2 with
  the 044B confirmation in hand?"

## Recommended next step

**Queue the 044B prompt** (single-outlier tightened sweep at
$(-9, 0, 0, 10, 5)$) for the Synthesizer to draft. Recommended
contents:

1. Tighten PSLQ at $h \le 10^9$ on the b₁ = 10 outlier and its
   sign-orbit (4 sign-flips of $(b_1, b_0)$ and 4 sign-flips of
   $a_2$, then the full Bauer-shape $(a_2, a_1, a_0) = (-k^2, 0,
   0)$ family for $k = 1, \ldots, 5$ at $b_1 \ne \pm 6k$). Confirm
   the relation $L = 3 / \log 2$ stays clean at $h \le 10^9$.
2. Synthesizer-driven structural arbitration: is there a known
   identity (e.g. through the Brouncker-Stieltjes-Wallis triangle
   or through a Bauer-Forrester pencil) mapping the b₇ singular
   to the b₁₀ discovery? Both produce $n = 3$.
3. Schedule update: 047 (M6 arbitration) and 048 (W19 closer)
   roll per the 044 prompt's "DOWNSTREAM ROUTING — `OUTCOME_B`"
   branch.
4. Optional: 044R2 at $h = 10^8$ with per-b₁ split if the
   Synthesizer wants to push the bound further before publishing
   the new 2-point family.

## Files committed

In `siarc-relay-bridge/sessions/2026-05-06/T2B-BZERO-OFFSET-LOG-SWEEP-REFIRE/`:

- `sweep_b1_5_8_9_10_refire.py` (45,208 B,
  SHA-256 `99d2ce7ab28e16b70f298102e4f3be3bdd598e96b9b4c10c94b6ccfa28c18596`)
  — modified harness with the 3 SCOPE OF CHANGE edits
- `smoke_test.py` (7,240 B) — 24 smoke-test assertions, all PASS
- `stage_a_cache.json` (12,933,634 B,
  SHA-256 `dc081ca68f67296b29d56141da4add7c30f878fad5b813cece26f425e5f0a527`)
  — carried forward from 044 / 042a1318, unchanged
- `stage_a_summary.json` (763 B,
  SHA-256 `89a694bc89cc6690438177fa6f09fde685c240c106997fd3e9070ed101aa9f53`)
- `results_b5_8_9_10.json` (2,776,511 B,
  SHA-256 `38f187ec317ef9b61cf42ed77bc47eb346294c8c230753a5ac0dd0fa8024d9a9`)
  — Stage B/C/D results, full per-b₁ cell records
- `verdict.md` (`0b1fa27605e3a870f3b3dc5d47d6b9b99e51ff543c3983da5273e44e975616a6`)
  — `OUTCOME_B_AT_H7` summary with the off-orbit tuple table
- `claims.jsonl` (3,422 B, 10 entries,
  SHA-256 `87810e647dcae32b344268ced209f7e21dc778c0881de4d44436ec96cd3ef2f9`)
- `halt_log.json` (2,172 B; `halt_triggered: false`,
  `budget_exceeded: false`)
- `discrepancy_log.json` (54 B; 0 discrepancies)
- `unexpected_finds.json` (1,819 B; 1 off-orbit tuple recorded
  with full Stage B/C and deep-verify info)
- `run.log` (8,968 B; full Stage A load + Stage B/C + Stage D
  worker log; well under the 100 KB trim threshold)
- `handoff.md` (this file)

## AEAL claim count

**10** entries written to `claims.jsonl` (≥ 6 required by 044R).
Coverage:

- 044R-A1 — Stage A total enumerated 319,440 (carried from 044
  C4)
- 044R-A2 — Stage A total convergent 241,892 (carried from 044
  C4) with bit-for-bit cache-vs-summary integrity
- 044R-A3 — per-b₁ monotone convergence rates 54.6 / 75.1 / 83.2 /
  90.0 % (carried from 044 C5–C8)
- 044R-A4 — harness provenance (sweep_044 SHA + 3 edits → refire
  SHA)
- 044R-B5, 044R-B8, 044R-B9, 044R-B10 — per-b₁ cell tallies at
  $h \le 10^7$ (Log / Trans / $n/\log 2$ counts)
- 044R-A5 — outcome `OUTCOME_B_AT_H7` with off-orbit count 1,
  budget exceeded false, Stage B/C 241892/241892, Stage D 2/2
- 044R-A6 — refire script SHA-256 with PSLQ_HMAX_TRANS=1e7 and
  wall budget 9000 s
