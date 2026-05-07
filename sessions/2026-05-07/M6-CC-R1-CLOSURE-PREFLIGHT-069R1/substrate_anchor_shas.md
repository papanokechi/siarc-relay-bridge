# Substrate anchor SHAs (071 M6-CC-R1-CLOSURE-PREFLIGHT-069R1)

**Session:** 071
**Date:** 2026-05-07
**Bridge HEAD at fire time:** `f65fe6c`

This file aggregates SHA-anchored substrate citations for 071 deliverables. All cited 058R + 069 + 070 deliverables, spec body, and slot anchors are pinned by SHA-256 prefix.

---

## A. 058R fire deposit (LANDED substrate)

Path: `sessions/2026-05-06/CC-VQUAD-PIII-NORMALIZATION-MAP-RERE-FIRE/`

| file                                  | SHA-256 prefix          | role in 071                                       |
|---------------------------------------|-------------------------|---------------------------------------------------|
| `handoff.md`                          | `AF88F99387D89758..`    | 058R verdict UPGRADE_V1_0_PARTIAL_NUMERICAL anchor |
| `phase_a_birkhoff_match.md`           | `413A3845F67E7166..`    | V_quad H4 substrate verbatim citation             |
| `phase_a_birkhoff_match.py`           | `7B4DD7636A3D9AD3..`    | $|C_{V}|$ provenance (≥ 108 dps); V_quad ODE form |
| `phase_b_canonical_map.md`            | `F831F9BD58D1F306..`    | M = Φ_symp ∘ Φ_shift ∘ Φ_resc; λ = 1/3, t_0 = -4√3; **L136-140 R1-residual statement** |
| `phase_b5_affine_weyl_crosswalk.md`   | `B9D4FFD2F279A33C..`    | KNY P_III equation-coefficients $(\alpha, \beta, \gamma, \delta)$ at L88-89 (NOT four-tuple) |
| `phase_c_literature_verification.md`  | `F698415C42782972..`    | slot 07 + slot 08 anchor SHA records              |
| `phase_d_verdict.md`                  | `025E36722BBF3A12..`    | residual R1 description                           |
| `cc_note_v1.tex`                      | `9C1649DCC51C9E02..`    | structural M6.CC closure note                     |
| `claims.jsonl` (25 entries)           | `0984F096B20577BF..`    | inherited AEAL claims                             |

---

## B. 069 fire deposit (LANDED substrate)

Path: `sessions/2026-05-07/CC-VQUAD-PIII-NORMALIZATION-MAP-PHASE-D-NUMERICAL/`

| file                                  | SHA-256 prefix          | size       | role in 071                                       |
|---------------------------------------|-------------------------|------------|---------------------------------------------------|
| `handoff.md`                          | `3534D6C8CBB0F4BD..`    | 15 795 B   | 069 PERSIST verdict + 069-D1 single-bottleneck observation + recommended-next-step P1 verbatim quote (L78-83) |
| `phase_0_readback.md`                 | `61D6935BF9063977..`    | 11 829 B   | 069 supersession-gate readback                    |
| `phase_b5_prelanded_drift_guard.md`   | `686632A08FDB9291..`    | 5 034 B    | B.5 PRE-LANDED drift guard                        |
| `phase_d_numerical.md`                | `E98D74EBD30EB43C..`    | 17 058 B   | **Liouville invariant $I_{V}(z) = (3 z^{2}+5 z-3)/(9 z^{3})$ §2; KNY linear relation $a_{0}+a_{1}=1$ §1; CT v1.3 four-tuple $(1/6, 0, 0, -1/2)$ §1** |
| `phase_d_numerical.py`                | `89D9EEFC57D9FA47..`    | 16 488 B   | sympy-derivation of Liouville invariant            |
| `phase_d_numerical.log`               | `73F355991E1FE441..`    | 7 197 B    | Liouville invariant printed at run-time           |
| `substrate_anchor_shas.md`            | `E45902293EB6796C..`    | 8 719 B    | 069 substrate-anchor table; **slot 07 SHA recorded `65294fbc..`** |
| `forbidden_verb_scan.md`              | `7681228FD03C8AA1..`    | 7 831 B    | 069 self-check pattern (template for 071 STEP E)  |
| `claims.jsonl` (13 NEW entries)       | `C2C99CE425E4AFC3..`    | 7 940 B    | inherited AEAL claims                             |
| `halt_log.json`                       | `321922DD466218B9..`    | 3 588 B    | 069 halt record                                   |
| `discrepancy_log.json`                | `06871E83157013C9..`    | 5 460 B    | 069 anomalies D1-D2-D3-D4 carry-forward            |
| `unexpected_finds.json`               | `6AE1A9A9C56777B7..`    | 2 483 B    | 069 unexpected finds                              |

---

## C. 070 PREFLIGHT deposit (LANDED substrate)

Path: `sessions/2026-05-07/PICTURE-V120-LATE-FIRE-PREFLIGHT-070/`

