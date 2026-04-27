# Handoff — TUNNELL-FAC-PREP
**Date:** 2026-04-27
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** COMPLETE

## What was accomplished
Prepared the FAC (Formal Aspects of Computing, Springer Nature) submission
package for the layered, axiom-isolated Lean 4 formalization of Tunnell's
criterion. Located the existing manuscript (`congruent-relay/paper/main.tex`),
copied it into the bridge as `tunnell_fac_submission.tex`, replaced the prior
"Target venue: ITP/CPP" framing with a focused-note paragraph (per relay
prompt), upgraded the author block with affiliation and ORCID, rewrote the
AI disclosure to the Springer-prescribed wording, recompiled the PDF
(2 pdflatex passes, exit 0 both), and produced the cover letter, claims.jsonl,
halt/discrepancy logs.

## Source files located (Step 1)
- Manuscript: `congruent-relay/paper/main.tex` (909 lines pre-edit; identical
  duplicate at `congruent-relay/paper/source/main.tex`).
- Lean source directory: `congruent-relay/formal/` — single file
  `CongruentStubs.lean` (954 lines), per the manuscript's own claim.
- No `tunnell*.tex` or `Tunnell/` directory exists; the manuscript is the
  one in `congruent-relay/paper/`.
- Workspace `lean4/` directory exists but is unrelated (SIARCRelay /
  Lyapunov controllability project).

## Manuscript metadata (post-edit)
- Title: *A Layered, Axiom-Isolated Lean 4 Formalization of the
  Congruent Number Problem up to Tunnell's Criterion*
- Compiled pages: **10**
- Source lines (post-edit): **923**
- Approx word count (whitespace-tokenised, including LaTeX markup): ~3,830
- Sections: Introduction; Related Work; Overview of the Lean Development
  (subsections S1–S6); Axiom Boundary; Evaluation; Conclusion and Future Work;
  Appendix A "File Tour"; Appendix B "Selected Lean Excerpts";
  References; AI-Assistance Disclosure.

## Lean source line count
- `congruent-relay/formal/CongruentStubs.lean`: **954 lines**
  (only `*.lean` file in `congruent-relay/formal/`).

## Sorry inventory (from manuscript text only — no fresh grep)
- The manuscript states 0 `sorry` placeholders.
- 1 named axiom: `tunnell_conditional_on_BSD`
- 2 opaque definitions: `AlgebraicRank`, `AnalyticRank`
- ~30 theorems/lemmas, ~15 definitions
- (A fresh grep is deferred to P15-SORRY-AUDIT per relay instructions.)

## JAR-specific content removed
- The manuscript carried no JAR cover sheet, editor-addressed remarks, or
  Blanchette-specific headers; the only venue-specific text was a
  "Target venue: ITP/CPP" paragraph in §1, which was replaced by the
  focused-note framing required by the relay prompt.

## Changes made to manuscript
1. **Header comment block (lines 1–7).** Updated the "Manuscript for
   internal peer review" note to "Manuscript prepared for submission to
   Formal Aspects of Computing (Springer Nature) — April 2026".
2. **Author block (lines 75–85).** Replaced `\author{Papanokechi}` with a
   `\thanks{}`-augmented author block giving affiliation
   ("Independent researcher, Yokohama, Japan"), ORCID
   `0009-0000-6192-8273` (linked via `\href`), and repository URL.
