# Audience framing + venue list — V0 substrate Phase E

**Relay:** 096 T2-M9-V0-SUBSTRATE-PRE-STAGE
**Tier:** TIER-A.4 (audience-framing memo + candidate venue list
+ forbidden-verb translation table per Reviewer A blind-spot
BS-2)
**Status:** DRAFT_SUBSTRATE
**Default operator preferences (E.4):** math-ph audience
emphasis (broadest reception); medium length target ~15pp
(CMP / IMRN style); "correspondence" terminology in title.
Operator override at V0-fire dispatch supersedes.

---

## 1. Audience framing memo

The V0 announcement is one piece of substrate that three
distinct reader-groups will read with three different
lenses. This memo records what each group will look for so
the V0-fire writer can pre-empt the highest-leverage
reception risks.

### 1.1 math-ph readership

**Default V0 audience.** The math-ph reader will read the
announcement as a **map of moduli + physical interpretation**
(resurgence / WKB / Stokes-data side). The V0 reader will
look for:

* A clean source-target description of $\Phi$;
* Citation anchors to JMU 1981 + Okamoto 1987 + V1
  (Barhoumi-Lisovyy-Miller-Prokhorov 2024) + V2 (Its-Lisovyy-
  Prokhorov 2018) so they can place $\Phi$ in the existing
  isomonodromy / RH literature;
* The Stokes-data secondary classifier (G15 / G22 axis) at
  least at the **conditional** level (the program currently
  pins it as M6.CC R1-gated; see `numerical_consistency_check.md`
  PRE-FIRE-INPUT verdict);
* An explicit physical-interpretation paragraph
  (resurgence / Borel-singularity radius $\xi_0$ as the
  exponential-asymptotic scale).

**Reception risk:** if the V0 announcement uses "functor"
without naming source/target categories explicitly, the
math-ph reader will read this as a categorical claim and
expect at minimum the assignment-on-objects + assignment-on-
morphisms sketch. Per Reviewer A Q4 L57 (verbatim quote, 50
words):

> if you call it a "functor" in the announcement, the
> community will read that as a categorical claim, and you'll
> need at minimum the source/target categories named and the
> assignment on objects + morphisms sketched — even if proofs
> are deferred. That's lighter than full RH-correspondence

— exactly the disposition `phi_assignment_statement.md` §2-§3
addresses.

### 1.2 math.CA readership

**Secondary V0 audience.** The math.CA reader will read the
announcement as **a connection formula at the level of
asymptotic expansions**. The V0 reader will look for:

* A direct anchor to the asymptotic-expansion side: $\xi_0$
  via Borel-singularity-radius interpretation (D2-NOTE v2.1
  Theorem 4.1 leg);
* Citation anchors to Wasow §X.3 + Birkhoff 1930 + B-T 1933
  §§4-6 (the analytic-asymptotic skeleton — same spine the
  D2-NOTE v2.1 closure inherited);
* The Painlevé-class classification side (Conte-Musette
  algorithmic Painlevé test result + V5 reference);
* An explicit statement that **the formal series side** is
  what the asymptotic expansion bounds — not the full
  monodromy data.

**Reception risk:** math.CA reader will be skeptical of any
claim labelled "Riemann-Hilbert correspondence" without an
explicit RH problem statement. V0 substrate handles this by
**not** claiming RH correspondence at the V0 stage (M13
TIER-C deliverable per `phi_assignment_statement.md` §4.3).

### 1.3 math.NT readership

**Tertiary V0 audience; lower priority.** The math.NT reader
will read the announcement as **a continued-fraction +
modular-discriminant identity result**. The V0 reader will
look for:

* A direct anchor to the $\Delta_d + \|\Delta\|_{\mathrm{Pet}}$
  side (PCF-1 v1.3 §6 + PCF-2 v1.3 §6 + Q22 deposit memo at
  $\lvert\delta_a\rvert = 3.08904186542 \times 10^{-23}$);
* The Petersson $j=0$ closure (A=6-only branch);
* Modular-form references (the $SL_2(\mathbb{Z})$ weight-12
  context).

**Reception risk:** math.NT reader will not have the
isomonodromy / Painlevé-class background. V0 substrate handles
this by **structuring the announcement so the math.NT-relevant
$\Delta_d / \|\Delta\|_{\mathrm{Pet}}$ axis is self-contained**
(does not require the Stokes-data axis to be read).

---

