# Phase B — OA acquisition route findings

Date: 2026-05-04
Target: Wasow 1965, *Asymptotic Expansions for Ordinary Differential
Equations*, §X.3 Theorem 11.1 (sectorial asymptotic existence at
fractional rank q ≥ 2; eq. 11.1 statement + 11.2–11.10 proof
construction; "anormal-case" reduction).

## Route summary

| # | Source | URL | Access | Text-layer / OCR | Verdict |
|---|--------|-----|--------|------------------|---------|
| 1 | Internet Archive — `asymptoticexpans0000waso` (Trent Univ. donation, 1965 Interscience original) | https://archive.org/details/asymptoticexpans0000waso | **Controlled Digital Lending** (Log In and Borrow; 1-hour or 14-day loan; `inlibrary` + `printdisabled` + `access-restricted-item: true`) | **OCR present**: ABBYY FineReader 11.0 (Extended OCR), language = English, ix + 362 p., 24 cm | **PRIMARY ROUTE** — operator-side login required (Rule 2: not auto-submitted) |
| 2 | Internet Archive — `bwb_P8-CYE-039` (1965-01-01 Interscience reprint) | https://archive.org/details/bwb_P8-CYE-039 | Controlled Digital Lending (same scheme) | **OCR present**: tesseract 5.3.0-3-g9920, lang=en, 194 previews recorded | SECONDARY (parallel CDL copy) |
| 3 | Internet Archive — `DTIC_ADA038949` "Outer Solutions for General Linear Turning Point Problems" | https://archive.org/details/DTIC_ADA038949 | Open | Not Wasow 1965 — different DTIC technical report | NIA (false positive in IA search) |
| 4 | HathiTrust full-view filtered search ("ft=ft&setft=1") | https://catalog.hathitrust.org/Search/Home?lookfor=asymptotic+expansions+for+ordinary+differential+equations&searchtype=title&ft=ft&setft=1 | Public | "No results matched your search" | NIA — no full-view (fully-OA) Hathi copy exists |
| 5 | Google Books snippet view | search index | Public preview | Search-form returned for `id=tWoZAQAAIAAJ` was a non-match (Pierre Fournier biography); no clean snippet endpoint identified for Wasow 1965 | NIA — no public Google-Books snippet view located for the Wasow volume in this probe |
| 6 | Author / institutional repository (Wasow ↔ UW-Madison Math) | n/a | Not searched exhaustively | n/a | Out-of-scope at this budget (no obvious institutional OA deposit; deferred) |
| 7 | Local library loan (operator in Yokohama) — Yokohama City / Keio / Tokyo Univ. catalogs | n/a | Operator-side | n/a | Operator-gated per Rule 2; deferred (CDL via route 1 is faster) |

## Public DOWNLOAD endpoints — explicit checks

- `archive.org/details/asymptoticexpans0000waso` page has a "DOWNLOAD
  OPTIONS" panel that displays: **"No suitable files to display
  here."** This is consistent with `access-restricted-item: true`
  (CDL gating; download disabled outside borrow session).
- The conventional `archive.org/stream/<id>/<id>_djvu.txt` full-text
  endpoint returns the IA boilerplate page only (no OCR body served
  for this CDL item). Confirmed by fetching
  `archive.org/stream/asymptoticexpans0000waso/asymptoticexpans0000waso_djvu.txt`
  on 2026-05-04 — only the See-Other-Formats wrapper rendered, no
  text body.

## Quality assessment of route 1 (PRIMARY)

When borrowed via CDL session, the IA BookReader exposes:

- Per-page rendered scan (image-faithful);
- An OCR text layer underneath (ABBYY FineReader 11.0 extended OCR);
- An in-book search box that matches OCR tokens and jumps to page
  anchors (the URL pattern `?q=%22Theorem+11.1%22` is the standard
  search-anchor invocation);
- Copy-from-search snippets up to a few hundred characters per page
  (per IA's CDL UI conventions).

Provided that the OCR-detected language is English (confirmed) and
that the original Interscience typography is high-contrast Roman, the
ABBYY 11.0 OCR quality on a mathematical text of this period is
generally **acceptable for verbatim quotation of theorem statements
and short equation labels**, with two known caveats:

1. Fraktur / German typography (none expected in Wasow 1965 main
   text; bibliography may have foreign-language entries — out of
   scope for §X.3);
2. Mathematical inline expressions: ABBYY 11.0 reliably captures
   Latin letters, common operators (∂, Σ, ∫, ≤, ≥, ∞), Greek letters
   (mostly) and subscripts/superscripts at headline scale; small
   indices and accent marks may need manual proofing. For a verbatim
   §X.3 Theorem 11.1 quote (≤30 words per quote per the relay's
   forbidden-verb hygiene), this is **sufficient** but should be
   diff-checked against the slot-04 image PDF before AEAL-hashing.

## Conclusion of Phase B

Two clean **operator-gated** routes (CDL borrow at archive.org of
either `asymptoticexpans0000waso` or `bwb_P8-CYE-039`) and one clean
**in-house** fallback (Tesseract on slot 04 §X.3 pages, blocked on
operator-side `winget install --id UB-Mannheim.TesseractOCR`). No
fully-OA route was located within the compute budget.
