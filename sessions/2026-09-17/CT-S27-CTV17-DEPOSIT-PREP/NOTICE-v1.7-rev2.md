# Channel Theory for Polynomial Continued Fractions — version notice v1.7

**DRAFT ONLY.** Not deposited. No metadata edit has been made or is authorised by
this file. Concept DOI **`10.5281/zenodo.19941678`** — read from the live record
`10.5281/zenodo.22782807` (v1.6) on 2026-09-19 via its `conceptdoi` field, and
independently from DataCite, never from a record number and never from memory.
The concept record currently resolves to version **`1.6`**, which is why this
notice is **v1.7**.

Session: `sessions/2026-09-17/CT-S26-CTV17-DRAFT/`.

**The file attached to v1.7 is the v1.6 build, unchanged. The v1.7 corrections
are recorded in this description only.** v1.7 is a *description-only* new
version: no PDF was rebuilt, and none is claimed to have been. The v1.4–v1.6
LaTeX sources are not in the working repository, and the only source held is
v1.3.1 — a build made from it would silently revert two versions of
corrections, including the Painlevé-target correction made at v1.4 and the
analytic residual added at v1.6, both of which this notice relies on. Attaching
a build that cannot be verified is the v1.6 defect (1) repeated; **not**
attaching one is the avoidable choice, and it is the one taken. If the v1.6
sources or PDF become available and an updated build is wanted, that is v1.8.

---

## 0. Current state

*This section is the whole current state. Nothing below it is needed to know what
Channel Theory now asserts; §1 is history and §2–§7 are the detail.*

**Proven.** For `Q_n = b(n)Q_{n−1} + Q_{n−2}` with `Q_{−1} = 0`, `Q_0 = 1`,
`deg b = d ≥ 1` and `b(k) ≠ 0` for `k ≥ 1`:

* the normalised ratio `r_n = Q_n/∏_{k≤n} b(k)` converges unconditionally, with
  `r_∞ − r_n = O(n^{−(2d−1)})`;
* if `b(n) > 0` for all `n ≥ 1` then `1 ≤ r_∞ ≤ exp Σ_{k≥1} 1/(b(k)b(k+1)) < ∞`,
  so the hypothesis `(H): r_∞ ≠ 0` holds automatically and is two-sidedly bounded;
* under `(H)`, `lim |Q_n/(dn)!|^{1/n} = |β_d|/d^d`, hence
  `B(w) = Σ_n Q_n w^n/Γ(dn+1)` has radius `d^d/|β_d|` and, in the uniformiser
  `ζ = w^{1/d}`, **`ξ₀ = d/|β_d|^{1/d}`**;
* `Q_n/Γ(dn+1) = K (β_d/d^d)^n n^s (1 + O(1/n))` with
  **`s = β_{d−1}/β_d + (d−1)/2`**.

**Attributed, not claimed.** The radius identity — i.e. the statement carried
since v1.0 as `prop:xi0` at `d = 2` and promoted at v1.3 to
**Conjecture 3.3.A★** — is a corollary of the **Perron–Kreuser theorem** together
with **Pincherle**'s minimal/dominant dichotomy. **The conjecture label is
retired**: the statement is not a conjecture, it is classical, and the
cross-degree formula `ξ₀ = d/|β_d|^{1/d}` now holds at every `d ≥ 1` as a proved
statement rather than at `d = 2` proven / `d = 4` verified (§2).

**Verified, never proven.** The closed form
`K = r_∞ (2π)^{(d−1)/2} / (√d · ∏_i Γ(1 − r_i))`, where `b(n) = β_d ∏_i (n − r_i)`
(§4). It agrees with computation to 109–115 decimal digits over eight test
polynomials spanning `d = 2, 3, 4`, with a vacuity control that collapses the
agreement to ≤ 0.75 digits when the `∏_i Γ(1 − r_i)` factor is removed. It is
labelled VERIFIED and **must not be written as PROVEN**.

**Open.**

1. **`r_∞` itself has no closed form.** `K` isolates the single transcendental
   input into `r_∞`; it does not evaluate it.
2. **Whether the exponent `s` is already in print.** The literature route ends at
   Wong & Li II, which is **NOT OBTAINED** (§3). The priority position cannot be
   settled without it, and this notice does not settle it.
3. **A closed form for `S_{ζ*}`.** Excluded from one explicitly printed search
   space (§6.4); not excluded in general. It is carried here under its **own new
   tag, `op:cc-szeta-closed-form`**, and is **not** filed under
   `op:cc-stokes-closed-form`: the latter, created at v1.5 out of the demoted
   Theorem 3.7(iii), asks whether the CC-channel connection-coefficient *ratio*
   **matches** the Riemann–Hilbert datum of `P_V/D₅^(1)` at the `V_quad`
   τ-parameter, whereas the former asks whether one number admits a
   multiplicative closed form in a stated basis. **Both mention Stokes data;
   they are different questions, and one name for two objects is the trap §6.0
   forbids.** The relation between them is stated at §6.4 and is not a merger.
4. **The `V_quad` normalisation map**, which every comparison of Borel-plane
   constants across the two normalisations still waits on (§6.5). **The target is
   the Painlevé V transcendent on the Sakai surface `D₅^(1)`, and that
   identification is itself conjectural** — the `P-III(D₆)` naming was corrected
   at v1.4 and the identification marked conjectural at v1.5. Working material in
   this repository still says `P-III(D₆)`; it is stale and must not be copied
   forward.
5. **The singularity type at `ξ₀`.** `op:xi0-d3-direct` was **withdrawn as
   vacuous at v1.6** — not closed, not answered — and replaced by
   **`op:xi0-singularity-type`**, which is the live problem: the radius is now
   proved at every `d` (§2), and the type is untouched by that proof (§5, §8).
6. **Whether the generating-function operator and the `V_quad` Borel-plane
   datum determine one another.** New at v1.7, and **untagged**. The operator
   `L_d` annihilating `Σ_n Q_n z^n` has a formal type that can be read against
   van der Put–Saito's Table 2.1: for `deg b = 2` and `deg a ≤ 2` the row
   `D̃₅/P_V` is **excluded**, and the reachable rows are `PIII(D₈)`, `PIII(D₇)`,
   `PIII(D₆)`, with Channel Theory's own `a ≡ 1` giving `PIII(D₈)` (§7). This
   neither supports nor disputes item 4: **it has not been shown that the two
   are the same object**, and treating them as one would be the
   one-name-two-objects error §6.0 forbids (§7.0, §7.4).

**Not formalised.** The Lean development carries **seven `sorry`s** and zero
discharged obligations. `lake build` succeeding shows the statements typecheck; it
shows nothing about provability. **No result in Channel Theory is
machine-checked, and this notice does not claim formal verification.**

---

## 1. Erratum and version stack

Read downward for history only. **Entries for v1.4, v1.5 and v1.6 are quoted from
the deposited descriptions of records `20585624`, `22717792` and `22782807`,
fetched on 2026-09-19 and held in `refs/`** — those versions are not in this
repository (see the box below).

| Version | Version DOI | Published | Disposition |
|---|---|---|---|
| v1.1 | `10.5281/zenodo.19941679` | — | superseded |
| v1.2 | `10.5281/zenodo.19951331` | — | superseded |
| v1.3 | `10.5281/zenodo.19972394` | 2026-05-02 | superseded |
| v1.4 | `10.5281/zenodo.20585624` | 2026-06-07 | superseded |
| v1.5 | `10.5281/zenodo.22717792` | 2026-09-12 | superseded |
| v1.6 | `10.5281/zenodo.22782807` | 2026-09-16 | **the current published version** |
| v1.7 | — | — | this notice, draft |

