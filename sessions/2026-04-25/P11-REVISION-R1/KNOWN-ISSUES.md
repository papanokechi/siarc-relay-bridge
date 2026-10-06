# Known issues: this draft of "A Complete Arithmetic Stratification of Degree-2 PCFs: The F(2,4) Base Case"

**Do not cite the results in this folder.** The paper (`main_R1.tex` and `main_R1.pdf`) is an unpublished draft. It was rejected by
Mathematics of Computation (April 2026) and by the Journal de Théorie des Nombres de Bordeaux (May 2026). A later
independent check of all 531,441 families in F(2,4) found that its main theorem on the rational stratum is false.
The files are kept unchanged as a record. This notice was added on 2026-10-06.

1. **The headline count is not a count of rational limits.** The draft says that "exactly 113,270" families are
   Rat (line 244 of `main_R1.tex`). The rule actually counted also files a family as Rat when a(0) = 0, but
   K = b(0) + K_{n≥1} a(n)/b(n) never uses a(0). Under that rule Brouncker's family, a(n) = n², b(n) = 2n + 1,
   whose limit is 4/π, is counted as rational. An independent census finds at least 68,878 rational limits. The
   count 113,270 could not be reproduced by any of the counting rules tried. Its own two parts,
   729 + 112,540 = 113,269, do not add up to it.

2. **The proof cites cases that cannot exist.** The proof of the Rat theorem (line 261) says the 1,971
   "numerical-not-structural" families "satisfy a(k) = 0 for some k ∈ {21, …, 100}". In F(2,4),
   a(k) = a₂k² + a₁k + a₀ with |aᵢ| ≤ 4. If a is not identically zero, any positive integer root k divides a₀
   (when a₀ ≠ 0) or equals −a₁/a₂ (when a₀ = 0), so k ≤ 4. No family terminates at any k from 21 to 100.

3. **The "if and only if" characterisation of Rat is false.** The theorem says termination (a(1) = 0, or
   a(k) = 0 for some k ≥ 2) accounts for all Rat families "with zero overlap" (line 252). At least 2,102
   convergent families in F(2,4) have a rational limit and a(k) ≠ 0 for every integer k ≥ 0. Example:
   a(n) = −3n² − 4n − 1, b(n) = −4n − 3, whose limit is −1.

Also, at least 40 convergent families in F(2,4) have a quadratic-irrational limit, which contradicts the main
theorem's "Alg(0)" (the Alg stratum is empty, i.e. no convergent family has an algebraic irrational limit).
Example: a(n) = −n² − 3n + 1, b(n) = −2n − 4, with limit −(3 + √13)/2.

A corrected treatment is in preparation. Until it appears, treat every count and every theorem in this draft as
unverified.
