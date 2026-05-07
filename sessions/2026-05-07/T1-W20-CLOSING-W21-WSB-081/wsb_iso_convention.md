# WSB ISO-week boundary convention memo

**Author:** CLI-Synth in-tier under v2026-05-08 RACI Tier 2
**Date:** 2026-05-07 (drafted as part of relay 081 Phase F)
**Bridge HEAD at write time:** `72f9850`
**Substrate-only.** No advocacy. This memo describes past usage; it does not recommend a convention.

## Two conventions observed in the substrate

The project's W-numbering exhibits two co-existing conventions across canonical artefacts. Both are substrate-attested. No single document declares one or the other authoritative.

### Convention A — ISO-aligned

Under Convention A, project W_n = ISO week n. The ISO-8601 calendar week starts Monday and closes Sunday. For 2026:

- ISO W19 = Mon 2026-05-04 to Sun 2026-05-10.
- ISO W20 = Mon 2026-05-11 to Sun 2026-05-17.
- ISO W21 = Mon 2026-05-18 to Sun 2026-05-24.

Convention A is used in the following canonical artefacts:

- `cli_log/2026-W19.md` (W19 closing handoff written 2026-05-06): file header `# W19 closing handoff (2026-05-04 → 2026-05-10)`. Bridge HEAD anchor at write time `78c7b16`.
- `cli_log/2026-W19_wsb.md` (W19 WSB drafted 2026-05-05 08:38 JST): defines W19 as 2026-05-04 to 2026-05-10.
- `cli_log/2026-W20_wsb.md` (W20 WSB drafted 2026-05-06 as part of 048 re-fire): file header `# W20 WSB (2026-05-11 → 2026-05-17)`.
- `cli_log/2026-W19_master_prompt.md` (drafted 2026-05-05 08:38 JST).

### Convention B — "+1-shifted" (W_n project = ISO W_(n-1))

Under Convention B, project W_n = ISO W_(n-1). The same Mon-to-Sun calendar window is labeled with a W-number one greater than its ISO assignment.

- Project W20 (Convention B) = Mon 2026-05-04 to Sun 2026-05-10 = ISO W19.
- Project W21 (Convention B) = Mon 2026-05-11 to Sun 2026-05-17 = ISO W20.
- Project W22 (Convention B) = Mon 2026-05-18 to Sun 2026-05-24 = ISO W21.

Convention B is used in the following artefacts:

