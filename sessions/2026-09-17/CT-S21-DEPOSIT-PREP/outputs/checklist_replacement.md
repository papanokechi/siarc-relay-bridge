## Deposit-day checklist (P0 citation rule) — RUN, 18 September 2026

The operator's ruling was to perform this pass **immediately before uploading**,
not earlier, so that the recorded hashes match what is actually cited on the day.
It was run on the day of deposit. All four rows re-fetched; all four
load-bearing page images re-read by eye.

| # | External citation | Result |
|---|---|---|
| 1 | van der Put & Saito, *Ann. Inst. Fourier* **59** (2009), Table 2.1, p. 2635, and the strong-Riemann–Hilbert passage on p. 2634 | re-fetched, sha256 `1666bd6b…`, unchanged from the held copy; pp. 2634, 2635 and 2637 re-read from images, all as quoted |
| 2 | Jimbo, *Publ. RIMS*, p. 1152 — the PV dictionary **and** assumption (A1)_PV | re-fetched, sha256 `255d4f07…`, unchanged; printed p. 1152 re-read from an image: (3.1) prints diag(1,0), (A1)_PV prints theta_0, theta_t not in Z, and the dictionary gives gamma = 1 − theta_0 − theta_t |
| 3 | Companion v1.2 (Zenodo version DOI) — Remark 2.2, Conjecture 4.1, the tuple, the scaling paragraph on p. 6, §7.1 | re-fetched; still version **1.2**, version DOI `10.5281/zenodo.20481592`, concept DOI `10.5281/zenodo.20455089`; deposited file unchanged |
| 4 | DLMF §32.2 (cited by v1.2 for the PV normalisation) | re-fetched; **Version 1.2.8, released 2026-09-15** — the release this notice cites |

Per the rule, **hypotheses as well as theorem statements** are in scope — that
is the lesson of the Gautschi (2.8) near-miss, where an OCR layer rendered the
hypothesis in a way that would have reversed the conclusion. Read page images,
never the text layer, for anything load-bearing.

The pass also found a defect of our own, recorded above under
**CT-S15-COLDREAD-DEFERRED**: a stored page image had been named by its position
in the PDF rather than by the number printed on it. No quotation in this notice
was affected, and every affected passage was re-read from the correct page. A
rendered page is now identified by the number printed on it, never by the
arithmetic that produced it.

**Status of the notice itself:** all three gates closed; both cold reads
(`CT-S14-COLDREAD-B` on row **B**, `CT-S15-COLDREAD-DEFERRED` on `R1-56` and
`CT-S9-PVPARAMS-C014`) have returned and been adopted claim by claim. Every
supporting claim is `cold` or INSPECTED except `R1-57`, which is CONJECTURED
on the face of the notice and carries no weight. The deposit-day citation pass
above is complete. Nothing in this record has been committed or submitted
elsewhere.
