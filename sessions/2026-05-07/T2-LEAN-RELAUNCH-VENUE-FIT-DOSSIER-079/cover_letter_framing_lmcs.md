# Cover-Letter Framing Draft — LMCS

**Draft fire time:** 2026-05-07 ~14:55 JST
**Substrate-anchor SHAs:**
- Title verbatim from submission_log.txt L152 + L174 + tunnell_afm_R2.tex L74-77
  (SHA 91546B54974E25A4CF54A13CA71FA75380F0C5ED3C0EFA421C6CCAC2333D8BB9; 46708 B)
- Abstract opening sentence verbatim from tunnell_afm_R2.tex L90-93
- Multi-submission disclosure from submission_log.txt Item 25 L201
**HALT self-check:** title unchanged; abstract not redrafted; scope
unchanged; no venue selection performed (LMCS is one of four
parallel framing drafts).

---

## Cover letter draft

Dear Managing Editors,

I am writing to submit the manuscript entitled *"A Layered,
Axiom-Isolated Lean 4 Formalization of the Congruent Number Problem
up to Tunnell's Criterion"* for consideration for publication in
*Logical Methods in Computer Science*.

Quoting the manuscript abstract verbatim (sentence 1):

> We present a 954-line Lean 4 formalization of the combinatorial
> and structural backbone of Tunnell's criterion for the congruent
> number problem.

Continuing the abstract verbatim (sentence 2):

> The development is organized into six layers, each mathematically
> natural and fully proved, culminating in a clean axiom boundary
> where the sole remaining assumptions are the Birch and
> Swinnerton-Dyer (BSD) conjecture and Tunnell's conditional
> theorem.

The submission is a natural fit for LMCS for three reasons. First,
LMCS's diamond-OA + arXiv-overlay model aligns with the existing
public artefacts of this work: a Zenodo deposit
(10.5281/zenodo.19834824) and a GitHub repository
(github.com/papanokechi/tunnell-cnp-lean4) already mirror the
manuscript's content. Second, the Tunnell-criterion-specific
contribution — a formal non-vacuity proof for the axiom boundary,
a generic fixed-point-free involution lemma, an eightfold sign
symmetry for positive-definite ternary quadratic forms, and a
theta-series interface — sits inside LMCS's logical-methods scope.
Third, the layered architecture (constructive core / named
conjecture axiom / conditional consequences) is a reusable template
the LMCS reviewer pool is well placed to evaluate.

Multi-submission disclosure: this manuscript is currently under
consideration at no other venue. The prior submission to the
Annals of Formalized Mathematics (afm:18102) was returned
2026-04-28 by the editorial board; that submission is closed.

Code and artefacts are publicly available at
github.com/papanokechi/tunnell-cnp-lean4 and Zenodo
10.5281/zenodo.19834824.

Sincerely,

Papanokechi (Independent researcher, Yokohama, Japan)
ORCID 0009-0000-6192-8273

---

**Word count target check (cover-letter body, excluding signature):**
~225 words (slightly above 150-220 envelope; surfaced as a
non-blocking discrepancy in handoff Anomalies; trim-to-220
recommended at 080 finalize step).

**Forbidden-verb scan (cover-letter prose only, excluding the
verbatim abstract quote which is structurally exempt):** zero hits
against the FV-7 verb set (enumerated only in forbidden_verb_scan.md
to avoid set-literal echoes in production deliverables).

**Quote-length scan:** abstract sentence 1 = 21 words; sentence 2 =
35 words; both under 50-word ceiling. No other > -prefixed span in
this draft.

