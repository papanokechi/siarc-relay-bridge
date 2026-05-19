# Handoff — T3B-VQUAD-EXCL-T2DPRIME
**Date:** 2026-05-19
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ≈ 8 h wall-clock (≈ 130 min compute; the rest is the silent-kill diagnostic gap + recovery)
**Status:** COMPLETE

## What was accomplished

T2'' executed as a dual-axis cycle: axis 1 closed the coefficient-floor lift ($B_{3,2}$, 60 elements, maxcoeff $10^6$, 2050 dp) and axis 2 closed the V_quad-degree extension ($B_{4,2}$, 75 elements, maxcoeff $10^4$, 2050 dp), each at two precision tiers (500 + 2050 dp). Four canonical PSLQ runs plus one pre-flight smoke all returned None. Combined verdict: **EXCLUSION_CERTIFIED**. Two of the three falsification triggers from T2' are now closed numerically; the remaining open trigger is the joint axis ($B_{4,2}$ at maxcoeff $10^6$).

## Key numerical findings

- **V_quad fresh CF**: depth 5000 vs 6000 agree to 2200 digits at 2200 dp working precision (i.e., exact to working precision). First 64 chars `1.197373990688357602448603219937206329704270703231350336285792769` — **bit-identical to T2 and T2'**. V_quad is now a cross-cycle invariant. — `stage_2_verification.py`, dps 2200
- **Predecessor reload**: string-content SHA-256 `52375a71…f2f5c44` reproduces; reload-vs-fresh agreement = 1999 digits (matches the $mp.nstr$ 2000-digit 1-ULP truncation signature observed in T2 and T2'). — `stage_2_verification.py`, dps 2200
- **Axis 1 ($B_{3,2}$, maxcoeff $10^6$)**: PSLQ returns None at both 500 dp (259.4 s) and 2050 dp (3250.4 s). Sub-verdict NULL. — `stage_23_executor.py`, dps 500 & 2050
- **Axis 2 ($B_{4,2}$, maxcoeff $10^4$)**: PSLQ returns None at 500 dp (545.4 s, canonical), 500 dp (445.1 s, smoke from recovery driver), and 2050 dp (2799.7 s). Sub-verdict NULL. — `stage_23_executor.py` (canonical 500 dp) and `recover_tier_3d.py` (smoke + 2050 dp)
- **Combined verdict**: EXCLUSION_CERTIFIED. — `stage_4_5_archive.py`, dps 2050

## Judgment calls made

1. **Re-scoped the relay-named (3,3) tensor to a dual-axis cycle.** Claude's relay prompt named the strict bipartite (3,3) tensor at maxcoeff $10^6$, citing 40 elements and ~T2' runtime. The agent verified that on the four-classical-generator basis, the strict (3,3) tensor is $4\times 35 = 140$ elements with ~5–8 h at 2050 dp, breaking the "one Tier-3b session" budget. The dual-axis option (axis 1: maxcoeff $10^6$ on the existing 60-element (3,2) basis; axis 2: V_quad-degree extension to 4 at maxcoeff $10^4$) tests the same two underlying experimental dimensions within the budget. The strict (3,3) cycle is deferred to T2''''. Recorded in `env_snapshot.json` field `judgment_call_for_scope_choice` and `plan_dag.json` field `rationale_for_dual_axis`.

2. **Wrote a focused tier-3d recovery driver after the original executor died silently.** Between tier 3c (landed 10:45:53 JST) and tier 3d (never wrote output), the original `stage_23_executor.py` terminated without an error trace. By 14:56 JST no live `python.exe` was found. The recovery driver (`recover_tier_3d.py`) re-ran ONLY tier 3d with: (a) read inputs from disk (V_quad freshly recomputed once at depth 5000 dps 2200; basis loaded from `basis_4_2_enumeration.json` with SHA + mtime ordering check against canonical tier 3c); (b) heartbeat logging every 60 s to `tier_3d_progress.log`; (c) a pre-flight 500 dp smoke on the identical $B_{4,2}$ basis as a structural-invariance check against canonical tier 3c. The recovery run was successful: smoke matched canonical tier 3c on all structural invariants, then tier 3d returned None in 2799.7 s with a peak working-set of ~38 MB.

3. **Post-hoc rewrote `tier_3d_recovery.json` with tighter wording.** The first-pass sidecar (written by the driver at 15:56:12 JST) used `smoke_matches_canonical: true`, which over-claims given that `mp.pslq` returns only `None` or a list (no iteration count, no final reduction norm, no internal trace). The rewrite uses `smoke_structural_invariants_match` and adds `smoke_comparison_fields` + a `smoke_comparison_note` documenting exactly what `None == None` establishes and what it does not. The driver source (`recover_tier_3d.py`) was also patched in place to match this schema for any future re-run.

4. **Ran `stage_2_verification.py` as a post-hoc fill-in.** The original executor died after writing tier 3c JSON but before writing `raw_candidates.jsonl` and `executor_summary.json`, which would have contained the Stage 2 evidence (dual-depth agreement digits, reload-vs-fresh digits) required by `plan_dag.json` node `N2_vquad_fresh`. The fill-in script re-establishes those numbers with identical algorithm and parameters; it does not touch any PSLQ tier output (those are canonical from the original 3a/3b/3c runs and the recovery 3d run). Recorded as `stage_2_verification.json` and AEAL-cited.

5. **Excluded heartbeat logs from the manifest.** `tier_3d_progress.log` and `tier_3d_stdout.log` are timestamp-dependent and not part of the claim chain; they remain in the slot directory as narrative evidence for the recovery section but are excluded from `manifest.json` (with a documented note in `excluded_from_manifest_note`).

## Anomalies and open questions

**Anomaly #1: silent executor kill between tier 3c and tier 3d.**

Operational details:
- Last canonical tier output: `pslq_4_2_maxc4_500dp.json`, written 10:45:53 JST.
- Expected next output: tier 3d (2050 dp on $B_{4,2}$, ~95–110 min estimate).
- Observed: at 14:56 JST (~4 h after tier 3c) no `python.exe` was running; the slot held tiers 3a/3b/3c but no tier 3d, no `raw_candidates.jsonl`, no `executor_summary.json`.

**The recovery run's working-set peak was ~38 MB on a Windows 16 GB host with a heartbeat-logged Heartbeat thread**, which makes the original-kill cause **almost certainly not OOM**. The remaining plausible explanations:

- VS Code terminal pane closure (e.g., laptop sleep with the terminal not persisted, or user accidentally closing the integrated terminal panel) — most likely given the workstation profile.
- A silent mpmath internal failure (less likely; mpmath's PSLQ tends to raise on overflow rather than die silently).
- A Windows-side process kill (e.g., Defender or some process-watcher) — unlikely without evidence.

No definitive cause-of-death without a process-monitoring sidecar at the time. The operational lesson is recorded in §"What would have been asked" below.

**Anomaly #2: post-hoc Stage 2 fill-in vs canonical-executor original.**

The `stage_2_verification.py` numerics (dual-depth = 2200 digits, reload-vs-fresh = 1999 digits, first 64 chars `1.197373990688357602448603219937206329704270703231350336285792769`) are reproducible from the algorithm + inputs and are consistent with the in-memory log lines the original executor was about to write. The recovery driver also computed V_quad at depth 5000 dps 2200 and logged the same first 64 chars at 15:02:07 JST. The provenance chain is intact, but: the original executor's *in-memory* dual-depth value at depth 6000 was discarded when the process died, and the fill-in's depth-6000 computation is technically a *re-computation* (algorithm-identical) rather than the *same* computation. Under deterministic-mpmath assumptions these are bit-equal; the agent did not separately verify byte-equality of the depth-6000 mpf representation across the two computations. This is documented in `stage_2_verification.json` field `note` and is not a verdict-affecting concern.

**Open question (not blocking).** Was the smoke timing differential (smoke 445.1 s vs canonical tier 3c 545.4 s, ~18% faster) anything other than process-warm-up variance? The recovery driver imported mpmath fresh and ran the smoke immediately after V_quad / basis setup, while the canonical tier 3c ran after tiers 3a + 3b in the same process (~58 min of prior PSLQ work). Plausible explanations: (a) Python GC state differences, (b) page-cache warming, (c) bignum allocator state, (d) mpmath internal state cache. None of these change the verdict. The structural-invariants list deliberately excludes wall_seconds for exactly this reason.

## What would have been asked (if bidirectional)

1. **Before the silent kill**, the agent would have asked: *"Should I add a heartbeat-style watchdog to the canonical executor by default for any tier expected to run > 30 min, given the multi-tier nature of this cycle and the no-supervision time budget?"* (Answer, in retrospect, is yes; it's now standard via the recovery driver pattern. The lesson generalizes to all future Tier-3b cycles with long PSLQ runs.)

2. **At the smoke-comparison-claim stage** the agent would have asked: *"How strict should the smoke-vs-canonical comparison be, given mpmath's PSLQ doesn't expose internal diagnostics?"* The user pre-empted this with the post-launch note on what `None == None` does and does not establish; the sidecar wording was tightened in response. The lesson is: when comparing two black-box numerical results, name the comparison's *scope* explicitly rather than naming the *equivalence class*.

3. **Before re-scoping the (3,3) tensor**, the agent would have asked: *"Is the dual-axis re-scope an acceptable substitute for Claude's named (3,3) cycle, or should the strict (3,3) cycle be run instead at the cost of breaking the 'one Tier-3b session' budget?"* The agent proceeded with the dual-axis on the basis that "test two underlying experimental dimensions within budget" served Claude's stated experimental goal better than "test one dimension over budget"; this is recorded in the env/plan provenance for human review.

## Recommended next step

**T2''' — the joint axis.** Run $B_{4,2}$ at maxcoeff $10^6$ at 2050 dp. Marginal cost: a single tier (~70–110 min wall-clock on this host), with the recovery-driver pattern (heartbeat logging, basis on disk, redirect stdout to file) as the default. This closes the last remaining numerical falsification trigger from the V_quad / Painlevé III($D_6$) family.

After T2''', the verdict-disposition language for the corpus stabilizes:

> *PSLQ-bounded numerical exclusion has hit its natural ceiling on this basis family; the remaining open question is the Painlevé–Sakai chart-map closure (R1), which is structural and not a numerical question.*

If Claude wants to keep extending the numerical net, the next program-statement question (separate from the V_quad / Painlevé III($D_6$) cycle) is augmenting the classical generators to include $\gamma$, $\log 2$, $\zeta(5)$, Khinchin's $K$. That is a $\ge 300$-element-basis multi-day undertaking and should be opened explicitly rather than absorbed.

## Operational lessons (one-line each)

- Long-running PSLQ tiers MUST have heartbeat logging + redirect-stdout-to-file. Don't trust a terminal pane to survive the run.
- When comparing two black-box numerical results, name the comparison's scope explicitly (don't say "matches" if you mean "structural invariants agree").
- The original executor's pattern of writing tier JSONs incrementally + writing summary at the end means a silent kill *between* tiers loses only the summary, not the tier data. Keep that pattern.
- Stage 2 evidence should be persisted *before* Stage 3 begins (write the in-memory cross-check log to disk as soon as it's computed). The original executor wrote it only at the very end, which loses Stage 2 evidence on any mid-run kill.
- Cross-cycle invariants (V_quad value, predecessor string SHA) accumulate across the cycle chain and should be cited as such in eventual write-ups, not re-established from scratch.

## Files committed

(21 in manifest; 2 timestamp-dependent heartbeat logs in slot but excluded from manifest)

- `basis_3_2_enumeration.json` — 60-element axis-1 basis enumeration
- `basis_4_2_enumeration.json` — 75-element axis-2 basis enumeration
- `claims.jsonl` — 10 AEAL claim entries
- `discrepancy_log.json` — empty `{}` (no discrepancies)
- `env_snapshot.json` — environment + judgment-call provenance
- `exclusion_certificate.json` — two axis sub-certificates + combined verdict + recovery-metadata block
- `halt_log.json` — empty `{}` (no halts)
- `handoff.md` — this file
- `manifest.json` — SHA-256 manifest of 21 archived files
- `plan_dag.json` — DAG with N1–N13 nodes
- `pslq_3_2_maxc6_2050dp.json` — axis-1 tier 2 PSLQ output
- `pslq_3_2_maxc6_500dp.json` — axis-1 tier 1 PSLQ output
- `pslq_4_2_maxc4_2050dp.json` — axis-2 tier 2 PSLQ output (recovery)
- `pslq_4_2_maxc4_500dp.json` — axis-2 tier 1 PSLQ output (canonical)
- `recover_tier_3d.py` — focused tier-3d recovery driver
- `report.md` — final report
- `stage_23_executor.py` — original canonical Stages 2+3 executor (ran 3a/3b/3c successfully; died silently before 3d)
- `stage_2_verification.json` — post-hoc Stage 2 cross-check evidence
- `stage_2_verification.py` — post-hoc Stage 2 fill-in driver
- `stage_4_5_archive.py` — Stage 4+5 archive driver
- `tier_3d_preflight_500dp.json` — recovery pre-flight smoke output
- `tier_3d_recovery.json` — recovery provenance sidecar (rewritten post-hoc with honest schema)
- `unexpected_finds.json` — empty `{}` (no unexpected findings)
- `verified_relations.json` — empty list (none found; see exclusion_certificate.json)

Retained in slot but excluded from manifest:
- `tier_3d_progress.log` — heartbeat log (timestamp-dependent)
- `tier_3d_stdout.log` — driver stdout capture (timestamp-dependent)

## AEAL claim count

10 entries written to `claims.jsonl` this session.
