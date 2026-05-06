# P11 SICF Four-Options Decision — W20 Re-Fire

**Relay:** 049 (re-fire 2026-05-06 W20-Wed; original fire same date HALTED at
`HALT_049_JTNB_VERDICT_AWAITED`).
**Author:** GitHub Copilot (VS Code) — Claude Opus 4.7, in CLI-Synth in-tier
role under v2026-05-08 RACI Tier 2.
**AEAL class:** PROSE-DECISION (rule5 grounding required).
**Substrate files (this session):**
- `sicf_options_verbatim.md` — sha256
  `0AF25F0C2BC4E308E054DFE182AF593E015E824DA2F8F8FE7DCF246BDEDDC2DD`
- `sicf_options_scoring_matrix.json` — sha256
  `1049A94840F1793F61C164A553D567423760AF58E83F672C21F579F5C5BAE1BC`
- `jtnb_policy_snapshot.md` — sha256
  `7B41F5D318FC3B2A7F1B0AEB494D7117A0FA7E5C2F29462191097A051D15F513`
- SICF run anchor (auto-appended `claims.jsonl`, 2026-05-05 ~12:58 JST):
  sha256 `b3b339507ec0337e7217d426cacf0c64a9c94c37192ff76b813f6a3b750b3453`

**Operator-pasted preconditions (relay 049 §P3, this re-fire):**
- JTNB-2400 verdict status: `RECEIVED_NEGATIVE`
- JTNB verdict landing date: 2026-05-06
- Subtype: hard reject; verdict letter excerpt:
  > "After consideration, we feel that the content of the manuscript does not
  > meet the standards expected for publication in the journal."
- No referee comments accompanying the rejection (operator-confirmed "none").

---

## Decision

**Option 3: Withdrawal + restructure (resubmit).**

`selected_option_id = 3` in `sicf_options_scoring_matrix.json`.
Selection basis: `FORCED_BY_ELIMINATION` (Options 1, 2, and 4 are dominated
by the post-2026-05-06 hard-reject reality; Option 3 is the only LIVE option
under post-verdict scoring).

