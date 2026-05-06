# T1 Synth W20 weekly question set — n=3 fourth-law arbitration

**Date:** 2026-05-06
**Author:** CLI-Synthesizer (T2 in-tier; v2026-05-08 RACI standard cadence)
**Class:** STRUCTURAL-ANALYSIS-SUBSTRATE (substrate-only; questions
           drafted, no answers proposed)
**Companion:** `substrate_inventory.md`, `hypothesis_catalogue.md`,
              `pcf2_v3x_wording_softening.md`
**Cadence:** input for T1 Synthesizer W20 weekly cadence (W20
           weekly fires no earlier than 2026-05-11 Sun close-of-week
           per relay 055 prompt body).

**Discipline note:** the questions below are framed without
ranking, scoring, "most likely" / "should" prescriptive language in
prediction-or-conjecture contexts, or forbidden framing verbs
("shows", "confirms", "proves", "establishes", "must"). Each
question takes a defer / fire / branch decision; T1 Synth selects
at W20 weekly cadence.

---

## Q1 — Higher-h sweep commissioning

**Question.**
Is the n=3 collision (A1 b₇ singular `(8, −4, 0, 7, 4)` ratio 8/49 +
A2 b₁₀ 044R outlier `(−9, 0, 0, 10, 5)` ratio −9/100, both yielding
L = 3/log(2) at h ≤ 10⁹) sufficient to motivate a new scan extending
h beyond 10⁹?

**Decision options.**

- **Q1 = fire.** Commission a 044C-style probe at h ≤ 10¹¹,
  b₁ ∈ {11, 12, 13, 14, 15} (avoiding ±6k = ±12 and ±18), b₀ ∈
  [−7, 7], allowing both Bauer-shape numerator (`a₂ = −k²`) and
  generic-numerator (`a₂ ∈ [−30, 30] \ {0}`) families. Fires the
  H_BSW falsification probe. Substrate-cited estimated runtime:
  ~30 minutes.
- **Q1 = defer.** Hold scan extension. Falsification of H_BSW
  remains pending future cadence.

**Decision input.** §1 + §2 anchor data, §3 coverage map (no third
anchor at h ≤ 10⁹ in b₁ ∈ {5, 7, 8, 9, 10}), and H_BSW
falsifying-probe specification in `hypothesis_catalogue.md`.

---

## Q2 — Quadratic ratio-pattern PSLQ commissioning

**Question.**
Is a quadratic ratio-pattern PSLQ scan over (a₂, b₁) of degree 2
warranted, given that the 044B linear fit `3·a₂ + 17·b₁ − 143 = 0`
satisfies neither the low-denominator threshold (max_abs_denom = 143
> 30) nor the underdetermined-fit guard (only 2 anchors)?

**Decision options.**

- **Q2 = fire.** Commission a quadratic PSLQ scan at degree 2 over
  the basis {a₂², a₂·b₁, b₁², a₂, b₁, 1} at the project low-
  denominator threshold (max_abs_denom ≤ 30) through anchors A1 +
  A2; sweep-test predicted-anchor locations. Fires the H_BFP
  falsification probe. Substrate-cited estimated runtime: ~45
  minutes.
- **Q2 = defer.** Hold quadratic PSLQ. Falsification of H_BFP
  remains pending future cadence.

**Decision input.** §2 NR3 (linear fit fails low-denominator),
hypothesis catalogue H_BFP falsifying-probe specification.

---

## Q3 — Default-null acceptance for PCF-2 v3.x wording softening

**Question (conditional on Q1 = defer ∧ Q2 = defer).**
Does T1 Synth accept H_C (numerical coincidence at h ≤ 10⁹) as
default null hypothesis for the PCF-2 v3.x wording softening?

**Decision options.**

- **Q3 = accept H_C as default null.** PCF-2 v3.x wording softens
  to "two known off-orbit data points at h ≤ 10⁹" (W2 candidate
  in `pcf2_v3x_wording_softening.md`) without a structural
  hypothesis flag.
- **Q3 = reject H_C as default null.** PCF-2 v3.x wording softens
  to "off-orbit data points subject to T2B Trans-stratum
  coincidence" (W4 candidate) — i.e., wording withholds a
  structural framing entirely while flagging the coincidence
  status as open.

