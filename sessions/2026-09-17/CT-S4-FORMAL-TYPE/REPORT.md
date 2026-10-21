# REPORT.md — CT-S4-FORMAL-TYPE (P5)

**Session:** `sessions/2026-09-17/CT-S4-FORMAL-TYPE/`
**Prompt:** P5 — Step 4 pre-test: formal type versus the P_V linear system.
**Repo root:** `C:\LocalWork\siarc-relay-bridge`, branch `log-pv-01`, HEAD
`08aa0e2381b3dc37ee54a3200b7272755ca11d59` (unchanged).
**Status:** steps 1 and 2 **complete**; step 3 **not executed — halted as the
prompt instructs** (no classification table in the repository); step 4 verdict
given as far as steps 1–2 allow.
**No conjecture was revised in any file.** Nothing was committed.

---

## 1. Headline

The two objects are **formally different**, and the difference is *exactly* a
ramified double cover:

| | System A — Channel Theory object | System B — the `D5^(1)` object |
|---|---|---|
| what it annihilates | `f(z) = Σ Q_n z^n` (PCF numerators) | `φ(z) = Σ a_n z^n` (Riccati/WKB series) |
| type at `z = 0` | **irregular, RAMIFIED** | **irregular, UNRAMIFIED** |
| ramification index | **2** | **1** |
| Katz invariant at `0` | **1/2** | **1** |
| exponential parts at `0` | `exp(∓(2/√3)·z^{−1/2})` | `exp(∓(1/√3)·z^{−1})` |
| other finite singularities | none | `ρ± = (−1±i√11)/2`, regular singular |
| at `∞` | irregular, RAMIFIED, Katz 1/2 | regular singular |

Both of the prompt's premises are **confirmed**: Channel Theory does have a
slope-1/2 (ramified) edge at `z = 0`, and the `D5^(1)` object is unramified.

But they are not simply incompatible. Pulling System A back along the ramified
double cover `z = w²` doubles its Katz invariant, `1/2 ↦ 1` — landing exactly on
System B's value. And `w = √z` is precisely the uniformiser `u = √z` that
Channel Theory already uses. So the honest verdict is **(c)**, with the
transformation named (§6).

---

## 2. Step 1 — which linear system is the `D5^(1)` attribution about?

### 2.1 A missing-data finding: the companion paper is not in this repo

> **AMENDED IN AUDIT ROUND R1 (`CT-R1-AUDIT`).** The original heading read
> *"there is no Conjecture 4.1"* and asserted a citation defect. That
> overstated what was checked. The correction is below; the original reasoning
> is retained after it for provenance.
>
> **SUPERSEDED IN ROUND R2 (`CT-R1-AUDIT`, operator ruling 2).** The companion
> paper was obtained from Zenodo (concept DOI `10.5281/zenodo.20455089`) and
> all three versions are now in `CT-R1-AUDIT/refs/` with sha256 recorded.
> The question is settled, and the operator's version hypothesis is confirmed
> exactly:
>
> * **v1.0** (`…20455090`, the version this repo cites) — object 4.1 is a
>   **Theorem**.
> * **v1.1** (`…20480603`) — object 4.1 is a **Theorem**.
> * **v1.2** (`…20481592`) — object 4.1 is a **Conjecture**.
>
> So "Conjecture 4.1" does exist, from v1.2 onward; it is simply absent from
> the version the bibliography points at. There is no citation defect of the
> kind originally alleged, only a version mismatch.
>
> **Conjecture 4.1 is about neither System A nor System B.** It concerns a
> third ODE (companion §2.2, eq. (6)–(7)), recorded here as **System C**:
> `(3x²+x+1)y'' + (6x+1)y' − x²y = 0`, exact because `b = a'`. Its finite
> singular points are `(−1 ± i√11)/6`, which coincide exactly with those of
> the *inverted* System B. The conjecture also states its own weakness: the
> `D5^(1)` determination *"rests on a match against the Jimbo–Miwa–Ueno
> classification table [5] and is not yet corroborated by an independent
> Lax-pair derivation"* — and the JMU tables exclude ramified cases, which is
> the phenomenon at issue. Details in `CT-R1-AUDIT/AUDIT.md` §R2.1 and
> `CT-R1-AUDIT/CLASSIFICATION-TABLE.md` §6. The halt recorded as claim S4-08
> is **lifted**. No conjecture file was edited.

