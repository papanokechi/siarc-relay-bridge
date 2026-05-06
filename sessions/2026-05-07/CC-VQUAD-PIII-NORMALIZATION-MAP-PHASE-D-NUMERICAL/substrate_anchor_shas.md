# Substrate anchor SHAs (rule5 grounding)

**Session:** 069 CC-VQUAD-PIII-NORMALIZATION-MAP-PHASE-D-NUMERICAL
**Purpose:** SHA-anchor every cited 058R deliverable + spec body + B.5 PRE-LANDED bridges + slot anchors + KNY 2017 PDF, per envelope D10 (rule5 grounding).

---

## §1 — 058R fire deposit (read-only-cited; do NOT modify)

Path: `siarc-relay-bridge/sessions/2026-05-06/CC-VQUAD-PIII-NORMALIZATION-MAP-RERE-FIRE/`

| file                                | SHA-256 prefix      | size (B) | role                             |
|-------------------------------------|---------------------|----------|----------------------------------|
| handoff.md                          | AF88F99387D89758..  |  13 149  | 058R verdict + recommendation    |
| phase_a_birkhoff_match.md           | 413A3845F67E7166..  |   5 587  | Phase A V_quad ODE substrate    |
| phase_a_birkhoff_match.py           | 7B4DD7636A3D9AD3..  |   5 233  | Phase A re-derivation script    |
| phase_b_canonical_map.md            | F831F9BD58D1F306..  |  10 635  | Phase B M = Φ_symp ∘ Φ_shift ∘ Φ_resc |
| phase_b5_affine_weyl_crosswalk.md   | B9D4FFD2F279A33C..  |   9 699  | Phase B.5 INCLUSION cross-walk  |
| phase_c_literature_verification.md  | F698415C42782972..  |   9 247  | Phase C 5/5 anchor PASS         |
| phase_d_verdict.md                  | 025E36722BBF3A12..  |  10 331  | 058R verdict body               |
| cc_note_v1.tex                      | 9C1649DCC51C9E02..  |   5 579  | Phase E outline (NOT BUILT)     |
| claims.jsonl                        | 0984F096B20577BF..  |  14 256  | 058R 25-claim ledger            |

All 9 SHAs verified at 069 fire time (Phase 0 STEP 0.1; see `phase_0_readback.md`).

---

## §2 — Spec body (cited at SHA; not re-fired)

Path: `siarc-relay-bridge/sessions/2026-05-04/CC-VQUAD-PIII-NORMALIZATION-MAP-PROMPT-SPEC/prompt_spec.md`

* full SHA-256: `BE3F8FE9D0857E2916452A8E5E6102B73F195B0E177457A077372CB6EF6E3319`
* envelope-recorded prefix: `BE3F8FE9D0857E29..`
* size: 52 197 B / 1089 lines

---

## §3 — Phase B.5 PRE-LANDED bridges (cited via 058R verbatim quote + 069 drift guard)

| commit     | session                                  | role                                               |
|------------|------------------------------------------|----------------------------------------------------|
| `a9d34fd`  | SIARC-PRIMARY-W-HOMOMORPHISM-DERIVATION  | Injective $\varphi: W^{\mathrm{aff}}(B_2) \hookrightarrow \mathrm{Aut}(D_6^{(1)}) \ltimes W((2A_1)^{(1)})$ |
| `95ffa1e`  | SIARC-OKAMOTO-1987-SEC3-SCAN             | Cokernel $\mathbb{Z}/2 = P^{\vee}(B_2)/Q^{\vee}(B_2)$ identified concretely |
| `f8099b4`  | spec v1.1 amendment block                | 7-patch absorption of 033 verdict into spec body  |

069 deliverable `phase_b5_prelanded_drift_guard.md` reproduces 4 verbatim fragments from `non_promotion_index2_final.md` at the 036 bridge, satisfying envelope D8.

---

## §4 — M4-closure context (068 commit)

| commit     | session                              | role                                |
|------------|--------------------------------------|-------------------------------------|
| `e7bfe49`  | T1-PHASE-3-COSTIN-BORDERLINE-M4-CLOSURE-068 | M4 closure attempt; bridge HEAD |

This commit is the bridge HEAD at 069 fire time. 068 LANDED M4-closure-relevant verdict at this commit; 069 re-fires Phase D.2 of M6.CC against this HEAD.

---

## §5 — 057 preflight context

| commit     | session                              | role                                    |
|------------|--------------------------------------|-----------------------------------------|
| `9d6e801`  | CC-VQUAD-PIII-LITERATURE-PREFLIGHT   | 058 prerequisites GO; 16/16 SHA PASS    |

---

## §6 — Slot anchors (Phase C literature substrate; SHA prefix verified at 057 preflight)

Path: `siarc-relay-bridge/anchors/cc_vquad_piii_normalization_map/`

