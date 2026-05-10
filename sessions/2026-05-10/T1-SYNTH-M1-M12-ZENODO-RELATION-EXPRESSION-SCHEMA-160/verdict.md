# Slot 160 — T1-Synth Verdict (verbatim)

**Task:** T1-SYNTH-M1-M12-ZENODO-RELATION-EXPRESSION-SCHEMA-160
**Class:** T1-Synth single-witness consultation
**Witness:** claude-opus-4-7-anthropic (claude.ai web; receipt 2026-05-10 ~20:42 JST)
**Band ceiling honoured:** MEDIUM-HIGH
**RULE 1:** clean (consultation; no Zenodo deposit)

**Predecessor verdicts:**
- Slot 157 framing-consultation (`34563a6`)
- Slot 159 canonical outlook source-of-record (`961b828`)

**Successor consumers (anticipated):**
- F6 Umbrella v2.3 substrate-prep (next math-axis fire)
- Slot 137 `zenodo_v14_description_block.md` amendment-overlay (operator-side, small scope)

---

## Verdict packet (verbatim from synth)

```
LABEL:    SCHEMA_LOCK_INLINE
BAND:     MEDIUM-HIGH
WITNESS:  claude-opus-4-7-anthropic-2026-05-10
```

Phase 0 gates: STEP 0.1 supersession PASS (no prior LANDED M1-M12 Zenodo metadata schema fire; slot 157 scope was deposit-cascade not metadata) | STEP 0.2 SHAs 12/12 trust-on-prompt (synth lacks shell; agent-side rev-parse already attested in §2) | STEP 0.3 DOIs 5/5 trust-on-prompt (synth lacks resolver; live-resolve gate deferred to deposit time per slot 116 J2 sidebar precedent) | STEP 0.4 ceiling MEDIUM-HIGH honoured | STEP 0.5 schema below.

---

### Q1_RESPONSE

**Q1a.** The 4-row set is **sufficient at the paper-tier for PCF-2 v1.4**. Adding more `IsSupplementTo`/`Cites` rows for Channel Theory (`19941678`), D2-NOTE (`19996689`), and the picture v1.19 deposit would over-couple PCF-2 v1.4 to deposits whose relation is *axis-mediated*, not paper-mediated. PCF-2 v1.4's direct relations are: (i) it succeeds v1.3 (`IsNewVersionOf`), (ii) it is supplementary to PCF-1 (`IsSupplementTo` + `Cites`), and (iii) it is supplementary to Umbrella per Option α' (`IsSupplementTo`). Channel Theory and D2-NOTE are siblings in the program — they don't have a paper-tier supplementary relation to PCF-2 v1.4; they share *axis coverage*, which is a Layer-2 concern. **One amendment recommended:** add `Cites 10.5281/zenodo.19885550 Umbrella concept` alongside the new `IsSupplementTo` row, mirroring the PCF-1 pattern (both `IsSupplementTo` and `Cites` for the same target). This is symmetric with row 2/3 and lossless.

Final Q1a row set for PCF-2 v1.4:
```
IsNewVersionOf  10.5281/zenodo.19963298    PCF-2 v1.3
IsSupplementTo  10.5281/zenodo.19931635    PCF-1 concept
Cites           10.5281/zenodo.19931635    PCF-1 concept
IsSupplementTo  10.5281/zenodo.19885550    Umbrella concept
Cites           10.5281/zenodo.19885550    Umbrella concept
```

