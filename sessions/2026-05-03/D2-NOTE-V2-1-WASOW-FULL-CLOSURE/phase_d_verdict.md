# Phase D — verdict

**Verdict:** `UPGRADE_V2_1_FULL`

## Build outcome

- d2_note_v2_1.pdf: 9 pages, 443 759 bytes
- pdflatex: 0 errors, 0 undefined references, 0 undefined citations
  on pass 3
- bibtex: 0 warnings, 0 errors
- Page count 9 ∈ [9, 12] = FULL band per Phase E.10 spec

## Pre-conditions all met

- Phase 0 GATE_PASS (all sub-gates 0.0–0.6)
- Phase A `A_PHASE_A_STAR_VERIFIED` (18/18 at dps=50, max rel_err
  1.73e-51 at d=5,β=11; SHAs locked)
- Phase B `B_LEMMA_DERIVED` (Newton-polygon characteristic-polynomial
  Lemma with 3-step mechanical proof, no multiplicity-2 dependency
  per spec NOTE)
- Phase C `C_LITERATURE_CHAIN_CLOSED` (BT1933 §§4-6 verbatim quoted
  + Costin 2008 ch.5 §5.0a as see-also; no other gaps)
- Phase E build clean

## Q20 arbitration record

`WASOW_Q20_CLOSURE_VERDICT: PUBLICATION_GRADE_PROOF`

The full citation chain (Newton-polygon Lemma → Birkhoff 1930 §2 →
Wasow §19 → Birkhoff–Trjitzinsky 1933 §§4-6 → Phase A* numerical
verification) is now closed at all d ≥ 2 uniformly with:

- mechanical Lemma replacing the v2 black-box;
- formal-series existence anchored;
- sectorial-asymptotic resummation anchored;
- Borel-summability anchored (the residual that v2 admitted as
  open in its annotated bibliography);
- numerical verification at d ∈ {2..10} at dps=50.

This retires the merged Prompt 7 by closing the F1 (rigour)
residual without re-running any mpmath or SymPy pipeline.

## Outputs

- d2_note_v2_1.tex (SHA-256 `840120e7…b388165`)
- annotated_bibliography.bib (SHA-256 `ba5baec0…7fb8fed7`)
- d2_note_v2_1.pdf (SHA-256 `a8b6026a…d5ef74e`)
- pypdf metadata + body verification PASS (Phase E.11)
