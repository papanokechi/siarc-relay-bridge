# Subject-Fit Matrix — ARXIV-ENDORSEMENT-TEMPLATES-EXPAND
# Date: 2026-05-04
# Scope: 3 records × 3 Tier-1 endorsers = 9 cells

Per arXiv policy (`https://info.arxiv.org/help/endorsement.html`,
captured 034 PHASE D), an endorser may endorse a submission to any
arXiv subject-class for which they have active endorsement
privileges. arXiv grants endorsement privileges per subject-class
based on prior submission record in (or sufficiently close to) that
class. Cross-listed records may be endorsed by anyone with privileges
in **any** of the listed categories (primary or cross).

Anchor sources:
  - 034 PHASE D capture of arXiv help text (`endorsement.html`).
  - `ENDORSER-HANDLE-ACQUISITION/candidate_dossier.md` (2026-05-04;
    Tier-1 handles confirmed-public; Tier-2 handles pending).
  - 034's `zenodo_metadata_5_records.json` for record arXiv-class
    annotations.

Grading legend:
  - **H** (HIGH)     — endorser has direct submission history in
                       record's primary or one of its cross
                       categories.
  - **M** (MODERATE) — endorser publishes in adjacent areas;
                       arXiv routinely accepts such endorsements
                       provided the endorser judges topical fit.
  - **L** (LOW)      — clear domain mismatch; template skipped.

---

## Record × endorser grading

| record (arXiv classes)                            | Zudilin (math.NT, math.CA) | Mazzocco (math.CA, math-ph, math.QA, math.AG) | Garoufalidis (math.GT, math.NT, math.CA) |
|---------------------------------------------------|----------------------------|-----------------------------------------------|------------------------------------------|
| **#1 umbrella v2.0** — math.HO                    | M                          | M                                             | M                                        |
| **#4 CT v1.3**       — math-ph; +math.DS, math.NT | H (math.NT cross)          | H (math-ph primary)                           | H (math.NT cross)                        |
| **#5 T2B v3.0**      — math.HO; +math.NT          | H (math.NT cross)          | M (Painlevé/asymptotic adjacent; math.NT cross-judgement plausible) | H (math.NT cross)                        |

### Cell-by-cell rationale

  - **(umbrella, Zudilin) — M.** umbrella v2.0 is a math.HO program
    statement. Zudilin's recent math.NT publication record overlaps
    the irrationality-measure / continued-fractions tradition that
    umbrella v2.0 frames. arXiv math.HO endorsement requires
    judgement that the work is suitable for the history-of-math
    overview category; an active math.NT endorser publishing
    Apéry-tradition papers can plausibly judge this.

  - **(umbrella, Mazzocco) — M.** umbrella v2.0 contains §4.4
    invariant-triple framing connected to Painlevé / integrable-
    systems data; Mazzocco's Painlevé / monodromy-manifold work
    makes her a competent judge of the Painlevé-adjacent overview
    even though math.HO is not her primary class.

  - **(umbrella, Garoufalidis) — M.** umbrella v2.0 frames the
    SIARC stack (PCF + resurgence + integrable systems);
    Garoufalidis's broad activity in math.NT / math.CA / math.GT
    qualifies him to judge an umbrella-program statement.

  - **(CT, Zudilin) — H.** CT v1.3 cross-lists math.NT; Zudilin is
    a math.NT primary endorser per Tier-1 dossier.

  - **(CT, Mazzocco) — H.** CT v1.3's primary class is math-ph;
    Mazzocco publishes in math-ph (Joshi–Mazzocco–Roffelsen 2024
    arXiv:2405.10541, math-ph + math.AG + nlin.SI). Direct fit.

  - **(CT, Garoufalidis) — H.** CT v1.3 cross-lists math.NT; CT's
    bibliography cites Garoufalidis–Costin on resurgence of
    Kontsevich–Zagier power series (CT's BoT channel directly
    builds on this line).

  - **(T2B, Zudilin) — H.** T2B v3.0 cross-lists math.NT; T2B's
    Birkhoff–Trjitzinsky / Gauss-CF dichotomy is a math.NT
    irrationality-flavoured discriminant analysis directly
    parallel to Zudilin's Apéry-tradition body of work.

  - **(T2B, Mazzocco) — M.** T2B's BoT-side formal asymptotics
    mirror the Stokes-phenomenon / confluence techniques
    Mazzocco has published in (Horrobin–Mazzocco 2020
    arXiv:2009.07607). Cross-list math.NT not Mazzocco's primary,
    but math-ph adjacency keeps the topical-fit gate plausible.

  - **(T2B, Garoufalidis) — H.** T2B cross-lists math.NT;
    Garoufalidis's Bloch-group / Habiro-ring math.NT activity is
    directly compatible with refereeing a math.NT continued-
    fraction discriminant paper.

---

## Total templates emitted this prompt

9 of 9 cells receive a template (no L cells).

  - 3 × umbrella v2.0 (Zudilin, Mazzocco, Garoufalidis)
  - 3 × CT v1.3       (Zudilin, Mazzocco, Garoufalidis)
  - 3 × T2B v3.0      (Zudilin, Mazzocco, Garoufalidis)

Verdict: `COMPLETE_NINE_TEMPLATES_EMITTED` (per prompt §7
outcome ladder).

---

## Note on prior CT templates

Three Tier-1 CT-record templates already exist at
`sessions/2026-05-04/ENDORSER-HANDLE-ACQUISITION/`
(`endorsement_request_record4_CT_{zudilin,mazzocco,garoufalidis}.md`).
The CT templates emitted in this session are the spec-canonical
037 deliverables and are written from scratch in the same style as
034's PCF-1 / PCF-2 templates so that the operator has a single
contiguous template set under one folder. They are content-
equivalent to the prior CT templates modulo minor wording.

---

## Subject-fit gate verdict per record

  - **umbrella v2.0**  — 3/3 templates (all M); operator may
    consider whether to also seek a Tier-2 math.HO-active endorser
    if any of the M judges declines on category-fit grounds.
  - **CT v1.3**        — 3/3 templates (all H).
  - **T2B v3.0**       — 3/3 templates (2 H + 1 M); robust coverage.

No record falls under HALT_NO_SUBJECT_FIT_FOR_RECORD (§4).
