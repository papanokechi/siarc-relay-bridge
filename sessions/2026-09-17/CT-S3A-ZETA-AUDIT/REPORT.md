# CT-S3A-ZETA-AUDIT — is ζ* = 4/√3 the same variable as ξ₀ = 2/√3?

- **Session ID:** CT-S3A-ZETA-AUDIT · **Date:** 2026-09-17
- **Mode:** read-only. **No computation was run.** No resurgence computation was
  started. No `PREREG.md` exists because P0 requires one only before running a
  computation, and none was run.
- **Nothing committed, pushed, tagged or deposited.**

## Verdict up front

**Classification (b): ζ\* and ξ₀ are different objects.**

ξ₀ = 2/√β₂ = |c| is the **action of a single formal solution** — the Newton-polygon
characteristic root appearing in `exp(c/u)`.
ζ\* = 4/√3 = 2ξ₀ is the **action difference** `|c₊ − c₋|` between the two
conjugate formal solutions, which is where the Borel transform of either one
actually has its nearest singularity.

This is precisely the alternative P1 itself names under (b): *"the distance
between ±ξ₀ in the u-plane."* They are **not** the same singularity in different
variables; the factor 2 is not a normalisation artefact. The Borel variable,
uniformiser and factorial normalisation are **identical** in both sources, which
is what rules out (a).

The ~1.7 % residual in CC-PIPELINE-G **is accounted for** (§4).

## 1. Files read (exact paths and hashes)

| Path | sha256 |
|---|---|
| `sessions/2026-05-01/THEORY-FLEET/H4/summary.md` | `98e9d8460349cad9de44a2acc46322a97f6adad0c669c955c308ffa940c18cf1` |
| `sessions/2026-05-01/THEORY-FLEET/H4/predictions.json` | `787fbbde672698b2d21e8510a292d247b5aec2f85771b847928d20306281140a` |
| `sessions/2026-05-01/CC-PIPELINE-G/vquad_recovery.py` | `32539d9e0d6b8d6217aab63800865d985b3087917b51e8f0f6c6dad32b842877` |
| `sessions/2026-05-01/CC-PIPELINE-G/newton_birkhoff.py` | `6c1c3ab4be1bc3bdf1371e6dc8c8ed179abb6ec6314520d4f8a4d7333f1b4d15` |
| `sessions/2026-05-01/CC-PIPELINE-G/results_vquad.json` | `2452ca27a37da70f5cc83ce8562d3ce3edfde68319b2d2e18ae9d05ea12e9d2f` |
| `sessions/2026-05-01/CC-PIPELINE-G2/g2_pade_borel.py` | `e54cfef708d8667b4bf9469dcb3fa1846dfde4d2d1965c33437f6ae43ce3b592` |
| `sessions/2026-05-01/CC-PIPELINE-G2/pade_singularity_log.json` | `0737e62d799812381f6eb0269dcd2957f69dbffb246938609335759df5c1b368` |

Also read: `THEORY-FLEET/H4/claims.jsonl`, `CC-PIPELINE-G/cc_channel_table_v2.tex`,
`CC-PIPELINE-G/run.log`.

> **Correction to P1's brief.** P1 cites "Channel Theory's **Proposition 3.3.A**".
> In the newest in-repo Channel Theory source (v1.3.1,
> `sessions/2026-05-08/T1-OPERATOR-CT-V131-3.5.1-R1A-AMENDMENT-VQUAD-CAVEAT-117/channel_theory_outline_v131_with_r1a_caveat.tex`)
> the object is **Conjecture 3.3.A★**, "Cross-degree universality of ξ₀". The
> statement `ξ₀ = 2/√β₂` that P1 actually wants is `\label{prop:xi0}` (L502),
> proven at d = 2. There is no Proposition 3.3.A.
>
> **Channel Theory v1.5 is not in this repo**, so "the v1.5 notice" referenced by
> P1 could not be read. The halving it describes was nevertheless located
> directly in the code (§3).

## 2. Verbatim extraction of the conventions

### 2a. CC-PIPELINE-G2 — `g2_pade_borel.py`, module docstring L5–12

This is the **decisive source**. Verbatim:

```
    f_+(u) = exp(c/u) u^rho (1 + sum_{k>=1} a_k u^k),
    c = +2/sqrt(3),  rho = -11/6,  beta_2=3, beta_1=1, beta_0=1, alpha_1=0, alpha_0=1.

The Borel transform B(zeta) = sum_{k>=0} a_k zeta^k / k! is convergent
in a disk and analytically continues; resurgence theory predicts the
nearest singularity at zeta* = 2 c0 = 4/sqrt(3) (action of the partner
formal solution f_-(u) = exp(-c/u) u^rho (...)).
```

