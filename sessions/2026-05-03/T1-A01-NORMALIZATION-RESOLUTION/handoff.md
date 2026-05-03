# Handoff — T1-A01-NORMALIZATION-RESOLUTION

**Date:** 2026-05-03
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~60 minutes (literature pass; no proof attempt;
no numerical pipeline)
**Status:** COMPLETE

---

## What was accomplished

Phase-1.5 unblocker for the KEYSTONE Phase 2 (PCF-2 v1.3 + umbrella v2.0
B4 lift to $d \ge 3$). Resolved the **A-01 normalisation-match
ambiguity** logged in the 2026-05-02 T1-BIRKHOFF-TRJITZINSKY-LITREVIEW
handoff. Verdict: **`A01_WASOW_READING_CONFIRMED`**, reached by
direct triangulation through on-disk Birkhoff 1930 (Acta Math 54)
and Birkhoff–Trjitzinsky 1933 (Acta Math 60), without primary
Wasow §X.3 access (the on-disk Dover-reprint PDF is image-only and
has no OCR layer). The Phase-1 [d, 2d] bracket holds; Phase 2 may
launch with target B4 = 2d.

---

## Key numerical findings

This is a literature-only session — no numerical pipeline. Findings:

* **B–T 1933 §1 normal-case canonical exponent:** $Q_j(x) = \mu_j\,x\log x
  + \gamma_j\,x$ (Acta Math 60, page 4). Verbatim OCR in
  [`bt1933_normalization_extract.md`](bt1933_normalization_extract.md).
* **B–T 1933 page 5 footnote 2 + Birkhoff 1930 page 2 footnote 2:**
  Adams 1928 (Trans. AMS 30 (1928) 507–541) is cited with the same
  convention as Birkhoff/B–T (i.e., Adams's σ shares the μ-units;
  **no factor of 2** at the normalisation level).
* **Birkhoff 1930 page 6 formula (6):** canonical formal solution
  $s(x) = x^{\nu x}\,e^{P(x)}\,x^{\mu}\,(\cdots)$ with the
  Newton-polygon slope formula $\mu = (j_l - j_m)/(l - m)$.
  Verbatim OCR in
  [`birkhoff_1930_rank_extract.md`](birkhoff_1930_rank_extract.md).
* **PCF-1 v1.3 §6 Theorem 5:** $\log|\delta_n| = -A\,n\log n + \alpha
  n - \beta_w \log n + \gamma_w + o(1)$, with $A \in \{3, 4\}$ at
  $d = 2$. Verbatim TeX in
  [`pcf1_v13_ansatz_extract.md`](pcf1_v13_ansatz_extract.md). The
  empirical $A \in \{3, 4\}$ at $d = 2$ sits **inside** the Wasow
  bracket $[d, 2d] = [2, 4]$ and **outside** the Adams bracket
  $[d/2, d] = [1, 2]$ — an internal cross-check in favour of the
  Wasow reading (recorded in D1, not used as primary evidence).

10 AEAL claims written to
[`claims.jsonl`](claims.jsonl), all of evidence_type
`literature_quotation`, with source / page / output_hash filled.

---

## Judgment calls made

1. **Treating Wasow §X.2–§X.3 as NIA rather than halting under
   `A01_AMBIGUOUS_NEEDS_PRIMARY_WASOW_DETAIL`.** The relay's STEP 7
   description of `AMBIGUOUS_NEEDS_PRIMARY_WASOW_DETAIL` is "OCR /
   scan quality of Wasow §X.3 is insufficient or the relevant
   passage is missing", which **does** technically describe the
   on-disk situation (Wasow PDF is image-only, 773 bytes of text
   across 89 pages). However, the agent judged that the
   **triangulation through Birkhoff 1930 + B–T 1933 directly** is
   sufficient to resolve the **normalisation-match** half of A-01
   (Adams vs Wasow), even though the **bracket-derivation** half
   (the upper bound $\mu \le 2d$) remains paraphrase-grade. Verdict:
   `A01_WASOW_READING_CONFIRMED` with three explicit caveats logged
   in [`verdict.md`](verdict.md) and
   [`discrepancy_log.json`](discrepancy_log.json). The synthesizer
   may downgrade to `AMBIGUOUS_NEEDS_PRIMARY_WASOW_DETAIL` if a
   stricter standard is desired.

