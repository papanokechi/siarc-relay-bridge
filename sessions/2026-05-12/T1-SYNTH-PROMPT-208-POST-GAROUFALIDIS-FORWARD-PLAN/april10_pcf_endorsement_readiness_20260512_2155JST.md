# APRIL-10 PCF PAPER — ENDORSEMENT-READINESS STATUS CHECK — 2026-05-12 ~21:55 JST

**Paper:** "Polynomial Continued Fractions: a Proved Logarithmic Ladder, a 4/π Casoratian Identity, and 482 Irrational Constants" (April 10, 2026, v1)
**Trigger:** External reviewer (3rd 3rd-party input of the night, 21:48 JST) recommended this paper as the strongest single arXiv math endorsement candidate; operator requested "help check status"
**Agent:** GitHub Copilot CLI (claude-opus-4.7-xhigh)
**Anchor:** bridge HEAD `e74c47c` (corpus-review append)

═══════════════════════════════════════════════════════════════════════════════

## TL;DR

**Reviewer's recommendation is sound** — this paper is genuinely the strongest single endorsement candidate in the corpus. However, **endorsement-readiness is currently BLOCKED by three concrete defects** that an endorser will hit within minutes of clicking through. **Do not fire any endorsement quest for this paper until D1 + D2 are fixed.**

| | Finding |
|---|---|
| Reviewer's verdict | CONFIRMED — strongest endorsement candidate |
| Endorsement-ready today? | **NO** |
| Blocking defects | D1 broken reproducibility link (CRITICAL) + D2 Zenodo abstract rendering bug (HIGH) |
| Estimated remediation effort | 1-2 hours of operator work |

═══════════════════════════════════════════════════════════════════════════════

## A. PAPER IDENTIFICATION

| Field | Value |
|---|---|
| Title (canonical) | Polynomial Continued Fractions: a Proved Logarithmic Ladder, a 4/π Casoratian Identity, and 482 Irrational Constants |
| Deposit date | 2026-04-10 |
| Zenodo concept-DOI | `10.5281/zenodo.19491767` |
| Zenodo version-DOI (v1) | `10.5281/zenodo.19491768` |
| File md5 | `70151855c854c58643886cbed53f1c89` (422.1 kB) |
| Manuscript .tex | `tex\pcf_unified_arxiv.tex` (local) + `tex\submitted\pcf_unified_expmath_submission.tex` (ExpMath variant) |
| arXiv status | **NOT STAGED** (no arXiv ID; never submitted) |

═══════════════════════════════════════════════════════════════════════════════

## B. SUBMISSION HISTORY

| # | Venue | Submitted | Outcome | Notes |
|---|---|---|---|---|
| Submission_log item 2 | Zenodo | 2026-04-10 | Published (concept 19491767 / v1 19491768) | open access |
| Submission_log item 7 | Experimental Mathematics | 2026-04-18 (sub ID 266999523) | **REJECTED** | ExpMath now blacklisted in venue matrix |

**Key implications:**
- Paper is NOT under any active journal review (Q-208-2 simultaneous-submission rule trivially satisfied)
- Paper has NOT been arXiv-staged — this is precisely the reviewer's recommended target
- ExpMath rejection is on record but does NOT preclude arXiv staging
- This paper is independent of the R4 JNT submission fired this evening (R4 = Spectral Classes, Item 16, JNTH-D-26-00612 — different paper)

═══════════════════════════════════════════════════════════════════════════════

## C. WHY THE REVIEWER'S RECOMMENDATION IS SOUND (verification)

Cross-checked reviewer's claims against the actual Zenodo deposit:

