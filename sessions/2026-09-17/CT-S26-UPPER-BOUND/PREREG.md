# CT-S26-UPPER-BOUND — PREREG

**Written before any computation was run.**

Scope: close the single open drafting item recorded in
`CT-S24-PAPER-OUTLINE/OUTLINE.md` §2 (revision 5, item II) and in
`CT-S24-PAPER-OUTLINE/REPORT.md` §5 — the **upper bound** on `r_∞`, which the
outline's §1 ¶2 method paragraph asserts as half of a "two-sided bound" but
which exists nowhere in the corpus.

---

## 1. The gap, stated exactly

`CT-S1-THEOREM/theorem.tex` proves, for the recurrence

```
Q_{-1} = 0,  Q_0 = 1,  Q_n = b(n) Q_{n-1} + Q_{n-2}   (n >= 1)
B_n = prod_{k=1..n} b(k),   r_n = Q_n / B_n
```

under (A1) (`b` a polynomial of degree `d >= 1`, `b(n) != 0` for `n >= 1`):

| source | lines | statement | claim |
|---|---|---|---|
| `prop:exists` | 109–111 | `r_n -> r_∞` unconditionally, by absolute summability of the increments and telescoping | `S1-01` PROVEN |
| `prop:positive` | 123–136 | if `b(n) > 0` for all `n >= 1` then `r_n` is strictly increasing with `r_n >= 1`, so **`r_∞ >= 1`** | `S1-02` PROVEN |

That is the **lower** half only. The outline's method paragraph says "with a
two-sided bound", and a search of the `.tex` sources for an upper bound of the
form `r_∞ <= exp(sum ...)` returns nothing (`S24-21`). The outline therefore
carries the upper bound as an **unfolded drafting addition with no claim id**,
with the explicit instruction that it must **not** be written citing `S1-02`,
and with the pre-declared alternative of weakening §1 ¶2 to the one-sided form.

**Provenance warning carried forward.** The bound came out of a from-scratch
derivation in conversation and was never written back to the source of record.
That is the same shape as the Odlyzko citation living outside the worktree
(`S24-12`): a result believed because it was once derived, not because it is
written down anywhere checkable. This session exists to remove that status.

## 2. Hypothesis

**U.** Let `b` be a polynomial with `deg b = d >= 1` and `b(n) > 0` for every
integer `n >= 1`. Then `Σ_{k>=1} 1/(b(k) b(k+1))` converges, and for every
`n >= 1`

```
r_n  <=  exp( Σ_{k=1}^{n-1} 1/(b(k) b(k+1)) )                      (U-finite)
```

and consequently

```
1  <=  r_∞  <=  L := exp( Σ_{k>=1} 1/(b(k) b(k+1)) )  <  ∞ .       (U-limit)
```

`(U-finite)` is the object actually tested: it is an **exact finite-`n`
inequality**, checkable at every `n` without any limit or tail estimate, and
`(U-limit)` follows from it by monotone passage to the limit. Testing the
finite form rather than the limit form is deliberate — it removes the tail
estimate from the falsifier and so removes the place where a numerical
"agreement" could be manufactured by a loose tail bound.

**The proof is claimed to be complete and elementary**, and is written out in
`PROOF.md` **before** the numerics are run. The numerics are a check on the
proof and on the transcription, **not** its evidence. The proof carries the
label PROVEN; no numerical arm may be cited as if it established `U`.

## 3. Observables

1. For each test polynomial `b` and each `n` in `2..N`, the **slack**
   `S_n := exp(Σ_{k=1}^{n-1} 1/(b(k)b(k+1))) - r_n`. Hypothesis U says
   `S_n >= 0` for all `n`.
2. The **ratio** `R := r_N / exp(Σ_{k=1}^{N-1} ...)`, in `(0, 1]`.

`N = 20000`, mpmath at `dps = 60`.

## 4. Falsifiers, with thresholds fixed now

