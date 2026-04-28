# Master Theorem Audit — SIARC Submitted Manuscripts

**Date:** 2026-04-28
**Auditor:** GitHub Copilot (VS Code)
**Scope:** All submitted manuscripts in `tex/submitted/` plus the
W4 draft `trans_minus29_full.tex` from the bridge sessions.

---

## 1. Master Theorem Table

| ID | Label | Statement (brief) | Status | Paper | Referee Risk |
|----|-------|-------------------|--------|-------|---|
| T29-T3.1 | Plus-form indicial pair on r=-2/9 | r=-2/9 ⇒ plus-form indicial roots {1/3, 2/3} | PROVED (elementary) | trans_minus29_full | LOW |
| T29-C3.2 | Transcendental Ratio Identity | Trans + r∈(-1/4,0) ⇒ r=-2/9 | EMPIRICAL (~585k families, 0 ctrex) | trans_minus29_full | LOW (clearly labelled Conjecture) |
| T29-L4.1 | Minus-form characteristic roots | μ²-b₁μ+a₂=0; on r=-2/9, μ±=b₁(3±√17)/6 | PROVED | trans_minus29_full | LOW |
| **T29-T4.2** | **Algebraic signature (Claim A)** | r=-2/9 ⇔ \|μ+/μ-\|=(13+3√17)/4 (a₂<0) | PROVED (elementary algebra) | trans_minus29_full | LOW |
| **T29-T4.3** | **PSLQ certificate (Claim B)** | PSLQ relation [13,3,-4] on {1,√17,ρ} at dps=150 | PROVED but **TAUTOLOGICAL** | trans_minus29_full | **MEDIUM** |
| T29-P5.1 | Minus-form indicial closed form | α(μ) = -((b₁-b₀)μ+(a₁-a₂))/(b₁μ-2a₂) | PROVED (sympy) | trans_minus29_full | LOW |
| T29-L5.2 | Compatibility ideal for {1/3,2/3} | Two-equation ideal in Q[a₀..b₁] | PROVED (sympy) | trans_minus29_full | LOW |
| **T29-T5.3** | **Integer-grid obstruction (Claim C)** | indicial pair {1/3,2/3} ∩ Trans ⇒ b₀/b₁ = (27±√17)/18 | PROVED symbolically (with typo) | trans_minus29_full | **MEDIUM** |
| **T29-P5.5** | **Leading-order invariant search (Claim D-i)** | No new rational-coef leading invariant on Trans | EMPIRICAL (50+20 family survey) | trans_minus29_full | **MEDIUM-HIGH** |
| T29-P5.6 | Sub-leading c₁ coefficient | A = (a₂-b₁μ)(4a₂-b₁²)/D | PROVED (sympy) | trans_minus29_full | LOW |
| **T29-C5.7** | **No sub-leading resonance (Claim D-ii)** | A_num vanishes only at degenerate/Alg loci | PROVED | trans_minus29_full | LOW |
| **T29-P5.8** | **Convergence-rate experiment (Claim D-iii)** | rate constant reduces to Vieta-tautological value | EMPIRICAL (panel of 20 families) | trans_minus29_full | **MEDIUM-HIGH** |
| **T29-P5.9** | **Direct PSLQ on Trans limits** | No relation found among {1,L,L²,...} or with √17,π,log2 | EMPIRICAL (10 families, dps=300) | trans_minus29_full | **MEDIUM** |
| | | | | | |
| SC-Lem | Discrete Wronskian | Standard | PROVED | area2_selfadjoint_pcf_SUBMISSION | LOW |
| SC-T1 | Self-adjoint structure of degree-(2,1) PCF op | Symbolic | PROVED | area2_selfadjoint_pcf_SUBMISSION | LOW |
| SC-T2 | General apparent singularity | Symbolic | PROVED | area2_selfadjoint_pcf_SUBMISSION | LOW |
| SC-T3 | Discriminant universality | Symbolic | PROVED | area2_selfadjoint_pcf_SUBMISSION | LOW |
| SC-T4 | Perron–Bessel identification | Standard + new | PROVED | area2_selfadjoint_pcf_SUBMISSION | LOW |
| SC-Cor | Structural exclusion | Follows from T3 | PROVED | area2_selfadjoint_pcf_SUBMISSION | LOW |
| | | | | | |
| RU-T1 | Meinardus (cited) | classical | PROVED (citation) | paper14-ratio-universality | LOW |
| RU-T2 | Ratio Universality | main theorem | PROVED (k≤4) / CONDITIONAL (k≥5) | paper14-ratio-universality | LOW |
| RU-Tprime | Ratio Expansion w/ controlled error | main | PROVED | paper14-ratio-universality | LOW |
| RU-LemSel | General Selection Rule | combinatorial | PROVED | paper14-ratio-universality | LOW |
| RU-T-Cube | Cube-Root Ratio | main | PROVED | paper14-ratio-universality | LOW |
| RU-LemPP | Plane Partition sub-leading | techincal | PROVED | paper14-ratio-universality | LOW |
| RU-T-A1k | A₁⁽ᵏ⁾ for k=1..4 | proved cases | PROVED (k=1..4) | paper14-ratio-universality | LOW |
| RU-T2star | Theorem 2* (formerly Conj 2*) | restated as theorem | PROVED (per label) | paper14-ratio-universality | **MEDIUM** — verify labelling matches proof completeness |
| RU-LemK | Lemma K (Kloosterman bound, conductor 24) | bound | PROVED | paper14-ratio-universality | LOW |
| RU-T-A2k | A₂⁽ᵏ⁾ and βₖ | k=1 proved; k≥2 = Conj 3* | MIXED (proved k=1; CONDITIONAL k≥2) | paper14-ratio-universality | LOW (clearly labelled) |
| | | | | | |
| Tak-P1 | Spectral class complete only mod modular sampling | structural | PROVED | paper4_takeuchi_outline | LOW |
| Tak-T1 | Arithmetic PCF families uniformize X(1) | classification | PROVED | paper4_takeuchi_outline | LOW |
| Tak-Lem | Takeuchi obstruction for non-arithmetic families | obstruction | PROVED | paper4_takeuchi_outline | LOW |
| Tak-Prop-Heun | Heun obstruction for V_quad | symbolic | PROVED | paper4_takeuchi_outline | LOW |
| Tak-C0..C3 | Tier 0..3 conjectures (transcendence, cusp rigidity, rigidity, uniformization) | OPEN | CONJECTURE | paper4_takeuchi_outline | LOW (clearly labelled) |
| Tak-CMaster | Master hierarchy conjecture | OPEN | CONJECTURE | paper4_takeuchi_outline | LOW |
| | | | | | |
| Des-Conj | PCF-43 desert conjecture | OPEN | CONJECTURE | pcf_desert_negative_result | LOW |
| RatCon-P-Fin | Finite CF | structural | PROVED | pcf_rational_contamination_2026 | LOW |
| | | | | | |
| Uni-T-Log | Logarithmic Ladder | main | PROVED | pcf_unified_expmath_submission | LOW |
| Uni-T-Pi0 | Pi Family m=0 | main | PROVED | pcf_unified_expmath_submission | LOW |
| Uni-Conj-Ratio | Ratio Formula | OPEN | CONJECTURE | pcf_unified_expmath_submission | LOW |
| Uni-Cor-Pi | Full Pi Family | conditional | CONDITIONAL on Conj-Ratio | pcf_unified_expmath_submission | LOW |
| Uni-T-Conv0 | m=0 convergent numerators | structural | PROVED | pcf_unified_expmath_submission | LOW |
| Uni-T-Conv1 | m=1 convergent numerators | structural | PROVED | pcf_unified_expmath_submission | LOW |
| Uni-Conj-Rnm | General m | OPEN | CONJECTURE | pcf_unified_expmath_submission | LOW |
| Uni-LemShift | Casoratian shift | technical | PROVED | pcf_unified_expmath_submission | LOW |
| Uni-Cor-Special | Special-value corollary | conditional | CONDITIONAL on Conj-Ratio | pcf_unified_expmath_submission | LOW |
| Uni-T-Cas | Casoratian closed form | symbolic | PROVED | pcf_unified_expmath_submission | LOW |
| Uni-T-4overpi | 4/π identification | symbolic | PROVED | pcf_unified_expmath_submission | LOW |
| Uni-Prop-Gauss | Gauss CF identification | classical+sym | PROVED | pcf_unified_expmath_submission | LOW |
| Uni-Prop-Euler | Euler CF identification | classical | PROVED | pcf_unified_expmath_submission | LOW |
| Uni-Lem-Worp | Worpitzky bound | classical | PROVED | pcf_unified_expmath_submission | LOW |
| Uni-Lem-Bracket | Bracket lemma | technical | PROVED | pcf_unified_expmath_submission | LOW |
| Uni-Lem-Qgr | Denominator growth | technical | PROVED | pcf_unified_expmath_submission | LOW |
| Uni-Prop-Irr | Irrationality | classical | PROVED | pcf_unified_expmath_submission | LOW |
| | | | | | |
| Rig-T-FD | Quantitative first-digit anomaly | inequality | PROVED (R1/R2) | rigidity_entropy_*resubmission_R[12] | LOW |
| Rig-P-CRT | Conditional averaged persistence under RT hypothesis | conditional | CONDITIONAL | rigidity_entropy_*_R[12] | LOW |
| Rig-Cor-Poly | Weaker polynomial tail corollary | conditional | CONDITIONAL | rigidity_entropy_*_R[12] | LOW |
| Rig-Conj-AM | Conditional arithmetic memory principle | OPEN | CONJECTURE | rigidity_entropy_*_R[12] | LOW |
| | | | | | |
| Vq-T-AppSing | Apparent singularity exclusion | symbolic | PROVED | vquad_resurgence_R[12] | LOW |
| Vq-T-PIII | PIII(D₆) classification | classification | PROVED | vquad_resurgence_R[12] | LOW |
| Vq-T-Borel | Borel singularity | analytic | PROVED | vquad_resurgence_R[12] | LOW |
| Vq-P-Stokes | Stokes constant estimate | numerical | EMPIRICAL/numerical | vquad_resurgence_R[12] | LOW–MEDIUM |
| Vq-Conj-S | Identification of S | OPEN | CONJECTURE | vquad_resurgence_R[12] | LOW |
| | | | | | |
| JAR-T-Caps | Capstone master_certificate_summary | Lean-verified | PROVED + 7 documented infrastructure sorries (1 discharged Apr 2026) | manuscript_JAR_R1 (lean4) | **MEDIUM** — sorries disclosed, but reviewer scrutiny on `evolutionMap` opaque |
| JAR-T-Num | Numerical Thermoelastic Theorem | Lean | PROVED | manuscript_JAR_R1 | LOW |
| JAR-T-Heat | Linear Heat Equation Certificate | Lean | PROVED | manuscript_JAR_R1 | LOW |

