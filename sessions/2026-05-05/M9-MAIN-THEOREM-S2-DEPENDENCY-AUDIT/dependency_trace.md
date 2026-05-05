# Dependency Trace — M9 main theorem ↔ closed-form S_2

This file records the clause-by-clause dependency analysis demanded by
Step 2 of the relay spec. Because Step 1 returned NONE
(`INDETERMINATE_NO_FORMAL_STATEMENT`), this trace is **non-binding** —
it is a pre-rendering across the schema-level fragments that exist on
disk, recorded for synthesizer P-008/P-009 reference only.

## Reference: classification types from Step 2.2 of the spec

- **(a) closed-form-value invocation** — e.g. "S_2 = explicit
  expression in Gamma values / algebraic numbers / transcendentals".
- **(b) structural-existence invocation** — e.g. "the second Stokes
  constant exists / is well-defined / acts on the Borel transform".
- **(c) sign-of-discriminant / dichotomy invocation** — e.g.
  "Δ_b > 0 vs Δ_b < 0 corresponds to S_2 in / not in some structural
  set".
- **(d) numerical-bound invocation** — e.g. "|S_2| = ..." measured
  numerically; "S_2 lies in some numerical cone".

Verdict per fragment:

- HARD: at least one type-(a) occurrence on which the statement
  logically depends.
- SOFT: only type (b)/(c)/(d), but statement still references S_2.
- NONE: no S_2 reference whatsoever.

---

## Fragment 1 — Umbrella v2.0 `eq:Phi-functor`

**File:** `tex/submitted/umbrella_program_paper/main.tex`, L273
**Verbatim:**

```latex
\Phi : \PCF(1,b) \;\longmapsto\;
       \bigl(\Delta_d(b),\ \PetN{\Delta}(\tau_b),\ \xi_0(b)\bigr)
```

**S_2 occurrences:** 0 (the bridge functor's image is
`(Δ_d, ‖Δ‖_Pet, ξ_0)` only; no Stokes data axis).

**Verdict for this fragment:** **NO_DEPENDENCY.**

---

## Fragment 2 — Umbrella v2.0 `prob:b4-allD`

**File:** `tex/submitted/umbrella_program_paper/main.tex`, L686–696
**Verbatim:**

> Establish $A_{\mathrm{PCF}}(b) = 2d$ for all $d$ and all irreducible
> non-singular $b \in \Q[x]$ with $\deg b = d$, in the sharp form of
> \eqref{eq:b4-conjecture}. PCF-1 v1.3 verifies $d=2$; PCF-2 v1.3
> verifies $d \in \{3, 4\}$ on $110/110$ families. The strong-form
> upgrade follows the Birkhoff--Trjitzinsky asymptotic theory of
> irregular linear difference equations
> \cite{Birkhoff1930, BirkhoffTrjitzinsky1933}; this is the gating
> move toward the SIARC Master Conjecture v0.

**S_2 occurrences:** 0.

**Verdict for this fragment:** **NO_DEPENDENCY.** The gating move named
here is Birkhoff--Trjitzinsky theory at the level of *irregular linear
difference equations* (i.e. the formal-series existence + structural
asymptotic theory), not the closed-form alien amplitude S_2 of
particular families.

---

## Fragment 3 — Picture v1.18 M9 block

**File:** `siarc-relay-bridge/sessions/2026-05-04/PICTURE-V18-AMENDMENT-DRAFTING/picture_v1.18.md`, L973–989
**Verbatim:**

> M9: SIARC-MASTER-V0 announcement — Phi formally stated and the
>     master classification result conditional on P-NP + P-B4 + P-CC
>     [downstream; gated on M2 + M4 + M6]
>     NB: M9 is one step further out under v1.1 because M4's path
>     now requires primary-source resolution before Phase 2 can even
>     start.
>     🔄 v1.15 amendment: M9 gating reduces from {M2, M4, M6} to
>     **{M4, M6} UNCONDITIONALLY** (D2-NOTE v2.1 UPGRADE_FULL
>     2026-05-03; M2 closure citation-complete via QS-2 verdict).
>     **First time in the program where M9 gating reduces
>     unconditionally.** Pre-stage drafting for SIARC-MASTER-V0
>     announcement may proceed in parallel with M4 / M6 closure.
>     🔄 v1.16 amendment: M4 status now
>     `M4-with-formal-baseline-+-structural-roadmap`
>     (Phase 2 verdict UPGRADE_PARTIAL_FORMAL_LEVEL 2026-05-04;
>     A_naive <= d+1 derived; closure path = T1 Phase 3 borderline-case
>     anormal ansatz + sectorial upgrade). M9 gating remains {M4, M6}
>     unconditionally (substantively unchanged but M4 has more content).

**S_2 occurrences in M9 block:** 0.