The concept record `10.5281/zenodo.19941678` currently resolves to **version
`1.6`**, and DataCite lists exactly the six `HasVersion` identifiers above, so
**v1.7 is the correct next version number**. (Read 2026-09-19 from
`refs/datacite_concept.json` and `refs/zenodo_22782807.json`; the concept DOI is
taken from the `conceptdoi` / `parent` field, never from a record number.)

**v1.1 → v1.2.** The v1.1 cross-degree candidate `c(d) = 2√((d−1)!)` — which
agrees with `d = 2` by coincidence — was empirically falsified at `d = 4`: it
predicts ≈ 4.899 against a measured 4, ≈ 22 % disagreement (Remark 3.3.E).

**v1.3 (2026-05-02).** Purely additive framing revision; nothing rewritten or
retracted. Added §3.5 (`rem:h4-median`), §3.6, and `op:cc-median-resurgence-execute`.
Promoted the cross-degree formula to **Conjecture 3.3.A★**, `ξ₀(b) = d/β_d^{1/d}`,
*proven at `d = 2`, verified at `d = 4`, `d = 3` deferred to `op:xi0-d3-direct`*.

**v1.4 (2026-06-07) — two corrections.** (1) **The EBR `ξ₀` upgrade.** For
positivity families `b(n) > 0 (n ≥ 1)`, the identity `ξ₀ = d/β_d^{1/d}` was
proved *for the physical generating-function object* by the holonomic/positivity
argument of the companion EBR preprint `10.5281/zenodo.20564079` §3 (D-finite `G`;
leading coefficient `a_{2d}(s) = d^d s^{2d}(d^d − β_d s)`, roots `{0, R}`;
Pringsheim), with scope *positive-`b` families, physical object, symbolic +
verified-to-`d6` + Lean-checked algebraic layer `d = 2–5`, **not** a
symbolic-degree formal proof*. That superseded the Conjecture-3.3.A★ status **for
the positive-`b` case only**. (2) **Surface-type correction.** All references —
body, keywords and description — were corrected from **Painlevé III(D₆)** to the
**Painlevé V transcendent on the Sakai surface `D₅^(1)`** (`W(A₃^(1))`,
`δ = −1/2 ≠ 0`). Channel Theory was the last deposit carrying the stale
`P-III(D₆)` root claim.

**v1.5 (2026-09-12) — a demotion.** Clause **(iii)** of Theorem 3.7, the match
between the CC-channel connection-coefficient ratio and the Riemann–Hilbert datum
of `P_V/D₅^(1)` at the `V_quad` τ-parameter, **is not a theorem of this paper**
and became the open problem **`op:cc-stokes-closed-form`**. Two grounds: the
imported surface-type premise is itself conjectural (companion paper Conjecture
4.1, `10.5281/zenodo.20455089`, read at v1.2), and the cited run stores a
comparison its own verdict did not incorporate — a factor of about two accounted
for by an explicit halving in the source, **with ~1.7 % unexplained**. v1.5 also
withdrew as non-evidential a Domb–Sykes sentence that rounded two endpoints
agreeing to two digits into a three-digit "range", and corrected five citations
that pinned a version in which the cited object was not yet a conjecture. **The
v1.4 sentence "both corrections are additive/clarifying; no … claim is retracted"
does not describe v1.5.**

**v1.6 (2026-09-16) — five defects repaired; a build, labelling and
open-problem erratum.** (1) The v1.5 PDF was the **draft build**, watermarked
"DRAFT — NOT DEPOSITED", its date line stalled at "2026-06-07 (v1.4, draft)" and
its changelog ending at v1.3 — front matter, not text. (2) **`op:xi0-d3-direct`
withdrawn as vacuous**, replaced by **`op:xi0-singularity-type`**, with
**`rem:d3-vacuous`** recording the withdrawal (see §5). (3) A **citation gap**:
`10.5281/zenodo.20542162` (deposited 2026-06-04) derives the slope-`1/d` edge
polynomial `χ_d(c) = 1 + (−1)^{d+1}(β_d/d^d) c^d` symbolically and `d`-free for
all `d ≥ 2`, **with only `β_d` appearing on the edge**; it is now cited at
Conjecture 3.3.A★ and `op:xi0-degree-d`, and that problem is restated — *no
per-degree computation remains, and the residual is analytic rather than
algebraic*. (4) Every cross-reference to a proposition, conjecture, remark,
definition, example or open problem **rendered as "Theorem N"** in v1.0–v1.5
(110 sites), because the environments share one counter; the numbered blocks
themselves were always correct. **Readers of v1.0–v1.5 must treat "Theorem N.N"
in running text as naming whatever class the numbered block declares.** (5)
**Falsifiers added** to `op:cc-median-resurgence-execute` and `op:cc-formal-borel`,
the former also gaining a **vacuity pre-check** — hold `β₂` fixed, vary the
lower-order coefficients, and confirm that `S_{ζ*}` actually moves — and all
surviving §9 cost estimates marked unverified.

**v1.7 (this notice) changes five things.**

1. **§2 Attribution.** Conjecture 3.3.A★ is retired and attributed. **This
   replaces the v1.4 EBR grounding**, which held only for positive `b` and only
   for the physical object; the classical route needs **no positivity hypothesis
   at all**.
2. **§3 The exponent.** `s = β_{d−1}/β_d + (d−1)/2` is stated with its derivation
   and its priority position, including that **Wong & Li II is NOT OBTAINED**.
3. **§4 `K` and `r_∞`.** The closed form, and `r_∞` identified as exactly the
   constant the classical turning-point method normalises out of view.
4. **§5 The vacuity explanation.** A one-line structural reason **generalising
   and de-empiricising `rem:d3-vacuous`**: v1.6 established the phenomenon for
   `ξ₀` by a coefficient sweep; §5 derives it for `ξ₀` **and `ρ`** from two proved
   statements, with no sweep.
5. **§6 The Borel material.** `ζ* = 2ξ₀` is an **action difference, not a change
   of variable**; `op:cc-median-resurgence-execute` is restated to name the series
   it concerns; and a pre-registered negative result is recorded against a search
   space printed in full, filed under a **new tag `op:cc-szeta-closed-form`**
   kept deliberately separate from `op:cc-stokes-closed-form` (§0, §6.4).

> ### What was fetched, and what still was not
>
> **Channel Theory v1.4, v1.5 and v1.6 are not in this repository** — the newest
> in-repo source is v1.3.1, and the v1.3.1 claims record points at
> `pcf-research/channel/…`, which does not exist on this machine. The deposited
> **descriptions** were therefore fetched from the records themselves on
> 2026-09-19 and are held in `refs/` with their bytes and hashes: v1.5 and v1.6
> from the Zenodo API, v1.3 and v1.4 from DataCite after `zenodo.org` began
> returning HTTP 504 on every further request. **Everything in the stack above is
> quoted from that deposited text.**
>
> **Still not obtained, and therefore not quoted:**
>
> * **The v1.5 and v1.6 PDFs.** Both file endpoints returned HTTP 504 (`api/
>   records/…/files/…/content` and the classic `records/…/files/…?download=1`).
>   So **§9's falsifier statements and their numeric thresholds have not been
>   read** — v1.6's description says both open problems now carry one, and §6.3
>   below says only that, not what the threshold is.
> * **The v1.4 description may be partial.** DataCite returned a single 5808-byte
>   description for it; the Zenodo record carries the full HTML, which could not
>   be fetched. The v1.4 text quoted above is also retained verbatim inside the
>   v1.6 description, which is the copy actually used.
>
> **A correction to this session's own earlier finding.** Before the records were
> fetched, `op:xi0-singularity-type` was reported as having *zero occurrences* and
> was not cited. That was true **of the repository** and false of the corpus:
> the tag was created at v1.6 and is real. A repo-wide search establishes absence
> from the repo, not absence from the published record.

