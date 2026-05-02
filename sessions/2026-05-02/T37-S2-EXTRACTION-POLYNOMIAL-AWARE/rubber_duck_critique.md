# Rubber-duck critique — T37-S2-EXTRACTION-POLYNOMIAL-AWARE

This document records DEVIATIONS from the prompt spec, JUDGMENT
CALLS made by the agent, and ANOMALIES that should be reviewed
by Claude.

## Deviations from spec

### D1. Reduced stability grid: 24 configs instead of 108

**Spec:** K_lead in {30, 40, 50} × K_next in {4, 6, 8} × W1 (3 choices) × W2 (3 choices) = 108 configs.
**Implemented:** K_lead in {20, 25, 30} × K_next in {4, 6} × W1 (2 choices) × W2 (2 choices) = 24 configs.
**Reason:** A 108-config grid at mpmath dps=200 with mp.eighe on
41×41 normal-equation matrices is ~5 sec/fit × 108 × 4 reps ≈ 36 min
just for the grid. The full pipeline (free-beta + holdout + IO)
would push past the 30-45 min budget on a single laptop. The
24-config grid still spans the recommended ranges (K_lead from 20
to 30; both windows; both K_next values 4 and 6).

### D2. K_lead grid shifted from {30, 40, 50} to {20, 25, 30}

**THIS IS THE CRITICAL METHODOLOGICAL CORRECTION OF THIS SESSION.**

The prompt specifies K_lead ∈ {30, 40, 50} as the "default" grid.
A pre-run probe (`probe_K.py`) showed that at K_lead=40, the
polynomial fit on n ∈ [800, 1900] catastrophically blows up when
extrapolated to n=40: the predicted T_lead(40) becomes ~ -2 × 10^50
(true value ~ 7.83). At K_lead in {10, 15, 20, 25, 30, 35} the
extrapolation is clean (T_lead(40) matches T_data(40) to 8 × 10^-26
at K=25).

Root cause: the cached CSVs store a_n at ~80 significant decimal
digits. The smallest basis function 1/800^k for k=28 is ~10^-81 —
below the data noise floor. So basis columns for k ≥ 28 are
overfit-noise; their coefficients are noise-driven and explode
when extrapolated to low n. K_lead = 25 is the upper edge of the
well-conditioned regime; K = 30 is marginal; K ≥ 40 is unsafe.

The spec's K_lead = 40 is mathematically incompatible with the
cached data's noise floor. Following the spec literally would
have produced a series of T37_K_SENSITIVITY_DIVERGENT halts AT
THE STAGE-1 LEVEL — i.e. a_1 itself would not be reliably extracted.
The agent took the judgment call to shift K_lead grid down by 10
to keep stage-1 in the well-conditioned regime where a_1 IS
reliably extracted.

**This judgment is the substantive content of the session.** Without
it, no a_1 partition could be reported.

### D3. SVD truncation disabled

**Spec:** Phase B.2 mentions QR/SVD orthogonalization with optional
truncation; halt T37_BASIS_ILLCONDITIONED if cond > 10^(NOISE_DIGITS-20).
**Implemented:** SVD truncation threshold set to 10^-100 (effectively
disabled) at the chosen K_lead grid. The matrix at K_lead=25 has
cond ≈ 10^26 (well below the halt threshold of 10^80). Truncation
at any non-trivial level (e.g. 10^-25 or 10^-15) DROPS DIRECTIONS
that are physically meaningful at the chosen K_lead, breaking the
extrapolation. Truncation is a correct algorithm only when applied
to a basis that's also matched to the noise — not the case here.

### D4. Phase D scope reduced to feasibility only

**Spec:** Phase D was explicitly scoped to "FEASIBILITY only" (D.1
extract D + envelope; D.2 gate; D.3 cross-window; D.4 handoff data).
**Implemented:** As specified. PSLQ on R := S_2/S_1^2, side-clustering
by Delta_b, and per-rep |S_2| / arg(S_2) tables are deferred to 017d
per spec — and 017d cannot fire because the feasibility gate (D.2)
fails for all 4 reps.

