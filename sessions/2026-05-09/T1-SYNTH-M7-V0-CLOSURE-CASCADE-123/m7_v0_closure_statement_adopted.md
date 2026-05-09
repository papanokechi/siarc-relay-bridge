# M7 V0 Closure Statement (Adopted) — Canonical Source-of-Record

**Adopted at**: T1-SYNTH-M7-V0-CLOSURE-CASCADE-123 (2026-05-09)
**Source**: R1 §5 verbatim (full math-mode template §4 wording); corroborated by R2 §5 (substantively identical compressed variant)
**Cascade verdict**: `RATIFY_WITH_AMENDMENT` × 2 independent T1-Synth reviewers (R1: MEDIUM-HIGH; R2: HIGH)
**Aggregated confidence band**: MEDIUM-HIGH (most-conservative dual-reviewer aggregation)
**Annotation**: `(SOFT-BRANCH; HARD-BRANCH-PENDING)`
**Mirror anchor**: M4 V0 cascade `(MEDIUM-HIGH; HIGH-PENDING)` annotation pattern (sessions/2026-05-08/M4-V0-CLOSURE-CASCADE-106/)

---

## Operative closure text (LaTeX math-mode; suitable for manuscript inclusion)

M7 V0 CLOSED in the soft branch via the j=0 Chowla–Selberg PSLQ-exhaustion mechanism (Prompt 014 verdict PASS\_A\_EQ\_6\_ONLY). Max $|\delta_\text{lin}| = 3.09 \times 10^{-23}$ across 4 j=0 cubic families (Q\_30..Q\_33, dps=25000, $N$ up to 1200, 11-param LIN refit at $K_\text{FIT}=7$) clears the $10^{-15}$ minimum target with 8+ orders of margin; PSLQ on the 17-member deduplicated H6 Chowla–Selberg basis B19+ at maxcoeff $=10^{50}$ / tol $=10^{-40}$ returns no $\Gamma(1/3)$ relation in any of the 4 families. The closure runs in the deduplicated basis (NOT the literal 18-basis, which contains the $\mathbb{Q}$-redundant pair $\{\sqrt{3}, \Gamma(1/3)\Gamma(2/3)/(2\pi)\}$ via gamma-reflection; running PSLQ on the literal basis returns the trivial relation $1\cdot\sqrt{3} - 3\cdot\mathrm{CS}_{\sqrt{3}} = 0$ with target coefficient $= 0$, NOT a Chowla–Selberg signal). Q23 PSLQ basis hygiene rule forward-pointed.

Closure is at the algebraic-combinatorial level (deep-WKB amplitude refit on saved cf\_value series, no new high-dps mpmath generation needed for the soft-branch result). Hard-branch stretch goal $|\delta| < 10^{-30}$ NOT achieved; would require $K_\text{FIT}=9$ on extended series at $N \le 2400$ / dps $\ge 44{,}300$ (Q22 path-(b), forward-pointed not-blocking).

PCF-2 v1.4 §6 amendment drafted as Phase F output of Prompt 014; Zenodo deposit step TABLED under RULE 1 (admin/distribution deferred until M1–M12 math-foundational closure complete); math-content amendment in scope.

No halt conditions triggered (12 AEAL claims ledgered; halt log carries verdict + summary; discrepancy log records $K_\text{FIT}$ judgment + Phase E precision impedance; unexpected\_finds records PSLQ trivial-relation flag in literal basis).

Confidence: SOFT-BRANCH. HARD-BRANCH reserved for post-$K_\text{FIT}=9$ hard-branch refit at extended series. Picture-chain v1.20+ M7\_V0\_CLOSED tag should annotate `(SOFT-BRANCH; HARD-BRANCH-PENDING)` to prevent silent inheritance of unqualified closure state.

---

## Compact short-form (for index tables / single-row summaries)

> **M7 V0 CLOSED (SOFT-BRANCH; HARD-BRANCH-PENDING)** — j=0 Chowla–Selberg PSLQ-exhaustion via Prompt 014 PASS\_A\_EQ\_6\_ONLY at max $|\delta| = 3.09 \times 10^{-23}$ across 4 j=0 cubic families; no $\Gamma(1/3)$ relation in 17-member dedup H6 B19+ basis. Hard-branch ($|\delta| < 10^{-30}$, $K_\text{FIT}=9$, $N\le 2400$, dps$\ge 44{,}300$) forward-pointed not-blocking. Cascade: 121→122→123 dual-reviewer @ MEDIUM-HIGH.

---

## Plain-text variant (for non-math-mode contexts)

