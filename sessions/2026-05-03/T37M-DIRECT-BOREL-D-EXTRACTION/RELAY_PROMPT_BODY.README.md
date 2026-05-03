# RELAY_PROMPT_BODY — T37M-DIRECT-BOREL-D-EXTRACTION (A3)

This is **paste-ready** (no edits needed). Fire by pasting `RELAY_PROMPT_BODY.txt`
into a fresh Copilot CLI session as the first user message.

## Pre-flight checklist

- [ ] Fresh CLI session (no prior turns).
- [ ] Working dir = `C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat`
      (not the bridge — the bridge is git-only).
- [ ] Bridge repo is reachable (`git -C siarc-relay-bridge fetch origin` works).
- [ ] Anchor sessions exist on bridge from prior runs:
      - `sessions/2026-05-02/T37E-EXTENDED-RECURRENCE/`  (CRITICAL: a_n series cache)
      - `sessions/2026-05-02/T37-S2-EXTRACTION-POLYNOMIAL-AWARE/`
      - `sessions/2026-05-02/T35-STOKES-MULTIPLIER-DISCRIMINATION/`

## Provenance

- Source: `tex/submitted/control center/prompt/017m_t37m_direct_borel_d_extraction.txt`
- Modifications applied for paste-ready firing:
  - `<TODAY>` → `2026-05-03` (2 substitutions)
  - B4 push step: added rebase-fallback for parallel-fire concurrency:
        `git pull --rebase origin main && git push` (one retry max)
- SHA-256: see `RELAY_PROMPT_BODY.sha256`

## Parallel-fire context

Part of the **A1+A2+A3 parallel triple** fired 2026-05-03:
- A1 = QS-2 (`D2-NOTE-V2-1-WASOW-FULL-CLOSURE/`) — already running
- A2 = T37L (`T37L-A1ZERO-CATALOGUE-SCAN/`) — fire next
- **A3 = THIS PROMPT (T37M)** — fire ~15 min after A2

Output dirs are disjoint; reads are concurrency-safe. The B4 rebase
fallback handles the end-of-session push race.

## Compute budget

~2-3 hr CLI runtime. Borel transform + Padé approximants per rep
dominate; mpmath dps=400 + sympy + mpmath.pade. Single-laptop CPU.

## Expected outcomes

- `T37M_S2_EXTRACTED` — D extracted via Borel-Padé, |S_2| partitions Δ_b sign
- `T37M_NO_PARTITION_CONFIRMED` — Borel-Padé confirms no partition (S_2 closure foreclosed)
- `T37M_PADE_DIVERGENT` — Padé approximants do not stabilise (escalation needed)
- HALT_*: see §4 of body

## Why direct Borel-Padé (not Stage-2 LSQ)

017c (dps=250) and 017e (dps=400) both foreclosed the Stage-2 LSQ branch:
extracting an exp(−2ζ_* n) sub-leading from raw a_n requires projecting
out the leading exp(−ζ_* n) at amplitude ratio ~10^−2000 — infeasible at
any reasonable precision. Direct Borel-Padé locates singularities of
B[a_n](ξ) at ξ = 2ζ_* directly, bypassing the projection.
