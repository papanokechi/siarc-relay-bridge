# Recommended next phase — T1-BIRKHOFF-PHASE2-LIFT-LOWER

**Phase-1 verdict (this session):** `T1_PHASE1_GAPTYPE_C` under the
Wasow-normalisation reading; literature-derivable bracket
$A \in [d, 2d]$; B4 conjectures $A = 2d$ at the upper bound.

**Phase-2 task (recommended scope only — to be re-prompted as a
separate relay):** lift the literature lower bound from $d$ to $2d$,
i.e. establish the theorem
> For every irreducible non-singular $b \in \mathbb{Q}[x]$ of degree
> $d \ge 3$, $A_{\mathrm{PCF}}(b) = 2d$ rigorously.

---

## Pre-conditions before Phase 2 may be launched

1. **Operator institutional access** to:
   * Birkhoff & Trjitzinsky, Acta Math 60 (1933), 1–89 — directly,
     to verify the precise statement of Theorems 1 and 2 in the
     normalisation B–T use, and confirm whether SIARC's $A$
     corresponds to Wasow's $\sigma$ or Adams's $2\sigma$
     (the **normalisation match** of Q3 §3).
   * Adams, Trans. AMS 30 (1928), 507–541 — directly.
   * Wasow 1965 §X.2–§X.3 — directly.
   * Immink 1984 LNM 1085 §II.3 — directly.
   * Optionally, Braaksma 1991 / 1992 §1 — directly, only if
     Phase-2 P2.1 reveals a fractional-rank degeneracy at any
     SIARC arithmetic locus.
2. **Disposition of the H1 verdict label inconsistency** (D-04):
   the operator should decide whether Theory-Fleet H1's
   `B4_PROVED_AT_d≥3_RESIDUE_AT_d=2` label is to be
   downgraded to `B4_FORMAL_PROVED_AT_d≥3` (or similar) in light
   of the Phase-1 reading; this determines whether Phase 2 is
   labelled as a new proof attempt or as a rigour-grade upgrade
   of an existing claim.

## Decomposition (carried over from Q3 §5)

* **P2.1 (Newton-polygon non-degeneracy).** For every
  irreducible non-singular $b$ with $\deg b = d \ge 3$, the
  Newton polygon of the SIARC three-term recurrence at $\infty$
  has a **single slope** equal to $d$ (Wasow normalisation),
  with no spurious lower-slope vertices. This is a finite
  combinatorial / algebraic-geometric statement; expected
  outcome: provable directly from the SIARC PCF normalisation
  in PCF-2 v1.3 §2.1.

* **P2.2 (formal-exponent extremality / non-resonance).** Among
  the two formal characteristic exponents $\rho_1, \rho_2$ at
  $\infty$, $|\rho_1 - \rho_2|$ contributes to $A$ exactly the
  maximal-slope value, with no resonance cancellation. This is
  the technical core of Phase 2 and may need an arithmetic
  argument on the discriminant axis $\Delta_d(b)$ of PCF-2 v1.3.

* **P2.3 (sectorial uniformity / formal-to-analytic upgrade).**
  Turrittin 1955 + Immink 1984 sectorial-asymptotic existence
  applies uniformly across the SIARC PCF stratum; the SESSION-T2
  $j = 0$ cell finite-$N$ artefact is consistent with this.

## Suggested Phase-2 verdict labels

| Label | Meaning |
|---|---|
| `T1-PHASE2-PROVED-d>=3` | Lower bound lifted to $2d$ rigorously; B4 established at $d \ge 3$. |
| `T1-PHASE2-PROVED-d>=3-MOD-RESONANCE` | Proved away from a finite list of resonance loci; residue cells deferred. |
| `T1-PHASE2-FAILED-NORMALIZATION-MISMATCH` | Primary-source consultation reveals SIARC $A$ corresponds to Adams's $2\sigma$ rather than Wasow's $\sigma$; bracket becomes $[d/2, d]$ and B4 is **outside** the literature bracket. **Major halt.** |
| `T1-PHASE2-FAILED-RESONANCE-DEEPER-THAN-EXPECTED` | P2.2 fails on a positive-measure subset; B4 needs refinement. |
| `T1-PHASE2-PARTIAL-NEEDS-MULTISUMMABILITY` | At certain arithmetic loci the rank-1 Immink upgrade is insufficient; Braaksma multisummability must be invoked. |

## Companion Phase-2 deliverables (recommended)

* `phase2_proof_skeleton.tex` — the full theorem statement and
  proof of the lower-bound lift, in publication-grade LaTeX,
  with citations to the eight-author cohort of Q2.
* `claims.jsonl` ($\ge 25$ AEAL entries) — enriched with the
  derivation provenance of each step in P2.1 + P2.2 + P2.3.
* `dependency_audit.md` — per-citation page/equation references
  to B–T 1933, Adams 1928, Wasow §X.3, Immink LNM 1085 §II.3,
  pinning each step of Phase 2 to a primary-source theorem.
* `verdict.md` — one of the labels above.

## Out-of-scope for Phase 2 (deferred)

* Closed-form expression for the sub-leading $A = 6$ amplitude
  at the equianharmonic $j = 0$ cell — handled by
  `op:j-zero-amplitude-h6` (relay `T2.5d`).
* Modular-discriminant axis stratification — handled by
  `op:b5-b6-d3-strong` (PCF-2 v1.3 §B5/B6, future extensions).
* Channel-theory $V_{\mathrm{quad}}$ resurgence — orthogonal
  (`CHANNEL-CC-MEDIAN-RESURGENCE-EXECUTE`).
* Painlevé classification at $d = 2$ — orthogonal (Theory-Fleet
  H3 follow-up).

## Interaction with the umbrella v2.0 Open Problems list

If Phase 2 succeeds with `T1-PHASE2-PROVED-d>=3`, the umbrella
v2.0 Open Problem `op:b4-degree-d` (Conjecture B4 at all $d$ via
Birkhoff–Trjitzinsky) is **closed at $d \ge 3$** (modulo $d = 2$
which is already PCF-1 v1.3 Theorem 5). The umbrella v2.0 §6
(Open Problems) entry should be re-classified accordingly, with
the residual at $d = 2$ noted as the two-branch sign-split
mechanism (which PCF-1 v1.3 already addresses) and the residual
at all $d \ge 5$ flagged as an empirical-coverage gap (no SIARC
data at $d \ge 5$).

If Phase 2 fails, the umbrella v2.0 Open Problem is amended with
the precise nature of the failure and the failure mode is
reported to Claude for arbitration.
