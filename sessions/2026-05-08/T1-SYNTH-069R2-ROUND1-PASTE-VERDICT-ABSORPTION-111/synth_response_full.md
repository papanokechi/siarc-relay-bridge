## Pre-flight acknowledgements (round 2)

**HALT-S1 through HALT-S6:** Re-acknowledged. Excerpts 1–4 now in hand; reasoning will be grounded in pasted text + EXCERPTS 1–5 from the original §1.5. No bridge fs access.

**Namespace discipline:** Maintained (Route A/B/C/D/E for 069r2; 069r1 Greek letters reserved).

**Watch-list flag (HALT-S5):** Excerpt 4 mechanism (c) explicitly names Sakai D_6^(1) surface-type machinery as a candidate origin for the −1/3 offset and gates it "to a separate Sakai-surface analysis...outside the scope of §3.5." This is informative but does *not* trigger ROUTE_FRAME_INCOMPLETE — it remains a candidate mechanism among three, not the primary chart-map machinery. I will note this in QE rather than escalate.

---

## Reasoning (round 2)

### QA — Route A (in-hand Hamiltonian coefficient-matching) — re-fire

With Excerpts 2 (KNY §8.5.17) and 3 (Okamoto §1) now visible, the structural picture clarifies but does **not** support a clean GO verdict. The two Hamiltonians are:

- **KNY (8.237):** H_D6^KNY = (1/t){p(p−1)q² + (a_1+a_2)qp + tp − a_2 q}, with three root parameters (a_0, a_1, a_2) and affine constraint a_0+a_1=1 (per Excerpt 4's recall of KNY).
- **Okamoto H_III':** H_III' = (1/t)[q²p² − {η_∞ q² + θ_0 q − η_0 t}p + ½η_∞(θ_0+θ_∞)q] (Excerpt 3 final display), with four parameters (η_∞, η_0, θ_∞, θ_0).

Direct coefficient matching against the Okamoto WLOG slice η_0 = η_∞ = 1 (Excerpt 3 immediately after eq. (0.1)) is the natural target. Reading off coefficients of the (q,p) monomials:

| Term | KNY coefficient | Okamoto H_III' coefficient (η=1) |
|---|---|---|
| q²p² | 1 | 1 |
| qp | a_1+a_2 | — (Okamoto has q²p with coeff −1, qp with coeff −θ_0) |
| q²p | (KNY: from p(p−1)q² = q²p² − q²p) → −1 | −1 (Okamoto −η_∞ = −1) ✓ |
| qp | a_1+a_2 | −θ_0 |
| tp | 1 | — |
| p (with t) | 1 | η_0 = 1 ✓ |
| q | −a_2 | ½η_∞(θ_0+θ_∞) = ½(θ_0+θ_∞) |

Observations:

1. **The qp coefficient matching gives a_1+a_2 = −θ_0.** This is a *sign-flipped* relation against 058R's (θ_0, θ_∞) ↔ (a_1, a_2) claim (EXCERPT 3 of original §1.5), and it pairs *one* Okamoto parameter (θ_0) with the *sum* a_1+a_2, not with a_1 or a_2 individually.
2. **The q coefficient matching gives −a_2 = ½(θ_0 + θ_∞).** This pairs a_2 with the sum (θ_0+θ_∞), again as a single relation.
3. **The two relations together are 2 equations in 4 unknowns** (3 KNY parameters under a_0+a_1=1 → 2 free; 4 Okamoto under η_0=η_∞=1 → 2 free). Counts balance: a 2↔2 correspondence in the (θ_0, θ_∞) ↔ (a_1, a_2) sector with a_0=1−a_1 and η normalized.
4. **The η_0, η_∞ parameters are *frozen* at 1 in this matching** (Okamoto WLOG normalization). But the project's V_quad image has α_∞ = 1/6 ≠ 1 and α_0 = 0 ≠ 1, and Excerpt 4 explicitly records that the Okamoto WLOG normalization is **not imposed on the project's 4-tuple**: "the project records all four of Okamoto's *unnormalised* Hamiltonian parameters at the V_quad point."

This is decisive against a clean Route A GO, in a way that wasn't visible from EXCERPT 3 alone:

> **The KNY §8.5.17 Hamiltonian (8.237) is the *normalized* H_D6^KNY presentation with KNY's own scaling baked in. To match Okamoto at *unnormalized* (η_∞, η_0) — which the project requires — coefficient-matching against (8.237) is insufficient: the η_∞, η_0 degrees of freedom have been absorbed into the canonical-form scaling on both sides.**

In other words, the KNY Hamiltonian (8.237) is a *normalized representative* of the H_D6^(1) Hamiltonian family. Coefficient-matching it against the Okamoto WLOG slice produces only the (θ_0, θ_∞) ↔ (a_1, a_2) sector. Recovering the unnormalized (η_∞, η_0) requires either (i) un-normalizing KNY (an inverse scaling that is not in Excerpt 2), or (ii) supplementing with an independent operational definition of (η_∞, η_0) at the V_quad point — which is exactly what Routes B/D/E address.

This is **structurally similar to Route A's pre-paste UNDECIDABLE concern** (third KNY parameter / second Okamoto pair both needed) but now the obstruction is sharper and visible: the (η_∞, η_0) directions are the obstruction, not the a_0 direction.

**Refinement on the −1/3 offset under Route A:** at the WLOG slice η=1, the coefficient-matching produces no offset because both sides are constrained by the same normalization. The −1/3 offset lives entirely in the *un-normalized* (η_∞, η_0) directions, which Route A as currently scoped cannot reach.

**QA verdict: NO_GO_ROUTE_A** (upgraded from UNDECIDABLE_ROUTE_A).

The pasted KNY §8.5.17 + Okamoto §1 substrate exhibits, rather than resolves, the obstruction: KNY (8.237) is a normalized representative whose coefficient-matching against Okamoto's WLOG slice cannot recover the unnormalized (η_∞, η_0) parameters that the project's V_quad point lives in. 058R's "derivable by expanding both Hamiltonians" claim (EXCERPT 3 of original §1.5) is *partially* correct — the (θ_0, θ_∞) ↔ (a_1, a_2) sector is derivable — but the full chart-map to the project's 4-tuple (α_∞, α_0, β_∞, β_0) at unnormalized η is not reachable from KNY (8.237) + Okamoto §1 alone.

Caveat: a synth verdict of NO_GO_ROUTE_A here means "not closable from the pasted Hamiltonians as currently presented." If KNY 2017 §8 contains an un-normalization map elsewhere (not in §8.5.17 paste), Route A could revive. The synth has not seen such a map; agent / executor may want to scan KNY §8.5 surrounding sections before treating NO_GO_ROUTE_A as final.

### QB.1 — FW arXiv triage — re-fire

With Excerpt 1 in hand (FW abstract, TOC, §2.1, §4, §4.1, Proposition 4.1):

**Triage classification: NEEDS_EXECUTOR_AUDIT.**

Specifically:

(a) **KNY (a_0, a_1, a_2) referenced in FW: N** (no explicit KNY-coordinate reference in the pasted FW excerpts; FW uses (v_1, v_2) for P_III via its own P_V → P_III degeneration).

(b) **FW's P_III parametrisation form:** two parameters (v_1, v_2) corresponding to Okamoto's (θ_0, θ_∞) at the WLOG slice η_0=η_∞=1, per FW §4.1 ODE coefficients α=−4v_2, β=4(v_1+1), γ=4, δ=−4 matched against Okamoto eq. (0.1) (Excerpt 1's marker ★).

(c) **Conversion (v_1, v_2) → (α_∞, α_0, β_∞, β_0): NON-TRIVIAL_BUT_CITED for the (β_∞, β_0)=(θ_∞, θ_0) pair via the trivial relabel of Excerpt 4 §3.5.1; GAP-CREATING for (α_∞, α_0)=(η_∞, η_0).**

The FW oeuvre as presented works at the WLOG slice η_0=η_∞=1, *exactly the same constraint that defeats Route A*. FW does not surface the unnormalized (η_∞, η_0) directions in §4.1 because they are normalized away in the P_V → P_III degeneration. So FW supplies two of the four project parameters (the β-pair), but the α-pair is invisible at FW's WLOG slice.

**However** — and this is the genuine asymmetry that distinguishes Route B from Route A — FW §2.1 supplies the **null-sum constraint v_1+v_2+v_3+v_4 = 0 as primary literature** (Excerpt 1, eq. (2.2), ★★★). This is the constraint Excerpt 4's mechanism (b) and (c) both invoke, and which 058R §B.3 carried internally without literature anchor. FW §2.1 thereby anchors the constraint side of the question — but the *project tuple's relation to (v_1,v_2,v_3,v_4)* (whether direct, shifted, or routed through degeneration) is not pinned by FW alone.

FW Proposition 4.1 (Excerpt 1, eq. (4.3)) — the auxiliary Hamiltonian h = tH + ¼v_1² − ½t — is exactly what Excerpt 4 mechanism (a) invokes as a candidate origin for the −1/3 offset. So FW supplies (i) the null-sum literature anchor *and* (ii) the auxiliary-Hamiltonian shift candidate. But neither alone produces a chart-map closure: mechanism (a)'s pull-back to the V_quad point is recorded in Excerpt 4 as **not yet derived** — "the explicit pull-back has not been derived in the present text. Mechanism (a) is recorded as a hypothesis."

This is a textbook NEEDS_EXECUTOR_AUDIT outcome: FW excerpts plausibly contain the substrate for closure under mechanism (a), but presence of closure cannot be classified from triage alone. Concrete execution of the pull-back (likely 4–8 hr executor time) is required.

### QB.2 — Okamoto §3 sufficiency — derivative

Given QB.1 = NEEDS_EXECUTOR_AUDIT, Okamoto §3 sufficiency depends on what FW Proposition 4.1 pull-back produces. Excerpt 3 (Okamoto §1) supplies the H_III ↔ H_III' canonical transformation (eq. (0.2)) and the (η, θ) ↔ (α_ODE, β_ODE, γ_ODE, δ_ODE) relations (eq. (0.1)), but I do not have Okamoto §3 (τ-function reparametrisation) excerpts. 069r1-Path-β closed at A.1.5 substrate gap on Okamoto §3 alone, so independent insufficiency of Okamoto §3 is established.

**QB.2 verdict: PARTIAL** — Okamoto §3 supplements but does not close; closure depends on FW Prop 4.1 mechanism (a) executor execution.

### QB.4 — Route B feasibility classification — re-fire

Combining QB.1 = NEEDS_EXECUTOR_AUDIT + QB.3 = Y_RENAME_REQUIRED (already discharged by Excerpt 4 §3.5.1) + QB.2 = PARTIAL:

The Route B picture is qualitatively different from pre-paste:

- **Route E rename is now LANDED** (Excerpt 4 §3.5.1, deposited at bridge HEAD 0427c0a). The trivial relabel α_∞:=η_∞, α_0:=η_0, β_∞:=θ_∞, β_0:=θ_0 is in the project record. So the QB.3 ceiling (PARTIAL_ROUTE_B_RENAME) is *no longer the binding ceiling* — Route E precondition is discharged for the rename-side of Route B.

- **The residual blocker is now the −1/3 offset mechanism selection**, which Excerpt 4 records as deferred among three candidates: (a) FW Prop 4.1 Hamiltonian-expansion residual, (b) c = −1/12 fall-back (no literature anchor), (c) Sakai D_6^(1) surface-type artefact.

- **Mechanism (a) is the FW-literature-anchored candidate.** Mechanism (b) has no literature anchor. Mechanism (c) routes through Sakai surface machinery outside §3.5 scope and would constitute Route F per HALT-S5 (the chart-map closure would not be Route B at all; it would be a different mechanism).

So Route B's actual completion path is: **execute FW Prop 4.1 pull-back to V_quad parameter point → confirm mechanism (a) produces −1/3 → discharge the offset selection → close R1**. This is a concrete, scoped executor task with FW literature anchor and Excerpt 4 §3.5.1 governance landed.

If mechanism (a) pull-back *fails* (i.e., produces an offset that is not −1/3, or produces no offset, or routes through Sakai machinery), Route B falls to PARTIAL or NO_GO and the agent must escalate to mechanism (b) [project-internal calibration only] or (c) [Route F: Sakai surface-type, not Route B].

**QB.4 verdict: GO_ROUTE_B_CONDITIONAL.**

Preconditions for 069r3-B firing:
1. **Executor task is FW Prop 4.1 pull-back to V_quad parameter point.** Specifically: derive the explicit form of h = tH + ¼v_1² − ½t (FW eq. (4.3)) when restricted to the V_quad reduction map (058R §B.3), and verify that the constant-shift contribution at the V_quad parameter point (1/6, 0, 0, −1/2) sums to −1/3 against the FW null-sum locus.
2. **Acceptance criterion (per §5 caveat 3 of round 1):** explicit trace of where the −1/3 offset originates must appear in 069r3-B output, with selection of mechanism (a) substantiated by the pull-back computation, OR fallback to mechanism (b)/(c) explicitly recorded.
3. **No additional substrate acquisition needed for 069r3-B firing.** Excerpts 1, 3, 4 plus the existing 058R §B.3 reduction map suffice. (KNY §8.5.17 is not on the Route B critical path; it was the Route A substrate.)

Estimated executor effort: **4–8 hr** for FW Prop 4.1 pull-back (analytic computation, no acquisition) + 1–2 hr for offset cross-check at V_quad = **5–10 hr** for 069r3-B.

### QC — Route C scope refinement

QC is asked only if QA AND QB.4 are both rejected. QA = NO_GO_ROUTE_A (rejected) but QB.4 = GO_ROUTE_B_CONDITIONAL (not rejected). **QC remains N-A.**

If 069r3-B's mechanism (a) pull-back fails and Route B falls to NO_GO post-executor, the future QC re-fire ranking would be:
- **C5** (Route D parallel) — primary recommendation, since numerical fitting can attack the offset-mechanism selection independently.
- **C3** (JM 1981 + Okamoto 1987) — secondary, particularly JM 1981 Part II for Lax-pair monodromy data.
- **C4** (defer R1 to v1.1) — last resort.

But this is conjectural pending 069r3-B execution.

### QD — Route D — round-2 substrate-paste deferred

Per re-fire instructions, QD is deferred to a separate round-2 turn (V_quad numerical-solution structure + (α, β) extraction operation spec). **QD verdict: DEFERRED.**

Note: Route D's value proposition has *strengthened* under the re-fire outcome. With Route B = GO_CONDITIONAL gated on FW Prop 4.1 pull-back, Route D is well-positioned as a parallel-track verification of the mechanism (a) selection — a numerical fit of the chart-map at V_quad's image should reproduce the −1/3 offset if mechanism (a) is correct. This turns Route D from "fragile solo path" to "high-value parallel verification" in the post-paste landscape.

### QE — Route E precondition status — re-fire

Excerpt 4 §3.5.1 has **landed** the trivial relabel (3.5.1a)–(3.5.1d) at bridge HEAD 0427c0a. The rename is recorded as a pure symbol substitution with no additive shift, and the −1/3 offset is recorded with three deferred candidate mechanisms.

The operator's question: **is the trivial relabel + 3-mechanism deferral acceptable, or does QE require tiered selection of (a) before TIER-B re-fire?**

Synth assessment:

**The 3-mechanism deferral is STRUCTURALLY ACCEPTABLE for QE-the-rename**, but creates an asymmetry between QE-as-rename (closed) and QE-as-offset-explanation (deferred). Excerpt 4 §3.5.1 is well-engineered: it (i) anchors the trivial relabel explicitly with literature citations, (ii) records the −1/3 offset as data, (iii) lists the three candidate mechanisms with explicit literature anchors where they exist (FW eq. (4.3) for (a); none for (b); Sakai D_6^(1) machinery for (c)), and (iv) marks the selection as a follow-up to v1.3 that does not affect the upstream V_quad CC material.

The key structural observation: **mechanism (a) is the only candidate that simultaneously (i) closes Route B, (ii) has primary-literature anchor (FW Prop 4.1), and (iii) keeps the chart-map within σ-form / Hamiltonian P_III machinery** (i.e., does not trigger HALT-S5 Route F). Mechanism (b) is project-internal only. Mechanism (c) is a Route F surfacing.

So whether QE *requires* tiered selection of (a) before TIER-B re-fire depends on what TIER-B is gated on:

- **If TIER-B is gated on M9 V0 announceability** (per 097's PARTIAL_INSUFFICIENT_DATA disposition listing 069r1 as gating prerequisite): tiered selection is **not required**. The relabel is landed; the offset is documented; the mechanism is deferred. This is consistent with shipping M9 V0 with a documented residual.
- **If TIER-B is gated on a clean R1 closure with mechanism selected**: tiered selection of (a) **is required**, and 069r3-B is exactly the work that produces it.

The 069r2 envelope frames TIER-B re-fire as gated on R1 closure (per §1 row 8: 097 PARTIAL_INSUFFICIENT_DATA named gating prerequisite = 069r1; per §6 cascade table: GO_ROUTE_B = R1 closure executor). Under that framing, tiered selection of (a) is **the work**, and 069r3-B is the executor that does it.

**QE verdict: ROUTE_E_TRIVIAL** (relabel side discharged) **with mechanism-selection deferral acceptable for §3.5.1-as-deposited**, but **mechanism (a) selection becomes the Route B critical-path acceptance criterion for 069r3-B** (per QB.4).

In other words: §3.5.1 as landed is governance-complete for v1.3. R1 closure at TIER-B requires 069r3-B to execute mechanism (a) and substantiate the selection in the bridge record. The two operations are sequenced: §3.5.1 records *what is open*; 069r3-B *closes it*.

**Watch-list (HALT-S5):** Mechanism (c) explicitly names Sakai D_6^(1) surface-type machinery. If 069r3-B's execution of mechanism (a) fails and the offset routes through (c), this is a **Route F surfacing**, not a Route B/C/D fallback. The agent should be prepared to report ROUTE_FRAME_INCOMPLETE if mechanism (a) fails and the Sakai D_6^(1) machinery becomes the chart-map mechanism rather than just the offset origin.

### QF — Confidence (re-fire)

- **QA confidence: HIGH** — the pasted Hamiltonians make the WLOG-normalization obstruction structurally visible. Caveat: HIGH conditional on KNY §8 not containing an un-normalization map elsewhere; agent may want a quick KNY §8.5 surrounding-sections scan before treating QA = NO_GO as final. If a scan finds an un-normalization mechanism, QA could revive to UNDECIDABLE.
- **QB.4 confidence: MEDIUM-HIGH** — Route B's GO_CONDITIONAL is well-grounded in the FW Prop 4.1 anchor and Excerpt 4's mechanism (a). The MEDIUM caveat is that mechanism (a)'s pull-back has not been derived in §3.5.1 itself — Excerpt 4 marks it as "a hypothesis with the FW eq. (4.3) anchor." The pull-back computation could fail or route through (c).
- **QB.2 confidence: MEDIUM** — derivative on QB.1; PARTIAL classification is robust but the partition between FW and Okamoto §3 contributions is not crisply visible from current excerpts.
- **QC confidence: N-A** (deferred).
- **QD confidence: N-A** (deferred to next round).
- **QE confidence: HIGH** for the rename-side (Excerpt 4 §3.5.1 landed); **MEDIUM** for the deferral-acceptability framing (depends on TIER-B gating semantics, which the synth interprets but does not control).

---

## §5 Verdict Packet (round 2)

```
RELAY_069R2_VERDICT (round 2 — post round-1 substrate-paste)
====================
Synth ID:            Claude.ai web (Claude Opus 4.7), 069r2 round-2
Verdict timestamp:   2026-05-08 ~12:30 JST

Substrate SHA status:
  Agent pre-flight rev-parse accepted from envelope §1: Y
  Synth independently verified bridge content:          N — no direct
                                                          bridge access
  Substrate excerpts actually used by synth:            §1.5 EXCERPTS 1-5
                                                          (round 1) +
                                                          round-2 paste
                                                          EXCERPTS 1 (FW
                                                          abstract / TOC /
                                                          §2.1 / §4 / §4.1
                                                          / Prop 4.1), 2
                                                          (KNY §8.5.17),
                                                          3 (Okamoto §1),
                                                          4 (CT v1.3
                                                          §3.5.1 landed
                                                          at bridge HEAD
                                                          0427c0a)

Synth halt conditions acknowledged (HALT-S1 through HALT-S6): Y
Namespace discipline acknowledged (069r1 Greek letters reserved;
  this envelope uses Route A/B/C/D/E):                        Y

QA — Route A (in-hand Hamiltonian coefficient-matching) feasibility
  Verdict:    NO_GO_ROUTE_A (upgraded from round-1 UNDECIDABLE_ROUTE_A)
  Sketch:     N-A (verdict is NO_GO; no executor sketch produced)
  Reasoning:
    Coefficient-matching of KNY (8.237) H_D6^KNY against Okamoto
    §1 H_III' at the WLOG slice η_0 = η_∞ = 1 produces a 2↔2
    correspondence (a_1+a_2 = -θ_0 from qp coefficient; -a_2 =
    ½(θ_0+θ_∞) from q coefficient) covering only the (θ_0, θ_∞)
    sector under η-normalization. The project's V_quad image
    (1/6, 0, 0, -1/2) carries unnormalized α_∞ = 1/6 ≠ 1 and
    α_0 = 0 ≠ 1 (Excerpt 4 explicit: "the project records all
    four of Okamoto's UNNORMALISED Hamiltonian parameters at the
    V_quad point"). KNY (8.237) is a normalized representative
    of H_D6^(1); coefficient-matching against it cannot recover
    the unnormalized (η_∞, η_0) directions because they are
    absorbed into the canonical-form scaling on both sides.

    058R's "derivable by expanding both Hamiltonians" claim is
    confirmed for the (θ_0, θ_∞) ↔ (a_1, a_2) sector but does
    not extend to the full chart-map at unnormalized η.

    Caveat (HIGH-confidence verdict pending small scan): KNY 2017
    §8 surrounding sections beyond the §8.5.17 paste may contain
    an un-normalization map for H_D6^(1) (e.g., the relation of
    KNY (8.237) to a parent unnormalized Hamiltonian via a scaling
    of (q, p, t)). If such a map exists in KNY §8.5 prose, Route
    A could revive to UNDECIDABLE_ROUTE_A and require a re-fire.
    Recommend agent perform a KNY §8.5 surrounding-sections scan
    (~30 min) before treating NO_GO_ROUTE_A as final.

QB.1 — FW arXiv TRIAGE (excerpt-based)
  Triage classification:                    NEEDS_EXECUTOR_AUDIT
  (a) KNY (a_0,a_1,a_2) referenced in FW:   N
  (b) FW (α,β) parametrisation form:        Two parameters (v_1, v_2),
                                              corresponding to Okamoto's
                                              (θ_0, θ_∞) at WLOG slice
                                              η_0=η_∞=1, per FW §4.1
                                              ODE coefficients matched
                                              against Okamoto eq. (0.1).
                                              Four parameters
                                              (v_1, v_2, v_3, v_4) for
                                              FW's P_V (§2.1), with
                                              null-sum constraint
                                              v_1+v_2+v_3+v_4 = 0
                                              (eq. (2.2)).
  (c) Conversion to (α_∞,α_0,β_∞,β_0) form: PARTIAL. (β_∞, β_0) =
                                              (θ_∞, θ_0) is recovered
                                              via Excerpt 4 §3.5.1
                                              trivial relabel
                                              (NON-TRIVIAL_BUT_CITED).
                                              (α_∞, α_0) = (η_∞, η_0)
                                              is GAP-CREATING at FW's
                                              WLOG slice; recovery
                                              routes through FW Prop
                                              4.1 mechanism (a) pull-
                                              back, executor work.
  Reasoning:
    FW excerpts (round-2 paste) supply:
      (i) FW §2.1 eq. (2.2) null-sum constraint v_1+v_2+v_3+v_4=0
          as PRIMARY LITERATURE — anchors what 058R §B.3 carried
          internally and discharges that provenance question.
      (ii) FW §4.1 P_III development at the (v_1, v_2) parametrisation
           (= Okamoto (θ_0, θ_∞) at WLOG slice).
      (iii) FW Proposition 4.1 auxiliary Hamiltonian h = tH + ¼v_1²
            − ½t (eq. (4.3)) — anchors Excerpt 4 mechanism (a) for
            the −1/3 offset.

    FW does NOT supply:
      - Direct chart-map to KNY (a_0, a_1, a_2). FW does not
        invoke the KNY frame.
      - The unnormalized (η_∞, η_0) parametrisation at FW's
        natural P_III development (FW works at WLOG slice η=1).
      - Pull-back of Prop 4.1 to the V_quad parameter point.
        Excerpt 4 marks this pull-back as "not yet derived" and
        records mechanism (a) as "a hypothesis with the FW eq.
        (4.3) anchor."

    Triage outcome NEEDS_EXECUTOR_AUDIT: FW excerpts plausibly
    contain substrate for closure under mechanism (a), but
    presence of closure cannot be classified from triage alone.
    Concrete pull-back computation is required.

QB.2 — Okamoto §3 sufficiency
  Sufficient given QB.1 outcome:            PARTIAL
  Reasoning:
    069r1-Path-β established Okamoto §3 alone is insufficient
    (closed at A.1.5 substrate gap). With round-2 Excerpt 1
    (FW) and Excerpt 4 (CT v1.3 §3.5.1) in hand, Okamoto §3
    contributes the τ-function reparametrisation framework but
    closure depends on FW Prop 4.1 pull-back per QB.1. Synth
    has not seen Okamoto §3 verbatim; cannot pin the partition
    between FW and Okamoto §3 contributions more crisply.

QB.3 — (η,θ) → (α,β) rename probe
  Verdict:    Y_RENAME_REQUIRED (discharged by Excerpt 4 §3.5.1
              landed at bridge HEAD 0427c0a; round-2 re-evaluation
              not requested per re-fire instructions, retained as
              robust)

QB.4 — Route B feasibility classification
  Verdict:    GO_ROUTE_B_CONDITIONAL (upgraded from round-1
              UNDECIDABLE_ROUTE_B)
  Preconditions for 069r3-B firing:
    1. Executor task scope: FW Prop 4.1 pull-back to V_quad
       parameter point (1/6, 0, 0, −1/2). Specifically, derive
       the explicit form of the auxiliary Hamiltonian shift
       h − tH = ¼v_1² − ½t (FW eq. (4.3)) when restricted to
       the V_quad reduction map (058R §B.3), and verify that
       the constant-shift contribution at the V_quad point sums
       to −1/3 against the FW null-sum locus
       v_1+v_2+v_3+v_4=0.
    2. Acceptance criterion: explicit trace of where the −1/3
       offset originates must appear in 069r3-B output, with
       mechanism (a) selection substantiated by the pull-back
       computation. If pull-back fails to produce −1/3,
       fallback to mechanism (b) (project-internal
       calibration, no literature anchor) or (c) (Sakai
       D_6^(1) surface-type, Route F surfacing per HALT-S5)
       must be explicitly recorded.
    3. No additional substrate acquisition required for 069r3-B
       firing. Excerpts 1, 3, 4 plus existing 058R §B.3
       reduction map suffice. (KNY §8.5.17 is not on Route B
       critical path; it was the Route A substrate.)
    4. Estimated executor effort: 5–10 hr (4–8 hr Prop 4.1
       pull-back + 1–2 hr V_quad cross-check).

  Reasoning:
    Round-1 ceiling for Route B was PARTIAL_ROUTE_B_RENAME
    (Y_RENAME_REQUIRED forced ceiling). Round-2 Excerpt 4
    landed §3.5.1 with trivial relabel (3.5.1a)–(3.5.1d),
    discharging the rename-side of the Route E precondition
    and lifting the ceiling. The remaining residual is
    mechanism (a) selection for the −1/3 offset, which
    Excerpt 4 anchors to FW Prop 4.1 (eq. (4.3)) — primary
    literature substrate that exists and is in hand.

    Mechanism (a) is uniquely positioned among the three
    candidates because it (i) closes Route B without
    additional acquisition, (ii) has primary-literature
    anchor in FW Prop 4.1, (iii) keeps the chart-map within
    σ-form / Hamiltonian P_III machinery (does not trigger
    HALT-S5 Route F surfacing). Mechanisms (b) and (c) are
    fallbacks: (b) is project-internal calibration only;
    (c) is a Route F (Sakai D_6^(1) surface-type) surfacing.

    GO_ROUTE_B_CONDITIONAL is therefore the right verdict bin:
    Route B is GO conditional on the named executor task
    completing successfully with mechanism (a) selection. If
    mechanism (a) pull-back fails, agent escalates to mechanism
    (b) (degrade to PARTIAL_ROUTE_B_RENAME with project-
    internal calibration record) or recognizes Route F
    surfacing per HALT-S5.

  Recommended next agent action:
    Draft 069r3_route_b_executor_envelope.txt with the
    precondition list above. Operator-side governance work on
    Route C / Route D fallbacks can stay deferred pending
    069r3-B outcome.

QC — Route C scope refinement
  Verdict:    N-A (premature; QB.4 = GO_ROUTE_B_CONDITIONAL,
              not rejected)
  Reasoning:
    QC is asked only if QA AND QB.4 are both rejected. QA =
    NO_GO_ROUTE_A but QB.4 = GO_ROUTE_B_CONDITIONAL
    (not rejected). QC remains N-A.

    Conjectural pre-rank if 069r3-B's mechanism (a) pull-back
    fails and Route B falls to NO_GO post-executor: C5 (Route
    D parallel) primary recommendation, since numerical
    fitting can attack offset-mechanism selection
    independently. C3 (JM 1981 Part II + Okamoto 1987) for
    Lax-pair monodromy data secondary. C4 (defer R1 to v1.1
    per 097) last resort. Deferred pending 069r3-B execution.

QD — Route D (numerical chart-map fitting) feasibility
  Verdict:    DEFERRED (per re-fire instructions; round-2
              substrate-paste for V_quad numerical-solution
              structure + (α, β) extraction operation spec is
              the next paste round)
  Reasoning:
    Note: Route D's value proposition has STRENGTHENED under
    round-2 outcome. With Route B = GO_CONDITIONAL gated on
    FW Prop 4.1 pull-back, Route D is well-positioned as
    parallel-track verification of the mechanism (a)
    selection. A numerical fit of the chart-map at V_quad's
    image should reproduce the −1/3 offset if mechanism (a)
    is correct. This turns Route D from "fragile solo path"
    (round-1 framing) to "high-value parallel verification"
    (round-2 framing).

  Recommended dispatch (conditional on QD resolution):
    PARALLEL_TO_ROUTE_B as mechanism (a) verification.
    Recommend operator schedule QD round-2 substrate-paste
    BEFORE 069r3-B fires, so 069r3-D can launch in parallel
    rather than sequentially.

QE — Route E precondition status
  Verdict:    ROUTE_E_TRIVIAL (relabel side discharged by
              Excerpt 4 §3.5.1 landed at bridge HEAD 0427c0a)
              with offset-mechanism deferral acceptable for
              §3.5.1-as-deposited
  Reasoning:
    Excerpt 4 §3.5.1 records a pure symbol-substitution
    relabel (α_∞ := η_∞, α_0 := η_0, β_∞ := θ_∞, β_0 := θ_0)
    with no additive shift; ROUTE_E_TRIVIAL is the right bin.
    The Okamoto WLOG normalization is explicitly NOT imposed,
    so the project's 4-tuple lives in unnormalized (η, θ)
    space — which is what allows V_quad's image
    (1/6, 0, 0, −1/2) to live in the project namespace.

    The 3-mechanism deferral for the −1/3 offset is
    structurally acceptable for §3.5.1 as a v1.3 governance
    deposit. The deferral creates an asymmetry: QE-as-rename
    is closed; QE-as-offset-explanation is open. Resolution
    of the open side is the Route B critical-path acceptance
    criterion (see QB.4) and is properly executor work
    (069r3-B), not synth-decidable governance work.

    Operator's question — "is tiered selection of mechanism
    (a) required before TIER-B re-fire?" — synth answer:
    only if TIER-B re-fire is gated on R1 closure with
    mechanism selected, which the 069r2 envelope frames as
    the case (per §1 row 8: 097 PARTIAL_INSUFFICIENT_DATA
    named gating prerequisite = R1 closure preflight). Under
    that gating, tiered selection of (a) IS the work, and
    069r3-B IS the executor that does it. The §3.5.1 deposit
    + the 069r3-B envelope together discharge QE in tiered
    fashion: §3.5.1 records WHAT is open; 069r3-B closes it.

    HALT-S5 watch: mechanism (c) explicitly names Sakai
    D_6^(1) surface-type machinery. If 069r3-B's mechanism
    (a) execution fails and the offset routes through (c),
    this is a Route F surfacing per HALT-S5 — agent should
    be prepared to flag ROUTE_FRAME_INCOMPLETE rather than
    fold into A–E.

QF — Confidence
  QA confidence:       HIGH (with HIGH-confidence caveat that
                        a quick KNY §8.5 surrounding-sections
                        scan is recommended before treating
                        NO_GO_ROUTE_A as final)
  QB.4 confidence:     MEDIUM-HIGH (Route B's GO_CONDITIONAL is
                        well-grounded; MEDIUM caveat is that
                        mechanism (a)'s pull-back has not been
                        executed and could fail or route through
                        Sakai (c))
  QB.2 confidence:     MEDIUM (derivative; PARTIAL classification
                        robust but partition between FW and
                        Okamoto §3 not crisply visible)
  QC confidence:       N-A (deferred)
  QD confidence:       N-A (deferred to next round)
  QE confidence:       HIGH for the rename-side (Excerpt 4
                        §3.5.1 landed); MEDIUM for the
                        deferral-acceptability framing (depends
                        on TIER-B gating semantics)
  Caveats:
    1. Route A and Route B both face the same structural feature
       — the (η_∞, η_0) directions live outside both KNY's
       normalized presentation and FW's WLOG slice. Route A
       cannot reach them via coefficient-matching; Route B
       reaches them via FW Prop 4.1 mechanism (a) pull-back.
       This is the fundamental reason Route B succeeds where
       Route A fails: Route B routes through the auxiliary
       Hamiltonian h, which carries the constant-shift degrees
       of freedom that the primary tH does not.

    2. Round-1 Caveat 3 (the −1/3 offset is the most informative
       single technical clue) is upheld and sharpened. Mechanism
       (a) selection IS the chart-map closure mechanism for the
       (α_∞, α_0) sector. The synth recommends the 069r3-B
       executor envelope explicitly name the −1/3 offset trace
       as the primary acceptance criterion.

    3. Route D parallel scheduling recommendation: operator
       should prioritize QD round-2 substrate-paste BEFORE
       069r3-B fires. If QD resolves to GO_ROUTE_D, parallel
       dispatch of 069r3-B (analytic) and 069r3-D (numerical)
       provides cross-validation of mechanism (a) selection
       and lowers the risk of 069r3-B failure cascading to a
       Route C / Route F escalation. The two routes are
       independent: Route B is FW-Prop-4.1-pull-back analytic;
       Route D is V_quad → P_III(D_6) numerical-trajectory
       fitting. They converge on the same answer (the chart-map
       and the −1/3 offset origin) by orthogonal means.

    4. 069r1 Greek-letter labels remain reserved (HALT-S6).
       This verdict does not reuse α/β/γ/δ outside their
       069r1-Path-X prefix or their well-defined mathematical
       roles (P_III ODE coefficients per Excerpt 4
       Remark, Okamoto Hamiltonian parameters per Excerpt 3,
       project 4-tuple per Excerpt 4 (3.5.1a)–(3.5.1d), FW
       (v_1,v_2,v_3,v_4) per Excerpt 1 §2.1).

Rubber-duck QA acknowledged (Round-1 9 findings + Round-2
                              6 findings absorbed): Y
====================
```

---

**Net recommendation to operator (round 2):**

1. **Route A is rejected** (NO_GO_ROUTE_A) — the WLOG-normalization obstruction is structurally visible from Excerpts 2 + 3. Recommend a quick (~30 min) KNY §8.5 surrounding-sections scan before treating this as final, in case an un-normalization map exists outside §8.5.17.

2. **Route B is GO_CONDITIONAL** — the FW Prop 4.1 mechanism (a) pull-back is the named executor task for 069r3-B. No additional acquisition required; effort estimate 5–10 hr. The −1/3 offset trace is the primary acceptance criterion. Excerpt 4 §3.5.1 has discharged the Route E rename-side; Route B's path to closure is now clear.

3. **Route E is governance-complete for v1.3** — §3.5.1 landed at bridge HEAD 0427c0a with trivial relabel + 3-mechanism deferral. The deferral is structurally acceptable; mechanism (a) selection is properly 069r3-B executor work, not §3.5.1 governance work.

4. **Schedule Route D round-2 substrate-paste BEFORE 069r3-B fires.** Route D's value has shifted from "fragile solo path" to "high-value parallel verification of mechanism (a)." Parallel dispatch of 069r3-B + 069r3-D lowers cascade risk if mechanism (a) fails.

5. **HALT-S5 standing watch:** if 069r3-B's mechanism (a) pull-back fails and the offset routes through Sakai D_6^(1) surface-type machinery (Excerpt 4 mechanism (c)), this is a Route F surfacing — agent should flag ROUTE_FRAME_INCOMPLETE rather than fold into Routes A–E.

The single-paste round was efficient: four named excerpts converted three UNDECIDABLE verdicts (QA, QB.1, QE) into actionable verdicts (NO_GO, NEEDS_EXECUTOR_AUDIT → GO_CONDITIONAL, ROUTE_E_TRIVIAL with deferral) and identified mechanism (a) as the chart-map closure path. Recommend round-2 substrate-paste for QD next.