---

## 2. Attribution: Conjecture 3.3.A★ is not a conjecture

**The statement.** With `b(n) = β_d n^d + …`, `β_d ≠ 0`, `b(k) ≠ 0` for `k ≥ 1`:

```
lim_{n→∞} | Q_n / (dn)! |^{1/n}  =  |β_d| / d^d ,
```

so `B(w) = Σ_{n≥0} Q_n w^n / Γ(dn+1)` has radius of convergence `d^d/|β_d|` in
`w`, and in the uniformiser `ζ = w^{1/d}`

```
ξ₀ = d / |β_d|^{1/d} ,        and at d = 2,  ξ₀ = 2/√β₂ .
```

**This is prior art.** Write the recurrence in the classical form
`Q_{n+1} + a_n Q_n + b_n Q_{n−1} = 0` with `a_n = −b(n+1) ∼ −β_d n^d` and
`b_n = −1`, so that in Gautschi's notation `α = d` and `β = 0`. Hypotheses (2.2)
and (2.8) hold, and the Newton–Puiseux vertex `P₁ = (1, d)` lies above the segment
`P₀ = (0,0)` — `P₂ = (2,0)` for every `d ≥ 1`, so case (a) applies and the ratio
asymptotics follow.

*Cited to:* W. Gautschi, *Computational aspects of three-term recurrence
relations*, **SIAM Review 9 (1967)**, **Theorem 2.3(a), p. 35** (Perron–Kreuser)
and **Theorem 1.1, p. 31** (Pincherle); **DLMF §3.6(ii)** for the same dichotomy.
Held and hashed: `CT-S8-LITCHECK/refs/gautschi1967.pdf`, page image
`CT-S8-LITCHECK/refs/g1967_p35_mid.png`, `CT-S8-LITCHECK/refs/dlmf_3_6.txt`.

Gautschi's condition (2.8) constrains the **exponents** `α, β` to be real. It does
**not** constrain the coefficients, so complex `β_d` is inside the classical
statement.

**Retire the conjecture label.** Conjecture 3.3.A★ asserted `ξ₀(b) = d/β_d^{1/d}`
for every degree-`d` PCF in scope, with the status *proven at `d = 2`, verified at
`d = 4`, `d = 3` deferred*. That tiered status is withdrawn. The identity holds at
every `d ≥ 1`, classically by Perron–Kreuser plus Pincherle, and independently by
an elementary proof carried in the AEAL record — `thm:radius`, proved **without
Gamma asymptotics**, its Step 3 using a combinatorial multinomial sandwich rather
than Stirling (`S1-03`, **PROVEN**). Both routes need only `(H): r_∞ ≠ 0`.

**This supersedes, for this purpose, the EBR positivity upgrade as the grounding.**
The v1.4 grounding (`10.5281/zenodo.20564079` §3) proves the identity only *for
positivity families `b(n) > 0 (n ≥ 1)`*, only *for the physical
generating-function object*, and with a Lean-checked algebraic layer covering
`d = 2–5` — by its own §8 scope statement, **not a symbolic-degree formal proof**.
The route stated here needs **no positivity hypothesis**, is not restricted to the
physical object, and carries no degree ceiling; the EBR argument remains a valid
independent proof on its own narrower scope and is not withdrawn. What `(H)` asserts is exactly that
`Q_n` is *not* the minimal solution of the recurrence; the minimal subspace has
codimension one, so `(H)` is generic. That Pincherle reading is **interpretive and
load-bearing on nothing** (`S1-05`, STRUCTURAL). Positivity of `b` re-enters only
as the cheapest *sufficient* condition for `(H)`: if `b(n) > 0` for all `n ≥ 1`
then `r_n` is strictly increasing with `r_n ≥ 1` (`S1-02`, PROVEN), and it is then
also bounded above by `exp Σ_{k≥1} 1/(b(k)b(k+1))` (`S26-01`, PROVEN), the
positivity being load-bearing in that bound — three of six sign-changing `b`
violate it outright (`S26-04`).

> **Do not let this paragraph migrate into a method statement.**
> Perron–Kreuser-plus-Pincherle is the **classical** route and is cited here as
> prior art. Channel Theory's own `(H)` comes from the positivity proposition, not
> from Pincherle, and the upper bound `S26-01` uses no minimal-solution,
> Pincherle or Perron–Kreuser input at any step. A method paragraph led by
> Pincherle would also invite the Birkhoff–Trjitzinsky rigour question that §3
> exists to close.

*Claims:* `S1-01`, `S1-02`, `S1-03`, `S1-05`, `S26-01`, `S26-04`.

> **What §2 does not close.** §2 closes the **algebraic** part of
> `op:xi0-degree-d` and nothing more. v1.6 had already restated that problem as
> having *no per-degree computation remaining and an analytic residual*; **that
> analytic residual is open, and its name is `op:xi0-singularity-type`** — the
> type of the singularity at `ξ₀`, and indeed whether `ξ₀` is a singularity of
> the Borel transform at all rather than only the radius the recurrence fixes.
> A proof of where the radius sits is not a proof of what sits there. Nothing in
> §2 touches it, and `op:xi0-degree-d` **must not be reported as closed** on the
> strength of §2 (§8).

---

## 3. The exponent, and the priority position

**The statement.**

```
Q_n / Γ(dn+1)  =  K · (β_d/d^d)^n · n^s · (1 + O(1/n)) ,
      s = β_{d−1}/β_d + (d−1)/2 ,
```

equivalently, as an indicial exponent in the Borel plane,
`ρ_d = −s − 1 = −(d+1)/2 − β_{d−1}/β_d`, which at `d = 2` is the
`ρ = −3/2 − β₁/β₂` carried since v1.0 (for `V_quad`, `β₂ = 3`, `β₁ = 1`, giving
`ρ = −11/6`).

**Derivation, in outline.** `Q_n = r_n B_n` exactly, with
`B_n = ∏_{k≤n} b(k) = β_d^n (n!)^d ∏_i Γ(n+1−r_i)/Γ(1−r_i)` after factoring
`b(n) = β_d ∏_i (n − r_i)`; Gauss multiplication converts `(n!)^d` against
`Γ(dn+1)`, and the `d` Gamma ratios contribute `n^{−Σ r_i} = n^{β_{d−1}/β_d}`
through `Σ_i r_i = −β_{d−1}/β_d`, while multiplication supplies the `(d−1)/2`.
The one classical ingredient quoted rather than proved is
`Γ(z+a)/Γ(z+b) ∼ z^{a−b}`, **DLMF (5.11.12)**; with that quoted, the growth law is
`S1-04`, **PROVEN** (`thm:growth`).

**Numerically confirmed independently** at `d = 4` over eight quartic
representatives, at dps ≥ 60 and `n` to 20000, with Richardson extrapolation, and
with both pre-registered vacuity arms: varying `β_0 … β_{d−2}` leaves `s` unmoved
beyond fit error, varying `β_{d−1}` moves it as predicted (`S2-01`–`S2-04`,
VERIFIED).

### 3.1 Priority position — stated plainly