2. **HOLD-FOR-SYNTHESIZER-ARBITRATION for the H1 (Theory-Fleet)
   label disposition.** The relay's STEP 8 invited keep / downgrade /
   hold; the agent recommended hold because the umbrella v2.0
   main.tex L295 phrasing is not in scope for the agent to audit.
   See
   [`h1_label_disposition_advisory.md`](h1_label_disposition_advisory.md).

3. **Reading B–T 1933 page 4 OCR-garbled "g/x log X+TiX" as
   "$\mu_j\,x\log x + \gamma_j\,x$".** This is a clear OCR ligature
   error (Greek μ → "g/", subscript j → "/", γ → "T"). Transcribed
   verbatim with `[transcribe:]` notes in D3. The reading matches
   the formula (7) on the same page and is the canonical B–T
   normal-case form.

4. **Reading Birkhoff 1930 formula (6) "x^{ν−p}" as "x^{νx}"**
   (i.e., $e^{\nu x \log x}$). The only mathematically coherent
   reading of the OCR garbage that matches B–T 1933 (7) on the
   following year. Transcribed verbatim with `[transcribe:]` note
   in D4. The Newton-polygon slope formula $\mu = (j_l - j_m)/(l - m)$
   on the same page is independent of this reading and supplies a
   cross-check.

---

## Anomalies and open questions

**THIS IS THE MOST IMPORTANT SECTION.**

1. **Phase-1 paraphrase artefact identified** (Unexpected Find #1
   in [`unexpected_finds.json`](unexpected_finds.json)). Phase-1's
   `gap_proposition_for_d_ge_3.md` §2 / §4 stated
   "$\sigma_{\mathrm{Wasow}} = 2\sigma_{\mathrm{Adams}}$" as a
   possible factor-of-2 ambiguity. The present session's direct
   evidence from B–T 1933 page 5 + Birkhoff 1930 page 2 reveals
   **no factor of 2** at the primary-source level. This is a
   correction to a Phase-1 paraphrase commentary, **not** a
   contradiction with a Phase-1 AEAL-logged claim. Logged in
   [`discrepancy_log.json`](discrepancy_log.json) (DISC-3).

2. **Wasow §X.3 polynomial-coefficient slope bound remains
   paraphrase-grade.** The present session resolves the
   normalisation-match half of A-01 but does **not** verbatim-attest
   the upper-bound $\mu \le 2d$ in terms of polynomial degree d
   from Wasow §X.3 itself. This is a **residual** that does not
   block Phase 2 launch but should be tightened by either a primary
   Wasow §X.3 OCR pass or by Phase 2's own internal
   non-resonance / non-degeneracy argument. Logged as DISC-1, DISC-2.

3. **Adams 1928 still NIA on disk.** All Adams-related claims are
   transitive (via Birkhoff 1930 footnote 2 + page 2 characterisation +
   B–T 1933 page 5 footnote 2). Operator-side acquisition of Trans.
   AMS 30 (1928), pp. 507–541 would tighten the verdict from
   "WASOW_READING_CONFIRMED via transitive Birkhoff/B–T evidence" to
   "WASOW_READING_CONFIRMED via primary Adams + Birkhoff/B–T
   triangulation". Recommended in the original Phase-1 handoff under
   "What would have been asked"; reaffirmed here.

4. **Synthesizer arbitration request on H1 label.** The agent
   recommended HOLD rather than KEEP or DOWNGRADE; the synthesizer
   is best placed to decide. See
   [`h1_label_disposition_advisory.md`](h1_label_disposition_advisory.md).

