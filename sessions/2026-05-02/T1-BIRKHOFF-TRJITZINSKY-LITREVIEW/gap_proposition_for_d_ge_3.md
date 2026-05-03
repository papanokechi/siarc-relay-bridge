# Q3 — Precise gap proposition for the SIARC PCF stratum at $d \ge 3$

**Task:** T1-BIRKHOFF-TRJITZINSKY-LITREVIEW, Phase 1
**Date:** 2026-05-02
**Goal:** Formalise the literature-derivable interval
$A \in [\psi_{\mathrm{lower}}(d),\ \psi_{\mathrm{upper}}(d)]$ for the
SIARC PCF stratum at $d \ge 3$, classify the residual gap into one of
the four types (A / B / C / D), and recommend the Phase-2 entry point
conditional on the classification.

---

> **⚠ AMENDED 2026-05-03 per A-01 verdict** (`T1-A01-NORMALIZATION-RESOLUTION`,
> verdict label `A01_WASOW_READING_CONFIRMED`).
>
> All passages below that frame "$\sigma_{\mathrm{Wasow}} = 2 \sigma_{\mathrm{Adams}}$"
> as a possible normalisation-level factor-of-2 ambiguity (notably § 2 lines
> ~77–86, the Caveat block at § 4, and the "Halt-on-normalisation mismatch"
> bullet at § 5) are **resolved**: direct evidence from B-T 1933 page 5
> footnote 2 + Birkhoff 1930 page 2 footnote 2 + PCF-1 v1.3 §6 Thm 5 ansatz
> shows **no factor-of-2 ambiguity at the normalisation level** — Wasow /
> Birkhoff / B-T / Adams $\sigma$ all share the same $\mu$-units (per A-01
> verdict 2026-05-03). The Phase-1 worry was a paraphrase artefact (likely
> from a confused secondary-source recollection), not a real literature
> ambiguity.
>
> **Net effect on this document:** the **Wasow-normalisation reading** is
> confirmed (so the document's best-guess GAP_TYPE_C classification stands);
> the alternative GAP_TYPE_A scenario (which would have placed $B4 = 2d$
> outside the literature bracket) is **falsified** at the primary-source
> level. The remaining open work is the **lift** of $\psi_{\mathrm{lower}}$
> from $d$ to $2d$, not the normalisation match.
>
> No Phase-1 AEAL-logged claim is contradicted by this amendment; only the
> paraphrase commentary is corrected. The original Phase-1 prose is
> preserved below for audit-trail purposes; readers should treat the
> "$\sigma_{\mathrm{Wasow}} = 2 \sigma_{\mathrm{Adams}}$" framing as
> historical Phase-1 worry, **not** as a current open question.

---

## §1. Statement of B4 and the SIARC normalisation

**SIARC Conjecture B4 (sharp, umbrella v2.0 main.tex line 290).**
For every irreducible non-singular polynomial $b \in \mathbb{Q}[x]$
of degree $d \ge 2$, the polynomial-continued-fraction approximant
error $\delta_n = \mathrm{Pcf}(1, b)_n - \lim$ obeys
$$
   \log|\delta_n| \;=\; -A \, n \log n + \alpha \, n - \beta \log n + \gamma + o(1),
   \qquad A = 2d.
$$

**Empirical record cited from prior verdicts (no re-execution):**

* PCF-1 v1.3 Theorem 5: rigorous proof at $d = 2$ with the sign
  split $A = 4$ for $\Delta_2 > 0$, $A = 3$ for $\Delta_2 < 0$
  (the "two-branch anomaly").
* PCF-2 v1.3 R1.1 + R1.3 + Q1: $d = 3$ supported on $50/50$ cubic
  families and $d = 4$ supported on $60/60$ quartic families,
  joint $110/110$ at the relevant tail-window precision (dps
  $\ge 24$ minimum, $4000$ for the deep R1.3 cubic harvest;
  $A_{\mathrm{fit}} - 2d$ within $\le 1.0 \times 10^{-2}$ for
  cubic families, mean $A_{\mathrm{fit}} = 7.954$, $\sigma =
  3.7 \times 10^{-3}$ for quartic families).
* PCF-2 v1.3 / PCF2-SESSION-T2: at $d = 3$ on the $n = 50$
  R1.3 catalogue,
  $\rho(\log\|\Delta\|_{\mathrm{Pet}}, A_{\mathrm{fit}} - 6) = +0.638$,
  $p_{\mathrm{Bonf}}(K{=}14) = 8.6 \times 10^{-6}$, beating the
  $\log|j|$ baseline by $\sim 30\times$ in Bonferroni $p$.

The conjecture is **empirically supported** at $d \in \{3, 4\}$ in
the sense above; it is **not** rigorously pinned by any post-1933
result currently in the SIARC bibliography.

---

## §2. Translating B–T 1933 + descendants to bounds on $A$

We extract bounds on $A$ from the literature consulted in Q1+Q2.
The chain of reasoning is:

1. **Newton-polygon slope (B–T 1933 + Wasow 1965 §X.3).**
   The SIARC PCF stratum at degree $d$ corresponds to the
   three-term recurrence
   $\,p_2(x) y(x+1) - p_1(x) y(x) + p_0(x) y(x-1) = 0$
   with $p_0, p_1, p_2 \in \mathbb{Q}[x]$ and
   $\max(\deg p_0, \deg p_1, \deg p_2) = d$. In SIARC's
   canonical convention (PCF-1 v1.3 §2; PCF-2 v1.3 §2.1) the
   leading and trailing coefficients have $\deg p_0 = \deg p_2 = d$
   and $\deg p_1 = d$. Under this convention the Newton polygon
   at $\infty$ has a single slope
   $\,\sigma = d - n_0\,$
   for a normalisation shift $n_0$ that depends on the SIARC
   convention; the precise value is **the principal source of
   slack** in $[\psi_{\mathrm{lower}}, \psi_{\mathrm{upper}}]$.

2. **Formal characteristic exponents at $\infty$
   (Adams 1928 / B–T 1933 / Wasow 1965 §X.3).** The two formal
   solutions $\widehat y_{1,2}$ of the recurrence have
   characteristic exponents whose **difference** governs the
   approximant-error rate. Specifically, the SIARC ansatz
   $\log|\delta_n| = -A n \log n + \alpha n - \beta \log n + \gamma$
   exposes $A$ as $q \cdot \sigma$ in the normalisation of the
   Newton-polygon slope, where $q$ is the LCM denominator of
   the slope (here $q = 1$ in the regular case). In the
   normalisation of Adams 1928, this gives
   $A = 2 \sigma_{\mathrm{Adams}}$, while in the
   normalisation of Wasow 1965 §X.3 it gives
   $A = \sigma_{\mathrm{Wasow}}$, with
   $\sigma_{\mathrm{Wasow}} = 2 \sigma_{\mathrm{Adams}}$. Whether
   B4's $A = 2d$ corresponds to the Adams or Wasow
   normalisation depends on the SIARC convention, and **the
   agent could not pin this down from the secondary literature
   alone**. This is the central paraphrase ambiguity flagged
   in `handoff.md`.
   *[⚠ AMENDED 2026-05-03 per A-01: this factor-of-2 ambiguity
   is FALSIFIED — see top-of-file amendment block. Wasow,
   Birkhoff, B-T, Adams $\sigma$ all share the same $\mu$-units.
   Read the paragraph above as historical Phase-1 framing only.]*

3. **Sectorial-analytic upgrade (Turrittin 1955 / Immink 1984).**
   Once the formal slope is fixed, Turrittin 1955 (regular-
   singular case) or Immink 1984 (irregular Borel-1-summable
   case) upgrade the formal series to a genuine sectorial
   asymptotic of an analytic solution. **Both upgrades preserve
   the slope value**; they do not introduce new slack into
   $A$. The contribution of Turrittin / Immink to the
   $[\psi_{\mathrm{lower}}, \psi_{\mathrm{upper}}]$ bracket is
   therefore **not in the value of $A$ but in the rigour
   tier**: with Turrittin / Immink, the bracket is a rigorous
   theorem; without them, it is a formal-Newton-polygon
   prediction.

4. **Polynomial-coefficient refinement (Wasow 1965 §X.3).**
   For the SIARC sub-case where all $p_k$ are polynomials,
   Wasow's §X.3 refines B–T's bound: the formal Newton-polygon
   slope **equals** $\max_k(d_k - k_0)$ exactly (no slack from
   meromorphic corrections), and the polynomial coefficient
   structure constrains the formal exponents to a finite
   set of values $\{2d, 2d-1, \ldots, d, \ldots\}$ depending
   on the resonance pattern.

5. **Multisummability (Braaksma 1991/1992).** Relevant only at
   the SIARC arithmetic loci where the Newton polygon
   degenerates (multiple slopes), introducing fractional-rank
   corrections. **At generic $b$ in the SIARC PCF stratum,
   Braaksma is not invoked.**

---

## §3. Literature-derived bracket $[\psi_{\mathrm{lower}}(d), \psi_{\mathrm{upper}}(d)]$

Combining the chain above:

### $\psi_{\mathrm{upper}}(d)$ — upper bound.

**$\psi_{\mathrm{upper}}(d) = 2d$.**

**Derivation.** Wasow 1965 §X.3 (polynomial-coefficient
refinement of B–T 1933 / Adams 1928) shows that for a three-term
linear difference equation with polynomial coefficients of degree
exactly $d$ at the leading and trailing ends, the maximum formal
Newton-polygon slope at $\infty$ is bounded by **twice** the
ambient polynomial degree in the normalisation that matches the
SIARC ansatz, giving the **upper bound** $A \le 2d$.

**Rigour tier.** Theorem (Wasow 1965 §X.3 + Turrittin 1955 for
sectorial-analytic upgrade). The upper bound is rigorous in the
literature reading.

**Caveat.** The matching of normalisations between Wasow §X.3
and SIARC's $A = -\lim_n \log|\delta_n|/(n \log n)$ is **a
paraphrase from secondary sources**; a primary-source consultation
of Wasow §X.3 plus a direct computation in the SIARC normalisation
is required to certify $\psi_{\mathrm{upper}}(d) = 2d$ as a
**theorem-grade** literature bound. Currently it is a
**high-confidence paraphrase**; logged as borderline case
B-01 in `handoff.md`.

### $\psi_{\mathrm{lower}}(d)$ — lower bound.

**$\psi_{\mathrm{lower}}(d) = d$.**

**Derivation.** Birkhoff 1911 Thm 4 (the "regular-rank-1"
existence theorem for Newton-polygon slopes; predecessor to
B–T 1933) gives the **lowest possible non-trivial slope** of a
formal solution of an order-$n$ linear difference equation with
polynomial coefficients of degree $\le d$ as $\sigma \ge d/n$ in
Birkhoff's normalisation; for $n = 2$ this is $\sigma \ge d/2$,
which translates to $A \ge d$ in the SIARC normalisation under
the same matching as in $\psi_{\mathrm{upper}}$.

**Rigour tier.** Theorem (Birkhoff 1911), with the SIARC-
normalisation match **paraphrased from secondary sources** (the
match is implicit in Wasow 1965 §X.3 and Wimp–Zeilberger 1985,
but the explicit calculation in the SIARC normalisation is not
in the literature consulted).

**Caveat.** This lower bound is **substantially loose**:
empirically $A = 2d = \psi_{\mathrm{upper}}(d)$ at all $d \in
\{2, 3, 4\}$ where SIARC has data, so the literature-derived
$\psi_{\mathrm{lower}}(d) = d$ is a factor of **2** below the
empirical $A$. The Phase-1 reading is that
**$\psi_{\mathrm{lower}}(d) = d$ is the strict literature-
rigorous lower bound from Birkhoff 1911 / B–T 1933 alone**, and
that **tightening to $\psi_{\mathrm{lower}}(d) = 2d$ requires a
separate non-resonance / non-degeneracy argument** that the
SIARC PCF stratum sits at the **maximal-slope** point of the
Newton polygon, not the minimal-slope point.

### Resulting bracket.

$$
   \boxed{\,
     A \in [d,\ 2d]
     \quad \text{for } d \ge 3, \text{ literature-derivable}
   \,}
$$

with $A = 2d$ at the **upper end** of the interval. The interval
is **strictly loose**: $\psi_{\mathrm{lower}}(d) = d < 2d =
\psi_{\mathrm{upper}}(d)$.

---

## §4. Gap-type classification

The four types are:

* **GAP_TYPE_A:** $\psi_{\mathrm{lower}}(d) < 2d < \psi_{\mathrm{upper}}(d)$.
* **GAP_TYPE_B:** $\psi_{\mathrm{lower}}(d) = 2d$, $\psi_{\mathrm{upper}}(d) > 2d$.
* **GAP_TYPE_C:** $\psi_{\mathrm{lower}}(d) < 2d$, $\psi_{\mathrm{upper}}(d) = 2d$.
* **GAP_TYPE_D:** $\psi_{\mathrm{lower}}(d) = 2d = \psi_{\mathrm{upper}}(d)$.

**Phase-1 classification:** **GAP_TYPE_C.**

*Justification.* From §3, the literature-derived upper bound
$\psi_{\mathrm{upper}}(d) = 2d$ matches the conjectural value
B4. The literature-derived lower bound $\psi_{\mathrm{lower}}(d)
= d$ is strictly below $2d$ for $d \ge 1$. SIARC Conjecture B4
therefore sits **at the literature upper bound**; Phase 2's
target is to **lift the lower bound from $d$ to $2d$** via a
non-resonance / non-degeneracy argument on the SIARC PCF
stratum.

**Caveat on the classification.** Both $\psi_{\mathrm{upper}}(d)
= 2d$ and $\psi_{\mathrm{lower}}(d) = d$ depend on the
**normalisation match** between Wasow 1965 §X.3 / Birkhoff 1911
and the SIARC ansatz $\log|\delta_n| = -A n \log n + \dots$. If
the normalisation match shifts by a factor of $1/2$ (i.e. SIARC's
$A$ corresponds to Adams's $2\sigma$ rather than Wasow's
$\sigma$), then $\psi_{\mathrm{upper}}(d) = d$ and
$\psi_{\mathrm{lower}}(d) = d/2$, which would give **GAP_TYPE_A**.
Resolving this normalisation match is **the first item in the
"What would have been asked" section of `handoff.md`**.

If the operator's reading of the primary B–T 1933 (or Adams
1928) shows the normalisation puts SIARC's $A$ at **$\sigma$**
(matching Wasow), the Phase-1 classification stands as
**GAP_TYPE_C**. If at **$2\sigma$** (matching Adams), the
classification becomes **GAP_TYPE_A** with literature-derivable
bracket $[d/2, d]$ and $A = 2d$ **strictly above** the upper
bound — which would be a **major** halt condition (B4 would
contradict the literature) and would require Phase 2 to
re-derive both bounds from scratch.