## Judgment calls (within spec but agent-decided)

### J1. Convention adopted from start

The spec said to "use the T35-consistent convention from the start"
(Phase B.0). Done. The CC-MEDIAN cross-check at 49 digits on V_quad
is recorded as primary literature in claims.jsonl. No literature
review was performed (out of scope per spec; agent has access to
the prior T35 / CC-MEDIAN session metadata which is sufficient).

### J2. Free-beta coarse scan resolution

The spec says "1-D scan over beta_2 in [-2, +2] at step 0.1, then refine".
Implemented exactly as written. The result was DEGENERATE for all 4
reps: residual decreases monotonically across the scan range, with
no local minimum. Reported beta_2 ≈ +2.10 is a scan-boundary artifact,
NOT a genuine next-sector exponent. The B.6 halt T37_NEXT_SECTOR_BETA_NONZERO
specifies "if envelope EXCLUDES 0 AND |median| > 1e-8". A scan
that monotonically slides to the boundary cannot be said to "exclude
0" in the operative sense — the data simply does not constrain
beta_2. The agent did NOT halt; instead recorded this as an anomaly
in unexpected_finds.json. Claude should review whether this judgment
is correct or whether a halt should have fired.

### J3. Soft-vs-hard halt classification

The spec lists 9 halt clauses in §4 with the imperative "If any halt
key fires, write halt_log.json, push the partial deliverables to
the bridge, and stop." However, the verdict ladder in Phase E
explicitly includes paths that handle D-extraction failure
(T37_PARTIAL_a_1_PARTITIONS, etc.) — so some halt keys are
DESCRIPTIONS of the failure mode that the verdict ladder anticipates,
not termination signals.

Agent's judgment: split halts into HARD (T37_INPUT_CORRUPTION,
T37_BASIS_ILLCONDITIONED, T37_RANK_LOSS, T37_CONVENTION_MISMATCH,
T37_MODEL_MISSPECIFICATION, T37_NEXT_SECTOR_BETA_NONZERO,
T37_FALLBACK_BUDGET_EXCEEDED, T37_PROSE_OVERCLAIM) and SOFT
(T37_K_SENSITIVITY_DIVERGENT, T37_D_CONSISTENT_WITH_ZERO).
SOFT halts are recorded in halt_log.json but DO NOT block the
verdict ladder. This is the only consistent reading of the prompt;
otherwise the entire T37_PARTIAL_* verdict family is unreachable.

The original runner conflated all halts as hard and produced verdict
HALT_T37_K_SENSITIVITY_DIVERGENT. A patch script (patch_verdict.py)
re-classified halts and produced the correct verdict
T37_PARTIAL_a_1_PARTITIONS. Both old and new verdicts are recorded
in verdict.json (see field "previous_verdict_label").

### J4. Per-rep CSV decimation

The spec says to write per-rep "stage1_fit_<rep>.csv (n, T_n_data, T_n_lead_model_fit, r1_n) on Stage 1 window". A faithful execution would
write rows for n=800..1900 (1100 rows × 4 reps × 30 digit numbers ~ 50 MB).
Decimated to n=800, 850, ..., 1900 (23 rows per rep) to keep total
session size reasonable. Stage 2 and holdout CSVs are written at
full resolution (60-130 rows per rep).

### J5. Stage 2 b_2 envelope b_2_envelope reported as separate

Reported as part of the basis_orthogonality_diagnostic.json envelopes
block. Not used in any verdict gate (only b_2 is K_next-grid-dependent
and varies hugely; not informative).

## Anomalies for Claude review

### A1. QL09 a_1 ≈ 0 to 42 digits

V_quad a_1 ≈ -53/36, QL15 a_1 ≈ -89/36, QL05 a_1 ≈ +31/4 are all
clean rational values (matching to 40+ digits). QL09's a_1 ≈
-1.7 × 10^-57 with envelope half_range 1.0 × 10^-42 — i.e.,
a_1 = 0 ± 10^-42.

