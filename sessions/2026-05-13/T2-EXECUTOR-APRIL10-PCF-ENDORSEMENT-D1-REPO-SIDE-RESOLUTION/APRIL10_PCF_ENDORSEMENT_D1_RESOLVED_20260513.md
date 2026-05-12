# APRIL-10 PCF — ENDORSEMENT-READINESS D1 RESOLUTION (2026-05-13 ~07:40 JST)

**Status:** D1 (paper-side GitHub URL resolution + scripts-pointer)
RESOLVED via repo-side README work; NO Zenodo new-version mint required.

---

## A. Strategic pivot from prior plan

Last night's `RESUME_NEW_CLI_20260513_POST_ZENODO_INVENTORY.txt` listed
D1 as "April-10 PCF v2 Zenodo redeposit" with three patches bundled.
On closer inspection this morning the actual defect set decomposes into
two independently-actionable layers:

| Layer | Defect | Fix path | Action owner |
|---|---|---|---|
| Repo-side | GitHub URL `pcf-research` exists but README didn't surface verification scripts for the April-10 paper | Add `casoratian/` pointer + update top-level README | Agent — DONE this session |
| Repo-side | `pcf-casoratian-identities/README.md` cited "Experimental Mathematics, forthcoming" instead of Zenodo concept-DOI (anomaly A-STEP1-1) | Edit README to cite Zenodo concept-DOI 10.5281/zenodo.19491767 | Agent — DONE this session |
| Zenodo-side | Metadata abstract has rendering-bug spacing ("computational application,wecertify482quadratic") | Zenodo Edit form (preserves DOI; metadata-only edit) | Operator — PENDING |

The Zenodo metadata abstract fix is a metadata-only edit on the existing
record (no new-version mint, no paper-PDF rebuild). It does NOT require
operator to upload a new file; it preserves the DOI 10.5281/zenodo.19491768.

The paper PDF itself (`https://doi.org/10.5281/zenodo.19491768`) cites
`https://github.com/papanokechi/pcf-research` in its Data Availability
section (source.tex line 1366). That URL is now valid AND its README
now surfaces the verification scripts (via the new `casoratian/`
subdirectory pointer). Therefore **no PDF rebuild is necessary**.

## B. Actions completed this session

### B.1 — `pcf-research/casoratian/README.md` (NEW FILE)

Created stub pointer at https://github.com/papanokechi/pcf-research/blob/main/casoratian/README.md
Content: cites April-10 paper concept-DOI; points to dedicated companion
repo; explains the deliberate split between full SIARC research workspace
(pcf-research) and lightweight endorsement-ready package (pcf-casoratian-identities).

### B.2 — `pcf-research/README.md` (UPDATED)

Replaced the bare-Zenodo-link entry for the April-10 paper with a
structured block that:
  - Names the paper with full Zenodo-deposit title
  - Cites the concept-DOI `10.5281/zenodo.19491767` explicitly
    (preserving the version-DOI `19491768` as a parenthetical)
  - Links to the dedicated companion repo
  - Adds a `Subdirectories` section listing area2/channel/pcf2/vquad/casoratian
  - Preserves all prior content (Paper 14, key scripts, requirements, citation)

