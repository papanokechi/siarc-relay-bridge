# DELTA-FREDHOLM-P0 — Phase-0 validation of the Fredholm-determinant representation of the pcf-delta constant

## VERDICT: **PASS**

The conjectured Fredholm log-determinant representation of the pcf-delta constant
δ(1,0,1) is **confirmed** to 65 significant digits by two fully independent
computational channels, both anchored to the certified reference value.

```
delta_A (spectral / Hadamard)  = 0.1238571943606263927285049897025908409675795458522965682131312667
delta_B (trace / closed-walk)  = 0.1238571943606263927285049897025908409675795458522965682131312667
delta_ref (pcf-delta v1.3)     = 0.12385719436062639272850498970259084096757955   (44 digits)

|delta_A - delta_B|  = 6.84e-66   ->  65 digits   (PRIMARY evidence: independent channels)
|delta_A - delta_ref| = 4.15e-45  ->  44 digits   (capped by delta_ref's own precision)
|delta_B - delta_ref| = 4.15e-45  ->  44 digits   (capped by delta_ref's own precision)
```

The A-vs-B agreement deepens monotonically with working precision
(52 digits at dps 90 → 65 digits at dps 120), which is the signature of a genuine
identity rather than a coincidental cancellation. All three pairwise agreements
exceed the 40-digit PASS threshold, and each channel's stated enclosure is
consistent with the observed differences (|A−B| < encl_A + encl_B).

## Object under test

Triple (A,B,C) = (1,0,1); b(k) = k²+1; u_n = 1/( b(n−1)·b(n) ) for n ≥ 2.
R_N = weighted independence polynomial of the path on indices {2..N} with vertex
weight u_i; R_N := R_N(1); **δ = log R_∞**. T is the edge-weighted path-adjacency
operator (zero diagonal, off-diagonal √u). Since Σ u_n < ∞, T is trace-class.

## T0 — LOCKED CONVENTION (hard gate, PASS)

A unique convention passes the finite identity to < 1e-80 at every M ∈ {1..12} and
every test λ (worst residual **7.75e-121**); all eight other (size, offset) variants
fail with residual O(0.3 .. 2). Stated verbatim:

```
matrix size     : s = M            (M = upper vertex index of R_M on {2..M})
off-diagonal    : T[j-1,j] = T[j,j-1] = sqrt(u_{j+1}),  j = 1..M-1
identity        : R_M(lam)^2 = det(I + lam*T^2)     equivalently  R_M = det(I + i*sqrt(lam)*T)
note (problem)  : the brief's T_M has size M+1 (off-diagonals sqrt(u_2..u_{M+1})),
                  so det(I + lam*T_M^2) = R_{M+1}(lam)^2   (an index +1 shift).
```

Consequence (the representation under test, now confirmed):
**δ = Σ_{s_k>0} log(1 + s_k²) = ½ log det(I + T²)**, a Fredholm log-determinant.

## T1 — TRACE SANITY (PASS)

½ Tr T_N² = Σ_{n=2}^{N} u_n: exact in rational arithmetic for N ∈ {5,10,25};
residual 0 at dps ≥ 80 for N = 1000.

## T2 — TWO INDEPENDENT CHANNELS

**Channel A (spectral / Hadamard product).** δ_A = log R_N (N up to 8000) plus an
analytic cluster tail Σ_l c_l ζ(l, N+1) whose coefficients (c4=1, c5=2, c6=1, …)
are obtained EXACTLY by truncated-power-series arithmetic on the depth-D backward
continued fraction for ρ_k = R_k/R_{k−1}. Enclosure **2.67e-61** (spread over
N∈{2000,4000,8000}, D∈{8,9,10}, jhi). The actual eigenvalues s_k of T_160 (Rayleigh-
quotient iteration on the exact tridiagonal) satisfy Σ_{s>0} log(1+s²) = log R_160 to
**80 digits** — explicitly exhibiting the Hadamard-product / spectral form.

**Channel B (trace / closed-walk series — independent of the continuant and of
eigenvalues).** δ_B = Σ_m (−1)^{m+1} τ_m/m, τ_m = ½ Tr T^{2m} computed as closed-walk
sums by window dynamic programming. The per-site bulk asymptotics are resummed
exactly (TPS in 1/n + Hurwitz ζ) for small m, with rigorous geometric tail bounds for
large m; m-series truncated at m = 68. Enclosure **8.84e-66**. Cross-checks:
- τ_1 = S = Σ u_n = 0.13066961898743246965362031790000019617826250656153 agrees to
  **75 digits** with the digamma closed form S = −Σ_ρ A_ρ ψ(2−ρ) over the four roots
  ρ ∈ {i, −i, 1+i, 1−i} of b.
- Observed τ-ratio limit **0.121042** = s_max² ( = u₂·O(1), u₂ = 0.1), as anticipated.
- Leading bulk coefficient a_{4m} = **C(2m,m)** (central binomial: 6,20,70,252,924 for
  m=2..6), so g_m(n) ~ C(2m,m)·n^{−4m}.

## T4 — PSLQ probe of s₁, s₂ (optional, on PASS): **NULL** (as expected)

