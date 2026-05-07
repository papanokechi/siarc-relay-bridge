# [M4-CLAIM-CHAIN] — Relay 074 Phase C ledger

**Task ID:** `T2-M4-RATIFICATION-DOSSIER-ASSEMBLY-074`
**Authoring tier:** T2 substrate-inventory dossier (no new claims)
**Bridge HEAD at session start:** `3410e5d`
**Companion files:** `m4_substrate_inventory.md`,
`m4_substrate_anchor_shas.md`

This file is a directed-graph-style ledger from 068's verdict claim
back to its substrate. Each link is a single inference step with the
form

    [CLAIM-Mn] = [SUBSTRATE-X] under [INFERENCE-RULE-Y]

074 does NOT introduce inference rules. Every `[INFERENCE-RULE-Y]`
label is the inference rule already invoked by 068 / 072 / 073 /
D2-NOTE v2.1 / M4 spec at the named substrate anchor. 074's role is
to assemble the chain, not to re-derive any link.

---

## C.1 Top claim

`[CLAIM-M0]` (the 068 verdict's top-level closure-path claim).

Substrate anchor: 068 handoff `[S1.handoff]` SHA `6CAACB57622DB185…`,
section "What was accomplished" L31-36 (the verbatim 068 §Verdict
paragraph quoted verbatim in `m4_substrate_inventory.md` §B.1.1).

Top-claim verbatim text (≤ 50 words; quote 1 of 1 permitted in this
file for the over-claiming-verb-bearing 068 verdict):

> Verdict: `UPGRADE_FULL_VIA_DEG_A_ZERO_ROW` at MEDIUM-HIGH confidence
> (HIGH reserved for post-W21-LANE-1-T1-Synth-ratification +
> post-Wasow-§X.3-OCR-acquisition state). G11 H1 disposition updated
> from PHASE_2_GATED to PROVEN at general d ≥ 3 (subject to W21
> ratification). M9 SIARC-MASTER-V0 announcement gating reduces from
> {M4, M6.CC} to {M6.CC} only.

(41 words; 068 verbatim.)

`[CLAIM-M0]` decomposes into sub-claims `[CLAIM-M1]` through
`[CLAIM-M5]` below.

---

## C.2 Sub-claim decomposition (C.2.1 - C.2.5)

### C.2.1 [CLAIM-M1] — deg_a = 0 row identification is well-defined

`[CLAIM-M1]` = "the SIARC stratum's operative row in 064 §2.3
four-row Phase A WZ-balance enumeration is the deg_a = 0 row."

Substrate: 068 phase_a_substrate_readback.md `[S1.phase_a]` (SHA
`FD437608E0074F45…`) Phase A.0 supersession gate Q.SUP = YES; cited
in 068 phase_e_verdict_selection.md `[S1.phase_e]` (SHA
`2A77C759B5E9C693…`) §E.2 row reading.

Inference rule (068-cited): "rubber-duck QA P10 supersession check"
(068 handoff §"Judgment calls made" item 1, L48-56; ≤ 50 words):

> When the rubber-duck-QA P10 supersession check fired Q.SUP = YES,
> the verdict ladder branched to UPGRADE_FULL_VIA_DEG_A_ZERO_ROW (the
> deg_a = 0 row enumeration-extension path) rather than
> UPGRADE_FULL_VIA_BORDERLINE_ANSATZ.

(40 words.)

Cross-substrate corroboration: 065 cf_value audit `[S1.subshas
§1.2]` (SHA `16512BCC71C9A19E…`) shows the SIARC stratum at deg_a = 0
in 13 of 13 PCF-2 implementations; 066 V_quad row reframing
`[S1.subshas §1.2]` (SHA `79933B694DD2BF99…`) places the V_quad d=2
anchor at the same row.

Link is FULLY substrated by 068 / 064 / 065 / 066 substrate as
recorded in 068 §1.2. No 074-introduced inference.

### C.2.2 [CLAIM-M2] — upgrade preserves M4 spec invariants

`[CLAIM-M2]` = "the deg_a = 0 row upgrade respects all M4 spec
invariants (over-claim 5-item rubber-duck checklist + d=2 V_quad
sanity + d=3 / d=4 empirical bands)."

Substrate: 068 phase_d_a2d_derivation.md `[S1.phase_d]` (SHA
`34C3E30F884B960F…`) §D.6 5-item HALT_068_OVER_CLAIM checklist (5/5
satisfied) + Phase B §B.5 d=2 V_quad sanity + Phase D §D.5 d=3 / d=4
cross-check.

Inference rule (068-cited): "5-item HALT_068_OVER_CLAIM rubber-duck
checklist" (068 handoff §"What was accomplished" L23-25; ≤ 50 words):

> The 5-item HALT_068_OVER_CLAIM rubber-duck checklist was fully
> satisfied (5/5).

(13 words.)

Cross-substrate corroboration: PCF-2 v1.2 release Sessions B + C1 +
Q1 empirical claims `[S1.subshas §1.4]`; G24 readback verdict
`UPGRADE_G24_DEFINITIONS_MATCH_PHASE2_ANOMALY_REAL` (068 §1.4 cited
verbatim). All cited as substrate-anchored prior verdict
inheritance.

Link is FULLY substrated by 068 §B.5 + §D.5 + §D.6. No 074-introduced
inference.

### C.2.3 [CLAIM-M3] — Adams §§1-2 are the pre-Wasow substrate base

`[CLAIM-M3]` = "Adams 1928 §§1-2 supply the pre-Wasow asymptotic-
expansion substrate base for the Birkhoff / Newton-polygon /
canonical-form lineage that 068's deg_a = 0 row upgrade relies on
(via the V6 + 064 four-row enumeration's Stirling-Birkhoff form
assumption, normal case p = 1)."

Substrate: 072 deliverables `[S2.section_1]` (SHA `742D2EF380BF7462…`)
+ `[S2.section_2]` (SHA `1C7A6DAF0D54BF6A…`) + `[S2.theorems]` (SHA
`7D0FE053F517B0F8…`) + `[S2.ladder_v1]` (SHA `60AE4328517B13EF…`).
Adams 1928 PDF anchor `[S5.adams_pdf]` (SHA `d7ac4017a9737fef…`).

Inference rule (072-cited): "T1-T9 indexing covers unlabelled results"
(072 handoff §"Judgment calls made" item 2, ≤ 50 words):

> Adams 1928 contains only 2 explicitly labelled theorems (Theorem A,
> Theorem B). The other 7 headlining results are stated narratively
> without `Theorem X` / `Proposition X` / `Lemma X` labels. … An
> internal T1-T9 index was constructed.

(38 words.)

Link is FULLY substrated by 072 deliverables. No 074-introduced
inference. The "Adams §§1-2 supply the pre-Wasow substrate base"
framing is a substrate-inventory label not an analytic content
claim; the analytic content sits with 068 phase_b / phase_c /
phase_d.

### C.2.4 [CLAIM-M4] — BT 1933 §§4-6 strengthen Adams §§1-2

`[CLAIM-M4]` = "BT 1933 §§4-6 strengthen Adams §§1-2 with explicit
indicial-equation + period-functions treatment at §-level granularity
sufficient for 068's verdict-chain corroboration of the V6 closed-form
formula's normal-case (p = 1, q = 1) regime assumption."

Substrate: 073 deliverables `[S3.section_4]` (SHA `B3ABEDE24FF368D0…`)
+ `[S3.section_5]` (SHA `EC2C0D5A2DADEF3B…`) + `[S3.section_6]` (SHA
`744A197DEC758E0D…`) + `[S3.theorems]` (SHA `EDDFE12431A9B29F…`) +
`[S3.ladder_v2]` (SHA `DC3B048C39ACA27A…`). BT 1933 PDF anchor
`[S5.bt_pdf]` (SHA `DCD7E3C6B2A12AE1…`).

Inference rule (073-cited): "T6 PARALLEL → EXTENDED reclassification"
(073 handoff §"Judgment calls made" item 2, ≤ 50 words):

> 072 v1's PARALLEL label was based on the absence of a separately-
> titled "§ Periodic functions" header in BT 1933. The verbatim 073
> readthrough surfaces the same periodic-functions object inside the
> BT §5 Theorem I proof at p. 47 (13 a). Reclassified to EXTENDED.

(45 words.)

073-side resolution status (verbatim ≤ 50 words; 073 handoff §"Key
numerical findings" bullet 6):

> All 6 of 9 072 v1 DEFER markers RESOLVED at §-level BT granularity
> in `adams_bt_ladder_map_v2_with_bt_4_6.md`. **072 D4 RESOLVED** for
> §§4-6 content.

(26 words.)

Link is FULLY substrated by 073 deliverables. No 074-introduced
inference.

### C.2.5 [CLAIM-M5] — D2-NOTE v2.1 §4.5 substantiates rigour grounding

`[CLAIM-M5]` = "D2-NOTE v2.1 §4.5 substantiates the BT 1933 → ODE-side
rigour grounding via 3 EXACT page-anchor matches (p.30 Lemma 8 / p.41
Theorem I / p.48 Lemma 9)."

Substrate: 073 D2-NOTE audit `[S3.d2_audit]` (SHA `7CF2279AA15DF44F…`)
+ D2-NOTE v2.1 PDF `[S4.pdf]` (SHA `A8B6026A3453F901…`) + .tex source
`[S4.tex]` (SHA `840120E73534DA8E…`).

Inference rule (073-cited): substrate-inventory page-anchor audit
(073 handoff §"Key numerical findings" bullet 8 + bullet 9; ≤ 50
words):

> D2-NOTE v2.1 §4.5 BT-citation audit = 3/3 EXACT page-anchor matches
> (p.30 Lemma 8 / p.41 Theorem I / p.48 Lemma 9) + 3/3 form-of-equation
> /object substrate-inventory agreement.

(26 words.)

Link is FULLY substrated by 073 D2-NOTE audit. No 074-introduced
inference. Per 073's own self-framing, the audit is
SUBSTRATE-INVENTORY-ONLY, not a Borel-summability framing
endorsement (see 073 handoff §"Anomalies and open questions" bullet 3
for synthesizer-routed wording question; carried forward to
`m4_residual_questions.md` as Q-D3-1).

---

## C.3 Residual un-discharged links (substrate gap audit)

This section enumerates each link `[LINK-Cn]` in the chain that
068 / 072 / 073 do NOT fully substrate. Each entry is a question
the synthesizer is asked to weigh; 074 does not propose answers.

### C.3.1 [LINK-C1] — MEDIUM-HIGH-vs-HIGH gap

The 068 verdict carries MEDIUM-HIGH confidence. The reasoning for
the not-HIGH leg is anchored in 068 phase_e_verdict_selection.md
`[S1.phase_e]` L82-89 (≤ 50 words):

> the Wasow §X.3 Theorem 11.1 Newton-polygon factorization theorem
> (the canonical text-book reference for the Newton-polygon →
> Birkhoff-form connection in difference-equation setting) remains
> OCR-deferred; T1-A01 paraphrase-grade access carries the connection
> at the operative level.

(38 words.)

Open: the residual question gating MEDIUM-HIGH → HIGH per 068's own
framing is **{W21 LANE-1 T1-Synth ratification + Wasow §X.3 OCR
acquisition}**. W21 LANE-1 ratification is the cadence event this
074 dossier is being assembled for; Wasow OCR acquisition is
forward-pointed (068 handoff §"Recommended next step" item b).
Whether MEDIUM-HIGH at the time of W21 LANE-1 ratification is
sufficient for synthesizer's purposes is part of the synthesizer's
arbitration scope.

Carried forward as `Q-D4-1` in `m4_residual_questions.md`.

### C.3.2 [LINK-C2] — 068 PARTIAL / DEFERRED caveats

068 contains 0 halts triggered (S1.halt SHA `75CEFE9588813121…`)
and 4 non-blocking discrepancies D1-D4 (S1.discrep SHA
`88107B5466208220…`) and 4 unexpected finds U1-U4 (S1.unexpected
SHA `E28AB52D27B42B84…`). None of these are PARTIAL or DEFERRED at
verdict-statement scope.

Specifically, the 068 verdict ladder selection §E.1 considered and
honestly REJECTED the partial branches `UPGRADE_PARTIAL_NUMERICAL_
STRUCTURAL` / `UPGRADE_PARTIAL_NUMERICAL_EMPIRICAL` /
`UPGRADE_PARTIAL_FORMAL` / `UPGRADE_NONE` per 068 §E.1 ladder table.

Open: any inheritance from D1-D4 / U1-U4 that should be carried
into the W21 LANE-1 ratification scope is fully enumerated in
`m4_residual_questions.md` §D.1 (068 carry-forward).

### C.3.3 [LINK-C3] — V_quad d=2 anchor row alignment

The V_quad d=2 anchor (PCF-1 v1.3 §6 Theorem 5; H4_EXECUTED_PASS at
108 digits per Prompt 005 anchor) sits at the deg_a = 0 row per 066
row reframing (`[S1.subshas §1.2]` SHA `79933B694DD2BF99…`). The
066 row reframing was 074's predecessor session 067's antecedent
substrate (LANE-2 Item 1 R1 PCF-1 leg implementation). Per LANE-2
Item 3 ruling `LEAVE_V1_0_CANONICAL`, no v1.0 .tex / PDF amendment
was made by 066 / 067; PCF-1 v1.3 source `[S1.subshas §1.2]` SHA
`E83BB377F297DBF0…` is unmodified.

Open: whether the synthesizer wishes to carry the 066 row-reframing
forward into a PCF-1 v1.4 amendment cycle (G12 jurisdiction;
forward-pointed at 066 handoff item U3) is a follow-up scope
question not blocking M4 ratification. Carried forward as
`Q-D4-2`.

---

## C.4 Chain integrity self-check

Top-claim `[CLAIM-M0]` decomposes into 5 sub-claims `[CLAIM-M1]` ...
`[CLAIM-M5]`. Each sub-claim cites:

- a primary substrate anchor `[SUBSTRATE-Sn]` with SHA-256 in
  `m4_substrate_anchor_shas.md`,
- an inference rule label that reproduces the inference-rule label
  used by the source session itself,
- and (where the source session provides one) a verbatim ≤ 50-word
  quote of the inference-rule statement.

3 residual links `[LINK-C1]` ... `[LINK-C3]` are surfaced as
synthesizer-routed open questions, NOT as 074-introduced
counter-claims.

Per §6: 074 introduces no theorems, lemmas, or bibliographic
citations of its own. The 074 dossier presents the chain
substrate-side without re-deriving any 068 / 072 / 073 / D2-NOTE
v2.1 result.

---

*End of `m4_claim_chain.md`. The 5 sub-claims trace back to 8
substrate anchors enumerated in `m4_substrate_inventory.md`. The 3
residual links are forwarded to `m4_residual_questions.md` for
synthesizer arbitration.*
