# PCF-2 v3.x wording softening — decision tree (relay 055)

**Date:** 2026-05-06
**Author:** CLI-Synthesizer (T2 in-tier; v2026-05-08 RACI standard cadence)
**Class:** STRUCTURAL-ANALYSIS-SUBSTRATE (substrate-only; wording
           candidates enumerated, not selected)
**Companion:** `substrate_inventory.md`, `hypothesis_catalogue.md`,
              `t1_synth_question_set.md`

**Discipline note:** this file enumerates 4 candidate phrasings
(W1–W4) and their epistemic load. It does NOT select a candidate.
Selection is reserved for T1 Synth W20 weekly cadence (per
`t1_synth_question_set.md` Q3 / Q5). Forbidden framing verbs are
not used in candidate-prediction-or-conjecture contexts.

---

## §1 The current wording (verbatim source)

Per the 044B handoff section "PCF-2 v3.x WORDING SOFTENING (queued
for T1 Synth W20 weekly)" — the current PCF-2 v3.x wording (which
the 2-point softening replaces):

**FROM:** "b₇ is the only off-orbit n/log(2) data point"

**TO:** "b₇ and b₁₀ are the two known off-orbit n/log(2) data
points at h ≤ 10⁹ (sign-orbit + Bauer-shape Stage B at h ≤ 10⁷)"

The "FROM" wording is the v3.x baseline that the 044R OUTCOME B AT
H7 verdict and the 044B B-T-A clean result jointly soften. The "TO"
wording is the 044B-suggested phrasing.

This relay 055 enumerates 4 candidate phrasings around the 044B-
suggested target.

---

## §2 Candidate phrasings W1–W4

Enumerated in order of epistemic load (W1 weakest claim → W3
strongest claim; W4 reserves judgement). No ranking is implied by
order; all four are NOT FALSIFIED candidate phrasings at h ≤ 10⁹.

### W1 — DEFENSIVE / minimal

> "Two off-orbit n/log(2) data points are known at h ≤ 10⁹; their
> relationship is open."

**Epistemic load.** Minimal. No structural framing. No hypothesis
flag. Withholds even the "n=3 collision" framing.

**Where it sits.** Maximally conservative. Suitable if T1 Synth
treats the 2-point pair as a bare empirical observation pending
all arbitration outcomes (Q1–Q4).

**Trade-off.** Loses the "n=3 collision" empirical signal that
prompted relay 055 in the first place. Reads as if the operator is
unwilling to acknowledge the pattern even at the bare-empirical
level.

### W2 — SUBSTRATE-CITED / moderate (the 044B-suggested phrasing)

> "b₇ and b₁₀ are the two known off-orbit n/log(2) data points at
> h ≤ 10⁹ (sign-orbit + Bauer-shape Stage B at h ≤ 10⁷)"

**Epistemic load.** Moderate. Names the two anchors; cites the
sweep regime via h-bound qualifiers; does not assert a structural
identity. The h-bound qualifiers carry the same caveat as the 044R
verdict tag (`OUTCOME_B_AT_H7`, not bare `OUTCOME_B`).

**Where it sits.** Verbatim 044B suggestion. Suitable if T1 Synth
defers both Q1 and Q2 (no further probes fired) and accepts H_C
as default null at Q3.

**Trade-off.** Acknowledges the 2-point pattern at empirical level
but withholds any structural claim. Compatible with both H_BSW
and H_BFP being NOT FALSIFIED at h ≤ 10⁹ (does not preempt T1
Synth ranking).

### W3 — HYPOTHESIS-CITED / strong

> "b₇ and b₁₀ are the two known off-orbit n/log(2) data points at
> h ≤ 10⁹ (sign-orbit + Bauer-shape Stage B at h ≤ 10⁷); identity-
> vs-coincidence between b₇ and b₁₀ pending T1 Synth arbitration on
> Brouncker–Stieltjes–Wallis vs Bauer–Forrester pencil hypotheses."

**Epistemic load.** Strong. Names the two anchors; cites the
sweep regime via h-bound qualifiers; flags the open structural
question; cites the hypothesis pair (H_BSW vs H_BFP) without
selecting between them.

**Where it sits.** Suitable if T1 Synth fires Q1, Q2, or both
(further probes commissioned). The hypothesis flag prepares the
reader for a future v3.x.2 amendment carrying the H_BSW or H_BFP
falsification probe outcome.