**Adjacent M8b block (L959–972) S_2 occurrences:** 4, all type-(c)
numerical-foreclosure ("S_2 PERMANENTLY FORECLOSED via Stage-2-LSQ ...
Borel-Padé ... structurally open"). M8b is a sibling milestone to M9
in the linear M-block, not a gate.

**Verdict for this fragment:** **NO_DEPENDENCY** at the M9 statement
level. The v1.15 amendment explicitly excludes M8b from M9 gating.

---

## Fragment 4 — Channel Theory v1.3 §"Implications for the Master Conjecture"

**File:** `siarc-relay-bridge/sessions/2026-05-02/CHANNEL-THEORY-V13-RELEASE/channel_theory_outline.tex`, L1336–1349
**Verbatim:**

```latex
\section{Implications for the Master Conjecture}
\label{sec:implications}

A rigorous announcement of the Master Conjecture requires:
\begin{enumerate}
\item Pipeline closure for the five non-$\Vquad$ families
(\textsf{op:cc-monodromy-RH}). \Cref{prop:xi0,tab:cc-channel-v2}
provide the formal-solution data for all six families;
the missing piece is the full Stokes-matrix datum.
\item No-go proof or refutation (\textsf{op:no-go-proof})
of \Cref{conj:nogo}.
\item Bridge identity tier discrimination
(\textsf{op:bridge-witness-tier}) for at least one family
beyond $\Vquad$.
\item Cubic extension along
\cite{siarc_pcf2_v11, siarc_pcf2_program}
(\textsf{op:xi0-degree-d}).
\end{enumerate}
```

**S_2 occurrences:** 0 (the symbol "S_2" does not appear). However:

- Item 1 references "the full Stokes-matrix datum". This is a Stokes
  *data* invocation, not an S_2 *value* invocation. Type-classification:
  **(b) structural-existence**.
- Elsewhere in CT v1.3 the symbol `S_{ζ_*}` appears (L1379), the
  V_quad leading alien amplitude. This is structural (it's the channel
  functor's image at V_quad); the value of S_{ζ_*} is what op:vquad-cc
  closes, not the master conjecture statement.

**Verdict for this fragment:** **SOFT_DEPENDENCY.** The Master
Conjecture announcement, as scoped by CT v1.3 §"Implications", requires
the *Stokes-matrix datum* for the five non-V_quad families to be
populated — but as a structural object (the multiplier vector), not as
a closed-form value of any individual constant.

---

## Fragment 5 — Channel Theory v1.3 channel-functor definition

**File:** `siarc-relay-bridge/sessions/2026-05-02/CHANNEL-THEORY-V13-RELEASE/channel_theory_outline.tex`, L1026 ff.
**Verbatim:**

```latex
The Master Conjecture \cite{siarc_umbrella_v2} posits a functor
$\chi : \Sigmaspace \to \Channel$ where $\Sigmaspace$ is a
category of deformations of PCF families.
```

**S_2 occurrences:** 0.

The channel functor `χ` is defined as a categorical object. Its values
on individual families involve alien amplitudes structurally (V_quad
example, L109/L221), but the *defining statement* of `χ` does not
invoke any specific S_2 value.

**Verdict for this fragment:** **NO_DEPENDENCY** at the functor-definition
level.

---

## Fragment 6 — Umbrella v2.0 `prob:chi-Phi-compatibility`

**File:** `tex/submitted/umbrella_program_paper/main.tex`, L759–763
**Verbatim:**

> Establish that the bridge functor $\Phi$ of \eqref{eq:Phi-functor}
> factors through the channel functor $\chi$ of \cite{CT} in a way
> compatible with the cell decomposition $E / P_k / B$ of
> \S\ref{sec:triple-cells}. Tag: \textsf{op:chi-Phi-compatibility}.

**S_2 occurrences:** 0.

**Verdict for this fragment:** **NO_DEPENDENCY.** This problem
statement asks for a factorisation property of `Φ` through `χ`, not for
a closed-form value of any Stokes constant.

---

## Aggregate verdict (across schema-level fragments)

| Fragment | S_2 type | Per-fragment verdict |
|----------|----------|----------------------|
| 1 (Umbrella `eq:Phi-functor`) | none | NO_DEPENDENCY |
| 2 (Umbrella `prob:b4-allD`) | none | NO_DEPENDENCY |
| 3 (Picture v1.18 M9 block) | none in M9; (c) in M8b sibling | NO_DEPENDENCY |
| 4 (CT v1.3 §"Implications") | (b) structural Stokes-matrix datum | SOFT_DEPENDENCY |
| 5 (CT v1.3 χ functor) | none | NO_DEPENDENCY |
| 6 (Umbrella `prob:chi-Phi-compatibility`) | none | NO_DEPENDENCY |

**Aggregate (non-binding):** the worst case across all schema fragments
is SOFT_DEPENDENCY (Fragment 4); no fragment exhibits HARD_DEPENDENCY.
A draft Phi statement consistent with all six fragments would carry at
most a SOFT dependency, in which case the M9 announcement could
proceed with a structural caveat (no closed-form S_2 needed at
announcement time).

---

## Cross-check rule (Step 2 spec)

Spec: *any HARD_DEPENDENCY verdict must cite verbatim the clause that
invokes the closed-form value AND identify why the statement cannot be
re-cast in type-(b)/(c) language.*

No HARD_DEPENDENCY occurrence found. Cross-check rule is vacuously
satisfied.
