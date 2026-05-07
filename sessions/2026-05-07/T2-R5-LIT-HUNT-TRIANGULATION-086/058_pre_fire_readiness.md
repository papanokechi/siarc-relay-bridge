# Phase F — 058 Pre-Fire Readiness Verdict

**Session:** 086 T2-R5-LIT-HUNT-TRIANGULATION
**Phase:** F (058 main-fire pre-fire readiness assessment)
**Spec basis:** 058 main-fire spec v1.1, SHA `BE3F8FE9D0857E29..F6E3319`,
  52 197 B (anchored at 058 main fire HEAD `f8099b4`).

Substrate-inventory scope. No 058 main-fire authorisation; that
remains an operator decision after W21 LANE-1 arbitration of
OQ-W21-LITERATURE-ALTERNATIVE.

---

## §F.1 — Decision matrix

The envelope §F.F1 question is:

> "Is $\Phi_{\rm prov}$ sufficient to pre-fire 058 main without R5
>  physical access?"

| Option                       | Description                                                                                                            | Operative blocker? |
|------------------------------|------------------------------------------------------------------------------------------------------------------------|--------------------|
| READY_PROVISIONAL            | $\Phi_{\rm prov}$ + V1 Lax pair + V2 methodology suffice to pre-fire 058 main with $\Phi_{\rm prov}$ in place of Okamoto-Hamiltonian-chart-derived map; R5 retained as final-pass audit anchor only. | NO                 |
| R5_GATED_RESIDUAL_ONLY       | $\Phi_{\rm prov}$ partial; R5 still blocks one or more 058 main-fire spec gates that $\Phi_{\rm prov}$ does NOT cover. | YES (partial)      |
| R5_FULLY_BLOCKING            | $\Phi_{\rm prov}$ insufficient; R5 physical access still gates 058 main fire entirely.                                 | YES (full)         |

## §F.2 — 058 spec-gate cross-walk

The 058 main-fire spec v1.1 enumerates 9 phases (0.0 / 0.5 / A /
B / B.5 / C / D / E / F at L215 / 223 / 233 / 267 / 318 / 388 /
464 / 530 / 552 per 058R `prompt_spec_used.md`) and 8 spec halts
(HALT_M6_LITERATURE_NOT_LANDED + HALT_M6_AFFINE_WEYL_MISMATCH +
HALT_M6_BIRKHOFF_SERIES_DRIFT + HALT_M6_PHASE_B_CONSTRUCTION_INCOMPLETE
+ HALT_M6_NORMALIZATION_INCONSISTENCY + HALT_M6_LITERATURE_DISAGREES_WITH_H4
+ HALT_M6_STOKES_NUMERICAL_MISMATCH + HALT_M6_BIBKEY_COLLISION).

The 086 cross-walk question is which of these spec gates require
R5 (Okamoto 1987) physical access vs. are fillable by V1 + V2 + 058R.

| 058 spec halt                                | Coverage by Φ_prov (V1 + V2 + 058R) | R5 dependency      |
|----------------------------------------------|--------------------------------------|--------------------|
| HALT_M6_LITERATURE_NOT_LANDED                | 086 LANDS V1 + V2; 057 PEND status (058R Phase 0.5 dependency)   | partial            |
| HALT_M6_AFFINE_WEYL_MISMATCH                  | 058R B.5 Sakai-classification cross-walk substrate; V1 §4 D_6 named in title | LOW (audit)        |
| HALT_M6_BIRKHOFF_SERIES_DRIFT                | V1 §4.1 (4.7)+(4.8) gives formal-solution Birkhoff factorisation   | LOW                |
| HALT_M6_PHASE_B_CONSTRUCTION_INCOMPLETE      | Φ_prov §E.2 6-stage composition; Φ_symp Jacobian deferred to Phase D.2 | LOW (audit)        |
| HALT_M6_NORMALIZATION_INCONSISTENCY          | Φ_prov §E.6 discipline reassertion: composition is internally consistent on V_quad chart | LOW                |
| HALT_M6_LITERATURE_DISAGREES_WITH_H4         | V1 + V2 do NOT explicitly invoke H4 / D_6 Weyl group; Reviewer D symmetry consistency check open | MEDIUM (W21)       |
| HALT_M6_STOKES_NUMERICAL_MISMATCH            | Numerical residual deferred to Phase D.2 (058R B.3 sub-tasks)     | LOW (numerical computation) |
| HALT_M6_BIBKEY_COLLISION                     | 058R 0.5 bibkey-preflight already PASS; 086 adds 2 new bibkeys to manifest (BLMP24 + ILP18) | LOW                |