The Phase-1 best-guess classification is **GAP_TYPE_C** under
the **Wasow-normalisation reading**, which is the one used by
all the secondary sources consulted (Wasow 1965, Wimp–Zeilberger
1985, Immink 1984). Under this reading, B4 is the
literature-rigorous **upper bound**, and Phase 2's task is to
**lift the lower bound to $2d$**.

---

## §5. Phase-2 entry recommendation conditional on GAP_TYPE_C

Under **GAP_TYPE_C**, Phase 2's task is to establish:

> **Theorem (Phase-2 target).** For every irreducible non-singular
> polynomial $b \in \mathbb{Q}[x]$ of degree $d \ge 3$, every
> formal solution of the SIARC three-term recurrence at $\infty$
> sits at the **upper vertex** of the Newton polygon (no
> lower-slope solutions occur), and the formal-to-analytic
> upgrade (Turrittin 1955 + Immink 1984) preserves this fact
> sectorially. Therefore $A_{\mathrm{PCF}}(b) = 2d$.

**Decomposition of the Phase-2 task into three sub-claims:**

* **P2.1 (Newton-polygon non-degeneracy).** For every
  irreducible non-singular $b$ with $\deg b = d \ge 3$, the
  Newton polygon of the SIARC three-term recurrence at $\infty$
  has a **single slope** equal to $d$ (in the Wasow
  normalisation), with **no spurious lower-slope vertices**.
  This is a finite combinatorial / algebraic-geometric statement
  about the leading coefficients of $p_0, p_1, p_2$.

