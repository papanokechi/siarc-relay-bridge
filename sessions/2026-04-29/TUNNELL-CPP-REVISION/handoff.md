# Handoff — TUNNELL-CPP-REVISION
**Date:** 2026-04-29
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** COMPLETE

## What was accomplished
Applied the SICF minor-revision fixes to the P-Tunnell manuscript,
producing `tunnell_cpp_R1.tex` from the prior `tunnell_afm_R2.tex`
source. The paper has been re-framed methodology-first to target
CPP 2027 instead of the previously-rejected AFM/JAR/FAC venues.
PDF compiles cleanly in two pdflatex passes with no warnings or
undefined references.

## Key numerical findings
- Page count R2 (AFM submission): 12 pages, 490,183 bytes
- Page count R1 (CPP revision):   12 pages, 491,011 bytes
- Net length change: +828 bytes (≈ neutral; tables and contribution
  list balance the removed long-form AI disclosure)
- Compile: 0 errors, 0 warnings, 0 undefined references
- Lean source: 954 lines (170 bridging / 680 reasoning / 104 axiom)

## Changes applied (per task spec)

| Step | Change | Location |
|------|--------|----------|
| 1 | Copied `tunnell_afm_R2.tex` → `tunnell_cpp_R1.tex` | session folder |
| 2 | Abstract rewritten (~150 words, methodology-first) | `\begin{abstract}` block, ~line 91 |
| 3 | `\subsection*{Contributions}` (4-item enumerate) added | §1 Introduction, ~line 130 |
| 4 | Dependency budget table moved to §1 (kept `\label{tab:depbudget}`) | §1, ~line 165 |
| 4 | Axiom inventory table moved to §1 (new `\label{tab:axiom-inventory}`) | §1, ~line 185 |
| 4 | Removed duplicate dep-budget block in §3 | §3 now points to Table 1 |
| 4 | §"Axiom Inventory" renamed → "Axiom Inventory: Verification"; duplicate inline table dropped | §5 |
| 5 | `\subsection*{Comparison}` table (FLT-regular / Loeffler–Stoll / This work) added | §2 Related Work, end |
| 6 | `\subsection*{Toward Unconditional Tunnell}` with label `sec:future-unconditional` added | §Conclusion |
| 7 | GitHub URL + Zenodo DOI + Lean v4.14.0 / Mathlib v4.14.0 hoisted to §1 (Reproducibility first-page pointer) | §1, ~line 152 |
| 7 | §Evaluation/Reproducibility now back-references §1 | §Evaluation |
| 7 | Title-page footnote URL updated `congruent-relay` → `tunnell-cnp-lean4` | `\thanks{}` |
| 8 | Long AI disclosure replaced with single-paragraph `\section*{Declarations}` | end of paper |
| 9 | Two pdflatex passes — clean compile | `_pdflatex_pass1.log`, `_pdflatex_pass2.log` |

## Judgment calls made
- **Repo URL update.** The new abstract uses
  `github.com/papanokechi/tunnell-cnp-lean4` (different from the R2
  `congruent-relay`). I propagated the new URL to the title-page
  `\thanks{}` footnote for consistency. If the canonical repository
  is still `congruent-relay`, this should be reverted in one place.
- **Tables placed via `table` float** (not raw `center`) so they
  acquire LaTeX numbers and `\ref{}` works from §3 / §5.
- **§"Axiom Inventory"** retained but renamed to "Axiom Inventory:
  Verification" since the inline table moved to §1; the verification
  evidence (grep + `#print axioms` listings) stayed in place.
- **Future Work** added as `\subsection*{}` inside the existing
  §Conclusion and Future Work section (per task spec: "or subsection
  in Discussion/Conclusion") rather than a top-level `\section`,
  to avoid disrupting numbering.
- **§"Future directions" enumerate** kept above the new subsection
  because it lists complementary research directions; the new
  subsection focuses specifically on discharging the BSD axiom.

## Anomalies and open questions
- **Mathlib PR pending.** Per task instructions, do NOT submit until
  the involution lemma / quadratic-form lemmas are upstreamed to
  Mathlib. The Future Work item §4 references this. Recommend a
  follow-up session to prepare the Mathlib PR before CPP submission.
- **CPP 2027 deadline.** `https://popl26.sigplan.org/home/CPP-2026`
  was not fetched (per `do not generate URLs unless asked`). Claude
  / human should confirm CPP 2027 dates when CFP appears.
- **Repo name discrepancy.** New abstract URL
  `tunnell-cnp-lean4` vs previously-used `congruent-relay`. The
  Zenodo DOI `10.5281/zenodo.19834824` should also be confirmed
  (carried over verbatim from task spec).
- **Title unchanged.** "A Layered, Axiom-Isolated Lean~4
  Formalization of the Congruent Number Problem up to Tunnell's
  Criterion" — still works for CPP framing but Claude may want to
  shorten / re-key for the CPP submission template.

## What would have been asked (if bidirectional)
1. Should `congruent-relay` references in §Evaluation (Python
   pipeline section, `pytest -q`, `python -m src.runner`) also be
   re-pointed to `tunnell-cnp-lean4`, or is the Python pipeline
   in a separate repo?
2. Is the CPP submission template a single-column `\documentclass`
   different from the current `article`? The current source uses
   `[11pt,a4paper]{article}` with 1-inch margins; CPP/POPL usually
   uses ACM `acmart`. Conversion not done — awaiting confirmation
   of the target template.
3. Should the §Conclusion "Future directions" enumerate be merged
   into the new "Toward Unconditional Tunnell" subsection, or
   kept as two complementary blocks (current state)?

## Recommended next step
Prepare the **Mathlib PR for `card_even_of_involution`** (the
generic `Finset` fixed-point-free involution lemma) before CPP
submission. Once accepted upstream, bump the manuscript's
"This work" line in Table~Comparison from "954 lines, 1 axiom"
to reflect the off-loaded lemma, and convert the source to the
ACM `acmart` template if CPP 2027 keeps that format.

## Files committed
- `tunnell_cpp_R1.tex`        (47.8 KB)
- `tunnell_cpp_R1.pdf`        (491 KB, 12 pages)
- `_pdflatex_pass1.log`
- `_pdflatex_pass2.log`
- `claims.jsonl`              (1 entry)
- `halt_log.json`             (empty `{}`)
- `discrepancy_log.json`      (empty `{}`)
- `unexpected_finds.json`     (empty `{}`)
- `handoff.md`                (this file)

## AEAL claim count
1 entry written to `claims.jsonl` this session
