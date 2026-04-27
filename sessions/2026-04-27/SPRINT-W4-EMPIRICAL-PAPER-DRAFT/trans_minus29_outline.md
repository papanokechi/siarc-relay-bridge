# trans_minus29_outline.md

**Title (working).** *The Trans −2/9 Identity for Degree-(2,1) Polynomial Continued Fractions: Empirical Evidence, an Algebraic Signature, and the Limits of Standard Asymptotic Methods*

**Author.** Papanokechi (independent, Yokohama). ORCID 0009-0000-6192-8273.
**Target length.** 18–25 pages. **Candidate venues** (post-SICF): Ramanujan J., IMRN, JNT (Monat. holds the short companion).

**Relationship to the Monatshefte conjecture note.** This paper is the *full* version of the conjecture note (sessions/2026-04-27/T2B-MONAT-PREP-FIX/t2b_monat_submission_R1.tex, Zenodo DOI 10.5281/zenodo.19801038). It (i) restates the same conjecture and same 585k-family evidence, (ii) **adds** the new W2 algebraic signature `|μ_+/μ_-| = (13+3√17)/4`, and (iii) **adds** the three negative results from the W1/W2/W3 sprints that bound the analytic landscape. Author decision required on whether to keep both submissions live; see handoff.

---

## §1 Introduction (~2 pp.)

- The Trans/Log/Alg trichotomy of integer degree-(2,1) PCFs.
- Empirical observation (~585 000 families, 0 counterexamples): every Trans limit has Worpitzky parameter `r := a₂/b₁² = −2/9`.
- Companion Log anomaly: 2 Log families at b₁=±6 have r=−1/36 (boundary of admissible rational-indicial set).
- New result of this paper: the algebraic signature `|μ_+/μ_-| = (13+3√17)/4` (an iff with `r = −2/9`, sign condition `a₂ < 0`).
- Three negative proof attempts (W1/W2/W3): no standard Birkhoff/asymptotic method can prove the conjecture from leading or sub-leading data alone. The mechanism is global, not local-asymptotic.
- Open problem statement (formal).
- Section guide.

## §2 Background and notation (~2 pp.)

- Definition 2.1: degree-(2,1) PCF, partial-numerator/denominator polynomials, `r = a₂/b₁²`.
- Definition 2.2: Trans/Log/Alg/Rat/Des strata as in the Monat note.
- §2.1 Two recurrence conventions. **PLUS form** `y_{n+1}=b(n)y_n+a(n)y_{n-1}` (standard CF). **MINUS form** `y_{n+1}=b(n)y_n−a(n)y_{n-1}` (used in W1–W3 of this paper). They are conjugate by `y_n ↦ (−1)^n y_n` *up to* a sign on a(n); this conjugation maps the locus `r=−2/9` to itself, but maps the indicial roots between {1/3,2/3} (PLUS) and (3±√17)/6 (MINUS). We use PLUS form for §3 (definitional content) and MINUS form for §§4–5 (asymptotic content).
- PSLQ methodology and the **phantom-hit rule** (relations with target-coefficient zero are rejected; T2A pipeline rejected 38).
- Bridge-repository reproducibility convention.

## §3 The conjecture and empirical evidence (~3 pp.)

- Theorem 3.1 (Indicial pair under PLUS form). On the locus `r = −2/9`, the standard CF indicial equation `λ²−λ−r=0` has rational roots `{1/3, 2/3}`.
- Conjecture 3.2 (Trans −2/9 conjecture, restated from the Monat note).
- Theorem 3.3 (Empirical census). Combined T2A/T2B sweep across ~585 000 convergent families:
    - F(2,4) complete: 24 Trans, all r=−2/9.
    - F(2,5) complete: 56 Trans + 12 Log at r=−2/9; 14 Brouncker at r=+1/4 (boundary, excluded by hypothesis).
    - Resonance sweeps b₁∈{4,5,6,7,8…12} at admissible rational-indicial r∈{−3/16,−4/25,−6/25,−2/49,−35/144}: **0 Trans, 0 Log** in the interior except the −1/36 anomaly.
- Table reproduced from Monat note (Tables 1–3).
- Phantom-hit discipline: 38 PSLQ relations rejected across the T2A pipeline.

## §4 The algebraic signature (~3 pp.)

This is the new content beyond the Monat note.