| slot | filename                                                | SHA-256 prefix |
|------|---------------------------------------------------------|----------------|
| 01   | `01_birkhoff_1930_acta54.pdf`                          | aeb5291e..     |
| 03   | `03_birkhoff_trjitzinsky_1933_acta60.pdf`              | dcd7e3c6..     |
| 04   | `04_wasow_1965_dover.pdf`                              | f59d6835..     |
| 06   | `06_costin_2008_chap5.pdf`                             | 436c6c11..     |
| 07   | `07_okamoto_1987_painleve_III_FE30.pdf`                | 65294fbc..     |
| 08   | `08_barhoumi_lisovyy_miller_prokhorov_2024_pIII_D6.pdf` | 96c49cdd..     |

All 6 PRIMARY anchor SHAs verified at 057 preflight (slot_sha_verification.md, all PASS), inherited at 058 + 058R + 069.

KNY 2017 §8.5.17 PDF: slot anchor `g3b_2026-05-03 KNY 2017 PDF` (auxiliary slot 14; verified at 058R Phase C; cited in 069 deliverables for §8.5.17 eq. 8.237–8.239 as the actual 2×2 Lax pair source per envelope V1.2.D4).

---

## §7 — H4 measurement (V_quad-native Stokes amplitude substrate)

Path: `siarc-relay-bridge/sessions/2026-05-02/CC-MEDIAN-RESURGENCE-EXECUTE/S_zeta_star_digits.txt`

* `|C_V| = 8.127336795495072367112578732...` at ≥ 108 digits
* `β = 2.18803285172899266083291260384e-108` (i.e. β = 0 to ≥ 107 digits)
* `|ζ_*| = 4/√3 = 2.30940107675850305803659512201...` (sympy-derived from $3 C_V^{2} - 4 = 0$; 058R Phase A re-verified at ≥ 30 dps)

058R Phase A re-derived these quantities at fresh hash; bit-identical to 2026-05-02 partial session.

---

## §8 — CT v1.3 §3.5 (algebraic identity)

Path: `siarc-relay-bridge/sessions/2026-05-02/CHANNEL-THEORY-V13-RELEASE/channel_theory_outline.tex` L~680–820

Records the algebraic identity $V_{\mathrm{quad}} \leftrightarrow P_{III}(D_{6})$ at "Painlevé-class level only", flagging the canonical-form normalisation map as a residual of `op:cc-formal-borel`. The CT v1.3 §3.5 four-tuple $(\alpha_{\infty}, \alpha_{0}, \beta_{\infty}, \beta_{0}) = (1/6, 0, 0, -1/2)$ is the V_quad-side parameter input; its Okamoto null-sum violation ($-1/3 \neq 0$) is anomaly D2 (carry-forward from 2026-05-02 partial through 058R into 069).

---

## §9 — Bridge HEAD lineage anchors (envelope-recorded)

| commit    | role                                                                            |
|-----------|---------------------------------------------------------------------------------|
| `a9d34fd` | 033 SIARC-PRIMARY-W-HOMOMORPHISM (B.5 PRE-LANDED)                              |
| `95ffa1e` | 036 OKAMOTO-1987-SEC3-SCAN (B.5 PRE-LANDED; cokernel identification)           |
| `f8099b4` | spec v1.1 amendment block                                                       |
| `9d6e801` | 058R fire substrate                                                             |
| `e7bfe49` | 068 M4-closure (envelope HEAD anchor; current HEAD at 069 fire time)           |

Phase 0 STEP 0.6 verified: all 5 ancestors PRESENT in HEAD lineage.

---

## §10 — 069 deliverables (this session; for Phase F handoff Files-committed table)

Path: `siarc-relay-bridge/sessions/2026-05-07/CC-VQUAD-PIII-NORMALIZATION-MAP-PHASE-D-NUMERICAL/`

(SHA-256 prefixes computed by `B1 — Collect deliverables` step at deposit time.)

| file                                  | role                                                |
|---------------------------------------|-----------------------------------------------------|
| phase_0_readback.md                   | Phase 0 supersession-gate readback                  |
| phase_b5_prelanded_drift_guard.md     | B.5 PRE-LANDED exact-quote drift guard              |
| phase_d_numerical.md                  | Primary D.2 write-up                                |
| phase_d_numerical.py                  | Sympy + mpmath runner                               |
| phase_d_numerical.log                 | Full run log                                        |
| substrate_anchor_shas.md              | This file                                           |
| forbidden_verb_scan.md                | Self-check audit                                    |
| claims.jsonl                          | ≥ 12 NEW AEAL entries                              |
| halt_log.json                         | (Empty `{}` if no halt fired)                       |
| discrepancy_log.json                  | Anomalies surfaced                                  |
| unexpected_finds.json                 | Unexpected finds                                    |
| handoff.md                            | Per spec §6 + envelope                              |

End substrate anchor SHA list.
