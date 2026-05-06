# Rubber-duck QA on synthesizer-substitute Q1/Q2/Q4 draft

**Date.** 2026-05-06 ~16:55 JST.
**Dispatcher.** T2 (Copilot CLI), acting cross-tier as T1-Synth-substitute
per operator authorization.
**Mandate.** Operator instruction 2026-05-06 ~16:40 JST: *"double check
with a prompt for copilot researcher agent as necessary (in order to
avoid unexpected outcome and for quality assurance)."*
**Tool.** `task` agent_type `rubber-duck`, mode sync.
**Recommendation received.** **REVISE** (NOT adopt-as-is, NOT retract).

================================================================
## Rubber-duck verbatim recommendation
================================================================

**Final recommendation: REVISE**

### Blocking issues

**C1. `cf_value()` conclusion** — Verdict: Yes, the script implements
canonical `(1,b)` backward CF (`session_c1_wkb.py:79-86`); same pattern
in `session_b_pslq.py:162-168` and `quartic_tail_fit_all60.py:21-30`.
Strong evidence of protocol/stratum mismatch against
`pcf2_program_statement.tex:229-234` which declares
`a_n = δ_1 n + δ_0`. Fix: phrase as "harvested PCF-2 empirical scripts
for R1.1/R1.3/Q1 use `(1,b)` / `a_n ≡ 1`, despite the program
statement's linear-`a_n` declaration."

**C2. WZ analysis with `deg_a = 0`** — Verdict: Yes; from Phase A
general formula, balance (III) gives `μ = deg_a − deg_b`; with
`deg_a = 0`, `deg_b = d`, this gives `μ_sub = −d`, hence
`A_naive = d − (−d) = 2d` (`phase_a_summary.md:22-30`;
`bt_baseline_note.tex:344-348`). **Sign error in draft**: for balance
(III), `γ = −c_a/c_b`, so here `γ = −1/c_b`, not `+1/c_b`. Does not
change `A_naive` but matters for branch structure.

**C3. "Neither (i') nor (ii') is realised" is too strong** — Verdict:
The pivot overreaches.
- The **PCF-2 d=3,4 gap-framing** likely collapses under corrected
  `(1,b)` identification.
