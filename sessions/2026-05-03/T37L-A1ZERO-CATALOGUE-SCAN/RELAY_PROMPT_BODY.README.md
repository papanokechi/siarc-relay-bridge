# RELAY_PROMPT_BODY — T37L-A1ZERO-CATALOGUE-SCAN (A2)

This is **paste-ready** (no edits needed). Fire by pasting `RELAY_PROMPT_BODY.txt`
into a fresh Copilot CLI session as the first user message.

## Pre-flight checklist

- [ ] Fresh CLI session (no prior turns).
- [ ] Working dir = `C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat`
      (not the bridge — the bridge is git-only).
- [ ] Bridge repo is reachable (`git -C siarc-relay-bridge fetch origin` works).
- [ ] Anchor sessions exist on bridge from prior runs:
      - `sessions/2026-05-02/T37F-Q18-NUMERICAL-PROBE/`
      - `sessions/2026-05-02/T35-STOKES-MULTIPLIER-DISCRIMINATION/`
      - `sessions/2026-05-02/T37E-EXTENDED-RECURRENCE/`
      - `sessions/2026-05-02/T37-S2-EXTRACTION-POLYNOMIAL-AWARE/`

## Provenance

- Source: `tex/submitted/control center/prompt/017L_t37L_a1zero_catalogue_scan.txt`
- Modifications applied for paste-ready firing:
  - `<TODAY>` → `2026-05-03` (2 substitutions)
  - B4 push step: added rebase-fallback for parallel-fire concurrency:
        `git pull --rebase origin main && git push` (one retry max)
- SHA-256: see `RELAY_PROMPT_BODY.sha256`

## Parallel-fire context

This is part of the **A1+A2+A3 parallel triple** fired 2026-05-03:
- A1 = QS-2 (`D2-NOTE-V2-1-WASOW-FULL-CLOSURE/`) — already running
- **A2 = THIS PROMPT (T37L)** — fire next
- A3 = T37M (`T37M-DIRECT-BOREL-D-EXTRACTION/`) — fire ~15 min after A2

Output dirs are disjoint; reads are concurrency-safe. The B4 rebase
fallback handles the end-of-session push race.

## Compute budget

~1-2 hr CLI runtime. Algebraic enumeration via sympy + numerical
confirmation via mpmath dps=300. Single-laptop CPU.

## Expected outcomes

- `T37L_A1ZERO_CATALOGUE_DIM_K` — sub-stratum (iii) populated with K candidates
- `T37L_A1ZERO_SINGLETON_CONFIRMED` — QL09 is the unique a_1=0 rep
- HALT_*: see §4 of body
