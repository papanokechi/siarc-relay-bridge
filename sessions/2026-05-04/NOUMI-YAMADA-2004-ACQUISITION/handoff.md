# Handoff — NOUMI-YAMADA-2004-ACQUISITION

**Date:** 2026-05-04
**Agent:** GitHub Copilot (VS Code, Claude Opus 4.7 xhigh)
**Session duration:** ~75 minutes
**Status:** PARTIAL (best-OA-route exhausted; ILL recommended)

## What was accomplished

Probed 8 OA routes for Noumi 2004 "Painlevé Equations through
Symmetry" (AMS MMONO/223). The book itself is paywalled at $155 with
no Internet Archive / HathiTrust borrow path located, but the AMS
digital TOC was retrieved and reveals **no chapter dedicated to
Painlevé III** (8 chapters, all on Bäcklund / τ-functions / Jacobi-
Trudi / Lax — A-type focus). Three NY-family Tier-2/3 OA preprints
were acquired and full-text-searched: KNY 2017 (arXiv:1509.08186, 168
pp), NY 1998 (arXiv:math/9804132, 16 pp), NY 2000 (arXiv:math/0012028,
31 pp). Across all three sources, the explicit W(B_2) ↔ W((2A_1)^(1))
homomorphism is **not stated**. Verdict: UPGRADE_NY04_NIA_ILL_
RECOMMENDED with strong predicted-absence inference (NY 2004 is
unlikely to contain the bridge given the TOC and its 2017-review
companion does not).

## Key numerical findings

- AMS MMONO/223: 156 pp, 2004, DOI 10.1090/mmono/223, $155 paywall,
  eBook ISBN 978-1-4704-4647-5; 8 chapters, none PIII-dedicated.
- KNY 2017 (slot 14, sha256=7CD884617FC8F17E430DEAF0520148362E1871CAFB
  8F8471B462029CBE387DDE): 168 pp; covers PIII6/PIII7/PIII8 in Sakai
  surface-classification framework (sec.8.6.16); contains 0
  occurrences of "B_2" / "B(2)" as Lie-group symbol.
- NY 1998 (slot 15, sha256=32424FE6CC4FCEC386A0D2C1733F40CDED52AE5E29
  5AC344DC8B5E2A79F58524): 16 pp, CMP 199 (1998) 281-295; lists PIII
  in passing (line 25) but develops only A_l^(1) construction.
- NY 2000 (slot 16, sha256=75698AFB6AF9D593DEA674CACF1CA6F40CFCC067E2
  9941ACD17472754E4EAAF3): 31 pp; abstract Weyl-action framework;
  worked example W(G_2) only; no PIII / B_2 / 2A_1 specialization.
- 13 AEAL claims appended to claims.jsonl.

## Judgment calls made

1. **Prioritized KNY 2017 over Witte-Forrester 2010.** Spec §6 Phase
   D.6 listed both as follow-on candidates for the absence path. KNY
   2017 was prioritized because (a) all three principal authors of NY
   2004 are co-authors, (b) it post-dates NY 2004 by 13 years and
   would absorb any homomorphism that the book contained, (c) it is
   the canonical comprehensive review (168 pp, 142 references). If
   the bridge is absent in KNY 2017, it is overwhelmingly likely
   absent in NY 2004 too. Witte-Forrester 2010 is recommended as the
   next probe (Prompt 030 candidate) but was deferred for budget.
2. **Did not download q-alg/9708018** ("Symmetries in PIV and Okamoto
   polynomials"). Spec §1 Tier-2 listed math/9806032, but that ID is
   actually Schlichenmaier's Sugawara construction (correction logged
   to discrepancy_log.json / unexpected_finds.json). The correct NY
   PIV paper is q-alg/9708018, which is PIV-focused (W(\tilde A_2))
   and would not contain a PIII W(B_2) bridge. Skipped to budget.
3. **Did not auth-fetch HathiTrust full-view.** Per Rule 2 (no
   on-behalf auth), HathiTrust full-view of MMONO/223 (which depends
   on US institutional partner status) is operator-side action.