| Reviewer claim | Verification |
|---|---|
| Self-contained, readable cold by analytic number theorist | ✅ Confirmed — abstract proves two convergence theorems + cites Gauss/Brouncker only; no SIARC vocabulary |
| Two convergence theorems | ✅ PCF(−kn², (k+1)n+k) → 1/ln(k/(k−1)) for k>1 + PCF(−n(2n−3), 3n+1) → 4/π |
| Discrete Casoratian telescope method | ✅ "combination of closed-form convergents and a discrete Casoratian telescope" — verbatim in abstract |
| Explicit error rate O(2⁻ᴺ/N^(7/2)) | ✅ In abstract (though math-rendered as "O(2−N/N7/2)" due to defect D2 below) |
| 482 constants, Arb at 10,000-bit, depth N=5000 | ✅ All present in abstract verbatim |
| 1500+ correct digits + rigorous irrationality | ✅ Verbatim |
| 2F3 over ℚ(√5) obstruction proving 4/π not Gauss ₂F₁ | ✅ Verbatim |
| No private SIARC vocabulary | ✅ Confirmed — no V0/cascade/M-axis/RULE 1 jargon anywhere |
| Classical literature positioning (Gauss, Brouncker) | ✅ Both named in abstract |

**The mathematical content is exactly as the reviewer described.** This paper does not suffer from the jargon-density / RULE-1 visibility / cascade-vocabulary defects that affect umbrella v2.2, PCF-2, Channel Theory, etc.

═══════════════════════════════════════════════════════════════════════════════

## D. CRITICAL DEFECTS BLOCKING ENDORSEMENT-READINESS

### D1 [CRITICAL] — Broken reproducibility link

Zenodo description states verbatim: *"Code and verification scripts available at https://github.com/papanokechi/pcf-research"*

What the endorser will actually find by clicking that link:

- **pcf-research** repo README at root lists 4 "Key scripts": `g01_lemma_k_diagnosis.py`, `dichotomy_d34_scan.py`, `vquad_heun_connection_check.py`, `generalized_dichotomy_scan.py`
- **GitHub code-search across the entire pcf-research repo for `g01_lemma_k_diagnosis` returns ZERO matches.**
- All four named scripts are absent. The repo's subdirs (area2/channel/pcf2/vquad) contain different scripts for different papers.

**The actual reproducibility scaffold for this paper exists** — but at a different path:

- **Local directory:** `C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\pcf-casoratian-identities\`
- **NOT git-tracked** (no `.git/`)
- **NOT published to GitHub** (`github.com/papanokechi/pcf-casoratian-identities` returns 404)
- **Contents:** `README.md` (3.4 KB, manuscript-titled), `src/casoratian_verifier.py` (4.9 KB), `src/pslq_search.py` (8.4 KB), `data/new_irrational_constants.csv` (45 KB), `data/new_irrational_constants.json` (128 KB), `requirements.txt`
- **README explicitly states:** *"Reproducibility scaffold for the manuscript 'Polynomial Continued Fractions: Proved Families, Casoratian Series Identities, and 482 New Irrational Constants'"*

**Severity:** an endorser performing the standard 15-minute due-diligence check will follow the Zenodo→GitHub link, find empty promises in the README, conclude the reproducibility claim is unsupported, and decline. **This is the single most-important defect.**

### D2 [HIGH] — Zenodo abstract rendering bug (confirmed verbatim)

Reviewer's flagged quote: *"computational application,wecertify482quadratic"*

Verified verbatim on the Zenodo page:

> "errorO(2−N/N7/2) for the resulting series. As**a**computationalapplication,wecertify482quadratic generalizedcontinued fractions against abasis of 15 standardconstants using Arbballarithmeticat10,000-bitprecisionanddepthN=5000."

Bug count: ~30+ missing inter-word spaces; math superscripts mangled (`O(2−N/N7/2)` should be `O(2^{-N}/N^{7/2})`); `\,` (thin space) and superscript-stripping during PDF→Zenodo metadata extraction.

**Severity:** signals carelessness to mathematical reviewers; reduces probability of an endorser engaging seriously with the abstract.

### D3 [LOW] — README cites version-DOI not concept-DOI

`pcf-research/README.md` cites `10.5281/zenodo.19491768` (version-DOI of v1) rather than `10.5281/zenodo.19491767` (concept-DOI). Per project's substrate-citation memory ("concept-DOI is the citation-stable identifier"), concept-DOI is preferred for cross-link integrity.

**Severity:** minor; both resolve to the same record. Easy fix during D1 remediation.

### D4 [LOW] — Missing Z?? slot in venue matrix TABLE 5

`PAPER_VENUE_LIKELIHOOD_MATRIX_20260512.md` TABLE 5 lists Z1-Z8 but does NOT list the April-10 pcf_unified paper, even though it predates all other PCF deposits. Suggested slot: **Z0** (or insert before Z1).

**Severity:** admin completeness; can be addressed in next venue-matrix update.

═══════════════════════════════════════════════════════════════════════════════

## E. RECOMMENDED REMEDIATION ORDER

**STEP 1 [CRITICAL, ~30-60 min] — Fix the reproducibility scaffold.**

Two options:

**Option α (cleaner):**
1. Initialize git in `pcf-casoratian-identities/`
2. Create public repo at `github.com/papanokechi/pcf-casoratian-identities`
3. Push README + src/ + data/ + requirements.txt + .gitignore
4. Verify repo is publicly accessible
5. Re-deposit Zenodo v2 with corrected URL in description: `github.com/papanokechi/pcf-casoratian-identities`

**Option β (faster, less clean):**
1. Copy `pcf-casoratian-identities/{README.md,src/,data/,requirements.txt}` into `pcf-research/casoratian/` or similar
2. Update `pcf-research/README.md` to point at the new subdirectory (correct script list)
3. Commit + push to existing `pcf-research` repo
4. Re-deposit Zenodo v2 with updated description (URL unchanged but description specifies the subdirectory)

**Drafter recommendation:** Option α — the paper-titled subject matches the repo name 1:1; gives clearest attribution.

**STEP 2 [HIGH, ~30 min] — Fix Zenodo abstract rendering.**

Re-deposit v2 with:
- Re-extracted abstract text (manually, from .tex source) with correct spacing and math symbols
- Updated GitHub URL (per Step 1)
- Optional: also fix the title-rendering bug if it propagates ("PolynomialContinuedFractions:" → "Polynomial Continued Fractions:")

Note: Zenodo's "publish new version" preserves concept-DOI but mints a new version-DOI. This is the standard reversible-amendment pattern; no risk to citation integrity.

**STEP 3 [LOW, ~5 min] — Update venue matrix TABLE 5.**

Insert new row Z0 in `PAPER_VENUE_LIKELIHOOD_MATRIX_20260512.md`:

| # | Manuscript | Concept-DOI | Latest version-DOI | Latest version | Notes location |
|---|---|---|---|---|---|
| Z0 | PCF unified (logarithmic ladder + 4/π + 482 constants) | 10.5281/zenodo.19491767 | 19491768 (or v2 post-D2-fix) | v1 or v2 | tex/pcf_unified_arxiv.tex; pcf-casoratian-identities repo |

**STEP 4 [DECISION GATE] — Endorsement quest.**

Only after STEPs 1-3 complete. Per project memory (endorsement quest discipline; post-031 verdict; bibliographic identifier pre-verification): every prospective endorser must be substrate-verified against framing-overlap before fire.

═══════════════════════════════════════════════════════════════════════════════

## F. RULE 1 + PACING-FLAG INTERACTION

| Step | RULE 1 classification | Pacing-flag (Q-208-4) interaction |
|---|---|---|
| STEP 1 publish reproducibility repo | **Foundational hygiene** (fixing broken claim) OR Distribution (making code public) — defensible either way; drafter scopes as foundational | Not a journal fire; pacing-clear |
| STEP 2 re-deposit Zenodo v2 | Distribution (amendment-grade) | Not a journal fire; pacing-clear |
| STEP 3 update venue matrix | Internal admin (no public release) | N/A |
| STEP 4 endorsement quest | Distribution (arXiv staging) | Not a journal fire (arXiv is staging not submission); pacing-clear |

**Net:** none of Steps 1-4 are RULE-1-blocked under the foundational-hygiene scoping of Step 1. Even under conservative distribution-class scoping, the operator's existing endorsement-related operational work (Q-208-3 γ Carneiro fire tomorrow) demonstrates this category is already in active execution.

═══════════════════════════════════════════════════════════════════════════════

## G. INTERACTION WITH TONIGHT'S THREE OTHER INTAKE STREAMS

| Intake stream | Interaction with this paper |
|---|---|
| Verdict 208 forward plan | R4 (JNT, Spectral Classes) is a DIFFERENT paper, not this one. This paper is independent. Carneiro cs.LO fire (Q-208-3 γ) is independent. T2B framing decision is independent. |
| Journey-pivot intake brief | This paper would be a strong S2 anchor-paper candidate (sharper-review): "Write one anchor paper per program optimized for outside readers" — this paper ALREADY IS that anchor paper. No new drafting needed; just remediation + staging. |
| Two-part corpus review | Reviewer 1 said this paper "anchors the empirical PCF program" — confirmed. Reviewer 2 (sharper assessment) said *"For PCF, this would be a 25-35 page paper that states the five-stratum classification theorem..."* — different content, but this paper serves the same anchor-role function for the empirical / pre-stratification thread. |

**Net:** this paper is the natural execution path for tonight's converging recommendations from three independent intake streams. Reviewer's recommendation is the operator's lowest-friction next step.

═══════════════════════════════════════════════════════════════════════════════

## H. DRAFTER SUMMARY ASSESSMENT

**The reviewer correctly identified the strongest endorsement candidate in the corpus.** Mathematical content is exactly as described: self-contained, classically-positioned, theorem-bearing, falsifiable, empirical-result-equipped, jargon-free.

**However, the paper is not currently endorsement-deliverable** due to two concrete defects an endorser will hit immediately. Both are fixable in 1-2 hours of operator work.

**Single highest-priority action:** **STEP 1 publish `pcf-casoratian-identities` to GitHub** (Option α recommended). Without this, every other downstream action (Zenodo amendment, arXiv staging, endorsement-quest fire) is wasted because the reproducibility link will remain broken.

**Operator pacing observation:** It is 21:55 JST and operator declared "last action for today" at 19:51 JST. The status check itself is finished (this document). **STEP 1 should NOT be attempted tonight** — git-init + GitHub-create + push + Zenodo-re-deposit during fatigue carries unacceptable risk of stray-commit / wrong-DOI / metadata-error mistakes. Recommended: schedule STEP 1 for tomorrow alongside other verdict-208 actions.

═══════════════════════════════════════════════════════════════════════════════

## I. AGENT STATE CHANGES

- File saved: `tex/submitted/control center/notes/APRIL10_PCF_PAPER_ENDORSEMENT_READINESS_20260512.md` (this document)
- Bridge mirror: `siarc-relay-bridge/sessions/2026-05-12/T1-SYNTH-PROMPT-208-POST-GAROUFALIDIS-FORWARD-PLAN/april10_pcf_endorsement_readiness_20260512_2155JST.md`
- SQL todos inserted:
  - `april10-pcf-step1-publish-casoratian-repo` (PENDING, CRITICAL)
  - `april10-pcf-step2-zenodo-v2-redeposit` (PENDING, HIGH, gated on STEP 1)
  - `april10-pcf-step3-venue-matrix-z0-row` (PENDING, LOW)
  - `april10-pcf-step4-arxiv-stage-endorsement-quest` (BLOCKED on STEPS 1-2)
- No fires triggered. No verdict status change.

═══════════════════════════════════════════════════════════════════════════════

**End status check.**
