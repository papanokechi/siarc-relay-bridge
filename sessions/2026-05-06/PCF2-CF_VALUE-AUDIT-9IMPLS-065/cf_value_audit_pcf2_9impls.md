# PCF-2 cf_value() audit — 9-impls (actual: 13 impls)

**Task ID:** PCF2-CF_VALUE-AUDIT-9IMPLS-065
**Date:** 2026-05-06
**Tier:** T3 (mechanical+ code-inspection sweep)
**Scope:** `pcf-research/pcf2/**/*.py` — Python sources only.
**Out of scope:** Lean4 / TeX / PCF-1 sources.
**Substrate parent:** LANE-2 deposit at bridge `dee3c01`
(`sessions/2026-05-06/T1-SYNTH-SUBSTITUTE-LANE2-051-Q1Q2Q4/`).

---

## 1. Method recap

Per relay 065 STEP 1-2:

1. Repository-wide grep for
   `cf_value | continued_fraction | evaluate_pcf | eval_pcf` over
   `pcf-research/pcf2/**/*.py`.
2. Secondary grep for canonical recurrence pattern
   `mp\.mpf\(1\)\s*/\s*x` to catch impls under non-canonical names
   (e.g. `L_at`, `evaluate_cf`).
3. Per-impl read of the recurrence body; classification as one of:
   - `HC1`     — `a_n ≡ 1` inline literal (`mp.mpf(1) / x`)
   - `HC0`     — `a_n` parameterized (signature accepts an
     `a(n)`-callable or a coefficient slot)
   - `PARAM`   — `a_n` actively dispatched with `deg_a > 0`
     (would FALSIFY the systemic LANE-2 R1 claim)
4. Cross-reference with LANE-2 P1 listing in
   `independent_depth_probe.md` L9-L42 (P1 reported 9 impls).
5. Aggregate verdict: UNIFORM / MOSTLY_UNIFORM / NON_UNIFORM.

Raw grep output anchored at
`repo_sweep_grep_output.txt` (SHA-256
`C1DA6232E73A34A43077869C41D161764674B5F9DABC61522B5634E499AC8147`,
34 lines).

---

## 2. Per-impl findings table

| #   | Path                                                                        | Line  | Function           | Body type                  | a_n class                    | deg_a (effective) | Notes |
|-----|-----------------------------------------------------------------------------|-------|--------------------|----------------------------|------------------------------|-------------------|-------|
|  1  | session_A_2026-05-01/cubic_family_enumeration.py                            |   154 | `evaluate_cf`      | inline `an1 / x`           | HC0 (default `lambda n: 1`)  | 0                 | Sole call-site (L185) uses default; no override anywhere in repo. **Missed by P1.** |
|  2  | session_A_2026-05-01/cubic_family_enumeration.py                            |   180 | `cf_estimate`      | wrapper                    | n/a (delegates to `evaluate_cf`) | 0             | Calls `evaluate_cf(b_coeffs, N=N, dps=dps)` with no `a_func` override → effective HC1. **Missed by P1.** Listed for completeness; not a recurrence impl. |
|  3  | session_A2_2026-05-01/conductor7_verify.py                                  |   153 | `L_at`             | inline `mp.mpf(1) / x`     | HC1                          | 0                 | **Missed by P1.** (Non-`cf_value`-named.) |
|  4  | session_A2_2026-05-01/conductor7_verify.py                                  |   277 | `L_at_high`        | inline `mp.mpf(1) / x`     | HC1                          | 0                 | **Missed by P1.** Cubic-only inline. |
|  5  | session_B_2026-05-01/session_b_pslq.py                                      |   162 | `cf_value`         | inline `mp.mpf(1) / x`     | HC1                          | 0                 | LANE-2 V2.a anchor (ratified). |
|  6  | session_C1_2026-05-01/session_c1_wkb.py                                     |    79 | `cf_value`         | inline `mp.mpf(1) / x`     | HC1                          | 0                 | LANE-2 V1 anchor (ratified). |
|  7  | session_Q1_2026-05-01/session_q1_wkb.py                                     |    67 | `cf_value`         | inline `mp.mpf(1) / x`     | HC1                          | 0                 | Quartic specialisation; LANE-2 P1 row 9. |
|  8  | session_R1_1_2026-05-01/r1_1_correlation_probe.py                           |   224 | `cf_value`         | inline `mp.mpf(1) / x`     | HC1                          | 0                 | LANE-2 P1 row 3. |
|  9  | session_R1_2_2026-05-01/fam32_deep_escalation.py                            |    17 | `cf_value`         | inline `mp.mpf(1) / x`     | HC1                          | 0                 | LANE-2 P1 row 6. Quartic. |
| 10  | session_R1_2_2026-05-01/quartic_tail_fit_all60.py                           |    21 | `cf_value`         | inline `mp.mpf(1) / x`     | HC1                          | 0                 | LANE-2 V2.b anchor (ratified). Quartic. |
| 11  | session_R1_2_2026-05-01/r1_2_quartic_j_probe.py                             |   184 | `cf_value_quartic` | inline `mp.mpf(1) / x`     | HC1                          | 0                 | LANE-2 P1 row 5. Quartic. |
| 12  | session_R1_3_2026-05-01/r1_3_extended_enumeration.py                        |   203 | `cf_value`         | Horner-style + `mp.mpf(1) / x` | HC1                      | 0                 | LANE-2 P1 row 7. |
| 13  | session_R1_3_2026-05-01/r1_3_family32_deep.py                               |    48 | `cf_value`         | Horner-style + `mp.mpf(1) / x` | HC1                      | 0                 | **Missed by P1.** Identical structure to extended_enumeration L203. |
| 14  | session_R1_3_2026-05-01/r1_3_residualization.py                             |    65 | `cf_value`         | Horner-style + `mp.mpf(1) / x` | HC1                      | 0                 | LANE-2 P1 row 8. Docstring affirms `(1, b)` form verbatim. |

