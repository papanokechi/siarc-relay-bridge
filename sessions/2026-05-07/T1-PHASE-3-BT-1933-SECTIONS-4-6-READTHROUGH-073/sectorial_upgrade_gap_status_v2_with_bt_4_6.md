# Sectorial-Upgrade Gap — Substrate-Inventory Status Report v2 (with BT 1933 §§4-6)

**Session:** 2026-05-07 T1-PHASE-3-BT-1933-SECTIONS-4-6-READTHROUGH-073.

**Predecessor:** 072 v1 at
`siarc-relay-bridge/sessions/2026-05-07/T1-PHASE-3-ADAMS-1928-READTHROUGH-072/sectorial_upgrade_gap_status.md`
(072 commit `5b297cb`).

**Scope:** SUBSTRATE-INVENTORY ONLY. This file enumerates which
classical-result substrate is on-disk for the SIARC-stratum
formal-to-analytic sectorial-upgrade question at d ≥ 3, after the
2026-05-07 Adams 1928 acquisition (072) **and** the present 073
session's verbatim BT 1933 §§4-6 readthrough. It does **not** assert
that any gap is closed, narrowed, proved, established, or
demonstrated. Per relay-prompt P8 (verdict-ladder honesty) and
HALT_073_LADDER_OVERREACH, this file maintains substrate-inventory
framing throughout.

---

## §1 — Substrate now on-disk + verbatim-extracted (post 2026-05-07 073)

| Slot | Author/Year | On-disk PDF SHA-256 (first 16 hex) | Verbatim-extracted in session | §-level coverage of verbatim extracts |
| --- | --- | --- | --- | --- |
| Adams-1928 | C. R. Adams (1928) | `d7ac4017a9737fef…` | 2026-05-07 (072) | §§1–2 + §6 + §8 verbatim with [CLAIM-A∗] tags; T1-T9 main-theorems index |
| 03 | BT 1933 | `dcd7e3c6b2a12ae1…` | 2026-05-07 (073, this session) | **§§4-6 verbatim with [CLAIM-B4∗], [CLAIM-B5∗], [CLAIM-B6∗] tags; T1=§4 Lemma 8 / T2=§5 Theorem I / T3=§6 Lemma 9 main-theorems index. §§1-3 + §§7-12 NOT verbatim-extracted in this session.** |
| 04 | Wasow 1965 (Dover repr.) | `f59d6835db58d2de…` | NOT (substrate is on-disk; §-level extract DEFER) | — |
| 06 | Costin 2008 ch.5 | `93f1e9bf0a5fc4f6…` | NOT (substrate is on-disk; §-level extract DEFER) | — |

**Delta from 072 v1:** the BT 1933 entry has changed from
"NOT-verbatim-extracted" to "§§4-6 verbatim-extracted on
2026-05-07 (073)". All other rows are unchanged from 072 v1 §1.

---

## §2 — Substrate pre-073 (i.e. as of 072 v1 close)

Pre-073 snapshot (the state of the project literature folder + the
verbatim-extraction inventory at the close of the 072 v1 session on
2026-05-07):

| Slot | Verbatim-extracted? |
| --- | --- |
| Adams-1928 | YES (072) |
| 03 BT 1933 | NO — only quick-scan coverage from 072 (BT p. 5 quoted; p. 213, p. 215 page-numbers tagged; §§1-9 NOT extracted) |
| 04 Wasow 1965 | NO |
| 06 Costin 2008 ch.5 | NO |

The pre-073 verbatim-extraction state corresponds to the 072 v1
substrate-inventory snapshot recorded in 072
`sectorial_upgrade_gap_status.md` §1 (which framed BT 1933 as
"on-disk; full-paper coverage available; §§5+7+9 cited" but did
**not** carry verbatim ≤ 30-word extracts of BT 1933 main-theorem
statements).

---

## §3 — Delta since 072 v1 close

Exactly **one** verbatim-extraction delta since the 072 v1 session
close on 2026-05-07:

