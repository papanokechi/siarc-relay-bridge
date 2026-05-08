# Handoff — T2-113-COPILOT-RESEARCHER-PROMPT-DRAFT-125

**Date:** 2026-05-08
**Agent:** GitHub Copilot CLI (claude-opus-4.7-xhigh)
**Session duration:** ~25 minutes (drafting + bridge deposit)
**Status:** COMPLETE

## What was accomplished

Drafted SIARC relay prompt 113 for a Copilot Researcher (T2 executor)
to consolidate the §10 Route F substrate from Sakai 2001 + KNY 2017
§8.5.17 + 058R Phase B canonical map into a single paste-ready
markdown packet. The packet, once produced by the executor, will be
dispatched by the operator into a fresh Claude.ai T1-Synth
conversation to re-fire question Q4 of the 069r3 FINAL synthesis
verdict (currently HEDGE_ROUTE_F at MEDIUM-HIGH confidence,
substrate-paste-pending).

Prompt deposited at
   tex/submitted/control center/prompt/
   113_t2_069r3_priority_1_s10_route_f_substrate_consolidation.txt
SHA `A64224FD7DD5FD81` (16-prefix); 25,163 B; ~470 lines.

This bridge session deposit (sequential 125) records the prompt's
existence + substrate-source SHA inventory + 5 pre-fire watch-list
items that the executor should be aware of at fire time.

## Key numerical findings

Not applicable — this is a prompt-draft session. No numerical
computation. Substrate-source SHA inventory captured in claims.jsonl
(6 entries, all evidence_type literature/structural).

| Source | Path (truncated) | SHA-16 |
|---|---|---|
| Prompt 113 | `prompt/113_t2_*.txt` | `A64224FD7DD5FD81` |
| S1 W((2A_1)^(1)) extract | `2026-05-04/SIARC-PRIMARY-W-HOM*/extract_sakai_2A1_generators.md` | `2CC9395BFF74B1C4` |
| S2 KNY 2017 .txt | `g3b_2026-05-03/14_kajiwara_noumi_yamada_2017_*.txt` | `AAA2B0958F22BB03` |
| S3 Sakai 1999 PDF | `g3b_2026-05-03/13_sakai_1999_preprint_kyoto99_10.pdf` | `EC1BBDA3B77634E6` |
| S4 058R Phase B | `2026-05-06/CC-VQUAD-PIII-NORM*/phase_b_canonical_map.md` | `F831F9BD58D1F306` |

## Judgment calls made

1. **Task tier classification.** Chose T2-OPERATOR over T1-OPERATOR
   for the embedded executor task ID, on the rationale that this is a
   substrate consolidation (mechanical extraction + verbatim quoting)
   rather than a structural derivation. The task does NOT cross the
   T1 threshold of needing synth-tier reasoning. Mirrors precedent
   105 prompt structure but at lighter operational tempo.

2. **Substrate burden estimate corrected.** Prompt 112 §10 framed
   the substrate-paste burden at "~30-90 min including potential ILL
   acquisition". On-disk audit revealed all 4 sources present,
   reducing the estimate to "30-60 min consolidate-and-paste only".
   Corrected estimate stated explicitly in prompt 113 §1 KEY
   OPERATING FACT block. Documented under UF-125-2.

3. **Item (iv) deliverable scoped to PARTIAL.** The full pull-back
   of W((2A_1)^(1)) action onto (η_∞, η_0, θ_∞, θ_0) is a structural
   derivation, not a substrate quote. Scoping (iv) to PARTIAL —
   provide raw materials side-by-side, intentionally defer the
   pull-back to synth — preserves the agent-as-substrate-curator
   role and prevents executor scope-creep into synth's domain.
   Section §2 D5 + §8 N1-N3 enforce this scope discipline. Watch-
   list documented under UF-125-1.

4. **No bibliographic-pre-verification halt for Sakai DOI.** Per
   custom_instructions standing rule (post-031 verdict), DOIs and
   arXiv IDs must be pre-resolved before any relay prompt fires that
   cites them as acquisition targets. For prompt 113, the Sakai
   1999 Kyoto preprint is the substrate anchor (SHA `EC1BBDA3...`),
   NOT the published Springer DOI 10.1007/s002200100446. The on-
   disk preprint SHA is the canonical anchor; published DOI
   resolution is only required if a peer-reviewable artifact later
   cites the published version. Documented in §4 G4.

5. **Cross-task SQL todo proposed.** Prompt 113 §7 C3 directs the
   executor to insert a follow-on todo
   `069r3-q4-route-f-rerun-synth-dispatch` depending on the
   executor's task-id. This pre-stages the synth dispatch
   downstream of substrate consolidation; if Q4 returns NO_GO,
   that todo can be marked blocked and a path-delta-escalation todo
   added in its stead.

## Anomalies and open questions

(See unexpected_finds.json for the same items in machine form.)