4. **Did not pursue J-STAGE / Sūgaku / RIMS preprints.** Per spec §2
   Phase B.6/B.7 these were optional sub-routes; NY's preferred
   deposition channel was arXiv, so these slots are redundant.
5. **Verdict ladder: chose UPGRADE_NY04_NIA_ILL_RECOMMENDED rather
   than UPGRADE_NY04_PREPRINT_SURROGATE_W_HOMOMORPHISM_NOT_IN_NY04.**
   The latter applies if the book *was acquired*; we did not breach
   the AMS paywall, so the strict ladder reading is "NIA + ILL". The
   absence-of-homomorphism finding from preprints (slots 14/15/16) is
   a *predictive* signal that strengthens the ILL recommendation but
   does not by itself qualify as a NY-2004-acquired outcome.

## Anomalies and open questions

**THIS IS THE MOST IMPORTANT SECTION — please read carefully.**

### Anomaly 1: NY 2004 has no PIII chapter (spec assumption falsified)

Spec §0 stated NY 2004 "contains a dedicated chapter on PIII / PIII'
with explicit generators in *both* conventions and typically an
explicit bridge proposition / corollary." The AMS digital TOC
falsifies this: 8 chapters, all on the τ-function / Bäcklund /
Lax-formalism unified A-type framework, with NO PIII chapter. The
AMS abstract explicitly states the worked examples are "especially
those of types II and IV." This significantly lowers the prior
probability that NY 2004 contains the W(B_2) ↔ W((2A_1)^(1))
homomorphism (estimated <20%).

This may indicate the spec author's memory of NY 2004 contents was
actually a memory of the related Noumi-Yamada line of papers (which
the book elaborates) or of the more recent KNY 2017 review (which
DOES cover PIII6/PIII7/PIII8 surface types — but not in W(B_2)
language).

### Anomaly 2: KNY 2017 contains 0 occurrences of "B_2" as Lie group

The 168-page KNY 2017 review by all three NY-circle principal authors
does NOT use the symbol W(B_2) anywhere (only stray hit is journal
name "Phys. Lett. B 236" in citation [7]). It works entirely in the
Sakai surface-classification convention (W((2A_1)^(1)) on D_6^(1) for
PIII6, etc.) and cites Okamoto's W-symmetry observation but does NOT
retrace the Okamoto-→-Sakai translation.

**Interpretation:** the W(B_2) ↔ W((2A_1)^(1)) bridge appears to be
folklore-Lie-theory that has never been written out as a theorem in
the PIII context within NY-circle literature. Two routes to close
M6 Phase B.5 properly:

- (a) Probe pre-Sakai Okamoto-circle literature (Umemura, Watanabe,
  Tsuda — separate Researcher prompt) for explicit W(B_2) →
  W((2A_1)^(1)) translation. May not exist.
- (b) SIARC primary derivation: write out the homomorphism from the
  Cartan-matrix data of B_2 ([[2,-1],[-2,2]]) and (2A_1)^(1)
  (decoupled rank-2 affine A_1 ⊕ A_1 = [[2,-2],[-2,2]] ⊕ [[2,-2],[-2,2]])
  and verify the Tits relations. This is folklore but produces a
  citable statement under SIARC authorship.

### Anomaly 3: Sakai Table 6 framework has effectively replaced W(B_2)

Post-2001 PIII research (slots 08, 13, 14) appears to have abandoned
the Okamoto W(B_2) framing entirely in favor of the Sakai
W((2A_1)^(1)) on D_6^(1) framing. The two are presumably equivalent
up to a folklore homomorphism, but the equivalence is not stated as a
theorem in the post-Sakai literature. This is a literature-historical
finding worth noting in the v1.18 picture amendment cycle.

### Anomaly 4: Spec arXiv-ID typo

Spec §1 Tier-2 list: "math/9806032" → actual NY-PIV paper is
q-alg/9708018. math/9806032 is Schlichenmaier 1998 Sugawara
construction. Substantive impact: zero.

