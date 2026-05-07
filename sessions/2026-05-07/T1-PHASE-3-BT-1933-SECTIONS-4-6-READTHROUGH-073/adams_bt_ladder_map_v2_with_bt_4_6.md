# Adams 1928 ↔ BT 1933 — Ladder Map v2 (with §§4-6 §-level granularity)

**This file resolves 072 D4** ("BT 1933 cross-walk DEFER for 6/9 Adams
references" recorded at 072 `discrepancy_log.json` entry D4) by
extending the 072 v1 ladder map with §-level granularity for BT
§§4-6 informed by the verbatim 073 readthrough.

**Adams 1928 SHA-256:**
`d7ac4017a9737fef00e10257f26b9a6a6f6cc23437d2654440359f2e24836e18`
**BT 1933 SHA-256:**
`dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6`

**072 v1 input:** 072 `adams_to_bt1933_ladder_map.md` at bridge HEAD
`5b297cb` (verified Phase A.4).

**072 main-theorems input:** 072
`adams_1928_main_theorems_summary.md` (Adams identifiers T1-T9; 2
explicitly labelled + 7 narrative).

**BT 1933 §§4-6 main-theorems index:** see this session's
`bt_1933_sections_4_6_main_theorems.md` (BT identifiers T1 = §4
Lemma 8, T2 = §5 Theorem I + T2.cor m = 1 case, T3 = §6 Lemma 9).

## Ladder labels (unchanged from 072 v1)

- **ABSORBED-VERBATIM**: BT 1933 contains the same result with the
  same scope.
- **EXTENDED**: BT 1933 generalises Adams's result.
- **SUPERSEDED**: BT 1933 strengthens Adams's bound or reduces
  hypotheses.
- **PARALLEL**: Adams treats a sub-case BT 1933 does not explicitly
  address.
- **DEFER** (legacy 072 label, retained for 6 of 9 Adams refs that
  pointed at BT §§4-6 region; resolved in this v2 by §-level
  granularity).

## Ladder table v2 (Adams T1-T9 → BT §§4-6 §-level + §§7-9 carry-over)

Each row carries: Adams ID + Adams scope + 072 v1 label + new BT
§-level mapping + revised label + closing comment.

| Adams ID | Adams scope | 072 v1 label | BT §-level mapping (this v2) | Revised label | Comment |
| --- | --- | --- | --- | --- | --- |
| **T1** (Theorem A; Adams §6 p. 529) | Class 1 (n-fold root); existence of determinant limits via infinite-left product P_m(x) | EXTENDED | BT §5 Theorem I (T2; Acta p. 41) — proper-curve construction of proper solutions on the right of Γ; the strip-V proper-fundamental-set hypothesis subsumes Adams's left-product P_m(x) construction. **AND** BT §6 Lemma 9 (T3; Acta p. 48) — Adams's λ-rowed-determinant construction generalises into BT's Q-factorability + factor-operator decomposition L_{n−Γ} · L_Γ. **AND** BT §9 Fundamental Existence Theorem (out of 073 scope). | **EXTENDED** | T1's "form the m-fold left-product P_m(x) = A(x−1) ⋯ A(x−m) T(x−m)" (Adams 1928 §6 p. 529 verbatim opening clause) maps to BT §6 Lemma 9 proof eq. (2) "Y_r(x) = D(x − 1) D(x − 2) ... D(x − r) T(x − r)" (BT 1933 §6 p. 48 verbatim) — the SAME left-product construction at the system level. **072 D4 RESOLVED**: §-level granularity = BT §6 (eq. 2) for the left-product mechanic + BT §5 Theorem I for the resulting proper-solution conclusion. |
| **T2** (Theorem B; Adams §6 p. 537) | Class 1 (n-fold root); right-product mirror P'_m(x) = A^{-1}(x) ⋯ A^{-1}(x+m−1) T(x+m) | EXTENDED | BT §5 Theorem I (T2) carries the right-product analogue implicitly via the proper-curve framework (the "right of a proper curve Γ" wording itself is the right-product orientation). BT §6 Lemma 9 covers the corresponding left-product version. BT 1933 p. 5 (extracted by 072) explicitly states "In quadrants other than Γ results will hold precisely analogous to those obtained with reference to Γ" — the symmetry argument that converts T2 from Adams's right-product to BT's "right-of-proper-curve" quadrant-Γ reading. | **EXTENDED** | **072 D4 RESOLVED**: §-level granularity = BT §5 Theorem I + BT 1933 p. 5 quadrant-symmetry remark. |
| **T3** (Adams §1 p. 509) | Class 1 simple-root regular-type formal series | ABSORBED-VERBATIM (formal-series setup) / EXTENDED (scope: BT covers regular + irregular) | BT §1 (out of 073 scope; covered by 072 v1 ladder) — formal-series setup. **§§4-6 contribution:** BT §6 Lemma 9 (1 b) "the series e^{Q_1(x)} s_1(x), ..., e^{Q_Γ(x)} s_Γ(x) are formal solutions of L_Γ(y) = o" verbatim shows that the BT framework treats Adams's "regular type" simple-root series as a special case (Γ = 1) of the factor-operator's formal-solution set. | **ABSORBED-VERBATIM** (formal-series setup) / **EXTENDED** (Γ = 1 special case explicit in §6) | **072 D4 partial resolution**: the §-level granularity for the §§4-6 share is BT §6 (1 b). The §1-level mapping was already covered in 072 v1. |
| **T4** (Adams §1 p. 511) | Class 2 multi-segment Newton-polygon construction | EXTENDED (different formalism; broader scope) | BT §6 Lemma 9 (T3; Acta p. 48) — the Q-factorability hypothesis "(1) + ... + (m), a subregion of F. If the equation is Q-factorable in (1) + ... + (m) (Def. 8; § 1)" replaces Adams's "(3) is replaced by several characteristic equations, one associated with each segment of L" with a region-and-factorisation framework. Adams's segment-by-segment construction maps to BT's "point of division" between Γ-th and (Γ+1)-st terms at each B'-curve crossing. | **EXTENDED** | **072 D4 RESOLVED**: §-level granularity = BT §6 Lemma 9 (1 a) + Q-factorability (Def. 8; §1). The "different formalism" 072 v1 wording is now anchored: BT replaces Newton-polygon-segment-cutting with Q-factorability-at-point-of-division. |
| **T5** (Adams §2 p. 513) | Class 2a / 2b existence theorems; n formal solutions (10) + matrices G(x), H(x) | EXTENDED | BT §5 Theorem I (T2; Acta p. 41) — the "completely proper in (m) + ... + (η)" conclusion gives existence of n analytic solutions (full matrix _r Z(x) = (_r z_{i j}(x)) at p. 46 verbatim eq. 10 a). BT does NOT carry the explicit Class-2a / Class-2b sub-classification; the unified "completely proper" notion subsumes both. **AND** BT §6 Lemma 9 supplies the factor-operator decomposition that Adams §2 handles via separate G(x) / H(x) matrix constructions. | **EXTENDED** | **072 D4 RESOLVED**: §-level granularity = BT §5 Theorem I (T2) + BT §6 Lemma 9 (T3). The matrix _r Z(x) at BT §5 p. 46 (10) corresponds to Adams's G(x); the periodic-functions matrix p^{r, r+1}(x) at BT §5 p. 46 (11 a) corresponds to Adams's H(x). |
| **T6** (Adams §3 p. 517) | Class 2a periodic-functions matrix P(x) = H^{-1}(x) G(x) with z = e^{2πi x} reduction | PARALLEL (BT focuses on factorisation + Stokes-data structure; no explicit periodic-functions section) | **REVISED** based on 073 readthrough: BT §5 Theorem I proof p. 47 verbatim eq. (13 a) "p^{r, r+1}_{i j}(x) = ∑ p^{r, r+1}_{i j; π} e^{−π_{i j}(r, r+1)}" with |z| = e^{−q+v} **IS** the BT analogue of Adams's P(x) periodic-functions matrix. BT does not name this object "P(x)" or have a §3-style section dedicated to it, but the structural object is present inside the §5 Theorem I proof. | **EXTENDED** (was PARALLEL in 072 v1) | **072 D4 RESOLVED + 072 v1 LABEL CORRECTED**: §-level granularity = BT §5 (13 a) tagged `[CHART-MAP-CANDIDATE-B1]` at `[CLAIM-B517]`. The 072 v1 PARALLEL label was based on the absence of a separately-titled "periodic functions" section header; the verbatim 073 readthrough surfaces the same object at BT §5 p. 47. |
| **T7** (Adams §4 p. 518–p. 525) | Class 2a asymptotic forms in entire plane; critical rays + curvilinear asymptotes C_i | EXTENDED | BT §5 Theorem I (T2) framework — the B'-curve partition (1), (2), ..., (η) plus the (m)-region asymptotic relations (4 a) `_m y_{i_1...i_k; 1...k}(x) ∼ e^{_m Q_1(x) + ... + _m Q_k(x)} _m S_{i_1...i_k; 1...k}(x)` (BT §5 p. 42 verbatim) supply the same content as Adams's critical-ray + C_i picture but with B'-curves as the boundary objects. | **EXTENDED** | **072 D4 RESOLVED**: §-level granularity = BT §5 (4 a) + B'-curves (2). BT's B'-curves replace Adams's C_i curves; the determinant-limit asymptotic form (4 a) replaces the explicit critical-ray transition. |
| **T8** (Adams §7 p. 538) | Class 1, n = 2, double-root strengthening | PARALLEL | (no §§4-6 contribution; the n = 2 sharpening is not separately addressed in BT §§4-6 — BT generalises in n without the explicit n = 2 sharpening Adams supplies) | **PARALLEL** (unchanged from 072 v1) | **072 D4 carry-through**: the n = 2 sharpening is genuinely outside BT §§4-6 scope; the only §-level resolution would have to look at BT §§7-9 which is out of 073 scope. Mark as PARALLEL persists. |
| **T9** (Adams §8 p. 539–p. 541) | Mixed-multiplicity generalisation + p. 541 regions-of-validity caveat | SUPERSEDED | BT §6 Lemma 9 (T3; Acta p. 48) — the Q-factorability hypothesis applied iteratively at each "point of division" supplies the mixed-multiplicity content. BT 1933 p. 5 (extracted by 072) "without restriction upon the form of the formal series" explicitly subsumes Adams's "Class 2 multiple-root extension is immediate" announcement. The regions-of-validity caveat (Adams p. 541 last paragraph) is carried forward by BT as the proper-curve / B'-curve / quadrant-Γ framework. | **SUPERSEDED** | **072 D4 RESOLVED**: §-level granularity = BT §6 Lemma 9 + BT §§7-9 Fundamental Existence Theorem (the §§7-9 part is out of 073 scope but is the natural follow-up). |

## Distribution table (post-073 update)

| Ladder label | 072 v1 count | 073 v2 count | Change | Adams IDs |
| --- | --- | --- | --- | --- |
| ABSORBED-VERBATIM | 1 | 1 | 0 | T3 (formal-series setup partial; same content) |
| EXTENDED | 5 | 6 | +1 | T1, T2, T3 (scope), T4, T5, T7 + **T6 (newly EXTENDED)** |
| SUPERSEDED | 1 | 1 | 0 | T9 |
| PARALLEL | 2 | 1 | −1 | **T8 only** (T6 reclassified) |
| DEFER (legacy 072 v1 secondary label on 6 refs) | 6 | 0 | −6 | (all six §-level resolved; see "072 D4 RESOLVED" annotations above) |

**Net delta vs 072 v1:** T6 promoted from PARALLEL to EXTENDED on
the strength of BT §5 (13 a) `[CHART-MAP-CANDIDATE-B1]` substrate
(SUBSTRATE-INVENTORY observation; not a closure assertion). T6
reclassification is the single label-change introduced by 073's
verbatim readthrough.

The 6 of 9 DEFER markers from 072 v1 are now all RESOLVED at §-level
granularity:

| Adams ID | 072 v1 secondary DEFER reason | 073 v2 §-level resolution |
| --- | --- | --- |
| T1 | "BT-side §-level granularity unknown for §§5+9 split" | §6 (eq. 2) for left-product + §5 Theorem I for proper-solution conclusion |
| T2 | "BT-side §-level granularity unknown for §§5+9 + p. 5 quadrant remark" | §5 Theorem I + BT 1933 p. 5 quadrant-symmetry remark |
| T4 | "BT-side §-level granularity unknown for §§3+6 split" | §6 Lemma 9 (1 a) + Q-factorability (Def. 8; §1) |
| T5 | "BT-side §-level granularity unknown for §§5+7+9 split" | §5 Theorem I (T2) + §6 Lemma 9 (T3) |
| T7 | "BT-side §-level granularity unknown for §§5+7 split" | §5 (4 a) + B'-curves (2) |
| T9 | "BT-side §-level granularity unknown for §9 attribution" | §6 Lemma 9 (T3) + §§7-9 Fundamental Existence Theorem (out-of-scope; natural follow-up) |

All 6 DEFER → RESOLVED transitions are based on the verbatim 073
readthrough's §-level mapping. **072 D4 is now closed for §§4-6
content.** The remaining unfinished cross-walk item is the §§7-9
verbatim readthrough, which is recorded as a residual in
`sectorial_upgrade_gap_status_v2_with_bt_4_6.md` §5 item 4.

## Substrate-inventory caveat

This ladder map is a **SUBSTRATE-INVENTORY observation** of the
content-overlap structure between Adams 1928 and BT 1933 §§4-6. It
is **NOT** an assertion that:

- the SIARC-stratum sectorial-upgrade gap is closed by Adams + BT
  §§4-6 alone, or
- the §-level mappings discharge any specific 069r1 R1 (chart-map)
  closure obligation, or
- D2-NOTE v2.1's BT-citation argument is substantiated or refuted by
  the §-level mapping.

These are all W21 LANE-1 Phase 3 synthesizer-arbitration questions.
The 073 ladder map is purely a structural cross-walk over
Adams + BT §§4-6 substrate.
