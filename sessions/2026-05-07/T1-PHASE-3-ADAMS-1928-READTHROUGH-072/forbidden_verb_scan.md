# Phase E Self-Check Report

**Session:** 2026-05-07 T1-PHASE-3-ADAMS-1928-READTHROUGH-072.
**Scan tool:** `_working/self_check.py` (Python; see file for source).
**Raw JSON output:** `_working/self_check_raw.json` (intermediate; not
committed to bridge).

This file consolidates the results of Phase E self-checks E.1
(forbidden-verb), E.2 (quote-length), E.3 (scope-discipline), E.4
(cite-coverage spot-check), E.5 (NEW-DRAFT scan), E.6 (deliverable
SHAs).

## Exemption policy (per P6, P7)

A match is **exempt** if any of the following hold:

- **(a) In-quote:** the match falls inside a Markdown blockquote (line
  starts with `>`), inside a straight-double-quoted span (whole-file
  quote-parity is odd at the match), or inside a backtick code span
  (whole-file backtick-parity is odd at the match).
- **(b) File-wholly-verbatim:** the match is in a deliverable file
  whose entire body is a verbatim Adams 1928 substrate-extraction
  rendering. The two such files in this session are
  `adams_1928_section_1_extract.md` and
  `adams_1928_section_2_extract.md`. Per P6, every Adams 1928 verbatim
  citation is exempt because it is a substrate citation rather than a
  new conjectural-or-prediction claim.
- **(c) File-is-scan-report:** the present file
  (`forbidden_verb_scan.md`) enumerates every forbidden + scope-
  overreach token by design (in the scan-token list and in the table
  rows that report each hit). Per the spirit of P6, these
  policy-token enumerations are not new conjectural-or-prediction
  claims and are exempt at file level.

## §A — E.1 forbidden-verb scan

Scan tokens: `\bshows\b`, `\bconfirms\b`, `\bproves\b`,
`\bestablishes\b`, `\bmust\b`, `\bdemonstrates\b`, `\btrivially\b`,
`\bclearly\b`, `\bobviously\b`, `\bWe claim\b`, `\bIt is clear that\b`
(case-insensitive).

| Status | File | Line | Match | Exemption basis |
| --- | --- | --- | --- | --- |
| EXEMPT | adams_1928_section_1_2_claim_table.md | 49 | shows | (a) in-quote |
| EXEMPT | adams_1928_section_1_2_claim_table.md | 50 | confirms | (a) in-quote |
| EXEMPT | adams_1928_section_1_2_claim_table.md | 50 | proves | (a) in-quote |
| EXEMPT | adams_1928_section_1_2_claim_table.md | 50 | establishes | (a) in-quote |
| EXEMPT | adams_1928_section_1_2_claim_table.md | 15 | must | (a) in-quote (header note enumerating policy tokens with backticks) |
| EXEMPT | adams_1928_section_1_2_claim_table.md | 51 | must | (a) in-quote |
| EXEMPT | adams_1928_section_1_2_claim_table.md | 52 | must | (a) in-quote |
| EXEMPT | adams_1928_section_1_2_claim_table.md | 50 | demonstrates | (a) in-quote |
| EXEMPT | adams_1928_section_1_2_claim_table.md | 50 | trivially | (a) in-quote |
| EXEMPT | adams_1928_section_1_2_claim_table.md | 51 | clearly | (a) in-quote |
| EXEMPT | adams_1928_section_1_2_claim_table.md | 51 | obviously | (a) in-quote |
| EXEMPT | adams_1928_section_1_2_claim_table.md | 51 | we claim | (a) in-quote |
| EXEMPT | adams_1928_section_1_2_claim_table.md | 51 | it is clear that | (a) in-quote |
| EXEMPT | adams_1928_section_1_extract.md | 75 | must | (b) file-wholly-verbatim (Adams §1 p. 510) |
| EXEMPT | adams_1928_section_1_extract.md | 108 | clearly | (b) file-wholly-verbatim (Adams §1 fn p. 510) |
| EXEMPT | adams_1928_section_1_extract.md | 122 | clearly | (b) file-wholly-verbatim (Adams §1 p. 511) |
| EXEMPT | adams_1928_section_2_extract.md | 135 | clearly | (b) file-wholly-verbatim (Adams §2 p. 515) |
| EXEMPT | sectorial_upgrade_gap_status.md | 203–204 | shows / proves / establishes / demonstrates | (a) in-quote (HALT-name enumeration in §4 self-check disclaimer block) |

**Non-exempt count:** 0. **Pass status:** PASS.
**HALT_072_FORBIDDEN_VERB:** NOT TRIGGERED.

## §B — E.2 quote-length scan

Tokenisation: split on `[\s\-\u2014\u2013()]+` per P7 "counting all
hyphen-joined / em-dashed / parenthesised segments as separate words".

Scan domain: every straight-double-quoted span on a single line + every
straight-double-quoted span within a Markdown blockquote.

**Hits with word count > 30:** 0.
**HALT_072_QUOTE_LENGTH_VIOLATION:** NOT TRIGGERED.

The maximum word counts observed across all deliverables (after Phase
E first-pass remediation) are:

