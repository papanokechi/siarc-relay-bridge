# [M4-SUBSTRATE-INVENTORY] — Relay 074

**Task ID:** `T2-M4-RATIFICATION-DOSSIER-ASSEMBLY-074`
**Authoring tier:** T2 substrate-inventory dossier (no new claims)
**Bridge HEAD at session start:** `3410e5d`
**Companion file:** `m4_substrate_anchor_shas.md` (SHA backbone)

This file is a substrate-inventory artefact for W21 LANE-1 Phase 3
M4 closure-path arbitration consumption. It introduces no claims of
its own. Each entry is either:

- a verbatim ≤ 50-word quote from `[SUBSTRATE-Sn]` with file + line/page
  anchor + SHA backbone in `m4_substrate_anchor_shas.md`, OR
- a structural label `[SUBSTRATE-Sn]`, OR
- a meta-policy declaration about scope / non-scope.

---

## B.1 PRIMARY SUBSTRATE (5 sources)

### B.1.1 [SUBSTRATE-S1] — 068 verdict text (verbatim)

Source: 068 handoff `[S1.handoff]` (SHA `6CAACB57622DB185…`),
section "What was accomplished" paragraph 4 (L31-36).

Verbatim quote (≤ 50 words):

> Verdict: `UPGRADE_FULL_VIA_DEG_A_ZERO_ROW` at MEDIUM-HIGH confidence
> (HIGH reserved for post-W21-LANE-1-T1-Synth-ratification +
> post-Wasow-§X.3-OCR-acquisition state). G11 H1 disposition updated
> from PHASE_2_GATED to PROVEN at general d ≥ 3 (subject to W21
> ratification). M9 SIARC-MASTER-V0 announcement gating reduces from
> {M4, M6.CC} to {M6.CC} only.

(Word count: 41 words; under the 50-word ceiling. The forbidden-verb
token "PROVEN" is permitted in this entry per §5.E.2's verbatim-quote
exemption — this paragraph is the canonical 068 verdict text.)