- **Borel variable:** `ζ`, conjugate to `u`.
- **Series transformed:** the coefficients `a_k` of the Birkhoff formal solution
  `S(u) = 1 + Σ_{k≥1} a_k u^k`, i.e. the series *after* the exponential and the
  power `u^ρ` are stripped off.
- **Normalisation:** `k!` = **Γ(k+1)**.
- **Uniformiser:** `u = √z` (Gevrey-1 in `u`, Gevrey-2 in `z`).
- **Explicit factor of 2:** yes — `zeta* = 2 c0`, and it is *justified*, not
  asserted: ζ\* is "the **action of the partner formal solution** `f_-`".

### 2b. CC-PIPELINE-G — `newton_birkhoff.py::borel_radius`, L537–545

```
    """Estimate the radius |w*| of the nearest singularity of the
    Gevrey-1 Borel transform B[S](w) = sum a_k w^k / k! using
    Domb-Sykes (ratio of consecutive coefficients of S/k! style) or
    direct |a_k / k!|^{1/k} -> 1/|w*|.

    We compute the limit of |b_k|^{1/k} where b_k = a_k / k! for large k.
    We expect 1/|w*| to converge as k grows.  Returns the inverse, |w*|.
    """
```

Same `a_k`, same `k!` normalisation, same uniformiser. The variable is named `w`
instead of `ζ`; **`w` and `ζ` are the same variable.**

### 2c. CC-PIPELINE-G — the explicit halving, `vquad_recovery.py` L70–79

The halving P1 was told to look for is here, verbatim:

```python
    # The Borel-plane singularity location is the OTHER characteristic root
    # (resurgence: alien derivative connects f_+ with f_-).  Distance
    # |w*| = |c_+ - c_-| / 2 = |c|.  So expected w* = 2 c0 = 4/sqrt(3)?
    # Actually the standard resurgence result for a slope-1 Gevrey-1
    # series at u=0 with action c/u gives a Borel singularity at
    expected_borel_radius = xi0_lit
```

Two observations:

1. The comment's own arithmetic is **wrong**: `|c₊ − c₋| = |2c| = 4/√3`, so
   `|c₊ − c₋|/2 = |c| = 2/√3`. Writing `|w*| = |c_+ - c_-| / 2` *is* the halving.
   The very next clause then asks "So expected w* = 2 c0 = 4/sqrt(3)?" — the
   author noticed the contradiction and left it unresolved.
2. The code then picks the **halved** value, `expected_borel_radius = xi0_lit`
   = 2/√3, and the trailing comment is truncated mid-sentence.

So the halving is a **deliberated but unresolved** choice, not a silent one.
CC-PIPELINE-G2 later resolves it the other way (§2a), without the halving.

### 2d. THEORY-FLEET H4 — `summary.md` §1 and Step A/B

H4's stated convention is **schematic and explicitly unfixed**:

> "Let the formal Birkhoff expansion be written, **after the project convention
> is fixed**, as Φ(x) ~ Σ_{n≥0} a_n x^{n+λ} … Its Borel transform is
> **schematically** Φ̂(ζ) = Σ_{n≥0} a_n/Γ(n+λ+1) ζ^{n+λ}."

and Step A is literally an instruction to go and determine it:

> "**Step A — fix normalization.** Record the exact series convention used for
> `V_quad`: expansion variable, factorial normalization, sign convention, and
> whether the Borel transform uses `Γ(n+1)`, `Γ(n+λ+1)`, or a shifted
> convention."

Step B then **imports** the value rather than deriving it:

> "**Step B — lock the singular action.** Use the analytically established value
> `A = ζ* = 4/√3` rather than refitting it."

`predictions.json` repeats this: *"Use the exact action A = zeta_star = 4/sqrt(3).
Fix the Birkhoff/Borel normalization and factorial shift."*

**Therefore H4 is not an independent source for ζ\*.** It does not pin the
singularity; it inherits `4/√3` from CC-PIPELINE-G2 and flags the normalisation
as an open task. Any claim that "the H4 prediction pins ζ\*" overstates H4.

### 2e. Channel Theory — what ξ₀ is

From `CC-PIPELINE-G/cc_channel_table_v2.tex` caption (verbatim):

> "All families share Newton-polygon slope $1/2$ at $z=0$ (Gevrey-2 in $z$,
> Gevrey-1 in $u=\sqrt{z}$). $\xi_0 = |c|$ where $c$ is the slope-$1/2$
> characteristic root $c^2 = 4/\beta_2$."