- Definition 4.1 (MINUS-form characteristic equation). `μ² − b₁μ + a₂ = 0`, μ_± = (b₁±√(b₁²−4a₂))/2.
- Lemma 4.2. On the locus `r = −2/9` with `a₂ < 0` and `b₁ ≠ 0`, the characteristic roots are `μ_± = b₁(3±√17)/6` (irrational quadratic over ℚ).
- Theorem 4.3 (Algebraic signature of the Trans locus). For a degree-(2,1) PCF with integer coefficients, b₁ ≠ 0, a₂ < 0, the following are equivalent:
    1. `a₂/b₁² = −2/9`.
    2. `|μ_+/μ_-| = (13+3√17)/4`.
    Proof: by Vieta, `a₂/b₁² = q/(1+q)²` with q = μ_+/μ_-; substituting q = −(13+3√17)/4 and simplifying yields −2/9. The opposite-sign branch gives r = +2/17, excluded by `a₂<0`.
- Theorem 4.4 (PSLQ certificate). At dps=150 on the basis `{1, √17, ρ}` with ρ = |μ_+/μ_-|, PSLQ returns the integer relation [13, 3, −4]; on the wider basis `{1, √2, √3, √5, √17, π, log 2, ρ}`, PSLQ returns [−13, 0, 0, 0, −3, 0, 0, 4]. Both pass the phantom-hit rule (target-coefficient ≠ 0). Reconstruction error vanishes at >100 digits.
- Remark 4.5 (Tautological vs. non-trivial). Theorem 4.3 is *Vieta-tautological* (it is a re-encoding of `r = −2/9`), yet it is the first explicit algebraic identification of the Trans locus with a quadratic irrationality (`√17`). Combined with the integer-grid result of §5.1 below, this establishes √17 as the natural algebraic invariant of the Trans property.

## §5 Three negative results bounding the analytic landscape (~5 pp.)

### §5.1 Indicial closed form and the integer-grid obstruction (W1)

- Proposition 5.1 (Indicial closed form, MINUS form). Under the Birkhoff ansatz `y_n ~ Γ(n+1)·μⁿ·n^α`, the n⁰ balance after `μ²=b₁μ−a₂` has unique solution `α(μ) = −((b₁−b₀)μ + (a₁−a₂))/(b₁μ − 2a₂)`.
- Lemma 5.2 (Compatibility ideal). The indicial pair `{1/3, 2/3}` (under MINUS form) corresponds to the ideal `C = (a₁−2a₂, a₂+9b₀²−27b₀b₁+20b₁²) ⊂ ℚ[a₀,a₁,a₂,b₀,b₁]`.
- Theorem 5.3 (Integer-grid obstruction). The intersection of `C` with the Trans locus `a₂/b₁² = −2/9` projects onto `b₀/b₁ = (27±√17)/18`, irrational. Consequently **no integer-coefficient family** has both indicial pair {1/3, 2/3} (in MINUS form) and `r = −2/9`.
- Verification on integer grid `|b₁|≤30, |b₀|≤30, |a₂|≤200`: 7.3·10⁵ triples, 0 simultaneous solutions.
- Interpretation. The W1 result is *not* a counterexample to the Monat note (which uses PLUS form, where {1/3, 2/3} is a *consequence* of r=−2/9). It is rather the statement that the alternative MINUS form of the recurrence has irrational indicial structure on the Trans locus, manifesting the same √17 that Theorem 4.3 records.

### §5.2 Leading-order Birkhoff invariant search (W2)

- Survey of 50 integer Trans families: only `|μ_+/μ_-|` is constant; sum, product, and discriminant of the indicial exponents all vary.
- Comparison to Log and Alg classes: `|μ_+/μ_-|` is always a function of r alone (by Vieta), so it separates the three classes by definition.
- Proposition 5.4 (Negative result, leading-order). Beyond `|μ_+/μ_-|` (Theorem 4.3, Vieta-tautological), the leading two-term Birkhoff balance produces no rational-coefficient invariant constant across the Trans locus.

### §5.3 Sub-leading [n⁻¹] resonance test (W3)

