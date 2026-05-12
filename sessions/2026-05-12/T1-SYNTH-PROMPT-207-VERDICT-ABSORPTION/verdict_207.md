# T1-Synth Verdict — PROMPT 207
## Tunnell CNP arXiv Endorsement Attractiveness Consultation

Issued: 2026-05-12 (claude.ai, Opus-class compute)
Substrate received: paper abstract + intro excerpt + contributions list + 12-candidate shortlist + venue history (operator-disclosed, endorser-invisible)
Scope: STRATEGIC pre-flight; arXiv endorsement = category-appropriateness gate, NOT peer review

---

## A. SECTION-(i) — ATTRACTIVENESS VERDICT

### Intrinsic-attractiveness score

**7.5 / 10** — Confidence band: **MEDIUM-HIGH**

**Rationale.** The paper is well-targeted for cs.LO on the dimensions an endorser actually evaluates. The arXiv endorsement criterion is "is this paper appropriate for the category" — not "is this novel mathematics." On that bar, the paper presents strongly: a concrete Lean 4 artifact (954 lines, zero `sorry`), a clearly articulated methodological contribution (the three-level `opaque`/`def`/`axiom` architecture for axiom isolation), a candidate Mathlib upstream lemma, and a Python-validated test suite against an external gold standard (OEIS A003273). The abstract leads with verifiable engineering facts rather than mathematical novelty claims, which is exactly the register cs.LO endorsers expect. The intro explicitly names the target community (ITP/CPP) and frames the contribution honestly as architecture rather than new mathematics — this is a maturity signal that reduces endorser hesitation.

The 2.5-point haircut from a 10 reflects three friction points an endorser would notice in a 5-minute skim: (1) the abstract's "key contributions" sentence is dense and somewhat list-like, masking the strongest single hook (axiom isolation as a portable pattern); (2) the paper's venue history is invisible to endorsers, but the *length* (~50pp) is visible from the PDF and may register as "long for what is being claimed" without a structural justification visible up front; (3) the "axiom-isolation pattern" claim is the paper's most portable contribution but is currently competing for attention with four other contributions in the bulleted list, weakening the methodological-pitch surface area.

The venue rejection chain (FAC defunct / JAR ×2 length / AFM 8-min board snap) is essentially **orthogonal** to endorser perception. JAR length-rejection is a journal-policy issue not detectable from the abstract. AFM's snap-reject pattern (EiC bypass of subject editor) is a venue-governance artifact, not a paper-quality signal an endorser would replicate. An endorser reading only the abstract and intro would have no reason to suspect this rejection history exists.

### Top revision recommendations (each ≥+1 point lift)

**R1. Lead-sentence rewrite in abstract — site: abstract opening — delta: +1.0**
Current opening leads with "954-line Lean~4 formalization of the combinatorial and structural backbone." Recommend reframing to lead with the methodological contribution: something like "We present a three-level architecture (`opaque`/`def`/`axiom`) for formalizing theorems conditional on open conjectures in Lean 4, demonstrated on a 954-line zero-`sorry` formalization of the combinatorial backbone of Tunnell's criterion for the congruent number problem." This shifts the perceived contribution from "we formalized X" (which invites the question "why is this new?") to "we propose a pattern, here's its first application" (which invites the question "where else does it apply?" — a much more endorser-friendly frame).

**R2. Move axiom-isolation pattern to first-position contribution — site: contributions list — delta: +0.5–1.0**
The contributions list currently leads with "Axiom-isolation pattern" already (good) but its description is one sentence; expand to two with an explicit forward-reference to other conjecture-conditional theorems (Riemann Hypothesis, Generalized Lindelöf, BSD itself in other contexts). Endorsers in the Mathlib ecosystem care about *portable patterns*; the more clearly this is signaled as a pattern with a worked example rather than an isolated formalization, the more endorser-comfortable the ask becomes.

**R3. README front-matter on GitHub — site: repo README — delta: +1.0**
Endorsers commonly skim the GitHub repo before responding. If the README's first 200 words don't include (a) the zero-`sorry` count, (b) the single named axiom, (c) the test-suite size + OEIS validation scope, and (d) a 5-line code snippet of the axiom-isolation pattern, add them. This is the lowest-cost, highest-leverage change — the README is a separable artifact that endorsers consult independently of the paper PDF. Estimated implementation cost: 30 minutes.

### Decision call

**PROCEED_AFTER_REVISIONS**

