# P-009 M8b caveat — audit trail of all four tense-variants

**Task:** P009-M8B-CAVEAT-FINAL (relay 050; CLI-Synth in-tier; W20 P2)
**Date:** 2026-05-06 (Wed, W19→W20 transition; task fires under W20 priority)
**Author:** GitHub Copilot Tactical Executer (in CLI-Synth in-tier role for relay 050)
**Inherited from:** W19 SYNTH-QUEUE #4 → A.4 under RACI v2026-05-08
**Provisional language source:** relay 050 prompt (verb-check PASS as of
  2026-05-05; carried forward from CLI-Synth W19 drafting turn).

---

## 1. Provisional language (input to relay 050)

> "Stokes-multiplier discrimination (companion milestone M8b) supplies
> an additional independent test of the SIARC stratification at d≥3,
> conditional on the M8b dispatch landing within the relevant binding
> window."

The provisional uses the present-tense permitted verb "supplies", which
is the v3 (DISPATCHED_RESULT_POSITIVE) form. STEP 3 picks the active
variant matching the actual P3 status; the provisional is used as the
template into which v1/v2/v3/v4 verb-substitution and conditional-clause
adjustment is applied.

---

## 2. P3 — M8b dispatch status determination

Scope of the 050 short caveat: **Stokes-multiplier discrimination at
d≥3** (the d=2 numerical-extraction sub-branch was permanently
foreclosed at T37M HALT 2026-05-03 and is folded into the longer
P-008-bound caveat in CMB.txt L953–967, not into this 050 short caveat).

Status sources consulted (rule5 grounding, all reachable in-session):

- (a) `tex\submitted\CMB.txt` (most recent header, RACI v2026-05-08 INSTALL CLOSED 2026-05-05 ~20:18 JST):
    "M8b (foreclosed, caveat-only)" — refers to d=2 numerical only;
    "Synth P-009 M8b positioning ... on call" — d≥3 dispatch not fired.

- (b) 30-day `siarc-relay-bridge/sessions/` grep (2026-04-13 .. 2026-05-08):
    - `2026-05-03/STRATEGIC-PICTURE-REVISED-V14/picture_v1.14.md` — M8b at d=2 closed numerical paths (T37D PERMANENTLY BLOCKED, T37M).
    - `2026-05-04/MILESTONE-RESIDUAL-GAP-SURVEY-M4-M7-M8B-M9/` — literature sweep; Costin 2008 = S_1 only; BLMP 2024 = RH partial.
    - `2026-05-05/PROMPT-038-DOSSIER-ABSORB/` — M8b dossier absorbed; no d≥3 dispatch follow-on todo created.
    - `2026-05-05/P008-INPUT-PACKAGE-FOR-MSB-2026-06/` — A.4 substrate pinned for next monthly cycle.
    - `2026-05-08/RACI-V2026-05-08-INSTALL/STRATEGYZER_HANDOFF_2026-05-08.md` §A.4 — explicit "may finalize and slot this into the M9 V0 draft (P-008) when that work fires", i.e. dispatch not yet active.

- (c) `cli_log/2026-05-05.md` L141, L323; `cli_log/2026-W19_wsb.md` (W19 in progress):
    "P-008 (M9 V0 draft) and P-009 (M8b positioning) HELD pending operator confirmation"
    — no W19 dispatch fired for d≥3 M8b structural test.

**Verdict:** P3 = `NOT_YET_DISPATCHED` for the d≥3 binding-window dispatch
referenced by the 050 short caveat.

→ Active variant: **v1**.

---

## 3. Tense-variants (all four rendered)

### v1 — M8b NOT_YET_DISPATCHED (ACTIVE)

> Stokes-multiplier discrimination (companion milestone M8b) will
> supply an additional independent test of the SIARC stratification
> at d≥3, conditional on the M8b dispatch landing within the relevant
> binding window and on the binding-window result.

Verb form: `will supply` (permitted v1 form per relay 050 STEP 4 rule).
Conditional structure: dispatch + result (per v1 spec template).

### v2 — M8b DISPATCHED_AWAITING_RESULT