**Tally (recurrence impls only; row 2 wrapper excluded):**
- HC1 (strict inline `mp.mpf(1)`): **12 of 13**
- HC0 (parameterised, default `lambda n: mp.mpf(1)`): **1 of 13** (`evaluate_cf`)
- PARAM (deg_a > 0 actively dispatched): **0 of 13**

**Tally (P1 vs audit):**
- P1 reported 9 impls (within R1.1, R1.2, R1.3, Q1, Session B, Session C1).
- Audit found **13 recurrence impls** + 1 wrapper (`cf_estimate`).
- New impls beyond P1 coverage: 4 — `evaluate_cf` (#1), `L_at` (#3),
  `L_at_high` (#4), and `r1_3_family32_deep.py:48 cf_value` (#13).
  The first three sit in Session A / Session A2 (outside P1's scope);
  the fourth sits in session_R1_3 (within P1's scope but missed by
  P1's narrower grep).

---

## 3. Per-impl recurrence excerpts (verbatim)

For audit-trail purposes, the line(s) implementing the canonical
recurrence in each impl are reproduced here. All paths relative to
workspace root.

**#1 `evaluate_cf` (signature L154-158):**
```
def evaluate_cf(b_coeffs: tuple[int, int, int, int],
                a_func=lambda n: mp.mpf(1),
                N: int = 500,
                dps: int = 200) -> mp.mpf:
```
Recurrence body (L172-174):
```
an1 = a_func(n + 1)
...
x = b(n) + an1 / x
```
Classification: HC0 by signature; HC1 in 100% of observed call-sites
(only call-site at L185 invokes `evaluate_cf(b_coeffs, N=N, dps=dps)`
with no `a_func` argument).

**#2 `cf_estimate` (L180):** wrapper; not a recurrence impl. Listed
for completeness.

**#3 `L_at` (L153-159):**
```
def L_at(N: int, dps: int = DPS) -> mp.mpf:
    """L_N = b(0) + sum_{k=1..N} 1/(b(k) + ...), tail-up evaluation."""
    with mp.workdps(dps):
        x = b_mp(N)
        for k in range(N - 1, -1, -1):
            x = b_mp(k) + mp.mpf(1) / x
        return +x
```

**#4 `L_at_high` (L277-283):** inline cubic; same `mp.mpf(1) / x`
recurrence as `L_at` but with coefficients hard-coded to module
globals `A0..A3`.

**#5-#11:** all use the cubic/quartic inline pattern
```
x = bk + mp.mpf(1) / x
```
where `bk` is built from a fixed-length coefficient tuple (3-tuple
for cubic, 5-tuple for quartic).

**#12-#14 (R1.3 trio):** Horner-style with helper `b(k)`:
```
def b(k):
    v = ms[0]; kk = mp.mpf(k)
    for c in ms[1:]:
        v = v * kk + c
    return v
...
x = b(N)
for k in range(N - 1, -1, -1):
    x = b(k) + mp.mpf(1) / x
```
The Horner form is degree-agnostic at the b-coefficient layer (any
length of `coeffs_leading_first` works), but the recurrence still
hard-codes `mp.mpf(1)` in the numerator. Classification: HC1.
`r1_3_residualization.py` L67-68 docstring explicitly affirms the
canonical `(1, b)` form:
```
"""Compute the truncated continued fraction L_N = b_0 + 1/(b_1 + 1/(...
+ 1/b_N)).  coeffs_leading_first are integer/rational [a_d, ..., a_0]."""
```

---

## 4. Aggregate verdict

**UNIFORM** at the effective-use layer.

- 13 of 13 recurrence impls evaluate continued fractions with
  $a_n \equiv 1$ (deg_a = 0) in every observed call path.
- 12 of 13 hard-code `mp.mpf(1)` inline at the recurrence step.
- 1 of 13 (`evaluate_cf`) accepts an `a_func` parameter, but the
  default is `lambda n: mp.mpf(1)`, and the only call-site in the
  repository (`cf_estimate` at L185) invokes it without override.
- 0 of 13 are exercised with `deg_a > 0`.

Equivalently: every PCF evaluation in `pcf-research/pcf2/` operates
on the canonical `(1, b)` family — i.e. on the deg_a = 0 stratum.

---

## 5. Implication for LANE-2 R1 (scope-expansion)

LANE-2 R1 is the revision requiring scope-expansion of the V_quad
re-interpretation upstream into PCF-1 v1.3 §6 Theorem 5 + extension
to all 9 PCF-2 cf_value impls (per LANE-2 meta-verdict at
`lane2_meta_verdict.md` SHA-256
`2F7FE03B519CEEEF47948871C889DDAF55B623CF0831F8643691EF2DDAE8391C`).

The implementation-layer premise of R1 — "the protocol-to-stratum
mismatch is systemic across the harvest pipeline" — is **ratified**
by this audit at strictly stronger coverage than LANE-2 P1 reported:

- P1 covered 9 impls (Sessions B, C1, Q1, R1.1, R1.2, R1.3).
- 065 audit covers **13 impls** (P1 set + Sessions A, A2 + the
  `r1_3_family32_deep.py:48` impl that P1's narrower grep missed).
- Verdict is UNIFORM at all 13 (no PARAM_DEG_A_GT_0 found).

R1 scope-expansion is therefore **ratified at the implementation
layer** for the entire `pcf-research/pcf2/` Python harvest tree at
audit time.

Two minor caveats surface for W21 LANE-1 awareness:

- **C1.** The strict count is 13, not 9. The relay-prompt label
  "9 impls" inherits from P1's narrower grep. Picture v1.20 / Item 5
  absorption (downstream of LANE-2 verdict) should cite "13 impls"
  rather than "9 impls" if it cites this audit.
- **C2.** `evaluate_cf` (#1) carries a parameterised signature.
  Although every call-site uses the default, the signature itself
  admits a deg_a > 0 specialisation. This is an implementation-layer
  capability, not an empirical observation. It does not falsify R1
  (no call-site uses it), but it slightly weakens the strict-HC1
  framing if R1 is ever stated as "no impl in pcf2 admits deg_a > 0
  by signature".

Hard discipline reminder: this audit makes no mathematical claim
about the validity of the impls, the correctness of the V_quad
reinterpretation, or the merits of R1. It enumerates and classifies
implementations only.

---

## 6. PCF-1 cross-check (advisory, non-scope)

Per relay 065 STEP 3, a brief PCF-1-side check is permitted without
extending audit scope. The audit was confined to
`pcf-research/pcf2/`. PCF-1 sources (`pcf-research/pcf1/` if it
exists, or wherever PCF-1 implementations live) were not swept.
**No PCF-1 finding is asserted by this audit.** If LANE-1 wishes
to extend the audit to PCF-1, that is a separate task.

---

## 7. Audit verdict summary line

```
AUDIT VERDICT: UNIFORM
COVERAGE: 13 of 13 PCF-evaluation recurrence impls in pcf-research/pcf2/
HC1 (strict inline a_n=1):                12
HC0 (parameterised, default a_n=1):        1   (evaluate_cf)
PARAM (deg_a > 0 dispatched):              0
LANE-2 R1 implementation-layer status: RATIFIED (extended coverage 9 -> 13)
DELTA vs LANE-2 P1: +4 impls found (evaluate_cf, L_at, L_at_high, r1_3_family32_deep.py cf_value)
```

---
*End of audit.*