**DLMF §2.9(ii) gives the exponent explicitly only for bounded coefficients, and
routes this degree away.** Equation **(2.9.6)** gives
`α_j = (f₁ρ_j + g₁)/(f₀ρ_j + 2g₀)` with `ρ_j` the roots of **(2.9.5)** — but only
under `f(n) ∼ Σ_s f_s n^{−s}`, `g(n) ∼ Σ_s g_s n^{−s}`, `g₀ ≠ 0`. Here
`f(n) = −b(n+2)` grows like `n^d`, so for **every `d ≥ 1`** that expansion, and
with it `f₀`, **does not exist**, and those clauses do not apply. DLMF then routes
exactly this class elsewhere, at **(2.9.14)**: *"in which `P` and `Q` are any
integers see Wong and Li (1992a)."* Both equation numbers and the (2.9.14)
deferral are present in the hashed capture `CT-S8-LITCHECK/refs/dlmf_2_9.txt`
(lines 127, 143, 327, 343).

**Wong & Li II: NOT OBTAINED.** R. Wong and H. Li, *Asymptotic Expansions for
Second-Order Linear Difference Equations, II*, **Studies in Applied Mathematics
87 (1992) 289–324**, DOI `10.1002/sapm1992874289`. Paywalled; the publisher
returned HTTP 403; it was **not purchased and no mirror was used**. Whether `s`
is already in print there, and whether a connection constant is given there in
closed form, are **NOT ESTABLISHED** (`S21-76`, INSPECTED).

The asymmetry must be stated with it, as a line and not as a footnote: the unread
article **cannot reach `s`**, which is derived and independently verified here,
and **cannot reach the Borel framing**; it could bear only on a closed form for
the amplitude.

**This notice is not gated on obtaining it.** The exponent is derived here and
verified independently of the literature, and the `r_∞` framing rests on
Wong & Zhao §3, which *is* held and hashed (§10). Only a closed form for `K` could
be affected. The article is therefore left **NOT OBTAINED**, recorded as such,
and a future version may settle priority if a copy is ever obtained through
non-purchase channels; **the priority position stated here must not be softened
in the meantime.**

> **The suffix and the numeral are load-bearing.** DLMF's "Wong and Li (1992a)"
> is the paper titled **II**, in *Studies in Applied Mathematics*. DLMF's
> "1992b" is a different paper, *J. Comput. Appl. Math.* **41** (1992) 65–94,
> which covers the **bounded** case and is therefore not ours. Quote the full
> citation including the word *linear* and the numeral *II*; a compressed
> citation here selects the wrong paper.

### 3.2 Nothing here rests on Birkhoff–Trjitzinsky

The *shape* `ρ^n n^s (1 + O(1/n))` is Birkhoff–Trjitzinsky's normal-solution
shape (*Acta Math.* **60** (1933), Fundamental Theorem §9, p. 69), which gives
existence and shape but **no formula for `s` in the `β_k`**. B–T is cited for that
provenance and for nothing else. This must be said in the same breath as the
citation, because **the standard survey objects to B–T on rigour grounds**:

> "The major objection to the use of the Birkhoff–Trjitzinsky results is that
> they may not be rigorous, since gaps are alleged to exist in the complicated
> proofs."
> — A. M. Odlyzko, *Asymptotic Enumeration Methods*, p. 77.

A referee who checks that page reads this. The growth rate here is
Perron–Kreuser via Gautschi, the exponent `s` is derived directly, and the upper
bound on `r_∞` is elementary. **Nothing rests on B–T.**

---

## 4. `K` and `r_∞`

**The closed form.** With `b(n) = β_d ∏_{i=1}^{d} (n − r_i)`,

```
K  =  r_∞ · (2π)^{(d−1)/2}  /  ( √d · ∏_{i=1}^{d} Γ(1 − r_i) ) .
```

**Label: VERIFIED, never PROVEN.** The derivation is complete except for the
quoted classical Gamma ratio and is recorded as STRUCTURAL (`S3B-04`); the form
agrees with the numerically computed limit of `Q_n/Γ(dn+1)` to between **109.66
and 114.69 decimal digits** for all eight test polynomials spanning `d = 2, 3, 4`,
including cases with negative `K` and with sign-changing `b` (`S3B-05`,
VERIFIED, pre-registered falsifier at 20 digits did not fire); and the vacuity
control — recomputing `K` with the `∏_i Γ(1 − r_i)` factor omitted — collapses the
agreement from ~110 digits to **at most 0.75 digits in every case** (`S3B-06`).
The test is therefore sensitive to the quantity the hypothesis is about.

**`r_∞` is the constant the classical method normalises away.** Classical
difference-equation asymptotics fixes solutions only up to a multiplicative
connection coefficient; `K` supplies that coefficient, with the single
transcendental input isolated into `r_∞`.

That this is a *structural* feature of the classical route, and not an oversight
in one survey, is recorded twice:

* **Absence, with positive controls fired first.** The growth law, the exponent
  `s`, and any explicit leading constant are **NOT FOUND** anywhere in
  Wong & Zhao §3 (PDF pp. 12–20) on a full-text read. Six positive controls were
  fired first, so the absence test was not vacuous (`S21-31`, INSPECTED).
* **The structural reason.** At **(3.23)** that section defines `K_n` by
  `K_{n+1}/K_{n−1} = c_n` and sets `x_n = y_n/K_n`; `K_n` therefore absorbs
  exactly the product growth, and Theorems 3.1–3.3 then describe `x_n` by uniform
  Airy/Bessel expansions near transition points. It is turning-point theory in a
  parameter: **the growth constant is normalised out of view in order to reach
  turning-point behaviour**, and `K_0, K_1` are left depending on the particular
  sequence (`S21-32`, STRUCTURAL).

*Source, held and hashed, version-pinned:* R. Wong and Y.-Q. Zhao, *Recent
Advances in Asymptotic Analysis*, **Analysis and Applications 20 (2022)
1103–1146**, DOI `10.1142/S0219530522400012`; preprint **arXiv:2204.09305v1**,
`CT-R1-AUDIT/refs/wong_zhao_2022_recent_advances_arxiv-2204.09305.pdf`,
464879 bytes, sha256 `123ab322619c723c…`, CC-BY-4.0. The version pin is
deliberate: the read was of v1 (`S21-33`).

**The connection-constant statement, cited from the sources actually held, with
the attribution split as the page has it.** On p. 77 Odlyzko writes:

> "Wimp and Zeilberger point out that it is usually easy to show that the largest
> of the terms of the form (9.35) does show up with a nonzero coefficient, and so
> determines the asymptotics of `a_n` up to a multiplicative constant. However,
> the Birkhoff–Trjitzinsky method does not in general provide any techniques for
> determining that constant."

**The first sentence is Odlyzko reporting Wimp and Zeilberger [384]; only the
second is his own.** Citing the whole passage to Odlyzko misattributes the first
half. Verified from a page image re-obtained from the author's site, not from any
intermediate record: `CT-S24-PAPER-OUTLINE/refs/odlyzko_asymptotic_enum.pdf`
(sha256 `d0b58928…`), page image `CT-S24-PAPER-OUTLINE/refs/odlyzko_p77.png`
(sha256 `f9843a43…`), checker
`CT-S24-PAPER-OUTLINE/scripts/verify_odlyzko_p77.py` at 5/5 controls
(`S24-12`, VERIFIED).

