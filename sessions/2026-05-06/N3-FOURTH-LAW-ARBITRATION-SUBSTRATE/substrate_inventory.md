# Substrate inventory — n=3 fourth-law-candidate arbitration (relay 055)

**Date:** 2026-05-06
**Author:** CLI-Synthesizer (T2 in-tier; v2026-05-08 RACI standard cadence)
**Class:** STRUCTURAL-ANALYSIS-SUBSTRATE
**Scope:** substrate-only synthesis; no NEW empirical claims; all
numerical anchors verbatim from prior AEAL-logged 044R-A1..A8 +
044B-A1..A8 entries.

**Anchor-folder SHA-256 (per claims.jsonl C1, C2):**

| folder | file | SHA-256 |
|--------|------|---------|
| 044R `T2B-BZERO-OFFSET-LOG-SWEEP-REFIRE` | `handoff.md` | `FE7ABBE728ECDE9FB3741EFABED2776C1F081BA39B93F607D7C191191C1E6FE5` |
| 044R `T2B-BZERO-OFFSET-LOG-SWEEP-REFIRE` | `claims.jsonl` | `87810E647DCAE32B344268CED209F7E21DC778C0881DE4D44436EC96CD3EF2F9` |
| 044B `T2B-TIGHTENED-SWEEP-OUTCOME-B` | `handoff.md` | `22530208FEBCAC6FE6BB12CE5BD84760873BE1DB155CA081284DE2375F8EEE0D` |
| 044B `T2B-TIGHTENED-SWEEP-OUTCOME-B` | `claims.jsonl` | `DE55E8F18A7D8B1E41F1FE628D8C7B018D634D60857B4CF5B5191238C38796E9` |

---

## §1 Anchor data (verbatim)

Two off-orbit n/log(2) data points at h ≤ 10⁹.

### A1. b₇ singular `(a₂, a₁, a₀, b₁, b₀) = (8, -4, 0, 7, 4)`

- L = 3/log(2) (EXACT at dps=300).
- 044B STEP 2C re-verify (claim 044B-A3, output_hash
  `3cdcedaa6beb894ef3fd977132459544f0e002765eda3eba428bb3fe9905b48c`):
  PSLQ relation in 8-element transcendental basis `[-3, 0, 0, 0, 0, 0, 0, 1]`
  → `-3 + L · log(2) = 0` → L = 3/log(2), n=3.
- Numeric value at dps=300 (from 044B handoff Key numerical findings):
  `4.32808512266689022207977404300567641227993786245895780240635...`
- Residual `|L − 3/log(2)| < 10⁻⁵⁰`.
- Ratio a₂/b₁² = **8/49** (numerator 8 — generic; not Bauer-shape −k²).

### A2. b₁₀ 044R outlier `(a₂, a₁, a₀, b₁, b₀) = (-9, 0, 0, 10, 5)`

- L = 3/log(2) (EXACT at dps=300).
- 044R deep-verify (claim 044R-A5, output_hash
  `38f187ec317ef9b61cf42ed77bc47eb346294c8c230753a5ac0dd0fa8024d9a9`):
  PSLQ relation `−3 + L · log(2) = 0` → L = 3/log(2), n=3.
- Numeric value at dps=300 (from 044R handoff Key numerical findings,
  60-dps prefix): same as A1 to dps=300, residual = 0,
  `residual_lt_1e_200 = True`.
- Ratio a₂/b₁² = **−9/100** (numerator −9 = −k² with k=3 — Bauer-shape
  pattern; denominator 100 — does not match the Bauer-on-orbit
  denominator 324 = 18² that would obtain at b₁ = ±6k = ±18).
- Bauer-orbit membership: **off-orbit** (a₂ matches Bauer numerator
  shape −k²; |b₁| = 10 ≠ 6k = 18).
- Discriminant identity class: `neither` (not on `4·a₂ − b₁² = 0`
  Brouncker boundary; not on `9·a₂ + 2·b₁² = 0` Trans-stratum-proper).

### Note on the n=3 collision

Both A1 and A2 yield L = n/log(2) with **n = 3** (verified to dps=300
in their respective AEAL entries). This 2-point coincidence at
h ≤ 10⁹ is what relay 055 calls the "n=3 collision". Whether this
collision is structural is the T1 Synth W20 weekly arbitration
question; relay 055 does not adjudicate it.

---

## §2 Negative results from 044B (B-T-A verdict)

Source: 044B handoff `What was accomplished` + claims 044B-A1, A2, A4,
A6.

### NR1. Bauer-shape sub-locus does not extend the pattern

Scan parameters (044B STEP 2B; claim 044B-A2):

- numerator family `(a₂, a₁, a₀) = (−k², 0, 0)` for k ∈ {1, 2, 3, 4, 5}
- b₁ ∈ ±B(k) \ {±6k} (off-orbit corridors)
- b₀ ∈ [−7, 7]
- Stage A K_500 convergence → Stage B PSLQ dps=150 h ≤ 10⁷ →
  Stage D deep-verify dps=300 h ≤ 10⁹ on Log/Trans hits.

