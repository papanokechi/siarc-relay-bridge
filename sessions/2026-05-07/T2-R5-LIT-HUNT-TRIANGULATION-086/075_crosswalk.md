# Phase D — 075 Cross-Walk

**Session:** 086 T2-R5-LIT-HUNT-TRIANGULATION
**Phase:** D (cross-walk V1's chart-map against existing SIARC
  M6.CC B-candidates from 075 verdict)
**Substrate anchored to:** 075 STRUCTURAL_MISMATCH verdict
  (synthesizer_decision_packet.md SHA `59305DE4FAB19C70..D241D50`)
  + 069r1 §A.1.5 chart-map specification (cited inside 075
  `chart_map_required_form.md` SHA `9A2ED794476DDC7C..C3A92886`).

Substrate-inventory scope; no R1-closure assertion; no new theorem.

---

## §D.1 — Existing SIARC B-candidates (M6.CC dossier)

The 075 dossier names exactly **one** instantiated B-candidate:

- **B1** — BT 1933 §5 (13 a) periodic-functions across-strip
  Fourier / q-series expansion (per 075 `bt_5_13a_structural_form.md`).
  **075 verdict: STRUCTURAL_MISMATCH at all 7 GAP-PRIMITIVE axes.**

The 086 envelope §D.D2 instructs comparison "for each of B1, B2,
B3 (existing SIARC candidates from M6.CC dossier)". At fire time
(bridge HEAD `14e6b09`), only B1 has been instantiated; **B2 and
B3 are referenced in the envelope but are not present as named
substrate items in any LANDED bridge session**. This is recorded
as discrepancy D1 (envelope-substrate naming gap).

The 075 contingent-076 forward-pointer enumerates three candidate
literature targets for path-δ acquisition: Jimbo-Miwa 1981 II /
Conte-Musette 2008 / Forrester-Witte 2002. These are **literature
acquisition targets**, not pre-instantiated B-candidates.

For 086 cross-walk purposes, the operative candidate set is:

- **B1** = BT 1933 §5 (13 a) — instantiated; 075 verdict
  STRUCTURAL_MISMATCH.
- **B2 / B3** = no instantiated substrate at fire time.

## §D.2 — Cross-walk: V1 chart-map vs. B1 GAP-PRIMITIVES

The 075 dossier formalised the gap-side specification at 7
primitives [GAP-PRIMITIVE-B1..B7] (per 075 `chart_map_required_form.md`):

| GAP-axis             | Gap (069r1 §A.1.5)                                                                       | V1 (Phase B Levels 1-6)                                                                                                          | Verdict        |
|----------------------|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------|
| GAP-PRIMITIVE-B1     | Domain = real 3-tuple $(a_0, a_1, a_2)$ KNY chart; constraint $a_0 + a_1 = 1$.            | Domain = complex 2-tuple $(\alpha, \beta)$ Painlevé-III($D_6$) seed-solution parameters in form (1.1).                            | MISMATCH       |
| GAP-PRIMITIVE-B2     | Codomain = real 4-tuple $(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0)$ Okamoto null-sum 0. | Codomain = $(e_1, e_2, x_1, x_2, x_3)$ on monodromy manifold cubic surface (1.13); equivalently 4 Stokes mults + connection-matrix entries. | MISMATCH       |
| GAP-PRIMITIVE-B3     | Form = closed-form polynomial OR rational, ALGEBRAIC identity, NOT series.                | Form = composite. Levels 2-3 are closed-form algebraic (4.6) + exponential (1.14)+(4.13). Levels 4-6 are RH-derived rational on cubic surface. | PARTIAL-MATCH  |
| GAP-PRIMITIVE-B4     | Cardinality = 4 separate scalar maps.                                                     | Cardinality = 2 (Level 2) + 2 (Level 3) + 8 (Level 4) + 2 essential (Level 5) + 3 (Level 6).                                       | MISMATCH       |
| GAP-PRIMITIVE-B5     | NOT sector-dependent; single global parameter-chart identity.                              | Levels 2-3: NOT sector-dependent. Level 4: IS sector-dependent (Stokes matrices attach to specific sectors $S_k^{(\infty, 0)}$).   | PARTIAL-MATCH  |
| GAP-PRIMITIVE-B6     | Algebraic constraints: $a_0 + a_1 = 1$ (domain) and null-sum 0 (codomain).                 | Linear constraint (4.6); exponential (1.14)+(4.13); cubic-surface (1.13) on $(x_1, x_2, x_3)$.                                     | MISMATCH       |
| GAP-PRIMITIVE-B7     | Type = ALGEBRAIC chart-translation between two parameter charts of the same P_III equation. | Type = COMPOSITE: parameter-chart algebraic at Levels 2-3, then Riemann–Hilbert / monodromy-data via Levels 4-6.                  | MISMATCH       |