(IDs prefixed by manuscript shorthand; T = Theorem, P = Proposition, L = Lemma, C = Conjecture, Cor/Lem variants as labelled.)

---

## 2. Verification of Claims A–D (trans_minus29_full)

### CLAIM A — Theorem 4.3 (Algebraic signature)

**Statement audited:** For a₂<0, b₁≠0, `a₂/b₁² = -2/9 ⇔ |μ+/μ-| = (13+3√17)/4`,
where μ± satisfy μ²-b₁μ+a₂=0.

**Verdict: PROVED by direct algebraic calculation. No additional assumptions required beyond a₂<0, b₁≠0 (both stated).**

Derivation steps (each elementary):
1. Vieta on μ²-b₁μ+a₂=0: μ+ + μ- = b₁, μ+μ- = a₂.
2. Hence `a₂/b₁² = (μ+μ-)/(μ++μ-)² = q/(1+q)²` with q := μ+/μ-. ✓
3. (⇒) Set q/(1+q)² = -2/9 → 9q = -2(1+q)² → `2q² + 13q + 2 = 0`.
   Roots q = (-13 ± 3√17)/4; both negative; |q| ∈ {(13+3√17)/4, (13-3√17)/4}.
   Reciprocal pair, so |μ+/μ-| (taking dominant root) = (13+3√17)/4. ✓
