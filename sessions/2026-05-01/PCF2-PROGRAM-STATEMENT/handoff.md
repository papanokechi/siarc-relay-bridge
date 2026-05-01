# Handoff -- PCF2-PROGRAM-STATEMENT
**Date:** 2026-05-01
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** COMPLETE

## What was accomplished
Drafted and compiled the PCF-2 / P13 program statement: a 10-page Zenodo
preprint framing the cubic extension of the PCF-1 Delta-discriminant
transcendence predicate. The document follows the structure requested
(position, setup, predictions, plan, why, ack, refs) extended with two
substantive sections (worked landmarks: Apery / Catalan-cubic /
cyclic-C3; literature relation). Four open conjectures B3(i)-(iv) are
stated. Three concrete follow-up sessions (PCF-2 A/B/C) are scoped with
precision/depth budgets and a risk register. Output: tex/submitted/
pcf2_program_statement.tex (35 KB) and .pdf (10 pp, 332 KB), copied
into this session directory.

## Key numerical findings
None. This is a program statement; no new computational results were
produced.
- Page count: 10 pp (target: 10-14 pp), pdflatex 2-pass build, 0 errors.
- Cross-references stable; only cosmetic warnings (2 overfull hboxes in
  Table 1 caption block, 3 hyperref-Unicode TOC entries).

## Judgment calls made
1. Section structure expanded from the requested 7 sections to 9 by
   inserting Section 4 (Worked Landmarks) and Section 6 (Relation to
   Existing Literature). Rationale: a program statement at 7 pp
   reads thinly; the user-stated target was 10-14 pp. The added
   sections are calibration / positioning, not new mathematical claims.
2. Conjectures named "B3 part (i)-(iv)" rather than "A v5 (cubic)" to
   distinguish them in the SIARC label space from PCF-1's Conjecture A
   while remaining clearly parallel in structure.
3. Painleve IV chosen as the conjectural cubic-case Painleve type
   (Conjecture B3 part (iv)). Justification given in Remark 3.5
   (Poincare rank 3/2, Backlund group A2^(1)). This is a forward-going
   bet, flagged explicitly as "generic-not-universal".
4. Cubic-period basis augmentation listed (Gamma(1/3), Gamma(2/3),
   2^{1/3}, 3^{1/3}, 2F1 at 1/3, plus zeta(3) already present). Smallest
   reasonable augmentation; full Hilbert-class-field basis deferred to a
   follow-up sweep noted in the risk register.
5. Three landmark families chosen for Table 1 (Apery 34n^3-51n^2+27n-5,
   Catalan-cubic n^3+n+1 with disc=-31, cyclic-C3 probe n^3-3n+1 with
   disc=81). The accompanying a_n is left for Session A to fix per the
   smallest-Z-primitive convention; not specified in this document.
6. Cited Cohen 2024 as "working notes / preprint" without a specific
   DOI. The PCF-1 paper cited "pcfdatabase2026" similarly. If the
   final Zenodo upload requires a verifiable Cohen reference, this
   citation should be replaced or removed before submission.

## Anomalies and open questions
1. **Apery family Galois group is TBD in the document.** The Apery
   denominator b(n) = 34n^3 - 51n^2 + 27n - 5 has a specific Delta_3
   value that determines whether it falls in the C3 cell or the S3
   totally-real cell. I deliberately did not compute this in the draft
   (the program statement is meant to motivate Session A, which is
   precisely the enumeration session). However, if Claude wants the
   prediction sharper, the Apery Delta_3 should be computed before
   Zenodo upload.
2. **The Poincare characteristic equation for d=3 (Eq. 4) is stated as
   a candidate, "or a closely related cubic depending on the precise
   scaling convention".** The exact form is left for Session A to
   determine. If Claude has a derivation already, the equation should
   be tightened before upload.
3. **No DOI reservation has been performed** for the Zenodo record.
   This is a draft only; the user will need to upload to Zenodo
   manually as a NEW record (not a new version of PCF-1, per the
   prompt).
