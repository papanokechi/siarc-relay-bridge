# Substrate A.3 — V_quad numerical baseline

**Source 1 (Hamiltonian-tuple anchor):** `tex/submitted/p12_journal_main.tex` §`sec:vquad` (lines 959–1100).
**Source 2 (Stokes-anchor numerical):** `pcf-research/vquad/scripts/jimbo_final.py` + `pcf-research/vquad/results/t2_iter23_jimbo.json`.
**Source 3 (connection-matrix):** `MANUSCRIPT_INSERTS_VQUAD_2026-04-16.md` (commit 3af07fc3).
**Loaded for:** prompt 110 Phase A.3 (relay envelope SECTION 3 A.3).

---

## V_quad recurrence + Wallis characteristic polynomial

```
a_n = 1
b_n = 3 n² + n + 1
b(x) = 3 x² + x + 1
Δ = 1² - 4·3·1 = -11
b(x) = a'(x) with a(x) = 3 x² + x + 1, c(x) = -x²
```
Discriminant `Δ = -11` generates the imaginary quadratic field `ℚ(√-11)`.

## V_quad apparent singularities + Frobenius indices

(`pcf-research/vquad/scripts/jimbo_final.py` L26–35; `t2_iter23_jimbo.json`.)

```
s_1 = (-1 + i √11) / 6
s_2 = (-1 - i √11) / 6
Δ_s = s_2 - s_1 = -i √11 / 3
ξ_0 = 2 / √3        (Borel-transform branch-point, p12 sec:vquad L1054)
β_exp = -1/(3√3)    (Borel-transform branch exponent, p12 L1056)
```

Frobenius exponents at `s_1`, `s_2`: both `{0, 0}` (recorded
`pcf-research/vquad/results/frobenius_apparent_verification.json`).
Therefore monodromies `M_{s_1}`, `M_{s_2}` are both UNIPOTENT at the
apparent singularities of V_quad's WKB-channel ODE.

## Painlevé III(D_6) parameter tuple — cited (p12 §sec:vquad subsec)

p12_journal_main.tex L981–984:
```
(α, β, γ, δ) = (1/6, 0, 0, -1/2)
```
labeled as classical-ODE convention in p12; per 105 §3.5.1 trivial
relabel + 117 R1a caveat block, ALSO interpreted as Hamiltonian-side
`(η_∞, η_0, θ_∞, θ_0) = (1/6, 0, 0, -1/2)` per CT v1.3.1.

`(α, β, γ, δ)` taken verbatim from `cite{Papanokechi2026Vquad}` §2
(p12 L985).

## Cited Stokes constant — 14-digit anchor

(`pcf-research/vquad/scripts/jimbo_final.py` L26; `t2_iter23_jimbo.json` L7.)

```
S = 0.43770528073458    (14 digits, from Dingle late-term formula)
```

p12 sec:vquad records 8-digit precision (`Stokes ≈ 0.43770528…` at L1064);
the 14-digit value above is the higher-precision baseline from the
`t2_iter23_jimbo.json` substrate.

## Connection-matrix entries (high-precision)

`MANUSCRIPT_INSERTS_VQUAD_2026-04-16.md` reports (commit 3af07fc3):
```
M_11 = 1.9420321374711220465        (~ 17-digit precision)
M_21 = -2.9999268666050110215       (~ 17-digit precision)
```
PSLQ search across 360 basis triples + 245 Jimbo (1982) connection-formula
variants returned null on closed-form identification (`t2_iter23_jimbo.json`
"closest = F19_mixed diff=9.79e-3"); best near-miss < 5.5 digits agreement
to any tested Γ-value combination.

## Accessory parameter

`q_CHE = -s_1² / 3 = (5 + i √11) / 54   ∈   ℚ(√-11)`

(p12 sec:vquad L1080; `jimbo_final.py` L130–135.)

`σ_conn` (Jimbo connection parameter) is TRANSCENDENTAL in `q_CHE`
(p12 L1075–1085 + memo.txt L27 framing).

## Painlevé-channel residual at depth 3000

p12 sec:vquad Table~tab:painleve-deep (L990–1020):
```
V_quad:  P-III ansatz residual = 4.59e-5 (marginal, BELOW 10^-6 candidacy threshold)
```

V_quad's Painlevé reduction does NOT live in the L(t) recurrence-parameter
channel; it lives in the Borel-resummation Stokes-constant channel
(p12 L1024–1042).

## Numerical anchors for Phase B/C cross-checking (110 fire time)

| Quantity | Value | Source | Precision target |
|----------|-------|--------|------------------|
| ξ_0 (Borel-singularity) | `2/√3 = 1.154700538…` | p12 L1054 + Domb-Sykes | ≥ 8 digits |
| β_exp (branch exponent) | `-1/(3√3) = -0.192450090…` | p12 L1056 | ≥ 8 digits |
| S (Stokes constant) | `0.43770528073458` | jimbo_final.py L26 | ≥ 14 digits |
| M_11 (connection) | `1.9420321374711220465` | MANUSCRIPT_INSERTS L9 | ≥ 17 digits |
| M_21 (connection) | `-2.9999268666050110215` | MANUSCRIPT_INSERTS L9 | ≥ 17 digits |
| q_CHE (accessory) | `(5 + i√11)/54` | p12 L1080 | EXACT (algebraic) |
| s_1, s_2 (sing.) | `(-1 ± i√11)/6` | jimbo_final.py L29 | EXACT |
| (η_∞, η_0, θ_∞, θ_0) | `(1/6, 0, 0, -1/2)` | p12 L982 + 105 §3.5.1 | EXACT (cited) |
| (a_0, a_1, a_2)_KNY | `(3/2, -1/2, 0)` | derived from above | EXACT (relabel) |

## Pre-existing numerical infrastructure

`pcf-research/vquad/scripts/`:
- `jimbo_final.py`: 245 Jimbo formula variants tested; PSLQ null.
- `t2_iter17_stokes.py`: Frobenius-to-WKB connection-matrix computation.
- `verify_frobenius_apparent.py`: indices {0,0} at apparent singularities reported.

These computations were carried out at dps ≤ 80; this 110 session
runs at dps ≥ 100 default (mp.dps = 200 target per G7).

## Numerical-extraction strategy for Phase B–E

Per 069r3 round-3 QD-1 verdict: Route D path is

```
V_quad recurrence  →  WKB-channel formal series
→  Borel transform (singularity at ξ_0)
→  Stokes constant S via Dingle late-term  [INDEPENDENT NUMERICAL]
→  Monodromy data (M_{s_1}, M_{s_2}) via Frobenius+connection  [INDEPENDENT NUMERICAL]
→  JM-Ueno isomonodromic inversion  ←—  REQUIRES JM 1981 PART II OR FW 2002 SUBSTITUTE
→  (η_∞, η_0, θ_∞, θ_0) extracted
```

Phase B (this session) runs the first 3 steps as cross-check on the
existing 14-digit S anchor + 17-digit M anchors; Phase D runs the
inversion via FW 2002 substitute path (D.1.b) since JM 1981 Part II
NOT on disk (G3 supplementary check at fire time: only `okamoto_1987_part_I_painleve_VI_AnnMat.pdf` and `forrester_witte_2002_math-ph-0201051.pdf/.txt` available).
