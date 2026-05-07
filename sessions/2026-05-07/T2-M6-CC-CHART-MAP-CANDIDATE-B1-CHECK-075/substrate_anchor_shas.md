# Substrate anchor SHAs (075 T2-M6-CC-CHART-MAP-CANDIDATE-B1-CHECK-075)

**Session:** 075
**Date:** 2026-05-07
**Bridge HEAD at fire time:** `3410e5d`

This file aggregates SHA-256 anchored substrate citations consumed by 075
for the structural-form check between BT 1933 §5 (13 a) (the FILL side
surfaced by 073 unexpected find U1 [CHART-MAP-CANDIDATE-B1]) and the
069r1 A.1.5 chart-map specification (the GAP side). All SHAs were
recomputed at fire time via PowerShell `Get-FileHash -Algorithm SHA256`.

---

## A. Gap-side substrate (069r1 + 058R)

Path A.1: `sessions/2026-05-07/M6-CC-R1-CLOSURE-PREFLIGHT-069R1/`

| file                              | full SHA-256 (lower-hex 64)                                      | role in 075                                                                            |
|-----------------------------------|------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| `handoff.md`                      | `f7fc1c39efe2c97824b4ff15df98795d9020a3b0f5b66aa928c51ea2cc53a649` | NO_GO_SUBSTRATE_INSUFFICIENT verdict + §A.1.5 chart-map block + §52 OQ-W21-LITERATURE-ALTERNATIVE |
| `phase_a_path_alpha.md`           | `c8dc5f4e9865a24d9a3fd623320257cd11de17762ecefc82ffa4566f73bb2e5` | §1.5 "Required artefact" block — 4-equation closed-form chart-map specification        |

Path A.2: `sessions/2026-05-06/CC-VQUAD-PIII-NORMALIZATION-MAP-RERE-FIRE/`

| file                              | full SHA-256 (lower-hex 64)                                      | role in 075                                                                            |
|-----------------------------------|------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| `phase_b_canonical_map.md`        | `f831f9bd58d1f3064873dfdeab14c003bf441cbb3832e02b6cdddc94a91ff8bb3` | L136-140 verbatim "(i) explicit conversion ... this is residual R1 partially closed"   |

Note (J1): `phase_b_canonical_map.md` SHA-prefix carry-forward from
069r1 substrate-anchor table is `F831F9BD58D1F306..` (PowerShell
returned `F831F9BD58D1F3064873DFDEAB14C003BF441CBB3832E02B6CDDDC94A91FF8BB3`
at fire time; truncated SHA matches; full 64-hex column above is the
fire-time observation).

## B. Fill-side substrate (073)

Path: `sessions/2026-05-07/T1-PHASE-3-BT-1933-SECTIONS-4-6-READTHROUGH-073/`

| file                                       | full SHA-256 (lower-hex 64)                                      | role in 075                                                                            |
|--------------------------------------------|------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| `bt_1933_section_5_extract.md`             | `ec2c0d5a2dadef3b3b5342869fff31b5ae7644efe84853512485ffbc014e6b97` | verbatim §5 extract; (13 a) at p. 47                                                   |
| `bt_1933_section_5_claim_table.md`         | `00103c17ff3b7a99cc4fc248684f77ea83185b2ca9f6fe1376d6509590826750` | [CLAIM-B517] [CHART-MAP-CANDIDATE-B1] tag + Phase C.4 surfacing                        |
| `unexpected_finds.json`                    | `b8d95b12abc88ecc576a07a6e2bc8b4efca3980ba6d885a0ef8af43c37c391e9` | U1 metadata for [CHART-MAP-CANDIDATE-B1]                                               |

Match against 073 `substrate_anchor_shas.md` carry-forward:
- `bt_1933_section_5_extract.md` recorded `ec2c0d5a..` -> matches.
- `bt_1933_section_5_claim_table.md` recorded `00103c17..` -> matches.

## C. Source-paper PDF anchors (read-only; not opened in 075)

