# Handoff — D2-NOTE-V2-1-WASOW-FULL-CLOSURE
**Date:** 2026-05-03
**Agent:** GitHub Copilot (VS Code) — Claude Opus 4.7 backend
**Session duration:** ~120 minutes
**Status:** COMPLETE

## What was accomplished

Closed the F1 (rigour) residual that v2 admitted as open in its
annotated bibliography by anchoring the Borel-summability layer in
Birkhoff–Trjitzinsky 1933 §§4–6 (Lemma 8 + Theorem I + Lemma 9, with
verbatim quotes from a pypdf full-text extraction). Promoted the v1
"by Phase A* symbolic derivation" black-box to a mechanical Newton-
polygon characteristic-polynomial Lemma (Lemma 3.1) with a 3-step
proof. Built v2.1 PDF (9 pages, FULL band per Phase E.10), staged for
new-version Zenodo deposit on existing concept DOI 10.5281/zenodo.19996689.
Wasow Q20 arbitration verdict: PUBLICATION_GRADE_PROOF; merged
Prompt 7 retired.

## Key numerical findings

- **Phase A* sweep** (carry-forward by SHA from Q20A-PHASE-C-RESUME;
  not re-run per spec §8): 18/18 PASS at d ∈ {2..10}, dps = 50,
  max relative error 1.73 × 10⁻⁵¹ at (d=5, β=11). Wrapper SHA
  `06d87de3…0ac277`, core SHA `8e6f9ebd…58f7496`.
- **PCF2-SESSION-Q1 d=4 measurement** (referenced; not re-run):
  spread 0 across 8 representatives at dps = 80; rules out
  v1.1-candidate c(d) = 2√((d-1)!) at d = 4 by ≈22%.
- **v2.1 PDF**: 9 pages, 443 759 bytes,
  SHA `a8b6026a3453f901a0da68c3849a9d7d828138ca4622b8a3686b68f01d5ef74e`.
  pdflatex pass-3: 0 undefined references, 0 undefined citations, 0
  multiply-defined labels.
- **pypdf metadata + body verification PASS**: title contains "(v2.1)",
  Author = Papanokechi, page count 9, "Birkhoff" / "Trjitzinsky" /
  "Lemma" / "Newton polygon" / "Appendix" / "SIARC" all present, PII
  tokens (OneDrive / Users / shkub / email) all 0.

## Judgment calls made

- **Loday-Richaud cite removed in §5(d).** Phase 0 ETHICS-GATE flagged
  PDF not on disk; Phase 0.5 prescribed OMIT. The pre-existing
  `lodayrichaud2016divergent` bib entry (carry-forward from v2) was
  left untouched but the load-bearing `\cite` in §5(d) was replaced
  with a prose acknowledgement that the volume was not consulted at
  v2.1 preparation time. Recorded in unexpected_finds.json item 1.
- **Multiplicity-2 framing of the Newton polygon edge OMITTED from
  Lemma 3.1.** Per spec Phase B NOTE: the multiplicity-2 framing
  carries data about the secondary indicial polynomial and the
  Birkhoff recursion, both beyond the scope of the leading-
  characteristic-polynomial Lemma. A Remark (Remark 3.2) records the
  framing and explains why the Lemma does not depend on it.
- **q = (d+2)/2 derivation in §1.1 written as a sketch, not a
  self-contained proof.** The derivation routes through the order-2
  matrix-system reduction without writing out the reduction
  explicitly; defers to SIARC Channel Theory v1.3 Prop. 3.3.A for
  the full derivation. Flagged in rubber_duck_critique.md item 2.
- **(-1)^d sign convention in Lemma 3.1 step (c) folded into "the
  standard WKB convention" without explicit citation.** Flagged in
  rubber_duck_critique.md item 1.
- **arXiv classification recommendation (Q31)**: primary `math.CA`,
  cross-list `math.NT`. v2.1's content centre-of-mass moved further
  toward `math.CA` (BT1933 + Newton-polygon Lemma + Wasow); deferred
  to operator per spec.