Outcome (044B handoff Key numerical findings):

| stage | count |
|-------|-------|
| enumeration_total | 1 620 |
| Stage A convergent | 1 058 |
| Stage B Log | 2 |
| Stage B Trans | 0 |
| Stage B Phantom | 0 |
| Stage D off-orbit | 2 |

The 2 Stage D off-orbit hits are exactly `(−9, 0, 0, 10, 5)` and
`(−9, 0, 0, −10, −5)` — both already in the b₁₀ 044R sign-orbit
closure (Bauer-shape parameterization at k=3 contains b₁ ∈ {±10},
b₀ ∈ [−7, 7]). After dedup against 044R sign-orbit closure:
**new_off_orbit = 0**.

This means: no new Bauer-shape Log hits beyond the b₁₀ 044R
sign-orbit at the bounded h-levels actually swept (h ≤ 10⁷
Stage B; h ≤ 10⁹ Stage D).

### NR2. Sign-orbit closure of b₇ + b₁₀ exhausts off-orbit data at h ≤ 10⁹

044B STEP 2A (claim 044B-A1) closed the sign-orbit of the 044R
hit: 8 tuples `(a₂, a₁, a₀, b₁, b₀) = (±9, 0, 0, ±10, ±5)`
evaluated at dps=300 with PSLQ at h ≤ 10⁹.

Per the 044B handoff Key numerical findings:

- 2 of 8 tuples are off-orbit n/log(2): `(−9, 0, 0, 10, 5)` (n=+3,
  the 044R anchor itself) and `(−9, 0, 0, −10, −5)` (n=−3, the
  L → −L sign-symmetric mirror).
- The other 6 tuples classify as Desert.
- All 8 tuples have `discriminant_identity_class = neither` (not on
  Bauer-1872 orbit, not on Brouncker boundary, not on Trans-stratum-
  proper).

Combined with the b₇ sign-orbit (4 tuples; A1 + the L → −L
sign-symmetric mirror at `(−8, 4, 0, −7, −4)` plus 2 desert tuples
from sign-coupling — see also §3 coverage map), the union of the
two sign-orbits exhausts off-orbit n/log(2) data at h ≤ 10⁹. This
means: no third off-orbit anchor with b₁ ∈ {5, 7, 8, 9, 10} exists
at h ≤ 10⁹.

### NR3. Low-denominator rational curve through 2 anchors

044B STEP 3 (claim 044B-A4): linear ratio-pattern fit through anchors
A1 and A2 yields the integer relation

> 3·a₂ + 17·b₁ − 143 = 0

verified at both anchors (24 + 119 − 143 = 0 and −27 + 170 − 143 = 0;
linear residual = 0). However, with only 2 anchor points any 2-term
integer relation through them is identically determined; the fit is
underdetermined. The relevant gating field reported by 044B:

> max_abs_denom = 143

The project low-denominator threshold is `max_abs_denom ≤ 30`
(044B fit-residual gating, judgment call 2 in 044B handoff). 143 > 30,
so the curve **does not** satisfy the project's "low-denominator
structural curve" criterion.

This means: no STRUCTURAL straight-line ratio-pattern curve unifies
the two anchors at the project's low-denominator threshold. The
linear fit is a numerical curiosity, not evidence either way.

---

## §3 Sign-orbit + Bauer-shape coverage map

Coverage at the bounded h-levels actually swept (sign-orbit at
h ≤ 10⁹; Bauer-shape Stage B at h ≤ 10⁷ / Stage D at h ≤ 10⁹).

| locus | scan extent | hits |
|-------|-------------|------|
| b₇ sign-orbit (A1 closure) | full closure, h ≤ 10⁹ | 4 tuples enumerated |
| b₁₀ 044R sign-orbit (A2 closure) | full closure, h ≤ 10⁹ | 4 tuples enumerated |
| Bauer k=1..5 (044B STEP 2B) | b₁ ∈ ±B(k) \ {±6k}, b₀ ∈ [−7, 7] | 0 NEW off-orbit |
| total off-orbit n/log(2) | b₁ ∈ {5, 7, 8, 9, 10} | 2 (A1 + A2) |

Notes:

- "b₇ sign-orbit closure" means the closure under the symmetry that
  flips numerator and denominator signs together; per 044B judgment
  call 3, for A1 = `(8, −4, 0, 7, 4)` this set is
  `{(±8, ∓4, 0, ±7, ±4)}` (4 tuples).
- "b₁₀ 044R sign-orbit closure" is `{(±9, 0, 0, ±10, ±5)}` (8 sign
  combinations; per 044B STEP 2A 2 of 8 are off-orbit n/log(2),
  6 of 8 classify Desert — see §2 NR2).
- "0 NEW off-orbit" in the Bauer-shape row is the 044B-A2 +
  044B-A6 dedup result (Stage D off-orbit count = 2, both already
  in the b₁₀ sign-orbit; new_off_orbit = 0).
- Total off-orbit n/log(2) data points at h ≤ 10⁹ in b₁ ∈ {5..10}:
  **2** (A1 + A2; per 044B-A5).

