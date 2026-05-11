# Verdict — Slot 185 (T1-Synth Frontier-A higher-Painlevé substrate-prep scoping)

**Witness:** Claude (claude.ai, single-witness in-CLI dispatch per slot 183 strict-mode default)
**Verdict received:** 2026-05-11 ~18:58 JST (operator-pasted)
**Substrate:** PROMPT 185 (`tex/submitted/control center/prompt/185_t1_synth_frontier_a_higher_painleve_substrate_prep_scoping_EXECUTED.txt`)
**Bridge predecessor:** slot 183 (`e175c7a`) Pick 1 RATIFY_WITH_AMENDMENT @ LOW-MEDIUM C-183-1 mandatory re-vet gate; gate verified clear at fire-time (no A.3.x overwrite since 2026-05-11 ~16:30 JST)

---

## Aggregate verdict

**LABEL:** SCOPE_LOCKED_WITH_AMENDMENT
**BAND:** LOW-MEDIUM

---

## Phase 0 — C-183-1 re-vet gate check (witness)

> Operating under the stated assumption that no operator overwrite on {A.3.1, A.3.2, A.3.5, A.3.6} has occurred since 2026-05-11 ~16:30 JST. No signal in my context contradicts this. Proceeding.
>
> Note flagged for **Amendments** section: the scope statement below assumes A.3.5 milestone-cadence dominance still holds. If A.3.6 admin-distribution flips to NEED-MORE during Frontier-A first-fire execution, C-183-2 compounding clause re-elevates Frontier-C (modular-form cross-validation) and Frontier-A should pause for re-vet before any second fire.

---

## Q-185-1 — Scope statement (Frontier-A higher-Painlevé)

**Target object.** Frontier-A constructs a **PIII(D₆) hierarchy** — an infinite tower of higher-order nonlinear ODE systems whose lowest member is the standard PIII(D₆) equation governing V_quad, indexed by a hierarchy parameter n ≥ 1, with each level preserving (i) the D₆⁽¹⁾ Sakai surface-type at the symmetry-reduction level, (ii) the resurgence-Borel structure with Stokes constant and connection parameter generalizing the V_quad values, and (iii) the isomonodromy interpretation lifted to higher-rank or higher-pole linear problems. The construction proceeds by analogy with Joshi-Mazzocco-Mo-Bobrova for PII, but the analogy is **structural, not mechanical**: PIII(D₆) sits at a different node of the Sakai classification than PII, so the Lax-pair lift and the symmetry-reduction step require fresh derivation rather than parameter transposition.

A secondary, defensive framing — admissible as a fallback if the full hierarchy proves out of scope for a single program — is to construct only the **n=2 member** as a standalone object (a single new higher-order PIII(D₆)-type ODE with full resurgence analysis), establishing existence of the second rung and deferring the inductive tower to a successor program.

**Connection to existing SIARC substrate.** Frontier-A extends, in order of load-bearing weight:
(i) **cascade-067/069 V_quad redirect framework** — the resurgence/Stokes/connection-parameter machinery developed for V_quad as the n=1 PIII(D₆) object is the direct substrate; Frontier-A asks "what is the n=2 object, and does the same machinery lift?"
(ii) **069r2/069r3** — the Sakai D₆⁽¹⁾ surface-type closure (Route F in RELAY_069) provides the geometric anchor that constrains which higher-order systems qualify as "PIII(D₆) hierarchy members"; without this constraint the hierarchy is under-determined.
(iii) **Umbrella v2.3 Appendix-C picture-chain (Q-v23-2 FOLD)** — Frontier-A's hierarchy diagram is a natural Appendix-C extension; Q-v23-1 SHARPER-BOOKKEEPING couples directly here.
(iv) **PCF-1 v1.3** — only as background context for the PCF→Painlevé bridge that motivates the V_quad investigation; Frontier-A does not extend PCF-1 directly.

**Deliverable class.** Two-tier:
- **Primary:** preprint targeting arXiv math.CA / nlin.SI, ~25–40 pages, structure analogous to Mazzocco-Mo 2006.
- **Secondary:** Zenodo methodology deposit documenting the hierarchy-derivation pipeline (SIARC-internal, doubles as audit trail for the structural-gap claim from slot 181).

