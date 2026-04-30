# Mismatches list — SIARC 7-paper coherence audit
**Date:** 2026-04-30 — Task `SIARC-COHERENCE-AUDIT`

Each entry records: the two (or more) papers in disagreement, the
specific claim, the suggested fix, and the proposed triage tier
(T1 = blocks submission, T2 = pre-arXiv, T3 = nice-to-have).

---

## MM-01 — P06 carries the (2,2) degree-profile regression  [TIER 1]

**Papers:** P06 vs P11, T2B, UMB
**Location:** `tex/submitted/p06_desert_ijnt_submission/pcf_desert_negative_result.tex` line 314

**Claim in P06 (verbatim):**
> "we replayed the desert pipeline […] on the $24$ Trans-stratum families of the $\mathcal{F}(2,4)$ base case~\cite{P11}, **which lie at degree profile $(2,2)$** with coefficient bound~$4$"

**Conflict with cited P11 (Proposition `prop:deg21`):**
> "All $24$ $\Trans$ families have $a(n)$ quadratic and $b(n)$ linear: $a_2 \neq 0$, $b_2 = 0$. **This degree-$(2,1)$ profile** occurs in $100\%$ of $\Trans$ families …"

UMB §1.1 and T2B `def:trans-stratum` both adopt degree-(2,1) for the
Trans-stratum object. Per CMB note: "regression: UMB v0 said (2,2);
now (2,1)." P06 is the only file in the portfolio still using (2,2).

**Suggested fix:** in P06 line 314, replace
`degree profile $(2,2)$ with coefficient bound~$4$`
by
`degree-$(2,1)$ profile inside the coefficient-bound-$4$ space $\mathcal{F}(2,4)$`.
A second-pass re-render of the PDF and a fresh AEAL claim-line
(`degree-(2,1) Trans-stratum profile, P11 prop:deg21`) are required
before P06 can be re-submitted (CMB T2-D scheduled SICF run).

**Tier rationale:** P06 has been rejected at Math.Comp and is queued
for the next venue under T2-D. Re-arXiv'ing or submitting with the
old (2,2) string would propagate the regression. Blocks resubmission
→ T1.

---

## MM-02 — UMB and #14 use the same labels T0–T3 for incompatible taxonomies  [TIER 1]

**Papers:** UMB vs #14 (`paper4_takeuchi_outline.tex`)

**UMB definitions (§1.2 / `def:tier-T0..T3`):**
- T0 — algebraic limits over ℚ, uniformly bounded degree
- T1 — transcendental, certified by Mahler / Nesterenko criterion
- T2 — trans-stratum: $\mu(K(x)) = 2 + c/\log x + o(1/\log x)$
- T3 — barrier: Fuchsian uniformization itself degenerates

**#14 definitions (Abstract / §1):**
- Tier 0 — genuinely modular families with signature $(\infty,2,3)$, non-CM
- Tier 1 — arithmetic but cuspidal degenerations (Catalan)
- Tier 2 — non-arithmetic Fuchsian families excluded by Takeuchi's list
- Tier 3 — $d=2$ irregular, confluent-Heun-type families outside Fuchsian

**The two taxonomies are NOT translations of each other.** A reader who
moves from UMB Conjecture 2.1 ("$K(x)$ lies in tier T2") to #14
("Tier 2 = non-arithmetic Fuchsian, Takeuchi-excluded") would draw
the wrong inference.

**Suggested fix (recommended, low blast radius):** rename UMB tiers to
`A0–A3` (arithmetic-classification tiers) and rename #14 tiers to
`O0–O3` (obstruction tiers), or equivalently keep one set as
`T0..T3` and qualify the other set as `Tier‑0(obstr)..Tier‑3(obstr)`.
Then add a one-paragraph translation table in UMB §1.2 explaining the
inclusion `T2 (UMB) ⊃ Tier 2 (obstruction) ∩ {trans-stratum}`.

**Tier rationale:** UMB is the program statement and currently sits at
DOI 19885550 on Zenodo; #14 (Four-tier paper) is at
JNTH-D-26-00480 (per `f1_mathcomp_submission/references.bib`). Both
papers will continue to be cited together. The label collision is a
referee-magnet and could trigger a desk-reject at JNTH on
"clarity/exposition". → T1.

---

## MM-03 — UMB Conjecture 2.1 omits Class B (+1/4); T2B includes it  [TIER 1]

**Papers:** UMB vs T2B
**Location:** UMB `conj:t2b` (line 228) vs T2B `conj:completeness`,
`thm:classB-stieltjes`, `cor:classB-pi`