**Q1b.** **Description-body only, not Related-identifier rows.** GitHub commit URLs are unsuitable as `References` targets in DataCite metadata for two reasons: (1) **archival mismatch** — DataCite `References` is intended for persistent-identifier targets (DOI, Handle, URN, arXiv ID), not VCS URLs which lack guaranteed persistence; (2) **rebase/rename risk** — a `siarc-relay-bridge` repo rename or history rewrite silently breaks every cascade reference in every deposit's metadata. Putting cascade SHA references in the **Description body as prose** (e.g., "M7 V0 closure: bridge cascade `7f93b9e`") is the right discipline: the SHA is the persistent identifier (git's content-addressing makes the SHA itself stable even under rebase, as long as the commit object is reachable), the URL is decoration, and prose-tier references don't pollute the machine-parseable graph. If the repo is later mirrored to Software Heritage (SWHID), *that* would be the right `References` target — but that's a Layer-3 concern and out of scope for slot 160.

**Q1c.** Concept-DOI discipline is **correctly applied** in the proposed row set: rows 2-5 all target concept-DOIs (`19931635`, `19885550`). Row 1 (`IsNewVersionOf 19963298`) correctly targets a **version-DOI** — this is the one row where version-DOI is not just permitted but *required*, because `IsNewVersionOf` is by definition a version-to-version relation (concept-DOI on either side would be semantically wrong: a concept doesn't have a "new version of" a different concept). The general rule "cross-link `IsSupplementTo` should target concept-DOI" is preserved; `IsNewVersionOf` is the documented exception. No anomalies.

---

### Q2_RESPONSE

**Q2a.** **Yes, standardize the table — but only for "anchor" deposits, not every deposit.** Anchor deposits are the long-lived program-tier homes: PCF-2 (`19936297`), Umbrella (`19885550`), Channel Theory (`19941678`), D2-NOTE (`19996689`). PCF-1 (`19931635`) is a foundational anchor and should also carry the table on its next version increment. Single-purpose deposits (e.g., a future M1-only update or a one-shot picture-chain consolidated deposit) need only cite the canonical outlook by reference. Rationale: redundancy of the table across 5 anchors is governance-positive (any one is forensically self-sufficient); redundancy across every deposit is overhead. Layer 1 alone is insufficient for axis-tier semantics because DataCite has no native vocabulary for "this paper covers program-axis Mx at status Sy" — Layer 1 is paper-to-paper, not paper-to-axis.

**Q2b.** **Lock the proposed 7-status set with two amendments:**

1. Rename `covered (V0-closed; primary)` → `closed (V0; primary)` and `covered (V0-closed; folded)` → `closed (V0; folded)`. Rationale: "covered" is redundant with the table's purpose (it *is* a coverage table); leading with closure-tier is more scannable. Future V1/V2 closure tiers slot in cleanly: `closed (V1; primary)`.
2. Add `closed (retired into Mx)` as the canonical form, dropping `retired (into Mx)` as a separate status. Rationale: retirement is a *form* of closure (the axis has no further work because it folded into another), so it should be expressed as a closure subtype, not a parallel status. M3→M4 and M5→M6.CC fit this naturally.

Final controlled vocabulary (7 statuses):
```
closed (V0; primary)             -- this deposit is the canonical home
closed (V0; folded)              -- this deposit absorbs the closure; primary lives elsewhere
closed (retired into Mx)         -- axis was retired into Mx; cite Mx's primary
partial                           -- this deposit covers part; full closure pending
external                          -- axis lives elsewhere; cite that deposit
not in scope                      -- axis not addressed in this deposit
tabled (RULE 1)                   -- not yet opened
```

**Q2c.** **List M1-M12 atomically.** Grouping the 5 RULE-1-tabled axes saves ~4 rows but loses forensic granularity: when M2 opens (and only M2), the operator must split the row anyway, and pre-split tables in older deposits become inconsistent with post-split tables in newer ones. Atomic listing means the migration is a status flip on a single row, not a structural edit. The 12-row cost is negligible (~12 lines of markdown).

---

### Q3_RESPONSE

**Q3a.** **Defer to post-RULE-1-lift. Re-affirm D-157-7.** Slot 159's canonical outlook does not change the calculus: Community creation is a one-way commitment to a discoverability surface that becomes load-bearing once announced (deposits get filed under it, external citations may reference the Community URL, etc.). With 5 axes still RULE-1-tabled and the Option α' cascade not yet deposited, creating the Community now means front-loading the program identity before the program's V0 closure surface is observable. The asymmetry of cost — easy to create later, hard to deprecate gracefully — favors deferral. The exception would be if a near-term external citation needed a Community URL as an anchor; no such commitment is on the books per slot 159.

**Q3b.** **Per-deposit snapshot, not Community-level master.** The Community description is a poor home for an evolving status table because: (1) Zenodo Communities don't have a versioned description (edits are silent overwrites with no audit trail), (2) the canonical outlook (slot 159 `M1_M12_CLOSURE_OUTLOOK_20260510_POST_OPEN_ITEMS.md`) is already the source-of-record and should remain so, (3) per-deposit snapshots create a natural temporal record (each deposit's table reflects axis state *at deposit time*, which is forensically useful). Community description should carry a one-line pointer to the canonical outlook bridge URL and nothing more.