## §F.3 — Verdict

**Verdict: READY_PROVISIONAL with R5_RESIDUAL_ONLY caveat**.

Specifically:

- $\Phi_{\rm prov}$ + V1 Lax pair + V2 methodology cover 7 of 8
  spec halts at LOW R5 dependency (substrate-inventory level).
- HALT_M6_LITERATURE_DISAGREES_WITH_H4 carries MEDIUM R5
  dependency: V1 / V2 do NOT explicitly invoke the $D_6$ affine
  Weyl group structure expected by H4 (Reviewer D's pre-W21-synth
  Symmetry Consistency Check). This is a W21 LANE-1 arbitration
  question, not an R5-blocking gate per se.
- HALT_M6_LITERATURE_NOT_LANDED: 057 (CC-VQUAD-PIII literature
  pre-flight) PENDING status remains a 058R Phase 0.5 dependency;
  086 partially fills 057's substrate (V1 + V2 added to literature
  manifest) but does not formally LAND 057. This is a pre-existing
  058R blocker, not a 086-introduced one.
- R5 (Okamoto 1987) physical access remains a useful **audit-
  anchor** for items (1)-(4) in §E.5 §F.4 below; downgraded from
  M6.CC critical-path blocker to final-pass cross-check.

The 058 main-fire authorisation decision is **not** delegated to
086; it remains an operator + W21 LANE-1 (T1 Synth) decision.
086's role is to provide the substrate that makes the decision
informed.

## §F.4 — R5 audit-anchor residual

Per §E.5 of `provisional_normalization_map.md`, the R5-residual
items (after $\Phi_{\rm prov}$ landing) are:

1. Okamoto Hamiltonian-chart numerical normalisation (Sakai-Okamoto
   convention dictionary).
2. V_quad CT v1.3 §3.5 four-tuple null-sum anomaly D2 (`-1/3 ≠ 0`).
3. $D_6$ Weyl group symmetry structure on V_quad Lax pair (Reviewer
   D's Symmetry Consistency Check).
4. $\Phi_{\rm symp}$ Jacobian determinant + numerical $(e_1, e_2)$
   values at V_quad parameter point (Phase D.2 numerical task).
5. Schlesinger transformation explicit formulae at V_quad
   parameter point.

R5 (Okamoto 1987) covers (1) directly; (2) and (3) require R5
PLUS Sakai 2001 + KNY 2017 §8.5 cross-reference; (4) is a
numerical computation task requiring V1 (4.1)+(4.2) + V2 §4.1 +
mpmath; (5) is an algebraic specialisation of V1 §6 / Gromak
Bäcklund (1.2).

None of (1)-(5) blocks 058 main pre-fire under the
$\Phi_{\rm prov}$ B4-routing. Each is a final-pass cross-check
that, if fails, would surface as a discrepancy_log entry post-058
fire — not as a 058 pre-fire halt.

## §F.5 — Recommended dispatch sequence (operator + W21 LANE-1)

The following recommended sequence does NOT bind operator
decision; it is the agent's reading of the most efficient
substrate-utilisation order:

1. **Land 057** (CC-VQUAD-PIII literature pre-flight): currently
   PENDING; 058R Phase 0.5 dependency. 086 partially fills the
   substrate by adding V1 + V2 to the literature manifest.
2. **W21 LANE-1 arbitrate OQ-W21-LITERATURE-ALTERNATIVE** with
   086 substrate available: synthesizer chooses among
   (a) accept B4 routing as M6.CC pre-fire substrate,
   (b) require additional path-δ acquisition (Conte-Musette V5
   ch. 7 / Forrester-Witte 2002 / Jimbo-Miwa 1981 II) before
   058 main re-fire, or
   (c) require R5 (Okamoto 1987) physical access before 058 main
   re-fire.
3. **058 main re-fire** under chosen routing; if (a) → fire
   immediately under $\Phi_{\rm prov}$ + V1 + V2 substrate;
   if (b) or (c) → fire after additional acquisition lands.

## §F.6 — Discipline reassertion

086 does NOT authorise 058 main re-fire. 086 documents the
$\Phi_{\rm prov}$ provisional map, cross-walks it against the 058
spec-gate set, and surfaces the R5 audit-anchor residual. Operator
+ W21 LANE-1 own the dispatch decision.

End of `058_pre_fire_readiness.md`.