3. **Introduction §1 (lines 119–134).** Replaced the "Target venue:
   ITP/CPP" paragraph with a new "Scope of this note" paragraph using
   the relay-prescribed focused-note framing ("self-contained, layered
   Lean 4 formalization … proof hygiene and axiom isolation rather than
   encyclopedic coverage … reusable building blocks for larger
   verification efforts"), retaining the original sentence framing the
   contribution as a new formalization architecture.
4. **AI-Assistance Disclosure §* (lines 905–921).** Prepended the
   Springer-prescribed wording verbatim ("During the preparation of
   this work the author used GitHub Copilot (Microsoft) and Anthropic
   Claude … reviewed and edited the content as needed and takes full
   responsibility for the content of this article."). The pre-existing
   reproducibility paragraph (mpmath 1.3.0, repository pointer) was
   retained as a second paragraph.

No mathematical content, Lean code excerpts, theorem statements, or
numerical claims were modified.

## AI disclosure
Confirmed present at line **905** of `tunnell_fac_submission.tex`,
with Springer-prescribed wording in the first paragraph of the
`\section*{Computational and AI-Assistance Disclosure}` block.

## BSD-conditional axiom labeling
Confirmed clearly labeled and explained:
- `axiomenv` block "Tunnell's theorem, conditional on BSD"
  (`\label{ax:tunnell}`) at line **505** introduces the axiom and
  states both forward (unconditional) and reverse (conditional)
  directions.
- §6 "Tunnell's Criterion Under BSD" (`\label{sec:s6}`) explicitly
  defines `BSD_for(n)` and labels `AlgebraicRank` / `AnalyticRank`
  as opaque, with a Remark stressing non-vacuity.
- Theorem 6.1 "Axiom non-vacuity" (§ Axiom Boundary) further
  documents the axiom hygiene.
- The Lean identifier `tunnell_conditional_on_BSD` is referenced at
  line **823** (Appendix A file tour, §6 row).

## PDF output
- Path: `sessions/2026-04-27/TUNNELL-FAC-PREP/tunnell_fac_submission.pdf`
- Size: **472,377 bytes** (≈ 461 KB), 10 pages.
- Build: 2 × `pdflatex -interaction=nonstopmode -halt-on-error`,
  exit code 0 on both passes. No mathematical or Lean content altered.

## Cover letter
- Path: `sessions/2026-04-27/TUNNELL-FAC-PREP/tunnell_fac_coverletter.txt`
- Format: plain text, addressed to the FAC editors. Includes exact
  manuscript title, Lean line count (954), sorry/axiom statement,
  affiliation + ORCID, AI-disclosure pointer, scope-fit rationale.

## Judgment calls made
- The pre-existing manuscript had no JAR cover page or
  editor-addressed remarks (it was already a generic submission
  draft). The only venue-specific paragraph was "Target venue:
  ITP/CPP", which I replaced rather than deleted, per the relay's
  instruction to add a focused-note paragraph in the Introduction.
- The pre-existing AI disclosure differed from the Springer wording
  in the relay; I prepended the prescribed wording verbatim and
  kept the existing reproducibility text as a second paragraph
  (rather than deleting it) since it carries factual repository /
  mpmath-version information.
- Author block previously read just `\author{Papanokechi}` with no
  affiliation; I added a `\thanks{}` footnote with the
  Yokohama / ORCID / repository data specified in the prompt.
- I did not run a fresh grep over Lean sources for `sorry`; the
  relay prompt explicitly defers that to P15-SORRY-AUDIT and
  instructs to use the manuscript's own count.

## Anomalies and open questions
- The manuscript's Conclusion section ends at line ~728, but
  there is **no `\bibliography{}` or `\bibitem{}` content visible
  in the body of the file beyond a single pre-existing
  `\begin{thebibliography}{99}` block (lines 829–891)**. All citation
  keys used in the body do resolve into items in this `thebibliography`
  block; pdflatex emitted no undefined-reference warnings on pass 2.
- pdflatex completed cleanly, but `cleveref` is loaded without an
  explicit `\Crefname` for `axiomenv`; references to the axiom are
  rendered via the default theorem-counter name. This is a minor
  cosmetic point only — no broken references.
- The `congruent-relay/formal/` directory contains only one Lean
  file. The "954 lines" claim in the abstract / metrics table
  matches the actual file. No multi-file Lean source exists, so the
  cover letter cites the single-file count.

## What would have been asked (if bidirectional)
- Should the focused-note paragraph fully replace the
  "Target venue: ITP/CPP" paragraph (as I did), or should both
  appear with ITP/CPP relegated to a footnote? I chose full
  replacement because the manuscript is being repositioned for FAC.
- Should the existing `Computational and AI-Assistance Disclosure`
  text be deleted in favour of the prescribed wording, or
  augmented? I augmented (prepend prescribed wording, retain
  existing reproducibility paragraph) because the prescribed text
  is policy-only and does not subsume the mpmath / repository
  reproducibility content.
- Does FAC require a separate title page / structured abstract /
  highlights document? The relay prompt did not request these;
  papanokechi may need to add them at portal-submission time.

## Recommended next step
P-TUNNELL-FAC-SUBMIT: papanokechi to upload
`tunnell_fac_submission.pdf` and `tunnell_fac_coverletter.txt`
via the Editorial Manager portal at
https://link.springer.com/journal/165 (Submit New Manuscript).
At submission time, verify whether FAC requires a structured
abstract or a separate Conflict-of-Interest declaration; the
Tunnell paper has none of either today.

## Files committed
- `tunnell_fac_submission.tex`        (923 lines, edited copy of manuscript)
- `tunnell_fac_submission.pdf`        (472,377 B, 10 pages)
- `tunnell_fac_coverletter.txt`       (FAC cover letter, plain text)
- `claims.jsonl`                      (1 entry, submission_package_prepared)
- `halt_log.json`                     (empty array)
- `discrepancy_log.json`              (empty array)
- `unexpected_finds.json`             (empty array)
- `handoff.md`                        (this file)

(Auxiliary build files `*.aux`, `*.log`, `*.out`, `_build*.log` are
left in the directory for reproducibility; they are <50 KB each.)

## AEAL claim count
1 entry written to `claims.jsonl` this session.
