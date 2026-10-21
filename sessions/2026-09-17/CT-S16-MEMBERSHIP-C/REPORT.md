# CT-S16-MEMBERSHIP-C — REPORT

Session: `sessions/2026-09-17/CT-S16-MEMBERSHIP-C/`
Packet: operator review #12, issued verbatim.
Status: **steps 1, 2 and 3(a) complete. Step 3(b)/(c) NOT run** — see §6.
Nothing committed, deposited or sent. No notice or conjecture file was edited.

---

## 0. Headline

**The question was answered, and the answer is positive.**

System C satisfies every hypothesis under which van der Put–Saito build the
moduli space `M` for the `(0,0,1)` row, and it is an explicit point of their
chart `U₀`. Since Painlevé V *is* the isomonodromy foliation on that space, and
since the foliation's vector field is regular at that point, **exactly one PV
leaf passes through System C.** The deformation exists; it does not have to be
guessed.

Three things the operator will most want, stated up front:

1. **The operator's description of the framework, given from memory, is
   confirmed** against the page images. In particular `t` really is an invariant
   computed from the configuration — it is the *scale of the irregular type at
   ∞* — which is why System C comes with a fixed `t` and no deformation written
   down.
2. **The hypothesis flagged as most at risk came out SATISFIED, against my own
   pre-registration.** van der Put–Saito impose no semisimplicity and no
   non-resonance condition; they admit exactly the logarithmic local data that
   Jimbo's `(A1)` excludes. I pre-registered the expectation that this would
   fail. It did not. Pre-registration is the only reason that is reportable
   rather than invisible.
3. **A typo in the published paper**, caught by the paper's own constraint. See
   §2.

---

## 1. Step 1 — framework (INSPECTED, from page images)

Pages rendered from the local PDF and read **by looking**, one image per
message, per the P0 rule. Journal page = PDF page + 2609, verified from the
running heads.

**§3.2, p.2637** — for a type-`(0,0,1)` module the *strong* Riemann–Hilbert
problem has a positive answer. The module is `d/dz + A₀/z + A₁/(z−1) + A_∞`,
trace-zero constant matrices, `A_∞ = (t/2)·diag(−1,1)` with `t ∈ C*`,
`det A_i = −θᵢ²/4`, singular points normalised to `0, 1, ∞`.

> **No semisimplicity hypothesis. No non-resonance hypothesis.** Neither appears.

**p.2636** defines resonance as an eigenvalue difference in `Z\{0}`, and treats
resonance and reducibility as sources of *singularities of the monodromy space*
— such modules are **inside** `M`, not excluded from it.

**p.2656** supplies packet item 1(b) in exactly the required form, so the halt
condition did not fire:

> "the foliation given by the 2-form `Ω = dp∧dq/(q(q−1)) − dH_V ∧ dt` on
> `U₀ × (C\{0})` coincides with the foliation given by isomonodromy."

with the flow `(4.4)` and `H_V` `(4.5)` transcribed in `flow_regularity.py`.

Claims `S16-01` … `S16-04`.

---

## 2. A typo in the published paper (VERIFIED)

On **p.2655**, the entry `b(z)` of family `(4.1)` prints its first term as
`(p + ½(q−1)q)²` — with no `t` — while the second term carries `(q−1)q t`.

Tested against the paper's **own** constraint `det A(1) = −θ₁²/4`:

| reading | `det A(0) = −θ₀²/4` | `det A(1) = −θ₁²/4` |
|---|---|---|
| as printed | holds | **nonzero remainder** |
| `(p + ½(q−1)q t)²` | holds | **holds identically** |

`det A(0)` does not discriminate; `det A(1)` does. The corrected reading is used
throughout and is **flagged here rather than adopted silently** (`S16-05`).

Separately, the prose "`θ_∞` is the (1,1) entry of `A₀+A₁`" does **not** hold for
the printed family — it yields `−θ_∞/2`. I did not rely on it; all matching is
done through the projective normal potential, which is convention-free.

---

## 3. Step 2 — hypothesis check

