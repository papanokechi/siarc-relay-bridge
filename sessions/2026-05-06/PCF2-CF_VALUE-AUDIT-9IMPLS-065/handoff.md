# Handoff — PCF2-CF_VALUE-AUDIT-9IMPLS-065
**Date:** 2026-05-06
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** COMPLETE

## What was accomplished

Executed relay 065 — a code-inspection audit of all PCF-evaluation
(`cf_value` and analogous) implementations across `pcf-research/pcf2/`,
to confirm whether the `a_n = 1` (deg_a = 0) hardcoding posited by
LANE-2 V1 + V2 + P1 is uniform at the implementation layer. The
audit covers 13 recurrence implementations (vs LANE-2 P1's reported
9), classifies each by `a_n` treatment, and reports an aggregate
verdict that ratifies LANE-2 R1 scope-expansion at strictly stronger
coverage than P1 provided.

## Key numerical findings

- **13 PCF-evaluation recurrence impls** identified in
  `pcf-research/pcf2/` (vs P1's count of 9).
- **12 of 13 HC1 (strict inline `mp.mpf(1)`):** session_b_pslq.py:162,
  session_c1_wkb.py:79, session_q1_wkb.py:67, r1_1_correlation_probe.py:224,
  fam32_deep_escalation.py:17, quartic_tail_fit_all60.py:21,
  r1_2_quartic_j_probe.py:184 (`cf_value_quartic`),
  r1_3_extended_enumeration.py:203, r1_3_family32_deep.py:48,
  r1_3_residualization.py:65, conductor7_verify.py:153 (`L_at`),
  conductor7_verify.py:277 (`L_at_high`).
- **1 of 13 HC0 (parameterized, default `lambda n: mp.mpf(1)`):**
  cubic_family_enumeration.py:154 (`evaluate_cf`); only call-site at
  L185 uses default — no override anywhere in repo.
- **0 of 13 PARAM (deg_a > 0 dispatched).**
- 1 wrapper (cf_estimate L180) noted for completeness; not counted.
- Aggregate verdict: **UNIFORM** at the effective-use layer.
- Repo sweep grep output anchored at SHA-256
  `C1DA6232E73A34A43077869C41D161764674B5F9DABC61522B5634E499AC8147`.
- Audit document SHA-256
  `16512BCC71C9A19ED59B808D8D070877F2160C5A7A062381C0FC9533182D3BF9`.

## Judgment calls made

- **J1.** Counted `cf_estimate` as a wrapper (excluded from 13-of-13
  tally) because it has no recurrence body of its own. Listed in
  audit table for completeness. Not specified in relay 065; judged
  best for audit-trail clarity.
- **J2.** Classified `evaluate_cf` as **HC0 by signature, HC1 in use**
  rather than forcing it into one bin. Relay 065's HC0/PARAM/HC1
  rubric does not directly handle "parameterized but defaulted to 1
  with no override." Surfaced as discrepancy D2 + caveat C2 in audit
  doc section 5.
- **J3.** Re-included Session A and Session A2 in audit scope even
  though LANE-2 P1's stated coverage excluded them. Relay 065 P4
  scope is `pcf-research/pcf2/**/*.py` without session-directory
  exclusions, so re-inclusion is the literal reading. Surfaced the
  resulting count delta (13 vs 9) as discrepancy D1.
- **J4.** Classified `cf_value_quartic` (suffix-named symbol) as a
  cf_value-family impl in row 11 of the audit table. The relay's
  enumeration target ("cf_value, evaluate_pcf, eval_pcf, ... or
  similar") admits suffix variants.
- **J5.** Classified `L_at` and `L_at_high` (in conductor7_verify.py)
  as PCF-evaluation impls under the relay's "or similar" clause and
  the secondary "any inline lambda/closure that computes a continued
  fraction from coefficient arrays" provision. Both have inline
  recurrences `x = b(k) + mp.mpf(1)/x`.

## Anomalies and open questions

- **A1 (most important).** The relay-prompt label "9 impls" inherits
  from LANE-2 P1's listing. The audit found 13 recurrence impls — a
  +4 delta. Three of the four are out-of-scope-for-P1 (Sessions A,
  A2); one is in-scope-for-P1 but missed by P1's listing
  (`r1_3_family32_deep.py:48`). The verdict UNIFORM is unchanged,
  but downstream artefacts (picture v1.20, Item 5 absorption,
  PCF-2 v3.x wording-softening) that cite the count should cite
  **13**, not 9. **Surface to W21 LANE-1 for picture / framing
  alignment.**
- **A2.** `evaluate_cf` is the ONE impl with a parameterized `a_func`
  signature. If LANE-2 R1 is ever sharpened to "no impl in pcf2
  admits deg_a > 0 by signature," that strict claim is false at the
  signature layer (though true at every observed call-site). LANE-1
  may want to choose: (a) keep R1 as effective-use claim and
  acknowledge the signature-layer capability as caveat; or (b) sharpen
  R1 with a narrower wording. See discrepancy D2.
- **A3.** Should the audit have extended to PCF-1? Section 6 declined
  to do so per relay 065 STEP 3 + scope discipline, but PCF-1
  implementations may exhibit different behavior, and LANE-2 R1's
  "extension to PCF-1 v1.3 §6 Theorem 5" is the upstream half of the
  scope-expansion. **Recommend a future T3 audit task targeting
  pcf-research/pcf1/**.
- **A4.** Classification rubric ambiguity: relay 065 STEP 2 distinguishes
  HC1 / HC0 / PARAM but does not provide guidance for "HC0 by
  signature with default = HC1 lambda." Future audits may benefit from
  a four-bin rubric: HC1 / HC0_DEFAULT_HC1 / HC0_DEFAULT_NON_HC1 /
  PARAM_ACTIVE.

## What would have been asked (if bidirectional)

- Should the audit treat `cf_estimate` as a separate impl or a
  wrapper? (J1 chose wrapper.)
- Should `evaluate_cf` be classified HC0 strictly per signature, or
  bumped to HC1 because no call-site overrides? (J2 reported both.)
- Was Session A / Session A2 inclusion intended? (J3 went literal.)
- Is the "9 impls" in the task ID a hard target or a P1-inherited
  estimate? (Treated as estimate; reported actual 13.)

## Recommended next step

Two parallel tracks:

1. **W21 LANE-1 picture/framing alignment.** Relay or note for LANE-1
   to update picture v1.20 + Item 5 absorption + PCF-2 v3.x wording
   to cite "13 cf_value impls" instead of "9 cf_value impls" if
   citing this audit. The R1 verdict itself does not change.

2. **PCF-1 audit (T3 mechanical+).** A sibling audit targeting
   `pcf-research/pcf1/**/*.py` to confirm/falsify the systemic claim
   for the upstream half of LANE-2 R1's scope-expansion. Suggested
   relay-prompt template: clone 065 with scope = `pcf-research/pcf1/`.

Either can run independent of the other; neither blocks downstream
066 / 067 (3-D PCF-1 V_quad row reframing + Item 3 follow-up note),
which gain audit_065 as substrate citation.

## Files committed

- `cf_value_audit_pcf2_9impls.md` — primary audit document
- `repo_sweep_grep_output.txt` — verbatim Select-String output
- `substrate_anchor_shas.md` — LANE-2 deposit + audited source SHAs
- `claims.jsonl` — 10 AEAL claim entries (C1-C8, with C5 split into C5a/C5b/C5c for the 3 newly-found impl groups)
- `halt_log.json` — 6 halts evaluated, all PASS (zero triggered)
- `discrepancy_log.json` — 4 non-blocking discrepancies D1-D4
- `unexpected_finds.json` — 3 unexpected finds U1-U3
- `handoff.md` — this file

## AEAL claim count

10 entries written to `claims.jsonl` this session:
- C1 (repo sweep grep output SHA)
- C2 (V1 substrate session_c1_wkb.py)
- C3 (V2.a substrate session_b_pslq.py)
- C4 (V2.b substrate quartic_tail_fit_all60.py)
- C5a (NEW evaluate_cf in cubic_family_enumeration.py)
- C5b (NEW L_at + L_at_high in conductor7_verify.py)
- C5c (NEW cf_value in r1_3_family32_deep.py — missed by P1)
- C6 (aggregate verdict UNIFORM)
- C7 (R1 implementation-layer ratification at coverage 9 -> 13)
- C8 (forbidden-verb self-check PASS post-rephrase)

Exceeds the relay 065 STEP G floor of ≥7.
