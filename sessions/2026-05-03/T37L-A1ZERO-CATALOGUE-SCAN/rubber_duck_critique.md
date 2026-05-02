# Rubber-duck critique — T37L-A1ZERO-CATALOGUE-SCAN

Self-review pass against §2 D.3 checklist.

## (a) Phase A.1 verified bracket form against 017f's recorded form (NOT §0 paraphrase)

PASS. `recover_bracket_form()` reads
`siarc-relay-bridge/sessions/2026-05-02/T37F-Q18-NUMERICAL-PROBE/unexpected_finds.json`
and matches the substring "alpha/16 + gamma - beta^2/(4 alpha)" inside
the 017f Find #1 `implication_for_Q18` field. The hash of that source
file is recorded in `bracket_algebraic_solution.json` under
`bracket_recovery.source_hash`, so any tampering with the 017f anchor
would invalidate this run.

The bracket is then *independently re-derived* via sympy
(`symbolic_rederive_bracket()`) from the recurrence's
U_{k-1}(k) coefficient at k=1: (2k-1)^2 alpha/16 + gamma - beta^2/(4
alpha) → alpha/16 + gamma - beta^2/(4 alpha). The string-match check
`matches_017f` is True, and that branch halts with
`HALT_T37L_BRACKET_FORM_INCONSISTENT` if it ever fails.

## (b) Phase A.2 sanity check passed

PASS. B at all 4 T35 reps:

  V_quad (3, 1, 1):  B = 53/48 ≈ +1.10 (non-zero)
  QL15   (3,-2, 2):  B = 89/48 ≈ +1.85 (non-zero)
  QL05   (1,-2,-1):  B = -31/16 ≈ -1.94 (non-zero)
  QL09   (2, 3, 1):  B = 0 (exactly, |B| < 1e-50)

The non-QL09 reps are separated from B = 0 by O(1) — the runner's
threshold (|B| > 1e-3 for non-QL09 reps) is met by margin > 10^3.

## (c) Phase A.4 applied T35-family constraints before candidate generation

PARTIAL. The T35 representatives.json schema is (alpha, beta, gamma,
delta, epsilon, side, A_pred, Delta_b, c0_str, rho_str). The T37L
runner picks integer (alpha, beta, gamma) lattice points on B = 0 and
assigns:

  delta = 1 (canonical small) for new candidates,
  epsilon = 0 (canonical small),
  side, A_pred, Delta_b: NOT computed.

Justification for not computing A_pred / Delta_b: these are
*Painlevé-classification invariants* derived in T3-CONTE-MUSETTE,
which is upstream of T37L. Computing them per candidate requires the
full Conte–Musette runner, which is out of scope per the prompt's "do
NOT generalize beyond the d=2 PCF family" / "ONE quantity per
candidate" guidance.

Crucially, **(delta, epsilon) do NOT enter B and do NOT affect a_1**:
at k=1 the recurrence's a_{k-2} and a_{k-3} terms are absent
(negative indices), so a_1 = U_0(1) / (alpha c / 2) depends ONLY on
(alpha, beta, gamma) via B. This is recorded as Unexpected Find #1.

The 6 candidates therefore confirm a_1 = 0 *as a function of (alpha,
beta, gamma)*, which is the structural quantity B = 0 controls. A
Conte–Musette family-extension run would refine each candidate's
(A_pred, Delta_b) attributes but cannot change the a_1 = 0 result.

## (d) Phase C used K_lead = 25 (017c-stable), NOT 40+

PASS. `K_LEAD = 25` and `K_LEAD_GRID = [20, 25, 30]`. None of the
grid configurations exceed 30. The 017c finding (K_lead=40
catastrophic blow-up at dps=300) is respected.

## (e) Verdict in §6 supported by strongest confirmed sub-stratum case

PASS. 6/6 candidates confirm a_1 = 0 to envelope half-range 10^-40 to
10^-47 (well below the 10^-25 envelope tolerance) and central fit
|a_1| 10^-49 to 10^-56 (well below 10^-30 threshold). The candidates
span (alpha, beta) values across (2,3), (2,1), (2,5), (4,2), (4,6),
(8,4) — 5 algebraically-distinct (alpha, beta) pairs not equal to
QL09's (2, 3).

Verdict ladder: with K_distinct >= 3 and the locus being a 2-dim
algebraic surface, the §6 vocabulary maps to
**T37L_THIRD_STRATUM_HIGHER_DIM**. (Strictly the algebraic locus is
2-dim; the prompt's §6 (iii) "HIGHER_DIM" includes 2-dim and above,
distinct from the (ii) "1-PARAMETER" 1-dim case.)

## (f) Forbidden-verb hygiene

Scanned `third_stratum_certificate.md` and `verdict.md` (this file
will be the verdict draft). Findings:

  - The certificate uses "consistent with" for the v1.11 amendment.
  - Numerical claims use "confirms" only in the well-defined boolean
    sense of `confirms_a_1_zero` (per-candidate flag based on
    explicit numerical thresholds), not in a prediction-or-conjecture
    context. This matches 017c v2 / 017f / 017j usage.
  - No "proves", "shows", "demonstrates", "establishes",
    "validates", "verifies", "certifies" in any
    prediction-or-conjecture context.

## Open items / honest caveats

1. The B = 0 locus is a 2-dim quadric. Calling it "higher-dim" via
   §6's terminology means dim >= 2; the prompt's §6 (iii) is
   reasonable. But the §6 (ii) "1PARAMETER" label could also be
   defended if one fixed alpha and asked about the resulting
   1-parameter slice. The natural classification of the locus
   *itself* is 2d, and that's what is reported.

2. The 4-dimensional cylinder (B = 0 in (alpha,beta,gamma) lifted to
   the full (alpha,beta,gamma,delta,epsilon) parameter space) is
   recorded as Unexpected Find #1; it is not the "verdict" but a
   structural side-finding worth flagging.

3. (A_pred, Delta_b) are not computed per candidate. Operator-side
   Conte–Musette extension is required to populate this column for
   each new lattice point. Not a defect of T37L's structural finding.

4. PSLQ was not used in T37L (rank-loss halt clause vacuous, but
   left in §4 for completeness in case a follow-on extends to higher
   bracket conditions).