1. **Scope-discipline watch (UF-125-1).** Prompt 113 §8 (N1-N6)
   carries an unusually heavy must-not-do block compared to peer
   prompts (e.g. 105). Justified by the load-bearing nature of Q4
   for M9 V0 critical path: any derivation slip (executor pre-
   classifying V_quad image as fixed-point or generic-orbit) would
   bias synth's Q4 verdict and could send the cascade down the wrong
   branch. Watch-list at fire time: the executor should scan for
   derivation language ('therefore', 'we obtain', 'computing this
   gives', 'it follows that') in non-quote prose before dispatch.

2. **Substrate burden correction (UF-125-2).** Documented in
   "Judgment calls" #2 above.

3. **Parameter-count alignment between KNY and Sakai (UF-125-3).**
   KNY uses (a_1, a_2) [3 free incl. a_0] for P_III(D_6) Hamiltonian;
   Sakai uses (a_0, a_1, b_0, b_1) with a_0+a_1=b_0+b_1=1 [2 free
   independent or 4 with two constraints]; CT v1.3 uses
   (η_∞, η_0, θ_∞, θ_0) [3 free under Okamoto null-sum]. Alignment
   requires either (i) one KNY parameter is the discrete shift
   orbit index (cf. eq 8.240) or (ii) one Sakai parameter is fixed
   by the surface choice. Acceptance criterion A8 directs the
   executor to surface this under UF-126-PARAM-COUNT if encountered.

4. **Preprint-vs-published version drift (UF-125-4).** Sakai 1999
   Kyoto preprint may differ from Comm. Math. Phys. 220 (2001) in
   equation numbering or Add-table layout. If executor needs cross-
   walk between preprint eq 16-18 and published eq numbers, document
   under UF-126-PREPRINT-PUBLISHED-DRIFT. Not blocking.

5. **Synth-bias prevention (UF-125-5).** Prompt 113 §3 S6 + §8 N4
   explicitly direct the executor to NOT include 069r3 FINAL
   handoff Q4 hedge text in the substrate packet. Rationale: synth's
   prior hedge ('MEDIUM-HIGH confidence Q4_HEDGE_ROUTE_F') could
   anchor the re-fire verdict toward hedging rather than decisive
   GO/NO_GO. The substrate paste must be SUBSTRATE-ONLY.

## What would have been asked (if bidirectional)

1. Confirm task tier classification (T2 substrate consolidation vs
   T1 substrate-plus-light-derivation). Defaulted to T2.

2. Confirm scope of item (iv): PARTIAL (substrate side-by-side, no
   pull-back) vs FULL (pull-back to (η, θ) included). Defaulted to
   PARTIAL per Judgment call #3 above.

3. Confirm output filename. Defaulted to
   `route_f_substrate_paste_packet.md` (descriptive +
   matches operator's mental model from the 8-step checklist
   delivered in the prior chat turn).

4. Confirm whether to add an explicit "no derivation" forbidden-
   phrase scan at Phase F (alongside the standing forbidden-verb
   scan). Defaulted to documenting as UF-125-1 watch-list item only,
   not adding a new mandatory scan, since the existing Acceptance
   criterion A4 + scope discipline §8 N1-N3 should be sufficient.

## Recommended next step

Operator fires prompt 113 in a fresh Copilot Researcher session
(VS Code Copilot CLI or equivalent). Expected fire time ~30-60 min.
Output: bridge deposit at
   sessions/2026-05-08/
   T2-OPERATOR-069R3-PRIORITY-1-S10-ROUTE-F-SUBSTRATE-
   CONSOLIDATION-126/
with primary deliverable `route_f_substrate_paste_packet.md`.

Once that lands, operator dispatches the packet to a fresh Claude.ai
T1-Synth conversation with the §2 D6 dispatch instruction line.
Expected synth turn-around ~10-15 min. Synth's Q4 re-fire verdict
then absorbs into a follow-on bridge session
(T1-SYNTH-069R3-Q4-ROUTE-F-VERDICT-ABSORPTION-127 or similar).

Branch:
- **Q4 = GO_ROUTE_F** → unblock
  `069r3-route-f-executor-envelope-draft` (Sakai surface-type
  machinery executor; ~8-20 hr novel-framework work)
- **Q4 = NO_GO** → escalate `path-delta` (JM 1981 Part II + Okamoto
  1987 + Sakai 2001 hybrid lit acquisition) OR pre-stage
  `governance-parallel-m9v0-amendment-draft` (M9 V0 with
  PARTIAL_NUMERICAL caveat)

## Files committed

- `113_t2_069r3_priority_1_s10_route_f_substrate_consolidation.txt`
  (the prompt body, 25,163 B / ~470 lines, SHA A64224FD7DD5FD81)
- `claims.jsonl` (6 entries: prompt SHA + 4 source SHAs + bridge
  ancestry)
- `halt_log.json` (empty `{}` — no halt triggered at draft time)
- `discrepancy_log.json` (empty `{}` — no discrepancy at draft time)
- `unexpected_finds.json` (5 entries: UF-125-1 through UF-125-5)
- `handoff.md` (this file)

## AEAL claim count

6 entries written to claims.jsonl this session.