- **BT 1933 §§4-6** verbatim extracts now on-disk in the bridge
  session directory (this session, 073). Specifically:
  - `bt_1933_section_4_extract.md` — verbatim §4 with [p.NN] page
    anchors; Lemma 8 statement at p. 30.
  - `bt_1933_section_5_extract.md` — verbatim §5 with [p.NN] page
    anchors; Theorem I statement at p. 41; embedded periodic-functions
    object at p. 47 (13 a) tagged `[CHART-MAP-CANDIDATE-B1]`.
  - `bt_1933_section_6_extract.md` — verbatim §6 with [p.NN] page
    anchors; Lemma 9 statement at p. 48; D2-NOTE v2.1 §4.5 citation
    region surrounded by Lemma-9 verbatim quote.
  - Three claim tables (`bt_1933_section_4_claim_table.md`,
    `bt_1933_section_5_claim_table.md`,
    `bt_1933_section_6_claim_table.md`) — total 53 [CLAIM-B∗] tags.
  - Main-theorems index `bt_1933_sections_4_6_main_theorems.md` — 4
    indexed identifiers (T1, T2, T2.cor, T3).
  - Internal cross-reference tabulation
    `bt_1933_sections_4_6_internal_xref.md` — 24 earlier-section
    deps + 4 internal §4→§5 cites + 12 BT 1930 (I)/(II) cites.

No new PDFs were acquired in 073. The slot-PDF count is unchanged
from 072 v1.

---

## §4 — Gap characterisation (substrate-inventory level; with §§4-6 verbatim layer)

This section enumerates which classical-result coverage is now
verbatim-extracted in the on-disk substrate that was not
verbatim-extracted before BT 1933 §§4-6 went onto disk in
verbatim form. It is a substrate-coverage report, not a gap-closure
assertion.

1. BT 1933 §4 Lemma 8 (T1; Acta p. 30) is now on-disk in verbatim
   form. The statement gives the existence of an analytic solution
   y(x) of the difference equation y(x+1) − y(x) = e^{Q(x)} h(x) under
   the proper-curve + ℜ Q′ ≦ 0 hypotheses, with asymptotic relation
   y(x) ∼ e^{Q(x)} s(x).

2. BT 1933 §5 Theorem I (T2; Acta p. 41) is now on-disk in verbatim
   form. The statement gives the existence of a "completely proper"
   operator L_n in the region (m) + ... + (η) under a strip-V
   proper-fundamental-set hypothesis (or its m = 1 corollary form
   T2.cor where the strip-V hypothesis is omitted on the strength of
   Γ ⊂ region (1) only).

3. BT 1933 §6 Lemma 9 (T3; Acta p. 48) is now on-disk in verbatim
   form. The statement gives the factor-operator decomposition
   L_n = L_{n−Γ} L_Γ at a point of division between Γ-th and
   (Γ+1)-st terms when L_n is Q-factorable on (1) + ... + (m).

4. The §§4-6 verbatim layer adds explicit BT-side §-level granularity
   for the 6 of 9 Adams T1-T9 references that 072 v1 marked as
   secondary-DEFER pending the §§4-6 readthrough; these are now all
   resolved at §-level (cf. `adams_bt_ladder_map_v2_with_bt_4_6.md`
   distribution-table closing summary).

5. The §§4-6 verbatim layer carries one structural surface that was
   not surfaced by 072: the `[CHART-MAP-CANDIDATE-B1]` tagged
   sentence at `[CLAIM-B517]` (BT §5 p. 47 eq. (13 a) — the
   periodic-functions across-strip expansion). This is a
   substrate-inventory observation only; per Phase C.4 caveat in
   `bt_1933_section_5_claim_table.md`, this is **not** an R1 closure
   assertion and **not** a chart-map-discharge claim.

6. The §§4-6 verbatim layer confirms three D2-NOTE v2.1 §4.5 page
   anchors as exact: §4 Lemma 8 p. 30 (verified), §5 Theorem I p. 41
   (verified), §6 Lemma 9 p. 48 (verified). The page-anchor agreement
   does **not** by itself substantiate or refute v2.1's BT-citation
   argument; that is a synthesizer arbitration question
   (cf. `d2_note_v21_bt_citation_audit.md` for the side-by-side
   substrate-inventory layout).

7. The §§4-6 verbatim layer sets up the natural follow-up of a §§7-9
   verbatim readthrough (parallel to the §§4-6 readthrough), which
   would supply the verbatim text of the Fundamental Existence
   Theorem (§9) and Theorem II (§7). That follow-up is recorded
   below as residual item (4).

8. Per HALT_073_LADDER_OVERREACH and the verdict-ladder honesty
   discipline (P8), no statement in this section is a gap-closure
   assertion. Each of items 1–7 above is a substrate-coverage fact
   about what is now verbatim-extracted on-disk.

(Sentence count: 8. Within the E.5 ≤ 25-sentence cap. Anchoring rate:
8 / 8 = 100% — every sentence traces to a verbatim BT quote, a
substrate-anchor SHA, or an inventory observation.)

---

## §5 — Residual items (substrate-inventory level; post-073)

The following classical-result substrate elements remain
**NOT-VERBATIM-EXTRACTED** at the SIARC-stratum d ≥ 3
sectorial-upgrade-question level, after the present 073 session:

1. **Wasow 1965 Chapter X §3 Theorem 11.1** — (carried over from 072
   v1 §5 item 1; status unchanged in 073.) The Wasow PDF is on-disk
   at slot 04; verbatim Theorem 11.1 statement is not yet captured
   into a session deliverable.

2. **Loday-Richaud 2016 Chapter 2 multisummability synthesis** —
   (carried over from 072 v1 §5 item 2; status unchanged in 073.)
   Acquisition status: OPEN. Whether Loday-Richaud 2016 is needed at
   the SIARC-stratum sectorial-upgrade level is gated on
   OQ-W21-LITERATURE-ALTERNATIVE per 069r1 substrate. (No Phase 3
   answer yet.)

3. **Jimbo-Miwa 1981** (Painlevé monodromy / isomonodromic
   deformations) and **Conte-Musette 2008** (*The Painlevé
   Handbook*) — relevant to the Painlevé-side resurgence companion
   thread; acquisition status: OPEN. Out-of-073-scope; recorded as
   carry-forward.

4. **Forrester-Witte 2002 / 2005** family of papers (cf. 031
   FORRESTER-WITTE-2005 acquisition by SHA `efdc1c…`) — the
   acquired 031-substitute paper is on-disk; verbatim §-level extract
   for the F-W BT-citation region DEFER.

5. **A verbatim BT 1933 §§7-9 readthrough** parallel to the present
   073 session's §§4-6 readthrough. The BT 1933 paper is on-disk; a
   future relay session analogous to 073 would extract verbatim
   ≤ 30-word theorem-statements + claim tables for BT §7 Theorem II
   (Acta p. 51), §8 (proof completion), and §9 Fundamental Existence
   Theorem (Acta p. 69).

6. **A verbatim BT 1933 §§1-3 setup readthrough** to ground the
   24 earlier-section dependencies (cf.
   `bt_1933_sections_4_6_internal_xref.md` "Earlier-section
   dependencies" table) in verbatim Defs. 1, 3, 4, 5, 6, 8, 9 + Lemmas
   4-7.

7. **D2-NOTE v2.1 §§1-3 + §5-6** verbatim cross-walk against the
   §§4-6 readthrough (this session's `d2_note_v21_bt_citation_audit.md`
   covers v2.1 §4.5 only; v2.1's earlier §§1-3 + later §§5-6 framing
   is OUT-OF-SCOPE for 073).

8. The five carry-over items from 072 v1 §5 (Carmichael 1912;
   Galbrun 1913; Nörlund 1924; Perron 1917; pre-Adams literature)
   remain unchanged from 072 v1.

(Sentence count: 8. Within the E.5 ≤ 25-sentence cap. Anchoring rate:
8 / 8 = 100% — every sentence traces to a substrate-inventory carry-
forward fact or a verbatim §-level reference.)

---

## §6 — Gating-on-069r1 reminder

Items in §5 above (notably (2) Loday-Richaud 2016) are gated on
**OQ-W21-LITERATURE-ALTERNATIVE** — the open question recorded in the
069r1 substrate. The 073 session does not, and is not authorised by
the relay prompt to, supply a Phase 3 answer to OQ-W21-LITERATURE-
ALTERNATIVE; per HALT_073_LADDER_OVERREACH and the relay-prompt
PROHIBITED-CLAIMS clause forbidding "069r1 R1-closure assertion", any
inference from §§4-6 substrate to 069r1 closure is OUT-OF-SCOPE for
073. The §§4-6 verbatim layer is a substrate-inventory contribution
to the W21 LANE-1 Phase 3 arbitration substrate; the actual Phase 3
arbitration is conducted by the synthesizer-tier reader.

---

## Self-check status (Phase G)

- §4 token scan: the strings "closes", "closes the gap", "proves the
  gap", "establishes the upgrade", "narrows the gap", "demonstrates
  closure", "shows closure" do **not** appear in §4 outside
  policy-exempt contexts (the HALT-name reference in
  `HALT_073_LADDER_OVERREACH` is a halt-name reference, not a
  gap-closure assertion). See `forbidden_verb_scan.md` §C / §D for
  the consolidated 073 forbidden-verb scan.
- §4 sentence count: 8 (≤ 25). §5 sentence count: 8 (≤ 25). §6
  sentence count: 3 (≤ 25). Anchoring rate: 100% by inspection.
- The 072 v1 § structure (§1, §2, §3, §4, §5) is preserved; this v2
  adds §6 (069r1-gating reminder) which is new in 073 to satisfy the
  relay-prompt FORBIDDEN-CLAIM clause about 069r1.
