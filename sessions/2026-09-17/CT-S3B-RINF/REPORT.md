# REPORT.md — CT-S3B-RINF (P3)

**Session:** `sessions/2026-09-17/CT-S3B-RINF/`
**Prompt:** P3 — Step 3B: `r_∞` for V_quad, the leading amplitude, and a PSLQ probe.
**Repo root:** `C:\LocalWork\siarc-relay-bridge`, branch `log-pv-01`, HEAD
`08aa0e2381b3dc37ee54a3200b7272755ca11d59` (unchanged; nothing committed).
**Prerequisite check:** `sessions/2026-09-17/CT-S3A-ZETA-AUDIT/REPORT.md` was read.
P1 **did** resolve the variable convention (verdict: classification **(b)**), so
Part C was executed as well as Parts A and B.

---

## 1. What was done

All three parts ran to completion.

* **Part A** — `r_∞` for V_quad by the `r_n` recurrence plus Neville
  extrapolation. One pre-registered *finding* was raised before any computation:
  the prompt's own acceptance threshold is unreachable (§3, S3B-F1).
* **Part B** — the leading amplitude `K` was derived in closed form
  (`DERIVATION.md`) and then confirmed numerically against
  `Q_n/Γ(dn+1)` on eight polynomials spanning `d = 2, 3, 4`.
* **Part C** — PSLQ probe on `r_∞` over the basis frozen in `PREREG.md` §5,
  at dps 500, 1000 and 2000. **Null result** at all three.

No falsifier fired.

---

## 2. Claims, with labels

Machine-readable record: `claims.jsonl` (9 claims, each with a sha256 of its
output file).

| id | Label | Claim (abridged) |
|----|-------|------------------|
| S3B-01 | **PROVEN** | The Part A `10^−3000` tail threshold is ill-posed; it needs `N ≈ 10^999.5`. |
| S3B-02 | **VERIFIED** | `r_∞`(V_quad) `= 1.0166044410585109363370972132676576869179835143890…`, nonzero, 180.25 digits (Part A). |
| S3B-03 | **PROVEN** | No root of `3n²+n+1` is a positive integer, so `Γ(1−r_i)` is finite; the Part A halt condition does not fire. |
| S3B-04 | **STRUCTURAL** | Closed form `K = r_∞ (2π)^((d−1)/2) d^(−1/2) / ∏ᵢ Γ(1−rᵢ)`, with `s = β_{d−1}/β_d + (d−1)/2`. |
| S3B-05 | **VERIFIED** | That closed form matches numerics to 109.66–114.69 digits over 8 cases. Falsifier F-B (<20 digits) did not fire. |
| S3B-06 | **VERIFIED** | Vacuity control passes: dropping the Γ-product collapses agreement to ≤0.75 digits. |
| S3B-07 | **STRUCTURAL** | Germ coefficient `A = K·Γ(s+1)` with exponent `−(s+1) = ρ_d`, at `ξ₀` — *not* at `ζ*`. |
| S3B-08 | **VERIFIED** | PSLQ NULL at dps 500 / 1000 / 2000, height bound `10⁶`, 10-element basis. |
| S3B-09 | **VERIFIED** | `r_∞`(V_quad) to **2317.8** confirmed digits. |

---

## 3. Finding S3B-F1 — the Part A threshold is ill-posed (declared pre-run)

P3 Part A step 2 asks to "choose `N` so the tail bound
`Σ_{k>N} |r|/|b(k)b(k−1)|` is below `10^−3000`".

For V_quad, `b(n) = 3n² + n + 1`, so `b(k)b(k−1) ~ 9k⁴` and

    Σ_{k>N} |r| / (b(k)b(k−1))  ≈  r_∞ / (27 N³).

This decays **polynomially**, not geometrically. Requiring `< 10^−3000` gives
`N ≈ 10^999.5` — about `10^995` times more iterations than are physically
executable. The threshold as written cannot be met by any machine.

Per P0 ("If a threshold proves ill-posed, report that as a finding") this is
reported rather than silently retuned. The substitute procedure — Neville
polynomial extrapolation in `x = 1/n` to `x = 0`, accepted on `N`-vs-`2N`
agreement — was written into `PREREG.md` §1 **before** any numbers were produced.