* **P2.2 (formal-exponent extremality).** Among the two formal
  characteristic exponents $\rho_1, \rho_2$ of B–T 1933 Thm 1,
  **the difference $|\rho_1 - \rho_2|$ contributes to $A$
  exactly the maximal-slope value**, i.e. there is **no
  resonance cancellation** that would drop the leading
  $-A n \log n$ to a lower-slope $-A' n \log n$ with $A' < 2d$.

* **P2.3 (sectorial uniformity).** The Turrittin–Immink
  sectorial-analytic upgrade applies **uniformly across the
  SIARC PCF stratum** (no $b$-dependent loss of rigour at
  arithmetic loci). The PCF-2 v1.3 / SESSION-T2 finding that
  $j = 0$ cubic families exhibit a finite-$N$ tail-window
  artefact (rather than a violation) is consistent with this
  sub-claim.

**Recommended Phase-2 relay name:** `T1-BIRKHOFF-PHASE2-LIFT-LOWER`.

**Recommended Phase-2 inputs:**

* B–T 1933 directly (operator institutional access required).
* Adams 1928 directly (operator institutional access required).
* Wasow 1965 §X.3 directly.
* Immink 1984 LNM 1085 §II.3.
* PCF-2 v1.3 §2.1 (SIARC normalisation of $A$).
* PCF-2 v1.3 / SESSION-T2 (the modular-discriminant axis is
  the **separate** signal at sub-leading order $\delta = A_{
  \mathrm{fit}} - 6$; Phase 2 should not conflate the leading
  $A$ with sub-leading $\delta$).