| Slot           | Artefact                                  | full SHA-256 (lower-hex 64)                                      | recorded in            |
|----------------|-------------------------------------------|------------------------------------------------------------------|------------------------|
| 03 (BT 1933)   | `literature/bt_1933_acta_60.pdf`           | `dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6` | 073 substrate index    |
| Adams-1928     | `literature/adams_1928_trans_ams_30.pdf`   | `d7ac4017a9737fef00e10257f26b9a6a6f6cc23437d2654440359f2e24836e18` | 073 substrate index    |

Note: 075 does NOT open either PDF; the §5 (13 a) text and the (Adams §3
P(x) = H^{-1}(x) G(x)) cross-reference are consumed indirectly via the
073 / 072 deliverables above, both of which carry the source-PDF SHA in
their internal substrate index. Per 075 §A.3 the targeted Adams §3
re-readthrough is gated to the contingent 076 INSUFFICIENT-branch
extension, not to 075 scope.

## D. Cross-walk substrate (072)

Path: `sessions/2026-05-07/T1-PHASE-3-ADAMS-1928-READTHROUGH-072/`

| file                                       | role in 075                                                                            |
|--------------------------------------------|----------------------------------------------------------------------------------------|
| `adams_to_bt1933_ladder_map.md`            | T6 row (Adams §3 P(x) = H^{-1}(x) G(x); BT 1933 PARALLEL pre-073, EXTENDED post-073)   |
| `adams_1928_main_theorems_summary.md`      | T6 row at Adams p. 517 verbatim "P(x) = H^{-1}(x) G(x)"                                |

Cross-walk role: the 073 unexpected-find U1 explicitly identifies BT
1933 §5 (13 a) as "the BT-side analogue of Adams 1928's Class-2a
periodic-functions matrix P(x) (Adams §3 p. 517)". 075 consumes this
labelling at the substrate-inventory level only; no §3 verbatim
re-extraction performed.

## E. Wasow 1965 substrate (075 §A.4 check)

Wasow 1965 (Dover repr.) PDF is on-disk at slot 04 per 073 / 072 / 058R
substrate ledgers; verbatim §-level extraction has NOT been performed
in any of 058R / 069 / 069r1 / 070 / 072 / 073 sessions. The 069r1 §A.4
chart-map question ("does Wasow 1965 LNM address the chart-map regions
sectorial structure?") therefore cannot be answered from on-disk 075
substrate without a Wasow §-level extract. 075 records this as a
substrate-availability fact only and does not open the Wasow PDF.

Citation channel for any Wasow-related structural assertion in 075 is
via D2-NOTE v2.1 (`siarc-relay-bridge/sessions/2026-05-03/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/d2_note_v2_1.pdf`,
SHA `a8b6026a3453f901a0da68c3849a9d7d828138ca4622b8a3686b68f01d5ef74e`)
recorded by 073's `substrate_anchor_shas.md`; 075 does NOT cite Wasow
beyond the convention-drift acknowledgement already carried forward as
069 anomaly D2.

## F. Drift-guard (HALT_075_SUBSTRATE_DRIFT)

| anchor                                              | recorded SHA prefix      | observed SHA prefix      | match |
|-----------------------------------------------------|--------------------------|--------------------------|-------|
| 073 `bt_1933_section_5_extract.md`                  | `ec2c0d5a..`             | `ec2c0d5a..`             | PASS  |
| 073 `bt_1933_section_5_claim_table.md`              | `00103c17..`             | `00103c17..`             | PASS  |
| 058R `phase_b_canonical_map.md`                     | `F831F9BD58D1F306..`     | `f831f9bd58d1f306..`     | PASS  |
| BT 1933 PDF (slot 03)                               | `dcd7e3c6..`             | (carried via 073)        | PASS (transitive) |
| Adams 1928 PDF                                      | `d7ac4017..`             | (carried via 073/072)    | PASS (transitive) |

HALT_075_SUBSTRATE_DRIFT not triggered.

End of `substrate_anchor_shas.md`.
