# Handoff — T2-M4-RATIFICATION-DOSSIER-ASSEMBLY-074
**Date:** 2026-05-07
**Agent:** GitHub Copilot (VS Code; Claude Opus 4.7 xhigh)
**Session duration:** ~40 minutes (single continuous run)
**Status:** COMPLETE
**Verdict:** DOSSIER_COMPLETE

## What was accomplished

Assembled a substrate-inventory dossier for W21 LANE-1 (Mon 2026-05-12
AM JST) M4 closure-path ratification. The dossier presents 5 primary
substrate sources (068 verdict + 072 CLEAN_EXTRACT + 073 CLEAN_EXTRACT
+ D2-NOTE v2.1 §4.5 + Adams §§1-2 + BT 1933 §§4-6 PDFs) plus 3
secondary substrate sources (073 ladder-map v2 + gap-status v2 + D2-NOTE
audit) all SHA-anchored to fire-time bridge HEAD `3410e5d`. A directed-
graph claim-chain ledger traces 068's verdict text back to 5 sub-claims
`[CLAIM-M1]` through `[CLAIM-M5]` plus 3 residual links `[LINK-C1]`
through `[LINK-C3]`. 18 residual questions are surfaced for synthesizer
weighing without proposing any answer. A synthesizer-ready dispatch
packet is drafted for W21 LANE-1 cadence consumption. Phase F.1 + F.2
self-checks PASS at zero hits / zero violations.

## Key numerical findings

This is a SUBSTRATE-INVENTORY-ASSEMBLY session, not a numerics session.
The substrate-counting findings are:

- Bridge HEAD at fire time: `3410e5d` (T1-PHASE-3-BT-1933-SECTIONS-4-6-
  READTHROUGH-073). Floor `3410e5d` MET. Recorded in claims.jsonl C1.
- 5 primary substrate sources `[SUBSTRATE-S1]` through `[SUBSTRATE-S5]`
  enumerated in `m4_substrate_inventory.md` §B.1; 3 secondary substrate
  sources `[SUBSTRATE-S6]` through `[SUBSTRATE-S8]` in §B.2; 5 explicit
  out-of-scope items in §B.3.
- Top claim `[CLAIM-M0]` decomposes into 5 sub-claims `[CLAIM-M1]` ...
  `[CLAIM-M5]` plus 3 residual links `[LINK-C1]` ... `[LINK-C3]`
  enumerated in `m4_claim_chain.md` §C.
- 18 residual questions `[Q-D1-1]` through `[Q-D4-4]` enumerated in
  `m4_residual_questions.md` §D (5 from 068 + 4 from 072 + 5 from 073
  with 1 M6.CC cross-reference-only + 4 from M4 spec invariants).
- Forbidden-verb scan: 0 literal hits across 5 deliverables under
  strict §5.E.2 token list `{asserts, proves, closes, demonstrates,
  establishes, ratifies}`. Recorded in `forbidden_verb_scan.md` F.1.
- Quote-length scan: 36 block-quotes total; max 48 words; zero
  violations of 50-word ceiling. Recorded in `quote_length_scan.md` F.2.
- AEAL claim count: 10 entries deposited in `claims.jsonl` (>= 8 floor).
- Halt evaluation: 0 of 10 envelope halts triggered; full enumeration
  in `halt_log.json`.

## Judgment calls made

The following decisions were made autonomously and were not specified
verbatim in relay prompt 074. Each is recoverable / overridable by W21
LANE-1.

1. **§1.B.1 100-word allowance vs §6+§7 50-word ceiling enforcement.**
   The relay prompt §1.B.1 specifies "verbatim quote ≤ 100 words from
   handoff §Verdict" while §7 envelope HALT_074_QUOTE_LENGTH triggers
   above 50 words. 074 enforces the tighter 50-word ceiling
   throughout; the 068 §Verdict verbatim quote at §B.1.1 / §C.1 / §E.2
   measures 41 words (under the tighter ceiling), so no content is
   trimmed. Surfaced as discrepancy D1 for synthesizer arbitration on
   future-cycle convention.

