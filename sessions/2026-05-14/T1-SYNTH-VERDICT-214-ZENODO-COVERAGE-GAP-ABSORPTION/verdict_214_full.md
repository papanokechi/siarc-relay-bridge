# T1-SYNTH VERDICT 214 — ZENODO COVERAGE-GAP MINT-OR-WAIT

**Verdict ID:** T1-SYNTH-VERDICT-214-ZENODO-COVERAGE-GAP
**Date:** 2026-05-14 ~08:25 JST
**Witness class:** solo-witness Opus-class (claude.ai)
**Substrate anchor:** bridge HEAD `efa68b4`; PROMPT 214 substrate §2A–§2E
**Aggregation rule:** cascade-123 §3.2 (most-conservative LABEL/BAND across Q-LOCKs)

---

## Q-214-1 — Per-item mint-or-wait (sub-locked)

### Q-214-1a — Item 5 (Khinchin-Signature, ExpMath, 25d in)

- **LABEL:** PROCEED
- **BAND:** MEDIUM
- **LOCK:** α (MINT NOW)
- **Confidence:** 0.78
- **Reasoning:** 25 days in is well past the priority-anchor sweet spot where pre-verdict mint dominates. ExpMath is now blacklisted per project memory (7 no-reason rejections including this one's predecessor pattern); a rejection-route is the modal outcome, in which case Zenodo concept-DOI becomes immediately load-bearing for re-route substrate-prep. Cost-asymmetry favors α: ~15 min metadata work now vs. needing it under time-pressure when ExpMath returns.
- **Sensitivity flag:** Inverts to β if synth/operator believes ExpMath verdict is imminent (<7d); current 25d position with no editor signal makes that unlikely.

### Q-214-1b — Item 13 (Self-Adjoint PCF, JDE, 22d in)

- **LABEL:** PROCEED
- **BAND:** MEDIUM
- **LOCK:** α (MINT NOW)
- **Confidence:** 0.80
- **Reasoning:** JDE is a 3-6mo verdict horizon; 22d in is early-cycle, priority-anchor value still high. Elsevier preprint policy explicitly permits Green OA deposit at submission stage (§2D confidence 0.90), so policy posture is clean. Symmetry with Items 26 (JSC) and 27 (Compositio) — both Elsevier-or-comparable, both Zenodo-backed pre-verdict — argues for parity treatment.
- **Sensitivity flag:** Inverts to ε (NEVER) only if synth's preprint-policy reading at §2D is wrong for JDE specifically (e.g., a math.AP sub-policy disallows pre-acceptance deposit). 0.90 prior makes this low-probability.

### Q-214-1c — Item 28 (R4 Spectral Classes, JNT, 2d in)

- **LABEL:** PROCEED
- **BAND:** HIGH
- **LOCK:** α (MINT NOW)
- **Confidence:** 0.88
- **Reasoning:** 2d in is the cleanest possible α case — maximum priority-anchor value, minimum verdict-proximity-decay. More importantly, Item 28 is the 3rd venue in a redirect cascade (Items 3 → 16 → 28 per `a15091c`) with NO prior Zenodo deposit at any step; this is the single most exposed manuscript in the in-flight portfolio for priority-anchor risk. JNT is Elsevier (same permissive policy as JDE).
- **Sensitivity flag:** Inverts to β only if Q-214-4 surfaces a strategic non-deposit rationale (Q-214-4 γ); 0.88 reflects that this is the lowest-probability invert across the three.

**Q-214-1 aggregate (cascade-123 §3.2 most-conservative):**
- **LABEL:** PROCEED
- **BAND:** MEDIUM (driven by 1a + 1b)
- **LOCK:** α across all three items (uniform α)

---

## Q-214-2 — Mint timing

- **LABEL:** PROCEED
- **BAND:** MEDIUM
- **LOCK:** ε (OPERATOR-DRIVEN substrate-prep; agent stages metadata YAML + abstract + concept-DOI plan)
- **Confidence:** 0.75
- **Reasoning:** V213 ε BIFURCATE is in force through 2026-05-27; operator-fire cadence is the governance-aligned default. Agent prepares all three deposit packages (metadata YAML, abstract reuse from journal-portal versions, concept-DOI mint plan with PCF-2 paste-verify discipline) in the 5/15 evening bundle window; operator fires the auth-confirm step when convenient. This preserves operator bandwidth without coupling to a fixed calendar slot, and respects the Carneiro 7d silence-watch which is the higher-priority operator-attention claim through 5/20.
- **Sensitivity flag:** Inverts to α (5/15 bundle) if operator signals bandwidth is fine and prefers single-window minimum-touch; inverts to δ (staggered 1-per-2-days) if operator flags any concern about single-deposit blast radius given the V213 cycle-compression posture.

---

## Q-214-3 — Manuscript-version mapping

- **LABEL:** PROCEED
- **BAND:** HIGH
- **LOCK:** α (ANONYMIZED-AS-SUBMITTED across all three)
- **Confidence:** 0.85
- **Reasoning:** Matches Items 21/26/27/29 baseline pattern (every other in-flight manuscript). Preserves reviewer-blind across all three venues — ExpMath, JDE, and JNT all run single-blind or stricter, and a reviewer hitting Zenodo and seeing a deanonymized version is a non-trivial editorial-trust hazard. The δ option (dual versions) is defensible but adds bookkeeping cost without clear value pre-verdict; defer to post-verdict if desired. Concept-DOI ↔ version-DOI discipline per project memory: mint concept-DOI first, then v1.0 version-DOI = anonymized PDF.
- **Sensitivity flag:** Inverts to γ (asymmetric per blinding policy) only if ExpMath turns out to be open-review rather than single-blind; agent's prior is 0.85 single-blind, defer to operator if uncertain.

---

## Q-214-4 — Item 28 spectral-classes deep-dive

- **LABEL:** PROCEED
- **BAND:** MEDIUM
- **LOCK:** δ (CHECK ITEMS 3 + 16 SUBMISSION FILES FIRST)
- **Confidence:** 0.70
- **Reasoning:** Agent has no recall of a strategic non-deposit rationale for the spectral-classes manuscript across its three submissions — the most likely explanation is genuine oversight (α). However, the redirect cascade Items 3 → 16 → 28 spans ExpMath (rejected) → RNT (rejected) → JNT (current), and the manuscript framing has plausibly evolved across submissions (hypergeometric framework + arithmetic obstructions in current title suggests substantive R4 reframing post-RNT). Verifying the Items 3/16 submitted files against Item 28's current substrate before mint is cheap (~10 min) and resolves whether v1.0 deposit should be backdated-metadata (essentially-same) or just-current (substantively different).
- **Sensitivity flag:** Inverts to α (oversight, mint v3 only) if Items 3/16 file diff confirms substantive reframing; remains δ until that diff is done. Inverts to β/γ only if synth/operator surfaces a previously-undocumented suppression rationale, which agent has no prior on.

---

## Q-214-5 — Documentation-gap coupling

- **LABEL:** PROCEED
- **BAND:** MEDIUM
- **LOCK:** β (COUPLED with explicit separation in commit message)
- **Confidence:** 0.78
- **Reasoning:** The 5/15 evening bundle window is already operator-attention-allocated for the 7-deposit submission_log §3 patch + PORTFOLIO_INVENTORY refresh + D-209-2 audit. Bundling the Items 5/13/28 substrate-prep into that window (per Q-214-2 ε, agent-side prep only) is minimum-touch and amortizes a single auth-confirm cycle. Explicit commit-message separation (e.g., `bundle/214: logging-gap-patch | items-5-13-28-zenodo-prep | inventory-refresh`) preserves cascade-123 §3.2 audit-trail parseability. The γ option (separate 5/18 mints) is defensible but adds an operator-attention cycle that the V213 cadence is trying to minimize.
- **Sensitivity flag:** Inverts to γ if Q-214-2 resolves to α (5/15 fire, not just substrate-prep) AND operator flags 5/15 cognitive load as already saturated by Carneiro silence-watch + bundle ops.

---

## Q-214-6 — Memory-promotion: pre-verdict Zenodo-backup rule

- **LABEL:** PROCEED
- **BAND:** MEDIUM
- **LOCK:** ε (PROMOTE A WEAKER VERSION)
- **Confidence:** 0.72
- **Reasoning:** The Items 21/26/27/29 baseline is real and worth codifying, but a hard 7d-or-14d binding rule with exception-logging overhead is heavier governance than the underlying practice warrants. A recommend-strong / mandatory-before-reroute formulation captures the operationally-useful invariant (priority-anchor exists before any re-route substrate-prep is needed) without forcing the agent into deliberation-overhead for every routine submission. The α option would retroactively bind Items 5/13/28 to immediate mint, but Q-214-1 already resolves that PROCEED-α independently, so binding rule-force isn't required to land the right outcome.

  **Refined candidate text:**
  > "Recommendation: every manuscript submitted to a peer-reviewed venue SHOULD have a corresponding Zenodo concept-DOI minted within 14 days of journal-portal submission, anonymized version matching submitted manuscript. MANDATORY: before any post-rejection re-route substrate-prep begins, the rejected manuscript's most-recent submitted version MUST be Zenodo-deposited (concept-DOI if first deposit, version-DOI if updating existing concept-DOI). Software-class deposits follow the same MANDATORY rule for any code release referenced in a submitted manuscript."

- **Sensitivity flag:** Promote to α (binding 7d rule) only if operator flags that recommendation-class governance has historically slipped to non-compliance; agent's read is that the Items 21/26/27/29 compliance pattern shows recommendation-force is sufficient.

---

## §5 ANOMALIES / OPEN THREADS

1. **G5 gate remains live until operator runs Zenodo `/me/uploads` audit.** Agent confidence on Items 5/13/28 true-coverage-gap is 0.75 (per §2E); operator ground-truth from Zenodo profile pushes to 1.0 or inverts the consultation. Recommend operator runs this audit BEFORE firing the 5/15 bundle, not after — if any of the three has an unrecorded deposit, Q-214-1 collapses to a documentation-fix for that item and Q-214-3/4 are moot for it.

2. **Preprint-policy verification residual.** §2D agent priors are 0.85 (ExpMath) / 0.90 (JDE) / 0.90 (JNT). For Q-214-1 LOCKs to be load-bearing pre-mint, recommend a 5-min web-check of each journal's current preprint policy before the 5/15 substrate-prep lands. Elsevier policies are stable, but T&F has historically been more variable across imprints.

3. **Item 28 redirect-cascade file diff (Q-214-4 δ).** The 10-min diff of Items 3/16 submitted PDFs against Item 28's anonymized JNT submission is a hard prerequisite for the Q-214-4 LOCK and a soft prerequisite for the Q-214-1c MINT. Should land in agent-side substrate-prep before 5/15 bundle.

4. **PCF-2 concept-DOI `19936297` paste-verify discipline applies.** Per project memory, before any post-lift Zenodo deposit. Items 5/13/28 deposits will mint NEW concept-DOIs (not PCF-2-related), but the paste-verify habit transfers: confirm each new concept-DOI value before it propagates to submission_log §3 / PORTFOLIO_INVENTORY §B.

5. **Carneiro 7d silence-floor (5/20) is the higher-priority operator-attention claim through next week.** Q-214-2 ε resolution is partly defensive against accidentally coupling Zenodo-mint operator-attention with arXiv-endorsement reply-watch attention. If Carneiro replies in-window (high-probability outcome), Q-214-2 may upgrade to α 5/15 within bandwidth.

---

## §6 AEAL SUMMARY TABLE

| Q-LOCK | LABEL | BAND | LOCK | Conf | Inverts on |
|---|---|---|---|---|---|
| Q-214-1a (Item 5) | PROCEED | MEDIUM | α MINT NOW | 0.78 | ExpMath verdict imminent (<7d) |
| Q-214-1b (Item 13) | PROCEED | MEDIUM | α MINT NOW | 0.80 | JDE math.AP preprint sub-policy disallows |
| Q-214-1c (Item 28) | PROCEED | HIGH | α MINT NOW | 0.88 | Q-214-4 surfaces non-deposit rationale |
| Q-214-1 aggregate | PROCEED | MEDIUM | α uniform | — | — |
| Q-214-2 | PROCEED | MEDIUM | ε OPERATOR-DRIVEN | 0.75 | Operator signals 5/15 bandwidth fine |
| Q-214-3 | PROCEED | HIGH | α ANONYMIZED-AS-SUBMITTED | 0.85 | ExpMath turns out open-review |
| Q-214-4 | PROCEED | MEDIUM | δ DIFF FIRST | 0.70 | Diff confirms reframing (→α) |
| Q-214-5 | PROCEED | MEDIUM | β COUPLED+separation | 0.78 | 5/15 cognitive load saturated (→γ) |
| Q-214-6 | PROCEED | MEDIUM | ε WEAKER promotion | 0.72 | Recommendation-class compliance slips |

**Aggregate verdict (cascade-123 §3.2 most-conservative):**
- **LABEL:** PROCEED
- **BAND:** MEDIUM
- Driven by Q-214-1a/b, Q-214-2, Q-214-5, Q-214-6 all MEDIUM; no Q-LOCK below MEDIUM.

---

## §7 MEMORY-PROMOTION CANDIDATES

1. **Pre-verdict Zenodo-backup rule (Q-214-6 primary):** PROMOTE — ε WEAKER VERSION per refined text above. Recommendation-class within 14d; mandatory before any post-rejection re-route substrate-prep. Confidence 0.72.

2. **Submission_log §3 ↔ PORTFOLIO_INVENTORY §B reconciliation discipline (§5 candidate 2):** PROMOTE AS-IS. The 7-deposit gap discovery 2026-05-13 ~19:00 JST is a clear failure-mode signal; 7d reconciliation window is operationally light-weight. Includes software-class deposits explicitly. Confidence 0.85.

3. **Redirect-cascade Zenodo-mint timing rule (§5 candidate 3):** PROMOTE WITH MODIFIED TEXT — the "mint at FIRST submission" framing is right but the version-DOI semantics need to be explicit. Refined text:

   > "When a manuscript enters a redirect cascade (rejection → next venue), the Zenodo concept-DOI MUST be minted no later than the SECOND submission, with v1.0 = first submitted version (anonymized). Each subsequent venue submission corresponds to a new version-DOI under the same concept-DOI, preserving cascade lineage as a queryable version history. If the manuscript is substantively reframed across cascade hops (e.g., new theorem statement, new title), document the reframing in the version-DOI metadata description field."

   Confidence 0.80. Item 28 is the canonical violation that motivated the rule.

---

**END VERDICT 214.** Absorption target: bridge slot `T1-SYNTH-VERDICT-214-ZENODO-COVERAGE-GAP-ABSORPTION`. Pre-absorption operator action: run G5 Zenodo `/me/uploads` audit to retire 0.75 confidence residual on Items 5/13/28 true-coverage gap; substrate-prep for 5/15 bundle proceeds in parallel pending that audit.
