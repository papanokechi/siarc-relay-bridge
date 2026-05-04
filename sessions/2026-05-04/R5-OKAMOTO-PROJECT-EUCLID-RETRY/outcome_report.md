# R5-OKAMOTO-PROJECT-EUCLID-RETRY — Outcome Report

**Date:** 2026-05-04
**Task class:** Operator-side acquisition retry (NOT AEAL relay)
**Hard time cap:** 15 min — respected
**Target:** Okamoto, K. "Studies on the Painlevé equations IV. Third
Painlevé equation P_III." *Funkcialaj Ekvacioj* **30** (1987), 305–332.
**Slot:** `literature/g3b_2026-05-03/07_okamoto_1987_painleve_III_FE30.pdf`

---

## OUTCOME

**`OUTCOME_R5RT_NOT_ON_PROJECT_EUCLID`** (with operator-supplied substitute)

Operator surfaced a file at the slot-07 path, but title-page +
last-page text extraction confirmed it is a DIFFERENT Okamoto
paper from the same series:

  Okamoto, K. "Studies on the Painlevé Equations. I. Sixth
  Painlevé Equation P_VI." *Annali di Matematica Pura ed
  Applicata* (IV), Vol. CXLVI (1987), 337–381.

Verification per task §2 step 3 FAILS for the slot-07 target:

| Check                       | Required             | Observed                                              | Result |
|-----------------------------|----------------------|-------------------------------------------------------|:------:|
| Title page series part      | "IV"                 | "I."                                                  | ❌ FAIL |
| Title page Painlevé equation| "Third / P_III"      | "Sixth Painlevé Equation P_VI"                        | ❌ FAIL |
| Journal                     | Funkcialaj Ekvacioj  | Annali di Matematica Pura ed Applicata (Italian)      | ❌ FAIL |
| Volume                      | 30 (1987)            | CXLVI (1987)                                          | ❌ FAIL |
| Pages                       | 305–332              | 337–381                                               | ❌ FAIL |
| Author                      | Kazuo Okamoto        | Kazuo Okamoto                                         | ✅ pass |
| Year                        | 1987                 | 1987 (received Aug 1985, revised Nov 1985)            | ✅ pass |
| %PDF magic bytes            | `25 50 44 46`        | `25 50 44 46 2D 31 2E 33` (PDF-1.3)                   | ✅ pass |
| File integrity              | reasonable PDF       | 1.94 MB, 45 pages, OCR'd TIFF scan                    | ✅ pass |

The author/year coincidence (Okamoto/1987) likely caused operator
search to land on Part I rather than Part IV.

---

## File disposition

Relocated to remove the misleading filename while preserving the artefact:

  Old path: `tex/submitted/control center/literature/g3b_2026-05-03/07_okamoto_1987_painleve_III_FE30.pdf.pdf`
  New path: `tex/submitted/control center/literature/g3b_2026-05-03/supplementary/okamoto_1987_part_I_painleve_VI_AnnMat.pdf`
  SHA-256:  `0982c60e262629edb4833c61eeaeb6281b1561b8b9a8da6134bef9824cd7cb1c`
  Size:     1,944,075 bytes (45 pages)

Slot 07 (Okamoto FE 30 P_III, target) remains UNFILLED.
SHA256SUMS.txt amended with full provenance note + supplementary entry.

All 10 entries in SHA256SUMS.txt self-verify (PASS 10 / FAIL 0).

---

## Aggregate scenario after retry

**SCENARIO C confirmed** (1 of 3 acquired):

| Slot | Source                                           | Status                 |
|------|--------------------------------------------------|------------------------|
| 07   | Okamoto FE 30 (1987) P_III — *target*            | ❌ NOT acquired        |
| 08   | Lisovyy / Barhoumi-Lisovyy-Miller-Prokhorov 2024 | ✅ acquired (prior R5) |
| 09   | Conte-Musette 2008 ch. 7                         | ❌ NOT acquired        |

Bonus (not a substitute for slot 07):
| —    | Okamoto Part I (P_VI), Ann. Mat. 1987            | ✅ supplementary       |

---

## M6 status

Per task spec §2 step 6, **OUTCOME_R5RT_NOT_ON_PROJECT_EUCLID → SCENARIO C confirmed**:

> M6 status: proceed with ethics-gate framing for Okamoto

Recommended downstream:
- `CC-VQUAD-PIII-NORMALIZATION-MAP` may fire when M4 disposition lands,
  with ethics-gate framing for the missing Okamoto P_III primary source.
- Lisovyy/Barhoumi-Lisovyy-Miller-Prokhorov 2024 (slot 08) provides the
  P_III(D_6) Stokes/monodromy data needed for the closure, so the
  closure attempt is NOT blocked — it just lacks the Lax-pair primary
  citation.
- Costin 2008 ch. 5 (slot 06, in-hand) substitutes for Conte-Musette
  ch. 7 per A-01 verdict.

Operator may consider deferring the M6 closure attempt to v1.17 cycle
if synthesizer prefers a fully-gated closure (SCENARIO A) over a
SCENARIO C closure with ethics-gate framing.

---

## Recommended re-fire path (if synthesizer wants another retry)

Project Euclid does not appear to carry Funkcialaj Ekvacioj
backlist (volume 30 not browseable from CLI agent perspective in
prior probes; Incapsula JS-challenge expected). Most likely OA
route NOT yet tried:

  **NUMDAM** — `https://www.numdam.org/`
  Funkcialaj Ekvacioj is hosted on NUMDAM with reasonably complete
  pre-2010 backlist. A direct article URL would look like:
    `https://www.numdam.org/item/FE_1987__30__305_0/`
  (operator confirms exact URL pattern).

If a future retry is fired, its acquisition-time verification
should require the strings "**équations IV**" or "**Third Painlevé**"
on the title-page OCR (not just author + year) to prevent the
Part-I/Part-IV confusion that occurred this session.

---

## 15-minute time cap

Respected. Total work consisted of: SHA hashing, pypdf text
extraction (page 1 + last page + metadata), single-source content
discrimination, file relocation, SHA256SUMS amendment, and bridge
handoff drafting — all CLI work, no browser-driven acquisition.
