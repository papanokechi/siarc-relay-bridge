# Cross-Bundle Compatibility [COMPATIBILITY-E1..E4] — 077

**Session:** T2-PORTFOLIO-BUNDLING-DOSSIER-ASSEMBLY-077
**Compiled:** 2026-05-07
**Scope:** Phase E enumeration of mutually-compatible / conflicting
bundle pairings, three-bundle stacks, and standalone-preserving
paths per spec §5. Per HALT_077_BUNDLE_SELECTION_OVERREACH, no
pairing is recommended. Each entry is an inventory tag.

---

## E.1 — Mutually compatible bundle pairs

A pair (Bi, Bj) is MUTUALLY COMPATIBLE when no record appears in
both Bi's and Bj's composition. Per the C.8 coverage table, the
boolean overlap matrix is:

| pair | shared records | MUTUALLY COMPATIBLE? |
|---|---|---|
| B1 + B2 | none (B1 = P1+P2+P5; B2 = P3+P4) | YES |
| B1 + B3 | P2 + P5 | NO (E.2 conflict) |
| B1 + B4 | P1 + P2 + P5 | NO (E.2 conflict) |
| B1 + B5 | P1 + P2 + P5 (all of B1 also in B5) | NO (set containment; E.2 conflict) |
| B2 + B3 | none (B2 = P3+P4; B3 = P2+P5) | YES |
| B2 + B4 | P3 + P4 | NO (E.2 conflict) |
| B2 + B5 | P3 + P4 (all of B2 also in B5) | NO (set containment; E.2 conflict) |
| B3 + B4 | P2 + P5 | NO (E.2 conflict) |
| B3 + B5 | P2 + P5 (all of B3 also in B5) | NO (set containment; E.2 conflict) |
| B4 + B5 | all 6 | NO (set containment; E.2 conflict) |

**[COMPATIBILITY-E1-RESULT] Two MUTUALLY COMPATIBLE pairs:**

- **B1 + B2** covers P1 + P2 + P3 + P4 + P5 = 5 of 6 records;
  umbrella v2.0 (P6) is the residual standalone (or absorbed
  into one of the bundle introductions per HALT_077 deprecation
  rule — see E.4).
- **B2 + B3** covers P2 + P3 + P4 + P5 = 4 of 6 records;
  PCF-1 v1.3 (P1) and umbrella v2.0 (P6) are the residual
  standalones.

