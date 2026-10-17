**Addendum (2026-10-17) to the KNOWN-ISSUES notice of 2026-10-06 (commit fd6cfda).** These issues are in addition to those already listed.

1. **Trivial-zero count.** The paper states 729 families with a(1) = 0 (`main_R1.tex`, line 247). The correct count is 44,469: 61 of the 729 numerator polynomials satisfy a(1) = 0, times 729 denominators. The figure 729 counts only a(n) ≡ 0.
2. **Termination count.** The largest positive integer root of any nonzero a(n) in F(2,4) is 4. At most 67,068 families have a(k) = 0 for some k ≥ 1, plus 729 with a(n) ≡ 0. The stated 112,540 terminations are impossible. This supplements the k ∈ {21..100} item already listed.
3. **The −2/9 law (abstract).** The abstract generalizes a₂/b₁² = −2/9 from three examined families to the Trans stratum. The 4/π family a(n) = n², b(n) = 2n+1 is Trans by the paper's own criterion and has a₂/b₁² = 1/4.
4. **Convergent count.** Two independent recomputations under the paper's stated criterion give 510,658 (the blind run) and 510,740 (the external referee's report, item 5b), not 513,387. The count moves by several hundred with the tolerance and NaN handling, since the criterion is heuristic and implementation-sensitive.
5. **Arithmetic.** 729 + 112,540 = 113,269, not 113,270. 513,387 − 113,270 = 400,117, not 400,119.
6. **The Trans count.** At least 54 families satisfy the Trans criterion numerically, forming 27 classes under b → −b. All have zero π² coefficient (Möbius images of π). This replaces "24".
7. **Transcendence wording.** The transcendence argument applies Lindemann to identities that were established numerically, not proved. "Rigorous" should read "conditional on the numerical identities".
8. **Problem 1.** F(3,4) has 9⁸ families, not 9⁶.

Evidence: items 1, 2, 3, 5 and 8 above, and the Alg(0) counterexamples cited in the notice of 2026-10-06, are checked by `check_census_addendum.py`, committed beside this notice; it needs only Python 3 and mpmath and works from the paper's definitions. Items 4 and 6 rest on a blind full recomputation and an independent referee recomputation (both 2026-10-16); the frozen outputs, with SHA-256 hashes, are available on request.
