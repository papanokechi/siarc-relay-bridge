# Corrections for the referees — MATH-D-26-00523

*All references are to the submitted manuscript, v1.2 (25 pages).*

The author has found five errors in the submitted manuscript. Four are
corrections of overclaims; one corrects a mathematical statement. The paper's
main identity is unaffected by all five.

---

### 1. The Sakai surface type D₅⁽¹⁾ is conjectural, not established

*Abstract, §1.1, §1.2, §7.1.* The manuscript states the surface identification
as fact. It rests on Conjecture 4.1 of the companion paper and should be read as
conditional throughout. The companion's v1.3 correction notice also revises the
derivation of the Painlevé parameters quoted in §1.1.

### 2. §7.1 does not complete part (ii)(a) for d = 2

The claim that the construction "completes part (ii)(a) for d = 2" is withdrawn.
What is established is an **instance** of part (ii)(a) for the single
representative V_quad, conditional on the surface identification of item 1. It
is not established for the stratum.

### 3. Theorem 1.2 is proved once, not twice

The manuscript presents a structural argument as an independent second proof.
It is not independent. A torus together with one root unipotent generates a
**Borel** subgroup; the step from Borel to SL₂(ℂ) uses Kovacic Case 1 exclusion
of reducibility — the same exclusion the first proof rests on.

**Kovacic case-elimination is the proof.** The structural argument is a
consistency check on it. Affected: Theorem 1.2, §1.3, §1.4, the proof in
§2.2 and the paragraph following it, and Appendix A.2 and A.5.

### 4. ξ = 0 is **not** an apparent singularity — it carries a logarithm

This is the one mathematical correction.

The manuscript reasons that the four local exponents at ξ = 0 are consecutive
integers and concludes the point is apparent. **Consecutive integer exponents do
not imply apparency**; they make the recursion resonant, and whether a logarithm
appears has to be computed.

It was computed exactly over ℚ(√3), with no floating-point arithmetic, from the
lowest exponent −1. **A logarithm is forced.** ξ = 0 is a regular singular point
with logarithmic local behaviour.

Affected: Proposition 2.4, Lemma 2.7, Table 1,
Remark 3.4, Figure 1 and its caption, and the proof of
Corollary 1.4.

**The main identity is unaffected.** B̂ is holomorphic at ξ = 0 on the principal
sheet, and the integration cycle does not approach the point; the period
computation never used apparency, only that holomorphy. The correction removes a
false justification, not a step.

### 5. Methods B and C are not independent of one another

*Abstract, §1.3, Theorem 1.1, §5, Table 2.*

The manuscript describes three "structurally independent" determinations of the
constant. Methods B and C are not independent as derived: the displayed
derivation in §5.3 begins by substituting A = (S/2πi)·Γ(1+β), so the Stokes
datum S enters Method B through the amplitude, and Method C uses the same A–S
relation. The agreement reported for Method B, 8.84482×10⁻⁴⁶, is therefore
algebraically **the same quantity** as Method C's, not a second measurement.

There **is** a genuinely S-free check, and the revision reports it instead: the
amplitude extracted directly from the coefficient stream, with no reference to
S, reconstructs S to **3.69×10⁻⁴⁶**. That check is independent; the printed
derivation was not.

Method A's independence is stated in the revision as **inferred**, not measured,
because it has not been measured.

The value of the constant, and the identity, are unchanged. What changes is the
claim about how many independent routes reach it.

---

**Summary.** Items 1, 2, 3 and 5 weaken claims the manuscript should not have
made. Item 4 corrects a false statement about the singularity at ξ = 0 whose
consequences were, fortunately, never used. The constant, the exponential-period
representation, and the numerical agreements are unaffected.