Retained alongside it, not replaced by it: **G. Nemes (2026), arXiv:2508.15246v2**,
abstract and §1 p. 3, on connection coefficients being *often treated as unknowns
in other methods* and at best computed numerically
(`CT-S8-LITCHECK/refs/nemes2025.pdf`, INSPECTED). Two independent sources for one
statement. Odlyzko is the stronger for *this* point because it is about
Birkhoff–Trjitzinsky specifically; Nemes is the more recent.

A third held source, Ibrahim & Salvy, *Positivity certificates for linear
recurrences* (SODA 2024, arXiv:2306.05930v2, CC-BY-4.0,
`CT-R1-AUDIT/refs/ibrahim_salvy_2023_positivity_certificates_arxiv-2306.05930.pdf`,
sha256 `36e9d025c89b6fa0…`), must be quoted **only in its weaker printed form** —
that the constant is one they *do not know how to compute*, **not** that it *is
not computable*.

---

## 5. The vacuity explanation

**One line replaces an empirical coefficient sweep:**

> **`ξ₀` reads only `β_d`, and `ρ` reads only `β_d` and `β_{d−1}`.** Any two
> families sharing their top two coefficients therefore share both invariants
> exactly, and no test built on `ξ₀` and `ρ` alone can separate them.

This is immediate from §2 and §3: `ξ₀ = d/|β_d|^{1/d}` and
`ρ = −(d+1)/2 − β_{d−1}/β_d`. It is structural, not empirical, and it does not
depend on degree, on the discriminant, or on which representatives were sampled.

It explains, without a sweep, the phenomena the earlier versions recorded
empirically: the `K`-SCAN marginal coincidence between `V_quad` and `QL15` — both
`β₂ = 3`, hence both `ξ₀ = 2/√3` to 200 digits — where **the same `β₂` forces the
same `ξ₀` without forcing the same Painlevé label** (Remark 3.3.C); and the
non-injectivity recorded as Proposition 3.3.B, where `QL01` and `QL02` share both
`ξ₀ = 2` and `ρ = −5/2` and split only at `a₂`. The same structure is what the
pre-registered vacuity arms of the `d = 4` exponent run measured directly
(`S2-03`, `S2-04`).

The consequence for the bridge tiering is that a **B1 witness — a `β_d`-only
witness — is by construction the weakest tier**, and cannot be strengthened by
more `ξ₀` data at any precision. Separation requires a coordinate that reads
below `β_{d−1}`.

> **This generalises and de-empiricises `rem:d3-vacuous`.** That remark was added
> at v1.6 to record the withdrawal of `op:xi0-d3-direct` as vacuous, and its
> evidence is a **coefficient sweep**: holding `β₃` fixed and varying `β₂, β₁, β₀`
> over `−1000…+999` moves `ξ₀` by `6.85 × 10⁻¹⁸`, while varying `β₃` alone moves
> it by `1.26 × 10⁻¹` (v1.6 description, defect (2)). That measurement is at
> `d = 3` and is about `ξ₀` only. The two lines above **derive** the same
> phenomenon, for every `d`, for `ξ₀` **and** `ρ`, from two proved statements and
> with no sweep at all. The sweep is retained as independent confirmation; it is
> no longer the reason.
>
> v1.6 already states the transferable form — *"an observable that depends on less
> data than the hypothesis it is posed to test cannot test it … it applies to open
> problems in this corpus that have not yet been examined for it"* — and v1.6's
> own vacuity pre-check for `op:cc-median-resurgence-execute` (hold `β₂` fixed,
> vary the lower-order coefficients, confirm `S_{ζ*}` moves) is an instance of it.
> **Whether `S_{ζ*}` passes that pre-check is not settled here.** `ξ₀` and `ρ`
> provably do not move; `S_{ζ*}` is a different object and nothing above decides
> it either way.
>
> The v1.6 citation repair is the algebraic half of the same fact:
> `10.5281/zenodo.20542162` derives `χ_d(c) = 1 + (−1)^{d+1}(β_d/d^d) c^d`
> symbolically and `d`-free, **with only `β_d` on the edge**.

---

## 6. The Borel material

### 6.0 Naming prohibition — binding on this notice and everything downstream

> **`K` is the amplitude at `ξ₀ = 2/√3`. `S_{ζ*}` is the Stokes constant at
> `ζ* = 2ξ₀ = 4/√3`.** They sit at points a factor of two apart in the action.
> **Neither name may ever be used for the other — not in prose, not in code, not
> in output filenames.** Any text that migrates out of this section carries this
> prohibition with it.

### 6.1 `ζ* = 2ξ₀` is an action difference, not a change of variable

`ξ₀ = |c| = 2/√β₂` is the action of a **single** formal solution: the slope-1/2
characteristic root in `exp(c/u)`, with `c² = 4/β₂`. The quantity
`ζ* = |c₊ − c₋| = 2|c| = 2ξ₀ = 4/√3` is the **action difference between the two
conjugate formal solutions**. The two numbers are different objects, at different
points of the Borel plane, and no change of variable relates them.

This is not an inference from the numbers. The Borel conventions were extracted
verbatim from the pipeline sources and are **identical across them** — Borel
variable `ζ ≡ w`, the series being transformed the coefficients `a_k` of `S(u)`,
normalisation `k! = Γ(k+1)`, uniformiser `u = √z` — which is exactly what
excludes the "same singularity in different variables" reading. The decisive
statement is in `sessions/2026-05-01/CC-PIPELINE-G2/g2_pade_borel.py`, lines 5–12,
which gives `zeta* = 2·c0 = 4/sqrt(3)` and justifies it as the *action of the
partner formal solution*. Classification: **a different singularity**
(`S3A-*`, STRUCTURAL).

### 6.2 The halving, and the ~1.7 % residual

The explicit halving is at `sessions/2026-05-01/CC-PIPELINE-G/vquad_recovery.py`,
lines 70–79; its own comment deliberates and contradicts itself, and the G2
pipeline resolves it against the halving. The previously unexplained ~1.7 %
residual is fully accounted for by two effects together: comparison against the
**halved** target, plus root-test truncation bias at `k ≈ 196` (`K_FORMAL = 200`,
samples `k = 193 … 200`, with convergence only `O(ln k / k)`). G2 at `K = 5000`
with conformal Padé reduces the disagreement to about seven digits:
`2.309400429346603600679460442221…` against `4/√3 = 2.309401076758503058…`.

No numerical re-derivation of the residual was performed in the session that
established this; the account is STRUCTURAL.

### 6.3 `op:cc-median-resurgence-execute`, restated

The v1.3 statement of this open problem did not name the series it acts on, and
named a Painlevé target that has since moved. Restated:

> **`op:cc-median-resurgence-execute` (restated at v1.7).** Run median Écalle
> resurgence on **the formal coefficient series `S(u) = 1 + Σ_{k≥1} a_k u^k`
> obtained from the Birkhoff formal solution
> `f₊(u) = exp(c/u) · u^ρ · S(u)` of the order-2 ODE governing
> `f(z) = Σ_n Q_n z^n` at `z = 0`, in the uniformiser `u = √z`, after stripping
> `exp(c/u)` and `u^ρ`** — for `V_quad` (`β₂ = 3, β₁ = 1, β₀ = 1`, `ρ = −11/6`),
> at 5000 coefficients and `dps = 250`, with `ζ* = 4/√3` pinned at 200 digits.
> The Borel transform is `B(ζ) = Σ_k a_k ζ^k / k!`, normalisation `Γ(k+1)`, Borel
> variable `ζ` conjugate to `k`. Target: extract the leading alien amplitude
> `S_{ζ*}` at `ζ*`.
>
> Status at v1.7: this resolves the residual Laplace step of `op:cc-formal-borel`
> for `V_quad`. **It does not close a `V_quad →` Painlevé correspondence at the
> Stokes-data level**, for two reasons that must be stated together:
> (i) the normalisation map is open (§6.5); and (ii) **the Painlevé target named
> in the v1.3 statement is stale, and was already corrected in the record** —
> v1.4 (2026-06-07) replaced `P-III(D₆)` throughout by the Painlevé V transcendent
> on the Sakai surface `D₅^(1)` (`W(A₃^(1))`, `δ = −1/2 ≠ 0`), and v1.5 marked
> that identification **conjectural** (companion paper Conjecture 4.1,
> `10.5281/zenodo.20455089`, read at v1.2). In this repository the same
> reclassification is recorded at
> `sessions/2026-05-29/T1-SYNTH-VQ-N1-VQUAD-RECLASSIFICATION-APPLY`, with the
> superseding disposition in
> `sessions/2026-05-02/VQUAD-PIII-NORMALIZATION-MAP/SUPERSEDED_BY_VQ-N1.json`.
> Any restatement that keeps the `P-III(D₆)` wording is repeating a premise the
> record corrected two versions ago.
>
> **v1.6 additions retained, not replaced.** v1.6 gave this problem an explicit
> falsifier with a numeric threshold, and a vacuity pre-check to be run before its
> compute budget is committed: hold `β₂` fixed, vary the lower-order coefficients,
> and confirm that `S_{ζ*}` actually moves. **The threshold itself has not been
> read** — it is in §9 of the v1.6 PDF, which could not be downloaded (§1) — so
> this restatement names the series and corrects the target and **does not restate
> the falsifier**. It **points** instead: the falsifier and its numeric threshold
> stand where v1.6 put them, in **§9 of version `10.5281/zenodo.22782807`**, and
> that is the citation a reader should follow. Pointing at unread text is
> accurate; paraphrasing it would not be. The operator must carry the v1.6
> falsifier text forward verbatim; nothing here supersedes it. v1.6 also marked
> all surviving §9 cost estimates unverified, which includes this one.
>
> The v1.3 forecast attached to this problem (H4: 30–50 digits, central ~40) was
> and remains **a theoretical prediction, not an executed measurement**, and H4
> explicitly does **not** forecast a closed form for `S_{ζ*}`.

### 6.4 A negative result for `S_{ζ*}`, against a search space printed in full

**The space is printed in full below, with no ellipsis, because a printed basis is
what lets a reader check it for internal degeneracy and an elided one is what
hides it.** That is not rhetoric: the first version of this search was run in a
space containing `Γ(1/6)` alongside `Γ(1/3)`, `π`, `2` and `3`, and that space is
**degenerate**. Legendre duplication at `z = 1/6` together with reflection at
`1/3` gives

```
Γ(1/6) = 2^(2/3) · √3 · Γ(1/3)² / (2√π)
```

(proved symbolically; `|difference| = 0.0` at dps 80, `S22-21`, PROVEN), so PSLQ
returned that identity — **with coefficient exactly zero on `log C`** — for the
target and for all three decoys alike. The search never tested the target. Its
vacuity pre-check nevertheless reported the required *three decoys rejected, one
control accepted* and so **passed for the wrong reason**. That first stage is
**VOID, not negative**, and its result is withdrawn rather than edited.

The corrected space, complete:

```
v = [ log C , log 2 , log 3 , log π , log Γ(1/3) , 1 ]

seeking integers (m, a, b, c, d, f) with m ≠ 0 such that

    m·log C + a·log 2 + b·log 3 + c·log π + d·log Γ(1/3) + f = 0

bounds:   |coefficient| ≤ 10^6
          1 ≤ |m| ≤ 12
          dps 120,  D_trust = 100
          cost = n_nonzero · log10(max|coeff|) ≤ 0.40 · D_trust = 40
```

`Γ(1/6)` was **removed as redundant**, so the corrected space is strictly
*smaller* than the degenerate one and no closed form representable in the original
space is lost. The bounds are unchanged from the withdrawn stage, deliberately.
Acceptance required **all four** of: a relation within bounds; cost ≤ 40;
stability at 90 and at 80 digits; and reconstruction of the target to ≥ 95 digits
at dps 150.

**The pre-registered result — a statement about a search, not about the
constant:**

> No multiplicative relation `C = ± 2^a 3^b π^c Γ(1/3)^d e^f` exists with all
> coefficients bounded by `10^6`, `1 ≤ |m| ≤ 12` and digit cost ≤ 40, against
> `C = 8.1273367954950723671…` known to 100 decimal digits. No candidate was
> returned at any bound, so no rejected candidate has a digit cost to report. The
> constants were first shown mutually independent by a degeneracy pre-check that
> returned no relation at any bound; all three decoys were rejected on their own
> merits; and the positive control `4π²/(3Γ(1/3))` was recognised at cost
> **1.5051**, at every bound.
>
> **Label: VERIFIED.** **This excludes that space.** It is **not** evidence that
> `C` has no closed form, and it says nothing about spaces containing other Gamma
> values, other algebraic irrationalities, polylogarithms, or `ζ(3)`.
> (`S22-22`, dps 120.)

**This negative is filed under a new tag, `op:cc-szeta-closed-form`, and not
under `op:cc-stokes-closed-form`.** The two are kept apart deliberately:

* **`op:cc-szeta-closed-form`** — does `C` (equivalently `S_{ζ*} = 2πi·C`, the
  amplitude at `2ξ₀`) admit a multiplicative closed form? The §6.4 result is a
  negative **against the one space printed above** and is recorded as the first
  entry under this tag, together with its stated space, so that any later search
  is read as widening a printed space rather than as a fresh question.
* **`op:cc-stokes-closed-form`** — does the CC-channel connection-coefficient
  **ratio match** the Riemann–Hilbert datum of `P_V/D₅^(1)` at the `V_quad`
  τ-parameter? This is an identification question inherited from the demoted
  Theorem 3.7(iii) at v1.5.

**How they relate, without merging.** A closed form for `C` would be *evidence
bearing on* `op:cc-stokes-closed-form`, because the Riemann–Hilbert datum is
expected to be expressible in Gamma values; and the identification, if ever
established, would *supply a candidate* for `C`. But neither implies the other:
`C` could have a closed form with the identification false, and the
identification could hold with `C` outside every Gamma basis. **The §6.4 negative
therefore says nothing about `op:cc-stokes-closed-form`, and must not be cited as
though it did.** They both mention Stokes data; that is a shared subject, not a
shared question — precisely the one-name-two-objects failure §6.0 forbids for
`K` and `S_{ζ*}`, applied here at the level of problems rather than constants.

### 6.5 The normalisation caveat that travels with `C`

`C` is read in **`V_quad` native normalisation**, with `S_{ζ*} = 2πi·C` and the
convention *leading `B[Φ] = 1`*. The `V_quad →` Painlevé normalisation map
**remains OPEN**. Anything found for `C` is therefore a closed form *of that
number in that normalisation*, and may not be compared with quantities computed in
a sectorial basis under a different convention without the map. This caveat is not
optional and is not separable from the negative result above.

---

## 7. The formal type of the generating-function operator

### 7.0 Which operator, and which it is not

Summing the recurrence against `z^n` gives, for the generating function
`f(z) = Σ_n Q_n z^n` of the **denominators**,

> `[ 1 − z·b(θ+1) − z²·a(θ+2) ] f = 1`,  `θ = z d/dz`,

