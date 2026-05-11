# results.md — PCF-2 v1.4 result statements (substrate-frozen)

## Q4a — Per-section result statements

PCF-2 v1.4 is a **program statement**, not a results paper. The §Q4a result statements are conjecture-tier (B₃, B4) and Open-Problem-tier (op:j-zero-amplitude-h6 and others). Result statements are not "theorems" with proofs but **forward-pointed conjectures with explicit caveats and substrate anchors**.

### Substrate-frozen result statements (verbatim register)

| Object | Statement | Caveat / Anchor |
|---|---|---|
| Conjecture B₃ | (cubic trichotomy — verbatim from v1.3 §3) | substrate-frozen; do NOT modify in v1.5 |
| Conjecture B4 | Sharp WKB exponent identity at d=3, d=4 (verbatim from v1.3) | substrate-frozen; do NOT modify |
| Open Problem `op:j-zero-amplitude-h6` (v1.4 status update) | RESOLVED-IN-SOFT-BRANCH: max \|δ_lin\| = 3.09 × 10⁻²³ across Q_30..Q_33 j=0 cubic families; PSLQ on 17-member deduplicated H6 Chowla–Selberg basis B19+ returns no Γ(1/3) relation; hard-branch goal \|δ\| < 10⁻³⁰ forward-pointed under Q22 path-(b) | Anchor: bridge `e857172` (Prompt 014 PASS_A_EQ_6_ONLY) → ratified at M7 V0 cascade `7f93b9e`; annotation (SOFT-BRANCH; HARD-BRANCH-PENDING) |
| 50-family catalogue scope | (verbatim from v1.3) | substrate-frozen |
| d=4 deep-WKB null (Session R1.3) | rule-out for verbatim degree-4 extension | scope-limit-honesty signal; preserved verbatim |

### Numerical anchor values (DO NOT MODIFY; cite verbatim from M7 V0 cascade `7f93b9e`)

```
j=0 amplitude / Chowla–Selberg closure (4 families Q_30..Q_33):

  max |δ_lin|          = 3.09 × 10⁻²³
  dps                  = 25,000
  N_max                = 1,200
  LIN refit params     = 11
  K_FIT (Padé order)   = 7

PSLQ verification on H6 basis:

  Basis                = 17-member deduplicated H6 Chowla–Selberg basis B19+
                         (NOT 18-element literal basis; Γ-reflection
                          identity deduplicates {√3, Γ(1/3)Γ(2/3)/(2π)} pair)
  maxcoeff             = 10⁵⁰
  tolerance            = 10⁻⁴⁰
  verdict              = no Γ(1/3) relation in any of the 4 families

Hard-branch stretch goal (NOT CLOSED; forward-pointed):

  Target               = |δ| < 10⁻³⁰
  Status               = forward-pointed under Q22 path-(b)
  Annotation           = (SOFT-BRANCH; HARD-BRANCH-PENDING)
```

### Residuals catalogue (PCF-2 v1.4 scope)

- **M7 HARD-BRANCH-PENDING** — see Q5a long+short caveat-language templates in `caveats.md`.
- **Q22 path-(b)** — see Q5a M2 Q22 final-disposition template in `caveats.md`.
- **d=4 deep-WKB null** — verbatim from v1.3 (preserved in abstract and §R1.3).

### NOT in scope for PCF-2 v1.4 results section (per scope distinction)

- M4 V0 anchor values (degree-2 result; cited as cross-reference in Reproduction Appendix, not as a PCF-2 result).
- M8a Painlevé-test catalogue (out-of-degree-scope).
- M8b laptop-feasible numerical foreclosure (out-of-degree-scope).
- M9 V0 substrate landings (program-tier).
- M10 Lean formalization (engineering tier).
- S153 quad-witness CONFIRM_CLOSURE (program-tier).

## Q4b — Cross-citation graph (verbatim Q4b table)

See `zenodo_metadata.json` for the deposit-state related_identifiers block. The Q4b cross-citation audit (verdict.md §Q4b) verifies that the live state at 10.5281/zenodo.20114315 correctly carries:

- `isNewVersionOf` → PCF-2 v1.3 version-DOI 10.5281/zenodo.19963298 (per IsNewVersionOf exception targeting immediate-predecessor version-DOI per slot 160 schema v1 Layer 1)
- Paired `isSupplementTo + cites` → PCF-1 concept-DOI 10.5281/zenodo.19931635
- Paired `isSupplementTo + cites` → Umbrella concept-DOI 10.5281/zenodo.19885549

Asymmetric to Umbrella v2.2 (which cites all 4 program-companions: PCF-1, PCF-2, CT, T2B); the asymmetry is intentional per math-content/program-tier scope distinction.

## Result-statement style guidance (for any future v1.5+ amendments)

1. **All claims carry residual annotation if they are forward-pointed** (e.g., (SOFT-BRANCH; HARD-BRANCH-PENDING), (NUMERICAL-FORECLOSURE; d≥3-CAVEAT-CARRIED-FORWARD)).
2. **Each numerical claim cites its V0 anchor bridge SHA.**
3. **No "theorem"-tier language for conjecture-tier claims.** Conjectures are conjectures; numerical evidence is numerical evidence; PSLQ-undetected is PSLQ-undetected.
4. **Hard-branch stretch goals are documented as forward-pointed, not closed.** Honesty signal.
5. **Deep-WKB null / scope-limits are preserved verbatim.** Honesty signal.
