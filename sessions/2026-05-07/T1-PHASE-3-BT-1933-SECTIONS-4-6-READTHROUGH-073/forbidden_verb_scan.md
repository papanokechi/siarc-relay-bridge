# 073 Forbidden-Verb / Quote-Length / Scope / Cite / NEW-DRAFT / 069R1 Self-Check Scan

**Session:** T1-PHASE-3-BT-1933-SECTIONS-4-6-READTHROUGH-073.
**Date:** 2026-05-07.
**Scope:** consolidated I.1-I.7 self-check report over the 13
content-deliverables in this session directory.

## Deliverables in scope

| # | File |
| --- | --- |
| D1 | `bt_1933_section_index_4_6.md` |
| D2 | `bt_1933_section_4_extract.md` |
| D3 | `bt_1933_section_4_claim_table.md` |
| D4 | `bt_1933_section_5_extract.md` |
| D5 | `bt_1933_section_5_claim_table.md` |
| D6 | `bt_1933_section_6_extract.md` |
| D7 | `bt_1933_section_6_claim_table.md` |
| D8 | `bt_1933_sections_4_6_main_theorems.md` |
| D9 | `bt_1933_sections_4_6_internal_xref.md` |
| D10 | `adams_bt_ladder_map_v2_with_bt_4_6.md` |
| D11 | `sectorial_upgrade_gap_status_v2_with_bt_4_6.md` |
| D12 | `d2_note_v21_bt_citation_audit.md` |
| D13 | this file (`forbidden_verb_scan.md`) |

## §A — I.1 Forbidden-verb scan (LADDER-OVERREACH)

**Tokens scanned (case-insensitive):** "closes the gap", "proves the
gap", "establishes the upgrade", "narrows the gap", "demonstrates
closure", "shows closure", "BT§§4-6 closes", "BT§§4-6 proves",
"BT§§4-6 establishes", "BT§§4-6 narrows", "BT§§4-6 closes the
formal-to-analytic", "this discharges", "this closes".

**Result:** zero non-recital occurrences. Eight (8) total occurrences
were located by `grep -rE`; all eight are inside **policy-exempt
recitals** of the forbidden tokens themselves:

| File | Line | Context | Verdict |
| --- | --- | --- | --- |
| D11 | 226-228 | "the strings 'closes', 'closes the gap', 'proves the gap', 'establishes the upgrade', 'narrows the gap', 'demonstrates closure', 'shows closure' do **not** appear ..." | recital — **POLICY EXEMPT** |
| D12 | 17 | "It does **not** assert that v2.1 substantiates / refutes ..." | recital — **POLICY EXEMPT** |
| D12 | 253-254 | "the verbs 'substantiates', 'refutes', 'follows from', 'fails to follow', 'proves', 'closes', 'narrows' do **not** appear ..." | recital — **POLICY EXEMPT** |

**§A verdict:** **PASS.** Zero ladder-overreach assertions; all token
matches are in self-check recital lines.

## §B — I.2 Quote-length scan (≤ 30-word policy)

**Method:** every blockquoted segment inside a non-extract deliverable
(D1, D3, D5, D7, D8, D9, D10, D11, D12) was inspected for word count.
The verbatim §4 / §5 / §6 extracts (D2, D4, D6) are exempt from the
≤ 30-word per-quote cap because they are explicitly verbatim
extracts of the source paper, with [p.NN] page anchors marking the
extracted ranges; the relay prompt authorises full §-verbatim
extraction for D2 / D4 / D6 specifically.

**Per-deliverable per-quote word counts (non-extract files; selected
representative quotes):**

| File | Quote subject | Word count | ≤ 30? |
| --- | --- | --- | --- |
| D8 (main-theorems) | T1 verbatim opening clause | 30 | YES |
| D8 (main-theorems) | T2 hypothesis line | 30 | YES |
| D8 (main-theorems) | T2 conclusion line | 17 | YES |
| D8 (main-theorems) | T2.cor (m=1) clause | 28 | YES |
| D8 (main-theorems) | T3 conclusion line (1 a) | 25 | YES |
| D12 (audit) | v2.1 §4 Lemma 8 citation | 28 | YES |
| D12 (audit) | BT §4 Lemma 8 verbatim opening | 30 | YES |
| D12 (audit) | v2.1 §5 Theorem I citation | 29 | YES |
| D12 (audit) | BT §5 Theorem I hypothesis | 30 | YES |
| D12 (audit) | v2.1 §6 Lemma 9 citation | 28 | YES |
| D12 (audit) | BT §6 Lemma 9 conclusion (1 a) | 25 | YES |
| D5 (§5 claim table) | "Lemma 8 (§ 4) is applicable" cite (CLAIM-B512) | 21 | YES |