4. (⇐) ρ = (13+3√17)/4 ⇒ q ∈ {±(13+3√17)/4}. Substitute back:
   - q = -(13+3√17)/4 → a₂/b₁² = -2/9 ✓
   - q = +(13+3√17)/4 → a₂/b₁² = +2/17
   The hypothesis a₂<0 excludes the second branch. ✓

**Numerical verification at dps=60 (b₁=1, a₂=-2/9):**
- ρ computed = 6.342329219...
- (13+3√17)/4 = 6.342329219...
- Difference: ~6.2e-61 (machine round-off).

**Hidden assumption?** The proof tacitly uses that the discriminant b₁²-4a₂
is positive so μ± are real and the modulus |q| equals |q|_real. With a₂<0,
b₁²-4a₂ > b₁² > 0. ✓ No hidden hypothesis.

**Risk: LOW.** This is a clean elementary identity. A referee will accept it.
The author should note explicitly in the proof that "the discriminant is
positive under a₂<0" to forestall any objection.

### CLAIM B — Theorem 4.4 (PSLQ certificate)

**Statement audited:** PSLQ on {1, √17, ρ} at dps=150 returns relation
[13, 3, -4], i.e. `13·1 + 3·√17 - 4·ρ = 0`, where ρ = |μ+/μ-|.