| | hypothesis | verdict | label |
|---|---|---|---|
| H-a | local data admissible | **SATISFIED** | STRUCTURAL |
| H-b | irreducibility | **SATISFIED** | PROVEN |
| H-c | time invariant matches | **SATISFIED** | PROVEN |

**H-c first, because it is the cleanest.** System C's normal potential
`r_C(x) = (12x⁴+4x³+4x²+11)/(4(3x²+x+1)²)` has singular points
`s± = (−1±i√11)/6`. Under `x = s₊ + δz`, `δ = −i√11/3`, the poles are **only** at
`z = 0, 1`, both double with coefficient `−1/4`, and there is **no apparent
singularity**. At infinity `r_z = −11/27 + (i√11/27)/z + …`, so

> `t²/4 = −11/27` ⇒ **`t = ∓2i√33/9`** — *exactly* the companion's printed value.

The companion's `t` **is** van der Put–Saito's time invariant. There is no
mismatch to explain (`S16-06`, `S16-07`).

**H-a, against pre-registration.** A probe on three exact draws fixed the
dictionary: the double-pole coefficients are `(θ₀²−1)/4` and `(θ₁²−1)/4` and
`R(∞) = t²/4` (3/3 each). The naive `1/z` entry `tθ_∞/2` **failed all three**;
the data give `t(θ_∞+1)/2`. Those draws double as the vacuity control, since they
carry `θ₀ ≠ 0` and the observable reports it.

Hence `θ₀ = θ₁ = 0`, so `A₀, A₁` are **nilpotent and nonzero** — non-semisimple
local data, with a log term, as C1 requires. But the eigenvalue difference is
`0 ∉ Z\{0}`, so this is **not resonance in van der Put–Saito's sense**; and §3.2
imposes no semisimplicity condition in any case.

> **The operator's worry does not materialise in this framework.** The `D̃₅` row
> match is not confined to the level of formal type, and no framework admitting
> logarithmic local data has to be sought — this one already does (`S16-08`,
> `S16-09`).

**H-b.** Riccati test `w' + w² = r`, exactly: all poles simple; residues at `s±`
satisfy `A²−A = −1/4` so `A = 1/2`; `w` bounded at ∞ with `c₀² = 1/3`; matching
`r₁ = −1/9` forces `n = −1 ∓ √3/18`, irrational, hence not a non-negative
integer. Contradiction ⇒ **irreducible**. So C does *not* sit on the classical
Riccati locus (`S16-10`).

---

## 4. Step 3(a) — the point, located and verified

Overdetermined solve — five coefficient equations plus `b₁ = 0` in four unknowns
— **consistent**, with two branches:

| | `t` | `θ_∞` | `q` | `p` |
|---|---|---|---|---|
| 1 | `−2i√33/9` | `−2 − √3/9` | `≈ 0.5 + 0.8123 i` | `≈ 0.4649 i` |
| 2 | `+2i√33/9` | `−2 + √3/9` | `≈ 0.5 − 25.6278 i` | `≈ 396.2089 i` |

Exact forms in `outputs/pq_solution.txt`.

**Independently verified** (`verify_point.py`) by re-substituting into the
*general* formula for `R`, not the reduced closed form used to derive it:
`R − r_z` simplifies to `0` identically, worst relative residual over five points
at dps 60 being `5.8e-56` and `7.0e-61`; `b₁ = 0`; and `q ∉ {0,1}`, so the point
lies in the chart `U₀ ≅ C × (C\{0,1})` (`S16-12`, `S16-13`).

`θ_∞ = −2 ∓ √3/9`, not the `−1 ∓ √3/9` the generic dictionary predicts: the
`t(θ_∞+1)/2` entry was derived for non-constant `b`, and the `b′/b` term shifts
the behaviour at ∞ by one when `b₁ = 0`. The double-pole entries at `z = 0, 1` are
untouched, since `b`'s zero lies elsewhere, so `θ₀ = θ₁ = 0` stands.

---

## 5. Membership (STRUCTURAL)