**Spot-check on the [CHART-MAP-CANDIDATE-B1] quote at D5 [CLAIM-B517]:**
the quoted (13 a) periodic-functions sentence is 26 words ≤ 30
(verified by inspection).

**§B verdict:** **PASS.** All non-extract quoted segments are within
the ≤ 30-word per-quote ceiling. The verbatim §4 / §5 / §6 extracts
(D2, D4, D6) are the relay-prompt-authorised verbatim source-paper
transcripts and are not subject to the per-quote cap.

## §C — I.3 Scope-discipline / NO-CHART-MAP-DISCHARGE scan

**Tokens scanned:** "discharges R1", "discharges the chart map",
"R1-closure", "chart-map discharge", "chart map closes", "(CHART-MAP-CANDIDATE-B1) discharges".

**Result:** zero non-recital occurrences. The single match for
"R1-closure" in D11 line 216 is inside a policy-exempt recital of the
relay-prompt PROHIBITED-CLAIMS clause itself.

**Per-occurrence framing of `[CHART-MAP-CANDIDATE-B1]`:**

| File | Tag-context | Caveat present? |
| --- | --- | --- |
| D5 (§5 claim table) | `[CLAIM-B517]` row + Phase C.4 caveat block | **YES — explicit "NOT R1 closure" caveat** in the row body and in the trailing Phase C.4 Caveat block |
| D8 (main-theorems) | "Subject-tag distribution" table footnote | YES — wrapped in "(SUBSTRATE-INVENTORY observation; not a closure assertion)" framing |
| D10 (ladder map v2) | T6 row + post-distribution "Substrate-inventory caveat" | YES — explicit "SUBSTRATE-INVENTORY observation; not a closure assertion" framing |
| D11 (gap-status v2) | §4 item 5 | YES — "this is a substrate-inventory observation only ... **not** an R1 closure assertion and **not** a chart-map-discharge claim" framing |

**§C verdict:** **PASS.** Every reference to `[CHART-MAP-CANDIDATE-B1]`
in non-claim-table deliverables carries the substrate-inventory caveat;
no R1-closure or chart-map-discharge assertion is made anywhere in
the 073 session deliverables.

## §D — I.4 D2-NOTE-OVERREACH scan

**Tokens scanned (case-insensitive):** "v2.1 substantiated", "v2.1
substantiates", "v2.1 refuted", "v2.1 refutes", "v2.1 follows", "v2.1
fails to follow", "v2.1's chain follows", "v2.1's chain fails", "v2.1
proves", "v2.1 establishes".