- **claims.jsonl extended to 20 entries** (≥18 spec floor): the
  Q20A baseline is referenced rather than re-listed verbatim, and 4
  new BT1933-related entries plus 16 v2.1-build / literature / synthesis
  entries are written.

## Anomalies and open questions

**THIS IS THE MOST IMPORTANT SECTION. Be thorough.**

1. **Page-count edge.** v2.1 lands at exactly 9 pages, the lower edge
   of the FULL band [9, 12]. Within band, no halt; but a v2.2 polish
   pass that incorporates rubber_duck_critique.md items 1, 2, 4
   (explicit WKB sign-convention citation, explicit matrix-system
   reduction in §1.1, explicit Borel-Laplace pair in §3.5) would
   push to ~10 pp more comfortably. Claude may want to advise whether
   v2.2 should be queued.

2. **Loday-Richaud / Mitschi modern Borel-Laplace volume not
   consulted.** Per ETHICS-GATE; PDF not on disk. The Costin 2008
   ch.5 §5.0a citation supplies the modern Borel-Laplace restatement
   (load-bearing in §3.5), so this is a "would make even more
   explicit" pointer rather than a load-bearing residual. Operator
   may source the PDF for v2.2.

3. **Pre-existing bib entry year mismatch.** The
   `birkhofftrjitzinsky1932analytic` entry (carry-forward) lists
   year = 1932, but Acta Math. 60 was actually published 1933. The
   new `birkhoff_trjitzinsky_1933` entry (added this session) uses
   the canonical 1933 year. The 1932 entry is left untouched (unused
   by v2.1). Cleanup deferrable.

