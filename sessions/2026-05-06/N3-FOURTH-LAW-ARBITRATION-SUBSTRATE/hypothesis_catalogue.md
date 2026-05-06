# Hypothesis catalogue — n=3 fourth-law-candidate arbitration (relay 055)

**Date:** 2026-05-06
**Author:** CLI-Synthesizer (T2 in-tier; v2026-05-08 RACI standard cadence)
**Class:** STRUCTURAL-ANALYSIS-SUBSTRATE (substrate-only; no ranking)
**Companion:** `substrate_inventory.md` (anchor data),
              `t1_synth_question_set.md` (question set),
              `pcf2_v3x_wording_softening.md` (wording decision tree)

**Discipline note (per HALT_055_RANK_DRIFT and HALT_055_FRAMING_DRIFT):**
the three hypotheses below are presented in the order H_BSW → H_BFP →
H_C without any ranking, scoring, or "most likely" language. Forbidden
framing verbs ("shows", "confirms", "proves", "establishes", "must")
are not used in prediction-or-conjecture contexts. T1 Synth ranks at
W20 weekly cadence.

---

## H_BSW — Brouncker–Stieltjes–Wallis-class identity

### Claim

A1 b₇ singular `(8, −4, 0, 7, 4)` and A2 b₁₀ 044R outlier
`(−9, 0, 0, 10, 5)` are both reductions of an underlying
Brouncker–Stieltjes–Wallis identity yielding L = 3/log(2) at the
integer n = 3 sector. The unifying structure under H_BSW is a
classical-CF identity (Brouncker triangle, Stieltjes-class
J-fraction, or a Wallis-class pi-product reduction), not a new
PCF-specific phenomenon.

### Substrate citations (already-existing AEAL-logged sessions)

- T2B-PLUS-QUARTER-SURVEY (sessions/2026-04-29/) — +1/4 sub-stratum
  enumeration. Brouncker-class identities at the sub-stratum
  4·a₂ − b₁² = 0 were enumerated in this session.
- T2B-STIELTJES-VERIFY (sessions/2026-04-29/) — Stieltjes-class
  follow-up at the +1/4 sub-stratum.

The 044R / 044B sweeps did not extend past b₁ = 10. The +1/4
sub-stratum substrate covers b₁ ∈ {≤ 10} at h ≤ 10⁷; b₁ ∈
{11, ..., 15} has not been swept under this hypothesis lens at
h > 10⁹.

### Predicted falsifying observation

A third anchor at higher b₁ (e.g. b₁ ∈ {11, 12, 13, 14, 15} avoiding
±6k = ±12 and ±18) extending the sign-orbit closure but unreachable
at h ≤ 10⁹ due to PSLQ cutoff. Under H_BSW one would anticipate at
least one further off-orbit n/log(2) hit at b₁ ∈ {11, ..., 15} when
the h-cutoff is raised to ≤ 10¹¹.

Falsifying observation: extend sweep to h ≤ 10¹¹ at b₁ ∈
{11, ..., 15}, b₀ ∈ [−7, 7], allowing both Bauer-shape numerator
(`a₂ = −k²` for k ∈ {2, 3, 4, 5}) and generic-numerator
(`a₂ ∈ [−30, 30] \ {0}`, a₁ ∈ [−5, 5], a₀ ∈ [−5, 5]) families. If
zero off-orbit n/log(2) hits surface, H_BSW receives a
non-trivial falsification signal at h ≤ 10¹¹.

### Falsification status

NOT FALSIFIED at h ≤ 10⁹. The 044R / 044B harnesses did not search
the b₁ ∈ {11, ..., 15} regime; absence of evidence at h ≤ 10⁷
inside the swept regime is not evidence of absence in the unswept
regime.

### Substrate-cited estimated probe runtime

Operator estimate (per relay 055 STEP 4 Q4): ~30 minutes agent
runtime at h ≤ 10¹¹, b₁ ∈ {11, ..., 15} on the 044B harness with
PSLQ_HMAX_TRANS lifted from 10⁷ to 10¹¹. This estimate is from the
055 prompt body and is not re-derived here.

---

## H_BFP — Bauer–Forrester pencil of orthogonal-polynomial relations

### Claim

A1 b₇ singular and A2 b₁₀ 044R outlier are non-Bauer points on a
pencil family interpolating Bauer-shape `(a₂, a₁, a₀) = (−k², 0, 0)`
and PCF generic moments-of-orthogonal-polynomials relations. The
unifying structure under H_BFP is a structural curve `f(a₂, b₁) = 0`
through both anchors of polynomial degree ≥ 2 (degree-1 already
excluded by the 044B integer-relation result `3·a₂ + 17·b₁ − 143 = 0`
which has max_abs_denom = 143 > 30).

### Substrate citations

- 044B STEP 3 (claim 044B-A4): linear ratio-pattern fit was
  attempted; quadratic and higher-degree PSLQ have not been
  attempted on the (a₂, b₁) → ratio relationship.