[COMPATIBILITY-E1-NOTE] B1 + B2 is the spec §5.E.1 example pairing
("B1 + B2 covers PCF-1 + PCF-2 + T2B + CT v1.4 + D2-NOTE v2.1 = 5
records; umbrella v2.0 stays standalone or absorbs"). Inventory
confirms.

---

## E.2 — Conflicting bundle pairs

A pair (Bi, Bj) CONFLICTS when the bundles share at least one
record (the shared record cannot be in two distinct submissions
simultaneously without explicit deprecation of one).

| pair | shared records | conflict resolution scope |
|---|---|---|
| B1 + B3 | P2 + P5 | tie-break: B1 absorbs P2 + P5, OR B3 absorbs P2 + P5; cannot both. Operator/synth scope per HALT_077_BUNDLE_SELECTION_OVERREACH. |
| B1 + B4 | P1 + P2 + P5 | B4 contains B1 ∪ {P3, P4, P6}; choosing both means B1's content appears in both monograph (B4) and standalone-bundle (B1). Operator/synth scope. |
| B2 + B4 | P3 + P4 | B4 contains B2 ∪ {P1, P2, P5, P6}; same containment-conflict pattern as B1+B4. |
| B3 + B4 | P2 + P5 | B4 contains B3 ∪ {P1, P3, P4, P6}; same containment-conflict pattern. |
| B1/B2/B3/B4 + B5 | depends | B5 = "each paper to its own venue" claims every record as a standalone; any non-empty bundle Bi's records by definition conflict with B5's per-record dispatch claim. |

[COMPATIBILITY-E2-NOTE] Spec §5.E.2 example pairing "B1 + B3 both
claim PCF-2 v1.3; pick one" inventory-confirmed. Tie-break is
operator/synth scope per spec §7 "NOT pick a bundle on synth's
behalf".

---

## E.3 — Three-bundle stacks

[COMPATIBILITY-E3-NOTE] Spec §5.E.3 enumerates two example
3-bundle stacks: (a) B1 + B2 + (umbrella standalone) full
coverage in 3 papers; (b) B3 + (PCF-1 standalone) + B2.
Inventory confirms and extends:

### (a) B1 + B2 + umbrella-standalone
- Coverage: P1 + P2 + P5 (B1) + P3 + P4 (B2) + P6 standalone = 6/6 records covered, 3 distinct submission artefacts
- Shared records: none across B1, B2; P6 standalone is independent
- Workflow-lift aggregate: B1 MEDIUM + B2 LOW-to-MEDIUM + P6 status quo LOW = MEDIUM aggregate
- Endorsement-category aggregate: math.NT (B1) + math-ph (B2) + math.HO (P6) = 3 distinct categories; per cross-listing rule each can be endorsed independently
- Time-to-submission: paced by latest GATED-ON-X (B2's G17-close per §4.D.7)

### (b) B3 + PCF-1-standalone + B2
- Coverage: P2 + P5 (B3) + P1 standalone (P1 of B5) + P3 + P4 (B2) = 5/6 records; P6 (umbrella) NOT covered
- Spec §5.E.3 note: "loses PCF-1 ↔ PCF-2 bundling synergy" (PCF-2 cites PCF-1 as parent paper per `paper_profile_pcf2_v13.md` §B.3)
- Workflow-lift aggregate: B3 LOW + P1 LOW (status quo for P1) + B2 LOW-to-MEDIUM = LOW aggregate; lower than (a)
- Endorsement-category aggregate: math.NT (B3 + P1) + math-ph (B2) = 2 distinct categories; lower than (a)

### (c) B1 + B2 + (P6 absorbed into B1 or B2 introduction)
- Coverage: P1 + P2 + P3 + P4 + P5 (5 of 6 in 2 bundles); P6's program-statement content absorbed
- Per HALT_077_DEPRECATION_PROPOSED, agent does NOT propose deprecating umbrella v2.0; operator/synth scope to decide whether to absorb-vs-cite
- Note: this option blurs into 2-bundle case if P6 is fully absorbed; surfaced for inventory completeness

### Diminishing-returns observation per spec §5.E.3
- Stacks beyond (a) and (b) (e.g., B3 + B2 + P1 + P6 = 4 separate submission artefacts) progressively distribute records across more submissions, increasing aggregate workflow-lift and endorsement-category count without adding coverage. Operator/synth scope to weigh.

---

## E.4 — Standalone-preserving paths

[COMPATIBILITY-E4-NOTE] Spec §5.E.4 asks which records are
"strong enough standalone per the 2026-05-07 impact assessment
to NOT need bundling". Per `portfolio_substrate_anchor_shas.md`
§A.5 NOTE-077-SHA-5, the 2026-05-07 impact assessment is
ORAL-OR-TRANSCRIPT-ONLY for 077 (not on disk). Inventory below
derives standalone-strength tags from on-disk evidence in the
6 paper profiles + the 2026-05-04 portfolio inventory only.

Standalone-strength tag per record (substrate-anchored):

| Record | Theorem-evidence strength | Endorsement-fit (Tier 1) | Page-count standalone-fit | Standalone-strength tag (077-internal) |
|---|---|---|---|---|
| P1 PCF-1 v1.3 | 1 proven theorem (Δ>0 closed form) + 4-part Conjecture A v5 (TIER-2 EMPIRICAL on 30 families) | 3H | ~16 pp fits standard math.NT venues | MEDIUM (theorem present; conjectures dominant) |
| P2 PCF-2 v1.3 | program-statement (no proven theorems internal); 110/110 d∈{3,4} verified; explicit "not a results paper" abstract | 3H | ~22 pp | PROGRAM-STATEMENT-STANDALONE (depends on whether venue accepts program-statement format) |
| P3 CT v1.3 | 1 proven theorem (V_quad CC-channel recovery, modulo Borel-Laplace) + 1 proposition (ξ_0 d=2) + 3 conjectures | 3H | ~17 pp | MEDIUM-to-HIGH (1 theorem + clear central object) |
| P4 D2-NOTE v2.1 | 1 proven theorem (cross-degree universality at d=2) + 1 verified (d=4) + 18/18 sweep at d∈{2..10}; closed citation chain v2.1 | 0 templates on disk + Tier-1 fit inferred from CT row | HIGH (≥ 9 pp short note format; closed proof at d=2; 50-dps Phase A* sweep verifies) |
| P5 T2B v3.0 | 3 proven theorems (Resonance family; Class A; Class B Stieltjes equivalence) + Completeness Conjecture + 134,040-candidate desert sweep at k=3 | 2H + 1M | ~8 pp | HIGH (3 theorems proven; large empirical base) |
| P6 umbrella v2.0 | 0 proven theorems internal (program-statement); 9 problems; 2 conjectures forwarded | 3M | ~12 pp | PROGRAM-STATEMENT-STANDALONE (frame artefact; absorbs companions by Zenodo cite) |

**[COMPATIBILITY-E4-RESULT]** Substrate-anchored standalone-strength
ranking by theorem-count + endorsement-fit:

- HIGH: D2-NOTE v2.1 (1 proven theorem + 18/18 verification + closed citation chain); T2B v3.0 (3 proven theorems + 134,040-candidate desert)
- MEDIUM-to-HIGH: CT v1.3 (1 proven theorem + central object)
- MEDIUM: PCF-1 v1.3 (1 proven theorem + 4-part conjecture leading)
- PROGRAM-STATEMENT-STANDALONE: PCF-2 v1.3 + umbrella v2.0 (frame artefacts)

[NOTE-077-E-1] Spec §5.E.4 anticipates "PCF-2 v1.3 + D2-NOTE v2.1
both Tier-1 standalone-strong" per 2026-05-07 oral-transcript
impact assessment. On-disk substrate places D2-NOTE v2.1 at
HIGH (3 named-theorem-class deliverables + closed citation
chain v2.1) and PCF-2 v1.3 at PROGRAM-STATEMENT-STANDALONE
(no proven theorems internal; 4 program-statement conjectures
+ 1 falsified conjecture B4'). Discrepancy with spec §5.E.4
oral-anchor surfaced D-077-5; not a halt because spec
acknowledges "expected: PCF-2 v1.3 + D2-NOTE v2.1 both
Tier-1 standalone-strong" is itself a 2026-05-07 expected-answer
example, not a substrate-anchored claim.

[NOTE-077-E-2] Standalone-strength tags above are inventory
labels for synth consumption, not portfolio-architecture
verdicts. Per HALT_077_BUNDLE_SELECTION_OVERREACH, the
agent does not assert that any record SHOULD remain
standalone vs. SHOULD be bundled. Synth scope.

---

End of cross-bundle compatibility surface.