**Verdict: NUMERICALLY CORRECT but TAUTOLOGICAL given Theorem 4.3.**

Direct check: 13 + 3√17 - 4·(13+3√17)/4 = 13 + 3√17 - (13+3√17) = 0. **Yes — the relation [13,3,-4] is by definition equivalent to ρ=(13+3√17)/4.**

So PSLQ here does not provide *independent* algebraic evidence; it only
verifies that the numerical computation of ρ from a representative Trans
family agrees with the closed form (Theorem 4.3) to >100 digits. That is
a *consistency check* on the symbolic derivation, not a new identification.

**This is the single most likely point of referee objection in the paper.**
A careful referee will write:
> "Theorem 4.4 is logically a corollary of Theorem 4.3, not a separate
> theorem. The PSLQ certificate is a numerical sanity check, not an
> independent integer relation."

**Recommended fix (HIGH PRIORITY):**
- Demote Theorem 4.4 to **Remark 4.4** ("Numerical consistency check") or
  **Corollary 4.4** ("Numerical verification of Theorem 4.3").
- Re-word the abstract sentence "PSLQ-certified at dps=150 with integer
  relation [13,3,-4]" to make clear this is a consistency check, not
  independent evidence. (The current phrasing — and Remark 4.5
  ("Vieta-tautological character and its content") *partly* addresses this
  but is buried after the theorem.)
- Better: state Theorem 4.3 first, then write "Numerical verification.
  At dps=150, PSLQ on {1,√17,ρ} reproduces the relation [13,3,-4] ⇔
  Theorem 4.3, with reconstruction error < 10⁻¹⁰⁰; see Appendix."

**Risk: MEDIUM** as currently labelled (a referee scrutinising the structure
will spot the tautology); LOW if relabelled as Corollary/Remark.

### CLAIM C — Theorem 5.3 (Integer-grid obstruction)

**Statement audited:** Under minus-form, the indicial pair {1/3, 2/3}
on the Trans locus r=-2/9 forces b₀/b₁ = (27±√17)/18, both irrational.
No integer family realises both simultaneously.

**Verdict: PROVED SYMBOLICALLY. The closed form (27±√17)/18 is correct.
A typo in the intermediate equation should be fixed.**

Verification:
- Compatibility ideal (Lemma 5.2): `a₂ + 9b₀² - 27b₀b₁ + 20b₁² = 0`. (trusted via sympy script `compatibility.py` per cite)
- Substitute a₂ = -2b₁²/9 and divide by b₁²: `81r² - 243r + 178 = 0`
  where r := b₀/b₁. Discriminant = 243²-4·81·178 = 1377 = 81·17;
  roots = (243±9√17)/162 = **(27±√17)/18**. ✓ Numerically confirmed:
  81·((27+√17)/18)² - 243·(27+√17)/18 + 178 = 0 (exactly, in mpmath).