> Stokes-multiplier discrimination (companion milestone M8b) is
> expected to supply an additional independent test of the SIARC
> stratification at d≥3, conditional on the binding-window result.

Verb form: `is expected to supply` (permitted v2 form).
Conditional structure: result only (dispatch already landed).

### v3 — M8b DISPATCHED_RESULT_POSITIVE

> Stokes-multiplier discrimination (companion milestone M8b)
> supplies an additional independent test of the SIARC stratification
> at d≥3, per <BRIDGE_LINK_TO_M8B_VERDICT>.

Verb form: `supplies` (permitted v3 form).
Conditional structure: replaced by bridge-link citation to M8b verdict.
Operator paste-time substitution: replace `<BRIDGE_LINK_TO_M8B_VERDICT>`
with the literal bridge URL of the M8b verdict session
(e.g. `siarc-relay-bridge/sessions/YYYY-MM-DD/M8B-Dxx-VERDICT/handoff.md`).

### v4 — M8b DISPATCHED_RESULT_NEGATIVE

Caveat is REMOVED entirely from P-009 §discussion.
Replacement note (for transparency, placed where the caveat would
otherwise have appeared, or in the AI-disclosure / methodology
appendix):

> The Stokes-multiplier discrimination companion milestone (M8b)
> returned a negative binding-window result (per
> <BRIDGE_LINK_TO_M8B_VERDICT>); the corresponding d≥3 stratification
> test is therefore not currently supported, and no caveat to that
> effect appears in this manuscript.

---

## 4. Verb-check log (STEP 4)

Forbidden verbs (must not appear in prediction-or-conjecture context):
`shows`, `confirms`, `proves`, `establishes` (and root-stems
`show*`, `confirm*`, `prov*`, `establish*`).

Permitted verbs (per active tense-variant):
`will supply` (v1), `is expected to supply` (v2), `supplies` (v3).

| Variant | Forbidden hits | Permitted form found |
|---|---|---|
| v1 (active) | 0 | `will supply` ✅ |
| v2 | 0 | `is expected to supply` ✅ |
| v3 | 0 | `supplies` ✅ |
| v4 (caveat-removed note) | 0 | n/a — note explains M8b negative; no prediction-or-conjecture verb. |

**Result:** STEP 4 PASS for v1 (active). HALT_050_VERB_CHECK_FAIL not
triggered. Programmatic check executed via PowerShell regex on
`p009_m8b_caveat_active.txt` (Get-FileHash + Select-String style word-
boundary regex over forbidden + permitted lists; PowerShell session
log captured in `verb_check.log`).

---

## 5. Provenance / change log

| Step | Source | Action |
|---|---|---|
| 050 input | relay 050 PROVISIONAL CAVEAT block | source language captured here verbatim in §1 |
| STEP 1 | `tex\submitted\` directory listing | `tex\submitted\p009_*.tex` does not exist → branch (b) of STEP 1 (DRAFT_NOT_YET_STARTED → pin to control center) |
| STEP 2 | this file (§3) | four variants rendered |
| STEP 3 | §2 verdict (NOT_YET_DISPATCHED) | v1 selected as active |
| STEP 4 | §4 verb-check | PASS |
| STEP 5 | branch (b) operator-dispatch | see `operator_dispatch.md` |

---

## 6. Re-fire conditions

This caveat MUST be re-rendered (active variant re-selected) if any of:

- The M8b dispatch fires for d≥3 (status flips to DISPATCHED_AWAITING_RESULT
  → re-render under v2).
- The dispatch lands with a positive binding-window result
  (→ re-render under v3 with the verdict-bridge link substituted in).
- The dispatch lands with a negative binding-window result
  (→ remove caveat from P-009 entirely under v4 + add the v4
  explanatory note).
- P-008 schema-shifts such that the underlying provisional caveat
  itself is no longer valid (per CMB L953–998 audit recommendation:
  "Re-audit if P-008 schema-shifts").

If P-009 acquires a `tex\submitted\p009_*.tex` working copy before any
of the above triggers, STEP 1 branch flips to (a); the active text in
`p009_m8b_caveat_active.txt` is then pasted into §discussion
per `operator_dispatch.md` instructions.