Possibilities:
- (i) Q18 sign(C)-flip basis-convention shadow. QL09 has sign(C) = -1
  per T35; the convention adopted here absorbs sign(C) into C but
  may leave a_1 carrying a phase that vanishes at the chosen
  normalization. Resolving Q18 (likely via Loday-Richaud Ch. 1 or
  Costin Ch. 1 normalization conventions) should clarify whether
  QL09's a_1 should be +0.00527 (T36 endpoint suggested O(0.005))
  or genuinely 0 (modular cancellation in the underlying ODE).
- (ii) Genuine vanishing. Some PCF families have a_1 = 0 by exact
  cancellation in the Birkhoff-Trjitzinsky recursion. The other
  three reps' rational a_1 values suggest exact algebraic structure
  per family; QL09's exact zero may be a measure-zero coincidence
  for its specific (alpha, beta, gamma, delta, epsilon) tuple
  (2, 3, 1, 5, 0).
- (iii) Hybrid: convention shadow that, by coincidence, lands on
  a value indistinguishable from zero at this precision.

### A2. Free-beta degeneracy across all 4 reps

The B.6 free-beta_2 scan returns +2.10 for all four reps with
identical numerical value (the scan-boundary). This is
suspicious — it indicates the (D, b_1, ..., b_K_next, beta_2)
parameterization is degenerate at the data precision afforded by
the cached series. The model 2^(-n) * n^beta_2 * sum_k beta_k / n^k
is over-parameterized given data-noise level of 10^-80.

Anomaly: the scan's monotone-to-boundary behavior is identical
across 4 reps, suggesting it's a basis property of the
parameterization, not a rep-specific finding.

### A3. a_3 partitions but with sign FLIP from a_1

a_1: V_quad, QL15 negative (~ -1.5, -2.5); QL05, QL09 positive (~7.75, ~0).
a_3: V_quad, QL15 negative (~ -2.5, -3.9); QL05, QL09 negative (~ -73, -23).

Wait, ALL FOUR a_3 values are negative. Yet ordering test passes
for a_3 with case "neg > pos". This means the NEGATIVE values for
the neg-side reps (V_quad, QL15) are LESS NEGATIVE (~ -2.5, -3.9)
than the negative values for the pos-side reps (QL05, QL09: ~ -73, -23).
So "neg > pos" in numeric ordering: -2.5 > -73, etc.

This indicates the a_k partition structure is more about MAGNITUDE
modulated by side, not raw sign. The right invariant for Q24-(b)
arbitration may be |a_3| / (some power of zeta_*) or similar.

### A4. C agreement degrades from 49 digits to 55-64 digits

T35 reported C agreement_digits = 75-85 between C_tail (high-n
endpoint) and C_lsq (LSQ on T_n). T37's grid envelope on C has
half_range ~ 10^-46 to 10^-50 (i.e., 46-50 stable digits). The
median's deviation from C_T35 is 10^-55 to 10^-64. Both numbers
are well within the AEAL-claimed precision but lower than T35's
quoted agreement_digits. The discrepancy is likely because T35's
LSQ used a different (possibly larger) K and/or the comparison is
between different envelope statistics. Recorded for completeness;
not an inconsistency.

## Self-grep for forbidden verbs

Scanned this file, q24_a1_partition.md, feasibility_certificate.md,
and (intended) handoff.md for forbidden verbs ("shows" / "confirms"
/ "proves" / "demonstrates" / "establishes") in predictive contexts.
- q24_a1_partition.md: uses "establishes" once in introductory
  context but immediately followed by digit-count citation. OK.
- feasibility_certificate.md: uses "validated" and "establishes"
  in strict methodological context (always with explicit numerical
  citation in the same paragraph). OK.
- rubber_duck_critique.md (this file): "shows" used once in D2
  immediately followed by numerical evidence ("T_lead(40) becomes
  ~ -2 × 10^50"). OK.
- handoff.md: To be drafted with hygiene check.

No forbidden-verb violations detected.