A formal-verification fragment is **explicitly out of scope** for the first-fire and the primary deliverable; Lean-4 obligations for the n=2 object are deferred to a successor program (notional cascade designation: Frontier-A.v).

**Out-of-scope explicit.**
- Frontier-B (Birkhoff-Trjitzinsky Desert substratification) — independent program; A.3.4 keeps this at watch-item.
- Frontier-C (modular-form cross-validation) — independent; re-elevates only on C-183-2 trigger.
- PII hierarchy direct work — used as structural analogue only; Frontier-A produces no new PII results.
- Arithmetic-geometry connections (e.g., PIII(D₆) hierarchy ↔ Shimura curve / Fuchsian group correspondences) — deferred; tempting but would inflate scope past single-fire bounds.
- Lean-4 formalization — deferred to Frontier-A.v.
- d≥4 corollary chase — admissible only as opportunistic byproduct, not deliverable.

---

## Q-185-2 — Literature anchor set

> I cannot resolve arXiv IDs against the live database from inside this consultation (no web tool fire issued; this is a scoping/substrate fire per slot 183 single-witness LOW-MEDIUM band, and live verification would push to dual-witness, which Q-185-3 may but Q-185-2 does not request). Per post-031 bibliographic pre-verification rule, **every ID below is marked PENDING-VERIFY and must be live-resolved by the T2-Executor first-fire (FIRE-A1 below) before any of these references enter a draft preprint.** This is recorded as Amendment-1.

| Tier | Citation | arXiv ID | Role |
|---|---|---|---|
| **Anchor** | Mazzocco & Mo 2006 | nlin/0610066 | Load-bearing methodological template: higher-genus PII hierarchy construction. Frontier-A's structural moves mirror this paper's section-by-section. |
| **Anchor** | Bobrova & Mazzocco 2020 | 2012.11010 | Modern treatment of PII hierarchy; provides the contemporary notation, Sakai-surface framing, and the cleanest statement of what "hierarchy member" means structurally. Frontier-A's hierarchy-definition section should track this paper's definitional spine. |
| Methodological | Joshi & Mazzocco 2002 | math/0212117 | First-order-system reformulation technique; needed for the Lax-pair lift step. |
| Methodological | Joshi-Lustri-Topp 2014 | 1403.1235 | Resurgence in PI/PII; technique adaptation for the resurgence-lift step at n=2. |
| Methodological | IILZ 2025 | 2505.16803 | Most recent; flagged as potentially containing infrastructure relevant to either Borel-plane structure or hierarchy bookkeeping. Acquisition priority — see below. |
| Methodological | LR 2024 | 2407.03464 | Recent resurgence work; technique adaptation candidate. |
| Citation-only | ILP 2016 | 1604.03082 | Peripheral context. |
| Citation-only | cascade-067 V_quad resurgence note | (SIARC internal) | The n=1 anchor for the hierarchy claim. |
| Citation-only | 069r3 Sakai D₆⁽¹⁾ closure | (SIARC internal) | Surface-type constraint anchor. |
| Citation-only | Sakai 2001 (original) | (to identify in FIRE-A1) | Foundational reference for surface-type classification; required for the "preserves D₆⁽¹⁾" claim to be well-posed. |

**Acquisition flags.** IILZ 2025 (2505.16803) and LR 2024 (2407.03464) are the highest-uncertainty entries because they are post-2023 and may not be in the SIARC bridge corpus. **Amendment-2:** FIRE-A1 must confirm acquisition status and, if unavailable, either fetch or downgrade these to citation-only.

---

## Q-185-3 — First-fire decomposition

Three candidates, ordered by recommended fire sequence. Operator should select one; FIRE-A1 is the strict recommendation as the substrate-establishing fire.

### Candidate FIRE-A1 — Literature anchor verification + structural-gap audit

