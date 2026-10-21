# Corrections for the referees

*An exponential-period representation of the V_quad constant* — corrections to
the submitted version. **Draft; not sent, not submitted.**

---

**1. The Sakai surface type D₅⁽¹⁾ is conjectural, not established.**
The submitted version states in the abstract, §1.1, §4 and §7.1 that V_quad is
the rank-one standalone closure *on* the Sakai surface D₅⁽¹⁾. That
identification is Conjecture 4.1 of the companion paper, not a theorem. Every
occurrence is now hedged. No result in this paper depends on it: Theorems 1.1
and 1.2, the main identity and its three verifications are statements about the
operators L_φ and L_V and the cycle γ alone. The companion's version 1.3
correction notice additionally revises the derivation by which the quoted
Painlevé parameters θ_∞ = 2/√3 and α = 1/6 were obtained; the reference is added
as [26], while [2] remains pinned to version 1.2.

**2. §7.1 claimed too much.** The submitted version says the paper "completes
part (ii)(a) for d = 2". It does not. What is established is an *instance* of
part (ii)(a) for the single representative V_quad, transcendental under the two
hypotheses of Corollary 1.4, and attached to the D₅⁽¹⁾ stratum only through the
conjectural identification above. Nothing here is proved for any other member of
the stratum, and nothing here proves that V_quad belongs to it.

**3. Theorem 1.2 is proved once, by Kovacic's algorithm — not twice.**
The submitted version says the differential Galois group of L_φ is SL₂(ℂ)
"proved twice", the second proof being a structural torus-plus-unipotent
argument, described as independent in §1.3, §1.4, the proof of Theorem 2.2 and
Appendix A.2/A.5. That is wrong on both counts. The structural argument gives a
maximal torus together with one root unipotent, which generates a **Borel
subgroup** — a proper subgroup of SL₂(ℂ). Reaching SL₂(ℂ) requires excluding the
reducible case, and that exclusion *is* Kovacic's Case 1. The structural
argument is therefore a consistency check on the same computation, conditional
on it, not a second and independent proof. Every claim of independence for it
has been removed and the argument restated correctly. (The separate claim that
the three *verification methods* A, B and C are structurally independent is
unaffected and stands.)

**4. ξ = 0 is not an apparent singularity of L_V. It carries a logarithm.**
This is a correction the referees did not raise, found while checking the claim.
The submitted version asserts apparency at ξ = 0 in Proposition 2.4, Lemma 2.7,
Table 1, Remark 3.3, the figure and the proof of Corollary 1.4, on the ground
that the four local exponents are consecutive integers. That ground does not
support the conclusion — consecutive integer exponents make the point
**resonant**, which is precisely the situation in which a logarithm can be
forced — and in fact one is.

Taking L_V exactly as printed in Appendix A.1 and computing in exact ℚ(√3)
arithmetic: the exponents at ξ = 0 are {−1, 0, 1, 2}; the first resonant step of
the Frobenius recursion started from the lowest exponent −1 is obstructed by the
nonzero element (38286 + 24984√3)/418501; there is therefore no formal solution
with leading exponent −1; the log-free local solution space has dimension 3, and
the fourth local solution carries log ξ, with leading log coefficient normalised
to v₀ = −(2 + √3)/24. So ξ = 0 is a genuine regular singular point of L_V with
unipotent local monodromy.

**The main identity is unaffected.** B̂ is the holomorphic exponent-0 solution,
which is all Lemma 2.7 and Theorem 1.1 use, and the Hankel cycle γ runs on
(−∞, −2/√3] and does not approach 0. Every affected statement has been corrected
and the computation is recorded in the new Appendix A.3. It was checked by three
implementations sharing no code, with a positive and a negative control, both of
which fired. The same defect is recorded independently as item C1 of the
companion's version 1.3 correction notice.

---

Revised manuscript: 26 pages (was 24), 0 undefined references, 0 undefined
citations. All existing citation numbers are unchanged; the single new reference
is [26].