**Aggregate match-matrix (V1 vs. 075 GAP-PRIMITIVES):**

- MATCH:          0 / 7
- PARTIAL-MATCH:  2 / 7  (B3, B5)
- MISMATCH:       5 / 7  (B1, B2, B4, B6, B7)
- UNDETERMINED:   0 / 7

Per the 075 envelope §9 verdict ladder applied to V1 directly,
this would be a STRUCTURAL_MISMATCH verdict at the same primitive
scope. **However, the verdict V1 ≠ B1 is not the operative
question for 086.** The operative question is whether V1 introduces
a NEW B-candidate that bypasses the open KNY ↔ Okamoto chart
gap.

## §D.3 — Reviewer D Symmetry Consistency Check (envelope D.D3)

The envelope §D.D3 asks: does V_quad's Lax pair admit the $D_6$
Weyl group structure expected by P_III($D_6$)? If V1 names this
structure explicitly, record. Do not invent.

**V1 §4 inspection:** V1 §4 does NOT explicitly invoke the $D_6$
affine Weyl group structure in the chart-map derivation. V1's
chart-map at Levels 4-6 is parametrised by the cubic-surface
coordinates $(x_1, x_2, x_3)$ on the monodromy manifold (1.13);
the $D_6$ symmetry classification appears only in V1's title
("P_III($D_6$)") and references [43] (cubic-surface derivation),
not as an operative structure inside V1 §4's chart-map formulae.

**Recorded outcome:** V1 does not name the $D_6$ Weyl group
structure as an operative ingredient of its chart-map. Reviewer
D's Symmetry Consistency Check therefore remains an OPEN W21
LANE-1 question; 086 substrate does not address it.

## §D.4 — V1 reframes the chart-map question (Reviewer A's BS-Q3 sense)

V1's chart-map operates at a **different ambient category** from
B1. B1 (BT 1933 (13 a)) is at the function-space level (periodic
functions across a strip; Fourier / q-series in $z = e^{-x_r}$).
V1 is at the **monodromy-data category**: the chart-map carries
P_III($D_6$) parameters $(\alpha, \beta)$ to a point on the
monodromy manifold (cubic surface (1.13)) via the Lax-pair Stokes-
sector RH problem.

This is an instance of Reviewer A's "BS-Q3" reframing: the
chart-map question itself can be answered in a different category.
B1 (function-space across-strip Fourier) and V1 (monodromy-data
RH-derived) are both valid answers to "what bridges the V_quad
chart to the P_III($D_6$) chart" — but they answer different
**routes** through the Painlevé-III geometry, not the same route.

## §D.5 — Phase D verdict

**Verdict: NEW_CANDIDATE_B4** (V1-derived monodromy-data chart-map
at Jimbo-Miwa convention, complementing rather than replacing the
open KNY ↔ Okamoto Hamiltonian-chart algebraic-translation B1 gap).

Specifically, V1 introduces a **NEW B-candidate (B4)** with the
following profile:

- **B4 source**: $(\alpha, \beta)$ Painlevé-III($D_6$) parameters in
  form (1.1).
- **B4 target**: monodromy-manifold point $(x_1, x_2, x_3) \in
  \mathbb{C}^3$ on cubic surface (1.13), parametrised by 2 essential
  monodromy parameters $(e_1, e_2)$ + exponential constants $(e_0,
  e_\infty)$.
- **B4 assignment rule**: 4-step composition
  $(\alpha, \beta)$ → [(4.6)] → $(\Theta_0, \Theta_\infty)$ →
  [(4.13)] → $(e_0, e_\infty)$ → [(4.27)+(4.28)] → $(e_1, e_2)$ →
  [(1.17)-(1.19)] → $(x_1, x_2, x_3)$.
- **B4 form**: closed-form algebraic at Level 2; exponential at
  Level 3; rational (with $(e_1, e_2)$ as parameters) at Levels
  4-6.
- **B4 sector-dependency**: GLOBAL on parameter space at Levels
  1-3; carries Stokes-sector-dependent data at Levels 4-6.
- **B4 cardinality**: composite (see §D.2 row B4).
- **B4 type**: composite chart-map: parameter-chart $\to$
  Lax-exponents $\to$ exponential constants $\to$ Riemann–Hilbert
  monodromy data $\to$ cubic-surface coordinates.

**Relation to B1**: V1 / B4 does NOT fill the open KNY ↔ Okamoto
Hamiltonian-chart algebraic-translation gap that B1 was attempting
to address. Instead, V1 / B4 **routes around** this gap by carrying
the chart-map onto monodromy-data coordinates directly via
Riemann–Hilbert. The B1 gap remains open at substrate-inventory
scope but is **decoupled** from M6.CC critical-path readiness
(see Phase F).

**Verdict tag (for AEAL-D-1):** `NEW_CANDIDATE_B4`.

## §D.6 — What B4 does NOT determine (residuals to other paths)

B4 (V1-derived monodromy-data chart) does NOT determine:

- The Okamoto 1987 four-tuple $(\alpha_\infty, \alpha_0,
  \beta_\infty, \beta_0)$ Hamiltonian-chart parametrisation — V1
  uses Jimbo-Miwa $(\Theta_0, \Theta_\infty)$ throughout.
- The KNY 2017 $(a_0, a_1, a_2)$ Sakai-classification chart with
  constraint $a_0 + a_1 = 1$ — V1 §4 does not bridge to KNY chart.
- The V_quad CT v1.3 §3.5 four-tuple $(1/6, 0, 0, -1/2)$ null-sum
  $= -1/3$ residual R1 anomaly D2 — V1 does not name this anomaly
  (it is a SIARC-internal 058R artefact).
- The Reviewer D Symmetry Consistency Check ($D_6$ Weyl group
  structure on V_quad Lax pair) — V1 §4 does not invoke this
  symmetry explicitly.

These four residuals are the items that R5 (Okamoto 1987 + KNY
2017 + 058R B.5 cross-walk) would address directly. They are
**not** M6.CC critical-path blockers under the B4 routing (Phase
F).

## §D.7 — Discipline reassertion

075 STRUCTURAL_MISMATCH verdict on B1 is UNCHANGED at 086 scope.
086 does not overturn 075. 086 introduces a NEW route (B4) that
sits alongside the open B1 gap, not in place of it. The W21 LANE-1
arbitration question OQ-W21-LITERATURE-ALTERNATIVE is now
**augmented** (not replaced) by the V1 B4 evidence: synthesizer
arbitrates whether B4 routing suffices for M6.CC pre-fire or
whether path-δ literature acquisition (Jimbo-Miwa 1981 II /
Conte-Musette V5 ch. 7 / Forrester-Witte 2002 / Okamoto 1987
R5) is still required.

End of `075_crosswalk.md`.