P5 asks me to identify the system that "Conjecture 4.1" is about. What I
actually searched was
`sessions/2026-06-15/VQUAD-PERIODREP-PAPER-001/` — the **period-rep paper**.
That is *not* the V_quad companion. The companion is a **distinct document**,
cited in `sections/section-9-references.md` L6–11 as

> `\bibitem{Vquad}` Papanokechi, *The $V_{\mathrm{quad}}$ polynomial continued
> fraction: a Painlevé-V standalone closure on the Sakai surface $D_5^{(1)}$*.
> Zenodo, 2026, version DOI `10.5281/zenodo.20455090` (concept
> `10.5281/zenodo.20455089`).

and a second related note is cited at L13–16 as `\bibitem{StokesNote}`,
*"$V_{\mathrm{quad}}$ companion (v1.2): the Stokes constant $S=2\pi K$ and its
resurgent reading"*.

A repo-wide search for the companion's title string returns **only citing
occurrences** — bibliography entries and outline mentions in
`PERIOD-REP-VQUAD-003/paper-outline.md`, `VQUAD-PAPER-CORRECTIONS-001`,
`VQUAD-PAPER-LAYOUTFIX-001` and the LaTeX preambles. **No copy of the companion
paper exists in this repository, at any version.**

Consequences:

* The claim *"Conjecture 4.1 does not exist"* is **retracted**. The honest
  statement is: **the document that would contain it is absent**, so
  Conjecture 4.1 can be neither confirmed nor refuted from stored materials.
* The operator's hypothesis — that a v1.0 or v1.1 copy in the repo would
  produce exactly this finding, because at v1.0 the object numbered 4.1 is a
  *theorem* — is **not confirmed either**. There is no copy to inspect. The
  only version number visible anywhere in the repo for companion materials is
  the **v1.2** in the `StokesNote` bibliography entry, and that is a citation,
  not a copy.
* **Finding S4-F1 stands, but as a pure missing-data finding**, not a citation
  defect: the operator must supply the companion paper (or the correct
  pointer). This is unchanged in operational effect — P5 step 1 still cannot
  be completed from the repo — but the *reason* is different, and the earlier
  wording was unfair to the source.

<details>
<summary>Original R0 text, retained for provenance</summary>

**No conjecture numbered 4.1 exists** in the V_quad companion materials.
Searching `sessions/2026-06-15/VQUAD-PERIODREP-PAPER-001/` (all nine section
files and the assembled `vquad-periodrep-paper.md`) for `Conjecture` returns
only:

* **Fresán–Jossen Conjecture 1.3.2** — the period conjecture for exponential
  motives (`section-1.md:109`, `section-6.md:34`); nothing to do with `D5^(1)`;
* **"the master conjecture of the Sakai-stratification program"**, part (ii)(a)
  (`section-7.md:4`) — this *is* the `D5^(1)` statement, but it is referred to
  only by description, via `\cite{Sakai}`, and is not restated in the paper;
* Section 4 is titled *"The main identity and its normalisation"* and contains
  `thm:main-restated`, **not** a conjecture.

</details>

Per `CT-S0-INVENTORY/REPORT.md` §3 item 8 there is also **no standalone "Sakai
Stratification" document** in this repo — all 68 mentions are inside the
period-rep materials. So the actual `D5^(1)` attribution for V_quad rests on two
in-repo sources:

1. **`sessions/2026-05-29/T1-SYNTH-VQ-N1-.../verdict.md`** (VQ-N1, 2026-05-29):
   *"V_quad base object is canonical doubly-degenerate PV on the Sakai `D5⁽¹⁾`
   surface, symmetry `W(A3⁽¹⁾) ≅ affine 𝔖₄`"*, retracting `PIII(D6)`.
2. **`section-7.md`** of the period-rep paper: V_quad is *"the rank-one `D5^(1)`
   representative"*.

