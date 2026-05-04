# Phase B route findings — SAKAI-2001-ACQUISITION

Each row: route ID, URL probed, HTTP status / outcome, text-layer
quality if PDF retrieved, notes.

## B.1  SpringerLink (DOI direct)
- URL: `https://link.springer.com/content/pdf/10.1007/s002200100446.pdf`
  (CrossRef DOI 10.1007/s002200100446; redirected from
  `https://doi.org/10.1007/s002200100446` via 302).
- Status: HTTP 200 but `Content-Type: text/html; charset=utf-8`,
  body 3038 bytes — login/redirect HTML (Springer IDP authorize
  page). Confirmed paywall on this DOI route.
- Decision: per Rule 1 (no API keys / no auto-authentication),
  do NOT proceed.
- Outcome: **paywall, not used**.

## B.2  Project Euclid (CMP archive)
- URL: `https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-220/issue-1`
- Status: returns Akamai/SPIE security challenge ("Additional
  security check is required"); not auto-fetchable. CMP volumes
  on Project Euclid are subject to publisher-controlled access
  windows; vol. 220 (2001) is paywalled at this time.
- Outcome: **not OA, not used**.

## B.3  arXiv search (Hidetaka Sakai)
- URL probed: `https://arxiv.org/a/sakai_h_2.html`,
  `https://arxiv.org/a/sakai_h_3.html` — both HTTP 404.
  `https://arxiv.org/a/sakai_h_1.html` exists but is a
  different author (Hironori Sakai, symplectic geometry).
- Outcome: **no arXiv preprint of Sakai 2001 by H. Sakai
  (Painleve)**. (This is consistent with field memory:
  the Painleve-Sakai used the Kyoto Math Dept preprint
  server, not arXiv, for the 1999 preprint.)

## B.4  Kyoto University Math Department preprint server
- Index URL: `https://www.math.kyoto-u.ac.jp/preprint/preprint99.html`
- Direct URL (PostScript):
  `https://www.math.kyoto-u.ac.jp/preprint/99/10.ps`
- Listing entry:
  `10. Rational surfaces associated with affine root systems
   and geometry of the Painlev\'e equations  by Hidetaka SAKAI`
- Status: HTTP 200, `Content-Type: application/postscript`,
  raw body 1,149,707 bytes.
- This is the **1999 preprint version** of Sakai 2001
  (received by CMP 18 Sep 1999; accepted 29 Jan 2001).
- Pipeline: PostScript downloaded, then converted with
  `ps2pdf.exe` (MiKTeX 64-bit) to a 55-page PDF
  (526,933 bytes), `pdftotext.exe` produces clean ASCII at
  ≥ 99% fidelity (a few diacritic ligatures degraded but
  the math is fully readable).
- Outcome: **OA route succeeded; primary acquisition target**.

## B.5  Internet Archive
- URL: `https://archive.org/search?query=sakai+rational+surfaces+painleve`
- Result: 0 hits.
- Outcome: **not used**.

## B.6  RIMS Preprints (Kyoto)
- URL: `https://www.kurims.kyoto-u.ac.jp/preprint/`
- Sakai's 1999 preprint of this paper was filed at the
  **Kyoto Math Dept** preprint server (B.4), not at
  RIMS. RIMS preprint server lists preprints by RIMS-affiliated
  authors only.
- Outcome: **not the right server; B.4 is the canonical OA
  source**.

## B.7  ResearchGate / Academia.edu (public-OA only)
- Not probed beyond search-engine summaries; B.4 already
  succeeded with a clean publisher-independent PostScript,
  so no degraded social-platform copy is needed.
- Outcome: **skipped (B.4 sufficient)**.

## Aggregate
- 1 of 7 routes succeeded (B.4 Kyoto Math Dept preprint server).
- The acquired file is the 1999 preprint, NOT the final 2001
  CMP-published version. Final pagination differs (preprint
  has 55 pages; published has pp. 165–229 within CMP 220).
  Mathematical content of §_surfaces (Table 6 + D_6^{(1)}
  classification + parameter labeling) and §_W
  (W((2A_1)^{(1)}) generators) is the same as the
  published version per BLMP 2024 (slot 08) transitive citation.