Rationale: the paper is already above the threshold where endorsement asks are reasonable to send (≥7.0), but R1+R3 are cheap (≤2 hours combined) and would lift the score to ~9.0, materially improving response rates from the top tier. R2 is optional. Do not let R-revisions stall the campaign for more than 48 hours; the cs.LO endorsement gate is a structural blocker on the LMCS venue route and on any future cs.LO submissions.

---

## B. SECTION-(ii) — PER-CANDIDATE RECEPTIVITY TABLE

| # | Candidate | Score | Band | Rationale | CoI Flag | Recommended Ask-Framing Angle |
|---|---|---|---|---|---|---|
| C1 | Asperti (Bologna) | **3.5** | HIGH | Already in flight on JFR pre-query; asking for arXiv endorsement on top of an open JFR negotiation creates an unnecessary multi-channel ask that risks both. Wait for JFR verdict floor (2026-05-29) before any endorsement ask. | ⚠️ Active JFR pre-query open; dual-role conflict if asked simultaneously | **DEFER UNTIL JFR VERDICT.** If JFR routes are eventually declined, he becomes a reasonable Tier-2 candidate (~6.5). |
| C2 | Buzzard (Imperial) | **6.5** | MEDIUM-HIGH | Strong topical fit (CNP is canonical NT, and his Xena Project amplifies exactly this kind of result). However, very high inbound volume and a known pattern of selective response. Decisive if positive, but probabilistic. | None | Lead with "axiom-isolation pattern" as portable methodology aligned with FLT4's own axiom boundary; 3-sentence cover max; include 10-line Lean snippet of `tunnell_conditional_on_BSD` definition. |
| C3 | Avigad (CMU) | **7.0** | MEDIUM-HIGH | Single best match between the paper's methodological framing and a known endorser's published views on formalization principles. His written work on "what formalization is for" maps almost 1:1 to the paper's design philosophy. | None | Lead with meta-pattern (axiom isolation as general technique); cite his own writing on formalization principles in the cover paragraph. |
| C4 | Massot (Paris-Saclay) | **6.5** | MEDIUM | Mathlib gatekeeper; receptive to outside-cluster contributors with concrete Mathlib-quality code. Slightly outside his core area (geometric topology) but the involution-lemma upstream-candidate angle is exactly his lane. | None | Lead with `card_even_of_involution` as Mathlib-upstream candidate; include the lemma source verbatim; mention it builds on Mathlib idioms. |
| C5 | Macbeth (Fordham) | **6.5** | MEDIUM | Strong public pattern of mentoring formalization outsiders; lower inbound volume than Tier-1 names. Field mismatch is real but her engagement pattern compensates. | None | Mathlib-upstream pitch + explicit "I'm an independent researcher without institutional Lean contacts" framing — her published behavior suggests this is a positive signal, not a negative. |
| C6 | Carneiro (CMU) | **7.5** | MEDIUM-HIGH | Single highest "decisive-verdict-on-code-quality" probability. He would form a fast judgment by reading the Lean source directly. If the code is as clean as the paper claims, he is the highest-probability YES in the table. | None | Code-first framing: 2-sentence cover, 30-line Lean excerpt of involution lemma + axiom definition in email body, link to repo. Minimize prose. |
| C7 | van Doorn (Bonn) | **6.0** | MEDIUM | Mathlib core; HoTT-trained perspective would engage with axiom-boundary architecture. Solid general fit, no specific topical hook. | None | Mathlib-upstream + axiom-isolation pattern; mention HoTT-adjacent treatments of opaque definitions as conceptual cousin. |
| C8 | Hölzl (VU Amsterdam) | **5.5** | MEDIUM | Cross-system perspective is genuinely useful but creates a longer evaluation path (he'd want to think about Isabelle-translatability). Likely respondent but slower decision. | None | Cross-system framing: "does this axiom-isolation pattern translate to Isabelle's locale/sublocale machinery?" — invites engagement rather than yes/no. |
| C9 | Baanen (VU Amsterdam) | **6.0** | LOW-CONFIDENCE-MEDIUM | Mathlib-active, less public profile, possibly faster-responding. Lower inbound suggests higher response probability conditional on contact. | None | Standard Mathlib-upstream pitch; no special framing needed. |
| C10 | Paulson (Cambridge) | **5.0** | MEDIUM | Very senior, high-volume inbound, will judge against Isabelle/AFP precedent. If positive, decisively positive. If silent, no signal. Lower probability per-ask than C2-C6. | None | Cross-system + classical-mathematics framing; reference his prime-number-theorem or Gödel formalization as precedent for "classical theorem, conjectural component" pattern. |
| C11 | Cremona (Warwick) | **6.0** | MEDIUM | Perfect math.NT topical fit but not a cs.LO author. Useful for math.NT cross-list endorsement *after* cs.LO primary lands, not before. | Limited cs.LO submission history — he may not have cs.LO endorsement privileges; **operator should check his arXiv submission record before contacting.** | OEIS A003273 + LMFDB framing; ask for math.NT cross-list endorsement only, not cs.LO primary. |
| C12 | Cohen (Bordeaux) | **2.0** | HIGH | Listed as R4 JNT suggested reviewer on a live submission (LIVE FIRE 2026-05-12). Contacting him for endorsement within the same week is a clear conflict. | ⚠️⚠️ R4 JNT suggested reviewer — DO NOT CONTACT until R4 verdict in. | **BLOCKED — DO NOT CONTACT.** Revisit after R4 verdict (≥4-6 weeks). |

### Ranked priority order

**Round 1 — Top 3 (initial dispatch, week 0):**
1. **C6 Carneiro** (7.5) — highest single decisive-yes probability; code-quality verdict
2. **C3 Avigad** (7.0) — best methodological-framing match; published views align
3. **C2 Buzzard** (6.5) — high-amplification if yes; topical resonance

Rationale for top-3 composition: these three represent three orthogonal endorsement-grant rationales (code quality / methodology / topical interest). If any one says yes, the others become irrelevant. Sending to all three in parallel costs nothing additional and triples coverage.

**Round 2 — Next 3 (week 2 if round 1 silent):**
4. **C4 Massot** (6.5) — Mathlib gatekeeper; involution-lemma pitch
5. **C5 Macbeth** (6.5) — known outsider-mentor pattern
6. **C7 van Doorn** (6.0) — Mathlib core, HoTT angle

**Round 3 — Backup (week 4 if rounds 1-2 silent):**
7. **C9 Baanen** (6.0) — lower-profile, possibly faster
8. **C8 Hölzl** (5.5) — cross-system framing
9. **C10 Paulson** (5.0) — senior cross-system

**Skip / defer:**
- **C1 Asperti** — DEFER until JFR verdict
- **C11 Cremona** — math.NT cross-list only, AFTER cs.LO primary lands
- **C12 Cohen** — BLOCKED until R4 JNT verdict

---

## C. SECTION-(iii) — STRATEGY OVERLAY

### Primary category recommendation

**cs.LO PRIMARY, math.NT cross-list.**

Rationale: the paper's stated target venue is the ITP/CPP community; the contribution is explicitly framed as formalization architecture rather than new mathematics; the artifact is a Lean 4 codebase. All of these are cs.LO signatures. The mathematical content (CNP, Tunnell's criterion) is the *substrate* for the architectural contribution, not the contribution itself — this is the correct posture for cs.LO primary. The math.NT cross-list captures the topical hook for the elliptic-curves community and increases discoverability for the Cremona-style reader who would recognize the OEIS A003273 validation.

