# Picture-Chain v1.20+ Zenodo Deposit Propagation Rule (slot 167; verdict-166-V4 absorption)

**Authority**: slot 166 synth verdict V4
**Trigger**: independent Zenodo deposit fire for picture-chain v1.20+ (separate work-stream from this slot 167 umbrella v2.2 deposit-prep)
**Picture-chain v1.20+ substrate**: bridge SHA `b9aa881` (slot 136 PICTURE-V120-M9-V0-AMENDMENT-PREP)
**Picture-chain Zenodo status**: NO PRIOR DEPOSIT (verified 2026-05-11 via Zenodo API `creators.name:"papanokechi"`; 18 records returned, picture-chain absent)

---

## Rule set for picture-chain v1.20+ Zenodo deposit (when fired)

### R1 — Reciprocal paired-row requirement

Picture-chain v1.20+ Related-identifiers MUST include the reciprocal paired pattern citing umbrella:

| Relation         | Identifier                                  | Resource type | Description                          |
|------------------|---------------------------------------------|---------------|--------------------------------------|
| `IsSupplementTo` | `10.5281/zenodo.19885549` (Umbrella concept) | Publication   | SIARC umbrella program statement     |
| `Cites`          | `10.5281/zenodo.19885549` (Umbrella concept) | Publication   | SIARC umbrella program statement paired |

### R2 — Additional program-tier companions (if in scope)

If picture-chain v1.20+ is in scope for additional program-tier companion citations per its own substrate-prep at slot 136 (`b9aa881`), apply slot 160 schema v1 §Layer 1 paired-row discipline to each. Default candidate set (from slot 162 program-tier interpretation):

- PCF-1 concept `10.5281/zenodo.19931635` — paired IsSupplementTo + Cites
- PCF-2 concept `10.5281/zenodo.19936297` — paired IsSupplementTo + Cites
- Channel Theory concept `10.5281/zenodo.19941678` — paired IsSupplementTo + Cites
- T2B concept `10.5281/zenodo.19783311` — paired IsSupplementTo + Cites

Decision on inclusion of R2 candidates: operator-tier at picture-chain deposit fire time, informed by slot 136 substrate-prep prose (`picture_revised_20260507.md` §6 Q-RELAY block + any picture-specific companion-paper declarations).

### R3 — Concept-DOI discipline (mandatory)

Picture-chain v1.20+ MUST NOT cite umbrella v2.2 version-DOI. The cross-link is concept-tier per slot 160 schema v1; this rule is unchanged from the umbrella → picture direction. The IsNewVersionOf exception does not apply here (picture-chain v1.20+ does not have a prior Zenodo version; this is its first deposit).

### R4 — Post-publish Edit on umbrella v2.2 (coupled)

After picture-chain v1.20+ deposit is published and its concept-DOI is minted:

1. Open the published umbrella v2.2 Zenodo record (whose version-DOI will be assigned by Phase B step 14 of `operator_runbook.md`).
2. Edit metadata → append 2 paired rows:
   - `IsSupplementTo` → `<picture-chain v1.20+ concept-DOI>` (Publication) — Companion picture-chain v1.20+
   - `Cites` → `<picture-chain v1.20+ concept-DOI>` (Publication) — Companion picture-chain v1.20+ paired
3. Save. NO DOI bump (metadata-only Edit per D2-NOTE v2.1 precedent 2026-05-04).
4. Terminal umbrella v2.2 Related-identifier row count: **11**.

### R5 — Reciprocal-citation completeness audit

At terminal state (post both umbrella v2.2 deposit and picture-chain v1.20+ deposit + post-publish Edit):

- Umbrella v2.2 record contains 11 Related-identifier rows.
- Picture-chain v1.20+ record contains ≥2 paired rows citing umbrella concept-DOI (R1 minimum), and possibly more per R2 inclusion decisions.
- No version-DOI cross-links exist in either direction between umbrella and picture-chain (IsNewVersionOf exception applies only within each chain's own version history; umbrella v2.2 → v2.0 internal; picture-chain has no prior version yet).

---

## Pre-flight schema-ambiguity check (UF-167-1 dependency)

**Before firing the umbrella v2.2 post-publish Edit (R4), operator should resolve UF-167-1.**

The verdict-166-V4 rule set assumes interpretation (A) of slot 160 §Layer 1 anti-rule line 47-48 (qualifier "in PCF-2 v1.4" scope-limits to PCF-2 v1.4; umbrella may freely cite picture-chain as Layer 1 program-tier companion). If interpretation (B) is the canonical reading (the named axis-mediated siblings — CT, D2-NOTE, picture v1.19 — are always Layer 2, never Layer 1 regardless of deposit), then:

- R1 paired-row requirement on picture-chain v1.20+ side STILL HOLDS (picture-chain → umbrella is unambiguous since umbrella is an anchor deposit; picture-chain is the supplementing record; supplementing → anchor relation is the most well-defined direction).
- R4 post-publish Edit on umbrella side is INVALID (umbrella v2.2 cannot cite picture-chain via Layer 1; relation lives in Layer 2 description body, not in Related-identifiers).
- Terminal umbrella v2.2 row count: stays at **9**, not 11.

**Recommended resolution**: fire a slot 168 (or later) T1-Synth schema-clarification consultation explicitly asking whether the slot 160 §Layer 1 "in PCF-2 v1.4" qualifier scope-limits or example-provides. The consultation can be lightweight (~5 KB) since both interpretations are already documented; synth just needs to pick one.

**Default if operator elects not to fire the clarification**: stay with verdict-166 interpretation (A) and apply R4 as specified. The semantic ambiguity is documented at UF-167-1 for future audit.

---

## Picture-chain v1.20+ deposit-prep work-stream pointers

- **Substrate**: `siarc-relay-bridge/sessions/2026-05-09/T2-EXECUTOR-PICTURE-V120-M9-V0-AMENDMENT-PREP-136/picture_revised_20260507.md` (3893 lines)
- **Placeholder-DOI marker**: `siarc-relay-bridge/sessions/2026-05-09/T2-EXECUTOR-PICTURE-V120-M9-V0-AMENDMENT-PREP-136/submission_log_v120plus_splice.diff` line 26 (`10.5281/zenodo.<picture-chain concept DOI>`)
- **Sub-DOI dependencies**: picture-chain v1.20+ deposit will REQUIRE its own paste-source preparation analogous to slot 162 → slot 167 for umbrella. Recommended next slot for this work-stream: slot 168 (paste-source prep) → slot 169 (operator-side Zenodo deposit fire).
- **Operator estimate of timing**: per cascade-132 Option α Step 3; no hard deadline; coupled with R4 umbrella post-publish Edit.

---

**End of `picture_chain_v120plus_propagation.md` (slot 167 verdict-166-V4 absorption).**
