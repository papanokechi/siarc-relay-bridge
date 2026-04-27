# Handoff — SPRINT-W4-EMPIRICAL-PAPER-DRAFT
**Date:** 2026-04-27
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~50 minutes
**Status:** COMPLETE (with two author-decision points flagged)

## What was accomplished

Drafted the full extended paper *"The Trans −2/9 Identity for Degree-(2,1) Polynomial Continued Fractions: Empirical Evidence, an Algebraic Signature, and the Limits of Standard Asymptotic Methods"* incorporating the W1/W2/W3 sprint findings as new content beyond the existing Monatshefte conjecture note. Produced the outline (`trans_minus29_outline.md`), the full LaTeX manuscript (`trans_minus29_full.tex`), and a clean compiled PDF (`trans_minus29_full.pdf`, 14 pages, 2-pass pdflatex, exit 0).

## Outline status

- **Outline (`trans_minus29_outline.md`):** complete, with explicit cross-references to the Monatshefte note for shared content (§§1, 2, 3) and the new content cleanly factored (§4 algebraic signature, §5 three negative results). Maps the source-of-content for each section (Monat note vs. W1/W2/W3 sprint reports).

## Manuscript status

- **Compiled:** YES, two `pdflatex` passes, EXIT 0, no errors.
- **Page count:** 14 (target was 18–25; see "Length" below).
- **Theorems / propositions inserted:**
    - Thm 3.1 (plus-form indicial pair {1/3, 2/3} on r = −2/9; trivial restatement of Monat Prop 2.3).
    - Conj 3.2 (Trans −2/9 conjecture, restated from Monat).
    - Lem 4.1 + Thm 4.3 (algebraic signature `|μ_+/μ_-| = (13+3√17)/4`, with `a₂ < 0` sign condition; new).
    - Thm 4.4 (PSLQ certificate [13, 3, −4]; new).
    - Prop 5.1 (W1 indicial closed form `α(μ) = -((b₁-b₀)μ + a₁-a₂)/(b₁μ - 2a₂)`).
    - Lem 5.2 + Thm 5.3 (W1 compatibility ideal C and integer-grid obstruction; the irrational `(27±√17)/18` result).
    - Prop 5.4 (W2 leading-order invariant negative result).
    - Prop 5.5 + Cor 5.6 (W3 sub-leading c₁ factorization `A_num = (a₂ − b₁μ)(4 a₂ − b₁²)`; resonance happens only on Alg discriminant-zero, never on Trans).
    - Prop 5.6 + 5.7 (W3 convergence-rate and direct-PSLQ negative results).
- **Tables:** 3 reproduced from Monat note (censuses, resonance, log-anomaly) + 2 new (sign-convention dictionary, SHA-256 hashes).
- **Standard elements:** Author block + ORCID, AI-disclosure, phantom-hit discipline disclosure, bridge repository citation, Zenodo DOI 10.5281/zenodo.19801038 cited.

## Length

The compiled draft is **14 pages**, below the 18–25 target. Density is high and the W1/W2/W3 results are cited rather than derived inline. A natural expansion to ~20 pages would (a) expand the symbolic derivations of Prop 5.1, Lem 5.2, and Prop 5.5 inline (currently each is cited to the corresponding sprint report); (b) add a §6.5 "Towards a Galois-of-difference-equations proof" sub-section discussing van der Put–Singer; and (c) add a Schwarz-list dihedral subsection elaborating Remark 4.5. Recommended for a follow-up polish session before submission.

## Key mathematical content inserted

1. The new √17 algebraic signature (Theorem 4.3) and PSLQ certificate (Theorem 4.4) — entirely new vs. Monat.
2. Sign-convention dictionary (Table 1) reconciling the Monatshefte plus-form `λ²−λ−r=0` with the W1/W2/W3 minus-form `μ²−b₁μ+a₂=0`. *This is critical — the two sign conventions produce different rational/irrational pictures on the Trans locus, and without the dictionary the W1 "irrational compatibility ideal" result would appear to contradict the Monat "indicial {1/3, 2/3}" result.*
3. The triple appearance of √17 (char-root discriminant; W1 b₀/b₁ obstruction; sub-leading on-Trans c₁ value) framed as the "algebraic shadow" of the Trans property.
4. Four open problems framed in (i) Galois-of-difference-equations (van der Put–Singer), (ii) isomonodromic deformation (Jimbo–Sakai q-analogue of Painlevé VI), (iii) rational-coefficient extension, (iv) Log-anomaly classification.

## Judgment calls made