**Do NOT target math.LO primary.** Math.LO is for mathematical logic in the model-theoretic / proof-theoretic / set-theoretic sense; this paper is closer to applied formalization than pure logic, and math.LO endorsers would correctly redirect to cs.LO.

### Cross-listing recommendation

Include math.NT as cross-list on initial submission. Do NOT include math.LO. Optionally include cs.PL (programming languages) if the paper is later expanded to discuss the Lean 4 elaboration of the `opaque`/`def`/`axiom` mechanism in implementation terms; currently the paper doesn't lean enough on cs.PL territory to justify it.

### 14-day cadence dispatch sequence

- **Day 0:** Send R1+R3 revisions first (≤48h work). Do NOT dispatch endorsement asks until R3 (README front-matter) is live, since endorsers will scroll the repo.
- **Day 2-3:** Dispatch parallel asks to C6 Carneiro, C3 Avigad, C2 Buzzard. Three separate emails, not a CC; each tailored to the framing angle in the table.
- **Day 14:** If silence from all three, dispatch round 2 (C4, C5, C7).
- **Day 28:** If still silent, dispatch round 3 (C9, C8, C10).
- **Day 42:** If still silent, re-evaluate. Possible signals: (a) cover-paragraph weak — request CLI redraft; (b) wrong category — re-target; (c) operator-verification issue with emails — re-verify all addresses.

The 14-day gap is intentional. Sending all 9 candidates simultaneously would burn the candidate pool; sending one-at-a-time would extend the timeline to 6+ months. Parallel-batches-of-three is the right balance.

