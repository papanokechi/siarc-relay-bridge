---
# Handoff — PRE-DRAFT-D2-NOTE-V2-1-WASOW-FULL-CLOSURE-PROMPT
**Date:** 2026-05-03
**Agent:** GitHub Copilot (VS Code) — Claude Opus 4.7 xhigh
**Task class:** synthesizer-side prompt drafting (NOT AEAL relay execution)
**Session duration:** ~50 min (across two pre-compaction phases + one post-compaction
                       rubber-duck-and-finalise phase)
**Status:** COMPLETE — `prompt_spec.md` ready for operator inspection
            and (post-inspection) firing as the QS-2 relay prompt
            `D2-NOTE-V2-1-WASOW-FULL-CLOSURE`.

## What was accomplished

Drafted the merged D2-NOTE-V2.1-WASOW-FULL-CLOSURE relay-prompt spec
(`prompt_spec.md`, ~75 KB / ~1 445 lines) per task
`PRE-DRAFT-D2-NOTE-V2-1-WASOW-FULL-CLOSURE-PROMPT`. The spec
embeds all four synthesizer Q-S rulings from picture v1.14 §24
(Q-S1 theorem-with-documented-residual elevated to theorem;
Q-S2 Path A revise-first / v2.1 on existing concept DOI 19996689;
Q-S3 merge with retired Prompt 7 / Wasow Q20 full-closure; Q-S4
no further amendment from this prompt's verdict) and applies
Rev-A through Rev-H minus Rev-C(b) and minus Rev-E full
(Rev-E PARTIAL only) per the same source. The spec is
SIARC-SOP-conformant and includes a ready-to-fire relay-prompt
body in a code block plus synthesizer notes outside the operator-
paste boundary. After draft, ran one full rubber-duck pass
(11 findings adopted: 5 HIGH, 6 MEDIUM, 1 LOW partially) and
applied the resulting fixes before push.

## Key numerical findings

- `prompt_spec.md` — 75 202 chars / 1 445 lines
- §0 CONTEXT, §1 ANCHOR FILES (A1–A6), §2 PHASES (0 / A / B / C / D / E / F),
  §3 AEAL CLAIMS MINIMUM, §4 HALT CONDITIONS, §5 FORBIDDEN-VERB
  HYGIENE, §6 OUTCOME LADDER, §7 STANDING FINAL STEP, §8 OUT OF
  SCOPE — all populated, no placeholders
- HALT keys defined: 9 distinct (`HALT_QS2_INPUT_INVALID`,
  `HALT_QS2_PHASE_A_STAR_DRIFTED`, `HALT_QS2_V2_PDF_DRIFTED`,
  `HALT_QS2_QSA_NOT_DONE`, `HALT_QS2_PEER_REVIEW_BRIEFING_MISSING`,
  `HALT_QS2_BIBKEY_COLLISION`, `HALT_QS2_LITERATURE_CHAIN_INCOMPLETE`,
  `HALT_QS2_BT_SCOPE_INSUFFICIENT`, `HALT_QS2_RADIUS_IDENTIFICATION_UNSUPPORTED`,
  `HALT_QS2_LEMMA_NOT_SECURE`, `HALT_QS2_BUILD_FAIL`,
  `HALT_QS2_PAGE_COUNT_DRIFT`, `HALT_QS2_REV_LANDING_INCOMPLETE`,
  `EPISTEMIC_LANGUAGE_DRIFT`)
- Outcome ladder branches: 4 (`UPGRADE_V2_1_FULL`,
  `UPGRADE_V2_1_PARTIAL_PAGECOUNT`, `UPGRADE_V2_1_PARTIAL`, `HALT_*`)
- AEAL claims minimum: ≥ 18 entries
  (≥ 14 carry-forward + ≥ 4 new for v2.1; "carry-forward" defined
   as new session-local claims with `output_hash` referencing the
   upstream Q20A baseline, NOT literal claim-ID copies)
- Page-count gate: [9, 12] for FULL; [7, 8] ∪ [13, 14] for
  PARTIAL_PAGECOUNT; X ≤ 6 or X ≥ 15 halts
- Rubber-duck findings adopted: 5 HIGH (filename-drift fix in E.0;
  PARTIAL_PAGECOUNT branch added; B-T sub-gates C.2.1–C.2.4 added;
  Phase B multiplicity-2 gloss softened with HALT_QS2_LEMMA_NOT_SECURE;
  prompt_spec.md provenance via Phase 0.0); 6 MEDIUM (B3 handoff
  template inlined; Tier-2 ethics gate added; bib-key collision
  preflight at Phase 0.5; Phase B → E insertion contract concretised;
  C.2 quote budget loosened; Rev-E "full" → "partial" typo fix); 1 LOW
  (forbidden-verb status table; AEAL carry-forward clarification;
  concurrency note tightened).

## Judgment calls made

1. **No rubber-duck before drafting**: I drafted the spec without
   first calling rubber-duck on the plan. After draft, I ran one
   rubber-duck pass and applied 11 of 14 findings. The Tier-2-quote-
   budget (#10) was simplified to "≥ 1 anchor quote per section,
   plus extras as needed" rather than a quantitative table — the
   spec already gives enough specific gating elsewhere. The
   AEAL-clarification (#13) was applied as a one-paragraph note
   in §3 rather than a schema rewrite.

2. **Tier-2 sources ETHICS-gated**: per rubber-duck #7, the relay
   agent does NOT add Loday-Richaud / Costin bib entries unless it
   has opened the file on disk and verified the chapter content
   (Phase C.4 ethics gate). Unconsulted Tier-2 sources are mentioned
   only in the relay session's handoff under Anomalies. This is a
   stricter standard than the original spec drafted (which permitted
   "see also" cites unconditionally if the PDFs were "available").

3. **Page-count band split**: rather than HALT on any clean build
   outside [9, 12] (the original draft), the revised spec branches
   to UPGRADE_V2_1_PARTIAL_PAGECOUNT for X ∈ [7, 8] ∪ [13, 14] and
   HALTs only at X ≤ 6 or X ≥ 15 (drastic out-of-band). This avoids
   forcing operator triage on a usable but mildly mis-paginated PDF.

4. **Phase B multiplicity-2 commentary OMITTED if not derivable**:
   the original draft included an interpretive parenthetical about
   the slope-1/d edge having "multiplicity 2" as the source of
   c = ±d/β_d^{1/d}. Per rubber-duck #4, this was softened: the
   Lemma statement no longer mentions multiplicity 2 (it just says
   "unique non-trivial slope-1/d edge"); the proof body explicitly
   tells the agent to OMIT multiplicity commentary if it cannot be
   derived directly from the lattice-point list and WKB balance,
   AND adds `HALT_QS2_LEMMA_NOT_SECURE` if a load-bearing step
   turns out to have a hidden subleading correction.

5. **Markdown wrapper around relay-prompt body**: the spec is a
   markdown document with a code-block containing the operator-
   paste body. The wrapper holds synthesizer rulings tables, a
   "How to fire" section, page-count budget commentary, and
   provenance — none of which the relay agent needs. The
   operator pastes only the code-block body into a fresh CLI
   session.

6. **Bridge-located, not in `tex/submitted/control center/prompt/`**:
   per task §4 step 2, this prompt's spec lives on the bridge
   (vs. prompts 004 / 017m which lived in the control-center prompt
   directory). This is a synthesizer-arbitrated convention shift:
   major Q-S–arbitrated tasks stage on bridge directly. The bridge
   path is `siarc-relay-bridge/sessions/2026-05-03/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/`.

## Anomalies and open questions  ← MOST IMPORTANT

1. **`D2-NOTE-V2-PEER-REVIEW` bridge session referenced but not yet
   committed**. The spec's §1 anchor A3 references
   `sessions/2026-05-03/D2-NOTE-V2-PEER-REVIEW/` as the canonical
   peer-review consolidation session, but I did not verify this
   directory exists in the bridge at draft time. The spec includes
   a fallback (`HALT_QS2_PEER_REVIEW_BRIEFING_MISSING`) AND embeds
   the 5-reviewer F1–F4 findings + composite mean directly in §0,
   so the relay can run cleanly even if A3 is missing. If Claude /
   the operator has not yet committed `D2-NOTE-V2-PEER-REVIEW`, this
   is the moment to do so (or to instruct me / a future session to).

2. **No live AEAL run by THIS task**. This is a synthesizer-side
   drafting task; I did not produce numerical claims, so
   `claims.jsonl` is NOT emitted by this session. The spec instructs
   the relay agent to produce its own claims.jsonl per §3, but no
   AEAL ledger is created here. (This is the standard pattern for
   synthesizer-side prompt drafting — cf. the absence of claims.jsonl
   in prior `prompt/` directory drafts at e.g.
   `tex/submitted/control center/prompt/004_*` etc.)

3. **Phase B Lemma proof — possible blind spot in WKB balance**.
   The Lemma proof B.2 derives `chi_d(c) = 1 - (β_d/d^d) c^d` from
   the WKB ansatz `f ~ exp(c/u)` with `z = u^d`, `theta = (u/d) d/du`.
   I have not personally verified that this leading-order balance
   has no hidden subleading correction (e.g., from the `z^2` term
   in eq. (1) at finite-d corrections, or from the `B_d(theta+1)`
   subleading coefficients). The Q20A Phase A* sweep verifies the
   Lemma numerically at d ∈ {2..10} with rel err < 1.6e-51, which
   is strong evidence — but the analytic derivation may need a
   careful re-read in the relay session. The spec adds
   `HALT_QS2_LEMMA_NOT_SECURE` to catch this if it surfaces.

4. **B-T 1933 §§4–6 scope is ASSUMED to cover the
   Borel-singularity-radius identification at distance |c|**. I
   added four sub-gates (C.2.1 summability, C.2.2 sectorial
   construction, C.2.3 radius identification, C.2.4 difference→ODE
   transfer) to verify this in the relay session. If sub-gate C.2.3
   fails (B-T 1933 supplies summability but not radius
   identification), the relay halts with
   `HALT_QS2_RADIUS_IDENTIFICATION_UNSUPPORTED` — operator triages
   by Tier-2 acquisition or Theorem 4.1 softening. This is a
   plausible failure mode that warrants explicit handling, hence
   the new sub-gate; whether the failure actually occurs is empirical
   and answered only at relay time.

5. **No synthesizer-side review of the spec by Claude before firing**.
   The spec was drafted by Copilot CLI alone, then critiqued by an
   in-session rubber-duck pass. It has NOT been forwarded to Claude
   (synthesizer) for an independent review. The synthesizer notes
   section in `prompt_spec.md` recommends operator forward to
   claude.ai for a synthesizer-review pass before firing. Recommended.

6. **Picture v1.15 amendment scope deferred**. Per Q-S4, this
   task's verdict is absorbed into picture v1.15 by a FUTURE
   synthesizer pass — out of scope for this drafting and for the
   QS-2 relay agent. The operator should remember to schedule
   v1.15 amendment after QS-2's verdict lands (post-relay-fire).

## What would have been asked (if bidirectional)

- "Should the QS-2 prompt include an explicit Tier-2 acquisition
  fallback (e.g., 'if C.2.3 fails, the relay agent attempts to
  acquire Loday-Richaud 2016 via Project Euclid before halting'),
  or is HALT_QS2_RADIUS_IDENTIFICATION_UNSUPPORTED the cleaner
  pattern?" — defaulted to halt; tier-2 acquisition is a separate
  G3b-style operator-side workflow per Rule 1 (no API keys / browser
  automation).
- "Should the prompt acknowledge the picture v1.14 → v1.15
  amendment cycle by writing a synthesizer-callout file
  `picture_v1_15_amendment_request.md` for the future synthesizer
  pass to find?" — defaulted to no; that would be over-prescription.
  The bridge session itself + handoff already serve as the
  synthesizer-callout once committed.
- "Should the relay session also produce a delta-PDF
  (v2 → v2.1 redline)?" — defaulted to no; the synthesizer can
  do that at picture-v1.15 time if needed; not required for v2.1
  Zenodo deposit.

## Recommended next step

1. **Operator action — inspection**: open
   `siarc-relay-bridge/sessions/2026-05-03/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/prompt_spec.md`
   and read the front matter + the relay-prompt body in the code
   block. Check that the embedded Q-S rulings match picture v1.14 §24.
2. **Optional — synthesizer review**: forward the prompt_spec.md to
   Claude (claude.ai) via raw GitHub URL for a synthesizer-side
   independent critique before firing. Recommended but not required.
3. **Operator action — fire**: paste the relay-prompt body (the
   text inside the ```...``` code block) into a FRESH Copilot CLI
   session in the `claude-chat` workspace. The agent will execute
   Phase 0 → Phase F per the spec.
4. **Pre-fire dependency check**: confirm SQL todo
   `g3b-acquire-bt-1933` is `done` (it is, per QS-A completion
   2026-05-03) and that slot 03 PDF is at the canonical path
   (it is, SHA `dcd7e3c6…68fe6`). The spec's Phase 0 re-verifies
   both gates at fire time.
5. **Post-fire**: at QS-2 completion, the operator deposits v2.1 as
   a NEW VERSION on Zenodo concept DOI 19996689 per the
   `zenodo_upload_d2_note_v2_1_runbook.md` produced by Phase F.3,
   and flips the SQL todo `prompt-d2-note-v2-1-wasow-full-closure-fire`
   to `done`. The merged-retired todo
   `prompt-7-wasow-q20-full-closure-fire` flips simultaneously.
6. **Post-deposit**: schedule a synthesizer-side picture v1.14 →
   v1.15 amendment pass to absorb QS-2's verdict (closes M9 gating
   reduction unconditionally if UPGRADE_V2_1_FULL).

## Files committed

- `prompt_spec.md`        (75 202 chars / 1 445 lines; the QS-2
                            relay-prompt spec — primary deliverable)
- `handoff.md`            (this file; synthesizer-side handoff for
                            Claude review of the drafting work itself,
                            distinct from the relay-execution handoff
                            which the relay session will produce)

## AEAL claim count

0 entries written to `claims.jsonl` this session.

This is a synthesizer-side prompt-drafting task; no numerical
computations were performed by the drafting agent itself. The
relay-execution session (post-fire) will produce its own
`claims.jsonl` with ≥ 18 entries per the spec's §3.
---
