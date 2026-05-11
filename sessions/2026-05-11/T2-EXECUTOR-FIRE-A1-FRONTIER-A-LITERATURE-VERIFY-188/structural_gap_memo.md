# Structural-Gap Memo — Frontier-A "PIII(D₆) hierarchy" claim audit

**Date:** 2026-05-11
**Bridge predecessor:** slot 185 (`5ba0072`)
**Slot 181 prior:** `8c7b1b5` HALT_E_LITERATURE_NULL (18 keyword/author probes; did NOT specifically test "Painlevé III hierarchy" phrase)
**Verdict:** **HALT_A1_GAP_CLOSED** for broad "PIII hierarchy" scope; **narrow Sakai-classification scope (PIII(D₆) specifically) remains plausibly open** but needs operator + Claude re-vet

---

## Phase B query variants — results

### Variant Q01 — "Painlevé III hierarchy" (exact phrase)

**arxiv.org/search:** Returned **4 hits** with explicit phrase match:

1. **arXiv:1806.00545** — Bilman, D.; Ling, L.; Miller, P.D. — "Extreme Superposition: Rogue Waves of Infinite Order and the Painlevé-III Hierarchy" — Duke Math. J. 169(4) (2020) 671-760, DOI:10.1215/00127094-2019-0066. Quote: *"The spatial differential equations are identified with certain members of the Painlevé-III hierarchy."* **Submitted June 2018.**

2. **arXiv:** (Bilman, D.; Buckingham, R.) "Large-order asymptotics for multiple-pole solitons of the focusing nonlinear Schrödinger equation" — *"the solitons converge to functions satisfying the second member of the Painlevé-III hierarchy in the sense of Sakka."* **Submitted July 2018.** Explicitly references **Sakka's PIII hierarchy** as an established named construction.

3. **arXiv:** (Atkin, Max R.) "The Lenard Recursion Relation and a Family of Singularly Perturbed Matrix Models" — *"a Painlevé III hierarchy recently proposed by the author can be connected to the Lenard recursion formula."* **Submitted February 2015.** Explicitly states Atkin had **previously proposed a Painlevé III hierarchy** (in 1501.04475 below).

4. **arXiv:** (focusing complex mKdV / multi-rational solitons, December 2024) — *"are identified with certain members of the Painlevé-III hierarchy."* **Submitted December 2024.** Uses the PIII hierarchy as established machinery.

### Web-search supplement (cross-verification):

5. **arXiv:1501.04475** — Atkin, M.R.; Claeys, T.; Mezzadri, F. — "Random matrix ensembles with singularities and a hierarchy of Painlevé III equations" (January 2015). Quote: *"Our results are described in terms of **a hierarchy of higher order analogues to the Painlevé III equation, which reduces to the Painlevé III equation itself when the pole is simple**."* **This is an explicit construction of higher-order PIII analogues** indexed by the order of the pole singularity in random-matrix potentials. Directly competes with Frontier-A's intended construction.

6. **arXiv:2512.19381** — Wang, Z.; Xu, X. — "Asymptotic and monodromy problems for higher-order Painlevé III equations" (December 2025). Studies isomonodromic deformations for n×n linear ODE systems with two second-order poles; explicit Stokes-matrix and connection-matrix formulae; applies to tt* equations. **The most recent (December 2025) literature on higher-order PIII**, only 5 months before Frontier-A's intended fire.

### Variant Q02 — "Painlevé D6 hierarchy" (Sakai-classification notation)

**arxiv.org/search:** **0 hits**.

### Variant Q03 — "Sakai D6 hierarchy"

**arxiv.org/search:** **0 hits**.

### Variant Q04 (supplemental) — "PIII(D6) hierarchy"

**arxiv.org/search:** **0 hits**.

### Citation-graph scan (entries 1-2 anchors)

**Not executed** in this fire — Q01 results alone are decisive for the gap-claim falsification. Citation-graph scan would only confirm; opportunity cost vs immediate HALT-surface deemed unfavorable.

---

## Verdict

### Broad scope ("Painlevé III hierarchy" exists in literature)

**FALSIFIED.** Multiple independent constructions of "Painlevé III hierarchy" / "higher-order Painlevé III equations" exist on arXiv, with at least 4 distinct named formulations:

| Author / Source | Construction approach | Year | arXiv |
|---|---|---|---|
| Sakka (referenced by Bilman-Buckingham 2018) | "in the sense of Sakka" — original Sakka PIII hierarchy | (pre-2018) | likely Sakka 2009 J.Phys.A 42 025210 or similar |
| Atkin | Lenard recursion construction | 2015 | (separate paper referenced in Atkin Feb 2015) |
| Atkin-Claeys-Mezzadri | Random-matrix higher-order-pole singularities | 2015 | 1501.04475 |
| Bilman-Ling-Miller | NLS rogue waves of infinite order | 2018 | 1806.00545 |
| Wang-Xu | n×n linear ODE systems with two 2nd-order poles | 2025 | 2512.19381 |

Slot 181's HALT_E_LITERATURE_NULL signal **does NOT hold** when expanded with the "Painlevé III hierarchy" exact phrase. Slot 181 used 18 keyword/author probes per its handoff but did not include this phrase as a primary search term — this fire is the first to test it directly.