**UMB conjecture (verbatim):**
> "Let $\{K(x)\}$ be a PCF family of generic degree $(2,1)$ uniformized
>  by $\PSLZ$, satisfying the regularity conditions of companion
>  paper~T2B. Then $K(x)$ lies in tier T2, and **its trans-stratum
>  exponent satisfies $c_{\PSLZ,(2,1)} = -2/9$**."

**T2B Completeness Conjecture:**
> "The degree-$(2,1)$ Trans-stratum is exactly $\mathcal{T}_A \sqcup
>  \mathcal{T}_B$, with no third class. Equivalently: every convergent
>  generic-irrational integer degree-$(2,1)$ PCF has
>  $a_2/b_1^2 \in \{-2/9, +1/4\}$."

T2B explicitly identifies Class B (a₂/b₁² = +1/4, limits in ℚ·π⁻¹)
as part of the trans-stratum at degree-(2,1). UMB's conjecture, as
literally written, would be **falsified by the 16 Class B families
exhibited in T2B Section 4** if they meet T2B's regularity hypotheses
and qualify as T2 by UMB's μ-asymptotic definition.

**Suggested fix:** rewrite UMB `conj:t2b` as
> "… $K(x)$ lies in tier T2, and its trans-stratum exponent
>  $c_{\PSLZ,(2,1),A} = -2/9$ on the Class A locus
>  $\{a_2/b_1^2 = -2/9\}$ (T2B Theorem 2). On the Class B locus
>  $\{a_2/b_1^2 = +1/4\}$ the limits lie in $\mathbb{Q}\cdot\pi^{-1}$
>  (T2B Theorem 3) and the trans-stratum exponent is $+1/4$."

A new Remark right after the conjecture should disclose the
two-class structure and reference the T2B census.

**Tier rationale:** UMB's umbrella conjecture is the most-cited
single statement of the program. An external reader of UMB alone
could reasonably reject the conjecture as falsified by a 16-family
counterexample that T2B itself documents. Blocks UMB v3 release. → T1.

---

## MM-04 — UMB OP `prob:t2-d2-nonpsl` is partly resolved; UMB does not say so  [TIER 2]

**Papers:** UMB vs internal SIARC bridge result `UMB-GAMMA0-2-SWEEP` (2026-04-30)

UMB still lists `prob:t2-d2-nonpsl` as open. The bridge sweep
(commit pushed 2026-04-30, sessions/2026-04-30/UMB-GAMMA0-2-SWEEP)
returned a HALT_A: zero Trans families found at the predicted
ratios across Γ₀(2), G₄, G₅, G₆, and G₈, supporting the conjecture
that −2/9 is PSL₂(ℤ)-specific.

**Suggested fix:** in UMB, append a remark to `prob:t2-d2-nonpsl`:
> "*Status (2026-04-30):* a computational sweep of Γ₀(2) and the
>  Hecke triangle groups $G_4,G_5,G_6,G_8$ at the
>  $\Gamma$-predicted indicial ratios returned zero Trans
>  families (SIARC bridge, `UMB-GAMMA0-2-SWEEP`). The empirical
>  picture is consistent with the value $-2/9$ being
>  $\PSLZ$-specific; a structural proof is open."

**Tier rationale:** This is an evidence update, not a contradiction.
T2 (pre-arXiv) for next UMB push.

---

## MM-05 — Painlevé phrasing: UMB asks PVI, P08 proves PIII(D₆)  [TIER 2]

**Papers:** UMB `prob:painleve` vs P08 `thm:painleve`

UMB asks for "Painlevé VI with monodromy in Γ" as the
companion-Painlevé conjecture. P08 establishes
"degenerate Painlevé V, equivalently PIII($D_6$)" for the V_quad
family, which is a T3 (UMB-sense barrier) family, not a T2
trans-stratum family.

The two statements are not formally contradictory (different
families, different objects), but a casual reader could believe
P08 settles UMB's open problem when it does not.

**Suggested fix:** in UMB, qualify `prob:painleve`:
> "… correspondence between **trans-stratum (T2)** PCF families and
>  solutions of Painlevé~VI… The companion paper~P08 establishes a
>  **separate** PIII($D_6$) link for the T3 (irregular,
>  confluent-Heun) V_quad family; the T2 ↔ PVI correspondence
>  remains open."

**Tier rationale:** clarity, not correctness. T2.

---

## MM-06 — UMB does not cite T2A in §5 census problem  [TIER 2]

**Papers:** UMB `prob:census` vs T2A

UMB's `prob:census` says: "Extend the empirical census underlying
Conjecture~\ref{conj:t2b} beyond degree-(2,1)." T2A
(`t2a_paper_draft.tex`, Zenodo 19774029) does exactly that at
degree-(4,2): 1162/1162 Trans-hard at CMAX=1 and 1000/1000 at
CMAX=2, with a novel candidate $R_1$. UMB does not cite T2A.