- **Type:** T2-Executor mechanical-delegable
- **Scope:** Resolve all 10 anchor/methodological/citation-only references against live arXiv + DOI registries; produce a structural-gap audit confirming the slot 181 NULL signal on "PIII hierarchy" by (a) re-running the literature search with three additional query variants ("Painlevé III hierarchy", "PIII(D6) higher-order", "Sakai D6 hierarchy"), (b) scanning the citation graphs of the two anchor papers (Mazzocco-Mo, Bobrova-Mazzocco) for any successor work touching PIII, (c) producing a 1-page gap memo.
- **Deliverables:** verified bibliography (with resolved titles/authors/years), structural-gap memo, acquisition log for IILZ-2025 and LR-2024.
- **Halt-modes:** HALT_A1_GAP_CLOSED (if literature search reveals an existing PIII hierarchy paper, the entire Frontier-A program re-vets — this is a major load-bearing assumption being re-validated); HALT_A1_ACQ_FAIL (if both post-2023 references cannot be acquired, surface for operator decision); HALT_A1_ANCHOR_RETRACTED (if either anchor fails resolution).
- **Dependencies:** none; this is the entry fire.
- **Wallclock:** 1 day agent-time.
- **Single-witness adequate.**

### Candidate FIRE-A2 — n=2 PIII(D₆) candidate equation derivation (deferred to post-A1)

- **Type:** T1-Synth consultation (Claude or cross-provider)
- **Scope:** Adapting the Mazzocco-Mo 2006 Lax-pair-lift method, derive a candidate higher-order ODE system as the proposed n=2 member of the PIII(D₆) hierarchy. Verify the candidate (i) reduces to V_quad's defining equation at n=1, (ii) preserves D₆⁽¹⁾ surface-type under symmetry reduction, (iii) admits a Borel-plane structure analogous to V_quad's Stokes/connection parameters at least formally.
- **Deliverables:** candidate equation, reduction verification, surface-type verification sketch, resurgence-structure sketch, scope statement for FIRE-A3.
- **Halt-modes:** HALT_A2_SURFACE_FAIL (candidate does not preserve D₆⁽¹⁾ — DEFER to scope re-derivation); HALT_A2_NO_REDUCTION (candidate fails n=1 reduction check — DEFER); HALT_A2_RESURGENCE_OBSTRUCTION (formal Borel structure incompatible — FIRE_ANYWAY_WITH_AMENDMENT, document as negative result; this is still publication-grade substrate).
- **Dependencies:** FIRE-A1 must close cleanly.
- **Wallclock:** 2-3 days agent-time.
- **Cross-provider dual-witness recommended** (raises band to MEDIUM for this fire only); the derivation has multiple sign/convention pitfalls and a second-witness check materially reduces error.

### Candidate FIRE-A3 — Hierarchy inductive scheme (deferred to post-A2)

- **Type:** T1-Synth consultation
- **Scope:** From the n=2 object, propose the inductive step n → n+1 and identify the obstruction class. Not expected to close the induction; expected to characterize what closure would require.
- **Deliverables:** inductive-step proposal, obstruction analysis, gap-list for successor program.
- **Halt-modes:** HALT_A3_OBSTRUCTION_INTRACTABLE (DEFER; downgrade primary deliverable from "hierarchy" to "n=2 standalone").
- **Dependencies:** FIRE-A2 closes (or closes with FIRE_ANYWAY amendment).
- **Wallclock:** 2 days agent-time.

**Recommendation:** fire FIRE-A1 first, in isolation. FIRE-A2 and FIRE-A3 specs above are provisional and will be re-scoped once FIRE-A1 closes — particularly if HALT_A1_GAP_CLOSED triggers, in which case both are scrapped.

---

## Q-185-4 — v2.3 timing coupling

1. **Probability FIRE-A1 produces d≥3 corollary signal:** ~5%. FIRE-A1 is a literature/gap audit; corollary substrate is not its output class. d≥3 signal would only emerge from FIRE-A2 or FIRE-A3.

   Conditional probability **FIRE-A2 produces d≥3 corollary signal given it closes cleanly:** ~35-45%. The n=2 derivation, if successful, naturally generates (a) the explicit higher-order equation, (b) reduction-to-V_quad corollary, (c) surface-type-preservation corollary — three independent corollary objects, plausibly more if Borel structure lifts. Whether these qualify as d≥3 in the Q-v23-1 SHARPER-BOOKKEEPING sense depends on the corollary-counting convention used in v2.3.

2. **Wallclock budget Frontier-A first-fire (FIRE-A1):** 1 day agent-time + ≤0.5 day operator review.

