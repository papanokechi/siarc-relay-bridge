# Wrong-venue token decision — VQUAD-ZENODO-PREP-001 (Stage 4)

**Decision: forbidden-venue token = `Compositio` (case-sensitive substring).**
Secondary advisory token = `AAECC`. Both verified ABSENT from the current final
manuscript. **Do NOT use `JSC` / "Symbolic Comput" as a token** — citation
collision (see below).

## What the token is for

Sakai's playbook (Gate 2.2) pins a string for a venue *considered but not the
target*, and the gate confirms that string is ABSENT from the deposited PDF — a
tripwire that no stale venue-specific framing leaked into a venue-neutral Zenodo
preprint. Sakai used `ETNA`.

## V_quad venue history (from the parent slots)

| Venue | Role in planning | Source |
|---|---|---|
| **Compositio Mathematica** | **primary target**, priority-1 ("all 3 verify") | PERIOD-REP-VQUAD-002 dispositions.json L11; -003 ledger.json L111 "priority Compositio Mathematica" |
| JSC (J. Symbolic Computation) | "always-available backup; strongest CAS-context fit" | PERIOD-REP-VQUAD-003 paper-outline.md L94-96 |
| Math. Annalen / Constructive Approximation / Letters in Math. Physics | secondary alternatives | PERIOD-REP-VQUAD-002 dispositions.json L18/L25/L32 |
| AAECC | **not a target** — the Lecerf desk-reject *lesson* (CAS/SOTA paragraph) | PERIOD-REP-VQUAD-001 verdict.md L91; -003 paper-outline.md L96; memory Item-40 |

## Why `Compositio` is the chosen token

- It is the **dominant intended target** across every planning slot — the closest
  analog to Sakai's ETNA (the venue most associated with the paper in planning).
- A venue-neutral preprint must **not** name its target journal; if `Compositio`
  appears in the deposited PDF, target-venue framing leaked → exactly the tripwire.
- **Zero citation collision:** "Compositio" appears nowhere in the manuscript
  (body or bibliography) — verified 0 occurrences in `vquad-periodrep-paper.tex`.

## Secondary advisory token `AAECC`

- The desk-reject *lesson* venue (a sibling paper was desk-rejected there). If
  `AAECC` framing leaked into the body it would signal stale lesson-text.
- Also zero citation collision (no AAECC entry in the bibliography); 0 occurrences.
- Advisory only — the primary gate uses `Compositio`.

## Excluded: `JSC` / "Journal of Symbolic Computation" / "Symbolic Comput"

- **Citation collision.** The Kovacic 1986 reference legitimately prints
  "J.~Symbolic Comput. **2** (1986)…" at `vquad-periodrep-paper.tex` L1264.
- A gate keyed on "Symbolic Comput" would **false-positive** on this legitimate
  citation and HALT the deposit incorrectly. **Never use it as a forbidden token.**

## Current-state verification (informational; re-run on the FINAL corrected PDF)

Scanned `vquad-periodrep-paper.tex` (1352 lines):
- `Compositio` — **0 occurrences** (PASS).
- `AAECC` — **0 occurrences** (PASS).
- `ETNA` — 0 occurrences.
- only `submit` hit = "not yet submitted" (\thanks L46); only "Symbolic Comput"
  hit = Kovacic citation L1264 (legit).

The current draft is venue-neutral. Gate 2.2 should re-check `Compositio`
(case-sensitive) against the **final corrected PDF text** at deposit time.