For the analytic content of the verdict (i.e., the closure-path
mechanism and the V6 closed-form general formula), the synthesizer
is invited to read 068 `phase_e_verdict_selection.md` `[S1.phase_e]`
(SHA `2A77C759B5E9C693…`) directly via the bridge URL; 074 does not
re-quote the phase_e verdict statement here in order to keep the
B.1.1 entry strictly aligned with the §1.B.1 prompt scope ("verbatim
quote ≤ 100 words from handoff §Verdict").

### B.1.2 [SUBSTRATE-S2] — 072 CLEAN_EXTRACT verdict + claim count

Source: 072 handoff `[S2.handoff]` (SHA `3DF3671FEAEFA154…`),
section "AEAL claim count" final paragraph + section "Status" L4.

Verbatim quote (≤ 50 words):

> Status: COMPLETE. Verdict: CLEAN_EXTRACT.

> 10 entries written to claims.jsonl this session (C1-C10 per relay
> prompt schema; C9 + C10 conditional entries included because the
> Phase D.2 anchoring spot-check and the Phase E final-pass scan both
> produced quantifiable claim-worthy counts).

(Word count: ≈ 41 words combined. Both excerpts are status-marker
recital from the 072 handoff itself.)

### B.1.3 [SUBSTRATE-S3] — 073 CLEAN_EXTRACT verdict + claim count

Source: 073 handoff `[S3.handoff]` (SHA `0BE9AF3A06A83DC6…`),
section "Status" L4 + section "AEAL claim count" final paragraph.

Verbatim quote (≤ 50 words):

> Status: COMPLETE. Verdict: CLEAN_EXTRACT.

> 12 entries written to claims.jsonl this session (C1-C12); see the
> full enumeration in claims.jsonl.

(Word count: ≈ 21 words combined.)

### B.1.4 [SUBSTRATE-S4] — D2-NOTE v2.1 §4.5 (BT-citation block)

Source: D2-NOTE v2.1 PDF `[S4.pdf]` (SHA `A8B6026A3453F901…`),
verified bit-for-bit in 073 audit `[S3.d2_audit]` (SHA
`7CF2279AA15DF44F…`).

Verbatim 073-side audit verdict (≤ 50 words; 073 handoff §"Key
numerical findings" bullet 8):

> D2-NOTE v2.1 §4.5 BT-citation audit = 3/3 EXACT page-anchor matches
> (p.30 Lemma 8 / p.41 Theorem I / p.48 Lemma 9) + 3/3 form-of-equation
> /object substrate-inventory agreement.

(Word count: 26 words. This is 073's audit-verdict statement, NOT
074's claim. The audit itself is `[S3.d2_audit]` substrate.)

Per §6: D2-NOTE v2.1 is Zenodo-immutable (concept DOI
`10.5281/zenodo.20015923`); 074 does not amend, re-extract, or
reinterpret v2.1 content beyond citing the 073 audit's page-anchor
result tags.

### B.1.5 [SUBSTRATE-S5] — Adams 1928 §§1-2 (072 deliverables)

Source: 072 deliverables enumerated in `m4_substrate_anchor_shas.md`
§1.2 as `S2.section_1` / `S2.section_2` / `S2.claim_table` /
`S2.theorems` / `S2.bibliography` / `S2.section_index`. The Adams
1928 PDF anchor is `S5.adams_pdf` (SHA
`d7ac4017a9737fef00e10257f26b9a6a6f6cc23437d2654440359f2e24836e18`).

Verbatim 072-side substrate-summary statement (≤ 50 words; 072
handoff §"Key numerical findings" bullet 4 + bullet 5):

> Section count: 8 numbered sections (§1-§8) + 1 closing extension
> clause at printed p541. … Explicitly labelled theorems: 2
> (Theorem A at PDF p24 / printed p529 §6; Theorem B at PDF p32 /
> printed p537 §6). Total indexed results T1-T9: 9.

(Word count: 41 words.)

---

## B.2 SECONDARY SUBSTRATE (3 sources)

### B.2.1 [SUBSTRATE-S6] — 073 ladder-map v2 (resolves 072 D4)

Source: `[S3.ladder_v2]` (SHA `DC3B048C39ACA27A…`).

Verbatim 073-side resolution statement (≤ 50 words; 073 handoff
§"Key numerical findings" bullet 6):

> All 6 of 9 072 v1 DEFER markers RESOLVED at §-level BT granularity
> in `adams_bt_ladder_map_v2_with_bt_4_6.md`. **072 D4 RESOLVED** for
> §§4-6 content.

(Word count: 26 words.)

Verbatim 073-side ladder-distribution statement (≤ 50 words; same
handoff bullet 5):

> Adams T1-T9 ↔ BT §§4-6 ladder distribution v2 (post-073) = 1
> ABSORBED-VERBATIM, **6 EXTENDED**, 1 SUPERSEDED, 1 PARALLEL (T6
> promoted PARALLEL→EXTENDED on the strength of BT §5 (13 a)
> [CHART-MAP-CANDIDATE-B1] substrate; only label change vs 072 v1).

(Word count: 36 words.)

### B.2.2 [SUBSTRATE-S7] — 073 sectorial-upgrade gap status v2

Source: `[S3.gap_status_v2]` (SHA `D6BC0B7F72F27A9A…`).

Per 073 handoff §"What was accomplished" item (f) substrate-summary
statement (≤ 50 words verbatim):

> extended sectorial-upgrade-gap status report v2

This artefact is substrate-inventory-only per its own framing; it
does not assert closure of the gap. The 074 dossier consumes it as
substrate inventory (no closure inheritance).

### B.2.3 [SUBSTRATE-S8] — 073 D2-NOTE v2.1 §4.5 BT-citation audit

Source: `[S3.d2_audit]` (SHA `7CF2279AA15DF44F…`).

Cross-referenced with B.1.4 above. The audit is the operative D2-NOTE
v2.1 ↔ BT 1933 §§4-6 page-anchor verification. Per its own framing
(quoted in B.1.4) the result is 3/3 EXACT. 074 carries no
re-interpretation.

---

## B.3 SUBSTRATE NOT-INCLUDED (explicit non-inventory)

The following substrate is intentionally OUT-OF-SCOPE for the M4
ratification dossier. Each entry is paired with a one-sentence
why-not.

### B.3.1 069 / 069r1 outputs (M6.CC scope, not M4)

`sessions/2026-05-06/M6_CC_PHASE_D_NUMERICAL_FOLLOWUP-069/` and
`sessions/2026-05-07/M6-CC-R1-CLOSURE-PREFLIGHT-069R1/` are M6.CC
canonical-form-leg deposits; the M9 gating clause at picture v1.19
L69 explicitly distinguishes M6.CC from M4. M6.CC substrate is
out-of-scope for an M4 ratification dossier per §6 + envelope halt
`HALT_074_M6_SCOPE_CREEP`. (Cross-reference only — see D.3.U1.)

### B.3.2 T2B v3.0 outputs (separate stratum result)

T2B v3.0 (`sessions/2026-05-05/...` and 044R / 044B sweep deposits)
is the off-orbit n/log(2) two-data-point result for the b1 ∈ {7, 10}
anchors; it is a Trans-stratum / sign-orbit result, not a P-B4
sectorial-upgrade result, and lives in PCF-2 v3.x scope rather than
PCF-2 v1.3 §B / picture v1.19 §5 G11 / G24 scope.

### B.3.3 PCF-2 v1.3 deg_a-zero-row results (Trans stratum, not M4)

The PCF-2 v1.3 R1.1 / R1.3 / Q1 empirical anchors at d=3 / d=4 ARE
M4 substrate (used in 068 §B.5 + §D + §E.2 verbatim) and are
in-scope. What is OUT-of-scope is any newer-than-068 PCF-2 v1.3
follow-on Trans-stratum sweep result that does not feed back into
the deg_a = 0 row of 064 §2.3. No such follow-on is consumed.

### B.3.4 067 follow-up note v1.0 (non-canonical extension)

`sessions/2026-05-07/BT-BASELINE-NOTE-FOLLOWUP-V1-0-067/` is the
LANE-2 Item 3 follow-up note; it is an additive extension of the
v1.0 baseline note (Zenodo concept DOI 10.5281/zenodo.20048196) and
is forward-pointed for synthesizer review at G12 jurisdiction (per
067 handoff). 074 cites 067 in `m4_substrate_anchor_shas.md` §1.2
S1's antecedent chain only; the follow-up note is NOT primary or
secondary M4 substrate for ratification — it is upstream context.

### B.3.5 PCF-1 v1.3 source / `bt_baseline_note` v1.0 source

These are read-only canonical artefacts per LANE-2 Item 3
`LEAVE_V1_0_CANONICAL` ruling (recorded in 066 handoff). Their SHAs
are anchored in 068 §1.2 (S1.subshas references `6746692C517DC252…`
for `bt_baseline_note v1.0 .tex` and `E83BB377F297DBF0…` for
`p12_pcf1_main.tex` PCF-1 v1.3 source). 074 does not modify them and
does not consume them as new substrate; they are upstream context
for the verdict chain only.

---

## B.4 Inventory completeness self-check

This file inventories: 5 primary substrate sources (S1-S5) + 3
secondary substrate sources (S6-S8) = 8 substrate-inventory entries
matching §2 spec for "5 primary + 3 secondary" exactly.

The B.3 non-inventory section enumerates 5 explicit out-of-scope
items; each is paired with a one-sentence why-not. No item that the
synthesizer might reasonably expect to be in-scope is omitted
without an explicit B.3.x non-inventory entry.

---

*End of `m4_substrate_inventory.md`. No claims introduced; this is a
substrate-inventory artefact only. See `m4_claim_chain.md` for the
claim-chain ledger from 068 verdict back to substrate.*
