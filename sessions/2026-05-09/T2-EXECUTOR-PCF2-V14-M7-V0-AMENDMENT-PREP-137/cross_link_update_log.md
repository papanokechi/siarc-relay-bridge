# Cross-link update log — PCF-2 v1.4 (OPERATOR-PENDING template)

**Status**: TEMPLATE. To be filled by operator at the Zenodo deposit step (Phase D, TABLED under RULE 1).

**Source**: T2-EXECUTOR-PCF2-V14-M7-V0-AMENDMENT-PREP-137 (slot 137)

This log tracks DOI / cross-link metadata edits that need to be applied across the PCF-2 v1.4 deposit chain. Edits below should be applied AFTER the v1.4 version DOI is assigned and recorded in `zenodo_v14_deposit_log.md`.

---

## §1 PCF-2 v1.4 → other documents (cite-out)

PCF-2 v1.4 cites PCF-1 in its prose (e.g., `op:j-zero-amplitude-h6` `\paragraph{What remains open.}` paragraph (iii) cites "PCF-1 v1.3 §5"). Recommendation: where the v1.4 source uses `\cite{Papanokechi2026PCF1}`, the bibitem entry already points at the PCF-1 concept DOI. **No edits needed** — bibitems carry over from v1.3 unchanged (per §2.6 zero-bibitem-add rule).

## §2 Other documents → PCF-2 v1.4 (cite-in)

These edits attach the freshly-assigned PCF-2 v1.4 version DOI into other in-flight deposits:

### §2.1 Umbrella v2.2 (slot 135 substrate; deposits SECOND per Option α)

File: `siarc-relay-bridge/sessions/2026-05-09/T2-EXECUTOR-UMBRELLA-V22-M9-V0-DEPOSIT-PREP-135/zenodo_v22_description_block.md`

**Edit needed**: in the `Related identifiers` table, the `IsSupplementTo` row for PCF-2 should cite the PCF-2 v1.4 version DOI (TBD at v1.4 deposit time) **OR** the PCF-2 concept DOI `10.5281/zenodo.19936297` (recommended per Zenodo best-practice — concept DOI tracks all versions). Operator decides based on Zenodo convention; default recommendation: concept DOI for cross-paper `IsSupplementTo` rows.

| Action | Old value | New value |
|--------|-----------|-----------|
| TBD    | TBD       | TBD       |

### §2.2 Picture-chain v1.20+ (slot 136 substrate; deposits THIRD per Option α; substrate-prep not yet fired at slot 137 fire time)

File: TBD (when slot 136 fires, the analog of `zenodo_v22_description_block.md` will exist)

**Edit needed**: same as §2.1 — splice PCF-2 concept DOI (preferred) or v1.4 version DOI into picture-chain v1.20+ `IsSupplementTo` table.

### §2.3 PCF-1 v1.3 record (NO EDIT — Zenodo records are immutable post-deposit)

PCF-1 v1.3 is already deposited (concept DOI `10.5281/zenodo.19931635`, v1.3 version DOI `10.5281/zenodo.19937196`). Zenodo records are immutable post-deposit; PCF-1 v1.3 cannot be edited to cite PCF-2 v1.4. The cross-link is one-directional (v1.4 cites PCF-1; PCF-1 does not cite v1.4 retroactively).

### §2.4 Channel theory document (PCF-2 cite-back)

File: `pcf-research/channel/cc_pipeline_v13_2026-05-02/channel_theory_outline.tex`

The line ~L1522 cites `19936297` (PCF-2 concept DOI). **No edit needed** — concept DOI tracks all versions automatically. If a future channel-theory revision adds a version-specific cite, it should use the PCF-2 v1.4 version DOI; otherwise the existing concept-DOI cite remains correct.

## §3 Forward-pointed governance: PCF-1 IsSupplementTo correction

Per UF-137-6: slot 135 `zenodo_v22_description_block.md` (and slot 116 deliverables) cited `10.5281/zenodo.19937196` in `IsSupplementTo` rows pointing at PCF-1. This DOI is PCF-1's **v1.3 version DOI**, not its concept DOI. Per Zenodo best practice, `IsSupplementTo` for cross-paper relationships should use the **concept DOI** so the link tracks future versions automatically.

**Recommended forward-pointed correction** (deferred from slot 137; deposit-time judgment call by operator):

- File: `sessions/2026-05-09/T2-EXECUTOR-UMBRELLA-V22-M9-V0-DEPOSIT-PREP-135/zenodo_v22_description_block.md`
- Old: `IsSupplementTo` row → `10.5281/zenodo.19937196` (PCF-1 v1.3 version DOI)
- New: `IsSupplementTo` row → `10.5281/zenodo.19931635` (PCF-1 concept DOI)

If applied at deposit time, this correction propagates to picture-chain v1.20+ as well.

## §4 Edit-application log (OPERATOR FILLS as edits are made)

| Date / time (UTC) | File                                      | Edit description                                                                | Result        |
|-------------------|-------------------------------------------|----------------------------------------------------------------------------------|---------------|
| TBD               | TBD                                       | TBD                                                                              | TBD           |
| TBD               | TBD                                       | TBD                                                                              | TBD           |

## §5 Notes

(Operator-fillable free-form notes section.)