---

### Q4_RESPONSE

**Q4a.** **Status flip on tabled axes does NOT require a new version of older deposits.** Use option (iii) — leave existing deposits frozen; rely on newest-deposit table being the most-current snapshot, plus the canonical outlook (slot 159) as the authoritative source-of-record. Rationale: forcing a Zenodo "new version" every time M2 or M11 flips out of `tabled (RULE 1)` is governance-thrash with no scientific change to the underlying deposit content. Zenodo "edit description" (no version increment) is also wrong here because it silently rewrites the metadata of a published artifact — bad archival hygiene. The canonical outlook bridge fire is *already* the mechanism for axis-status updates; deposits should snapshot the outlook at deposit time and remain frozen thereafter. This makes the canonical outlook the single source of truth and deposits the historical record.

**Q4b.** Bridge cascade SHA references have **indefinite lifetime as content-addressed identifiers, but URL lifetime tied to GitHub repo identity.** Migration path:
- **If repo renamed**: SHAs remain valid; update operator runbook with new URL prefix; existing deposits' Description-body URLs decay but SHAs are independently recoverable from any clone or mirror. No deposit metadata edit required.
- **If repo deleted/lost**: SHAs valid only against surviving clones. **Mitigation**: when SIARC reaches a stable program milestone (e.g., post-RULE-1-lift V1 closure), submit `siarc-relay-bridge` to Software Heritage for SWHID assignment. SWHIDs are persistent and can be added to future deposits' `References` rows as a Layer-1 upgrade (this is the Layer-3-adjacent improvement noted in Q1b). Until then, treat SHA-in-prose as the operative reference and accept the residual repo-loss risk.

---

### Q5_RESPONSE  (slot 160 fire/no-fire BINARY)

**Q5a. NO-FIRE.** The agent's pre-consultation default is correct. Justification:

1. **Schema size**: the locked vocabulary (Q2b) is 7 statuses; the row pattern (Q1a) is 5 rows; the table template (Q2c) is 12 rows. Total artifact ~25-30 markdown lines. This is well below the threshold where a standalone fire produces governance value.
2. **Consumer count**: only two consumers in the visible horizon — F6 Umbrella v2.3 substrate-prep and PCF-2 v1.4 deposit description amendment. Both consumers are imminent; both will receive the schema as inline material. There is no "third consumer in 6 months" to amortize a fire over.
3. **Reusability gain**: a slot 160 fire would produce a citable bridge SHA for "the Zenodo metadata schema." The same citability is achieved by the F6 prompt referencing this verdict (slot 160 verdict packet is itself a bridge artifact, even without an associated fire-deliverable) plus the slot 137 substrate amendment. The marginal gain is minimal.
4. **Symmetry with slot 157**: slot 157 was a framing-consultation that produced a verdict but no fire-deliverable beyond the verdict itself; the verdict was absorbed into downstream prompts. Slot 160 is structurally identical (a synth consultation that resolves a governance question). The slot 157 precedent supports verdict-only resolution.