Generalisation: `r_∞ − r_n = O(n^{−(2d−1)})`. So the same threshold is ill-posed
at every degree `d`, merely less catastrophically as `d` grows.

---

## 4. Part A — `r_∞` for V_quad

**Coefficient tuple, taken from the repo, not guessed.** From
`sessions/2026-05-01/CC-PIPELINE-G/results_vquad.json` and
`newton_birkhoff.py`: V_quad is `b(n) = 3n² + n + 1`, i.e.
`β₂ = 3, β₁ = 1, β₀ = 1`, with the same `Q_n = b(n)Q_{n−1} + Q_{n−2}`,
`Q_{−1} = 0`, `Q_0 = 1` convention. The same file stores `ρ = −11/6` and
`ξ₀ = 2/√3`, both of which are consistent with `β₂ = 3, β₁ = 1`
(`−3/2 − 1/3 = −11/6`; `2/√3`).

**Root pre-check.** The roots of `3n²+n+1` are the complex-conjugate pair
`(−1 ± i√11)/6`. Neither is a positive integer, so every `Γ(1−rᵢ)` is finite
and no halt is triggered (claim S3B-03).

**Result (Part A run, dps 400, `N = 60000`, `L = 40`):**

    r_inf = 1.0166044410585109363370972132676576869179835143890949841775955919422234512933129270…

with `N`-vs-`2N` agreement **180.25 digits**. Nonzero, so hypothesis (H) of the
P4 theorem holds for V_quad and `Q_n` is *not* the minimal solution.

**Part C supersedes this** with 2317.8 digits (§6); the two agree on every
digit the shorter one asserts.

**Reconciliation with P2.** `CT-S2-RHO-D4/d2_anchor.json` records
`r_∞ = 1.0166044410585062…`, which differs from the above at the 14th digit.
This is **not** a contradiction: P2 used the raw `r_N` at `N = 20000` with no
extrapolation, and by `r_∞ − r_n ≈ r_∞/(27n³)` that value is expected to be good
to about 13.5 digits — exactly the `13.489` figure P2's own file records as its
diagnostic. P3's extrapolated value is the accurate one.

---

## 5. Part B — the leading amplitude `K`

### 5.1 Closed form (STRUCTURAL)

Derived in full in **`DERIVATION.md`**. With `b(n) = β_d ∏_{i=1}^{d}(n − rᵢ)`:

> **`Q_n / Γ(dn+1) = K · (β_d/d^d)^n · n^s · (1 + O(1/n))`**
> **`s = β_{d−1}/β_d + (d−1)/2`**
> **`K = r_∞ · (2π)^((d−1)/2) · d^(−1/2) / ∏_{i=1}^{d} Γ(1 − rᵢ)`**

Chain: `Q_n = r_n ∏_{k≤n} b(k)` exactly → `∏_{k≤n} b(k) = β_d^n ∏ᵢ Γ(n+1−rᵢ)/Γ(1−rᵢ)`
by telescoping `Γ(x+1)=xΓ(x)` → `Γ(n+1−r)/Γ(n+1) ~ n^{−r}` with
`Σᵢ rᵢ = −β_{d−1}/β_d` (Vieta) → Gauss multiplication for `Γ(dn+1)`, whose
`Γ(n+1)^d` cancels exactly against the product. **One gap (G1):** the classical
Gamma-ratio asymptotic is quoted, not proved. Hence STRUCTURAL, not PROVEN.

Note `s` here is produced by a route (Vieta + Gauss multiplication) that shares
no code with P2's numerical fit, yet reproduces P2's `s` exactly. That is an
independent corroboration of the P2 growth law.

### 5.2 Numerical verification (VERIFIED)

dps 160, Richardson/Neville in `1/n`. Falsifier F-B was "agreement below 20
digits"; observed agreement is **109.66–114.69 digits** everywhere.