**Recommended Phase-2 verdict labels:**

* `T1-PHASE2-PROVED-d>=3` — the lower-bound lift succeeds and
  B4 is rigorously established at $d \ge 3$.
* `T1-PHASE2-PROVED-d>=3-MOD-RESONANCE` — proved away from a
  finite list of resonance loci (the modular-discriminant
  axis residue), with the residue cells deferred to a
  follow-up.
* `T1-PHASE2-FAILED-NORMALIZATION-MISMATCH` — the
  normalisation match is **not** the Wasow reading (i.e.
  GAP_TYPE_A applies), and B4 contradicts the literature; this
  is a major halt.
* `T1-PHASE2-FAILED-RESONANCE-DEEPER-THAN-EXPECTED` — P2.2
  fails at a positive-measure subset of the SIARC PCF stratum;
  conjecture B4 needs refinement.

---

## §6. Summary

* **Literature-derivable bracket:** $A \in [d, 2d]$ for the
  SIARC PCF stratum at $d \ge 3$, under the Wasow-normalisation
  match (high-confidence paraphrase from secondary sources).
* **Gap type:** **GAP_TYPE_C**; B4 sits at the literature upper
  bound $\psi_{\mathrm{upper}}(d) = 2d$; the literature lower
  bound $\psi_{\mathrm{lower}}(d) = d$ is strictly looser.
* **Phase-2 entry:** lift $\psi_{\mathrm{lower}}(d)$ from $d$ to
  $2d$ via a Newton-polygon non-degeneracy + formal-exponent
  extremality + sectorial-uniformity argument
  (relay name `T1-BIRKHOFF-PHASE2-LIFT-LOWER`).
* **Halt-on-normalisation mismatch:** if a primary-source
  consultation reveals the SIARC ansatz uses Adams's $2\sigma$
  rather than Wasow's $\sigma$ normalisation, the bracket
  becomes $[d/2, d]$ and B4 is **outside** the literature
  bracket, which is a halt condition for the Phase-2 spec
  (the target theorem statement would have to be reformulated).
