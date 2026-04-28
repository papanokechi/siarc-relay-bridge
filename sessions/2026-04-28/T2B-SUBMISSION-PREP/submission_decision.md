# T2B Submission Decision

**Task:** T2B-SUBMISSION-PREP
**Date:** 2026-04-28
**Researcher:** Claude Opus 4.7 (strategy) / GitHub Copilot (execution)

## 1. Selected title

**Option A** — "The Transcendental Ratio Identity for Degree-$(2,1)$ Polynomial
Continued Fractions: A Birkhoff–Trjitzinsky Resonance and the $k=2$ Selection
Mechanism"

**Reasoning.**
- Option B ("a resonance-theoretic *proof* of the $-2/9$ identity") overclaims:
  the paper proves Theorem 1 (the resonance family) but the $-2/9$ identity
  itself is conjectural, gated on the unwritten $\Delta_2 = 0$ lemma.
  Submitting under Option B is the most likely scope-mismatch desk-reject
  trigger.
- Option C is descriptive but mutes the novel theoretical contribution
  (the BT resonance + Stokes framework).
- Option A is precise: advertises the proved theorem, names the framework,
  and is honest that $k=2$ is a *selection mechanism* not a full identity
  proof. "Birkhoff–Trjitzinsky" signals to the difference-equations
  community at a glance.

## 2. Venues

### Primary: Ramanujan Journal
- Scope: continued fractions, transcendence/irrationality, computer-
  discovered identities — all core territory.
- Tolerance: explicitly welcomes hybrid computational + theoretical papers
  and well-supported conjectures paired with a proved structural theorem.
- Length: 6–8 pages is short but acceptable for a letter-style structural
  result.
- Turnaround: moderate (typical 4–8 months to first decision).

### Backup: Journal of Difference Equations and Applications (JDEA)
- The BT machinery, resonance-locus characterization, and the codimension
  counting in $\Delta_k$ are squarely in JDEA's scope.
- Re-positioning strategy if Ramanujan J. desk-rejects: lead with
  Theorem 1 as a clean result on second-order linear difference equations
  with polynomial coefficients, with the PCF identity as motivating
  application.

### Rejected
- **Research in Number Theory:** leans toward fully proved arithmetic
  results; conjecture-heavy submission carries elevated desk-reject risk.
- **Aequationes Mathematicae:** functional-equations focus, weaker fit,
  slower turnaround.

## 3. Cover letter (148 words)

> Dear Editors,
>
> Please consider our manuscript, "The Transcendental Ratio Identity for
> Degree-$(2,1)$ Polynomial Continued Fractions," for publication in the
> Ramanujan Journal.
>
> The paper proves (Theorem 1) that the integer-resonance loci of the
> Birkhoff–Trjitzinsky characteristic polynomial of a degree-$(2,1)$ PCF
> are exactly $a_2/b_1^2 = -k/(k+1)^2$, $k \ge 1$. The novel theoretical
> contribution is the resulting Stokes-multiplier framework, which reduces
> the empirical $-2/9$ phenomenon to a single codimension-one selection
> condition at $k=2$ and predicts the observed desert at $k\ge 3$.
>
> The framework is supported by an exhaustive search of $\sim$150,000
> convergent generic-irrational families with zero counterexamples,
> including 134,040 candidates at $k=3$. The selection mechanism itself
> ($\Delta_2 = 0$) is stated as a conjecture.
>
> AI disclosure: portions of the search infrastructure and exposition
> were assisted by AI tools under author supervision.
>
> Sincerely,
> SIARC Collaboration

## 4. Desk-rejection risk + mitigation

**Single most likely risk.** An editor scanning the abstract sees
`[PENDING]` and `[VERIFIED]` markers, a conditional Theorem 2, and a
framing Conjecture, and concludes the paper is preliminary / incomplete —
desk-rejecting before peer review. With a 6–8 page submission and three
visibly open items, this is the dominant failure mode.

**Mitigation (two-part):**

1. **Strip `[PENDING]` / `[VERIFIED]` tags from the submitted abstract.**
   They are appropriate for an internal SIARC draft but read as "work in
   progress" to an editor. Replace with standard mathematical hedges
   ("we conjecture," "we verify symbolically that"). Retain the markers
   only in the internal version.

2. **Cover-letter framing (already applied above):** lead with Theorem 1
   as a self-contained proved result; frame the Stokes framework as the
   paper's contribution, with $\Delta_2 = 0$ as a precise, falsifiable
   consequence — not as a gap. The phrase "reduces the empirical $-2/9$
   phenomenon to a single codimension-one selection condition" presents
   the conjecture as a *theorem-shaped reduction*, which is the correct
   editorial framing.