| case | d | s | K (26 digits) | agreement (digits) | control (Γ-product omitted) |
|---|---|---|---|---|---|
| `3n²+n+1` (V_quad) | 2 | 5/6 | `3.055706807890481365701912…` | 113.66 | 0.16 |
| `n²+1` | 2 | 1/2 | `7.374798176027376814456881…` | 112.99 | −0.43 |
| `2n²−3n+5` | 2 | −1 | `27.47953836114786720143473…` | 112.64 | −1.14 |
| `n³−2n−3` | 3 | 1 | `−0.47654609141093472745314…` | 114.16 | −0.07 |
| `2n³+n²+1` | 3 | 3/2 | `6.004870189510790948137733…` | 113.75 | 0.20 |
| `n⁴−3n³−3n²+n+1` | 4 | −3/2 | `−4.75420451208950088814010…` | 109.66 | −0.20 |
| `n⁴+1` | 4 | 3/2 | `17.58274559040649149493303…` | 114.69 | −0.07 |
| `7n⁴+n` | 4 | 3/2 | `9.272030931369776754901277…` | 113.61 | 0.75 |

The **control** column is the pre-registered vacuity check: recompute `K` with
`∏ᵢΓ(1−rᵢ)` deleted. Agreement collapses from ~110 digits to ≤0.75 digits in
every case, so the test genuinely probes the Gamma product and is not vacuous.

Coverage includes negative `K` (two cases) and sign-changing `b` (the `d=3` and
`d=4` cases with negative coefficients), so the formula is not an artefact of
positivity.

**Methodological note (recorded because it nearly produced a false negative).**
The first Part B run reported agreement of exactly `−0.30` digits in two cases.
`−0.30 = −log₁₀2` is the exact signature of a *pure sign flip* with otherwise
perfect magnitude agreement. Cause: `Q_n` was being reconstructed from
`log|Q_n|`, which discards the sign. Fix: carry `sign(Q_n)` via the rescaled
iterate (`mp.sign(cur)`). After the fix all eight cases agree. No threshold was
changed; only a genuine implementation bug was repaired.

### 5.3 Germ coefficient (STRUCTURAL) — with the P1-mandated caveat

Let `B(w) = Σ_n Q_n w^n / Γ(dn+1)` (this is the normalisation established in
P1; `Γ(dn+1) = (dn)!`, and the variable is `w`, with `ζ = w^{1/d}`). From
`Q_n/Γ(dn+1) ~ K λ^n n^s`, `λ = β_d/d^d`, and `Σ_n n^s x^n ~ Γ(s+1)(1−x)^{−(s+1)}`
as `x → 1⁻`:

    B(w)  ~  K · Γ(s+1) · (1 − w/w*)^{−(s+1)},     w* = d^d/β_d.

So the **leading Borel-singular-germ coefficient is `A = K·Γ(s+1)`**, with
singular exponent `−(s+1)`, which is precisely the `ρ_d = −s−1` of P2.

For V_quad: `d = 2`, `s = 5/6`, `−(s+1) = −11/6 = ρ` — matching the stored
`ρ = −11/6` in `CC-PIPELINE-G`.

> **Caveat, required by P1.** This germ sits at the **radius-of-convergence**
> singularity, i.e. at `ξ₀ = 2/√3` (`w* = 4/3`). Session `CT-S3A-ZETA-AUDIT`
> returned classification **(b)**: `ζ* = 4/√3 = 2ξ₀` is a *different*
> singularity — the **action difference** `|c₊ − c₋|` of the two formal
> solutions, not a rewriting of `ξ₀` in other variables. Therefore `A` above is
> **not** the Stokes constant `S_{ζ*}` and must not be labelled as such. P3 Part
> B step 3's instruction was explicit on this point and it is honoured here.

---

## 6. Part C — PSLQ probe (null result)

**Basis, frozen in `PREREG.md` §5 before running** (10 elements):
`r_∞`, `1`, `π`, `√3`, `Γ(1/3)`, `Γ(2/3)`, `log 2`, `log 3`, `|Γ(1−r₁)|`,
`Re Γ(1−r₁)`. No basis element was added or removed after seeing any result.

**Precision.** PSLQ at dps `p` requires `r_∞` to noticeably more than `p`
digits; the script refuses any `p` not backed by confirmed digits. Reaching
dps 2000 therefore required improving `r_∞` well past Part A's 180 digits.
The Neville nodes were spread (`n = N, N+stride, …`) rather than consecutive,
which greatly improves conditioning:

| configuration | confirmed digits |
|---|---|
| `N=60000, L=460, stride=1` | 953.9 — supports dps 500 only |
| `N=20000, L=520, stride=400` | 1846.6 — supports dps 500, 1000 |
| `N=20000, L=640, stride=520` | **2317.8** — supports all three |