**Q5b.** N/A (NO-FIRE).

**Q5c.** **Option (i) + (ii) combined**, not (iii). Specifically:
- **(i)** F6 Umbrella v2.3 substrate-prep prompt body embeds the locked Q2b vocabulary and Q2c granularity rule, and produces an axis-coverage table for Umbrella v2.3 in its substrate-prep deliverable.
- **(ii)** Slot 137 `zenodo_v14_description_block.md` receives a one-paragraph operator-side amendment-overlay (analogous to slot 158's amendment-overlay role for cascade-132 sec 3.1) that: (a) adds the 5th row `Cites Umbrella concept`, (b) inserts the PCF-2 v1.4 axis-coverage table per the locked schema, (c) cites this verdict (slot 160 bridge SHA when landed) as the schema authority.
- **Not (iii)** because runbook-only loses in-repo discoverability for future operators reconstructing program governance from the bridge alone.

---

### Q6_RESPONSE

**Q6. Consistent.** No slot 157 amendment-overlay required. Verification:

- Slot 157 §Q4b prescribed Option α' (PCF-2 v1.4 → Umbrella v2.3) deposit cascade. Slot 160 schema is purely additive on top: it does not change *which* deposits exist, it specifies *how axis structure is expressed within* the prescribed deposits. Compatible.
- Slot 157 §Q4b-2 prescribed Appendix C with 4 sub-sections in Umbrella v2.3. Slot 160 schema does not redefine Appendix C content; the axis-coverage table lives in the **Zenodo Description metadata**, not in the Appendix C LaTeX. Orthogonal surfaces — no conflict.
- Slot 157 §Q5e M10 SAFE phrasing ("SATISFIED BY CONSTRUCTION" via Appendix C section ii) is preserved: M10 row in PCF-2 v1.4 axis-coverage table reads `partial` (consistent with slot 159 outlook §5 "M10 V0 OPEN"); SAFE phrasing language stays in Umbrella v2.3 Appendix C, not in the Zenodo metadata table. Compatible.
- D-157-7 (Community deferral) is **re-affirmed** by Q3a, not contradicted. Compatible.

---

### TRADEOFF MATRIX

| Axis | 3-layer hybrid (agent pre-prop) | Native-only (status quo) | Layer 2 only (no Community) | Layer 1+3 (no axis table) | All three full + slot 160 MAX fire |
|------|---|---|---|---|---|
| Machine-parseability of paper-tier | HIGH | HIGH | LOW | HIGH | HIGH |
| Human-readability of axis structure | HIGH | LOW | HIGH | LOW | HIGH |
| Discoverability | MEDIUM | LOW | LOW | MEDIUM | HIGH |
| Audit-trail completeness | HIGH | MEDIUM | MEDIUM | LOW | HIGH |
| Composition cost | LOW-MED | LOW | LOW | MED | HIGH |
| Amendment-ease as axes open | MED | HIGH (nothing to amend) | MED | HIGH | LOW |
| Forward-compat (10y horizon) | HIGH | MEDIUM | MEDIUM | MEDIUM | HIGH-but-locked |
| RULE 1 fire-eligibility (slot 160) | clean (NO-FIRE) | N/A | clean (NO-FIRE) | clean (NO-FIRE) | requires fire + Community decision |

**Pareto-dominated rows:**
- **Native-only (status quo)** is dominated by **3-layer hybrid** on every axis except composition cost and amendment-ease (where status quo trivially wins by doing nothing). Acceptable as a do-nothing baseline only.
- **Layer 1+3 (no axis table)** is dominated by **3-layer hybrid** on human-readability and audit-trail completeness, with no compensating gain — Layer 3 (Community) without Layer 2 (axis table) gives discoverability without forensic substance. Strictly worse.

**Pareto-frontier rows:**
- **3-layer hybrid (Layers 1+2 now, Layer 3 deferred per D-157-7)** — best HIGH/HIGH/MEDIUM/HIGH on the four substance axes at LOW-MED composition cost.
- **Layer 2 only (no Community)** — same as 3-layer hybrid given D-157-7 deferral makes them operationally identical until Layer 3 is unblocked.
- **All three full + slot 160 MAX fire** — top discoverability and forward-compat, but pays HIGH composition cost and LOW amendment-ease (full schema lock makes future evolution rigid). On the frontier but Pareto-tied with 3-layer hybrid until a forcing function for Layer 3 appears.

**Recommended row: 3-layer hybrid with Layer 3 deferred (= Layer 1+2 operative now)**, schema locked inline (NO-FIRE), Layer 3 lift gated on D-157-7 + RULE 1 lift.

---

### RECOMMENDATION + MIGRATION

**Q4a (recommendation).** **SCHEMA_LOCK_INLINE.** Slot 160 verdict-only resolution: lock Layer 1 row pattern (Q1a), Layer 2 controlled vocabulary (Q2b) and granularity rule (Q2c), Layer 3 deferral (Q3a re-affirms D-157-7). No fire-deliverable beyond this verdict packet itself.

**Q4b (specification).** N/A (NO-FIRE). The verdict packet is the artifact.

**Q4c (consistency).** Verified compatible with slot 157 §Q4b Option α' cascade, slot 157 §Q4b-2 Appendix C structure, slot 157 §Q5e M10 SAFE phrasing, slot 157 D-157-7 Community deferral, and slot 159 canonical outlook §5 axis statuses. **No slot 157 amendment-overlay required.**

**Q4d (migration path).** When tabled axes flip post-RULE-1-lift:
1. **Canonical outlook update**: amend slot 159 outlook source-of-record via standard fire (this is the authoritative status flip).
2. **Existing deposits**: frozen. No version increment, no description edit.
3. **Next anchor deposit** (whichever lands first post-flip): axis-coverage table reflects new status; this becomes the most-current snapshot. The temporal sequence of anchor-deposit tables forms the deposit-tier audit trail of axis evolution.
4. **Community description** (when D-157-7 lifts): one-line pointer to outlook URL; outlook URL updates point to current outlook bridge SHA, no Community description churn.
5. **GitHub URL decay**: if repo identity changes, prose-tier SHA references survive; prose-tier URLs become stale-but-recoverable. SWHID upgrade path documented in operator runbook for future V1 milestone.

---

### AMENDMENTS

- **§3 Q2b controlled vocabulary**: agent-proposed 7-status set amended to locked 7-status set per Q2b above (rename `covered (V0-closed; ...)` → `closed (V0; ...)`; fold `retired (into Mx)` into `closed (retired into Mx)`).
- **§3 Q1a row set**: 4-row set amended to 5-row set per Q1a (add `Cites Umbrella concept` for symmetry with PCF-1 pattern).
- **§3 Q4a options**: recommendation is option (iii), with the clarification that "newest-deposit table being authoritative" should be re-stated as "canonical outlook (slot 159) is authoritative; deposit tables are time-stamped snapshots."
- **§5 Q4a label space**: actual recommendation is `SCHEMA_LOCK_INLINE` (the §6 schema includes this label, but §5 Q4a's options list omitted it — read this as confirming the §6 label as the operative one).

### ANOMALIES

- **LOW**: §2 STEP 0.3 lists `10.5281/zenodo.19963298` (PCF-2 v1.3) as a target in Q1a row 1, but this DOI is not in the 5-DOI pre-verification table (which lists concept-DOIs only). Version-DOI for PCF-2 v1.3 should be live-resolved at deposit time; not a verdict blocker.
- **LOW**: §2 STEP 0.2 SHA `70d1a48` (PICTURE-V19-CONSOLIDATED-DEPOSIT) is referenced as M9 PARTIAL substrate but Q1a recommends *not* adding `Cites` rows for this deposit in PCF-2 v1.4 metadata. The picture v1.19 deposit's relation to PCF-2 v1.4 is axis-tier (M9 PARTIAL), expressed via the axis-coverage table, not Layer 1. No conflict, but operator should be aware that `70d1a48` does not appear in PCF-2 v1.4 Layer 1 row set.
- **LOW**: §2 STEP 0.3 verification of `19931635`, `19936297`, `19941678`, `19996689`, `19885550` is per-memory rather than live-resolved at consultation time. Per slot 116 J2 sidebar precedent, live-resolve at deposit time is sufficient; flagged here for operator awareness.

### ABSORPTION_GUIDANCE

- **SQL todo updates**:
  - Mark slot 160 status `LANDED-VERDICT-ONLY` (no fire-deliverable);
  - Add follow-up todo `F6 substrate-prep MUST embed Q2b vocabulary + Q2c granularity rule + Q1a 5-row pattern`;
  - Add follow-up todo `slot 137 zenodo_v14_description_block.md amendment-overlay: 5-row Layer 1 + 12-row axis-coverage table per locked schema; cite slot 160 verdict SHA`.
- **Follow-up fires (priority order)**:
  1. F6 Umbrella v2.3 substrate-prep (already gated; embed schema inline).
  2. Slot 137 amendment-overlay fire for `zenodo_v14_description_block.md` (analogous to slot 158's amendment-overlay role; small scope, ~1 deliverable).
  3. PCF-2 v1.4 deposit-time operator action (uses amended description block).
  4. Umbrella v2.3 deposit-time operator action (uses F6 deliverable).
  5. (Deferred) D-157-7 / F5 Zenodo Community decision post-RULE-1-lift.
  6. (Future-V1) SWHID submission for `siarc-relay-bridge` per Q4b mitigation.
- **Candidate memory promotions**:
  - "Anchor deposits (PCF-1, PCF-2, Umbrella, Channel Theory, D2-NOTE) carry M1-M12 axis-coverage table; single-purpose deposits cite canonical outlook by reference."
  - "Locked Zenodo metadata vocabulary: `closed (V0; primary)` / `closed (V0; folded)` / `closed (retired into Mx)` / `partial` / `external` / `not in scope` / `tabled (RULE 1)`."
  - "Zenodo `IsNewVersionOf` is the documented exception to concept-DOI-target discipline; it requires version-DOI on both sides."
  - "Cascade SHAs cited in deposit Description body (prose), not Related-identifier `References` rows; SWHID upgrade path reserved for V1 milestone."
- **Slot 137 / 135 substrate amendment requirements**:
  - **Slot 137 (`45e236c`)**: amendment-overlay required to add 5th Layer 1 row (`Cites Umbrella concept`) and embed PCF-2 v1.4 axis-coverage table.
  - **Slot 135 (`887981b`)**: superseded by F6 Umbrella v2.3 substrate-prep, which will embed the schema natively; no retroactive amendment to v2.2 needed.
- **D-157-7 (Community) status update**: **re-affirmed deferred**. No change. Lift gated on RULE 1 lift + emergence of a forcing function (external citation requiring Community URL anchor).
- **Dual-witness escalation**: **not required**. Single-witness sufficient because (a) NO-FIRE outcome means no deliverable to dual-witness over, (b) schema lock is on a small controlled vocabulary with high reviewability, (c) consistency check with slot 157/159 is mechanical and verifiable from in-prompt substrate alone, (d) symmetric with slot 157 framing-consultation single-witness precedent.

### ONE-LINE TAKEAWAY

Lock the 5-row Layer 1 pattern + 7-status Layer 2 vocabulary + Layer 3 deferral inline, no slot 160 fire — fold into F6 substrate-prep and a slot 137 amendment-overlay; canonical outlook (slot 159) remains the single source of truth, anchor deposits carry timestamped snapshots.