## 2. Forbidden-verb translation table (Reviewer A BS-2)

Per Reviewer A blind-spot BS-2, the program's internal AEAL
discipline forbids a set of "over-claiming" verbs in
agent-authored prose. The strict §5.E.3 envelope tokens are
the eight third-person-singular present forms enumerated in
the `forbidden_verb_scan.md` files of recent T2 fires (see
069 / 075 / 074 + 069r1 + 067 + 066 forbidden-verb scan
files for the project-canonical token list and inflection
extensions). The set-literal listing of the eight forbidden
verbs is recorded in those scan-pattern descriptor files only,
per 075 J2 + 069r1 mitigation precedent (set-literal echo
inside agent-authored prose triggers strict-pattern hits at
the scan stage).

External-facing publication venues use exactly these verbs as
their normal academic register. The V0 announcement, when
written for external venue submission, must translate the
program-internal voice to the external-venue voice. The
translation is a substrate-level deliverable (per A BS-2).

### 2.1 Translation table

| Internal program voice | External venue voice |
|------------------------|----------------------|
| "Phi is logged at AEAL claim 096-B-1" | "We announce a correspondence Phi" |
| "the residual envelope is (under threshold)" | "the residual is (under threshold), so the consistency of … holds" |
| "$\xi_0$ universality is upgraded THEOREM-GRADE in D2-NOTE v2.1" | "By [D2-NOTE v2.1, Theorem 4.1], $\xi_0(\mathcal{F}) = d / \beta_d^{1/d}$ for all $d \ge 2$" |
| "the Petersson $j=0$ branch closes A=6-only" | "By [Q22-memo], the Petersson amplitude in the H6 B19+ ring closes to A=6 with linear residual $\le 3.09 \times 10^{-23}$" |
| "M6.CC R1 carry-forward is open" | "We assume the $V_{\mathrm{quad}} \to P_{\mathrm{III}}(D_6)$ Lax-pair conjugation [Okamoto 1987 §§2-3] for the secondary classifier in §X" |
| "the verdict is PRE-FIRE-INPUT" | "the numerical consistency check at 10 dps is reserved for a forthcoming paper [M13]" |

### 2.2 Translation principle

The translation principle is per A Q4 L59 (verbatim quote, 41
words):

> Adopt a two-tier framing: V0 announcement states Φ at the
> assignment level (objects → objects, with morphism behavior
> described informally), explicitly defers the categorical-
> coherence verification, and lists RH-at-Stokes-data as the
> M13 deliverable

The external voice can use external register **as long as each
claim is anchored to an internal AEAL claim or a published
external citation**. The forbidden-verb prohibition is
internal-only; external-prose audit happens at the V0-fire's
own envelope (not at this fire — substrate only).

### 2.3 Internal-prose deliverable hygiene

In this 096 substrate-fire, all four production deliverables
(`phi_assignment_statement.md` / `numerical_consistency_check.md` /
`related_work_survey.md` / `audience_framing_and_venue_list.md` /
this file) are **internal-program prose** and therefore obey
the strict §5.E.3 forbidden-verb prohibition. The translation
table above is itself internal-program prose **describing**
the external translation — the table cells are quoted
register-shifts, not first-person claims by this fire's agent.

---

## 3. Candidate venue list (ranked)

The following 7 candidate venues are ranked by program-fit +
acceptance-rate priors. Operator may re-order at V0-fire
dispatch; the substrate is wording-agnostic.

### 3.1 Initial ranking

