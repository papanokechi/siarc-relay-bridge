# Evidence pack — suspected typo in van der Put–Saito, family (4.1), entry `b(z)`

Prepared for the operator's author letter. **Nothing has been sent.**
Findings: `S16-05`, `S16-18` … `S16-22`. Script: `typo_recheck.py`; output hashed
in `claims.jsonl`.

---

## 1. Where it appears

Identical in both versions:

| Source | Locator | Verified how |
|---|---|---|
| Ann. Inst. Fourier **59** (2009) 7, 2611–2667 | **p. 2655**, §4.3, the display defining `a(z), b(z), c(z)` | rendered at 8× and read by looking; running head asserted in the rendering script (`pages/vdps_j2655_bz_LOOK.png`) |
| **arXiv:0902.1702v5** | **p. 34**, same display | downloaded, rendered, read by looking (`pages/arxiv_v5_p34_bz_LOOK.png`); sha256 of PDF `1d4be8e4…d006e47` |

arXiv v5's comment records that *"the signs for Hamiltonian systems in Section 4
and the equations (3) (PV) and (7) (degenerate PV) are corrected"* — so §4 **was**
revised, and this entry was not among the corrections. A web check found **no**
published erratum or corrigendum.

## 2. What is printed

```
        z ( (p + ½(q−1)q)² − θ₁²/4 + (q−1)( θ₀²/4 − θ₁²/4 − qθ∞²/4 ) )
b(z) = − ──────────────────────────────────────────────────────────────
                                    q

         (q−1) ( p + ½((q−1)qt − θ₀ + qθ∞) ) ( p + ½((q−1)qt + θ₀ + qθ∞) )
       − ─────────────────────────────────────────────────────────────────
                                    q
```

The first term prints `(p + ½(q−1)q)²` — **no `t`** — while the parallel second
term carries `(q−1)qt` **twice**.

## 3. The test — the paper's own constraint

Since `A(z) = z(z−1)A_∞ + (z−1)A₀ + zA₁`, we have `A(0) = −A₀` and `A(1) = A₁`.
§3.2's `det A_i = −θᵢ²/4` therefore reads `det A(0) = −θ₀²/4`,
`det A(1) = −θ₁²/4`. **These are the authors' own equations**, not an external
assumption.

| reading | `det A(0)` | `det A(1)` |
|---|---|---|
| as printed | holds identically | **residual `−(q−1)(t−1)(4p + q²t + q² − qt − q)/4`** |
| `(p + ½(q−1)q t)²` | holds identically | **holds identically** |

`det A(0)` holds for both, so it does **not** discriminate; `det A(1)` does.

Concrete witness: at `p = 2/7, q = 5/3, t = 11/4, θ₀ = θ₁ = 0, θ∞ = 3/5` the
printed reading gives `det A(1) + θ₁²/4 = −223/144 ≠ 0`.

## 4. Corroborating structure

The residual carries the factor `(t − 1)`, so it vanishes **exactly at `t = 1`** —
which is precisely the value at which the two readings coincide, since
`(q−1)q·1 = (q−1)q`. A dropped factor of `t` produces exactly this signature.

*(Corroboration, not independent proof.)*

## 5. Control

A deliberately wrong variant, `(q−1)q t²`, is **rejected** by the same test. The
test therefore discriminates rather than accepting any perturbation.

## 6. Caveats to state plainly in any letter

- This is a **suspected** typographical error, inferred from an internal
  consistency condition. We have not seen the authors' source.
- The rest of §4.3 is unaffected so far as we checked; we did not audit the paper
  generally.
- Only `self` review: one worker, one code path. No independent reproduction.

---

## 5. DECISIVE CORROBORATION — the same bracket, printed correctly, on the same page

*Found at the CT-S19 adjudication, while checking a quotation from that cold read.*

The expression whose `t` is missing in `b(z)` **appears a second time on p. 2655**,
in the matrix `B₁` of the display `B = zB₀ + (1/t)B₁`. Its `(1,2)` entry prints:

```
            ( p + ½(q−1)q t )²  −  θ₁²/4  +  (q−1)( θ₀²/4 − θ₁²/4 − qθ∞²/4 )
    B₁[1,2] = − ──────────────────────────────────────────────────────────────
                                        q
```

**with the `t` present.** Compare `b(z)`'s first term, which prints the same
bracket **without** it. Read from `pages/vdps_j2655_B1_top_LOOK.png`, a 9×
render, confirmed by looking.

The two are related exactly:

| reading of `b(z)` | `b(z)` first term − `z · B₁[1,2]` |
|---|---|
| as printed (no `t`) | `z(4pqt − 4pq − 4pt + 4p + q³t² − q³ − 2q²t² + 2q² + qt² − q)/4` ≠ 0 |
| corrected (with `t`) | **`0`** |

So `b(z)`'s first term is **exactly `z · B₁[1,2]`** under the corrected reading,
and not under the printed one. Script `b1_corroboration.py`, output
`outputs/b1_corroboration.out.txt`, sha256
`0bb03ea1c8a9b0bb2049166024bc37ab34f456ee575a0e96b86015f7efa78cb8`. Three bogus
variants (`t²`, `t+1`, `2t`) are rejected by the same test, so it discriminates.

The difference between the two readings factors as

```
    −z(q−1)(t−1)(4p + q²t + q² − qt − q)/4 ,
```

carrying the **same** `(q−1)(t−1)(4p + q²t + q² − qt − q)` as the `det A(1)`
residual of §3 — the two independent tests agree on the correction, term for term.

### Why this changes the letter

The `det A(1)` argument shows the printed form is **inconsistent with a
constraint**. This shows the authors **print the expression correctly, with the
`t`, eight lines away**. That is a transcription slip, evidenced from the
authors' own page, and it needs no appeal to the correctness of any constraint.
This should lead the letter; the determinant argument becomes the corroboration
rather than the substance.