s₁ = 0.347911270027626353587053728914300431478868100242…,
s₂ = 0.086591357309165582340269942304665526428003730544…
(converged: N=200 vs N=400 agree to ≥ 90 digits).
No integer relation of height ≤ 1e10 ties s₁ or s₂ to the basis
{1/j_{ν,k} : ν∈{0,½,1,3/2,2}, k≤3} ∪ {1, π, √2, √5, √10}. Raw PSLQ "hits" are
**precision-unstable** (entirely different coefficients at dps 90 vs 130) — classic
working-precision artifacts — and the basis-internal degeneracy j_{1/2,k} = k·π
(reciprocals 1/(kπ), Q-rank 1) is deflated before judging the target.

## Four-class grading of every result

| Result | Grade | Basis |
|---|---|---|
| Locked convention identity R_M²=det(I+λT²), M=1..12 | **VERIFIED** | residual 7.75e-121; 8 alternatives fail |
| Determinant factorization det(I+λT²)=P_s² and its match to the R-recurrence (all M) | **STRUCTURAL** | algebraic derivation (pre-analysis); underlies T0 |
| T1 trace sanity ½TrT²=Σu_n | **VERIFIED** | exact rational + dps |
| δ_A (spectral channel) | **VERIFIED** | enclosure 2.67e-61 |
| Spectral = continuant (Σ log(1+s²)=logR) | **VERIFIED** | 80-digit eigenvalue confirmation |
| δ_B (trace channel) | **VERIFIED** | enclosure 8.84e-66 |
| S=τ₁ closed form (digamma) | **VERIFIED** | 75-digit agreement |
| Analytic-tail (cluster / CF) enclosure derivations | **STRUCTURAL** | asymptotic series + geometric tail bounds |
| Leading bulk coefficient a_{4m}=C(2m,m); decay n^{−4m} | **STRUCTURAL** | exact integer match m=2..6 (TPS DP) |
| Two-channel agreement δ_A=δ_B (65 digits) ⇒ representation holds | **VERIFIED** | primary evidence; deepens with precision |
| The Fredholm representation as a closed-form *theorem* | **CONJECTURED** | overwhelmingly evidenced + structurally backed, but not analytically proven here |
| Bessel-zero hypothesis for s₁, s₂ | **CONJECTURED** | outcome NULL |

**PROVEN (machine-checked): none this session** — none was expected.

## Limitations (honest)

1. **Not a theorem.** This session establishes the representation to 65 digits by two
   independent channels plus a primary-source anchor; it does not deliver an analytic
   proof. The finite identity R_M²=det(I+λT²) is, however, a genuine algebraic identity
   (det(I+λT²)=det(I+i√λ T)·det(I−i√λ T) = P_s², whose recurrence equals the R-recurrence
   under the locked offset); together with trace-class convergence (Σu_n<∞) this makes
   δ = ½ log det(I+T²) structurally compelling, but the limit interchange is asserted
   numerically, not proven.
2. **Spec decay exponent corrected.** The brief states the per-site terms decay like
   n^{−8m}; the measured and TPS-derived decay is **n^{−4m}** (leading coefficient
   C(2m,m)). This forced the analytic small-m resummation (a naive cutoff is infeasible)
   and is reflected throughout Channel B.
3. **Reference comparison is anchor-limited.** delta_ref carries 44 digits, so the
   δ_A/δ_B-vs-ref agreements saturate at 44; the meaningful precision lives in the
   independent A-vs-B agreement (65 digits). delta_ref is the anchor, not the primary
   evidence — the two-channel cross-check is.
4. **Spectral confirmation is finite-N.** Σ_{s>0} log(1+s²)=logR is exhibited at N=160
   (80 digits); the headline δ_A uses the high-N continuant + analytic tail, not a sum
   over all eigenvalues of the infinite operator (that sum has a delicate dynamic range).
5. **Channel A enclosure is conservative.** Its 2.67e-61 spread (dominated by the
   shallowest sweep variant) is looser than its true accuracy — A in fact agrees with the
   independently computed B to 6.84e-66. The reported enclosures are rigorous upper
   bounds, deliberately not tuned to the observed difference.
6. **T4 caveat.** With a ~20-element basis at height 1e10, spurious PSLQ relations are
   expected below ~190 digits; the NULL verdict rests on the precision-stability screen
   (coefficients must be identical across dps), not on a single PSLQ call.

## Files

```
t0_convention_lock.py     # T0 hard gate (brute-force R_M, continuant anchor, convention sweep)
t2_spectral_channel.py    # Channel A: logR + analytic tail + eigenvalue (Rayleigh) confirmation
t2_trace_channel.py       # T1 + Channel B: closed-walk traces, TPS resummation, S closed form
t4_pslq_probe.py          # T4: PSLQ probe of s1,s2 with deflation + precision-stability screen
results.json              # locked convention, all deltas, enclosures, agreements, tau-ratio, runtimes
claims.jsonl              # one entry per load-bearing claim (schema + sha256 output hashes)
out/                      # per-phase JSON outputs and full-precision delta_A/delta_B/s1,s2
```

Run (dps as CLI arg), e.g.: `python t2_trace_channel.py 120 58`,
`python t2_spectral_channel.py 120`, `python t0_convention_lock.py 120`,
`python t4_pslq_probe.py 90`.