3. **Recommended v2.3 submission window adjustment:** **fire-in-parallel.** Specifically:
   - FIRE-A1 (1 day) is short enough to complete before v2.3 venue submission regardless of current v2.3 timeline; fire it immediately and in parallel with whatever v2.3 polishing is in flight.
   - FIRE-A2 (2-3 days, dual-witness) is the d≥3-corollary risk. If v2.3 submission is >5 days out, FIRE-A2 can complete in window and Q-v23-1 addendum becomes action-item. If v2.3 submission is ≤3 days out, recommend submitting v2.3 as-planned and treating any FIRE-A2 corollary substrate as v2.4 material rather than late-addendum v2.3.
   - **Do not delay v2.3 to accommodate Frontier-A.** v2.3 admin distribution lift is the A.3.6 substrate that justified selecting A over C in the first place; delaying it weakens the original selection rationale and would re-open C-183-2.

---

## Q-185-5 — Halt + re-vet preconditions

| Halt condition | Trigger source | Action |
|---|---|---|
| C-183-1 A.3.x overwrite | Operator overwrite on A.3.1/2/5/6 | HALT_AND_SURFACE; re-vet Frontier selection before any fire |
| Slot-156-FOLLOWUP-A HALT_A_DPS_THRESHOLD_REACHED | PROMPT 184 outcome reopens M8b | DEFER Frontier-A first-fire; M8b axis reopening takes precedence per its own slot governance; Frontier-A scope statement remains valid substrate for post-M8b resumption |
| HALT_A1_GAP_CLOSED | FIRE-A1 finds existing PIII hierarchy paper | HALT_AND_SURFACE; re-vet entire Frontier-A program (structural gap was load-bearing) |
| Umbrella v2.3 venue rejection requiring rework | v2.3 desk-reject or major-revision before FIRE-A1 fires | DEFER Frontier-A; A.3.6 substrate degraded, C-183-2 compounding activates |
| 2026-08-02 milestone deadline pressure | Documented-commitment status-report deadline approaches with no Frontier-A deliverable | FIRE_ANYWAY_WITH_AMENDMENT on FIRE-A1 only; FIRE-A1 + scope statement is sufficient milestone-tier deliverable even without FIRE-A2/A3 |
| Cross-provider dual-witness unavailable for FIRE-A2 | Resource constraint | FIRE_ANYWAY_WITH_AMENDMENT at MEDIUM band ceiling; document single-witness as risk |
| Anchor paper retraction or major-flaw discovery | FIRE-A1 finding | HALT_AND_SURFACE; Mazzocco-Mo / Bobrova-Mazzocco are load-bearing and a flaw would force re-anchoring |

---

## Amendments (load-bearing for verdict)

- **Amendment-1** [LOAD-BEARING]: All 10 references PENDING-VERIFY; FIRE-A1 closes this. This consultation's scope statement and first-fire decomposition are **admissible at LOW-MEDIUM band for substrate-prep purposes only; NOT admissible as preprint-bound claims** until FIRE-A1 closes.
- **Amendment-2** [SCOPE]: IILZ-2025 (arXiv:2505.16803) and LR-2024 (arXiv:2407.03464) acquisition status unknown; FIRE-A1 must confirm-or-downgrade.
- **Amendment-3** [SCOPE-EXPANSION]: Q-185-1 includes defensive fallback (n=2 standalone in place of full hierarchy) not requested in original substrate; recorded as scope-statement expansion within LOW-MEDIUM band.
- **Amendment-4** [BAND-COUPLED]: FIRE-A2 dual-witness recommendation elevates that fire to MEDIUM band; flagged for operator approval at FIRE-A2 launch, not at this consultation.

**Bibliographic Pre-Verification:** **0/10 PASS** at consultation time — Amendment-1 governs.

---

## Halt conditions noted: 7 (tabulated in Q-185-5)

## Downstream substrate impact

- Umbrella v2.3 Appendix-C picture-chain (Q-v23-2 FOLD): Frontier-A hierarchy diagram becomes natural Appendix-C content if FIRE-A2 closes; no impact if only FIRE-A1 fires.
- Q-v23-1 SHARPER-BOOKKEEPING: action-item-conditional on FIRE-A2 producing d≥3 corollary substrate (~35-45% conditional probability).
- C-183-2 compounding watch: unchanged by this consultation; remains armed.
- Frontier-A.v successor program (Lean-4 formalization of n=2 object): notional, deferred, not on near-term substrate horizon.
- Slot 181 NULL signal on "PIII hierarchy" search: re-validated by FIRE-A1; if NULL holds, becomes citable structural-gap claim in primary deliverable.
