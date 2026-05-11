# T1-Synth Advisory Verdict — HALT_148E Remediation (PROMPT 194)

**Dispatch:** T1-SYNTH ADVISORY · off-cascade · single-witness LOW-MEDIUM
**Witness:** Claude (claude.ai web; Opus-class)
**Bridge antecedent:** `508d81c` (slot 148.E, 2026-05-11 ~20:23 JST)
**Verdict received:** 2026-05-11 ~20:45 JST
**Verdict absorbed by CLI:** 2026-05-11 ~20:48 JST
**Prompt source:** `tex/submitted/control center/prompt/194_t1_synth_halt_148e_remediation_consultation.txt` (6.2 KB)

---

## Q-194-1 — Recommended remediation path

**RECOMMENDED_OPT: OPT_X2** (move cache to fresh non-OneDrive directory).

Substantiation (verbatim): OPT_X1 attacks symptoms on a substrate that will keep generating them. The Windows `os error 5` at 7801/8399 decompressions is the signature of *concurrent* file-handle contention, not a single permission bit — and on `~\.cache\mathlib\` under OneDrive you have at least three independent contenders: OneDrive's file-virtualization layer (which can mark freshly-written files as cloud-only mid-extraction), Defender's real-time scan on .ltar/.olean writes, and the VS Code Lean server's lock on `.olean`/`.ilean` outputs. OPT_X1 mitigates each individually but leaves the OneDrive-sync substrate intact, so the next `lake update` (inevitable on mathlib bump) re-rolls the same dice. OPT_X2 removes the dominant variable (OneDrive virtualization) permanently; a Defender exclusion on `C:\lean-cache\` is still warranted but becomes a one-time hardening rather than a per-update ritual. The ~78 min re-download cost is regrettable but pays for itself on the next bump.

## Q-194-2 — Failure-mode ladder

1. **Next-best (if OPT_X2 still hits `os error 5`):** apply OPT_X1's hardening *on top of* the relocated cache — close VS Code, add `C:\lean-cache\` to Defender exclusions, ensure no OneDrive selective-sync rule reaches the new path, then `lake exe cache get!` again. This isolates whether the residual failures are Defender-only or something else.
2. **Last-resort (if 1 still fails):** invoke `leantar` decompression *serially* rather than via `lake exe cache get!`'s batched parallel calls — script a sequential loop over the 8399 `.ltar` paths. Slow (hours) but eliminates the concurrent-handle hypothesis entirely. If this also fails, the issue is filesystem-level (NTFS ACL inheritance, antivirus driver) and beyond reasonable Lean-axis ops scope.
3. **Declare-defeat:** fall through to OPT_X4.

**Earliest OPT_X4 decision point:** the moment step 2 (serial decompression) returns `os error 5` on a non-trivial fraction (say **>5%**) of `.ltar` paths. At that point the blocker is not a Lean-toolchain problem but a host-environment problem, and further ops investment has diminishing returns relative to advancing Frontier-A.

## Q-194-3 — Cross-axis prioritization

**PRIORITIZATION_RECOMMENDATION: (c) parallel** — operator runs FIRE-A2' Phase 0 substrate-prep in-CLI while OPT_X2 re-download/decompression runs in background.

Substantiation (verbatim): the two workstreams have no shared resource contention — FIRE-A2' Phase 0 is CLI-fireable and doesn't touch `lake`/`leantar`/`~\.cache\mathlib\`, while OPT_X2 is mostly wallclock-bound on download (~78 min) plus decompression (minutes-to-hours depending on serial vs parallel). Sequential ordering (a) wastes the download wallclock; pure-Frontier (b) accepts the M10 blocker as durable when it might be a one-shot ops fix. Parallel (c) hedges: if OPT_X2 lands within a few hours, M10 V0 lean-sorry discharge becomes fireable while FIRE-A2' is still mid-substrate; if OPT_X2 fails through the ladder, Frontier-A has already advanced and OPT_X4 becomes the natural fallthrough rather than a concession.

## Q-194-4 — Defer-Lean-axis acceptability

**ACCEPTABLE** (under stated conditions).

Substantiation (verbatim): (a) Deferring M10 V0 lean-sorry discharge does *not* violate any current cascade-132 / RULE 1 / M-axis obligation as the substrate is framed in the prompt — RULE 1 lift requires M10 closure as the *last* remaining hard SHA, not M10 closure *now*. The 4/4 hard SHAs already met from cascade-132 PATH_B are not invalidated by Lean-axis pause; they remain banked. M10 becomes the gating item whenever Frontier-A returns and operator wants to lift RULE 1, at which point the Lean axis must be reopened regardless. (b) Parallel cascade-vs-Lean-axis prioritization is consistent with standard SIARC discipline around independent-axis fires — the cascade architecture exists precisely so that an axis-local HALT doesn't propagate to unrelated axes. The discipline constraint to honor is explicit: when OPT_X4 is selected, M10-V0-lean-sorry-discharge must be tagged as a **RULE-1 lift gate** in the cascade ledger so the deferral is visible and the eventual lift attempt cannot proceed until M10 is reopened and closed. Provided that tagging is recorded at the bridge where the deferral happens, OPT_X4 is acceptable.

**Synth caveat:** "I'm reasoning from the substrate as stated and don't have independent visibility into whether any cascade-132 obligation has a *time-bound* M10 closure clause that I'm not seeing. If such a clause exists, that overrides this verdict and OPT_X4 becomes NOT_ACCEPTABLE."

---

**VERDICT_LABEL:** ADVISORY (no LOAD-BEARING math claim)
**CONFIDENCE_BAND:** LOW-MEDIUM
**NEXT_STEP_FOR_OPERATOR:** Initiate OPT_X2 (relocate cache to `C:\lean-cache\` with Defender exclusion, retry `lake exe cache get!`) in background while CLI-firing FIRE-A2' Phase 0 substrate-prep in parallel; promote to ladder step 1 → 2 → OPT_X4 per Q-194-2 decision points if OPT_X2 stalls.