| Rank | Venue | Type | Fit | Acceptance prior | Notes |
|------|-------|------|-----|------------------|-------|
| 1 | **CMP** (*Communications in Mathematical Physics*) | Journal | High (math-ph default audience) | Selective | Long-form (~15pp medium target fits); broad math-ph reception; Painlevé / RH papers regularly featured |
| 2 | **SIGMA** (*Symmetry, Integrability, Geometry: Methods and Applications*) | Open-access journal | High (V1 published here) | Moderate; OA model | **Precedent: V1 (Barhoumi-Lisovyy-Miller-Prokhorov 2024) published as SIGMA 20:019.** Direct fit for $P_{\mathrm{III}}(D_6)$ topic; OA reduces visibility-gap concern |
| 3 | **IMRN** (*International Mathematics Research Notices*) | Journal | Moderate-High | Selective | Pure-math venue with broad reach; Painlevé moduli + RH papers featured; medium length target good fit |
| 4 | **Duke MJ** (*Duke Mathematical Journal*) | Journal | High but bar high | Very selective | **Precedent: V2 (Its-Lisovyy-Prokhorov 2018) published Duke MJ 167:7.** High bar; V0 announcement may be tighter as V0 + full M13 follow-up (Tier-C) than as single Duke submission |
| 5 | **JMP** (*Journal of Mathematical Physics*) | Journal | Moderate (math-ph) | Less selective than CMP | Broader math-ph readership; faster turnaround; suitable if V0 wants speed-to-record over impact |
| 6 | **Lett. Math. Phys.** (*Letters in Mathematical Physics*) | Journal | Moderate (announcement-style) | Moderate | **Letter-format venue** — natural fit for V0 ANNOUNCEMENT with full proofs deferred to M13 follow-up; short target preferred (5-7pp); tradeoff vs medium target |
| 7 | **arXiv-only V0 preprint** (no journal) | Preprint server | Low cost / fast | n/a | Speed-to-public-record; V0 visibility without journal review-cycle delay; downstream M9 full submission to one of #1-#6 after community feedback |

### 3.2 Recommended ordering rationale (operator-overridable)

* **#1 CMP + #2 SIGMA tied as primary candidates.** SIGMA has
  the V1 precedent and is OA (lower visibility risk); CMP has
  the broader math-ph reach. Operator preference between OA
  reach (SIGMA) and indexing reach (CMP).
* **#3 IMRN as backup primary.** Broad math reach without the
  Duke selectivity.
* **#4 Duke deferred to M13 full RH-correspondence paper.**
  The V0 announcement alone may be too short for Duke;
  TIER-C submission has stronger Duke fit.
* **#5 JMP + #6 Lett. Math. Phys. as fallback / speed
  priority.** Letters in Math. Phys. is the natural
  letter-format venue for the announcement style.
* **#7 arXiv-only as concurrent action.** Posting to arXiv
  before journal submission is standard math-ph practice; V0
  substrate recommends arXiv post on V0-fire day **regardless
  of journal selection**.

### 3.3 Submission-staging recommendation

Per Reviewer D Q4 L294 + L341 (verbatim quote, 26 words):

> Staged / two-tier announcement: physics-level V0
> (assignment-level Phi + numerical Stokes consistency) +
> full RH-correspondence as M13 follow-up

the submission staging is:

1. **2026-Q3-class window (post M4 + M6.CC closure):** V0
   arXiv preprint + journal submission to #1 (CMP) or #2
   (SIGMA).
2. **2026-Q4 / 2027-Q1:** TIER-C / M13 follow-up (full RH
   correspondence at Stokes-data level + categorical-coherence
   verification) submitted to #4 (Duke MJ) or back to the V0
   journal for a longer companion paper.

The staging is **operator-side scheduling decision**; substrate
records it without committing to dates.

---

## 4. Audience-framing + venue-list cross-walk

| Audience | Best venue match | Reception strategy |
|----------|------------------|--------------------|
| math-ph (default) | CMP / SIGMA / Lett. Math. Phys. | Lead with $\Phi$ as map-of-moduli; emphasize Stokes-data secondary axis; cite V1 / V2 / JMU / Okamoto |
| math.CA | CMP / IMRN / JMP | Lead with $\xi_0$ Borel-singularity-radius interpretation; emphasize asymptotic-expansion side; cite Wasow / Birkhoff / B-T / D2-NOTE v2.1 |
| math.NT | IMRN / arXiv-only | Lead with $\Delta_d + \|\Delta\|_{\mathrm{Pet}}$; emphasize cubic-modular framing; cite PCF-1 v1.3 + PCF-2 v1.3 + Q22 memo |

**Cross-cutting recommendation:** the V0 announcement should be
**writable by a math-ph default reader** with sidebar paragraphs
reaching out to math.CA + math.NT secondary readers. Single
unified announcement; not three parallel announcements.

---

## 5. AEAL anchor block

* audience_framing_and_venue_list.md SHA-256: computed at
  fire end in `claims.jsonl` 096-E-1.
* peer-AI synthesis anchor: SHA-16 prefix `DF92466E123E16BF`
  at L57 (A Q4 50-word quote) + L59 (A Q4 41-word quote) +
  L294 (D Q4 25-word quote) + L341 (summary table 26-word
  quote).
* picture v1.19 anchor: SHA-16 prefix `8BD9043370872F07`.

---

End audience_framing_and_venue_list.md.