M7 V0 CLOSED in the soft branch via the j=0 Chowla-Selberg PSLQ-exhaustion mechanism (Prompt 014 verdict PASS_A_EQ_6_ONLY). Max |delta_lin| = 3.09e-23 across 4 j=0 cubic families (Q_30..Q_33, dps=25000, N up to 1200, 11-param LIN refit at K_FIT=7) clears the 1e-15 minimum target with 8+ orders of margin; PSLQ on the 17-member deduplicated H6 Chowla-Selberg basis B19+ at maxcoeff=1e50 / tol=1e-40 returns no Gamma(1/3) relation in any of the 4 families. The closure runs in the deduplicated basis (NOT the literal 18-basis, which contains the Q-redundant pair {sqrt(3), Gamma(1/3)Gamma(2/3)/(2pi)} via gamma-reflection; running PSLQ on the literal basis returns the trivial relation 1*sqrt(3) - 3*CS_sqrt3 = 0 with target coefficient = 0, NOT a Chowla-Selberg signal). Q23 PSLQ basis hygiene rule forward-pointed.

Closure is at the algebraic-combinatorial level (deep-WKB amplitude refit on saved cf_value series, no new high-dps mpmath generation needed for the soft-branch result). Hard-branch stretch goal |delta| < 1e-30 NOT achieved; would require K_FIT=9 on extended series at N up to 2400 / dps >= 44300 (Q22 path-(b), forward-pointed not-blocking).

PCF-2 v1.4 §6 amendment drafted as Phase F output of Prompt 014; Zenodo deposit step TABLED under RULE 1 (admin/distribution deferred until M1-M12 math-foundational closure complete); math-content amendment in scope.

No halt conditions triggered (12 AEAL claims ledgered; halt log carries verdict + summary; discrepancy log records K_FIT judgment + Phase E precision impedance; unexpected_finds records PSLQ trivial-relation flag in literal basis).

Confidence: SOFT-BRANCH. HARD-BRANCH reserved for post-K_FIT=9 hard-branch refit at extended series. Picture-chain v1.20+ M7_V0_CLOSED tag should annotate (SOFT-BRANCH; HARD-BRANCH-PENDING) to prevent silent inheritance of unqualified closure state.

---

## Provenance & SHA grounding

| Element | Source SHA / Path | Verified |
|---|---|:---:|
| Numerical max $\|\delta_\text{lin}\| = 3.09 \times 10^{-23}$ | Prompt 014 handoff.md (bridge `e857172`) | ✅ |
| 11-param LIN refit at $K_\text{FIT}=7$ | Prompt 014 handoff.md "Judgment calls #1" (bridge `e857172`) | ✅ |
| 17-member dedup H6 B19+ basis | Prompt 014 `pslq_results.json` + handoff.md "Judgment calls #2" (bridge `e857172`) | ✅ |
| Q22 hard-branch path | Prompt 014 handoff.md "Judgment calls #3" (bridge `e857172`) | ✅ |
| Q23 PSLQ basis hygiene rule | Prompt 014 `unexpected_finds.json` (bridge `e857172`) | ✅ |
| `(SOFT-BRANCH; HARD-BRANCH-PENDING)` annotation pattern | M4 V0 cascade 106 mirror anchor | ✅ |
| Cascade aggregation MEDIUM-HIGH | R1 + R2 dual-reviewer verdicts (this session, §2 cascade_record.md) | ✅ |

---

## Downstream propagation tracker (forward-pointed; deposit steps TABLED under RULE 1)

| Target document | Section | Action | RULE 1 status |
|---|---|---|---|
| Picture chain v1.20+ | M7 axis row + G5 + G16 closure rows | Adopt this canonical text (long-form for axis row; compact short-form for G-rows) | content **IN SCOPE**; deposit **TABLED** |
| PCF-2 v1.4 §6 | §6 amendment text | Already drafted at bridge `e857172` `pcf2_v1.4_amendment.md`; this canonical text is consistent with the drafted wording | content **IN SCOPE**; Zenodo new-version deposit **TABLED** |
| Umbrella v2.x reference table | M-axis closure row | Replace M7 row with compact short-form | content **IN SCOPE**; Zenodo new-version deposit **TABLED** |
| M-axis ratification index | M7 row entry | `121→122→123 (RATIFY_WITH_AMENDMENT @ MEDIUM-HIGH dual-witness)` | content **IN SCOPE**; index publish **TABLED** |

---

**Status**: ADOPTED 2026-05-09 by T1-SYNTH-M7-V0-CLOSURE-CASCADE-123 (bridge HEAD pre-fire `27ff47c`). This file is the canonical source-of-record for the M7 V0 closure statement under RULE 1.
