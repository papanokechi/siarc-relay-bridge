# Bridge SHA list — slot 137 substrate

**Session**: T2-EXECUTOR-PCF2-V14-M7-V0-AMENDMENT-PREP-137
**Date drafted/verified**: 2026-05-09 (pre-fire SHA pre-verification per §0.1)
**Bridge HEAD at fire-time (pre-deposit)**: `887981b` (slot 135 landed)

| 7-char | Full hash                                         | Session / role                                                                                                                                                                                                              |
|--------|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `7f93b9e` | 7f93b9e4d624fdfca62f5d85393b4ead35cea751         | T1-SYNTH-M7-V0-CLOSURE-CASCADE-123 — M7 V0 canonical closure statement (RATIFY_WITH_AMENDMENT × 2 dual-witness; aggregated MEDIUM-HIGH; annotation `(SOFT-BRANCH; HARD-BRANCH-PENDING)`); CRITICAL substrate cited verbatim in v1.4 abstract addendum + `op:j-zero-amplitude-h6` body + amendment-log paragraph. |
| `e857172` | e857172418de2e760e79ba001ba032f520b708f7         | T25D-RETRY-13PARAM (Prompt 014, 2026-05-02) — M7 V0 numerical substrate; verdict `PASS_A_EQ_6_ONLY`; max \|δ_lin\| = 3.09e-23 across Q_30..Q_33; 17-member dedup H6 B19+ basis; pre-existing brief v1.4 draft amendment at `pcf2_v1.4_amendment.md` (29 lines, draft form) used as base for slot 137 substrate edit. |
| `fd669d3` | fd669d347967db2e854f8e9d3725f625bf9fbc2a         | T1-SYNTH-M9-V0-CLOSURE-PATH-CONSULTATION-CASCADE-132 — PATH_B / Option α operative decision (PCF-2 v1.4 deposited FIRST before umbrella v2.2; unanimous across R1 Gemini + R2 Claude.ai + R3 Grok). Governance substrate; cited in §0.1 + §6 operator-side checklist; **NOT** cited in v1.4 manuscript body (per A7 spec). |
| `887981b` | 887981bf51860550a05ff949f0145c1687623689         | T2-EXECUTOR-UMBRELLA-V22-M9-V0-DEPOSIT-PREP-135 — umbrella v2.2 substrate-prep (structural-mirror precedent for slot 137 procedure); slot 137 inherits the lessons-learned-applied A6 = NOTE-class (page-count floor → soft) + UF-135-4 ANTI-CONFLATION rule (forward-pointed at slot 137 §0.5 + §3.3). |
| `5f9db69` | 5f9db69c754c410b79091cbd84e6d79b63d10b6e         | M4-V0-CLOSURE-CASCADE-106 — M4 V0 closure-cascade (mirror anchor for the `(MEDIUM-HIGH; HIGH-PENDING)` annotation pattern). v1.4 manuscript cites this SHA in `\paragraph{Cascade ratification.}` ONLY for annotation-pattern structure; per ANTI-CONFLATION rule §0.5 the M4 V0 *numerical* content is **NOT** cited in the v1.4 op:j-zero-amplitude-h6 body. |
| `70d1a48` | 70d1a4835ee0bc1f188aada9be65bb657f471730         | PICTURE-V19-CONSOLIDATED-DEPOSIT — picture v1.19 deposit; cross-reference for picture-chain v1.20+ tag form `M7_V0_CLOSED (SOFT-BRANCH; HARD-BRANCH-PENDING)` cited in v1.4 §`op:j-zero-amplitude-h6` `\paragraph{Soft / hard branch split.}`. Governance substrate; **NOT** cited as raw SHA in v1.4 manuscript body (cited via friendly tag form). |

## Verification record (G1 gate)

All 6 SHAs above resolved cleanly via `git rev-parse --verify <SHA>` against the bridge repo at slot 137 fire time (bridge HEAD `887981b`). G1 gate PASS.

## Categorization

- **Manuscript-body substrate** (must appear verbatim in v1.4 source per A7): `e857172`, `7f93b9e`, `5f9db69`. All 3 PASS — A7 verified at hits 3 / 3 / 1.
- **Governance substrate** (cited in operator-side runbooks / cascade chain only; NOT required in v1.4 body): `fd669d3`, `887981b`, `70d1a48`.

## Deposit-ordering note (per cascade-132 §3.1 unanimous Option α)

When RULE 1 lifts:

1. **PCF-2 v1.4** → Zenodo deposit FIRST (THIS slot's source; concept DOI `10.5281/zenodo.19936297`).
2. Umbrella v2.2 → Zenodo deposit SECOND (slot 135 substrate; cites PCF-2 v1.4 version DOI in `IsSupplementTo`).
3. Picture-chain v1.20+ → Zenodo deposit THIRD (slot 136 substrate, when fired; cites both PCF-2 v1.4 + umbrella v2.2 version DOIs).