**Typo to flag (high priority):** The paper writes the intermediate step as
> "−9 r² + 27 r − 20 = r, r := b₀/b₁, i.e. 81 r² − 243 r + 178 = 0"

The first equation cannot equal the second:
- The actual derivation is `-9r² + 27r - 20 = a₂/b₁² = -2/9`, not `= r`.
- Multiplying by -9: `81r² - 243r + 180 = 2 → 81r² - 243r + 178 = 0`. ✓

The "= r" is almost certainly a copy-paste error where the *symbol* r
appears with two different meanings (Worpitzky parameter a₂/b₁² vs. the
ratio b₀/b₁). The end result 81r²-243r+178=0 is correct.

**Recommended fix:** Replace the intermediate line with
`-9(b₀/b₁)² + 27(b₀/b₁) - 20 = a₂/b₁² = -2/9`, then "i.e. 81r²-243r+178=0
with r := b₀/b₁."

**Risk: MEDIUM** as written (typo in proof, even though final result is
correct, looks sloppy and may invite a referee to question sympy provenance).
LOW after the typo is fixed.

### CLAIM D — Propositions 5.5, 5.7 (W2/W3 sprints), Corollary 5.7, Proposition 5.8, 5.9

**Statement audited:** Three negative results (leading-order invariant search,
sub-leading resonance, convergence-rate / direct-PSLQ).

**Verdict: MIXED.**

| Sub-claim | Current label | Actual epistemic status | Recommended label |
|---|---|---|---|
| Prop 5.5 (No new leading-order invariant) | Proposition | EMPIRICAL (50+20 family computational survey) | **Observation** or **Empirical Proposition** |
| Cor 5.7 (No sub-leading resonance) | Corollary | PROVED (algebraic, from Prop 5.6) | Corollary ✓ (correctly labelled) |
| Prop 5.8 (Convergence-rate experiment) | Proposition | EMPIRICAL (panel of 20 families, dps=200) | **Observation** |
| Prop 5.9 (Direct PSLQ negative result) | Proposition | EMPIRICAL ("no relation found at dps=300, bound 10⁴") | **Observation** |

**The substantive concern:** A "Proposition" with an `\begin{proof}` whose body is "Computational survey, script `convergence_rate.py`" is not a proposition in the standard mathematical sense. It is an empirical observation. Cf. the paper14 manuscript style which carefully labels conditional and proved cases.

**Risk: MEDIUM-HIGH.** A referee at *Experimental Mathematics* or
similar will want explicit separation between *theorems* (proved
symbolically/analytically) and *observations* (computational evidence
on a finite panel, no proof of universality). The current paper mixes
them under the single label "Proposition (negative result)".

**Recommended fix:** Introduce a new theorem-style environment
```
\theoremstyle{remark}
\newtheorem{observation}[theorem]{Observation}
```
and re-label 5.5, 5.8, 5.9 as **Observations** (with the same numbering
sequence). Cor 5.7 stays as Corollary. Update §1 introduction and abstract
to say "three negative results — one proved corollary and two
computational observations" rather than "three negative results" tout
court. This pre-empts the most likely referee objection.

---

## 3. Risk Assessment per Submitted Paper

### `trans_minus29_full.tex` (W4 draft, not yet submitted)

- **Most likely referee objection:** The status of Theorem 4.4 — it is
  not an independent theorem but a numerical re-statement of Theorem 4.3.
- **Could trigger immediate rejection?** No, but could trigger major
  revision. The referee will demand re-labelling of 4.4 and of the W2/W3
  empirical "propositions".
- **Single most important fix:** Demote Theorem 4.4 to Corollary or Remark;
  introduce Observation environment for 5.5, 5.8, 5.9; fix the typo in
  the proof of Theorem 5.3 (`= r` → `= -2/9`).

### `paper14-ratio-universality-SUBMISSION.tex`

- **Most likely referee objection:** Theorem A₂⁽ᵏ⁾ (T-A2k) — proved for k=1,
  conjectural for k≥2, currently labelled as a single theorem with a
  parenthetical "Conjecture 3* for k≥2". A picky referee may want this
  split.
