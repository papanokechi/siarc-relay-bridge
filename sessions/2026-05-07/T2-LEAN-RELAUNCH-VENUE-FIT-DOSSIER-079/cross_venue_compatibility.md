# Cross-Venue Compatibility Note

**Fire time:** 2026-05-07 ~14:55 JST
**Substrate anchors:**
- venue_profile_lmcs.md / venue_profile_jfr.md / venue_profile_mcs.md
  / venue_profile_tcs.md
- cover_letter_framing_lmcs.md / cover_letter_framing_jfr.md
  / cover_letter_framing_mcs.md / cover_letter_framing_tcs.md
- submission_log.txt L173-205 (Item 24 + Item 25)
- tunnell_afm_R2.tex L74-118 (title + abstract verbatim;
  SHA 91546B54974E25A4CF54A13CA71FA75380F0C5ED3C0EFA421C6CCAC2333D8BB9)

---

## D.1 Parallel-submission policy compliance

All four candidate venues (LMCS / JFR / MCS / TCS) operate under
single-channel-only submission policies as a baseline (no concurrent
submissions to other journals while a manuscript is under review).
Specific 2026 wording was verified for two of the four venues
during this session:

- **LMCS**: standard Episciences single-channel policy (per the
  "For Authors" menu on https://lmcs.episciences.org/; exact wording
  not lifted in this session).
- **JFR**: about-page peer-review-process discussion implies single-
  channel routing (no explicit multi-submission permission).
- **MCS**: Springer-side standard single-channel policy applies (not
  directly verified at fire time due to auth-gate redirect; marked
  UNKNOWN for explicit 2026 wording).
- **TCS**: Elsevier-wide single-channel policy applies per standard
  ScienceDirect author-guide (not directly verified at fire time;
  marked UNKNOWN for explicit 2026 wording).

No conflicts surfaced: the operator may dispatch to any one of the
four candidates without colliding with single-channel requirements,
provided the prior AFM submission has been disposed (it has — Item
24).

## D.2 AFM-clearance carry-forward

Item 25 L205 records the operator-side note:
> "OPEN QUESTION RESOLVED 2026-05-07 ~12:46 JST: AFM Item 24
> verdict landed (DESK REJECTED); no active submission remains;
> multi-submission policy concern CLEARED for any next-venue
> dispatch."

The AFM disposition was final (no review, no rationale, 8-min
turnaround per Item 24 L175 + L179) and contained no R3-revision
request. The current parallel-flight count for the Lean 4
manuscript is zero. All four cover-letter framing drafts above
include a multi-submission-disclosure paragraph anchored to this
fact.

## D.3 Reuse risk (prior-deposit compatibility)

The Tunnell paper has two prior public artefacts that any next
venue must accept:

- **Zenodo deposit** at DOI 10.5281/zenodo.19834824
  (verbatim from submission_log.txt L181 + L201).
- **GitHub repository** at github.com/papanokechi/tunnell-cnp-lean4
  (verbatim from submission_log.txt L180).

LMCS's arXiv-overlay model is not just compatible but expects a
prior deposit (the journal manages refereeing on top of an arXiv
or HAL deposit). JFR's about-page open-access-policy text
explicitly permits pre-submission and pre-print deposits. MCS
(Springer Nature) and TCS (Elsevier) blanket policies permit arXiv
preprints with appropriate cross-referencing; whether each accepts
a prior Zenodo deposit specifically is UNKNOWN at fire time
without per-venue policy verification. No conflict surfaces between
the two diamond-OA candidates and the existing Zenodo + GitHub
artefacts.

## D.4 Cover-letter consistency (one-source-of-truth check)

All four cover-letter framing drafts (cover_letter_framing_lmcs /
_jfr / _mcs / _tcs) share the following constants:

- **Title** verbatim: *"A Layered, Axiom-Isolated Lean 4
  Formalization of the Congruent Number Problem up to Tunnell's
  Criterion"* — identical across all four drafts; matches
  submission_log.txt L152 + L174 + tunnell_afm_R2.tex L74-77.
- **Abstract opening verbatim quote** (six lines from "We present a
  954-line Lean 4 formalization ..." through "... and Tunnell's
  conditional theorem.") — identical across all four drafts.
- **Author** "Papanokechi (Independent researcher, Yokohama,
  Japan), ORCID 0009-0000-6192-8273" — identical across all four
  drafts.
- **GitHub repo + Zenodo DOI** "github.com/papanokechi/tunnell-cnp-
  lean4" + "10.5281/zenodo.19834824" — identical across all four
  drafts.
- **Multi-submission disclosure paragraph** — identical wording
  across all four drafts.

Venue-specific elements vary only in: salutation, named journal,
section-routing line (TCS only: "with a request for routing to the
Logic and Semantics section"), and per-venue framing paragraph.

The one-source-of-truth check returns CLEAN: a synth pick of any
one of the four candidates triggers a finalize step that swaps the
salutation + journal name + section-routing line into the chosen
draft and dispatches; no per-venue redrafting of title / abstract
/ author / artefact-link substrate is required.

---

**Word count target check:** ~580 words (slightly above 300-500
envelope target; surfaced as J1 in handoff Anomalies — operator may
trim D.1 venue-by-venue rows if a tighter envelope is required).

**Forbidden-verb scan (excluding verbatim quote of submission_log
L205, which is structurally exempt):** zero hits against the FV-7
verb set (enumerated only in forbidden_verb_scan.md to avoid
set-literal echoes in production deliverables).