### Narrow scope ("PIII(D₆) Sakai-classification" hierarchy)

**REMAINS PLAUSIBLY OPEN.** Specific Sakai-classification notation ("PIII(D₆)", "Painlevé D6", "Sakai D6") returns **0 arxiv hits** in this fire's 3 query variants. The existing PIII hierarchy constructions (Sakka, Atkin, Atkin-Claeys-Mezzadri, Bilman-Ling-Miller, Wang-Xu) are NOT framed in the Sakai-D₆⁽¹⁾ surface-preserving language; they use:

- **Matrix-model / random-matrix** formalism (Atkin-Claeys-Mezzadri, Atkin)
- **NLS / rogue-wave** asymptotics (Bilman-Ling-Miller, Bilman-Buckingham)
- **Isomonodromic-deformation / Stokes** formalism (Wang-Xu)
- **Lenard recursion** (Atkin)

A Sakai-geometric construction (surface-type-preserving, classified by D₆⁽¹⁾ affine root system, in the original Sakai-2001 language) would be **methodologically distinct** from all 5 prior constructions — but Frontier-A would need to:

1. **Demonstrate** that the existing 5 constructions do NOT coincide with the Sakai-D₆⁽¹⁾ surface-preserving construction (e.g., that they don't preserve the D₆⁽¹⁾ surface type at higher orders).
2. **Re-frame** the contribution as "Sakai-geometric construction of a PIII hierarchy" — NOT as "first PIII hierarchy" or "structural gap in literature".
3. **Cite** all 5 prior constructions in the eventual preprint and contextually relate them.

---

## Recommendation to operator + Claude (T1-Synth)

**HALT_A1_GAP_CLOSED.** Frontier-A scope must be re-vet BEFORE any FIRE-A2 (n=2 derivation) or FIRE-A3 (hierarchy inductive scheme) work proceeds.

Specifically:

1. The structural-gap framing of slot 185 verdict ("no PIII hierarchy exists in the literature") is **falsified at the broad scope** and must be abandoned.
2. The narrow Sakai-D₆⁽¹⁾-specific scope may still be defensible BUT requires preliminary demonstration that the 5 existing constructions are not Sakai-D₆⁽¹⁾ surface-preserving in disguise.
3. Required pre-FIRE-A2 work: **acquire and read** Atkin-Claeys-Mezzadri 2015 (arXiv:1501.04475), Bilman-Ling-Miller 2018 (arXiv:1806.00545), Wang-Xu 2025 (arXiv:2512.19381), Atkin 2015 (Feb), and the original Sakka PIII hierarchy paper. Compare with intended Sakai-geometric construction in detail.
4. The Mazzocco-Mo 2006 (PII hierarchy Hamiltonian structure) anchor methodology may still be transposable to PIII(D₆) — but Frontier-A is **not first** in any PIII hierarchy sense; only in a specific Sakai-classification sense if the comparison in step 3 confirms novelty.

Downstream impact on slot 185 Amendments:

- **Amendment-1 (10/10 PENDING-VERIFY):** 7/8 external identifiers verified PASS; 1/8 (entry 4 Joshi-Lustri-Topp) RETRACTED. Amendment-1 LOAD-BEARING gate does NOT close cleanly even ignoring Q01 finding.
- **Amendment-2 (acquisition flags):** entries 5+6 BOTH openly accessible on arXiv. CLEAR. (But moot if Frontier-A re-scopes.)
- **Amendment-3 (substrate-relevance of LR 2024):** confirmed PIII(D₆)-relevant (paper explicitly covers PIII₃ = PIII(D₆) degeneration). CLEAR.
- **Amendment-4 (FIRE-A2 dual-witness MEDIUM ceiling):** moot until Frontier-A re-scopes.

The cascading impact: FIRE-A2 + FIRE-A3 are **SUSPENDED** pending re-vet outcome.

---

## Halt rationale (per FIRE-A1 prompt halt-mode matrix)

| Halt mode | Triggered? | Evidence |
|---|---|---|
| HALT_A1_ANCHOR_RETRACTED | NO | Both anchors (entries 1+2 Mazzocco-Mo + Bobrova-Mazzocco) PASS verification |
| HALT_A1_ACQ_FAIL | NO | Entries 5+6 (IILZ-2025 + LR-2024) both openly accessible on arXiv |
| **HALT_A1_GAP_CLOSED** | **YES** | Q01 returned 4 PIII-hierarchy-named arXiv hits; web search confirmed 2 more (Atkin-Claeys-Mezzadri 2015 + Wang-Xu 2025); 5 distinct construction approaches exist in literature. Slot 181 NULL signal does NOT hold under "Painlevé III hierarchy" exact-phrase search. |
| CLOSE_WITH_AMENDMENT | (subordinate to HALT) | Entry 4 Joshi-Lustri-Topp 2014 retraction would default here ONLY if Q01 had returned NULL — superseded by HALT_A1_GAP_CLOSED. |

**Halt mode: HALT_A1_GAP_CLOSED.**
