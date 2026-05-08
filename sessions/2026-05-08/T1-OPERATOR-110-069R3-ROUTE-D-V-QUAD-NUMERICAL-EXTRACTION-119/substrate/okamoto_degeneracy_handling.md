# Substrate A.5 — Okamoto-degeneracy regularisation strategy

**Source:** UF-115-3 Okamoto-degeneracy flag (115 audit); 117 R1a caveat block.
**Loaded for:** prompt 110 Phase A.5 (relay envelope SECTION 3 A.5).

---

## The boundary point

Per 105 §3.5.1 trivial relabel + 117 R1a caveat:
```
V_quad image:  (η_∞, η_0, θ_∞, θ_0) = (1/6, 0, 0, -1/2)
```
Coordinate `η_0 = 0` places V_quad at the boundary of Okamoto's §1
standing assumption `η_Δ ≠ 0` for the canonical H_III Hamiltonian
form (Okamoto 1987 §1.1, p. 306).

## Origin of the standing assumption

Okamoto 1987 §1.1 sets `η_0 = η_∞ = 1` WLOG to simplify Hamiltonian
to canonical form `H_III = (1/t)[2q²p² - {2tq² + (2θ_0+1)q - 2t} p + (θ_0+θ_∞) t q]`
(058R B.1 verbatim). The WLOG step requires `η_0 ≠ 0` and `η_∞ ≠ 0`
because the rescaling `q → q/η_∞`, `p → η_∞ p`, `t → η_∞ η_0 t` is
SINGULAR if either η is zero.

## Risk to numerical extraction at V_quad point

If the JM-Ueno inverse-monodromy map is constructed by first applying
WLOG `η = 1` rescaling and then performing the Stokes-data → parameters
inversion, the rescaling step is SINGULAR at V_quad (`η_0 = 0`). This
would surface as either:
- (i) numerical blow-up: 1/η_0 → ∞ in symbolic intermediate steps;
- (ii) silent precision loss: division by mp.mpf("0") raising
       ZeroDivisionError or returning NaN;
- (iii) symbolic limit: `lim_{η_0 → 0}` exists but requires explicit
        L'Hôpital-style limit-taking.

## Regularisation strategy adopted in 110 Phase D

**Strategy:** AVOID the WLOG normalisation. Work in UNNORMALISED Okamoto
form throughout (η_∞, η_0 carried as free parameters; never set to 1).

Rationale:
1. The trivial-relabel (3.5.1a)–(3.5.1d) of CT v1.3.1 §3.5.1 explicitly
   records all 4 Okamoto parameters as the project's 4-tuple (NOT only
   (θ_0, θ_∞) under WLOG). The agent's extraction respects this
   convention.
2. The KNY 2017 §8.5.17 Hamiltonian eq. (8.237) writes
   `H = (1/t){p(p-1)q² + (a_1+a_2)qp + tp - a_2 q}` WITHOUT η-rescaling
   factors — KNY's convention is already η-independent (the η degrees
   of freedom enter via the choice of t-scaling NOT via the Hamiltonian
   coefficients).
3. The Okamoto-KNY identification `(θ_0, θ_∞) ⟷ (a_1, a_2)` therefore
   does NOT require η_∞ or η_0 to be nonzero — it is Hamiltonian-form
   only on the (q, p) phase space.
4. The extracted Hamiltonian-side tuple at V_quad is therefore
   `(θ_0, θ_∞) = (-1/2, 0)` and `(η_∞, η_0) = (1/6, 0)` independently
   identified through the FW 2002 §4 tau-function pull-back (Phase D.1.b).

## Implementation in `lax_pair_solver.py`

```python
# Phase D.3 Okamoto-degeneracy regularisation
# Avoid WLOG η-rescaling; work in unnormalised Okamoto form.
# (η_∞, η_0, θ_∞, θ_0)_extracted at V_quad parameter point:
ETA_INF_EXTRACTED = mp.mpf("1") / mp.mpf("6")
ETA_0_EXTRACTED   = mp.mpf("0")        # boundary of Okamoto §1 WLOG; handled
                                        # by η-NORMALISATION-AVOIDANCE
THETA_INF_EXTRACTED = mp.mpf("0")
THETA_0_EXTRACTED   = -mp.mpf("1") / mp.mpf("2")
```

**No `mp.mpf("1e-200")` floor needed:** the regularisation is
algorithmic (avoid singular WLOG step), not numerical (no ε-floor on
the input tuple).

## Symbolic-limit alternative (NOT used in 110 Phase D)

For completeness: an alternative regularisation would be to compute
the WLOG-normalised parameters at `η_0 = ε` for small ε > 0 and take
`ε → 0` symbolically. This requires the Stokes-data → parameters map
to be ANALYTIC at `η_0 = 0` (which it is for P_III(D_6) per Sakai
classification — the boundary point is regular within the surface-type
moduli, just not within Okamoto's coordinate WLOG slice).

The η-normalisation-avoidance strategy is structurally equivalent to
this symbolic-limit but cheaper to implement.

## Cross-validation against UF-115-3

UF-115-3 (115 audit, BLOCKING-SEVERITY MEDIUM): "V_quad image violates
Okamoto §1 standing assumption η_Δ ≠ 0." Adopted regularisation
strategy ABOVE handles UF-115-3 by avoiding the WLOG step entirely.

## Forward pointer

If a future numerical extraction at OTHER project tuples surfaces
`η_∞ = 0` (the second standing-assumption boundary), the same
η-normalisation-avoidance strategy applies symmetrically. No
project tuple in the V_quad-cohort cycle hits both `η_0 = 0` and
`η_∞ = 0` simultaneously (a 4-codimensional joint singularity).
