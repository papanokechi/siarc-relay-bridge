# Cover-Letter Framing Draft — JFR

**Draft fire time:** 2026-05-07 ~14:55 JST
**Substrate-anchor SHAs:**
- Title verbatim from submission_log.txt L152 + L174 + tunnell_afm_R2.tex L74-77
  (SHA 91546B54974E25A4CF54A13CA71FA75380F0C5ED3C0EFA421C6CCAC2333D8BB9; 46708 B)
- Abstract opening sentence verbatim from tunnell_afm_R2.tex L90-93
- Multi-submission disclosure from submission_log.txt Item 25 L201
**HALT self-check:** title unchanged; abstract not redrafted; scope
unchanged; no venue selection performed (JFR is one of four
parallel framing drafts).

---

## Cover letter draft

Dear Editors,

I am writing to submit the manuscript entitled *"A Layered,
Axiom-Isolated Lean 4 Formalization of the Congruent Number Problem
up to Tunnell's Criterion"* for consideration for publication in
the *Journal of Formalized Reasoning*.

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

JFR's declared scope is

> research papers describing significant, automated or
> semi-automated formalization efforts in any area, including
> classical mathematics

which is a precise description of the contribution under
submission. Three Tunnell-criterion-specific elements align directly
with JFR's stated emphasis on proof techniques and methodologies:
(i) a formal non-vacuity proof for the axiom boundary, which
isolates the BSD-conditional dependency in a named axiom rather
than as a vacuous assumption; (ii) a layered architecture
(constructive core / named conjecture axiom / conditional
consequences) that is a reusable formalization template for other
BSD-conditional or GRH-conditional results; (iii) an accompanying
Python computational pipeline (98 tests, validated against OEIS
A003273 for all squarefree n at most 500) that mirrors the Lean
development.

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

**Word count target check (cover-letter body):** ~230 words
(slightly above 150-220 envelope; surfaced as a non-blocking
discrepancy in handoff Anomalies; trim-to-220 recommended at 080
finalize step).

**Forbidden-verb scan (cover-letter prose only, excluding the
verbatim abstract + scope quotes which are structurally exempt):**
zero hits against the FV-7 verb set (enumerated only in
forbidden_verb_scan.md to avoid set-literal echoes in production
deliverables).

**Quote-length scan:** abstract sentence 1 = 21 words; sentence 2 =
35 words; JFR scope quote = 16 words; all three under 50-word
ceiling.