| # | Falsifier | Consequence |
|---|---|---|
| F1 | `S_n < -1e-40 * max(1, r_n)` for any test `b` and any `n <= N` | **U is false as stated.** Report it as a refutation of the outline's §1 ¶2, take the pre-declared fallback in §6, and do **not** adjust the statement to fit. |
| F2 | The engine control V1 agrees to fewer than **40 digits** | The recurrence implementation is wrong. **Halt and debug; report no result.** |
| F3 | The can-fail control V4 finds **no** violation anywhere | The inequality check cannot detect a violation on this family, so the passes in V3 are uninformative. **Report the test as vacuous** rather than reporting a pass. |
| F4 | The spread control V5 shows every ratio within `0.01` of `1` | The bound is satisfied only trivially on this family. Not a refutation, but the numerics must then be reported as **weak**, and said to be so. |

## 5. Vacuity pre-checks — registered before running, and run before the result is consulted

- **V1 (known-answer, positive).** `y_n = (-1)^n I_n(2)` satisfies
  `y_n = n y_{n-1} + y_{n-2}` exactly, because the modified Bessel functions
  obey `I_{ν-1}(2) - I_{ν+1}(2) = ν I_ν(2)`. Check the residual for
  `n = 2..40` against `b(n) = n`. **Threshold: >= 40 digits.** This tests the
  recurrence engine against an independently known solution, not against
  itself.
- **V2 (known-answer, negative).** The same check on a deliberately perturbed
  sequence `y_n (1 + 1e-20 δ_{n,7})` must **fail**. Guards against a residual
  computation that returns zero regardless of input.
- **V3 (the main arm).** `(U-finite)` at every `n <= N` for every test `b`.
- **V4 (can the check fail?).** Re-run V3 against the **weakened** bound with
  the `k = 1` term deleted, `exp(Σ_{k=2}^{n-1} ...)`. This is a genuinely false
  inequality for `r_2 = 1 + 1/(b(1)b(2))`, so a correct checker **must** report
  a violation. **If it does not, F3 fires.** *This is the arm the existing P0
  rules would not have supplied: it tests whether the inequality check is
  capable of returning a negative at all, independently of whether U is true.*
- **V5 (is the bound informative?).** The ratios `R` across the family must
  span a range. A family on which every ratio is `1` to 40 digits would satisfy
  `(U-finite)` for reasons having nothing to do with the argument.
- **V6 (is positivity load-bearing?).** Search sign-changing `b` (with
  `b(n) != 0` for `n >= 1`) for a violation of the positivity-free reading of
  `(U-finite)`. **Not a gate.** Either outcome is reported as found: a
  violation shows the hypothesis `b > 0` is necessary, and no violation is
  reported as *not established*, **not** as evidence that the hypothesis can be
  dropped.

**Basis-degeneracy pre-check (P0 Amendment A):** *not applicable, and said so
rather than skipped.* There is no basis and no integer-relation search here;
the test family is a list of polynomials, and its only role is to exercise an
inequality whose proof is independent of it.

## 6. Pre-declared fallback, fixed before any work

If **F1** fires — U is false — then the drafting instruction is the one already
recorded in the outline: **weaken §1 ¶2 to the one-sided statement** `r_∞ >= 1`
from `prop:positive`, and delete the upper bound from the outline entirely.
Nothing downstream depends on the upper bound; it is an expository
strengthening only. Taking the fallback is a recorded outcome, not a failure.

If **F2** fires, no result is reported at all.

## 7. Method notes

- The proof is written in `PROOF.md` **before** `scripts/upper_bound.py` is
  run, and the script does not read it.
- Every script reads back what it wrote, and hashes **from disk**.
- **Artefact hashing (P0 Amendment B):** this session writes only new output
  paths; no output already cited by an existing claim is touched. In particular
  `CT-S24-PAPER-OUTLINE/outputs/verify_outline*.out.txt` are read-only here,
  and any re-run of that checker goes to a new filename.
- `CT-S1-THEOREM/theorem.tex` is **not modified** — it belongs to an earlier
  session. The result is recorded here and referenced from the outline.