**Trade-off.** Carries forward the structural framing into PCF-2
v3.x.1 prose. Risk: if both Q1 and Q2 probes fail to falsify
H_C, the H_BSW / H_BFP flag in W3 ages awkwardly. Mitigation: a
later v3.x.2 amendment lowers W3 to W2 if H_C survives.

### W4 — FORECAST-WITHHELD / weakest

> "b₇ and b₁₀ are the two known off-orbit n/log(2) data points at
> h ≤ 10⁹ (sign-orbit + Bauer-shape Stage B at h ≤ 10⁷); further
> sweeps deferred."

**Epistemic load.** Weakest in the sense of forecast-withhold. Names
the two anchors but adds nothing forward-looking. Cites the h-bound
qualifiers as in W2 / W3 but explicitly defers further sweeps.

**Where it sits.** Suitable if T1 Synth judges arbitration premature
(W20 weekly cadence may judge the 2-point pattern too thin to
commission probes; explicit defer flag carries forward to a later
weekly cycle).

**Trade-off.** Compared to W2: adds an explicit "further sweeps
deferred" forward-looking statement (operationally identical to W2
+ Q1 = defer + Q2 = defer). Compared to W3: replaces the
hypothesis-pair flag with a deferral flag.

---

## §3 Decision tree — wording selection conditional on Q1–Q5

Per `t1_synth_question_set.md` Q1–Q5. The selection table reads
the (Q1, Q2, Q3, Q4, Q5) joint outcome and recommends a wording
candidate.

| Q1 | Q2 | Q3 (if applicable) | Q4 (if applicable) | Q5 | Recommended W |
|----|----|-------------------|--------------------|----|---------------|
| defer | defer | accept H_C | n/a | amend now | **W2** |
| defer | defer | accept H_C | n/a | hold | W2 (deferred to v3.x.2) |
| defer | defer | reject H_C | n/a | amend now | **W4** |
| defer | defer | reject H_C | n/a | hold | W4 (deferred to v3.x.2) |
| fire | defer | n/a | fork-A | amend now | **W3** |
| fire | defer | n/a | fork-A | hold | W3 (deferred to post-probe v3.x.2) |
| defer | fire | n/a | fork-B | amend now | **W3** |
| defer | fire | n/a | fork-B | hold | W3 (deferred to post-probe v3.x.2) |
| fire | fire | n/a | fork-AB | amend now | **W3** |
| fire | fire | n/a | fork-AB | hold | W3 (deferred to post-probe v3.x.2) |

**Rationale (substrate-only).**

- **Q1 = Q2 = defer + accept H_C → W2.** The 044B-suggested
  phrasing without hypothesis flag; matches H_C as default null.
- **Q1 = Q2 = defer + reject H_C → W4.** Withholds structural
  framing entirely; matches "off-orbit data points subject to T2B
  Trans-stratum coincidence" framing without H_C-as-null
  commitment.
- **Q1 = fire ∨ Q2 = fire → W3.** Hypothesis flag flags the
  structural question forward to readers; matches the post-probe
  v3.x.2 amendment trajectory.
- **W1 not in table.** W1 is the maximally-defensive option; it
  is enumerated above as a fallback if T1 Synth wants a
  pre-arbitration wording weaker than W2 (e.g., for an early v3.x.0a
  hot-fix amendment that does not yet quote the 044B sweep regime).

---

## §4 Synth-tier default forecast (relay-055-time, NOT a T1 selection)

Per relay 055 STEP 5 prompt body, the synth-tier default forecast
at relay-055 draft time (substrate-only; T1 Synth ranks at W20
weekly):

- **W2** if Q1 = Q2 = defer (default null H_C accepted at Q3).
- **W3** if Q1 ∨ Q2 = fire (probe commissioned).
- **W4** if T1 Synth judges arbitration premature.

This is a **default forecast at relay-055 draft time**, not a T1
Synth selection. T1 Synth at W20 weekly cadence overrides freely.

---

## §5 Operator-side timing (Q5)

Q5 (Zenodo-amend timing) is operator-side, not T1-Synth-side. T1
Synth recommends timing as input to the operator decision. The
recommendation matrix in §3 above carries `amend now` and `hold`
columns; the difference is whether the W candidate enters PCF-2
v3.x.1 immediately (operator chooses based on portfolio cadence)
or waits for the post-probe v3.x.2 amendment to fold the Q1–Q4
outcome.

This concludes wording softening substrate. T1 Synth W20 weekly
cadence selects W1 / W2 / W3 / W4 conditional on Q1–Q5 outcomes
per §3 table.
