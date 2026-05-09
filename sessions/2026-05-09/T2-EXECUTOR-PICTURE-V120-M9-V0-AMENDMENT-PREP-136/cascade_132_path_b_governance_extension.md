# Cascade-132 PATH_B governance extension (slot 136 §5 G36)

**Excerpt for operator review.** This file contains the full text of the new G36 entry inserted into §5 Gaps to Mitigate of `picture_revised_20260507.md` per slot 136 §2.4 edit pass.

---

## §5 G36 (NEW v1.20 M9 V0 absorption) — verbatim text

> **G36 (NEW v1.20 M9 V0 absorption): M9 V0 announcement-of-record gating.**
> Per cascade-132 PATH_B Option α (bridge `fd669d3`), the M9 V0
> announcement-of-record is gated on completion of three substrate-prep
> fires (slot 135 umbrella v2.2 LANDED 2026-05-09 SHA `887981b`; slot 137
> PCF-2 v1.4 LANDED 2026-05-09 SHA `45e236c`; slot 136 picture-chain v1.20+
> LANDED 2026-05-09 SHA `<this-fire>`) plus M10 status resolution. Once all
> four conditions satisfy, RULE 1 lifts and the operator-side Zenodo
> deposit window opens (Phase C+D for all three substrate-preps in
> sequence). Mitigation: slot 138+ orchestrates RULE 1 lift via
> M10-status-resolution sub-fire (TBD — operator decision on whether M10
> is a separate axis or bundled into the existing M-axis V0 closure). The
> deposit chain is **chronologically ordered** at the Zenodo layer (PCF-2
> v1.4 first, umbrella v2.2 second, picture-chain v1.20+ third) per
> cascade-132 §3.1 unanimous Option α; the substrate-prep fires landed
> in slot-numerical order (135 → 137 → 136) which reverses the deposit
> order. The qualifier-class governance rule (substantive vs staging;
> see §28.C) applies forward to slot 138+ and any future cascade-class V0
> closure amendment cycles.

---

## Insertion site

- File: `tex/submitted/control center/picture_revised_20260507.md`
- Section: `## 5. Gaps to Mitigate` (begins L1025 post-edit)
- Insertion point: between the severity legend (ending at L1059 post-edit) and the `---` separator before `## 6. Suggested Next Steps — Queued Prompts`
- Per slot 136 §2.4 prompt instruction: "append a new mitigation entry. Insertion point: just before `## 6. Suggested Next Steps — Queued Prompts`"

---

## Cross-references threaded

| Reference | Resolves to |
|-----------|-------------|
| cascade-132 PATH_B Option α | bridge `fd669d3`; T1-SYNTH-M9-V0-CLOSURE-PATH-CONSULTATION-CASCADE-132 (operative decision) |
| slot 135 / SHA `887981b` | umbrella v2.2 substrate-prep LANDED 2026-05-09 |
| slot 137 / SHA `45e236c` | PCF-2 v1.4 substrate-prep LANDED 2026-05-09 21:52 JST |
| slot 136 / SHA `<this-fire>` | picture-chain v1.20+ substrate-prep (THIS slot — the SHA placeholder is replaced post-deposit by the bridge HEAD SHA at deposit-confirmation) |
| §28.C | qualifier-class governance rule (UF-132-5 absorption) — see `qualifier_class_governance_rule.md` |
| cascade-132 §3.1 | unanimous Option α deposit ordering decision |

---

## Operator-pending tasks (Phase C+D, TABLED under RULE 1)

1. After slot 136 commit lands and the bridge HEAD SHA is known, replace the `<this-fire>` placeholder in §5 G36 with the actual short SHA. (Recommended: a one-line follow-up edit in a slot 138+ housekeeping sub-fire.)
2. Once M10 status resolves, slot 138+ orchestrates RULE 1 lift and Phase C+D opens for all three substrate-preps.
3. Cascade-132 §3.1 deposit ordering (PCF-2 v1.4 first, umbrella v2.2 second, picture-chain v1.20+ third) is binding at the Zenodo layer.

---

**Status:** governance reference inserted into picture-chain source-of-record per cascade-132 PATH_B Option α; THIRD and FINAL realization of the cascade-132 deposit chain.
