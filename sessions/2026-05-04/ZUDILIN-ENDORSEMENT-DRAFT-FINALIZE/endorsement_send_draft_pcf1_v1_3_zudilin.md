# Endorsement-request — PCF-1 v1.3 → Prof. Zudilin (send-ready draft)

> **Operator action required before sending:**
>
> 1. Fill `{{OPERATOR_NAME}}`, `{{OPERATOR_ORCID}}`, and (optionally)
>    `{{OPTIONAL_OPERATOR_HOMEPAGE_OR_GITHUB}}` in the body below.
> 2. Fill the `Date:` line in the header at send time.
> 3. Optionally attach a copy of the Zenodo PDF
>    (https://doi.org/10.5281/zenodo.19937196).
> 4. Send from your own mail client. Per arXiv etiquette, do **not**
>    email large numbers of endorsers at once or repeat-email the same
>    endorser. If no reply within ~2 weeks, fallback to a different
>    Tier-1 endorser (do **not** repeat-email Zudilin nor switch to the
>    private gmail address `wzudilin@gmail.com` for first contact).

---

## Mail header (operator pastes into mail client)

```
To:       w.zudilin@math.ru.nl
Subject:  arXiv math.NT endorsement request — Complex Multiplication as a Transcendence Predicate for Degree-2 Polynomial Continued Fractions
Date:     {{OPERATOR_FILLS_DATE_AT_SEND_TIME}}
```

---

## Mail body

Dear Prof. Zudilin,

I am writing to request your endorsement for an arXiv submission to
the `math.NT` category, with cross-listing to `math.CA`.  The paper,
"Complex Multiplication as a Transcendence Predicate for Degree-2
Polynomial Continued Fractions" (Zenodo deposit
10.5281/zenodo.19937196, version 1.3, see Zenodo record for page
count), is part of an independent research programme — the
Self-Iterating Analytic Relay Chain (SIARC) — on polynomial continued
fractions and their analytic / Painlevé / number-theory consequences.

**Paper summary.** We propose a transcendence predicate for
degree-two polynomial continued fractions (PCFs) based on the sign of
the balanced discriminant Delta = beta^2 - 4*alpha*gamma of the
denominator polynomial b_n = alpha*n^2 + beta*n + gamma. Working
inside the Spec(K) classification framework of Papanokechi (2026), we
present a v5 upgrade of the schema that fixes two cross-paper
inconsistencies and adds the Stokes exponent and connection-coefficient
proxy as components 6 and 7. Our central empirical finding is a sharp
dichotomy across 30 degree-two families: 24 F(2,4) Trans-stratum
families have Delta > 0 and admit elementary closed-form limits, while
6 CM-candidate families have Delta < 0 and fail PSLQ detection against
an 18-element basis at 220 digits.

**Why I am asking you.** Your published work in primary math.NT,
transcendence + irrationality measures + continued fractions overlaps
directly with the present paper's subject and methods; if you are
willing to endorse and your `math.NT` endorsement privileges are
currently active, you are an excellent match per the arXiv guidelines.

**Practical step.** I will start a new submission at
https://arxiv.org/submit which will trigger arXiv to issue a
6-character endorsement code and send me an email containing
endorsement instructions to forward to you. The endorser-side action
takes a few minutes and is one-time per category.

The Zenodo deposit at 10.5281/zenodo.19937196 contains the full PDF,
abstract, reproducibility metadata, and the SIARC bridge provenance
trail. The arXiv submission will mirror that deposit byte-for-byte
(MD5 + SHA-256 + size + page count verified against the Zenodo API
on 2026-05-04).

If you are unable to endorse — for example, if your `math.NT`
endorsement privileges are not currently active or if the topical fit
is too distant for your judgement — please simply reply to that
effect; I will then approach a different qualified endorser. No
follow-up email will be sent.

With many thanks for your consideration,

{{OPERATOR_NAME}}
Yokohama, Japan
ORCID: {{OPERATOR_ORCID}}
{{OPTIONAL_OPERATOR_HOMEPAGE_OR_GITHUB}}

---

## Send-target verification provenance (do NOT include in sent mail)

- **Verified send-target:** `w.zudilin@math.ru.nl`
- **Verification date:** 2026-05-04 ~17:50 JST
- **Verification sources** (synthesizer-Claude web_search + direct fetch):
  - <https://www.math.ru.nl/~zudilin/> (Zudilin's primary personal homepage)
  - <https://www.ru.nl/en/people/zudilin-v> (Radboud University faculty profile)
- **Stale address NOT used:** `wadim.zudilin@newcastle.edu.au`
  (University of Newcastle, Australia — full-professorship ended August
  2018 per ResearchGate; address ~7 years stale at send time).
- **Fallback address (reserve; do NOT use for first contact):**
  `wzudilin@gmail.com` — only escalate to this address if institutional
  send bounces with a delivery failure (not on silence).
- **ORCID:** 0000-0001-9551-2903
- **Current affiliation:** Professor of Pure Mathematics, Institute
  for Mathematics, Astrophysics and Particle Physics (IMAPP), Radboud
  University Nijmegen, PO Box 9010, 6500 GL Nijmegen, The Netherlands.
- **arXiv handle:** `zudilin_w_1` (<https://arxiv.org/a/zudilin_w_1>) —
  primary research area math.NT (transcendence, irrationality measures,
  continued fractions).

## AEAL provenance chain

- **Source template:** `endorsement_template_pcf1_v1.3_zudilin.md`
  (SHA-256: `B0EFCFA1581E584B3A6157B0CA02E04FB23D26FC70A9555937FDB2F20F161895`,
  4,923 B) in bridge session
  `sessions/2026-05-04/ARXIV-MIRROR-RUNBOOK-REFIRE/` (034 verdict).
- **PCF-1 v1.3 identifiers** (cross-checked against
  `tex/submitted/control center/RESUME_AFTER_REBOOT_20260502.txt` L40):
  - Concept DOI: `10.5281/zenodo.19931635`
  - Version DOI (v1.3): `10.5281/zenodo.19937196` (cited in body above)
- **Standing rule applied:** SOP `Bibliographic identifier
  pre-verification (lit-hunt prompts)` deposited 2026-05-04 at
  `.github/copilot-instructions.md` (workspace commit 79e7a22 + bridge
  commit 7fbe30d). Send-target email pre-verified at two independent
  authoritative sources before this draft was emitted.
- **Operator-personalisation placeholders deliberately NOT auto-filled
  by the agent** (per the source template's footer rule + standing
  RACI): `{{OPERATOR_NAME}}`, `{{OPERATOR_ORCID}}`,
  `{{OPTIONAL_OPERATOR_HOMEPAGE_OR_GITHUB}}`,
  `{{OPERATOR_FILLS_DATE_AT_SEND_TIME}}`.