- Relay prompt 081 (this prompt's frame): "Drafted: 2026-05-07 ~17:00 JST (Thu, W20)" labels Thu 2026-05-07 as a W20 day, which under Convention A is W19-Thu. Phase D §1 specifies "## W20 closing handoff (2026-05-04 → 2026-05-10)" — the same date range that Convention A names W19 close.
- W20-Wed cascade commit messages (074 / 077 / 078 / 079 commit-time Thu 2026-05-07): refer to the cascade as "W20-Wed" meaning Thu 2026-05-07 is in project W20. Forward-pointers reference "W21 LANE-1 Mon 2026-05-12 AM JST" — the date 2026-05-12 is ISO Tue, while the day-of-week label "Mon" plus the W21 frame is consistent with Convention B if W21 starts Mon 2026-05-11 (and the "05-12" is a one-day drift; see anomaly note below).
- 081 prompt §"Fire window: W20-Sun 2026-05-10 AM-PM JST" labels Sun 2026-05-10 as W20-Sun (Convention B; Convention A labels it W19-Sun).

### Convention-overlap range table

| Mon-Sun calendar window | Convention A label | Convention B label |
|---|---|---|
| 2026-04-27 → 2026-05-03 | W18 | W19 |
| 2026-05-04 → 2026-05-10 | W19 | W20 |
| 2026-05-11 → 2026-05-17 | W20 | W21 |
| 2026-05-18 → 2026-05-24 | W21 | W22 |
| 2026-05-25 → 2026-05-31 | W22 | W23 |

## Day-of-week label drift (separate phenomenon)

Independent of the W-numbering convention, several cli_log day-of-week labels in `cli_log/2026-W19.md` use day-of-week tokens that do not match the ISO day-of-week for the cited date. Examples:

- `cli_log/2026-W19.md` §Day-by-day arc: "Thu 2026-05-08 (paste-time of 046)" — but 2026-05-08 is ISO Fri (Mon=04, Tue=05, Wed=06, Thu=07, Fri=08). The same arc lists "Fri 2026-05-09" (ISO Sat), "Sat 2026-05-10" (ISO Sun), "Sun 2026-05-11" (ISO Mon-of-next-week). Pattern: -1-day shift on day-of-week labels for Thu through Sun within the W19.md doc.
- W20-Wed cascade commit messages: "Mon 2026-05-12 AM JST" — but 2026-05-12 is ISO Tue. Similar -1-day drift on day-of-week tokens.

The W19.md commit text was drafted on Wed 2026-05-06 looking forward to predicted activity later in the week. The day-of-week mismatches with ISO are most parsimoniously read as drafting-time miscounts that did not get audited before the doc landed. The dates themselves (2026-05-08, 2026-05-09, 2026-05-10, 2026-05-11) are correct as ISO calendar dates; the ISO day-of-week token attached to each is the artefact that drifts.

This day-of-week drift is independent of the W-numbering convention. Convention A or Convention B can each be applied with or without the day-of-week drift.

## Status of the W19/W20 ISO-boundary anomaly

The `w19-synthesizer-trust-failure-pattern-flag` (in_progress at fire time of 081) and the `w20-wsb-iso-w19-w20-boundary-reconcile` carry-set item flagged the convention drift. Per `HALT_081_BOUNDARY_FABRICATION` discipline (the Phase F halt that triggers if Phase F.1 cites unsubstantiated past usage), this memo:

- Documents both Convention A and Convention B with verbatim citations to canonical artefacts.
- Documents day-of-week drift as a separate phenomenon visible in `cli_log/2026-W19.md` and W20-Wed cascade commit messages.
- Does NOT advocate for either convention.
- Does NOT recommend retroactive renaming.
- Does NOT alter any prior canonical artefact.

## Convention used in this 081 fire

This 081 fire uses **Convention B** (per the prompt-081 envelope's explicit specification: "## W20 closing handoff (2026-05-04 → 2026-05-10)" plus "Drafted: 2026-05-07 ~17:00 JST (Thu, W20)"). Specifically:

- `cli_log/2026-W20.md` (this fire's closing handoff) covers Mon 2026-05-04 to Sun 2026-05-10. Under Convention A this is the same date range as the existing `cli_log/2026-W19.md` (W19 closing handoff written 2026-05-06).
- `cli_log/2026-W21_wsb.md` (this fire's strategy brief) covers Mon 2026-05-11 to Sun 2026-05-17. Under Convention A this is the same date range as the existing `cli_log/2026-W20_wsb.md` (W20 WSB written 2026-05-06).

The two existing Convention-A-named artefacts (`2026-W19.md` and `2026-W20_wsb.md`) are NOT modified by this 081 fire. The two new Convention-B-named artefacts (`2026-W20.md` and `2026-W21_wsb.md`) are added alongside them. Both naming sets remain on disk.

## Disposition

- `w20-wsb-iso-w19-w20-boundary-reconcile` carry-set item: status DOCUMENTED (not RESOLVED; the convention is described, not chosen).
- Recommendation for future relay-prompt drafting: each prompt-drafter pins the convention they intend to use in the prompt envelope (analogous to the 081 envelope's explicit "Drafted: 2026-05-07 ~17:00 JST (Thu, W20)" frame). Operator may at their discretion canonicalize one of the two conventions in a future RACI revision; this memo does not pre-judge that decision.

End of memo.
