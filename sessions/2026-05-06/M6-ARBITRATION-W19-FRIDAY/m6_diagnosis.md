# m6_diagnosis.md

> **Task:** M6-ARBITRATION-W19-FRIDAY (relay 047)
> **Date:** 2026-05-06 (UTC)
> **Inputs:** `m6_substrate_manifest.json`, `m6_substrate_extracts.md`,
> `m6_reconciliation_matrix.json`.
> **Output of this file:** decision among {D1, D2, D3, D4} (relay-047
> §STEP 4 candidate diagnoses), plus a fifth subsidiary classification
> (D5) for a calendar-date typo unrelated to the M6 substantive
> discrepancy.

---

## D1 — split definition (both sources correct under different definitions)

**Hypothesis:** S1's "M6 ✅" caveat-profile token and S2/S3/S4/S6/S11's
"Phase A or B.5 partial / PENDING ARBITRATION" status both refer to a
real, well-defined component of M6, but to **different components**.
Specifically:

- **M6.H4 (alien-amplitude leg).** Defined operationally by Prompt 005
  (`op:cc-median-resurgence-execute`). The closure criterion is the
  `H4_EXECUTED_PASS_108_DIGITS` verdict (cross-method Stokes-amplitude
  agreement to ≥108 digits via three independent extractors).
  **Status:** ✅ DONE 2026-05-02. **Anchored at:** §S6d (picture v1.18
  L363, "**M6 is achieved** with substantial precision margin"); §S6e
  row 005 ("M6 | ✅ DONE 2026-05-02"); §S6f P-CC row ("**STOKES-SIDE
  NUMERICALLY CONFIRMED at 108 digits 2026-05-02**").

- **M6.CC (canonical-form leg).** Defined operationally by the
  CC-VQUAD-PIII-NORMALIZATION-MAP `prompt_spec.md` (§S7), with phases
  0.0 / 0.5 / A / B / B.5 / C / D / E / F. The closure criterion is the
  `UPGRADE_V1_0_FULL` (or `UPGRADE_V1_0_PARTIAL_NUMERICAL`) verdict of
  that spec's Phase D. **Status:** 🟡 PARTIAL — Phase A not yet executed
  (spec drafted, awaiting CLI dispatch); Phase B Φ_resc + Φ_shift pinned
  (Prompt 009, 2026-05-02), Φ_symp residual; Phase B.5 = SIARC-primary
  derivation produced INDEX-2 EMBEDDING verdict 2026-05-04 (§S8a)
  pending operator+Claude pivot review per §S8b; Phases C-F not yet
  executed. **Anchored at:** §S6a (picture v1.18 L42 "Phase B.5 W
  cross-walk **STILL_PARTIAL_PENDING_PIVOT_DECISION**"); §S6e rows
  009 ("🟡 PARTIAL 2026-05-02") and 015 ("✅ DRAFTED 2026-05-02; **GATED
  on R5**"); §S7a (spec L91-98 verdict ladder); §S8a (SIARC-PRIMARY
  CLOSED at INDEX-2 EMBEDDING grade, pending pivot review).

**Substrate cross-walk to candidate definitions:**

| Substrate | Reads "M6" as | Status under that reading |
|-----------|---------------|---------------------------|
| S1 (038)  | M6.H4 (caveat-profile token in M9-announcement format note) | ✅ DONE |
| S2 (WSB)  | M6.CC (CC-VQUAD-PIII-NORMALIZATION-MAP, "M6 leg, gates SIARC-MASTER-V0") | 🟡 PARTIAL (Phase A or B.5 still firable) |
| S3 (W19 master) | M6.CC (dispatch-block uses prompt_spec.md S7) | 🟡 PARTIAL |
| S4 (Day-2 cli_log) | both — gating clause uses M6 (resolves to .CC per S7 L93); inconsistency flag uses M6 ✅ token (S1.H4 reading) | mixed; flag itself recognises the unresolved overload |
| S5 (CMB) | both — F4 audit row treats "M6 closure" as a gate-feeding precondition (S5a/S5b), no leg specified | unresolved at CMB level |
| S6 (picture v1.18) | both, **explicitly**: row 005 "✅ DONE" tagged M6.H4, row 009/015 + Phase-B.5 row tagged M6.CC | dual-status co-residence inside a single picture-grade substrate |
| S7 (CC-VQUAD spec) | M6.CC (defines M9-gating clause via `UPGRADE_V1_0_FULL` outcome) | not-yet-fired |
| S8 (SIARC-PRIMARY) | M6.CC Phase B.5 (one sub-leg) | CLOSED at INDEX-2 EMBEDDING grade pending pivot review |
| S9/S10 (Sakai/NY)  | M6.CC Phase B.5 anchor | both PARTIAL |
| S11 (045 §7) | both — the §-title is "M6 ✅-vs-Phase-A/B.5 status"; flags inconsistency between the two readings | PENDING ARBITRATION |
| S12 (M9 audit) | M6.CC (gate-feeding into M9 main-theorem) | SOFT precondition |

**Decisive evidence:** §S6e (picture v1.18 prompt-table) places
`M6 | ✅ DONE` against row 005 AND `M6 | 🟡 PARTIAL` against row 009 AND
`M6 (canonical-form full closure) | DRAFTED-GATED` against row 015 in
the **same authoritative substrate document, in adjacent rows**.
Picture v1.18 itself is the witness that M6 is operatively split
inside the project's own ground-truth file. Therefore D1 is
substrate-supported.

**Verdict on D1:** **HOLDS.**

---

## D2 — 038 caveat-profile is stale (predates a spec change)

**Hypothesis:** 038 was authored with an earlier, looser definition of
M6 (just M6.H4) and a later definition (M6 = bundle including M6.CC)
became operative without 038 being updated.

**Evidence for / against:**

- 038 is dated 2026-05-04 (mtime), the **same day** as picture v1.18
  publish (2026-05-04 17:00 JST), the SIARC-PRIMARY commit (16:12 JST),
  and the CC-VQUAD spec deposit (5e2ad95). 038's M6 token therefore
  cannot be "predates a spec change" in the temporal sense — the spec
  and 038 were drafted within the same ~24h window.
- The closer reading is that 038 used "M6 ✅" in shorthand, alongside
  M1/M2/M3/M5/M8 ✅, as a **structural-fit pattern token** for the M9
  announcement caveat profile (UF-038-3) rather than as a tracked
  milestone-state declaration. 038's section-header is "Sakai 1999 slot
  13 is a strong structural-fit precedent for SIARC M9 announcement
  format" — the bullet is about announcement *format*, not milestone
  *state*.

**Verdict on D2:** **DOES NOT HOLD as the primary cause.** 038 is not
substantively stale; its M6 token is merely shorthand inside an
announcement-format pattern-match note. (D1 already absorbs this
nuance: the announcement-pattern token is M6.H4 as a one-character
shorthand, while the ground-truth state is dual-leg.) D2 may be
re-raised if the spec-amendment recommendation (§"Spec-rollback or
spec-amendment recommendation" of `m6_verdict.md`) is rejected and the
project decides to retire the H4-only M6 token.

---

## D3 — WSB is over-scoped (added W cross-walk to M6 spec without dispatching arbitration)

**Hypothesis:** S2/S3 W19 WSB and master prompt added the W cross-walk
(B.5 leg) into M6 without the synthesizer first arbitrating whether
B.5 belongs in M6 or in a new M6.5 / M6′ milestone.

**Evidence for / against:**

- The CC-VQUAD-PIII-NORMALIZATION-MAP `prompt_spec.md` (§S7) was
  drafted on 2026-05-04 by the prior synthesizer, **before** W19 began.
  Phase B.5 is in §S7 verbatim ("PHASE B.5 — B_2 ↔ D_6 affine-Weyl
  cross-walk (mandatory pre-step before Phase B canonical-map
  construction)"). The WSB inherited the spec's Phase B.5 — it did not
  add it.
- The Q35 ruling in picture v1.18 §S6 explicitly authorised Phase B.5
  as a sub-task of M6 spec (sub-tasks B.5.1–B.5.4 explicit per Q35
  mandatory-pre-step ruling). Q35 is operator-side ruling, not
  WSB-side.

**Verdict on D3:** **DOES NOT HOLD.** Phase B.5 was in the spec before
WSB existed, ruled into M6 scope by Q35, and inherited verbatim by the
WSB.

---

## D4 — Both wrong (a third source has the operative state)

**Hypothesis:** A third source — bridge handoff or picture-grade file
— has the operative M6 state and neither 038 nor WSB caught up.

**Evidence for / against:**

- Picture v1.18 (§S6) is the closest candidate for "third source", and
  it does carry the operative dual-leg status. But picture v1.18
  **does not contradict** either 038 or the WSB — it absorbs both
  readings (S6e row 005 M6.H4 ✅, S6e row 009/015 + S6a Phase B.5
  M6.CC PARTIAL). 038 is a substring of picture v1.18's row-005
  reading; the WSB is a substring of picture v1.18's row-009/015 +
  Phase-B.5 reading.
- Therefore there is no third source that **contradicts** the SIARC
  framework's existing M6 treatment. The HALT_047_M6_REQUIRES_E2 gate
  (which would trigger if a third source contradicted PCF-1 v1.3 / T2B
  v3.1 / CT v1.3 / umbrella v2.0) does **not fire**.

**Verdict on D4:** **DOES NOT HOLD as the primary cause.** Picture
v1.18 is the operative third source, but it absorbs rather than
contradicts; D1 is the cleaner diagnosis.

---

## D5 — calendar-date typo (subsidiary, non-substantive)

**Hypothesis:** WSB §S2d row reads `Fri | 05-09` for the M6 Friday
slot, while calendar Fri W19 is 2026-05-08; relay 047 itself cites Fri
2026-05-08 in the prompt body.

**Evidence:** May 1 2026 is a Friday; W19 = 2026-05-04 to 2026-05-10;
hence Fri W19 = 2026-05-08. WSB L78 internal date is off-by-one.

**Verdict on D5:** **HOLDS as a separate, non-substantive WSB-internal
typo.** Logged in `discrepancy_log.json` as D5 separate from the M6
substantive discrepancy. This subsidiary holds whether or not D1
holds, and is independent of the M6 verdict.

---

## Decision

**D1 holds.** D2/D3/D4 ruled out as primary cause. D5 holds as a
separate non-substantive WSB date typo.

The diagnosis branch label for the C2 AEAL claim is `D1`.

The verdict in `m6_verdict.md` is therefore a **definitional split
verdict**: M6.H4 ✅ DONE 2026-05-02; M6.CC 🟡 PARTIAL (with phase-level
breakdown and the SIARC-primary INDEX-2 EMBEDDING qualifier on
Phase B.5).

---

## End of m6_diagnosis.md