with `a ≡ 1` in Channel Theory's own recurrence and general `deg a = e` allowed
below. Write `L_d := z·b(θ+1) + z²·a(θ+2) − 1`. The question asked here is the
**formal type of `L_d`**: its singular points, their Newton polygons, and the
multiset of Katz invariants, compared against the ten-row classification of
van der Put–Saito, Table 2.1 (p. 2635).

**This is not the object of §0 item 4.** That item concerns whether the
CC-channel **connection-coefficient ratio** matches the Riemann–Hilbert datum of
`P_V/D₅^(1)` at the `V_quad` τ-parameter — a statement about monodromy data of a
different object, carried under `op:cc-stokes-closed-form` and **conjectural**
since v1.5. `L_d` is the operator annihilating a generating function of
denominators. **Both are labelled by Painlevé equations; that is a shared
vocabulary, not a shared object**, and §6.0's prohibition applies here as it
does to `K` and `S_{ζ*}`. Nothing below is offered as evidence for or against
the `V_quad` identification, and §7.4 says why the apparent tension is not
resolved here.

### 7.1 What is established, in three tiers

Throughout, `deg b = 2` and `deg a = e ∈ {0, 1, 2}`, with `β₂ ≠ 0` and
`α_e ≠ 0`. A row of Table 2.1 is **compatible** with `L_d` when the multiset of
Katz invariants of `L_d` equals the row's printed multiset.

**Tier 1 — the exclusion. `D̃₅ / P_V` is not compatible with `L_d` for any
`e ∈ {0,1,2}`.** Its printed multiset `{0, 0, 1}` is not the multiset of `L_d`
for any of the three degrees. VERIFIED — the check is an equality of multisets
against a printed table, and it has been performed **twice independently**: once
here, and once by a reader given only the operator, its conventions and page
images of pp. 2634–2637, with no access to this work, its conclusions, or its
vocabulary. The same reader also excludes `D̃₄/P_VI`, `D̃₆/PIII(D₆)`, `Ẽ₆/P_IV`,
both `Ẽ₇/P_II` rows and `Ẽ₈/P_I` for every `e`.

**Tier 2 — the reachable set.** The rows compatible with `L_d` are

| `e = deg a` | Katz multiset | compatible row |
|---:|---|---|
| 0 | `{1/2, 1/2}` | `D̃₈ / PIII(D₈)` |
| 1 | `{1/2, 1}` | `D̃₇ / PIII(D₇)` |
| 2 | `{0, 0, 1/2}` | `D̃₆ / P_V(deg) = PIII(D₆)` |

and no others. STRUCTURAL, for the reason in §7.2 — a matching multiset is
**necessary, not sufficient**. This set too was obtained independently by the
same isolated reader, whose `e`-sensitivity control confirms that the method
does respond to `e` rather than ignoring it. Channel Theory's own recurrence is
the case `a ≡ 1`, i.e. `e = 0`, and so falls in the `D̃₈ / PIII(D₈)` row.

**Tier 3 — coefficient dependence.** Which row is reached depends on
`(α₂, α₁)` generically, with an exceptional locus of codimension 3.
**STRUCTURAL, and this tier is not independently confirmed.** It was found in
the course of a re-derivation that corrected an earlier error of its own, and
both isolated readings stop short of it: each states explicitly that it did not
classify the coefficient subloci on which an apparent singularity may be
removed by a common factor. A reader should treat tier 3 as the weakest of the
three and should not assume the exceptional locus has been characterised.

### 7.2 Why exclusions and matches carry different labels

Equality of Katz multisets is a **necessary condition** for `L_d` to sit in a
given row's family, not a sufficient one. A mismatch therefore settles the
question — the row is excluded, and that is VERIFIED, being an equality check
against a printed table. A match does not: it leaves open whether `L_d` actually
lies in the corresponding moduli family, which would need the classification's
sufficiency and not merely its invariants. That is why every positive row above
is STRUCTURAL while every exclusion is VERIFIED. **The asymmetry is deliberate
and must not be flattened in restatement.** It was arrived at independently by
the isolated reader, which recorded the same reason unprompted.

### 7.3 What was actually checked against the page

The ten rows of Table 2.1 were transcribed **three times independently** — once
during preparation and once by each of two readers — and the three
transcriptions agree in all ten rows and all six columns, including which
entries carry the printed dash. No statement in §7 rests on a single reading of
the table. The page images were rendered from the held PDF and each folio number
was read by eye from the image rather than inferred by index arithmetic. The
article is under *tous droits réservés*; no part of it is reproduced in this
deposit, and §7 cites it rather than restating it.

### 7.4 What §7 does not settle

* **It does not dispute, or support, the `V_quad` Painlevé-V identification.**
  That identification would have to be about the same object for `D̃₅/P_V`'s
  exclusion here to bear on it, and the two objects have not been shown to
  coincide. Asserting the tension either way would be the one-name-two-objects
  error twice over. Whether the generating-function operator and the `V_quad`
  Borel-plane datum determine one another is **open, and carries no tag**; none
  may be invented for it.
* **It does not establish sufficiency.** See §7.2.
* **It does not extend beyond `deg b = 2` or `e ≤ 2`.** Nothing above is a
  statement about general `d`.
* **It rests on one published table**, read three times, not on an independent
  derivation of the classification.

---

## 8. Open problems as they now stand

| Tag | Status at v1.7 |
|---|---|
| `op:xi0-degree-d` | **The algebraic part is closed.** `ξ₀ = d/\|β_d\|^{1/d}` holds at every `d ≥ 1` (§2), with no positivity hypothesis and no degree ceiling. v1.6 had already restated the problem as having **no per-degree computation remaining and an analytic residual**; that analytic residual is `op:xi0-singularity-type` and is **not** closed by §2. |
| `op:xi0-d3-direct` | **WITHDRAWN as vacuous at v1.6** — not answered, not subsumed. §5 now supplies the structural reason in place of v1.6's sweep. |
| `op:xi0-singularity-type` | **OPEN**, and this is the live successor problem. The **type** of the singularity at `ξ₀` — simple pole, branch point, algebraic-logarithmic — is untouched by the radius proof. Whether `ξ₀` is itself a Borel singularity, e.g. on another sheet or of another series, was not investigated here and is **not excluded**. |
| `op:cc-formal-borel` | **OPEN**, residual Laplace step; carries a v1.6 falsifier not read here (§6.3). |
| `op:cc-median-resurgence-execute` | **OPEN**, restated at §6.3 with its series named and its Painlevé target corrected; its v1.6 falsifier and vacuity pre-check stand unchanged. |
| `op:cc-stokes-closed-form` | **OPEN.** Created at v1.5 from the demoted Theorem 3.7(iii): the match between the CC-channel connection-coefficient ratio and the Riemann–Hilbert datum of `P_V/D₅^(1)` at the `V_quad` τ-parameter. **The §6.4 negative does not belong to this tag** and is not evidence about it (§6.4). |
| `op:cc-szeta-closed-form` | **OPEN; new at v1.7.** Does `C` — equivalently `S_{ζ*} = 2πi·C`, the amplitude at `2ξ₀` — admit a multiplicative closed form? First entry: the §6.4 negative, which excludes **only** the space printed there in full. Deliberately distinct from `op:cc-stokes-closed-form`; see §6.4 for how the two relate without merging. |
| — | A closed form for `r_∞`. Open, and the only transcendental input in `K`. No tag; none may be invented. |
| — | **New at v1.7:** whether the generating-function operator `L_d` and the `V_quad` Borel-plane datum determine one another. §7 reads `L_d`'s formal type against van der Put–Saito Table 2.1 and excludes `D̃₅/P_V` at `deg b = 2`, `deg a ≤ 2`; whether that bears on `op:cc-stokes-closed-form`'s Painlevé-V identification is exactly what is **not** established (§7.0, §7.4). No tag; none may be invented. |