The "withdrawal" verb in the option label is moot under hard reject (the
JTNB rejection already removes the manuscript from JTNB's editorial pipeline);
the operative content of Option 3 is **restructure per the four SICF fatals
+ resubmit to a different venue**. Quantitative scoring from
`sicf_options_scoring_matrix.json` `decision_summary`:

| Axis | Value (Option 3, post-verdict) |
|---|---|
| `manuscript_substance_preservation_pct` | 80.0 |
| `time_to_resubmit_days` | 21 |
| `aeal_rerun_cpu_hr` | 1.0 |
| `aeal_integrity_pct` | 97 |

---

## Rationale (substrate-only)

### Para 1 — Verdict landing collapses three of four options.

Under the operator-pasted verdict status `RECEIVED_NEGATIVE` (2026-05-06,
hard reject), the four options enumerated in `sicf_options_verbatim.md` §A
are subjected to a venue-state reality test. Option 1 ("No-op (wait for
referee verdict)") has no residual action surface: the verdict that the
no-op posture was waiting for has now landed. Option 2 ("Voluntary
corrigendum") is structurally infeasible: a corrigendum requires an
accepted-or-published host-journal version to attach to, and JTNB's hard
reject leaves no editorial relationship to leverage. Option 4 ("Hold for
JTNB-2400 leverage") was already partially degenerate at SICF authoring
time per discrepancy D3 inherited from 047 (P11 was JTNB-only after the
2026-04-28 Math.Comp desk-rejection; there was no parallel Math.Comp
submission to leverage against), and is fully dominated under the hard
reject (JTNB door closed; no leverage to hold). Per
`sicf_options_scoring_matrix.json`, Options 1, 2, and 4 carry status
`DOMINATED`; only Option 3 carries status `LIVE`.

### Para 2 — Option 3 substance-preservation under restructure-per-fatals.

Substrate from `sicf_options_verbatim.md` §A records Option 3's mechanics:
"Withdraw, address #1-#4 by reframing the theorem statements as
'T₁-relative' and the partition as 'conditional on basis-completeness',
resubmit. Cost: 2-3 weeks. Risk: 1 month of review queue restart." The
four Critic fatals from `sicf_options_verbatim.md` §C touch the rhetorical
strength of named theorems (Theorem 4.1's "exact counts" verbiage; the
basis-restricted "completeness" claim of the partition; Proposition 5.2's
Möbius identification justified only by ~10⁻²³⁸ numerical agreement;
Theorem 5.3's transcendence proof being conditional on an unproved exact
identity), but they do not invalidate any numerical content of the F(2,4)
classification. The 513,387 / 400,093 / 24 family counts stand at the
declared dps=500 / H_max=10¹² regime; the Trans-stratum locus ratios
{−2/9, +1/4} remain as computational facts; the Möbius numerical agreement
remains as PSLQ-grade evidence. The substance lost in Option 3 is the
named-theorem-grade strength of Theorem 5.3 (transcendence of K) and the
"completeness" rhetoric of the partition, both of which have explicit
reframing recipes in the option's verbatim text. The 80% preservation
estimate in `sicf_options_scoring_matrix.json` reflects ~20% loss in
named-theorem demotion + scope qualification, with all numerical content
preserved.

### Para 3 — Synthesizer framing aligns with elimination outcome.

Substrate from `sicf_options_verbatim.md` §B (synth-comment block,
2026-05-05 ~13:55 JST) records: "The right framing for that turn is:
which option preserves the most of the manuscript's structural
contribution while honestly addressing the four fatals, not which option
gets to 'submission_ready=True' fastest. Those are different
optimizations." The hard reject removes the "submission_ready=True
fastest" optimization from feasibility space (Options 1, 2, 4 dominated),
leaving Option 3 (the explicitly-fatal-addressing path) as both the
forced selection and the substrate-preferred selection on the
preservation axis. Substrate from `sicf_options_verbatim.md` §D records
the synth read on the four fatals, including the verbatim assessment that
"#18 (the 2-family discrepancy in Theorem 4.1: 26 vs 24+0+0) is a hard
arithmetic error. That alone forces withdrawal-or-correction regardless
of the other three." Under hard reject, "correction" via corrigendum
(Option 2) is infeasible; the residual feasible mechanism for #18 is
restructure via Option 3.

### Para 4 — AEAL chain integrity under Option 3 execution.

`sicf_options_scoring_matrix.json` axis-3 entry for Option 3 records
`{rerun_required: true, rerun_cpu_hr: 1.0, integrity_pct: 97}`. The
required reruns are: (a) reconcile #18 arithmetic via recount of the
Theorem 4.1 partition (26 = 24 Trans + 0 Log + 0 Alg leaves a 2-family
gap; the recount is bookkeeping, not new computation, and the underlying
sweep results in `claims.jsonl` are not invalidated); (b) re-anchor SHA
values for the restructured manuscript file. No PSLQ replays at dps=500,
no F(2,4) sweep re-execution, no Stage-A/B/C re-run is required by the
fatals as enumerated. The `aeal_integrity_pct = 97` reflects the small
recount + re-anchor delta; the AEAL chain integrity for downstream
manuscripts (PCF-1 v1.3, picture v1.18/v1.19) is unaffected by this
restructure because P11 is a stand-alone base-case manuscript, not an
upstream of those documents.

### Para 5 — Binding-window note carried forward.

`jtnb_policy_snapshot.md` §D and §E record that the JTNB
instructions-to-authors page returned no published "withdraw-and-resubmit
window" policy via web-fetch this session; the only published JTNB
constraint with submission-window semantics is the originality clause
(sicf_options_scoring_matrix.json `binding_window_note`). Under hard
reject, the relay-049 prompt's "JTNB withdraw-and-resubmit window
narrowing" framing reflects an operator-conceptual freshness window
rather than a journal-imposed deadline. The 30-day estimate adopted in
`sicf_options_scoring_matrix.json` is the conservative SICF-roadmap
freshness window: 4 fatals enumerated 2026-05-05, restructure dispatch
within 30 days keeps the fatal-fix mental model intact. This 30-day
figure is a JUDGMENT CALL, not a derived deadline; see Anomalies in
`handoff.md`.

---

## Binding-window posture

`binding_window_days_remaining = 30` (operator-conceptual SICF-roadmap
freshness window; not journal-imposed; see
`jtnb_policy_snapshot.md` §E and `sicf_options_scoring_matrix.json`
`binding_window_note`). Option 3 (selected) carries
`time_to_resubmit_days = 21` per verbatim cost (`2-3 weeks` in
`sicf_options_verbatim.md` §A). 21 ≤ 30, so Option 3 fits the
operator-conceptual window. No mitigations required for in-window
feasibility of the selected option.

---

## Operator dispatch checklist

Ordered by deadline (most urgent first):

1. **CMB.txt update — JTNB verdict landing.** Update `tex/submitted/CMB.txt`:
   (a) §PORTFOLIO STATUS L24 P11 row: status `Submitted` → `Rejected`.
   (b) §VERDICTS RECEIVED (L739-820): append entry for JTNB-2400,
   Adamczewski, 2026-05-06, RECEIVED_NEGATIVE, with the rejection-letter
   excerpt verbatim.
   (c) §VENUE STATUS L59-60: replace "Submitted to JTNB 28 Apr 2026" with
   "Rejected by JTNB 6 May 2026 (handling editor: Boris Adamczewski);
   manuscript exiting JTNB editorial pipeline."
   (d) Append SYNTH-TRACK block recording this 049 re-fire decision (see
   §STEP 5 in `handoff.md`).

2. **CLI daily log SYNTH-TRACK append.** Append a SYNTH-TRACK section to
   `cli_log/2026-05-06.md` recording: bridge folder, decision Option 3,
   substance-preservation estimate 80%, binding-window posture, and
   re-fire-vs-original-049-halt audit pointer to
   `sessions/2026-05-06/P11-SICF-DECISION-W20/handoff.md`.

3. **Restructure plan dispatch.** Within 30-day SICF-roadmap freshness
   window (see Binding-window posture above): plan the restructure work
   per the four-fatals reframing recipes from
   `sicf_options_verbatim.md` §A. The recommended substrate is the four
   SICF fatals + Minor #18 + reframable items {#7, #11} in
   `sicf_options_verbatim.md` §C/§D and the existing manuscript at
   `tex/submitted/f1_mathcomp_submission/main_R1.tex` (sha256 captured
   in `sessions/2026-05-06/P11-COVERLETTER-MATHCOMP-DEFENSIVE/`
   `final_anchor_hashes.json`).

4. **Venue selection for resubmission.** Candidate venues (operator
   discretion; not selected here): Acta Arithmetica, Manuscripta
   Mathematica, International Journal of Number Theory, Mathematika.
   Constraints: arithmetic-CF / Painlevé-resurgence scope alignment;
   acceptance of computer-assisted classification papers; 6-12 month
   review-cycle horizons.

5. **Cover-letter substrate reuse.** The 2026-05-06 defensive cover
   letter at `sessions/2026-05-06/P11-COVERLETTER-MATHCOMP-DEFENSIVE/`
   (originally drafted for Math.Comp re-submission) is a candidate
   substrate for the new venue's cover letter; per its handoff §"What
   was accomplished", the letter is venue-agnostic in §1 (paper subject)
   and venue-specific in §2 (positioning). §2 will need re-writing for
   the chosen venue.

6. **Pre-resubmit gate — SICF re-run.** Once the restructure draft lands,
   re-run the SICF arbitrator (`sicf-review-system/sicf.py`) on the
   restructured manuscript with paper-id `P11-v2` to verify all four
   fatals are addressed. If consensus rises above 7.0 with critic ≥ 6.0,
   resubmit; if not, second-round restructure.

7. **AEAL anchor refresh.** Post-restructure: re-anchor `claims.jsonl`
   entries that cite the manuscript SHA. No sweep recomputation expected.

---

## Discarded options (audit trail)

### Option 1 — No-op (wait for referee verdict).

Status: `DOMINATED`. Per `sicf_options_scoring_matrix.json` Option 1
post-verdict scoring: `axis_1_substance_pct = 0` because the wait-state
has zero residual action surface — the JTNB editorial verdict has now
landed (RECEIVED_NEGATIVE, 2026-05-06), so there is nothing left to wait
for. Substrate basis: hard-reject letter excerpt from operator paste this
session (rejection language verbatim quoted in §"Operator-pasted
preconditions" above). Rejection.

### Option 2 — Voluntary corrigendum.

Status: `DOMINATED`. Per `sicf_options_scoring_matrix.json` Option 2
post-verdict scoring: `axis_1_substance_pct = 0` because a corrigendum is
a publication-mechanism that requires an accepted-or-published host-journal
version to attach to. JTNB's hard reject (rejection language: "the
content of the manuscript does not meet the standards expected for
publication in the journal") leaves no editorial relationship to leverage,
no published version to correct, and no acceptance-pending state to
amend. Rejection.

### Option 3 — (selected, see Decision above).

### Option 4 — Hold for JTNB-2400 leverage (cross-venue strategy).

Status: `DOMINATED` (under post-verdict reality) AND `DEGENERATE` (under
inherited 047 D3 venue-labelling-drift correction). Per
`sicf_options_scoring_matrix.json` Option 4 venue-labelling-drift note:
the option was authored under the assumption of a parallel Math.Comp
submission to leverage against, but P11 was actually JTNB-only at SICF
authoring time (Math.Comp desk-rejected 2026-04-28; resubmitted same day
to JTNB-2400). Under D3 correction the option reduces to "wait for JTNB
referee", which is structurally equivalent to Option 1 and inherits
Option 1's domination. Under hard reject, the JTNB door closes and no
cross-venue leverage remains. Rejection.

---

## End of sicf_decision.md