- T2B-RESONANCE-B67 / T2B-RESONANCE-B67-A50 (sessions/2026-04-29/):
  earlier b₆/b₇ resonance triangulation establishing the b₇
  singular geometry; not a pencil-search but provides the b₇ side
  of the Bauer-Forrester pencil substrate.
- Forrester-Witte 2005 (sessions/2026-05-04/WITTE-FORRESTER-2010-
  ACQUISITION/): SCENARIO_C analogue acquired during 031
  literature-hunt verdict; Forrester-Witte orthogonal-polynomial
  pencil substrate is in the 031 acquired bibliography.

### Predicted falsifying observation

A quadratic PSLQ scan for an `(a₂, b₁)` relation of the form

> α·a₂² + β·a₂·b₁ + γ·b₁² + δ·a₂ + ε·b₁ + ζ = 0

(or with `(a₂/b₁²)` ratio variable, depending on T1 Synth's
parameterization choice) exact through both anchors yields a
1-parameter family of curves (since 6 unknowns minus 2 anchor
constraints leaves 4 free parameters; further dimension reduction
under degree ≤ 2 + max_abs_denom ≤ 30 may reduce this to a finite
set). Each candidate curve in the family predicts a third anchor
location; sweep-test each predicted anchor at h ≤ 10⁹.

Falsification: zero predicted-anchor locations from the quadratic
PSLQ family hit n/log(2) at h ≤ 10⁹.

### Falsification status

NOT FALSIFIED. The 044B STEP 3 ratio-pattern fit was LINEAR only.
Quadratic and higher-degree PSLQ on (a₂, b₁) has not been attempted
under this hypothesis lens.

### Substrate-cited estimated probe runtime

Operator estimate (per relay 055 STEP 4 Q4): ~45 minutes agent
runtime with PSLQ at degree 2 over (a₂, b₁) ∪ {a₂², a₂·b₁, b₁², 1}
at the project low-denominator threshold (max_abs_denom ≤ 30) plus
a sweep-test at one or two predicted-anchor locations.

---

## H_C — Numerical coincidence at h ≤ 10⁹

### Claim

A1 b₇ singular and A2 b₁₀ 044R outlier both yielding L = 3/log(2)
at h ≤ 10⁹ is a numerical accident at bounded h that does not
extend to a structural unifying law. The 044B B-T-A clean result
(no new off-orbit anchors at the bounded h-levels swept) and the
absence of a low-denominator straight-line ratio-pattern through
the 2 anchors are CONSISTENT with this hypothesis (though
consistency is not adjudication).

### Substrate citations

- 044B verdict B-T-A (claim 044B-A6, output_hash
  `8be42dd2d5ca3c36b4ac8dabfb3c993f209442f455089fe6aa37749f4b2562e0`):
  new_off_orbit_hit_count = 0 after Bauer-shape sub-locus + sign-
  orbit closure swept.
- 044B STEP 3 (claim 044B-A4): max_abs_denom = 143 on the linear
  fit `3·a₂ + 17·b₁ − 143 = 0`; fails the project low-denominator
  threshold of 30.
- 044B handoff Anomalies §"NO structural identity claimed": the
  044B harness disclaims structural identity in claims 044B-A4 and
  044B-A5; the structural-identity question is a T1 Synth question.

### Predicted falsifying observation

Under H_C there is no positive prediction; H_C is a null hypothesis
that asserts no structural law to find. Falsification of H_C
therefore requires verified positive evidence under H_BSW or
H_BFP — i.e., a third anchor at higher h (H_BSW falsification
probe) or a quadratic ratio-pattern relation at low denominator
(H_BFP falsification probe).

### Falsification status

NOT FALSIFIED. By construction, extending h alone or scanning more
loci without finding new anchors does not falsify H_C; only a
positive verified structural fit under H_BSW or H_BFP does.
H_C is the default null-hypothesis posture if H_BSW and H_BFP both
fail their predicted falsifying tests.

### Substrate-cited estimated probe runtime

H_C does not commission a new probe; it is the conditional posture
adopted if the H_BSW + H_BFP probes both fail. Adoption of H_C as
operating posture has zero compute cost; it has a wording cost in
PCF-2 v3.x (see `pcf2_v3x_wording_softening.md` candidate W2).

---

## §X Concluding note (substrate-only, no ranking)

The three hypotheses are presented above without ranking. The
relevant decision-tree input is in `t1_synth_question_set.md`
(Q1–Q5). The substrate-only synthesis here records:

- All three hypotheses are NOT FALSIFIED at h ≤ 10⁹ inside the 044R
  + 044B swept regime.
- H_BSW and H_BFP have positive predictions and falsifying probes
  with substrate-cited estimated runtimes.
- H_C has no positive prediction; falsification requires positive
  evidence under H_BSW or H_BFP.

T1 Synth W20 weekly arbitration ranks H_BSW / H_BFP / H_C and
selects the Q1 / Q2 fire-or-defer combination.