- But **(ii') definitional slippage remains live** because the actual
  scripts fit `log|delta_n|` with `delta_n = L_N − L_ref` / convergent
  residual, not `log|p_n/p_{n-1}|`
  (`session_c1_wkb.py:103-111`; `quartic_tail_fit_all60.py:35-44`;
  `pcf2_program_statement.tex:459-463`).
- Also, the **d=2 QL/V_quad split** is still a real empirical fact in
  the note (`bt_baseline_note.tex:467-489`), even if its explanation
  changes. Fix: revise Q1 to: "For PCF-2 R1.1/R1.3/Q1, the apparent
  d≥3 gap is likely a stratum/protocol mismatch first; mechanism (i')
  is not currently needed for those harvested scripts. Mechanism (ii')
  remains separately audit-worthy as an operational-definition
  question."

**C8. Confidence is overstated** — Verdict: HIGH justified for
script-level `(1,b)` mismatch and mechanical `deg_a=0 ⇒ A_naive=2d`,
but NOT for the full repo-level pivot. Use split confidence:
- HIGH: script/protocol mismatch
- HIGH: WZ plug-in `deg_a=0 ⇒ 2d`
- MEDIUM-HIGH: Section 5 of `bt_baseline_note` needs reframing
- MEDIUM: implications for PCF-1 / picture v1.20 / scope wording

### Non-blocking issues

**C4. Q4 independence** — Yes, Q4 remains live independently of Q1.
Even if the numerical gap dissolves, formal-to-analytic justification
is still a separate theorem-grade issue. Fix: change ranking to
"Wasow = canonical target / Costin = operational accessible substitute"
rather than a flat primary/secondary claim.

**C5. Blind spots** — Yes, three:
1. PCF-1 may use a different convention. `p12_journal_main.tex`
   defines the d=2 standard stratum with linear numerator
   `a_n = δ n + ε` (`p12_journal_main.tex:128-136`), while other repo
   code treats `V_quad` as a constant-`a` GCF
   (`algebraic_independence_audit.py:37-40`).
2. Seeds do not change the Newton polygon, but they can affect whether
   the observed residual exposes the subdominant branch/amplitude.
3. "Classifier mismatch" is close, but "protocol-to-stratum mismatch"
   is better, because the problem is not just labeling; the prose and
   scripts disagree.

**C6. AEAL wording** — Not fully. Phrases like "correctly predicts",
"matching exactly", "gap is artefact", "neither (i') nor (ii')" are
too absolute for a non-rerun arbitration note. Fix: use softer
AEAL-safe phrasing: "indicates", "is consistent with", "likely
reduces to", "pending Phase 3-A rerun".

### Suggestions

**C7. Defer canonical T1 Synth re-arbitration** — Yes. Given the
implications for `bt_baseline_note`, picture wording, and PCF-2 scope
language, an explicit note to re-arbitrate at canonical T1 weekly
cadence is prudent. Fix: add one sentence: "Because this finding
affects cross-document convention framing, canonical T1 Synth
re-arbitration next ISO week is recommended before any repo-wide
wording changes."

### Bottom line

The core technical finding is strong: the harvested PCF-2 scripts are
using `(1,b)` / `a_n ≡ 1`, and under that convention the normal-case
WZ baseline gives `A_naive = 2d`.

But the draft verdict should be revised before deposit because it
currently:
1. has a **sign error** in `γ`,
2. **overstates** the conclusion,
3. **over-generalizes** to PCF-1 / all of Section 5,
4. and **closes (ii') too aggressively** despite an actual fit-definition
   mismatch still needing audit.

================================================================
## Per-finding adoption record
================================================================

| Finding | Adopted? | How |
|---------|----------|-----|
| C1. `cf_value()` finding scoped to PCF-2 R1.1/R1.3/Q1 specifically | YES | Verdict explicitly scopes to "PCF-2 R1.1/R1.3/Q1 cubic+quartic harvest scripts"; PCF-1 substrate addressed separately under "Audited blind spots" §1. |
| C2. Sign error in `γ` for balance (III) | YES | Verdict's WZ analysis section now states `γ = −c_a/c_b ⇒ γ_sub = −1/c_b for c_a = 1` explicitly. |
| C3. Don't fully kill (ii'); leave audit-worthy | YES | Q1 verdict label changed to `PROTOCOL_TO_STRATUM_MISMATCH_FIRST_PIVOT`; verdict body explicitly states "Mechanism (ii') remains separately audit-worthy as an operational-definition question" with rationale. |
| C4. Q4 ranking softened | YES | Q4 verdict changed from "WASOW_PRIMARY_WITH_COSTIN_SECONDARY" to `WASOW_CANONICAL_TARGET_WITH_COSTIN_OPERATIONAL_SUBSTITUTE`; verdict body distinguishes "canonical target" (Wasow) from "operational substitute" (Costin) by accessibility, not strength. |
| C5. Three blind spots audited | YES | Audited blind spots section added covering PCF-1 convention (V_quad/QL01-QL26 split), seed independence, and classifier-vs-protocol-stratum naming. |
| C6. AEAL wording softened | YES | Replaced "correctly predicts" → "directly predicts" (mechanical-derivation context only); "matching exactly" → "is consistent with the empirical record … within σ"; "gap is artefact" → "likely reduces to the protocol-to-stratum mismatch"; "neither (i') nor (ii') is realised" → see C3 adoption. |
| C7. Defer canonical T1 Synth re-arbitration | YES | Dedicated section "Recommended canonical T1-Synthesizer follow-up (W20, Mon 2026-05-11)" with 6 specific items added. |
| C8. Split confidence | YES | Confidence assessment table with HIGH/MEDIUM-HIGH/MEDIUM splits per component. |

All 8 rubber-duck findings adopted in full. No findings rejected.

================================================================
## Pre-rubber-duck-critique draft (for diff/audit)
================================================================

The pre-revision draft Q1 verdict was **`STRATUM_MISMATCH_FIRST_PIVOT`**
(NOT `PROTOCOL_TO_STRATUM_MISMATCH_FIRST_PIVOT`); claimed
**"NEITHER (i') NOR (ii') is realised"** as absolute (now revised to
"likely unnecessary for harvested scripts"); used **"matching empirical
EXACTLY"** wording (now softened to "consistent with … within σ");
had `γ = +1/c_b` for balance (III) (now corrected to `γ = -1/c_b`);
ranked Q4 as **"WASOW_PRIMARY_WITH_COSTIN_SECONDARY"** (now revised
to canonical-target / operational-substitute).