**Decision input.** Q1 + Q2 outcome = (defer, defer); H_C
substrate citations in `hypothesis_catalogue.md` (044B B-T-A clean
result, max_abs_denom = 143 > 30 fail).

---

## Q4 — Probe prompt-spec body (conditional on Q1 = fire ∨ Q2 = fire)

**Question (conditional on Q1 = fire ∨ Q2 = fire).**
What is the prompt-spec body for the new probe T1 Synth drafts
for T3 dispatch?

**Decision options.**

- **Q4-fork-A: H_BSW probe only** (Q1 = fire ∧ Q2 = defer). T1
  Synth drafts a 044C-style sweep at h ≤ 10¹¹, b₁ ∈ {11, ..., 15},
  Bauer-shape + generic-numerator. Substrate-cited estimated
  runtime: ~30 minutes.
- **Q4-fork-B: H_BFP probe only** (Q1 = defer ∧ Q2 = fire). T1
  Synth drafts a quadratic-PSLQ probe through anchors A1 + A2 at
  max_abs_denom ≤ 30. Substrate-cited estimated runtime: ~45
  minutes.
- **Q4-fork-AB: both probes** (Q1 = fire ∧ Q2 = fire). Sequence:
  H_BFP first (faster, dependency-free; if a low-denominator
  quadratic exists, it sharpens the predicted-anchor list for
  the H_BSW probe), then H_BSW. Combined substrate-cited estimated
  runtime: ~75 minutes.

**Decision input.** Q1 + Q2 outcome (one or both fire); hypothesis
catalogue H_BSW / H_BFP probe specs.

**Drafting responsibility.** T1 Synth at W20 weekly cadence drafts
the prompt; T3 fires; this relay 055 substrate package does not
draft the prompt body.

---

## Q5 — PCF-2 v3.x Zenodo-amend timing

**Question.**
Should the operator Zenodo-amend PCF-2 v3.x to v3.1 (or v3.x.1)
with the 2-point softening IMMEDIATELY (not waiting for the Q1–Q4
outcome), or hold for arbitration outcome?

**Decision options.**

- **Q5 = amend now.** Operator Zenodo-amends PCF-2 v3.x to v3.x.1
  with the W1 (defensive) or W2 (substrate-cited) wording from
  `pcf2_v3x_wording_softening.md` immediately, capturing the
  044R + 044B verdicts as the rationale. Subsequent arbitration
  outcomes (Q1–Q4) are folded into a later v3.x.2 amendment.
- **Q5 = hold.** Operator defers Zenodo-amend until Q1–Q4
  arbitration completes (W2/W3/W4 selection conditional on
  outcomes). Single-amend covers all four arbitration outcomes
  and the 2-point softening together.

**Decision input.** PCF-2 v3.x current wording (per 044B handoff
"PCF-2 v3.x WORDING SOFTENING (queued for T1 Synth W20 weekly)";
verbatim From-To pair quoted in `pcf2_v3x_wording_softening.md`).

**Side note (operator-side).** This is an operator-side decision;
T1 Synth recommends timing but the operator dispatches.

---

## §A Recommended answer order

T1 Synth at W20 weekly cadence answers Q1, Q2, Q3, Q4, Q5 in that
order. The conditional structure is:

```
Q1 (defer | fire) ─┐
                   ├─→ if (Q1 = defer ∧ Q2 = defer): Q3 (accept | reject H_C)
Q2 (defer | fire) ─┤
                   ├─→ if (Q1 = fire ∨ Q2 = fire): Q4 (fork-A | fork-B | fork-AB)
                   │
                   └─→ Q5 (amend now | hold)         [unconditional]
```

Q5 is unconditional because the 2-point softening (b₇ singleton →
b₇ + b₁₀ pair) holds independent of whether further probes fire;
the Q1–Q4 outcomes only sharpen the wording strength (W1 / W2 /
W3 / W4 selection per `pcf2_v3x_wording_softening.md`).

---

## §B Substrate handoff to T1 Synth

T1 Synth W20 weekly cadence inputs are:

- This file (Q1–Q5).
- `substrate_inventory.md` (verbatim numerical anchors).
- `hypothesis_catalogue.md` (H_BSW / H_BFP / H_C without ranking).
- `pcf2_v3x_wording_softening.md` (W1–W4 candidate phrasings).

Adjudication is reserved for T1 Synth W20 weekly cadence.
