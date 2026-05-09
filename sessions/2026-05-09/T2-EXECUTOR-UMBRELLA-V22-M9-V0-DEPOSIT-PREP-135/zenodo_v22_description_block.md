# Zenodo v2.2 description block — operator-side runbook

**Session**: T2-EXECUTOR-UMBRELLA-V22-M9-V0-DEPOSIT-PREP-135
**Date drafted**: 2026-05-09
**Status**: OPERATOR-PENDING (Phase C+D TABLED under RULE 1; lift gated on slot 135 + 136 + 137 + post-M10 per cascade-132 §3.4 unanimous)

This document is the operator-side runbook for the umbrella v2.2 Zenodo new-version deposit. The agent does NOT execute the Zenodo upload; this file pre-stages the description-block text and metadata fields for the operator to paste into the Zenodo new-version form when RULE 1 lifts.

---

## §1. Deposit metadata

| Field             | Value                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------------|
| Concept DOI       | `10.5281/zenodo.19885550` (per slot 116 J2 resolution; reuse same concept; new version)                       |
| Version DOI       | `TO_BE_ASSIGNED` (operator fills at deposit time)                                                             |
| Version label     | `v2.2`                                                                                                       |
| Version sequence  | v1 → v2.0 → **v2.2** (v2.1 internal staging only; not deposited; FIRST version-skip in SIARC umbrella series per UF-132-7 / UF-135-2) |
| Resource type     | Publication / Working paper                                                                                  |
| Title             | `An Arithmetic Stratification of Polynomial Continued Fractions: Program Statement of the SIARC Series (v2.2: Full M-axis V0 Closure Series)` |
| Author            | papanokechi                                                                                                  |
| Affiliation       | Independent researcher, Yokohama, Japan                                                                      |
| Date              | May 2026                                                                                                     |

## §2. Version-difference description text

To be pasted into the Zenodo new-version form's "Version notes" / "What's new" field. Adopts the cascade-132 §5.3 verbatim text:

> **v2.2 (May 2026):** Consolidates full M-axis V0 closure series (M4, M7, M8a, M8b) and M6.CC R1; supersedes v2.1 internal staging.

### Expanded variant (longer "Description" field; optional)

> The v2.2 revision of the SIARC umbrella program statement extends the v2.0 Closure Cascade and Bridge Provenance section (§\ref{sec:closure-cascade}) from 3 milestones to 6 milestones, adding the M-axis V0 ratification cascade triple landed 2026-05-09: M7 V0 (cubic / quartic borderline-anormal $A$ residual; soft-branch ratification at MEDIUM-HIGH; bridge SHA `7f93b9e`; (SOFT-BRANCH; HARD-BRANCH-PENDING)), M8a V0 (catalogue-wide Painlevé-test stratum labeling via the Conte–Musette necessary criterion; 60/60 LABELED uniformly; bridge SHA `cb429e1`; (ALG-TEST-SCALE; STOKES-DICHOTOMY-DELEGATED-TO-M8B)), and M8b V0 (numerical foreclosure of the laptop-feasible $|S_2|$ extraction at $d=2$; cross-provider dual-witness; bridge SHA `74c5630`; (NUMERICAL-FORECLOSURE; d≥3-CAVEAT-CARRIED-FORWARD)). The v2.0 → v2.2 version sequence skips v2.1 (internal staging only at bridge `883dddf`, 2026-05-09) per the operative cascade-132 (`fd669d3`) PATH_B decision. All mathematical content, conjectures, open problems, and the cross-degree triple of §\ref{sec:triple} are unchanged from v2.0; v2.2 is a status / provenance addendum, not a content revision.

## §3. Picture-chain v1.20+ deposit accompaniment note

Per cascade-132 §3.2 unanimous (cross-axis sub-question Q-α-2):

> Picture-chain v1.20+ deposit accompanies this version.

**Operator decision at deposit time**: include this note IF picture-chain v1.20+ deposit is in the same Zenodo session (i.e., slots 135 + 136 + 137 are all dispatched / staged together); omit IF picture-chain v1.20+ deposit lags. The note is forward-pointed metadata, not a hard claim.

## §4. Companion-paper cross-link metadata

Per cascade-132 §3.4 cross-link discipline. To be added to the Zenodo "Related identifiers" section:

| Relation            | Identifier                                                          | Description                                                  |
|---------------------|---------------------------------------------------------------------|--------------------------------------------------------------|
| `IsNewVersionOf`    | `10.5281/zenodo.19885550` (concept DOI)                            | umbrella v1 / v2.0 (v2.1 internal staging; not deposited)     |
| `IsSupplementTo`    | `10.5281/zenodo.19937196` (PCF-1 v1.3)                             | Companion paper PCF-1 v1.3                                    |
| `IsSupplementTo`    | `10.5281/zenodo.19963298` (PCF-2 v1.3 — REPLACE WITH v1.4 IF v1.4 IS DEPOSITED FIRST PER CASCADE-132 §3.1 UNANIMOUS OPTION α) | Companion paper PCF-2 (v1.3 or v1.4)                          |
| `IsSupplementTo`    | `10.5281/zenodo.19951331` (Channel Theory v1.2)                    | Companion paper CT v1.2                                        |
| `IsSupplementTo`    | `10.5281/zenodo.19915689` (T2B v3.0)                               | Companion paper T2B v3.0                                       |
| `IsSupplementTo`    | `(picture-chain v1.20+ DOI; TO_BE_ASSIGNED at slot 136 deposit)`   | Picture-chain v1.20+                                          |
| `IsCitedBy`         | `(submission_log Item 12 series 2; if applicable)`                 | Operator splice at deposit time                                |
| `Cites` (bridge)    | `https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-05-09/T2-EXECUTOR-UMBRELLA-V22-M9-V0-DEPOSIT-PREP-135/` | Bridge session for this fire (substrate-prep)                  |

## §5. Operator deposit checklist (Phase C — TABLED under RULE 1)

When RULE 1 lifts:

1. Visit the Zenodo concept DOI `10.5281/zenodo.19885550`.
2. Click "New version".
3. Upload `umbrella_v22.pdf` (513,333 bytes, SHA-256 `8da215bc6b1e4370a64eb3fe26db33c92058069f3da311a47d9c9a667e08efd9`).
4. Optionally also upload `umbrella_v22.tex` source as supplementary file.
5. Update "Title" to the v2.2 form (see §1 above).
6. Update "Description" / "Version notes" with §2 text.
7. Add §4 related-identifier entries (resolve picture-chain v1.20+ DOI from slot 136 deposit first if it lands earlier).
8. Set publication date.
9. Click "Save" then "Publish".
10. Record the resulting version DOI in `zenodo_v22_deposit_log.md` (this folder).
11. Run the Phase D cross-link metadata edits (BibTeX, abstract DOI links, etc.) per `cross_link_update_log.md` (this folder).
12. Splice submission_log Item 12 series 2 per `submission_log_item12_splice.diff` (this folder; operator fills the actual splice text after Zenodo DOI is assigned).

## §6. RULE 1 lift gate

Per cascade-132 §3.4 unanimous: RULE 1 lifts when **slots 135 + 136 + 137 land + post-M10**. Until lift:
- Phase A + B + B.5 + E (substrate-prep + manuscript edit + pdflatex compile + bridge deposit) executed at slot 135 (this fire) — IN SCOPE under RULE 1 §3 ("math-foundational closure tasks").
- Phase C + D (Zenodo new-version deposit + cross-link metadata + submission_log splice) — TABLED under RULE 1 §1; this file pre-stages them for operator-side runbook.

---

**End of zenodo_v22_description_block.md.**