2. **B.1.1 strict-aligned to handoff §Verdict only.** First draft of
   `m4_substrate_inventory.md` §B.1.1 contained both the 068 handoff
   §Verdict quote AND a companion 068 phase_e_verdict_selection.md
   §E.2 quote. The §1.B.1 prompt-spec scope is the handoff §Verdict
   specifically, so the companion phase_e quote was removed. The
   synthesizer is invited to read 068 phase_e directly via the bridge
   URL for the analytic-content of the verdict.

3. **Adams 1928 PDF SHA cited verbatim from 072 handoff** rather than
   re-computed from workspace. Per upstream-substrate-inventory
   inheritance discipline; surfaced as discrepancy D5. The BT 1933 PDF
   SHA was independently re-computed and matches both 068 and 073
   anchors.

4. **§E.5 decision-tag labels (RATIFY / RATIFY_WITH_AMENDMENT /
   DEFER / OBJECT) preserved verbatim.** Per §5.E.1 prompt mandate.
   The bare-verb token "RATIFY" is not on the strict §5.E.2 forbidden
   3sg-present token list `{...ratifies}`; preserved as spec-required
   spelling.

5. **Single in-session edit to dispatch packet header for verb scope.**
   Initial draft of `w21_lane1_m4_dispatch_packet.md` header L8
   contained "T1-Synth (Claude.ai) ratifies" — a literal §5.E.2
   forbidden-token hit. Corrected in-session to "T1-Synth (Claude.ai)
   arbitrates" before sealing. Recorded in `forbidden_verb_scan.md`
   F.1.2 (zero post-edit hits).

## Anomalies and open questions

This is the most important section. 074 surfaces the following items
for W21 LANE-1 review (full enumeration in `unexpected_finds.json`
+ `discrepancy_log.json` + `m4_residual_questions.md`):

- **U1 — 5-source primary inventory aligns 1:1 with §1.B.1 spec**;
  the cumulative-cascade closure mechanism per 068 U4 is now
  structurally observable at the dossier level. Synthesizer may wish
  to consider whether picture v1.20 / RACI v2026-05-15 should
  formally recognise the cumulative-substrate-readback-cascade
  pattern as a first-class closure mechanism.
- **U2 — D2-NOTE v2.1 §4.5 is structurally load-bearing for the
  5-source inventory** even though 073 framed it as
  SUBSTRATE-INVENTORY-ONLY. Q-D3-1 (Borel-summability framing) becomes
  higher-priority when viewed at the dossier level.
- **U3 — MEDIUM-HIGH gating reduces to a single residual question
  Q-D4-1** (Wasow §X.3 OCR acquisition path). All other Q-D4-N items
  are forward-pointed downstream-of-ratification scope.
- **U4 — 18-question count is small enough for a single W21 LANE-1
  ratification session.** No multi-cycle split required.
- **D1 — §1.B.1 100-word vs §6+§7 50-word ceiling tension** (see
  Judgment Call 1).
- **D2 — picture v1.20 not deposited at fire-time HEAD** (Q-D4-3
  forwarded for synthesizer weighing).
- **D3 — 072 D4 RESOLVED scope (§§4-6 vs §§7-9 carry-over)** — the
  §§4-6 RESOLVED status is sufficient for 074 dossier scope; §§7-9
  readthrough is forward-pointed via Q-D3-4.
- **`Q-D3-5` chart-map-candidate cross-reference** — flagged as
  M6.CC scope (NOT M4) per envelope `HALT_074_M6_SCOPE_CREEP`
  discipline. Synthesizer is reminded that this entry is
  cross-reference-only and should not be conflated with M4 substrate.

## What would have been asked (if bidirectional)

1. "The §1.B.1 prompt-spec specifies '≤ 100 words from handoff §Verdict'
   for the 068 inventory entry while the §7 envelope halt
   `HALT_074_QUOTE_LENGTH` triggers above 50 words. Should the
   tighter 50-word ceiling apply throughout (the conservative reading),
   or should the 50-100 word band be permitted for the 068 verdict
   entry only (the literal §1.B.1 reading)?" — Resolved autonomously
   by enforcing the tighter 50-word ceiling throughout; surfaced as
   discrepancy D1.