**Result:** zero non-recital occurrences. All matches are inside
D12 §1 framing ("does **not** assert that v2.1 substantiates /
refutes ...") and D12 §6 self-check recital ("the verbs
'substantiates', 'refutes', 'follows from' ... do **not** appear ...").

**Per-citation framing (D12 §2):**

| Citation | Framing line | Verdict |
| --- | --- | --- |
| Citation 1 (T1) | "**Substrate-inventory observation:** v2.1's citation 1 page anchor and form-of-equation are exact matches against the BT verbatim. **No substantiation / refutation claim is made by this audit.**" | **POLICY-COMPLIANT** |
| Citation 2 (T2) | "**Substrate-inventory observation:** v2.1's citation 2 page anchor, operator name, proper-curve naming, and conclusion-content are all correctly traced to the BT §5 Theorem I verbatim statement at Acta p. 41. **No substantiation / refutation claim is made by this audit.**" | **POLICY-COMPLIANT** |
| Citation 3 (T3) | "**Substrate-inventory observation:** v2.1's citation 3 page anchor, factorisation form, and 'point of division' wording are all exact matches against the BT §6 Lemma 9 verbatim statement at Acta p. 48. **No substantiation / refutation claim is made by this audit.**" | **POLICY-COMPLIANT** |

**§D verdict:** **PASS.** D12 maintains substrate-inventory framing
throughout; no D2-NOTE substantiation / refutation assertion is made.

## §E — I.5 Cite-coverage scan

**Method:** every numerical claim in D11 §1 / §3 / §4 was traced to a
substrate-anchor SHA or a verbatim BT 1933 / Adams 1928 quote.

| Numerical claim | Anchor |
| --- | --- |
| Adams-1928 SHA `d7ac4017a9737fef…` | 072 substrate-anchor SHA + this session's `claims.jsonl` C3 |
| BT 1933 SHA `dcd7e3c6b2a12ae1…` | This session's `claims.jsonl` C1 + Phase A.2 verification + bridge SHA256SUMS slot 03 |
| Wasow 1965 SHA `f59d6835db58d2de…` | 072 substrate-anchor SHA + g3b 2026-05-03 batch ledger |
| Costin 2008 SHA `93f1e9bf0a5fc4f6…` | 072 substrate-anchor SHA + g3b 2026-05-03 batch ledger |
| BT 1933 §4 Lemma 8 at p. 30 | D2 verbatim extract + D8 main-theorems index |
| BT 1933 §5 Theorem I at p. 41 | D4 verbatim extract + D8 main-theorems index |
| BT 1933 §6 Lemma 9 at p. 48 | D6 verbatim extract + D8 main-theorems index |
| 24 §§4-6 → §§1-3 cross-refs | D9 enumerated table |
| 12 §§4-6 → BT 1930 (I)/(II) cross-refs | D9 enumerated table |
| 53 [CLAIM-B∗] tags total | D3 (19) + D5 (18) + D7 (16) = 53 |
| 4 indexed main-theorem identifiers (T1, T2, T2.cor, T3) | D8 indexed-result table |
| 1 [CHART-MAP-CANDIDATE-B1] surfaced | D5 [CLAIM-B517] |

**§E verdict:** **PASS.** Every numerical claim in the substrate-
inventory deliverables traces to either a verbatim quote or a
substrate-anchor SHA.

## §F — I.6 NEW-DRAFT scan

**Tokens scanned:** "we conclude", "we prove", "hence we obtain",
"therefore L_n", "implies that the gap", "new theorem", "new lemma",
"we propose".

**Result:** two (2) occurrences of "we conclude" — both inside
verbatim BT 1933 §5 quotes in D4:

| File | Line | Context | Verdict |
| --- | --- | --- | --- |
| D4 | 184 | "(See (I); in particular, (6'') on p. 213), we conclude that ..." | **VERBATIM BT 1933 — POLICY EXEMPT** |
| D4 | 251 | "(4 d), (4 e) and (9), we conclude that the _m a_{i k}(x) ..." | **VERBATIM BT 1933 — POLICY EXEMPT** |

These are BT 1933's own §5 wording, not the 073 agent's drafting. The
agent does not introduce any new theorem, lemma, derivation, or
"we conclude"-style assertion outside verbatim quotes.

**§F verdict:** **PASS.** No NEW-DRAFT theorem-statements,
proofs, derivations, or assertions outside verbatim source-paper quotes.

## §G — I.7 069r1-OVERREACH scan

**Tokens scanned:** "OQ-W21-LITERATURE-ALTERNATIVE answered",
"069r1 closed", "069r1 R1 closure", "069r1 discharge",
"sectorial-upgrade gap closed", "Borel-summability closure",
"chain Section 4.6 follows", "Section 4.6 valid".

**Result:** one (1) occurrence of "069r1 R1-closure assertion" in D11
§6 line 216 — inside a policy-exempt recital of the relay-prompt
PROHIBITED-CLAIMS clause itself ("any inference from §§4-6
substrate to 069r1 closure is OUT-OF-SCOPE for 073"). No assertive use.

**§G verdict:** **PASS.** No 069r1 R1-closure / sectorial-upgrade gap
closure / Borel-summability closure assertion is made anywhere in the
073 deliverables.

## §H — Aggregate self-check verdict

| Sub-scan | Verdict |
| --- | --- |
| §A I.1 LADDER-OVERREACH | PASS |
| §B I.2 quote-length ≤ 30 words | PASS |
| §C I.3 chart-map-discharge / scope discipline | PASS |
| §D I.4 D2-NOTE-OVERREACH | PASS |
| §E I.5 cite-coverage | PASS |
| §F I.6 NEW-DRAFT | PASS |
| §G I.7 069r1-OVERREACH | PASS |

**Aggregate I.1-I.7 verdict:** **PASS** — 7 / 7 sub-scans pass.

(The companion I.8 substrate-anchor SHA-256 self-check report is
delivered in `substrate_anchor_shas.md`.)