- **Could trigger immediate rejection?** No.
- **Single most important fix:** Consider splitting T-A2k into a Theorem
  (k=1) and a Conjecture (k≥2). The current presentation is acceptable
  but borderline.

### `area2_selfadjoint_pcf_SUBMISSION.tex`

- **Most likely referee objection:** Discriminant universality (T3) —
  scope of "universality" claim. As long as the universality is over
  the explicit family enumerated in the proof, this is fine.
- **Could trigger immediate rejection?** No.
- **Single most important fix:** None pressing.

### `pcf_unified_expmath_submission.tex`

- **Most likely referee objection:** Conjectures 4.x (Ratio Formula,
  General m) — clearly labelled, but the conditional corollaries
  Cor-Pi and Cor-Special might be misread as proved. They are
  explicitly labelled "(conditional on Conj. X)" in the source — verify
  the rendered PDF preserves this.
- **Could trigger immediate rejection?** No.
- **Single most important fix:** None pressing.

### `paper4_takeuchi_outline.tex`

- **Most likely referee objection:** This is an outline / conjecture
  paper; T-psl2z is the only proven theorem, the rest are explicit
  conjectures. The mix is appropriate for a programmatic paper.
- **Could trigger immediate rejection?** No.
- **Single most important fix:** None pressing.

### `rigidity_entropy_expmath_resubmission_R[12].tex`

- **Most likely referee objection:** The conditional propositions
  (P-CRT, Cor-Poly) hinge on the return-time hypothesis. Reviewer 2 in
  R1/R2 history may push back on whether this hypothesis is realistic.
- **Could trigger immediate rejection?** No.
- **Single most important fix:** None pressing — the conditional
  structure is well-flagged.

### `vquad_resurgence_R[12].tex`

- **Most likely referee objection:** Stokes constant estimate (P-Stokes)
  is numerical/empirical. Currently labelled Proposition.
- **Could trigger immediate rejection?** No.
- **Single most important fix:** Consider re-labelling as
  "Numerical Proposition" or "Computation"; minor.

### `manuscript_JAR_R1.tex` (Lean 4 verified)

- **Most likely referee objection:** The seven infrastructure sorries
  (six in Operators.lean, one in Control.lean), even though disclosed
  with explicit blocker reasons.
- **Could trigger immediate rejection?** Unlikely — the manuscript
  goes to lengths to disclose the sorry inventory and explain the
  trusted-core/untrusted-infrastructure separation. But a hostile
  referee could insist on full discharge before publication.
- **Single most important fix:** Continue discharging sorries
  (as already begun — LocalWellPosedness.lean discharged April 2026);
  for now, ensure InfrastructureSorryInventory is up to date in the
  appendix.

---

## 4. Summary of Recommended Fixes (priority order)

1. **[HIGH] `trans_minus29_full`:** Demote Theorem 4.4 to Corollary/Remark
   ("numerical verification of Theorem 4.3"). Re-word the abstract sentence
   accordingly. (Pre-empts the single most likely referee objection.)
2. **[HIGH] `trans_minus29_full`:** Fix the typo in the proof of Theorem 5.3:
   `-9r²+27r-20 = r` should be `-9(b₀/b₁)²+27(b₀/b₁)-20 = -2/9`.
3. **[MEDIUM] `trans_minus29_full`:** Introduce an `\newtheorem{observation}`
   environment and re-label Propositions 5.5, 5.8, 5.9 as Observations.
   Update §1 phrasing.
4. **[LOW] `paper14`:** Consider splitting T-A2k into proved (k=1) and
   conjectural (k≥2) statements.
5. **[LOW] `vquad_resurgence`:** Consider relabelling P-Stokes as
   "Numerical Proposition".
6. **[ONGOING] `manuscript_JAR_R1`:** Continue discharging the six
   remaining infrastructure sorries.

No claim in any submitted manuscript currently overstates evidence to a
degree that would trigger immediate rejection. The Trans -2/9 W4 draft
should be edited per items 1–3 before submission.