---

## 9. What this notice does not claim

* **No formal verification.** Seven `sorry`s stand; nothing is machine-checked.
* **`K` is not proven.** VERIFIED to 109–115 digits, with a vacuity control. The
  label does not move in prose.
* **The priority of `s` is not settled**, because Wong & Li II was not obtained.
* **`C` is not shown to be transcendental, irrational, or without closed form.**
  One explicitly printed space is excluded.
* **No claim about a Painlevé label for `V_quad`** is made or repeated here. The
  current record's own identification — Painlevé V on Sakai `D₅^(1)` — is
  **conjectural** by v1.5's statement, and this notice neither strengthens nor
  disputes it. In particular **§7's exclusion of `D̃₅/P_V` is not evidence about
  it**: §7 classifies the formal type of the generating-function operator `L_d`,
  and it has not been shown that `L_d` and the `V_quad` datum are the same
  object (§7.0, §7.4).
* **§7's positive row matches are not claims of family membership.** A matching
  Katz multiset is necessary, not sufficient; the exclusions are VERIFIED and
  the matches are STRUCTURAL, and that asymmetry is deliberate (§7.2).
* **§7's tier 3 is not independently confirmed.** The coefficient dependence and
  its codimension-3 exceptional locus rest on one derivation, which corrected an
  earlier error of its own; both isolated readings stop short of the subloci
  (§7.1).
* **`op:xi0-degree-d` is not reported as closed.** §2 closes its algebraic part;
  the analytic residual is open and is named `op:xi0-singularity-type` (§2, §8).
* **No forward reference is made to any undeposited document.** Material cut from
  elsewhere has been brought into this notice in full rather than promised to a
  future one. A pointer may be added in a later version if and when the document
  has an identifier; until then this notice cites only records that exist.
* **The v1.5 and v1.6 PDFs were not obtained** (HTTP 504). Everything quoted from
  v1.4–v1.6 comes from the deposited **descriptions**, held in `refs/`. **No §9
  falsifier text is reproduced**, because none was read.
* **No claim is made that the attached PDF is a v1.7 build.** It is the v1.6
  build, carried over unchanged, and the header says so. Nothing in this notice
  should be read as describing a document that was rebuilt for this version.
* **The cross-reference defect of v1.0–v1.5 is not re-litigated here.** Per v1.6:
  in those versions every cross-reference rendered as "Theorem N" regardless of
  the environment's class, so `"Theorem N.N"` in v1.0–v1.5 running text names
  whatever class the numbered block declares. Quotations in this notice follow
  the block, not the cross-reference.

---

## 10. Sources held and hashed

| Source | Location | Note |
|---|---|---|
| Gautschi, *SIAM Rev.* 9 (1967) | `CT-S8-LITCHECK/refs/gautschi1967.pdf`, `g1967_p35_mid.png` | Thm 2.3(a) p. 35; Thm 1.1 p. 31 |
| DLMF §3.6(ii) | `CT-S8-LITCHECK/refs/dlmf_3_6.txt` | Pincherle dichotomy |
| DLMF §2.9(ii) | `CT-S8-LITCHECK/refs/dlmf_2_9.txt` | (2.9.5), (2.9.6), (2.9.14) deferral |
| Birkhoff–Trjitzinsky, *Acta Math.* 60 (1933) | `CT-S8-LITCHECK/refs/bt1933.pdf` | normal-solution shape, §9 p. 69 |
| Nemes (2026), arXiv:2508.15246v2 | `CT-S8-LITCHECK/refs/nemes2025.pdf` | connection coefficients |
| Odlyzko, *Asymptotic Enumeration Methods* | `CT-S24-PAPER-OUTLINE/refs/odlyzko_asymptotic_enum.pdf`, `CT-S24-PAPER-OUTLINE/refs/odlyzko_p77.png` | p. 77, attribution split |
| Wong & Zhao, *Anal. Appl.* 20 (2022) | `CT-R1-AUDIT/refs/wong_zhao_2022_recent_advances_arxiv-2204.09305.pdf` | arXiv v1 pin, sha256 `123ab322…` |
| Ibrahim & Salvy, SODA 2024 | `CT-R1-AUDIT/refs/ibrahim_salvy_2023_positivity_certificates_arxiv-2306.05930.pdf` | quote the weaker printed form |
| Wong & Li II (1992) | **NOT HELD** | paywalled, HTTP 403, not obtained |
| van der Put & Saito, *Ann. Inst. Fourier* 59 (2009) | `CT-R1-AUDIT/refs/vanderPut-Saito-AIF-2009-59-7-2611.pdf`, page images of folios 2634–2637 | Table 2.1 p. 2635; sha256 `1666bd6b…`; *tous droits réservés*, not reproduced |
| Channel Theory v1.3 description | `sessions/2026-05-02/CHANNEL-THEORY-V13-RELEASE/zenodo_description_v1.3.txt` | concept DOI, version DOIs, v1.3 changelog |
| Channel Theory **v1.6** record + description | `refs/zenodo_22782807.json`, `refs/zenodo_22782807.description.txt` | the current published version; sha256 `cacfb91d…` / `82d51c53…` |
| Channel Theory **v1.5** record + description | `refs/zenodo_22717792.json`, `refs/zenodo_22717792.description.txt` | sha256 `fe6ca2f1…` / `0898719b…` |
| Channel Theory **v1.4** record + description | `refs/datacite_20585624.json`, `refs/datacite_20585624.description.txt` | DataCite fallback; sha256 `58ba35aa…` / `dd37d2a8…` |
| Channel Theory **v1.3** record (DataCite) | `refs/datacite_19972394.json`, `refs/datacite_19972394.description.txt` | sha256 `0c118344…` / `d278d5fa…` |
| Channel Theory **concept** record | `refs/datacite_concept.json` | current version `1.6`; six `HasVersion` relations; sha256 `22978f14…` |
| v1.5 / v1.6 **PDFs** | **NOT HELD** | HTTP 504 on both file endpoints, retried; §9 falsifier text therefore unread |
| Channel Theory v1.3.1 source | `sessions/2026-05-08/T1-OPERATOR-CT-V131-3.5.1-R1A-AMENDMENT-VQUAD-CAVEAT-117/channel_theory_outline_v131_with_r1a_caveat.tex` | newest in-repo source |
| `ζ*` convention | `sessions/2026-05-01/CC-PIPELINE-G2/g2_pade_borel.py` L5–12 | `zeta* = 2·c0` |
| the halving | `sessions/2026-05-01/CC-PIPELINE-G/vquad_recovery.py` L70–79 | self-contradictory comment |
| `V_quad` reclassification | `sessions/2026-05-02/VQUAD-PIII-NORMALIZATION-MAP/SUPERSEDED_BY_VQ-N1.json` | supersedes the P-III(D₆) premise |

*AEAL claims cited by this notice:* `S1-01`, `S1-02`, `S1-03`, `S1-04`, `S1-05`,
`S1-06`, `S2-01`, `S2-02`, `S2-03`, `S2-04`, `S3B-04`, `S3B-05`, `S3B-06`,
`S21-31`, `S21-32`, `S21-33`, `S21-76`, `S22-21`, `S22-22`, `S24-12`, `S26-01`,
`S26-04`.

---

*End of draft v1.7 notice. Draft only — no deposit, no metadata edit.*