> **Finding S4-F1 (missing data, amended R1).** The V_quad companion paper is
> not present in this repository in any version; only bibliographic references
> to it exist. "Conjecture 4.1" therefore cannot be resolved from the stored
> materials. The operator must supply the companion paper or the correct
> pointer. I did not guess which statement was meant.

### 2.2 Is it the `f(z) = Σ Q_n z^n` ODE? **No.**

P5 anticipates this and says: *"If it is not the `f(z) = Σ Q_n z^n` ODE, say so.
In that case analyse BOTH systems."* It is not. The relevant operator is
`L_φ`, and `section-2.md:54–57` states its provenance verbatim:

> *"Operationally `L_φ` is the scalar (Schrödinger) reduction of the V_quad
> Painlevé-V linear problem, recovered from the Riccati linearisation
> `c = ψ'/ψ`."*

and `rmk:provenance` (`section-2.md:59–70`):

> *"`L_φ` is obtained by holonomic recognition from the coefficient stream
> `(a_n)` … and **not** from an a priori Lax pair. The literature provides no
> explicit classical Lax pair for the V_quad transcendent (a dedicated search
> returned none) … The two exponential parts `exp(±(1/√3)/z)` at `z=0` found
> below are consistent with the V_quad WKB/Riccati seed `σ = −1/√3` … and with
> the formal monodromy exponent `θ_∞ = 2/√3`."*

So `L_φ` annihilates **`φ(z) = Σ a_n z^n`**, the Riccati/WKB series
(`section-2.md:10–14`: seeded by `σ = −1/√3`, coefficients exact in `ℚ(√3)`),
which is a *different series* from `f(z) = Σ Q_n z^n`. Both systems are
therefore analysed, as instructed.

### 2.3 A second discrepancy the operator should resolve

VQ-N1's tie-breaker table and the period-rep paper describe **different** local
data, and not by a rescaling:

| | VQ-N1 `verdict.md` | `L_φ` (period-rep paper, verified here) |
|---|---|---|
| `z = 0` | **ordinary**, exponents `{0,1}`, "no `z^(1/2)` ramification" | **irregular**, Poincaré rank 1 |
| finite singular points | two apparent Fuchsian at `(−1±i√11)/6`, indices `[0,0]` | two regular singular at `(−1±i√11)/2` |
| `∞` | rank-1 **unramified irregular**, `σ± = ±1/√3` | **regular singular** |