4. **Painleve IV alignment (Conjecture B3(iv)) is the most speculative
   claim.** It is supported by structural analogy (Poincare rank 3/2,
   Backlund A2^(1)), not by computation. Claude should review whether
   the alignment with cubic Galois groups is documented in
   Mazzocco / Iwasaki et al. tightly enough to cite, or whether the
   conjecture should be weakened to "some Painleve transcendent governs
   the cubic CM case, with the specific equation family-dependent".
5. **Apery row in Table 1 caption notes that PSLQ infrastructure
   correctness depends on detecting zeta(3)/6 for the Apery family
   at the conservative budget.** This is the calibration anchor; if it
   fails, the Session B null results lose force. This should be the
   first run in Session A, before the bulk enumeration.

## What would have been asked (if bidirectional)
1. Should Conjecture B3(iv) be weakened to "some Painleve transcendent"
   rather than committing to P-IV specifically?
2. Is Cohen 2024 a real, citable working notes document, or should this
   citation be removed?
3. Does the user want the Apery Delta_3 and Galois group computed and
   inserted into Table 1 before Zenodo upload?
4. Should the conjecture-naming convention be "A v6 cubic" (continuation
   of PCF-1) or "B v1" (fresh conjecture for PCF-2)? I chose the latter.

## Recommended next step
Run "PCF-2 Session A: cubic family enumeration and Delta_3
classification" exactly as scoped in Section 5 of the program statement.
First sub-task (calibration): compute Delta_3 and Galois group for the
Apery family b(n) = 34n^3 - 51n^2 + 27n - 5 and verify that the PCF-1
Wallis + PSLQ pipeline recovers zeta(3)/6 to >= 50 digits. If the
calibration succeeds, proceed to the |alpha_i| <= 5 bounded enumeration
(~200 families) and produce the stratification table. Output:
sessions/2026-05-01/PCF2-SESSION-A/{stratification_table.csv,
calibration_apery.json, claims.jsonl}.

## Files committed
- pcf2_program_statement.tex (35 KB, source)
- pcf2_program_statement.pdf (10 pp, 332 KB, build output)
- handoff.md (this file)
- halt_log.json (empty, no halt triggered)
- discrepancy_log.json (empty)
- unexpected_finds.json (empty)

## AEAL claim count
0 entries written to claims.jsonl this session. This is a program
statement, not a results paper -- no numerical claims were generated
that require AEAL logging. The conjectures stated in Section 3 are
not numerical claims; they are predictions to be tested in
Sessions A--C.

## 2026-05-01 micro-patch (post-handoff)

**Apery calibration computed (sympy, exact integer):** b(n)=34n^3+51n^2+27n+5 factors over Q as (2n+1)(17n^2+17n+5). Delta_3 = -459 = -3^3 * 17. Splitting field Q(sqrt(-51)); Gal(b/Q) = C_2. Apery is REDUCIBLE, hence out-of-scope of Conjecture B3(i) (which restricts to irreducible Z-primitive b). New Remark rem:apery-reducible added in Sec 4 explaining the reducible cell and reframing Apery as a positive-control infrastructure check rather than a predicate test.

**Conjecture B3(iv) softened:** No commitment to P-IV; now a P-II..P-VI hierarchy reduction, with P-IV as heuristic preference only. Channel question flagged open per PCF-1 Session E (rec-param + Borel both failed for d=2 Delta<0 vs V_quad's known P-III(D6)).

**Citation fix:** Cohen 2024 working-notes (unverifiable) removed; replaced with Cohen 2007 GTM 239 (Number Theory, Vol I), and the Sec 6 paragraph rewritten to cite Davenport-Heilbronn / Bhargava cubic-discriminant background rather than fabricating a PCF-specific Cohen enumeration.

**Build:** 10 pp, 0 errors, 0 undefined refs. Commit fd8c1fd.