All hypotheses SATISFIED; the point lies in `U₀`; `q(q−1) ≠ 0` and `t ≠ 0` there,
so the vector field `(4.4)` is **regular** at it and exactly one leaf passes
through. Since PV *is* the isomonodromy foliation, **System C lies on a PV
isomonodromic leaf** (`S16-14`).

**A caution on strength, and it matters.** The match is of **projective** normal
forms. What is established is that C's projectivisation is that of the family
member at `(p,q,t)` — equality **up to a rank-1 twist** — in precisely the sense
in which B and C were found projectively equivalent. That is why the label is
STRUCTURAL and not PROVEN, and the notice wording, if the operator ever uses
this, should say *projectively*.

**Consequence for C3** (`S16-16`): the "single fibre" concern is, on this
framework, a matter of **presentation** rather than a defect — `t` is an
invariant of the configuration, and every point of `M` already lies on a leaf.
**I have not acted on this.** The session is analysis-only and no notice or
conjecture file was touched; whether C3's wording changes is the operator's call.

---

## 6. What was NOT established

- **The pre-registered step-3(b) falsifier was NOT run** (`S16-15`). It requires
  monodromy *and Stokes* data at 30 digits for an irregular rank-2 system — a
  separate undertaking beyond this budget. **The threshold in `PREREG.md` is left
  unchanged**, and the regularity check in `flow_regularity.py` is reported as
  *supplementary*, not as a substitute. No label was raised to cover the gap.
- Step 3(c)'s vacuity pre-check belongs to 3(b) and likewise did not run.
- Whether **object A** — as opposed to the B/C class — lies in any such family is
  untouched here.
- Membership is established **up to a rank-1 twist**, per §5.

## 7. Defects caught in this session

All of one family: *a step that cannot fail cannot be trusted to report failure.*

1. **`irreducibility.py` was VOID** (`S16-11`). `sp.cancel((x-c)**2*r).subs(x,c)`
   returns `nan` for algebraic `c`; the admissible-residue list came out empty,
   the product over it was empty, and the verdict "IRREDUCIBLE" was reached **with
   no test performed**. Caught *only* because the reducible-by-construction
   control was also declared irreducible. Controls are now assertions. Related:
   `all(... for m in sp.roots(...).values())` is vacuously `True` on an empty
   dict.
2. **Page images that never rendered** (`S16-17`). `view` takes one image per
   message; two in one message returned "maximum number of images (1)" and
   displayed nothing — and I had begun reasoning from page content I had never
   seen. Stopped; every page was re-read alone. **Proposed P0 amendment, beside
   the OCR rule: confirm a page image actually displayed before quoting it.**

## 8. Open questions for the operator

1. **Report the p.2655 typo to the authors?** It is a genuine erratum in a
   published paper, found via their own `det A(1)` constraint.
2. **Does C3's wording change?** §5 says the single-fibre concern is
   presentational. I have deliberately not touched the notice.
3. **Should step 3(b) be commissioned** as its own packet, or is membership at
   STRUCTURAL sufficient for present purposes?
4. **Cold read?** Nothing here has had one. If any of this becomes load-bearing
   for a deposit, the four-route scoring says it needs one first.

## 9. Uncommitted files

All under `sessions/2026-09-17/CT-S16-MEMBERSHIP-C/`:

- `PREREG.md` (written before any computation), `REPORT.md`, `claims.jsonl` (17)
- scripts: `locate_pages.py`, `locate_snippets.py`, `render_pages.py`,
  `systemC_invariants.py`, `check_bz.py`, `probe_family.py`, `irreducibility2.py`,
  `locate_final.py`, `verify_point.py`, `flow_regularity.py`, `emit_claims.py`
- retained as records of caught defects / killed attempts: `irreducibility.py`
  (VOID), `locate_systemC.py`, `locate_systemC2.py`, `invert_dictionary.py`
- `outputs/` — one hashed `.out.txt` per script that ran, plus `pq_solution.txt`
- `pages/` — `vdps_p{2635,2637,2638,2639,2651,2654,2655,2656}.png`,
  `vdps_p2655_bz.png`, `vdps_p2656_HV.png`

Repo HEAD unchanged. Corpus now **276 claims**, all IDs unique, all five
invariants passing.
