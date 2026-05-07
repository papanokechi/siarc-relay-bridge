# BT 1933 §§4–6 — Section Index

**Source PDF SHA-256:**
`dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6`
**File:** `tex/submitted/control center/literature/g3b_2026-05-03/03_birkhoff_trjitzinsky_1933_acta60.pdf`
**Total PDF pages:** 89 (Acta Math. 60, 1933, pp. 1–89). PDF page index
equals printed Acta page number throughout (verified against PDF
running-head sample on PDF p. 30 which carries printed "30").

## §-titles (verbatim, from PDF p. 1 table-of-contents block)

The TOC on PDF p. 1 (printed p. 1) lists the section titles
verbatim. Three of them are this readthrough's scope:

| § | Title (verbatim from BT 1933 TOC, p. 1) |
| --- | --- |
| 4 | A lemma on summation. |
| 5 | Construction of proper solutions to the right of a proper curve. |
| 6 | A lemma on factorization. |

## Page span (PDF page = printed Acta page; PDF p N  =  Acta p N)

| § | Title | Acta first page | Acta last page | PDF first | PDF last |
| --- | --- | --- | --- | --- | --- |
| §4 | A lemma on summation | p. 29 | p. 40 | 029 | 040 |
| §5 | Construction of proper solutions to the right of a proper curve | p. 40 | p. 48 | 040 | 048 |
| §6 | A lemma on factorization | p. 48 | p. 51 | 048 | 051 |

§5 starts after the closing line of §4 on Acta p. 40, and §6 starts
after the closing line of §5 on Acta p. 48. The §6 trailing remark
"...will be s-series" sits on Acta p. 51, and §7 "On Products of
Completely Proper Operators" begins on the same Acta p. 51.

## Adjacent sections (out-of-scope context)

| § | Title (verbatim from BT 1933 TOC, p. 1) |
| --- | --- |
| 1 | Introduction. |
| 2 | On B′ and proper curves. |
| 3 | Lemmas on iteration. |
| 7 | Products of completely proper operators. |
| 8 | Completion of the proof of the Theorem of §7. |
| 9 | The Fundamental Existence Theorem. |
| 10 | Connection between 'upper' and 'lower' solutions. |
| 11 | The converse problem. |
| 12 | The related Riemann problem. |

§§1–3 supply the setup machinery that §§4–6 cite (Lemmas 4, 5, 6, 7
of §3 are referenced inside §5; the formal-series Definition 1 of §1
is referenced in Lemma 8 statement; the proper-curve Definitions 3,
5, 9 of §§1–2 are referenced in §5 + §6; the factorability Definition
8 of §1 is referenced in §6 Lemma 9). §§7–9 consume §§4–6 outputs
(§§7–8 use Theorem I of §5; §9 uses both Theorem I and Lemma 9).

## Pypdf glyph-substitution note

The pypdf 6.10.2 text-extractor renders the BT 1933 source-font §
glyph as the ASCII letter "w". Throughout this readthrough the
verbatim quotes silently restore § when reproducing TOC + section
headers (e.g., "w 4." in pypdf output  =>  "§ 4." in the printed
paper). Body-text quotes that contain the § symbol carry the same
silent restoration. No other glyph substitution was applied.
A second observed substrate-font artefact: the §6 title in pypdf
output reads "Faetorization" where the printed paper reads
"Factorization" (single-letter font-glyph drift "c" → "e"). The
two artefacts are documented in `discrepancy_log.json` D1.

## Cross-walk to 072 sectional-header quick-scan

072 (Adams 1928 readthrough; bridge HEAD `5b297cb`) recorded BT 1933
sectional-header structure via pypdf quick-scan (072
`adams_to_bt1933_ladder_map.md` "Cross-walk capability assessment"
section). The present 073 readthrough confirms that quick-scan
result: §4 = Lemma on Summation, §5 = Theorem I, §6 = Lemma 9, with
§-page anchors as listed above. No drift detected.