**Result — NULL at dps 500, 1000 and 2000**, with `maxcoeff = 10⁶`.

Per the prompt, a null result is a valid outcome. What it excludes: **there is
no integer relation among those 10 constants with coefficient height `≤ 10⁶`.**
This does not exclude relations of greater height, nor relations involving
constants outside the frozen basis. The acceptance criteria (identical at all
three precisions, height `≤ 10⁶`, re-verified at dps 3000) were never reached
because no candidate relation was produced at any precision.

`r_∞` to 2317 digits is stored in `rinf_highprec.txt` for any future probe with
a differently-motivated basis.

---

## 7. What was NOT established

* **`K` is not PROVEN.** Gap G1 in `DERIVATION.md`: the classical asymptotic
  `Γ(n+1−r)/Γ(n+1) = n^{−r}(1+O(1/n))` is quoted, not proved. Everything else in
  the chain is exact or elementary. Closing G1 would upgrade the label.
* **No closed form for `r_∞`.** The PSLQ probe is null over the pre-registered
  basis. `r_∞` remains a numerically-known constant only. No derivation motivating
  a `0F1`/`1F1`/Bessel enlargement of the basis was found, so per the prompt's
  own condition none was added.
* **The analytic type of the `ξ₀` singularity is untouched.** `A = K·Γ(s+1)`
  is a leading-coefficient statement; it does not establish that the singularity
  is a pure branch point of exponent `−(s+1)` versus that plus logarithms or
  subleading structure.
* **Nothing about `ζ* = 4/√3` was computed.** Per P1, that is a different
  singularity, and P3 was explicitly forbidden to name it. No Stokes constant
  was extracted.
* **No resurgence / alien-derivative computation** was attempted.

---

## 8. Open questions for the operator

1. **Should `r_∞` have a closed form at all?** The null PSLQ result over a
   plausible Gamma/log/π basis is mild evidence that it does not, or that the
   right basis involves objects nobody has derived yet. Is there a structural
   reason (a period interpretation?) to expect one? If the operator can supply a
   motivated basis, `rinf_highprec.txt` (2317 digits) is ready.
2. **Is the `ξ₀` germ the object the programme actually wants?** P1 says the
   literature's `ζ*` is the action *difference*. The quantity P3 can compute
   cleanly (`A = K Γ(s+1)`) lives at `ξ₀`. If the programme needs the `ζ*`
   Stokes constant, that is a genuinely different computation and P3 has not
   advanced it.
3. **Confirm the Part A threshold finding is accepted** as a finding rather than
   a failure, and that the Neville substitute (pre-registered) is acceptable for
   the record.
4. **Does closing Gap G1 matter?** If a PROVEN label on `K` is wanted, the
   Gamma-ratio asymptotic needs an explicit error-term proof; it is standard but
   would need to be written out (and, for P4 Task B, found in Mathlib).

---

## 9. Uncommitted files (all new, all under `sessions/2026-09-17/CT-S3B-RINF/`)

| file | role |
|---|---|
| `PREREG.md` | pre-registration: finding S3B-F1, substitute procedure, falsifiers F-A/F-B/F-C, vacuity control, frozen PSLQ basis |
| `DERIVATION.md` | full symbolic derivation of `K`, with Gap G1 marked |
| `REPORT.md` | this file |
| `claims.jsonl` | 9 labelled claims with sha256 output hashes |
| `rinf_amplitude.py` | Parts A and B |
| `partC_pslq.py` | Part C (high-precision `r_∞` + PSLQ at 3 precisions) |
| `make_claims.py` | emits `claims.jsonl` with hashes |
| `rinf.json` | Part A output (sha256 `bd38057cf84cae47…`) |
| `amplitude.json` | Part B output (sha256 `b1ce056d8535d332…`) |
| `pslq.json` | Part C output (sha256 `d62ada5df9bb4211…`) |
| `rinf_highprec.txt` | `r_∞` to 2317 digits (sha256 `4980093f647ec10f…`) |
| `partA.log`, `partB.log`, `partC.log` | run transcripts |

**Nothing was committed, pushed, tagged, or submitted.** No file outside
`sessions/2026-09-17/` was modified; all repo materials from earlier sessions
were read only. HEAD remains `08aa0e2`.