4. **Borel-Laplace duality-variable transfer in §3.5 hand-waved.**
   The transfer between the recurrence-side formal series (where
   BT1933 §§4–6 directly applies) and the generating-function side
   (where the manuscript's Borel-Laplace radius identification lives)
   is asserted via "standard Borel-Laplace transforms in the duality
   variable" without writing out the explicit Borel-Laplace pair. A
   determined referee may push on this. Mitigated by the Costin 2008
   ch.5 §5.0a modern-restatement citation but not eliminated. Flagged
   in rubber_duck_critique.md item 4.

5. **SIARC bridge sessions are not peer-reviewed.** All non-peer-
   reviewed self-citations (PCF-1 v1.3, PCF-2 v1.3, CT v1.3, Q20A
   bridge session, this session) carry SIARC-disclosure footnotes per
   spec Rev-H. The Phase A* numerical verification at d ∈ {2..10}
   and the PCF2-SESSION-Q1 d = 4 measurement are AEAL-anchored with
   SHA-256 output hashes on the public bridge, but a referee may
   still discount this evidence on independent-replication grounds.

6. **Costin 2008 PDF filename mismatch.** The runbook-canonical
   literature directory's slot 06 is named `06_costin_2008_chap5.pdf`,
   not `06_costin_2008_asymptotics.pdf` as the spec suggested. SHA
   matched (`436c6c11…3289`), so the file is the canonical chapter 5
   extract. No action; flagged here for downstream registry tidying.

7. **The "Newton polygon slope-1/d edge ↔ Wasow shearing exponent
   $g_0 = 1/d$" equivalence in §3.3 final paragraph is asserted, not
   proved.** Proof is one line (the slope $h/w = 1/d$ for the edge
   from $(0,0)$ to $(d,1)$), but the manuscript leaves it implicit.
   Flagged in rubber_duck_critique.md item 10.

## What would have been asked (if bidirectional)

- Should the v2.2 polish pass (rubber_duck_critique.md items 1, 2, 4,
  10) be queued now, or deferred until peer-review feedback on v2.1
  arrives?
- Does the Q20 arbitration verdict PUBLICATION_GRADE_PROOF imply that
  D2-NOTE should be submitted to a journal, or does the SIARC v1.3
  workflow keep it as a Zenodo cite-target only? The spec says retire
  merged Prompt 7 and stage Zenodo new-version deposit; no journal
  submission step is specified.
- Should the pre-existing `birkhofftrjitzinsky1932analytic` bib entry
  (year 1932) be deleted now or kept for v2 backward compatibility?
- The Loday-Richaud / Mitschi PDF — operator obtains and stages it
  in the literature directory, or v2.1 stays without it?

## Recommended next step

**Operator action: complete the Zenodo new-version upload following
zenodo_upload_d2_note_v2_1_runbook.md.** Steps 1–6 are operator-only
(the agent does not log in to Zenodo). After the v2.1 DOI is issued,
record it in step 6 of the runbook and notify Claude.

Optional follow-up (lower priority): a v2.2 polish pass incorporating
rubber_duck_critique.md items 1, 2, 4, 10 to push the page count
toward 10 and tighten the WKB sign convention / matrix-system
reduction / Borel-Laplace pair / Newton-polygon-vs-shearing-exponent
exposition.

## Files committed

All files in `sessions/2026-05-03/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/`:

| File | Size (B) | Role |
|---|---:|---|
| `d2_note_v2_1.tex` | 38311 | v2.1 LaTeX source |
| `d2_note_v2_1.pdf` | 443759 | v2.1 PDF (9 pp, FULL) |
| `annotated_bibliography.bib` | 35629 | bibliography (+ birkhoff_trjitzinsky_1933) |
| `d2_note_v2_1.aux` / `.bbl` / `.blg` / `.log` / `.out` | various | build intermediates |
| `phase_0_gate_pass.md` | 7344 | Phase 0 ethics + reuse |
| `phase_a_revalidation.md` | 3845 | Phase A* SHA re-anchoring |
| `phase_b_newton_polygon_lemma.md` | 6868 | mechanical proof of Lemma 3.1 |
| `phase_c3_bt1933_verification.md` | 18519 | BT1933 §§4–6 verbatim quotes |
| `phase_c_full_closure_synthesis.md` | 7440 | 5-step chain + Q20 verdict |
| `phase_d_verdict.md` | 1735 | UPGRADE_V2_1_FULL |
| `phase_e_pdf_verification.md` | 1066 | pypdf metadata + body PASS |
| `bt1933_fulltext.txt` | 141961 | pypdf extraction for quote provenance |
| `claims.jsonl` | 8318 | 20 AEAL claim entries |
| `zenodo_description_d2_note_v2_1.txt` | 4345 | Zenodo metadata copy |
| `zenodo_upload_d2_note_v2_1_runbook.md` | 3832 | operator runbook |
| `arxiv_classification_recommendation.md` | 3305 | math.CA primary advisory |
| `rubber_duck_critique.md` | 6614 | self-critique of 10 items |
| `unexpected_finds.json` | 2095 | 3 informational finds |
| `discrepancy_log.json` | 4 | empty `{}` |
| `halt_log.json` | 4 | empty `{}` |
| `verdict.md` | 19 | one-line verdict |
| `prompt_spec.md` | 61467 | operator-pasted relay body |
| `prompt_spec_synthesizer_draft.md` | 75824 | original synthesizer draft (preserved) |
| `RELAY_PROMPT_BODY.{txt,README.md,sha256}` | various | pre-staged relay-body bundle |
| `handoff.md` | (this file) | handoff |

## AEAL claim count

20 entries written to `claims.jsonl` this session (≥ 18 spec floor).
Breakdown: 3 v2.1 build attestations + 4 BT1933 literature anchors
(PDF + 3 quote claims) + 1 Costin 2008 see-also + 1 Newton-polygon
Lemma synthesis + 1 Phase A* sweep carry-forward + 1 Phase A core
script SHA + 1 Birkhoff 1930 §2 anchor + 1 Wasow §19 anchor + 1
q = (d+2)/2 mapping synthesis + 1 v1.1 falsification at d=4 + 1
V_quad worked example + 1 d=4 measurement + 1 bt1933_fulltext.txt
attestation + 1 prompt_spec.md attestation + 1 Q20 arbitration
verdict synthesis = 20.