So **ξ₀ = |c|**, a characteristic root — an *action*, one per formal solution,
with the two solutions at `c = ±2/√β₂`. ξ₀ is never defined as a Borel radius.

## 3. Classification

**(b) — a different singularity: the distance between ±ξ₀ in the u-plane.**

The conversion is exact and arithmetic:

```
c±  = ± 2/√β₂        (the two slope-1/2 characteristic roots)
ξ₀  = |c±|  = 2/√3                     (β₂ = 3)
ζ*  = |c₊ − c₋| = 2|c| = 2ξ₀ = 4/√3
```

Why (a) is excluded: classification (a) would require the two numbers to be the
same singularity read in different variables. They are not. §2a and §2b show the
Borel variable (`ζ` ≡ `w`), the transformed series (`a_k` of `S(u)`), the
normalisation (`k!` = Γ(k+1)) and the uniformiser (`u = √z`) are **identical**
across the two sources. With every convention held fixed, a factor of 2 cannot be
a change of variables. The 2 comes from the *resurgence geometry* — alien
derivative connecting `f₊` to `f₋` — not from a normalisation.

Why (c) is excluded: the stored materials are sufficient. `g2_pade_borel.py`
states the convention and the reason for the 2 explicitly.

**Label: STRUCTURAL.** This rests on reading definitions plus the standard
resurgence statement that the Borel transform of `S₊` is singular at the action
difference. It is not a proof, and no computation was run here. Per P1's own
instruction, a classification based only on reading definitions is STRUCTURAL at
most.

### Corollary for downstream sessions

P3 Part B step 3 warns: *"Do NOT call the result 'the Stokes constant S_{ζ\*}'
unless P1 established that ζ\* is this singularity."*

**P1 has established that ζ\* is the Borel singularity** (it is the partner
action, and it is where the singularity sits — §4 confirms numerically from
stored data). So the naming is permitted, **but the ξ₀ ↔ ζ\* identification is
not**: ζ\* = 2ξ₀, and any germ coefficient must be expressed against ζ\* = 4/√3,
never against ξ₀ = 2/√3.

## 4. The ~1.7 % residual in CC-PIPELINE-G — accounted for

**Yes, fully, by two compounding causes.**

Stored values (`results_vquad.json`):

```
borel_radius_numeric_plus   = 2.348440245504967212976427072585921923...
borel_radius_numeric_minus  = 2.348440245504967212976427072585921923...  (identical)
borel_radius_digits_agreement = -0.01444027165286647
xi_0_literature             = 1.154700538379251529018297561003914911...
```

**Cause 1 — the comparison was against the halved value.**
`vquad_recovery.py` sets `expected_borel_radius = xi0_lit = 1.1547…`. The measured
2.3484… is 2.034× that, so the recorded "digits agreement" is **−0.0144**, i.e.
*no agreement at all*. That −0.0144 is the headline number in the results file,
and it is an artefact of comparing against the wrong target. Against the correct
target ζ\* = 4/√3 = 2.309401…, the measured value is high by

```
2.348440… / 2.309401… = 1.016905…   →  +1.69 %
```

**which is the ~1.7 % residual P1 asks about.** So the residual only appears once
the halving is undone; before that, the discrepancy is 100 %, not 1.7 %.

**Cause 2 — the residual is root-test truncation bias, not a second singularity.**
`borel_radius` estimates `1/|w*|` by `|a_k/k!|^{1/k}` and averages the last
quartile. From `vquad_recovery.py`, `K_FORMAL = 200`, and the stored
`borel_sample_radii` run over **k = 193…200** only. For a branch point with
`b_k ≈ C k^σ (w*)^{-k}`,

```
|b_k|^{1/k} = |w*|^{-1} · exp( (ln|C| + σ ln k) / k )
```

so the root test converges only like `O(ln k / k)`. At k ≈ 196, `ln k / k ≈ 0.027`,
so an `O(1)` value of `σ` and `ln|C|` produces a **percent-level** bias — the same
order as the observed 1.69 %. This is a consistency estimate from the estimator's
own error term, **not** a numerical re-derivation (P1 forbids re-deriving it here).

**Independent confirmation from stored data.** `CC-PIPELINE-G2` redid this with
`K = 5000` and a Stahl conformal map. `pade_singularity_log.json` stores:

```
expected_zeta_star        = 2.309401076758503058036595122007829822590407005...
expected_zeta_star_value  = "4/sqrt(3)"
raw_pade      (m=60): smallest_pole_abs           = 2.310314863799356135633137154616...
conformal_pade(m=60): smallest_pole_abs_conformal = 2.309400429346603600679460442221...
```