- Adams 1928 main-theorems T9 quote: 27 words (regions-of-validity
  caveat at p. 541, trimmed to omit the "Whatever the relative size and
  position of the two polygons may be" prefix).
- Adams 1928 closing-paragraph extension-clause: 28 words (after light
  elision of "one or more of the").
- Adams 1928 BT 1933 p. 5 self-statement: 22 + 29 words across two
  paired sentences (each individually within the 30-word cap).
- Adams 1928 §1+§2 claim-table verbatim entries: each ≤ 30 words.

## §C — E.3 scope-discipline scan

Scan tokens (all case-insensitive): `closes`, `closes the gap`, `proves
the gap`, `establishes the upgrade`, `narrows the gap`, `demonstrates
closure`, `shows closure`.

| Status | File | Line | Match | Exemption basis |
| --- | --- | --- | --- | --- |
| EXEMPT | sectorial_upgrade_gap_status.md | 202 | closes (×2) | (a) in-quote (literal HALT-token enumeration in self-check disclaimer; backtick-quoted) |
| EXEMPT | sectorial_upgrade_gap_status.md | 202 | closes the gap | (a) in-quote (HALT-token enumeration) |
| EXEMPT | sectorial_upgrade_gap_status.md | 203 | proves the gap / establishes the upgrade / narrows the gap | (a) in-quote (HALT-token enumeration) |
| EXEMPT | sectorial_upgrade_gap_status.md | 204 | demonstrates closure / shows closure | (a) in-quote (HALT-token enumeration) |

**Non-exempt count:** 0.
**HALT_072_LADDER_OVERREACH:** NOT TRIGGERED.

The two earlier-flagged "closes" instances on
`adams_1928_main_theorems_summary.md` line 40 and
`adams_1928_section_index.md` line 25 were rewritten to "ends" (in the
T9 closing-paragraph caveat introduction) and "ends" (in the §8 row of
the section-index table) during Phase E first-pass remediation.

## §D — E.4 cite-coverage scan

Sampled 10 random claims spanning all primary deliverables:

1. Section index §1 row → page-anchor "p. 509"; SHA-anchor pinned at
   file-header. PASS.
2. §1 extract `[CLAIM-B4]` Newton polygon → page-anchor "p. 511";
   verbatim quote from PDF p. 6. PASS.
3. §2 extract `[CLAIM-B12]` Class 2a formal series → page-anchor
   "p. 513"; verbatim quote from PDF p. 8. PASS.
4. Claim table `CLAIM-B6` segment-degree formula → page-anchor
   "p. 511"; verbatim ≤ 29 words. PASS.
5. Main-theorems T1 (Theorem A) → page-anchor "p. 529"; opening clause
   verbatim 18 words; full statement paraphrased per P7. PASS.
6. Main-theorems T9 regions-of-validity caveat → page-anchor
   "p. 541"; verbatim 27 words. PASS.
7. Bibliography Birkhoff 1911 → footnote-anchor "PDF p. 03"; verbatim.
   PASS.
8. Bibliography BT-cross-walk Adams entry → BT 1933 page-anchor
   "p. 5"; verbatim. PASS.
9. Ladder map T1 → BT 1933 §5 + §9 cross-reference; SHA-anchored to BT
   slot 03. PASS.
10. Gap-status §4 item 5 (regions-of-validity caveat) → page-anchor
    "p. 541" + verbatim ≤ 30 words. PASS.

**Spot-check pass rate:** 10 / 10 = 100%.
**HALT_072_CITE_COVERAGE_GAP:** NOT TRIGGERED.

## §E — E.5 NEW-DRAFT scan (Phase D.2 §4 + §5)

`sectorial_upgrade_gap_status.md` Phase D.2 §4 (GAP CHARACTERISATION):
sentence count 10 (≤ 25 cap). Per-sentence anchoring:

- §4 items 1–8 each cite a section + printed-page anchor (Adams
  §§1, 2, 6, 8 with explicit printed-page numbers).
- §4 item 9 is a substrate-inventory-discipline restatement.
- §4 item 10 is a self-check disclaimer referring to
  HALT_072_LADDER_OVERREACH and P8.

Anchoring rate: 10 / 10 = 100%.

`sectorial_upgrade_gap_status.md` Phase D.2 §5 (RESIDUAL ITEMS):
sentence count 9 (≤ 25 cap). Per-sentence anchoring:

- Items 1–7 each cite a substrate slot (Wasow ch. X §3, Loday-Richaud
  2016, Carmichael 1912, BT 1933 §§7–9, Galbrun 1913, Norlund 1924,
  Perron 1917) with explicit Adams or BT 1933 page anchor or
  acquisition-status note.

Anchoring rate: 9 / 9 = 100%.

**HALT_072_NEW_DRAFT_ATTEMPTED:** NOT TRIGGERED.

## §F — E.6 SHA-256 of deliverable files

See `substrate_anchor_shas.md` for the canonical SHA list, computed
after all Phase E remediations.

## Aggregate verdict

| Halt | Status |
| --- | --- |
| HALT_072_FORBIDDEN_VERB | NOT TRIGGERED |
| HALT_072_QUOTE_LENGTH_VIOLATION | NOT TRIGGERED |
| HALT_072_LADDER_OVERREACH | NOT TRIGGERED |
| HALT_072_CITE_COVERAGE_GAP | NOT TRIGGERED |
| HALT_072_NEW_DRAFT_ATTEMPTED | NOT TRIGGERED |

All Phase E self-checks PASS. HALT_072_OVER_CLAIM 4-item checklist
items (1)–(3) are satisfied at the scan level; item (4) is satisfied
in the handoff.md "What was accomplished" + "Recommended next step"
sections.

**Verdict:** CLEAN_EXTRACT.