---

## §4 Ratio pattern panel

| anchor | a₂ | b₁ | a₂/b₁² | k (if Bauer) | denom-class (≤ 30?) |
|--------|----|----|--------|--------------|---------------------|
| A1 b₇ | 8 | 7 | 8/49 | n/a (a₂ = +8 ≠ −k²) | 49 ≤ 30 → No |
| A2 b₁₀ | −9 | 10 | −9/100 | k = 3 (numerator a₂ = −9 = −k² ✓; denominator off — Bauer requires b₁ = ±6k = ±18) | 100 ≤ 30 → No |

Ratio-pattern observations (substrate-only; per 044B-A4 verbatim,
disclaiming structural identity):

- Neither anchor's denominator (49 or 100) is "low" by the project
  threshold (max_abs_denom ≤ 30).
- The A2 numerator a₂ = −9 = −3² matches the Bauer-shape
  numerator pattern at k = 3 (Bauer 1872 numerator family
  a₂ = −k²); the A2 denominator b₁ = 10 does NOT match the
  Bauer-on-orbit denominator b₁ = ±6k = ±18.
- A1 a₂ = +8 is not of the form −k² for any integer k, so A1
  is structurally outside the Bauer-shape numerator family (per
  044B handoff "What would have been asked", item 3).
- The 044B integer-relation fit `3·a₂ + 17·b₁ − 143 = 0` passes
  through both anchors with residual 0, but with only 2 anchors
  any 2-term integer relation is identically determined and
  max_abs_denom = 143 > 30 (see §2 NR3). The fit makes no
  structural claim.

---

## §5 Pointers to substrate references in earlier sessions

These are sessions cited by 044R / 044B handoffs and by the
hypothesis catalogue (relay 055 STEP 3) as substrate context. They
are referenced for traceability only; relay 055 does not re-anchor
them.

- T2B-PLUS-QUARTER-SURVEY (sessions/2026-04-29/) — +1/4 sub-stratum
  enumeration including Brouncker-class identities at the
  sub-stratum 4·a₂ − b₁² = 0.
- T2B-STIELTJES-VERIFY (sessions/2026-04-29/) — Stieltjes-class
  follow-up at the +1/4 sub-stratum.
- T2B-RESONANCE-B67 (sessions/2026-04-29/) — earlier b₆/b₇
  resonance triangulation that surfaced b₇ singular.
- T2B-RESONANCE-B67-A50 (sessions/2026-04-29/) — a₅₀ extension of
  the b₆/b₇ resonance.
- T2B-LOG-MINUS-ONE-36 (sessions/2026-04-30/) — Log-stratum
  enumeration with 36 numerator coefficient.
- T2B-EQ8-LINEAR-CONSTRAINT (sessions/2026-04-28/) — earlier
  linear constraint study at b₁ = 8.
- T2B-B67-B6-RECONFIRM-HALT (sessions/2026-05-05/) — b₆/b₇
  reconfirmation halt.
- 042a1318 / 044 commit — 044R Stage A cache provenance.

These cover the +1/4 sub-stratum (where Brouncker-class identities
were enumerated; cited in H_BSW substrate) but did not search
b₁ ∈ {11, ..., 15} past 044R's b₁ = 10 ceiling.

---

## §6 Summary — what is on the table for T1 Synth

At h ≤ 10⁹:

- 2 off-orbit n/log(2) data points: A1 (b₇ singular, ratio 8/49,
  generic numerator) and A2 (b₁₀ 044R, ratio −9/100, Bauer-shape
  numerator k=3 with mismatched denominator).
- Both yield n = 3 (the n=3 collision).
- 044B B-T-A verdict closes the sign-orbit + Bauer-shape sub-locus
  question at the bounded h-levels swept: no new off-orbit anchors
  surfaced.
- The linear ratio-pattern fit `3·a₂ + 17·b₁ − 143 = 0` passes
  through both anchors but is underdetermined (2 points, 2 free
  parameters) and max_abs_denom = 143 exceeds the project low-
  denominator threshold of 30.

What remains open (T1 Synth W20 weekly arbitration scope):

- Identity-vs-coincidence question on the n=3 collision.
- Three candidate framings (substrate-only): H_BSW (Brouncker–
  Stieltjes–Wallis-class identity), H_BFP (Bauer–Forrester pencil
  of orthogonal-polynomial relations at non-on-orbit b₁), H_C
  (numerical coincidence at h ≤ 10⁹). See `hypothesis_catalogue.md`
  for full statements without ranking.
- Decision tree on whether to commission a higher-h sweep
  (b₁ ∈ {11, ..., 15} at h ≤ 10¹¹), a quadratic ratio-pattern
  PSLQ scan, both, or neither. See `t1_synth_question_set.md`.
- PCF-2 v3.x wording softening from "b₇ singleton" to a 2-point
  framing. See `pcf2_v3x_wording_softening.md`.

This concludes substrate inventory. Adjudication is reserved for
T1 Synth W20 weekly cadence.