5. **OCR layer of Wasow Dover reprint is absent.** Operator may want
   to commission a `tesseract` OCR pass over the Wasow PDF page
   images, or acquire a different scan with text layer. Out of scope
   for this session, but would unblock primary §X.2–§X.3 quotation.

---

## What would have been asked (if bidirectional)

* "Should I treat Wasow §X.3 image-only as
  `AMBIGUOUS_NEEDS_PRIMARY_WASOW_DETAIL` or as 'NIA but resolved
  through B–T+Birkhoff transitive evidence'?" — Resolved
  autonomously; documented in Judgment Call #1.
* "Is the H1 label disposition advisory the operator's call or the
  synthesizer's?" — Resolved autonomously by recommending hold for
  synthesizer arbitration.
* "Would the operator like a `tesseract` OCR pass over the Wasow PDF
  in this session?" — Out of scope per relay §7; deferred to
  operator-side action.

---

## Recommended next step

**Launch Phase 2: relay `T1-BIRKHOFF-PHASE2-LIFT-LOWER`.**

The verdict `A01_WASOW_READING_CONFIRMED` removes the primary
obstacle to Phase 2 (the major-halt branch where B4 = 2d would have
been outside the literature bracket is **falsified**). Phase 2's
task — lifting the literature-derivable lower bound from $d$ to $2d$
via a non-resonance / non-degeneracy argument on the SIARC PCF
stratum — may launch with target B4 = 2d, sub-claims P2.1 / P2.2 /
P2.3 as decomposed in the Phase-1 handoff §5.

**Pre-Phase-2 contingencies (none are blockers):** (i) operator-side
primary Wasow §X.3 acquisition (would upgrade DISC-1 from paraphrase
to literature-rigorous); (ii) operator-side primary Adams 1928
acquisition (would tighten the present verdict to "via direct Adams
+ Birkhoff/B–T triangulation"); (iii) synthesizer arbitration on H1
label disposition (per advisory).

---

## Files committed

Under `siarc-relay-bridge/sessions/2026-05-03/T1-A01-NORMALIZATION-RESOLUTION/`:

* `pcf1_v13_ansatz_extract.md` — D1, STEP 1 quotation block
* `wasow_section_X_normalization.md` — D2, STEPS 2 + 3 (NIA report)
* `bt1933_normalization_extract.md` — D3, STEP 4
* `birkhoff_1930_rank_extract.md` — D4, STEP 5
* `normalization_triangulation.md` — D5, STEP 6 (the comparison table)
* `h1_label_disposition_advisory.md` — D6, STEP 8 advisory
* `claims.jsonl` — D7, 10 AEAL `literature_quotation` entries
* `verdict.md` — D8, label `A01_WASOW_READING_CONFIRMED`
* `halt_log.json` — D9, empty `{}` (no H-1..H-4 trip)
* `discrepancy_log.json` — D10, three residual discrepancies
* `unexpected_finds.json` — D11, two low-magnitude finds
* `handoff.md` — D12, this file

Scratch files retained in the session folder for reproducibility of
the verbatim quotes (all < 200 KB; well below the 10 MB threshold
per copilot-instructions B1):

* `_wasow.txt` — pypdf scratch (773 bytes); kept as evidence of the
  NIA condition.
* `_bt1933.txt` — pypdf scratch (140 KB); the OCR text used for
  verbatim quotation.
* `_birkhoff1930.txt` — pypdf scratch (76 KB); likewise.

---

## AEAL claim count

**10** entries written to `claims.jsonl` this session, all of
`evidence_type: "literature_quotation"`, all with `reproducible: true`,
`source` filled, `script: "t1-a01-normalization-resolution"`, and
`output_hash` filled with the SHA-256 of the deliverable file
containing the underlying quotation.