**Suggested fix:** add a `\cite{T2A}` reference in `prob:census`
and an entry in UMB §6 program-papers table for T2A with DOI
10.5281/zenodo.19774029.

**Tier rationale:** evidence completeness. T2.

---

## MM-07 — T2A's bibliography has stale P11 venue (Math.Comp → JTNB)  [TIER 2]

**Papers:** T2A vs P11 / submission_log

`t2a_paper_draft.tex` line ~628 cites P11 as
> "Mathematics of Computation submission `260422-Papanokechi`."

Per CMB and `tex/submitted/submission_log.txt` row 24, P11 is now at
JTNB (ID: JTNB-2400, submitted 2026-04-28).

**Suggested fix:** in T2A `\bibitem{PCF24}`, replace the Math.Comp
note by
> "Submitted to Journal de Théorie des Nombres de Bordeaux,
>  ID JTNB-2400 (2026-04-28)."

**Tier rationale:** T2A is already published on Zenodo; this only
affects a v2 reupload. T2.

---

## MM-08 — Two distinct papers carry the "Paper14"/"#14" name  [TIER 2]

**Papers:** UMB vs `paper14-ratio-universality-SUBMISSION.tex`

UMB cites `\bibitem{Paper14}` = "Four-tier classification of
PSL₂(ℤ)-uniformized PCFs" (= `paper4_takeuchi_outline.tex`, P11
references it as `\cite{spectral}` JNTH-D-26-00480). The file
`tex/submitted/paper14-ratio-universality-SUBMISSION.tex` is a
**different** paper (Ratio Universality for Meinardus-Class
Partition Functions; CMB row P13, Acta Arith).

A reader doing a workspace search for "paper14" lands on the
partition-functions paper instead of the four-tier paper.

**Suggested fix:** rename
`paper14-ratio-universality-SUBMISSION.tex` →
`paper13-ratio-universality-SUBMISSION.tex` (matches CMB P13 label)
**or** rename `paper4_takeuchi_outline.tex` →
`paper14_four_tier_takeuchi_outline.tex`. Either way, fix the
`\bibitem{Paper14}` key in UMB to match.

**Tier rationale:** filename collision; recoverable via grep, no
mathematical impact. T2 (or T3 if conventions are kept stable
internally).

---

## MM-09 — UMB never cites its own concept DOI 19885549  [TIER 3]

**Paper:** UMB only

UMB's program-papers table cites itself as the version DOI
10.5281/zenodo.19885550 but never the concept DOI 19885549. Best
Zenodo practice is to cite the **concept** DOI for citation
stability across versions.

**Suggested fix:** in the program-papers table row "UMB", replace the
version DOI by the concept DOI 19885549, and add a footnote with
the version DOI 19885550.

**Tier rationale:** stylistic/best-practice. T3.

---

## MM-10 — P11 references list outdated `\cite{contamination}` and `\cite{spectral}` venues  [TIER 3]

**Paper:** P11 (`f1_mathcomp_submission/references.bib`)

- `@article{contamination}` `note = "Submitted, submission 261945835 (2026-04-20)"`. Per CMB row P01 this paper was **REJECTED** at Exp. Math.; the note should reflect status (rejected; under revision for next venue).
- `@article{spectral}` `note = "Submitted, JNTH-D-26-00480"`. Verified vs submission_log: status not changed, note OK at audit time. (Listed for completeness.)

**Suggested fix:** in `references.bib`, update the `contamination`
note to "Rejected at Experimental Mathematics (submission
261945835); revision in preparation."

**Tier rationale:** P11 is at JTNB awaiting verdict; cannot
re-upload until referee report. Cosmetic. T3.

---

## Summary

| MM | Description | Tier |
|---|---|---|
| 01 | P06 (2,2) regression vs P11 (2,1) | **T1** |
| 02 | UMB & #14 use T0..T3 for incompatible taxonomies | **T1** |
| 03 | UMB Conjecture omits Class B / contradicts T2B | **T1** |
| 04 | UMB OP `prob:t2-d2-nonpsl` not updated with HALT_A | T2 |
| 05 | Painlevé phrasing UMB(PVI) vs P08(PIII D₆) | T2 |
| 06 | UMB does not cite T2A in `prob:census` | T2 |
| 07 | T2A bib has stale Math.Comp venue for P11 | T2 |
| 08 | Two papers share "Paper14" name | T2 |
| 09 | UMB self-citation uses version DOI not concept DOI | T3 |
| 10 | P11 bib note: `contamination` rejection not reflected | T3 |
