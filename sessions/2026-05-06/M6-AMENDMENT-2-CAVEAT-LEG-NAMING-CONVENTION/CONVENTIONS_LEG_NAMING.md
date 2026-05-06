# SIARC milestone leg-naming convention

**Issued:** 2026-05-06 (in-tier T2 CLI-Synth, operator-promoted assent on
047 M6-ARBITRATION verdict spec-amendment §2; relay 053 forward-applied)
**Anchor:** `sessions/2026-05-06/M6-ARBITRATION-W19-FRIDAY/m6_verdict.md`
§"Spec-rollback or spec-amendment recommendation" §2

## Rule

Any milestone that has been split-defined in a synthesizer arbitration
verdict (the canonical example being M6 → M6.H4 + M6.CC per the 047
verdict landed at bridge 78c7b16 on 2026-05-06) MUST be referenced by
its leg-suffixed identifier in all NEW caveat profiles, M9
announcement-format renderings, and Strategyzer-monthly handoffs
drafted after the verdict's bridge-land timestamp.

Concrete pattern for the M9 announcement-format caveat profile (per 047
§"Spec-rollback" §2 recommendation):

```
OLD (pre-047):  M1/M2/M3/M5/M6/M8 ✅ + M4 partial + M7 soft +
                M8b foreclosed
NEW (post-047): M1/M2/M3/M5/M6.H4/M8 ✅ + M4 partial +
                M6.CC partial + M7 soft + M8b foreclosed
```

The leg suffix MUST appear inline at the token; abbreviated forms
(`M6 (H4)`, `M6/H4`, `M6 [H4]`) are not permitted in caveat-profile
contexts so that automated grep-disambiguation on the `M6.H4` /
`M6.CC` literal remains deterministic.

## Scope

- **APPLIES to:**
  - caveat profiles in milestone-tracking documents,
  - M9 announcement-format renderings,
  - Strategyzer-monthly handoffs (e.g. P008-INPUT-PACKAGE-FOR-MSB
    successor packages),
  - picture-version milestone schemas (per amendment #3, separately
    issued),
  - CMB gating-context citations of the unqualified `M6` token (per
    amendment #1, separately issued).
- **DOES NOT APPLY to:** deposit-time records pre-dating the verdict's
  bridge-land timestamp. Per the SIARC AEAL deposit-time-snapshot rule,
  files such as the 038 caveat-profile substrate
  (`sessions/2026-05-04/MILESTONE-RESIDUAL-GAP-SURVEY-M4-M7-M8B-M9/handoff.md`
  L102, anchor SHA-256
  `D774523E2B60761315403716B22EAB196D5A71B76AF486790FB50EA477DF3558`)
  are preserved as-is; they record caveat-profile state at their
  deposit time and are correct relative to that deposit time.
- **DOES NOT APPLY to:** prose where the unqualified `M6` is explicitly
  disambiguated by surrounding context (e.g. "M6 (the canonical-form
  leg, M6.CC)"). In such cases the leg suffix is recommended but
  optional.

## Future amendments

If a subsequent split-definition arises (e.g. M4 splitting into
M4.G + M4.H, or M8b splitting at a finer grain), the same leg-suffix
pattern is applied via a new conventions amendment. This document is
the template:

1. Cite the synthesizer arbitration verdict that introduced the split.
2. State the OLD / NEW pattern for caveat profiles.
3. Restate the deposit-time-snapshot exemption.
4. Append-only; do not retroactively edit prior conventions sections.

## References

- 047 M6-ARBITRATION-W19-FRIDAY verdict, bridge `78c7b16` (2026-05-06).
  Anchor SHA-256 of `m6_verdict.md`:
  `C9BBAB60FF1ACCE428A21A806D8DF0350C9756A58A9F5C4799E1D6D8EBF3263F`.
- 038 MILESTONE-RESIDUAL-GAP-SURVEY-M4-M7-M8B-M9 caveat-profile
  substrate, bridge 2026-05-04. Anchor SHA-256 of `handoff.md`:
  `D774523E2B60761315403716B22EAB196D5A71B76AF486790FB50EA477DF3558`.
- Memory: SIARC AEAL deposit-time-snapshot rule (deposit-time records
  are not retroactively modified by subsequent verdicts).
