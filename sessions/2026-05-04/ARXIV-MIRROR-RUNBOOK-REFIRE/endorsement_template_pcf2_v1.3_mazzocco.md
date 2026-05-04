# Endorsement-request template — PCF-2 v1.3 → Prof. {{ENDORSER_LASTNAME|Mazzocco}}

> **Operator action.**  This is a populated template.  Before sending,
> the operator (a) verifies the endorser's institutional email at the
> public homepage of University of Birmingham (do *not* paste an unverified address);
> (b) substitutes their own `{{OPERATOR_NAME}}` and `{{OPERATOR_ORCID}}`;
> (c) optionally attaches a copy of the Zenodo PDF.  Per arXiv help
> (https://info.arxiv.org/help/endorsement.html), the endorser receives
> a 6-character alphanumeric code once the operator starts a new
> submission in `math.NT` and is willing to provide endorsement;
> the endorser enters the code at https://arxiv.org/auth/endorse.
> Per arXiv etiquette, do **not** email large numbers of endorsers at
> once or repeat-email the same endorser.

---

**Suggested endorser (this populated template)**

- Full name:        Prof. {{ENDORSER_LASTNAME|Mazzocco}}
- arXiv author id:  `{{ENDORSER_HANDLE|mazzocco_m_1}}`  (https://arxiv.org/a/mazzocco_m_1)
- Affiliation:      University of Birmingham
- Email:            {{ENDORSER_EMAIL_TO_BE_CONFIRMED_BY_OPERATOR}}
- Research area:    math.CA + math-ph + integrable systems / Painlevé

---

**Subject:** arXiv `math.NT` endorsement request — *{{TITLE|PCF-2: A Program Statement for the Cubic Extension of the Δ-Discriminant Transcendence Predicate}}*

---

Dear Prof. {{ENDORSER_LASTNAME|Mazzocco}},

I am writing to request your endorsement for an arXiv submission to
the `math.NT` category, with cross-listing to `math-ph`.  The paper,
"{{TITLE|PCF-2: A Program Statement for the Cubic Extension of the Δ-Discriminant Transcendence Predicate}}" (Zenodo deposit {{DOI|10.5281/zenodo.19963298}}, version
{{VER|1.3}}, {{N_PAGES|see Zenodo record}} pp.), is part of
an independent research programme — the Self-Iterating Analytic Relay
Chain (SIARC) — on polynomial continued fractions and their analytic
/ Painlevé / number-theory consequences.

**Paper summary.** This paper is a program statement, not a results paper. It frames PCF-2 (P13 in the SIARC stack), the cubic extension of PCF-1~\cite{Papanokechi2026PCF1} from degree-two polynomial continued fractions to degree-three. PCF-1 established a sharp empirical dichotomy across 30 degree-two families: the sign of the balanced discriminant \Delta_{2}=\beta^{2}-4\alpha\gamma predicts whether the limit of the PCF admits an elementary closed form (\Delta_{2}>0, 24/24 Trans-stratum families) or fails PSLQ detection against an 18-element basis at 220 digits (\Delta_{2}<0, 6/6 CM candidates), with the Stokes…

**Why I am asking you.** Your published work in math.CA + math-ph + integrable systems / Painlevé overlaps directly
with the present paper's subject and methods; if you are willing to
endorse and your `math.NT` endorsement privileges are currently
active, you are an excellent match per the arXiv guidelines.

**Practical step.** I will start a new submission at
https://arxiv.org/submit which will trigger arXiv to issue a
6-character endorsement code and send me an email containing
endorsement instructions to forward to you.  The endorser-side action
takes a few minutes and is one-time per category.

The Zenodo deposit at {{DOI|10.5281/zenodo.19963298}} contains the full PDF,
abstract, reproducibility metadata, and the SIARC bridge provenance
trail.  The arXiv submission will mirror that deposit byte-for-byte
(MD5 + SHA-256 + size + page count verified against the Zenodo API
on 2026-05-04).

If you are unable to endorse — for example, if your `math.NT`
endorsement privileges are not currently active or if the topical fit
is too distant for your judgement — please simply reply to that
effect; I will then approach a different qualified endorser.  No
follow-up email will be sent.

With many thanks for your consideration,

{{OPERATOR_NAME}}
Yokohama, Japan
ORCID: {{OPERATOR_ORCID}}
{{OPTIONAL_OPERATOR_HOMEPAGE_OR_GITHUB}}

---

## Operator-personalisation placeholders (do NOT auto-fill)

- `{{OPERATOR_NAME}}`           — operator chooses
- `{{OPERATOR_ORCID}}`          — operator chooses
- `{{ENDORSER_LASTNAME|...}}`   — pre-filled with `Mazzocco`; operator may replace
- `{{ENDORSER_HANDLE|...}}`     — pre-filled with `mazzocco_m_1`; operator may replace
- `{{ENDORSER_EMAIL_TO_BE_CONFIRMED_BY_OPERATOR}}` — operator confirms institutional homepage
- `{{TITLE|...}}`               — pre-filled; verbatim from Zenodo
- `{{DOI|...}}`                 — pre-filled; verbatim from Zenodo
- `{{VER|...}}`                 — pre-filled

## AEAL provenance

- 034 session: `sessions/2026-05-04/ARXIV-MIRROR-RUNBOOK-REFIRE/`
- Endorser-handle source: ENDORSER-HANDLE-ACQUISITION 2026-05-04
  (Tier-1 confirmed-public arXiv handle).
