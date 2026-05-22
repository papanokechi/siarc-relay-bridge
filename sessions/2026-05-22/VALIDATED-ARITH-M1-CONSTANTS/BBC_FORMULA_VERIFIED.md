# BBC 1997 formula verification — pre-coding paper read

**Source:** Bailey, D. H., Borwein, J. M., and Crandall, R. E. (1997).
_On the Khintchine Constant._ Math. Comp. **66** (217), pp. 417–431.
DOI: `10.1090/S0025-5718-97-00800-4`.

**Local cache:** `harness_certified/_lit_cache/khinchin.pdf`
**SHA-256:** `7DD18D84B93A36B85F4F94D23671A202258CB6517CCBAA5794EDEADD0E793793`
**Extracted text:** `harness_certified/_lit_cache/khinchin_text.txt` (19 pages, 36,140 chars).

**Retrieval timestamp:** 2026-05-22 ~JST (this session). Matches `lit-002` cache SHA → no
fidelity drift since 2026-05-15 verification.

---

## 1. The cited identity (paper verbatim, page 2)

> "The following example of which having been used by Shanks and Wrench to provide the
> first high-precision numerical values for K_0:
>
> &nbsp;&nbsp;&nbsp;&nbsp; **log(K_0) log(2) = Σ_{s=1}^∞ ( ζ(2s) − 1 ) / s · ( 1 − 1/2 + 1/3 − ⋯ + 1/(2s−1) )**     (1)"

— BBC 1997, p.2, eq. (1).

The inner alternating-harmonic partial sum is defined formally as `A_s` in Lemma 1(a) on page 3:

> &nbsp;&nbsp;&nbsp;&nbsp; **A_s := Σ_{m=1}^{2s−1} (−1)^{m−1} / m.**

So eq. (1) reads, in symbolic form:

$$
\log(K_0)\,\log(2) \;=\; \sum_{s=1}^{\infty} \frac{\zeta(2s) - 1}{s}\, A_s,
\qquad A_s := \sum_{m=1}^{2s-1} \frac{(-1)^{m-1}}{m}.
$$

This is the **load-bearing identity** for the M1 K_0 enclosure.

---

## 2. Work-order sketch vs. BBC paper — discrepancy table

The original Work Order presented a sketch of the BBC identity. Verifying it against the paper
**before any code fires** (per the work order's own VERIFY-before-coding clause) produces:

| Element | Work-order sketch | BBC 1997 eq. (1), verbatim | Status |
|---|---|---|---|
| Outer summation sign | `(-1)^{k+1}` factor present | NO outer alternation; all terms positive in the partial-sum direction (each `(ζ(2s)−1)/s` is positive; `A_s > 0`) | **CORRECTED** — outer sign removed |
| LHS | `log K_0 = Σ …` | `log(K_0) · log(2) = Σ …` — i.e. an extra `1/log(2)` factor is required on the RHS to get `log K_0` directly | **CORRECTED** — `1/log(2)` factor added |
| Inner sum | `Σ_{j=1}^{2k-1} (-1)^{j+1}/j` | `A_s := Σ_{m=1}^{2s−1} (-1)^{m−1}/m` — identical up to index renaming | OK |
| Convergence rate | "(ζ(2k)−1) → 0 geometrically (~4^{-k})" | Confirmed: `ζ(2s)−1 ≤ 4^{1−s} · (ζ(2)−1)` for s ≥ 1 (rigorous; proof in §3 below) | OK |

**Resolution:** the verified BBC identity (no outer sign, with `1/log 2` on the RHS) is what
`certified_constants.py` codes. The work-order sketch corrections are flagged here and in
`_M1_REPORT.md` Anomalies section.

The Honesty Note from the work order applies as-is: the M1 enclosure is rigorous **conditional
on BBC 1997 eq. (1)**. We are certifying the arithmetic, not re-deriving the identity itself.

---

## 3. Rigorous tail bound (proved here, coded in `certified_constants.py`)

**Claim.** For each s ≥ 1:
$$\zeta(2s) - 1 \;\leq\; 4^{\,1-s}\,(\zeta(2) - 1).$$

**Proof.** For n ≥ 2 and s ≥ 1, `n^{-2s} = (n^{-2})^s = (n^{-2})^{s-1} · n^{-2} ≤ (2^{-2})^{s-1} · n^{-2}`
since `n^{-2} ≤ 1/4` for n ≥ 2 and `(·)^{s-1}` preserves the inequality. Summing over n ≥ 2:
$$\zeta(2s) - 1 = \sum_{n\geq 2} n^{-2s} \;\leq\; 4^{1-s}\sum_{n\geq 2} n^{-2} = 4^{1-s}(\zeta(2)-1).$$
∎

**Claim.** For each s ≥ 1: `0 < A_s ≤ 1`. In particular `|A_s| ≤ 1`.

**Proof.** `A_s` is the partial sum of the alternating harmonic series at odd cut-off `2s−1`.
The odd partial sums of an alternating series with monotonically decreasing positive terms are
themselves monotonically decreasing and bounded below by the limit `ln 2`. Hence
`ln 2 ≤ A_s ≤ A_1 = 1`. ∎

**Tail bound.** For truncation `N`, let `T_N := Σ_{s>N} (ζ(2s)−1)/s · A_s`. Then:

$$
|T_N| \;\leq\; \sum_{s>N} \frac{(ζ(2s)-1)}{s}\,|A_s|
\;\leq\; \sum_{s>N} \frac{4^{1-s}(\zeta(2)-1)}{s}
\;\leq\; \frac{4(\zeta(2)-1)}{N+1}\sum_{s>N} 4^{-s}
\;=\; \frac{4(\zeta(2)-1)}{3(N+1)}\cdot 4^{-N}.
$$

Since the LHS of BBC eq.(1) is `log(K_0)·log(2)`, the tail bound on **log(K_0)** itself is:

$$
\boxed{\;\;|\,\text{tail}_{\log K_0}(N)\,| \;\leq\; \frac{4(\zeta(2)-1)}{3(N+1)\log 2}\cdot 4^{-N}\;\;}
$$

This is the closed-form bound enclosed as an Arb ball inside `certified_constants.py`
(function `bbc_tail_bound`). Every quantity (`ζ(2)`, `log 2`, the rational `4·(·)/(3·(N+1))`,
the power `4^{-N}`) is an Arb ball; the final tail is then added to the radius of the partial
sum to obtain a rigorous enclosure of `log(K_0) · log(2)`.

### 3.1 Truncation N for working precision P_bits

We require `(4(ζ(2)-1) / (3(N+1) log 2)) · 4^{-N} ≤ 2^{-P_bits}`. Since `4^{-N} = 2^{-2N}` and
the prefactor is `< 1` for `N ≥ 1`, a sufficient condition is `2N ≥ P_bits + safety`, i.e.
`N ≥ ⌈P_bits/2⌉ + safety`.

| P_bits | P_dps approx | Required N (safety = 64 bits) |
|---:|---:|---:|
| 7178   | 2160         | 3653                          |
| 14356  | 4321         | 7242                          |
| 28712  | 8642         | 14420                         |

The driver enforces this and **verifies** the realised tail bound (an Arb-computed ball, not a
heuristic estimate) is ≤ `2^{-P_bits}` before claiming the precision.

---

## 4. AEAL provenance footnote

This document is itself the evidence trail backing the AEAL claim
`bbc_1997_eq1_identity_cited` (claims.jsonl). The `output_hash` for that claim is the
SHA-256 of this file (post-write).