### Interaction with DS873D math.NT chain

**Structurally orthogonal — safe to run simultaneously.** Two reasons:

1. **Different categories.** DS873D is a math.NT endorsement for PCF-1 v1.3. The Tunnell CNP cs.LO endorsement is a different category, different paper, different code. arXiv endorsement codes are paper-scoped or category-scoped (depending on user-status); a math.NT endorsement does not unlock cs.LO submissions.

2. **Different candidate pools with minimal overlap.** The only overlap candidates between the DS873D pivot list (Zudilin / Mazzocco / Garoufalidis) and this Tunnell endorser shortlist would be C11 Cremona and C12 Cohen on the math.NT side. Cremona is recommended for Tunnell math.NT cross-list, not cs.LO primary; Cohen is blocked anyway. So no candidate is being asked twice within a short window.

**Caveat:** if a single endorser ends up redeeming both — e.g. if Mazzocco accepts DS873D and is also asked for cs.LO endorsement on Tunnell — this is fine *in principle* (endorsement is a routine metadata gate, not a reciprocal obligation) but should be sequenced with at least 30 days between asks for politeness. None of the current Tunnell shortlist overlaps with the DS873D pivot list, so this caveat is precautionary only.

---

## D. SECTION-(iv) — ANOMALIES + OPEN QUESTIONS

### Anomalies in the substrate

1. **Email verification gap.** Six of twelve candidate emails are flagged [NEEDS-VERIFY] or [PUBLIC-listed]; only C1 Asperti is [CONFIRMED-internal]. Per the project's bibliographic identifier pre-verification rule, operator must re-confirm every email before sending. Especially C6 Carneiro (no stable public email known) — this is a non-trivial lookup that should happen before the round-1 dispatch.

2. **Carneiro contact path is the weakest link in the round-1 dispatch.** He is the highest-receptivity candidate (7.5) but the email is the least verifiable. Recommend operator check (a) the Lean Zulip chat handle, (b) the recent Mathlib commit-author email, and (c) CMU directory before sending. If no verified address is found within 24h, replace C6 in round 1 with C4 Massot and demote C6 to round 2.

3. **Paper version flagged in repo (Zenodo 10.5281/zenodo.19834824) versus current main.tex.** The substrate cites the abstract verbatim from `main.tex` lines 83-111 but does not confirm whether the Zenodo deposit matches the current main.tex word-for-word. If endorsers click through to Zenodo and see an older version, the discrepancy could create friction. Operator should verify Zenodo = current HEAD before round-1 dispatch, or update the Zenodo deposit.

4. **Length signal not addressed in substrate.** ~50pp typeset is on the long end for what is structurally a single-result formalization paper. Endorsers will not reject on length (that's a journal concern), but they may form a "this is dense" impression that slows response. Not actionable in 48h; flag for future reference.

### Open questions

1. **Has the GitHub repo README been updated since the JAR R2 desk-reject?** R3 (README revision) is recommended either way, but the answer affects whether R3 is a fresh write or a targeted edit.

2. **What is the current Lean toolchain version pinned in the repo?** Endorsers in the Mathlib ecosystem check this within seconds. If the repo is pinned to a stale Lean 4 version (more than ~3 months behind Mathlib HEAD), this is a small but visible negative signal. Quick fix if so.

3. **Is there a CI badge visible in the README?** A green CI badge showing "Lean build passes, 0 sorry" is worth roughly +0.5 attractiveness on its own among Mathlib-ecosystem endorsers. Cheap to add if not present.

4. **Decision call on LMCS-route gating.** If operator decides LMCS is no longer the priority venue for Tunnell CNP (perhaps based on a different post-R4 strategy), the urgency of cs.LO endorsement drops substantially — the endorsement is still useful for future submissions but stops being a near-term blocker. This consultation assumed LMCS is on-route; if not, the decision call could shift from PROCEED_AFTER_REVISIONS to PROCEED_WITH_CAVEATS (lower priority, same plan).

5. **AEAL claim-flag on quantitative receptivity scores.** All 0-10 receptivity scores in Section B are best-estimates based on public research patterns and inbound-volume heuristics, not measured response rates. Per AEAL discipline: treat as ordinal rankings, not cardinal probabilities. The *order* of candidates is more reliable than the absolute scores.

---

**End verdict 207.**

No HALT conditions triggered. No hallucinated emails introduced (all email-verification status preserved from substrate; no new addresses fabricated). No new candidate endorsers introduced. All quantitative claims about candidate behavior are flagged as best-estimate per A7.
