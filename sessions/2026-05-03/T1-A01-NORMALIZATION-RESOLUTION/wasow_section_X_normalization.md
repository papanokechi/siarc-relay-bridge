# D2 — Wasow 1965 §X.2–§X.3 normalization (NIA — image-only PDF)

**Task:** T1-A01-NORMALIZATION-RESOLUTION — STEPS 2 + 3
**Source file:** `tex/submitted/control center/literature/g3b_2026-05-03/04_wasow_1965_dover.pdf`
**File size:** 5 557 950 bytes (5.4 MB), 89 pages.
**OCR status:** **NO OCR LAYER PRESENT.** `pypdf 6.10.2` text-extraction
returns 773 bytes total across 89 pages — empty body, only
`===== PAGE k =====` headers.

---

## Status: NIA (Not In Agent — primary verbatim extraction infeasible)

The Dover reprint of Wasow 1965 on disk is a scanned image PDF without
an OCR'd text layer. The agent **cannot** primary-quote any
sentence of §X.2 (the σ definition) or §X.3 (the slope-bound
theorem) from this file. This is the same image-only condition
documented in the **2026-05-03 Q20A-PHASE-C-RESUME** dispatch (which
halted with `HALT_Q20A_WASOW_PDF_IMAGE_ONLY`).

This was anticipated by the relay specification under verdict label
`A01_AMBIGUOUS_NEEDS_PRIMARY_WASOW_DETAIL`.

## What we would have extracted (specification of the missing data)

Had OCR been available, the relay (STEP 2) called for:

* **(W.a)** Wasow's formal-exponent definition: the σ in any expansion
  of the form $\exp(\sigma\,z\log z)$ or $\exp(Q(z))$ where
  $\deg Q = \sigma$.
* **(W.b)** Wasow's slope-of-Newton-polygon definition: typically
  $\sigma = \max_i (d_i - d_0)/(i - 0)$ where $d_i$ is the polynomial
  degree of the $i$-th coefficient.
* **(W.c)** Wasow's explicit statement, if any, about the relationship
  between σ and the polynomial degree d of the coefficients.
* **(W.d)** Any explicit statement Wasow makes comparing his σ to
  Adams 1928's σ (typically in the chapter remarks).

And (STEP 3) the §X.3 theorem statement bounding σ in terms of
polynomial-coefficient degrees, e.g. "$\sigma \le \max_i (d_i - d_0)/n$"
or "in the polynomial-coefficient case σ equals the largest such ratio".

## What the agent CAN report from on-disk evidence

Wasow 1965 chapter X is the textbook secondary treatment of the
linear difference-equation analog of Hukuhara–Turrittin. The
**primary** sources that Wasow §X.2–§X.3 are themselves a paraphrase
of are on disk and DO have OCR layers:

* Birkhoff & Trjitzinsky 1933 (Acta Math 60) — see D3.
* Birkhoff 1930 (Acta Math 54) — see D4.

The 2026-05-02 Phase-1 deliverable
`gap_proposition_for_d_ge_3.md` and `bt1933_theorem_extraction.md`
already paraphrase Wasow §X.2–§X.3 from secondary recollection. The
present agent does NOT re-paraphrase; the present agent treats Wasow
as **NIA** and triangulates the A-01 ambiguity through B–T 1933 + the
Phase-1 paraphrase.

The triangulation in `normalization_triangulation.md` (D5) and the
verdict in `verdict.md` (D8) explicitly handle this NIA condition.

---

## Operator-side recommendation (out of scope for this session)

A cleaner Wasow scan with an OCR layer (e.g. a library scan, or the
Robert Krieger 1976 reprint, or the original 1965 Wiley edition) would
allow primary-grade verbatim quotation of §X.2–§X.3. Recommended
operator action: institutional access to Wasow 1965 §X.2 (the σ
definition) and §X.3 (the slope-bound theorem), specifically the
last paragraph of §X.3 where Wasow's text typically states the
polynomial-coefficient bound and cites Adams 1928 / Birkhoff 1911 /
Birkhoff 1930.

This action is **NOT** needed for the present A-01 verdict, but
would upgrade the bracket-derivation from the Phase-1 paraphrase to
verbatim literature-grade.
