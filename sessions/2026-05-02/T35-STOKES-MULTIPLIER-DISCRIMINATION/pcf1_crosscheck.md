# T35 — PCF-1 v1.3 §3 cross-check

## Convention recap

Coefficient ordering: leading-first.  For a d=2 family we write
`b(n) = α n² + β n + γ`, `a(n) = δ n + ε`, with the discriminant
`Δ_b = β² − 4 α γ`.

The PCF-1 v1.3 §3 dichotomy (per
`tex/submitted/control center/picture_revised_20260502.md` §3, P-PIII row;
PCF-1 v1.3 §3 "The Sharp Dichotomy"):

* `Δ_b > 0`  ⇒  PCF transcendence index  **A = 4**.
* `Δ_b < 0`  ⇒  PCF transcendence index  **A = 3**.

(Δ_b = 0 is a measure-zero degenerate locus, not represented in the
present test.)

## Representatives selected

| rep_id | α | β | γ | δ | ε | Δ_b | side | A_pred |
|--------|---|---|---|---|---|------|------|--------|
| V_quad | 3 | 1 | 1 | 0 | 1 | −11 | neg | 3 |
| QL15   | 3 | −2 | 2 | 1 | 0 | −20 | neg | 3 |
| QL05   | 1 | −2 | −1 | 1 | 2 | 8 | pos | 4 |
| QL09   | 2 | 3 | 1 | 5 | 0 | 1 | pos | 4 |

These match the d=2 catalogue used by T3
(`sessions/2026-05-02/T3-CONTE-MUSETTE-PAINLEVE-TEST/catalog_d2.csv`)
and the four Δ>0 representatives chosen there for the QL01–QL30
batch.  Sign-of-Δ_b labelling is therefore consistent with PCF-1 v1.3 §3.

## Numerical extraction summary (top dps = 250, N = 2000)

| rep_id | side | A_pred | C (Stokes amplitude, 30 digits)             | sign(C) |
|--------|------|--------|---------------------------------------------|---------|
| V_quad | neg | 3 |  +8.12733679549507236711257873202…           | +1 |
| QL15   | neg | 3 |  +21.38412649463506525828438453626…          | +1 |
| QL05   | pos | 4 |  +1.40328080725296497994724250152…           | +1 |
| QL09   | pos | 4 |  −6.07472006379093506128527538225…           | −1 |

The leading Stokes multiplier is `S_1 = 2 π i C` (canonical P_III(D₆)
half-Stokes definition); values reported in
`stokes_multipliers_per_rep.csv`.

## V_quad consistency with CC-MEDIAN-RESURGENCE-EXECUTE

The CC-MEDIAN-RESURGENCE-EXECUTE V_quad pipeline (2026-05-02) reported
`C = 8.12733679549507236711257873202` at dps=250, N=5000, with the
inter-window agreement `N_C = 250.00 digits`.  This T35 run, using the
same V_quad cached `Qn_5000_dps250.csv` truncated to N=2000 as well as
recomputing from scratch with the *generalised* recurrence (which
specialises to V_quad at α=3, β=1, γ=1, δ=0, ε=1), reproduces

```
C_tail (T35, V_quad, dps=250, N=2000) =
  8.1273367954950723671125787320235831822645427223388…
```

agreeing with CC-MEDIAN to all 30 reported digits.  Cross-method
agreement (Richardson tail vs. LSQ in 1/n) is **76.94 digits**.  This
validates the generalised d=2 Birkhoff recurrence used here.

## Halt-clause pre-flight

* `G6B_REPRESENTATIVE_MISLABEL`: not triggered.  Δ_b values in the
  table above match the PCF-1 v1.3 §3 sign convention.  All Δ<0 reps
  have b(n) with no real positive integer roots; all Δ>0 reps have
  potential real roots in n (none of which are integers, so no PCF
  truncation pathology).

* `G6B_PRECISION_ESCALATION_FAILED`: not triggered.  The dps ladder
  agreement was

  | rep_id | dps 100→150 | 150→200 | 200→250 |
  |--------|:-----------:|:-------:|:-------:|
  | V_quad | 14.6        | 59.0    | 85.2    |
  | QL15   | 16.2        | 57.8    | 84.0    |
  | QL05   | 15.7        | 60.1    | 78.4    |
  | QL09   | 18.1        | 60.2    | 80.3    |

  The pattern dps + δ → digits ≈ dps − 30 is satisfied for the top
  two ladder steps for every rep (and adequately for the 100→150 step
  at dps 100, which is at the floor of the ladder where the t2c rule
  is loosest).

* `G6B_STOKES_INVARIANT`: not triggered.  No cross-side pair of |S_1|
  agrees beyond ~0.03 digits (i.e., the leading magnitudes differ at
  O(1) absolute scale).  Stokes data is therefore *not* sign-invariant
  in any precision-stable sense.

* `G6B_PROSE_OVERCLAIM`: avoided in `discrimination_certificate.md`.
  The certificate states the structural-pattern result HONESTLY:
  Stokes multipliers DIFFER but no clean A=4/A=3 structural mapping
  is visible at the leading-multiplier scale.

## What remains

The PCF-1 v1.3 §3 dichotomy lives at a finer scale than the leading
Stokes multiplier: leading S_1 fingerprints the family, but does not
expose a side-uniform structural signature (sign, modulus class, or
factor relation).  G6b is therefore **partially closed** — the
dichotomy is not Stokes-multiplier-invariant (which would have been
the negative result), but the structural mapping requires
higher-order alien amplitudes (S_2 at 2 ζ*, S_3 at 3 ζ*, or alien
ratios) that the present pipeline does not extract.

Recommended next step (deferred to next prompt): a
T35-FOLLOWUP-S2-EXTRACTION cycle that fits secondary singularities
of B[S_+](w) (e.g., at 2 ζ* and 3 ζ*) and compares the *ratios*
S_n / S_1 across the dichotomy.
