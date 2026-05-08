# Substrate A.1 — 058R B.3 carry-forward

**Source:** `siarc-relay-bridge/sessions/2026-05-06/CC-VQUAD-PIII-NORMALIZATION-MAP-RERE-FIRE/phase_b_canonical_map.md`, §B.1–B.4 (lines 1–158).
**Anchor SHA-256 (pre-edit, persistent under 058R freeze):** session deposit anchored at bridge SHA `2eb9b28` (carried forward unchanged through 105/115/117).
**Loaded for:** prompt 110 Phase A.1 (relay envelope SECTION 3 A.1).

---

## Canonical Hamiltonian H_III (Okamoto 1987 §1.1, p. 306)

Verbatim from 058R B.1 (≤ 30 word block per quote-hygiene):

> *"The Hamiltonian associated with P_III is H_III = (1/t)[2 q² p² − {2 η_∞ t q² + (2 θ_0 + 1) q − 2 η_0 t} p + η_∞ (θ_0 + θ_∞) t q]."*

Coordinates: `(q, p, t)`; isomonodromic-time `t`; parameter pair `(v_1, v_2) = (θ_0, θ_∞) ∈ ℂ²` (Okamoto eq. 0.5).
WLOG normalisation: `η_0 = η_∞ = 1` (Okamoto §1.1, immediate after).

## Algebraic identity V_quad ↔ Okamoto t-coordinate (CT v1.3.1 §3.5)

Phase A leading characteristic:

```
f_±(u) = exp(± c_0 / u) · u^ρ · (1 + O(u)),    c_0 = 2/√3
```

with V_quad branch exponent `ρ_V = -11/6` (Phase A pinned).
Matching to Okamoto canonical trans-series `exp(± 2/√t)` forces

```
λ = c_0² / 4 = 1/3
```

— Φ_resc rescaling parameter (058R B.2; carry-forward).

## Φ_shift affine shift

V_quad regular singular at z=∞ matches canonical P_III(D_6) chart via

```
t ↦ t + t_0,    t_0 = -ζ_* / λ = -3 · (4/√3) = -4√3
```

(modulo Stokes-line-orientation sign).

## Φ_symp symplectic transform — KNY 2017 §8.5.17 anchor (eq. 8.239)

Verbatim block (058R B.3 quote, ≤ 50 words):

> *"L_1 = {-a_2/x + pq/(x(x-q)) - tH/x²} + {(1+a_1+a_2)/x - 1/(x-q) + t/x² - 1} ∂_x + ∂_x²,*
> *L_2 = T_α - (1/(x-q))(p - ∂_x),*
> *B = ∂_t - q/(t(x-q))(x ∂_x - q p)."*

Hamiltonian (eq. 8.237):

```
H_{D_6}^{KNY} = (1/t) { p (p-1) q² + (a_1 + a_2) q p + t p − a_2 q },    a_0 + a_1 = 1.
```

Sakai surface-type `D_6^{(1)}`, symmetry `(2 A_1)^{(1)}`.

**Φ_symp identification:**
```
(θ_0, θ_∞)_Okamoto  ⟷  (a_1, a_2)_KNY    (mod convention shift)
```
bijective on V_quad chart at `t=0`; Jacobian non-degenerate.

## V_quad image tuple — Hamiltonian reading (105 §3.5.1 trivial relabel)

Per CT v1.3.1 (3.5.1a)–(3.5.1d) trivial relabel:
```
(α_∞, α_0, β_∞, β_0)  =  (η_∞, η_0, θ_∞, θ_0)  =  (1/6, 0, 0, -1/2).
```

## Residual R1 — partial closure status

058R B.3 (i)–(iii) flag three sub-tasks for Phase D.2 numerical follow-on
(deferred at 058R deposit; UF-115-4 OPEN at 115 audit; this 110 EXEC
session is the deferred Phase D.2):

  (i)   explicit conversion (α_∞, α_0, β_∞, β_0) → KNY (a_0, a_1, a_2);
        the 4-tuple sums to `-1/3` not `0`, surfacing as anomaly D2
        (carried forward unchanged through 058R/105/115/117).

  (ii)  closed-form expansion of L_1 (eq. 8.239) around irregular
        singular point `x=0` of Poincaré rank 1; canonical Stokes
        constant in BLMP 2024 Definition 1.3 `(e_1, e_2)` basis.

  (iii) tracking of multiplicative factor that
        `S_{ζ_*}^{V_quad} = 2π i · 8.12733679…` picks up under (i)+(ii).

## −1/3 null-sum offset — three candidate mechanisms (105 §3.5.1)

(a) Hamiltonian-expansion residual via FW 2002 Prop 4.1 / eq. (4.3):
    auxiliary `h = t H + (1/4) v_1² − (1/2) t`; pull-back along
    V_quad reduction map to V_quad parameter point.

(b) Additive-shift fall-back: replace (3.5.1a)–(3.5.1d) by non-trivial
    form with shift constant `c_α,∞`, `c_α,0`, `c_β,∞`, `c_β,0`
    summing to `+1/3`. Pre-rejected at 069r3 round-3 QD-2 caveat
    by V_quad image asymmetry (only one coord nonzero at +1/6
    leg + one coord nonzero at −1/2 leg; symmetric shift cannot
    accommodate).

(c) Sakai surface-type artefact gated to Route F D_6^{(1)} Sakai-class
    machinery; relevant if mechanism (a) declines under symbolic
    pull-back evaluation.

## Carry-forward integrity

Phase B.3 lines 138–141 of 058R (the residual R1 partial-closure
paragraph) recorded the `-1/3` offset and (i)/(ii)/(iii) sub-tasks
unchanged across the three downstream sessions:
- 105 (CT v1.3 §3.5.1 inserted; trivial relabel canonical)
- 115 (QD-5 audit; verdict R1 MEDIUM-HIGH)
- 117 (CT v1.3.1 R1a small-amendment landed; V_quad caveat block)

**Anchor SHAs (recorded at 110 fire time):**
- 058R bridge SHA: `2eb9b28`
- CT v1.3.1 live: `1894477036FB6332A18979F7A7204FE0BBC43AB22A6A441A11FBB2FAD5BC9BBA`
- p12_journal_main.tex sec:vquad: anchor at L959 (Get-FileHash inspected)