2. "Picture v1.20 has a LATE-FIRE-PREFLIGHT (070, GO_PRIMARY_ONLY) but
   no v1.20 deposit at fire-time HEAD `3410e5d`. Should 074 anchor to
   v1.19 (the canonical spec at fire time) or wait for v1.20 to land?"
   — Resolved autonomously by anchoring to v1.19 with explicit Q-D4-3
   forwarding.
3. "Should the dispatch packet's §E.5 decision-tag labels be the bare-
   verb forms (RATIFY / DEFER / OBJECT) per §5.E.1 prompt mandate, or
   should they be reformatted into noun-phrase forms (e.g., 'ratification'
   / 'deferral' / 'objection') to fully avoid any verb form on the
   §5.E.2 list? — Resolved autonomously by preserving the spec-mandated
   bare-verb labels (which are not on the strict 3sg-present forbidden
   token list).

## Recommended next step

**For W21 (week of 2026-05-13) LANE-1 T1-Synth dispatch:**

Operator pastes the CLAUDE_FETCH URL of this 074 handoff to Claude.ai
synthesizer. The synthesizer is invited to read the dispatch packet at
`w21_lane1_m4_dispatch_packet.md` and then arbitrate one of the four
decision tags: RATIFY / RATIFY_WITH_AMENDMENT / DEFER / OBJECT. The
synthesizer may also wish to weigh the 18 residual questions
(`m4_residual_questions.md` §D) before issuing the decision tag.

**Forward-pointed dispatch recommendations (post-W21-arbitration):**

a. **PCF-2 v1.4 amendment cycle** (G12 jurisdiction, Q-D4-2): forward-
   pointed if synthesizer issues `RATIFY` or `RATIFY_WITH_AMENDMENT`.
b. **Picture v1.20 deposit cycle** (Q-D4-3): forward-pointed if
   synthesizer wishes M4 ratification absorbed in v1.20.
c. **Wasow §X.3 OCR acquisition** (Q-D4-1): forward-pointed if
   synthesizer wishes MEDIUM-HIGH → HIGH upgrade path.
d. **BT 1933 §§7-9 readthrough relay (075-class)** (Q-D3-4): forward-
   pointed by 073 itself; can fire in W21 LANE-2 parallel to LANE-1
   ratification arbitration.

## Files committed

All in `sessions/2026-05-07/T2-M4-RATIFICATION-DOSSIER-ASSEMBLY-074/`:

| # | File | SHA-256 (16-prefix) | Bytes |
|---|---|---|---|
| D1 | `m4_substrate_inventory.md` | `2C20A5F5A28327B2…` | 9591 |
| D2 | `m4_substrate_anchor_shas.md` | `2F25259344B77BEE…` | 12826 |
| D3 | `m4_claim_chain.md` | `A2188FC7140A5D34…` | 12055 |
| D4 | `m4_residual_questions.md` | `4C6A08761F06D075…` | 14170 |
| D5 | `w21_lane1_m4_dispatch_packet.md` | `B45B595A50A71D9C…` | 7387 |
| D6 | `forbidden_verb_scan.md` | `5F0DF31D2D1F7818…` | 6835 |
| D7 | `quote_length_scan.md` | `8ED3B056A6FF5680…` | 2882 |
| D8 | `handoff.md` | (this file) | — |
| D9 | `claims.jsonl` (10 entries) | `7618B533D6E20CD9…` | 4231 |
| D10 | `halt_log.json` | `B3BE6B71A9C5CA9B…` | 4370 |
| D11 | `discrepancy_log.json` (5 entries) | `1997802757BC81E4…` | 5311 |
| D12 | `unexpected_finds.json` (4 entries) | `1BFC40F6C5669089…` | 4195 |

Total: **8 deliverables (D1-D8) + 4 AEAL artefacts (D9-D12)** = 12 files.

## AEAL claim count

**10 entries** written to `claims.jsonl` this session (C1-C10).
HALT_074_AEAL_FLOOR (≥ 8) NOT TRIGGERED.

C1: bridge HEAD anchor; C2-C4: 068/072/073 handoff SHAs;
C5: 5+3+5 inventory entry count; C6: 5 sub-claims + 3 residual links;
C7: 18 residual questions; C8: forbidden-verb scan PASS 0 hits;
C9: quote-length scan PASS 36 blocks 0 violations; C10: dispatch
packet SHA + spec-mandated decision-tag labels.