| file                                  | SHA-256 prefix          | role in 071                                       |
|---------------------------------------|-------------------------|---------------------------------------------------|
| `handoff.md`                          | `0FCAB0A4E74D6070..`    | GO_PRIMARY_ONLY verdict + OQ-069-R1 forward-pointer (FIXED ENTRY TEMPLATE pattern); v1.20 scope-frozen anchor |

Bridge HEAD `f65fe6c` is the LANDED commit for 070.

Operator decision `027d7ff` (item (d) "LATE-FIRE post-W20 picture v1.20 chosen by operator (substrate scope frozen)"): cited as basis for HALT_071_SCOPE_CREEP_INTO_V120 self-check.

---

## D. Spec body (cited but not re-fired)

| anchor                             | SHA-256 prefix          | size       | LC      |
|------------------------------------|-------------------------|------------|---------|
| `prompt_spec.md` (CC-VQUAD-PIII)   | `BE3F8FE9D0857E29..`    | 52 197 B   | 1089    |

Path: `sessions/2026-05-04/CC-VQUAD-PIII-NORMALIZATION-MAP-PROMPT-SPEC/prompt_spec.md`.

---

## E. Slot anchor PDFs (per spec §1)

| slot   | filename                                                | recorded SHA | observed SHA prefix      | role in 071                                       |
|--------|---------------------------------------------------------|--------------|--------------------------|---------------------------------------------------|
| 07     | `07_okamoto_1987_painleve_III_FE30.pdf`                 | `65294fbc..` | `65294FBCA97E3CE1..`     | PRIMARY for path β; verbatim ≤ 30-word quote of eq. (3.1) extracted from text-extract `07_okamoto_1987_painleve_III_FE30.txt` L1816-L1825 |
| KNY 2017 §8.5.17 | `g3b_2026-05-03 KNY 2017 PDF`                 | (slot anchor; CARRY-FORWARD per QA REC #6) | not re-extracted in 071 | KNY linear relation $a_{0}+a_{1}=1$ cited via 069 `phase_d_numerical.md` SHA `E98D74EBD30EB43C..` only |
| 08     | BLMP 2024 §4.28                                         | `96c49cdd..` | (CARRY-FORWARD; not re-extracted in 071) | cited via 058R Phase B + 069 Phase D.2.d structurally |

Slot 07 PDF SHA observed `65294FBCA97E3CE1..` matches recorded `65294fbc..` PASS.

---

## F. CT v1.3 §3.5 (algebraic identity)

Path: `sessions/2026-05-02/CHANNEL-THEORY-V13-RELEASE/channel_theory_outline.tex` L~680-820.

CT v1.3 §3.5 four-tuple $(\alpha_{\infty}, \alpha_{0}, \beta_{\infty}, \beta_{0}) = (1/6, 0, 0, -1/2)$ cited via 069 `phase_d_numerical.md` §1 SHA `E98D74EBD30EB43C..` (carry-forward; not re-extracted in 071).

---

## G. V_quad Liouville invariant (NEW from 069)

$$I_{V}(z) \;=\; \frac{3 z^{2} + 5 z - 3}{9\, z^{3}}.$$

Source: 069 `phase_d_numerical.md` §2 sympy-derived; cited at 069 `phase_d_numerical.py` SHA `89D9EEFC57D9FA47..`. Re-derived independently in 071 `phase_a_path_alpha.py` STEP 3 and `phase_b_path_beta.py` STEP B.1.cont (anti-circularity rule); both re-derivations sympy-match the 069 anchor (difference = 0).

---

## H. Citation differentiation (per QA REC #6 — single policy)

### Verbatim-quote slots (re-extracted from PDFs in this session where ≤ 30 words; SHA confirmed at fire time)

| slot   | quote source                                | length    | location in 071 deliverable    |
|--------|---------------------------------------------|-----------|--------------------------------|
| 07     | Okamoto 1987 §3 eq. (3.1)                   | 17 words  | `phase_b_path_beta.md` §1; `phase_b_path_beta.py` `OKAMOTO_3_1_QUOTE` constant |

### Carry-forward slots (NOT re-extracted in 071; cited via 058R + 069 SHA)

| slot                              | citation channel                                     |
|-----------------------------------|------------------------------------------------------|
| KNY 2017 §8.5.17 (Lax pair, $a_{0}+a_{1}=1$, chart) | via 069 `phase_d_numerical.md` §1 SHA `E98D74EBD30EB43C..` |
| Birkhoff-Trjitzinsky 1933 (slot 03)| via 058R `phase_a_birkhoff_match.md` SHA `413A3845F67E7166..` |
| Wasow 1965 (slot 04)              | via D2-NOTE v2.1 convention; 058R Phase A            |
| Costin 2008 ch. 5 (slot 06)       | via 058R Phase A + B substrate                       |
| BLMP 2024 §4.28 (slot 08)         | via 058R Phase B + 069 Phase D.2.d structurally      |
| V_quad H4 substrate (108 dps from 051) | via 058R Phase A SHA `7B4DD7636A3D9AD3..`        |

End of `substrate_anchor_shas.md`.