- **Sign-convention reconciliation.** The Monat note uses plus-form (so {1/3, 2/3} is automatic on r = −2/9) and the W1/W2/W3 sprints use minus-form (so the indicial pair on Trans is irrational, with discriminant 17). Without explicit reconciliation, the W1 negative result would read as a contradiction of the Monat note. I added §2.2 ("Two recurrence conventions") with Table 1 to fix this. The choice to use minus-form for §§4–5 is justified because that is the natural setting for the Birkhoff `Γ(n+1)·μⁿ·n^α` ansatz that the sprints used.
- **Sign condition on Theorem 4.3.** The iff requires `a₂ < 0`; without it the q = +(13+3√17)/4 branch gives r = +2/17 (a positive-Worpitzky family). I flagged this as Remark 4.5 and noted it explicitly in the theorem statement.
- **Length.** Compiled to 14 rather than 18–25. I prioritised completeness and correctness over padding; expansion to target length is a polish step.

## Anomalies and open questions

- **The Vieta-tautology framing of Theorem 4.3** is an honest weakness. The signature is "Vieta-tautological" yet contains the new information that the discriminant `√17` shows up explicitly. Some referees may push back: "this is a re-encoding of r = −2/9, not an algebraic invariant." Remark 4.5 is the defence; whether it convinces is venue-dependent.
- **The W1 negative result depends on minus-form.** Under plus-form (Monat convention), there is no "compatibility ideal" obstruction at all — {1/3, 2/3} is automatic on Trans. So the W1 negative result, while real and interesting, only appears as a result *because we changed conventions*. A skeptical referee might call this "not a negative result, just an artifact of choosing the harder formulation". I have framed §5.1 carefully (Remark after Thm 5.3) but the issue should be revisited with Claude.
- **No new mathematics is unconditionally proved beyond the Monat note.** Theorem 4.3 is Vieta. The negative results are negative. The conjecture is unchanged. The paper's value is *structural*: it sharpens the framing, exposes √17, and bounds local methods. Whether this is enough for IMRN/Ramanujan J. is unclear; for JNT or Monat-extended it is plausible.
- **Length under target.** As noted above.

## CRITICAL AUTHOR DECISIONS NEEDED

### Decision 1 — Monatshefte / dual-submission conflict

The Monatshefte submission (9 pages, conjecture only, currently under review) and this paper (14 pages, full investigation) **cannot both be under review at different journals** without explicit disclosure to both editorial boards. Standard ethical options:

1. **Withdraw Monatshefte and submit this paper to a stronger venue** (recommended if the author is willing to risk a longer review queue).
2. **Position Monatshefte as "announcement", this as "full version"** — submit this to a *different* venue with explicit cross-reference and notification to both editors. Some venues (Ramanujan J., JNT) allow this; others (IMRN) do not.
3. **Wait for Monatshefte decision before submitting this paper anywhere.** Lowest-risk option but slowest.

### Decision 2 — Venue ranking for the full paper

Suggested venues, ranked by (i) topical fit, (ii) likely tolerance for an "empirical + structural negative results" paper, (iii) compatibility with Decision 1 above:

1. **Ramanujan Journal** — strong topical fit (PCFs, special functions, experimental mathematics), tolerant of empirical-heavy papers, compatible with all three options of Decision 1.
2. **IMRN (Int. Math. Res. Notices)** — strong empirical + structural results are welcome; a 14-page paper is at the short end but acceptable. Strict on dual submission, so Decision 1 must be option 1.
3. **J. Number Theory** — computational number theory orientation, tolerant of empirical results, mid-tier prestige.
4. **Monatshefte für Mathematik (extended)** — only if the short version is withdrawn (Decision 1 option 1).

## Recommended next step

1. Author resolves Decision 1 (Monat conflict).
2. SPRINT-W5-PAPER-POLISH: expand to 18–22 pages, add the Galois/Schwarz subsection, polish proofs of Prop 5.1 and Lem 5.2 inline, add SHA-256 hashes for W1 and W2 scripts to Table 4.
3. SPRINT-W6-SUBMISSION-PREP: cover letter, suggested referees, anti-plagiarism check against the Monat note.

## Files committed

```
sessions/2026-04-27/SPRINT-W4-EMPIRICAL-PAPER-DRAFT/
├── trans_minus29_outline.md           (Step 3 deliverable)
├── trans_minus29_full.tex             (Step 4 deliverable)
├── trans_minus29_full.pdf             (Step 6 deliverable, 14 pp.)
├── trans_minus29_full.log             (pdflatex transcript)
├── trans_minus29_full.aux,.out,.toc   (LaTeX auxiliaries)
├── _pass1b.log, _pass2b.log           (compile run logs)
├── claims.jsonl                       (1 entry, action=full_paper_draft)
├── halt_log.json                      (empty)
├── discrepancy_log.json               (empty)
├── unexpected_finds.json              (empty)
└── handoff.md                         (this document)
```

## AEAL claim count

1 entry in `claims.jsonl` (action `full_paper_draft`, page count 14, sprint result PATH_3, theorems/propositions enumerated, Monatshefte conflict flagged).