Commit: `8459b5d` (https://github.com/papanokechi/pcf-research/commit/8459b5d)
Branch: `main`

### B.3 — `pcf-casoratian-identities/README.md` (PATCHED)

Two surgical edits:
  - Title alignment: working title "Proved Families, Casoratian Series
    Identities, and 482 New Irrational Constants" → Zenodo-deposit canonical
    title "a Proved Logarithmic Ladder, a 4/π Casoratian Identity, and 482
    Irrational Constants"
  - Citation block: "Experimental Mathematics, forthcoming/submitted
    manuscript" → Zenodo concept-DOI `10.5281/zenodo.19491767` with full
    BibTeX entry; concept-vs-version DOI distinction explicitly noted

Commit: `1c0b37e` (https://github.com/papanokechi/pcf-casoratian-identities/commit/1c0b37e)
Branch: `main`

## C. Endorsement-readiness defect status table (post-this-session)

| Code | Description | Status |
|---|---|---|
| D1 | GitHub URL must resolve and README must point at verification scripts | **RESOLVED** (this session, repo-side) |
| D2 | Zenodo metadata abstract has rendering-bug spacing | OPERATOR-PENDING (Zenodo Edit metadata form) |
| A-STEP1-1 | Dedicated repo README cited "forthcoming" instead of Zenodo DOI | **RESOLVED** (this session, repo-side) |
| (D3, D4) | Lower-priority items from APRIL10_PCF_PAPER_ENDORSEMENT_READINESS_20260512.md | Unchanged; tracked separately |

After D2 metadata fix lands, the April-10 paper is endorsement-ready
from the substrate perspective. The remaining endorsement work is
candidate-endorser selection + outreach, which is a separate task class.

## D. Why this beats the original "v2 redeposit" plan

The prior D1 plan was: mint a new Zenodo version with paper-PDF changes.
That plan had three problems:
  1. Required rebuilding the LaTeX source (operator-side or agent-side build),
     introducing diff risk
  2. Created a v2 that would supersede v1 in default Zenodo listing but
     leave existing inbound citations pointing at v1 metadata
  3. Did not actually fix the issue — the GitHub URL in v1's PDF would
     still point at pcf-research; v1's README needed update either way

The repo-side fix executed this session:
  - Touches no LaTeX, no PDF build
  - Keeps DOI 10.5281/zenodo.19491768 stable (no superseding)
  - Fixes the actual reader-facing defect (URL → README → scripts)
  - Is RULE-1-PERMITTED (foundational maintenance, not new deposit)

A future Zenodo v2 redeposit can still be done for substantive
content reasons (e.g. Conjecture B5/B6 restriction to d=3 per PCF-2
v1.3 session R1.3 verdict, or other v1.3-cohort updates) — but it
should be a content-motivated revision, not a defect-driven patch.

## E. Operator action: Zenodo metadata abstract fix (~2 min)

To resolve D2 (the only remaining endorsement-readiness defect):

  1. Open https://zenodo.org/records/19491768
  2. Click "Edit" (top-right)
  3. In the "Description" field, locate the malformed string
     "computational application,wecertify482quadratic..." and replace
     with the properly-spaced version below
  4. Click "Save" then "Publish" (this is a metadata edit; preserves the DOI)

Suggested abstract text (cleaned; paste-ready):

> We prove that the polynomial continued fractions PCF(−kn², (k+1)n+k) and
> PCF(−n(2n−3), 3n+1) converge respectively to 1/ln(k/(k−1)) for every real
> k > 1 and to 4/π, and from the second family we derive a rapidly convergent
> identity for π/4. The key tool is a combination of closed-form convergents
> and a discrete Casoratian telescope for the underlying three-term
> recurrence. This differs from the classical Gauss and Brouncker formulas
> in that the evaluation is obtained directly inside the recurrence, with
> error O(2^{−N}/N^{7/2}) for the resulting series. As a computational
> application, we certify 482 quadratic generalized continued fractions
> against a basis of 15 standard constants using Arb ball arithmetic at
> 10,000-bit precision and depth N=5000. These computations yield 1500+
> correct digits and rigorous irrationality statements for 482 previously
> unclassified constants. We also prove that the 4/π family cannot be
> expressed as a Gauss ₂F₁ continued fraction, because its term ratio is
> forced into a ₂F₃ form over ℚ(√5). Code and verification scripts available
> at https://github.com/papanokechi/pcf-research (with a dedicated
> companion repository at https://github.com/papanokechi/pcf-casoratian-identities).

## F. Impact on next-action queue

D1 in `RESUME_NEW_CLI_20260513_POST_ZENODO_INVENTORY.txt` is now
**DONE-WITHOUT-V2-MINT**. The queue contracts to:

  D2 (HIGH)  → Verdict 208 Day-1 work (carried from prior triage)
  D3 (MED)   → Tier-1 substantive pick (M-A / M-C / S6)
  D4 (MED)   → Prompt 209 go/no-go
  D5 (LOW)   → Corpus-review offer
  D6 (LOW)   → TABLE 5 patch (Z9 + Z10)
  + NEW PENDING: D2-Zenodo-metadata (operator-side ~2 min)

Recommended next action (per autopilot bias-to-action): **D3 with M-A
choice** (close ξ₀ at d=3 direct, 1-2 hour Newton-polygon test on one
cubic representative per Galois bin — closes op:xi0-d3-direct cleanly).

## G. AEAL claims for this session

No numerical or computational claims made this session — pure
repository-maintenance work. README content is descriptive, not
load-bearing for any theorem or numerical assertion. No claims.jsonl
entries required.

## H. Files modified (off-bridge, repo-side)

  github.com/papanokechi/pcf-research/README.md
  github.com/papanokechi/pcf-research/casoratian/README.md  (NEW)
  github.com/papanokechi/pcf-casoratian-identities/README.md

  Commit SHAs:
  pcf-research                 8459b5d  (was ab85a7d)
  pcf-casoratian-identities    1c0b37e  (was f05d58b)

## I. Files committed to bridge (this session)

  This file: APRIL10_PCF_ENDORSEMENT_D1_RESOLVED_20260513.md