### Open questions for Claude review

- Q1: Should M6 spec Phase B.5 W cross-walk anchor be re-scoped
  from "find theorem-grade primary citation" to "SIARC primary
  derivation under SIARC authorship"? The literature audit suggests
  the former path may not be feasible.
- Q2: Is Witte-Forrester 2010 (J.Phys.A 43, 235202) worth a separate
  Researcher prompt for the τ-function PIII anchor, or is the v1.18
  picture better served by re-firing the SIARC primary derivation
  path?
- Q3: Does the post-Sakai literature pattern (W((2A_1)^(1)) replaces
  W(B_2) without an explicit translation theorem) warrant a v1.18
  picture amendment noting the historical-equivalence-as-folklore
  status of M6 Phase B.5?

## What would have been asked (if bidirectional)

- "Spec says NY 2004 has a dedicated PIII chapter with both
  conventions; AMS TOC shows no PIII chapter. Should I still try to
  ILL the book, or pivot directly to Witte-Forrester 2010 / SIARC
  primary derivation?"
- "Sakai 2001 + KNY 2017 work entirely in W((2A_1)^(1)) without
  retracing the W(B_2) → W((2A_1)^(1)) translation. Should I derive
  the bridge directly from Cartan-matrix data instead of continuing
  the literature hunt?"
- "Should the spec arXiv-ID typo (math/9806032 → q-alg/9708018) be
  patched in the spec template before the next prompt fires?"

## Recommended next step

**Prompt 030 candidate (recommended):** WITTE-FORRESTER-2010-PROBE.
J.Phys.A 43 (2010) 235202, "Application of the τ-Function Theory of
Painlevé Equations to Random Matrices: PIII", 40+ pp, OA via arXiv
math-ph/0103025 (PIV/PII version) + a separate 2010 PIII follow-on
paper. This is the next-most-likely source for the W cross-walk in
the τ-function framework; if it also lacks the bridge, M6 Phase B.5
should be re-scoped to a SIARC primary derivation.

**Alternative Prompt 030 candidate:** SIARC-PRIMARY-W-B2-2A1-
HOMOMORPHISM-DERIVATION. Direct Cartan-matrix-level derivation
producing a citable theorem statement under SIARC authorship; bypasses
the literature hunt entirely. ~2-3 hr Researcher prompt with
verification on a Lie-theory CAS (sympy abstract algebra module or
GAP).

**Operator-side action recommended:**
- ILL of NY 2004 from Yokohama City Library (proximity), University
  of Tokyo Math Library, Kobe University Math Library, or RIMS Kyoto.
- HathiTrust full-view check (if institutional partner status is
  available).

## Files committed

- prompt_spec_used.md (spec stub; full prompt text in operator chat log)
- route_findings.md (Phase B 8-route probe log + summary table)
- absence_audit.md (Phase D readback; verbatim grep evidence; M6
  Phase B.5 implication)
- claims.jsonl (13 AEAL entries)
- halt_log.json (empty `{}`)
- discrepancy_log.json (empty `{}`)
- unexpected_finds.json (4 anomalies logged)
- handoff.md (this file)

Plus literature/g3b_2026-05-03/ slots (deposited at workspace
location, NOT inside this session folder per literature/ convention):
- 14_kajiwara_noumi_yamada_2017_geometric_aspects.pdf (3.2 MB)
- 14_kajiwara_noumi_yamada_2017_geometric_aspects.txt (650 KB)
- 15_noumi_yamada_1998_affine_weyl_dynamical.pdf (200 KB)
- 15_noumi_yamada_1998_affine_weyl_dynamical.txt (53 KB)
- 16_noumi_yamada_2000_birational_weyl_nilpotent.pdf (290 KB)
- 16_noumi_yamada_2000_birational_weyl_nilpotent.txt (88 KB)
- SHA256SUMS.txt updated with slot 14/15/16 entries

## AEAL claim count

13 entries written to claims.jsonl this session.