The finite points differ by a factor 3 in `z` (a rescaling, benign), but
"`z = 0` ordinary and `∞` irregular" versus "`z = 0` irregular and `∞` regular
singular" is an **exchange of `0` and `∞`**, not a rescaling. The two are
plausibly related by `z ↦ 1/z` (the `σ± = ±1/√3` of VQ-N1 at `∞` matches
`L_φ`'s `±1/√3` at `0` exactly), but I did **not** verify that, and VQ-N1's
system is not reproduced anywhere I could read.

> **Finding S4-F2.** VQ-N1's linear system and the period-rep paper's `L_φ` are
> stated in inverted coordinates. They are probably the same object under
> `z ↦ 1/z`, but this is **unverified**. Operator input required.

---

## 3. Step 2 — exact formal types

Script: `formal_type.py` (SymPy 1.14.0, exact arithmetic over `ℚ(√3)` and
`ℚ(i√11)`; **no floating point** enters any structural conclusion).
Output: `formal_type.json`
(sha256 `c49cf8a547f60b66d201f48205ab83e6f5ec702eb14f628e8df0b7b4a19fed83`).
Method fixed in `PREREG.md` §2: reduce to normal form `u'' = r u` (gauge
invariant), read the pole order `m` of `r`, classify by parity of `m`.

### 3.1 Self-certification (falsifiers F1, F2 — neither fired)

* **System A's operator was derived, then certified.** From
  `Q_n = b(n)Q_{n−1} + Q_{n−2}`, `b(n) = 3n²+n+1`, summing gives
  `[1 − z·b(θ+1) − z²]f = 1` with `b(θ+1) = 3θ²+7θ+5`, `θ = zD`, i.e.
  **`3z³f″ + 10z²f′ + (z²+5z−1)f = −1`**. Substituting the exact integer
  sequence `Q = 1, 5, 76, 2361, 125209, 10144290, …` the residual is
  **identically zero** at every order `z^0 … z^38` in exact arithmetic.
* **System B's transcription was certified two independent ways.** (a) The
  paper's factorisation `q₂ = 4(2√3−3)z²(z²+z+3)` expands to the listed `q₂`:
  **true**. (b) Recomputing `r = ¼a² + ½a′ − b` from `(q₀,q₁,q₂)` reproduces the
  paper's printed `r(z) = (11z⁴+4z²+4z+12)/(4z⁴(z²+z+3)²)` **exactly**. This
  simultaneously validates my transcription *and* independently confirms the
  paper's own `eq:r`.

### 3.2 System A — the Channel Theory object

`3z³f″ + 10z²f′ + (z²+5z−1)f = 0`; normal form `r_A(z) = (−3z²−5z+3)/(9z³)`.

| point | `m` | formal type | ram. | Katz | exponential parts |
|---|---|---|---|---|---|
| `z = 0` | **3** (odd) | **irregular, RAMIFIED** | **2** | **1/2** | `exp(∓(2/√3)z^{−1/2})` |
| `z = ∞` | **3** (odd) | **irregular, RAMIFIED** | **2** | **1/2** | — |

`z = 0` is the only finite singular point (the leading coefficient `3z³` vanishes
nowhere else).

**Calibration check passes.** In the uniformiser `u = √z` the exponential parts
are `exp(∓(2/√3)/u)`, i.e. `c = ±2/√3` — exactly the value hard-coded in
`sessions/2026-05-01/CC-PIPELINE-G2/g2_pade_borel.py` (`c = +2/sqrt(3)`). The
prompt's premise ("a slope-1/2 edge at `z=0`, a RAMIFIED irregular singularity")
is **confirmed** by exact computation.

### 3.3 System B — the `D5^(1)` object (`L_φ`)

| point | `m` | formal type | ram. | Katz | exponential parts |
|---|---|---|---|---|---|
| `z = 0` | **4** (even) | **irregular, UNRAMIFIED**, Poincaré rank 1 | **1** | **1** | `exp(∓(1/√3)/z)` |
| `ρ₊ = (−1+i√11)/2` | 2 | regular singular | 1 | 0 | — |
| `ρ₋ = (−1−i√11)/2` | 2 | regular singular | 1 | 0 | — |
| `z = ∞` | 2 | regular singular | 1 | 0 | — |

**Calibration check passes.** Every entry reproduces the paper's own prose
(`section-2.md:78–84` and `tab:config`): "irregular singular point of Poincaré
rank 1 with two distinct exponential parts `exp(±(1/√3)/z)`", the two finite
poles regular-singular, `∞` regular-singular. Nothing was taken on trust; all of
it was recomputed from `r`.

The prompt's second premise ("the standard Jimbo–Miwa system for P_V (`D5^(1)`)
has unramified irregular singularities") is **consistent** with what `L_φ`
actually has.

### 3.4 Formal monodromy exponents

Computable and reported where the classification rule determines them: `0` at
every regular singular point of System B (`m = 2` with leading Laurent
coefficient `−1/4`, the exponent-difference-zero / apparent case, consistent
with the paper's `[0,0]` indices and its `prop:exponents` apparent-singularity
claim). At the irregular points the formal monodromy exponent is the `log`
coefficient of the formal solution, which requires the next order of the
expansion; for System A at `z = 0` the repository already records it as
`ρ = −11/6` (`CC-PIPELINE-G/newton_birkhoff.py`, derived independently there),
and P3 (`CT-S3B-RINF`) rederives `−(s+1) = −11/6` from coefficient asymptotics.
I did **not** recompute these here, since the classification does not need them.

---

## 4. A structural bonus: the action differences

The computation independently reproduces, from the ODEs alone, the entire
`ξ₀` / `ζ*` picture that P1 (`CT-S3A-ZETA-AUDIT`) reached by reading
definitions:

| system | single action `|c|` | action **difference** `|c₊ − c₋|` |
|---|---|---|
| **A**, in `u = √z` | `2/√3 = ξ₀` | **`4/√3 = ζ*`** |
| **B**, in `z` | `1/√3` | **`2/√3 = ξ₀`** |

Two things follow.

1. **P1's classification (b) is confirmed by an independent route.** For System A
   the Borel radius `ξ₀ = 2/√3` is a *single* solution's action, while
   `ζ* = 4/√3` is the *difference* of the two actions — exactly what
   `CC-PIPELINE-G2/g2_pade_borel.py` asserts (`zeta* = 2 c0`, "action of the
   partner formal solution") and exactly what P1 concluded from reading the
   conventions. Here it drops out of the pole structure of `r_A`, with no
   convention to interpret. **The factor 2 is not a normalisation artefact.**
2. **The Borel singularity sits at the action difference, in both systems.** For
   System B the action difference is `2/√3`, and the period-rep paper's Borel
   operator `L_V` has its branch singularity at `−ξ₀ = −2/√3` — the exact
   factorisation `p₄(ξ) ∝ ξ(ξ + 2/√3)` (`eq:p4-factor`). The same rule applied
   to System A predicts a Borel singularity at the action difference `4/√3 = ζ*`.
   This is a coherent, uniform structural rule across both objects.

---

## 5. Step 3 — **HALTED, not executed**

P5 step 3 requires comparison against an Ohyama–Kawamuko–Sakai–Okamoto-type
classification table of rank-2 linear systems for the Painlevé equations, and
states: *"use only a source available in the repo or supplied by the operator.
If no such table is available, STOP after step 2 and request it. Do not
reconstruct the table from memory."*

**No such table exists in this repository** (`CT-S0-INVENTORY/REPORT.md` §3
item 7). The only classification-adjacent material is VQ-N1's evidence chain,
which *cites* Sakai 2001, KNY 2017, Jimbo 1982 and Okamoto 1987 but reproduces
no table — and VQ-N1 itself records `Okamoto 1987 pages PENDING` and dropped its
own Okamoto block as `DROPPED-UNCONFIRMED`.

**Step 3 was therefore not performed, and no Painlevé classification table
appears anywhere in this session.** I did not consult memory, and I did not use
the web. *Request to operator: supply the table (§8 item 1).*

---

## 6. Step 4 — verdict

> ### Verdict: **(c) — inconclusive**, because a ramified change of the
> ### independent variable can and does alter the ramification.
> ### **Label: STRUCTURAL.**

This is not a shrug; it is a specific, positive statement. The transformation
that must be checked is named exactly:

> **The ramified double cover `π : w ↦ z = w²`** (equivalently Channel Theory's
> own uniformiser `u = √z`).

Reasoning:

* Ramification and the Katz invariant are invariant under *gauge* transformation
  and under any *unramified* change of variable, so no such transformation can
  reconcile System A's `1/2` with System B's `1`. Within a fixed base coordinate
  the two formal types are genuinely incompatible.
* But pullback along a degree-2 cover branched at the singular point **multiplies
  the Katz invariant by 2**. For System A, `1/2 × 2 = 1` — exactly System B's
  value, and the ramification index drops `2 → 1`. The computation records this
  (`covering_check` in `formal_type.json`). So System A's formal type at `z = 0`,
  read in `w = √z`, is *unramified of Katz invariant 1* — the same formal shape
  as System B and as an unramified Jimbo–Miwa `D5^(1)` system.
* Hence the slope-1/2 edge alone **does not** refute the `D5^(1)` attribution.
  It shows only that Channel Theory's `z` and the Painlevé linear problem's `z`
  are **not the same coordinate**; they differ by a square.

Why I do **not** claim (a) or (b):

* **(a) is not available** because "compatible with `P_V`/`D5^(1)`" requires
  matching against the classification table, which step 3 could not run. The
  Katz invariants agreeing after pullback is *necessary*, not sufficient: rank,
  the number and type of the other singular points, and the formal monodromy
  exponents must all match, and System A (one finite singular point, `∞`
  ramified irregular) and System B (three regular singular points plus one
  unramified irregular) have **visibly different global singular configurations**.
  A cover branched at `0` does not by itself reconcile the behaviour at `∞`.
* **(b) is not available** because naming "which Painlevé types are compatible
  instead" is precisely what the missing table would be needed for, and P5
  forbids reconstructing it from memory.

**The "two objects, two surfaces" reading is supported.** System A annihilates
`Σ Q_n z^n`; System B annihilates `Σ a_n z^n`. They are different series, with
different global singular configurations, and the `ξ₀`/`ζ*` factor-2 relation of
§4 is the shadow of the same square.

**No file was edited to reflect this.** Conjecture 4.1 — whatever it turns out
to be — is untouched, in this and every other session.

---

## 7. What was NOT established

* **Step 3 was not done.** No comparison against any Painlevé rank-2
  classification was performed. The verdict is correspondingly weaker.
* **No isomonodromy computation** was attempted; this was a cheap pre-test, as
  the prompt intended.
* **VQ-N1's own linear system was never reproduced.** Its table (`z=0` ordinary,
  `∞` rank-1 unramified) is recorded in `verdict.md` but the system itself is not
  written down anywhere I could read, so I classified `L_φ` instead. Finding
  S4-F2 records the coordinate inversion.
* **The `z ↦ 1/z` conjecture of §2.3 is unverified.**
* **Formal monodromy exponents at the irregular points were not recomputed**
  (existing repo values are cited instead).
* **Whether the pullback of System A along `z = w²` is actually *isomorphic* to
  System B** — as opposed to merely sharing a Katz invariant at one point — was
  **not** checked, and §1's table shows the global configurations differ. This is
  the single most valuable next computation (§8 item 3).
* The period-rep paper's own `L_V` (order 4, on `ξ`) was **not** classified; P5
  asks about the systems behind the `D5^(1)` attribution, and `L_V` is the Borel
  dual, not a candidate.

---

## 8. Open questions for the operator

1. **Supply the classification table** (Ohyama–Kawamuko–Sakai–Okamoto or
   equivalent) so step 3 can run, or confirm step 3 should stay unrun. Without
   it the verdict cannot move past (c).
2. **What is "Conjecture 4.1"?** (Finding S4-F1.) It is not in the period-rep
   paper. Is the intended statement the Sakai-program master conjecture part
   (ii)(a) (`section-7.md`), or the VQ-N1 verdict, or something in the
   `pcf-research/` repo that is not on this machine?
3. **Is VQ-N1's system the `z ↦ 1/z` image of `L_φ`?** (Finding S4-F2.) If the
   operator can supply VQ-N1's linear system explicitly, this is a ten-minute
   check and it would close a real ambiguity in the record.
4. **Should the `z = w²` relation be pursued?** The Katz invariants match after
   pullback but the global singular configurations do not. Determining whether
   `π*(System A)` and `System B` are genuinely related — and if so by what — would
   convert verdict (c) into (a) or (b) without needing the table for the local
   part.
5. **Note for the record:** §4 gives an ODE-level, convention-free confirmation
   of P1's finding that `ζ* = 2ξ₀` is an action *difference*. If the programme
   has been treating `ζ*` and `ξ₀` as the same singularity anywhere, that is now
   independently contradicted twice.

---

## 9. Uncommitted files (all new, under `sessions/2026-09-17/CT-S4-FORMAL-TYPE/`)

| file | role |
|---|---|
| `PREREG.md` | hypothesis, observable, classification rule, falsifiers F1–F3, vacuity check, mandated hard stop at step 3 |
| `formal_type.py` | exact SymPy computation: derivation + certification of both operators, normal forms, pole orders, classification, exponential parts, action differences, covering check |
| `formal_type.json` | machine-readable output (sha256 `c49cf8a547f60b66d201f48205ab83e6f5ec702eb14f628e8df0b7b4a19fed83`) |
| `run.log` | full run transcript |
| `claims.jsonl` | labelled claims with output hashes |
| `REPORT.md` | this file |

**Nothing was committed, pushed, tagged, or submitted. No conjecture was revised
in any file. All earlier-session materials were read only.** HEAD remains
`08aa0e2`.