The conformal Padé pole agrees with 4/√3 to **~7 digits**, against
CC-PIPELINE-G's 1.7 %. Increasing K from 200 to 5000 and replacing the root test
with conformal Padé collapses the residual. That is exactly the signature of
estimator bias and **excludes** a nearby secondary singularity as the cause.

`g2_pade_borel.py` additionally records a claim that *"Stahl conformal map (factor
`(1-zeta^2/zeta*^2)`) leaves no next-nearest Borel singularity within
`|zeta| < 2|zeta*|` at m=800"* — corroborating the absence of a competing
singularity.

**Label: STRUCTURAL** for the attribution of the residual to estimator bias
(reasoning from the estimator's error term plus comparison of two stored runs).
The underlying numbers are **VERIFIED** only in the sense that prior sessions
recorded them; this session re-ran nothing.

## 5. Claims with labels

| id | claim | label |
|---|---|---|
| S3A-01 | Both H4 and CC-PIPELINE-G/G2 use the same Borel variable (ζ ≡ w), the same series (`a_k` of `S(u)`), the same normalisation (`k!` = Γ(k+1)) and the same uniformiser (`u = √z`) | **STRUCTURAL** (file inspection) |
| S3A-02 | ζ\* = 2ξ₀ is the **action difference** `\|c₊ − c₋\|` of the two formal solutions, not ξ₀ in other variables → classification **(b)** | **STRUCTURAL** |
| S3A-03 | The explicit halving is `vquad_recovery.py` L70–72; it is deliberated and self-contradictory in the comment, and CC-PIPELINE-G2 resolves it against the halving | **VERIFIED** (file inspection) |
| S3A-04 | H4 does not derive ζ\*; it imports it and leaves the normalisation as open Step A | **VERIFIED** (file inspection) |
| S3A-05 | The ~1.7 % residual = root-test bias at k≈196 plus comparison against the halved target; G2 at K=5000 with conformal Padé reduces it to ~7 digits | **STRUCTURAL** |
| S3A-06 | "Proposition 3.3.A" does not exist; the in-repo object is Conjecture 3.3.A★, with `prop:xi0` carrying `ξ₀ = 2/√β₂` | **VERIFIED** (file inspection) |

## 6. What was NOT established

- **No computation was run**, so nothing here is VERIFIED in the numerical sense
  defined by P0. All numbers quoted are read from prior sessions' stored outputs.
- The **analytic type** of the singularity at ζ\* (algebraic, logarithmic, or
  algebraic-logarithmic) is untouched. H4 conjectures "square-root class" but
  says the exponent must be fitted.
- Whether `ξ₀` itself is *also* a Borel singularity (e.g. on another sheet, or of
  a different series) was **not** investigated and is not excluded.
- The content of Channel Theory v1.5, which is not in this repo.
- The 1.7 % attribution was not re-derived numerically, as instructed.

## 7. Open questions for the operator

1. **Channel Theory v1.5/v1.6 are absent from this repo.** The v1.5 notice about
   the halving could not be read. Where is that source? The v1.3.1 claims record
   points at `pcf-research/channel/…`, which does not exist on this machine.
2. **Does CT anywhere assert that ξ₀ *is* the Borel radius?** If so, that
   assertion is wrong by a factor of 2 and needs a correction notice. If CT only
   ever calls ξ₀ a characteristic root, then no CT statement is wrong and the
   error is confined to `CC-PIPELINE-G/vquad_recovery.py`, which G2 already
   superseded. This determines whether a corrigendum is needed.
3. **Should `CC-PIPELINE-G/results_vquad.json` be annotated?** Its
   `borel_radius_digits_agreement = -0.0144` is, as stored, a misleading
   artefact of the halved comparison. An add-only marker in the style of
   `SUPERSEDED_BY_VQ-N1.json` would fit repo convention. **No file was modified
   in this session.**
4. **H4 is stale in a second way**, beyond scope here but worth flagging: it
   frames everything as P-III(D6), while
   `sessions/2026-05-29/T1-SYNTH-VQ-N1-VQUAD-RECLASSIFICATION-APPLY` reclassified
   V_quad as doubly-degenerate P-V on Sakai D5^(1) with symmetry W(A3^(1)).
   H4's closed-form priors (claims H4-06, H4-07) are keyed to the superseded
   label. This affects P3 Part C's PSLQ basis and P5 directly.

## 8. Uncommitted files

All under `sessions/2026-09-17/CT-S3A-ZETA-AUDIT/`:

- `REPORT.md` (this file)
- `claims.jsonl`

No files outside this folder were created or modified.