- Setup: extend Birkhoff ansatz with `(1 + c₁/n + c₂/n² + ...)`, derive [n⁻¹] balance.
- Proposition 5.5 (Sub-leading c₁ coefficient). The c₁-coefficient at the [n⁻¹] balance, after reducing modulo the characteristic equation and substituting the W1 closed form for α, factors as `A_num = (a₂ − b₁μ)·(4a₂ − b₁²)` (numerator); the denominator does not vanish on Trans.
- Corollary 5.6 (No sub-leading resonance on Trans). `A_num` vanishes on Trans iff `4a₂ = b₁²` or `μ = a₂/b₁`. The first locus is the Alg-discriminant-zero locus, the second forces μ=0 by the characteristic equation. Neither contains the Trans locus. On Trans, `A|_{μ_±} = ∓√17·b₁/3 ≠ 0`. The sub-leading balance uniquely determines c₁ and yields no new constraint.
- Convergence-rate experiment (10 Trans + 5 Log + 5 Alg families at dps=200): the convergence rate constant collapses to `|μ_-/μ_+|`, again Theorem 4.3, with no new amplitude invariant exposed.
- Direct PSLQ on the Trans CF limits L (10 families, dps=300, maxcoeff=10000) against `[1,L,L²,L³,L⁴]` and `[1,L,√17,π,log 2]` returns no relation; pairwise relations on `(L_i,L_j)` are tautological linear scaling `L(λ·b₁) = λ·L(b₁)` for the (a₀,a₁,b₀)=(0,0,0) sub-family.
- Proposition 5.7 (Negative result, sub-leading). The [n⁻¹] Birkhoff balance imposes no constraint that singles out the Trans locus; the convergence rate is W2-tautological; the limits are not algebraic to bound 10⁴ at dps=300 nor expressible against `{√17, π, log 2}`.

## §6 Discussion and open problems (~2 pp.)

- The mechanism is *global*, not local-asymptotic. Three independent local methods all fail.
- The √17 signature is the algebraic shadow of `r = −2/9`. Its appearance in three forms — char-root ratio (Thm 4.3), W1 compatibility ideal (Lem 5.2), and sub-leading on-Trans coefficient (Cor 5.6) — supports a deeper Galois-theoretic / monodromy interpretation of the Trans property.
- The Log anomaly at r = −1/36 (the two b₁=±6 families) is the only known boundary phenomenon: it sits at the intersection of the Bauer–Stern doubling parameter and the rational-indicial admissibility set. Whether this is exceptional or the tip of an iceberg is open.
- Open Problem 6.1 (Galois-of-difference-equations form). Is there a (formal) Galois group of the difference operator `Δ = E² − b(n)·E + a(n)` (E shift) whose splitting-field property over ℚ(n) characterises the Trans locus?
- Open Problem 6.2 (Isomonodromy form). Is the Trans property a degeneration of a Painlevé-VI-type isomonodromic family at parameters (1/3, 2/3, ·, ·) on Schwarz's list?
- Open Problem 6.3 (rational-coefficient version). Does the conjecture survive over ℚ?
- Open Problem 6.4 (Log anomaly formal classification). Classify all (a₀,a₁,a₂,b₀,b₁) with `r = −1/36` producing Log limits.

## §7 Conclusion (~1 p.)

- Summary: empirical 585k corroboration; new √17 algebraic signature; rigorous bounds on standard methods.
- Stance: the Trans −2/9 conjecture is "near-miss" — empirically robust, structurally fingerprinted, but currently analytically opaque.
- Call for theorists from the Galois-of-difference-equations and isomonodromy communities.

## Appendix A: Computational methodology

- PSLQ: `mpmath.pslq` with `tol=10⁻⁵⁰`, `maxcoeff` bounds at each step recorded; phantom-hit rule.
- Precision protocol: dps=100 for census passes, dps=150 for PSLQ certificates, dps=200–300 for sub-leading verification.
- Bridge repository: github.com/papanokechi/siarc-relay-bridge.
- Reproducibility statement: every numerical claim has an AEAL `claims.jsonl` entry referencing a script and SHA-256 hash of its log.

## Appendix B: PSLQ relations and SHA-256 hashes

- W2 PSLQ relations (Theorem 4.4 evidence) and SHA-256.
- W3 PSLQ relations (negative C1, C3 + tautological C2) and SHA-256.

---

**Standard elements to include in the manuscript.**
- Author block, ORCID, email, address (matches Monat note).
- AI-disclosure paragraph (matches Monat note wording).
- Phantom-hit-rule disclosure paragraph.
- Bridge-repository citation.
- Zenodo preprint citation: DOI 10.5281/zenodo.19801038 (companion).
- AMS subject classification (matches Monat note: 11A55, 11J70, 11J81, 11Y65, 40A15) plus 39A06 (linear difference equations) for the new W1–W3 content.

**Distinctness from Monat note.**
- Title differs (this paper says "Empirical Evidence, an Algebraic Signature, and the Limits of Standard Asymptotic Methods"; Monat title is "The Transcendental Ratio Identity: A Conjecture on …").
- §4 (algebraic signature) and §5 (three negative results) are entirely new.
- §3 of this paper is a condensed restatement of Monat §§3–4.
- Standard cross-citation as the companion announcement.
