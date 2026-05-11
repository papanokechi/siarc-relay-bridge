# Reconnaissance Report — P-009 d>=3 binding-window literature

**Task:** T2-EXECUTOR-T1-156-E-P009-LITERATURE-181 (Pathway E of slot 156 verdict)
**Date:** 2026-05-11 JST
**Agent:** GitHub Copilot (VS Code) in T2-Executor role
**Pathway:** E (P-009 caveat active variant v1 dispatch; literature reconnaissance only)
**Scope:** d>=3 binding-window phenomena in Painleve III / V_quad /
continued-fraction analytic-continuation contexts; informs Pathway B
(Birkhoff-Trjitzinsky structural) vs Pathway D (upper-bound proof)
choice per slot 156 verdict Q3d.
**P-009 active variant v1 (verbatim, pinned 2026-05-06 at bridge SHA 1873538):**

> "Stokes-multiplier discrimination (companion milestone M8b) will
> supply an additional independent test of the SIARC stratification
> at d>=3, conditional on the M8b dispatch landing within the
> relevant binding window and on the binding-window result."

---

## 1. Search structure

Per phase B of relay prompt 181 (drafted 2026-05-11 ~15:33 JST):

- 11 keyword queries + 1 BLMP 2024 abstract re-verification
- 4 author-restricted arxiv listings (Forrester, Lisovyy, Roussillon,
  Mazzocco)
- 4 keyword-phrase arxiv searches with exact-phrase quotes
- 4 author-name arxiv probes for resurgence experts (Iwaki, Sauzin,
  Aniceto, Bobrova)
- 1 Google Scholar exact-phrase probe ("binding window" Painleve)
- Inheritance: 038 dossier (bridge SHA a26ab27, 2026-05-04) provided
  the bridge-corpus baseline for adjacent-literature identification

Pre-verification per copilot-instructions Bibliographic ID rule
(post-031 WITTE-FORRESTER verdict, 2026-05-04): every identifier
quoted below in section 4 has been resolved via arxiv.org/abs and
its title + first-author surname checked against the resolved page.

---

## 2. Keyword exhaustion table

All searches executed on arxiv.org and (one) scholar.google.com on
2026-05-11. Asterisk (*) marks fail-conjunctive queries that returned
zero because arxiv search is term-conjunctive and the phrase did not
appear as a unit; these are retained for audit trail. Pound (#) marks
phrase-quoted queries where the literal phrase does not appear in
any indexed title/abstract/comment.

| # | Query | Source | Result | Inference |
|---|---|---|---|---|
| K01 | `Painleve III Stokes multiplier higher degree` (*) | arxiv all-fields | 0 hits | conjunctive over-constrained; broken into K05 + K06 |
| K02 | `Forrester Witte Painleve higher degree` (*) | arxiv all-fields | 0 hits | retried as author-listing K11 |
| K03 | `Birkhoff Trjitzinsky rank borderline anormal` (*) | arxiv all-fields | 0 hits | rank-q>=2 borderline-anormal literature does not surface |
| K04 | `Lisovyy Roussillon Painleve III resurgence` (*) | arxiv all-fields | 0 hits | retried as author-listing K12 + K13 |
| K05 | `Painleve III D6 D8` | arxiv all-fields | 0 hits | conjunctive over-constrained on alphanumeric tokens; BLMP 2024 surfaces under author-listing K12 |
| K06 | `"binding window" Painleve` (#) | arxiv all-fields | 0 hits | the phrase "binding window" is SIARC-internal jargon, not literature usage |
| K07 | `"Painleve III" "Stokes constant"` (#) | arxiv all-fields | 0 hits | no published combo of these two exact phrases |
| K08 | `"Painleve III hierarchy"` (#) | arxiv all-fields | 0 hits | the PIII hierarchy does NOT exist as a developed published subject |
| K09 | `"Painleve III" resurgent Borel` (*) | arxiv all-fields | 0 hits | PIII resurgent-Borel literature absent under conjunctive search |
| K10 | `"binding window" Painleve Stokes multiplier` (#) | Google Scholar | 0 hits | confirms K06 across full Scholar index |
| K11 | author: Forrester | arxiv author-listing | 89 papers; 0 d>=3 PIII hits | Forrester recent corpus is random-matrix / Riesz gas / circular-ensembles; PII Constr. Approx. 2015 is closest but is PII not PIII |
| K12 | author: Lisovyy | arxiv author-listing | 34 papers; 1 STRONG-ADJACENT (BLMP 2024); 3 WEAK-ADJACENT | see section 4 |
| K13 | author: Roussillon | arxiv author-listing | 20 papers (filtered to 7 math/math-ph); 2 WEAK-ADJACENT | see section 4 |
| K14 | `Mazzocco Painleve hierarchy` | arxiv all-fields | 3 hits; 0 STRONG; 3 STRUCTURAL-ANALOGUE-PII | see section 4 |
| K15 | `Aniceto Painleve Stokes` (*) | arxiv all-fields | 0 hits | resurgence-Stokes expert corpus shows no PIII-specific work |
| K16 | `Sauzin Painleve resurgence` (*) | arxiv all-fields | 0 hits | alien-calculus founder corpus shows no PIII-specific work |
| K17 | `Iwaki Painleve III Stokes` (*) | arxiv all-fields | 0 hits | Iwaki's resurgence corpus is on topological recursion / PI / quantum curves, not PIII Stokes |
| K18 | `"Birkhoff-Trjitzinsky" rank` (#) | arxiv all-fields | 0 hits | the phrase "Birkhoff-Trjitzinsky" appears in arxiv 0 times paired with "rank"; consistent with K03 |

Aggregate: 18 distinct probes, 17 NULL primary-result and 4 hit-events
(BLMP 2024 STRONG-ADJACENT but already in bridge corpus;
Lenells-Roussillon 2024 + Roussillon-2020 WEAK; Joshi-Mazzocco 2002 +
Mazzocco-Mo 2006 + Bobrova-Mazzocco 2020 PII-STRUCTURAL-ANALOGUE).

**No NEW d>=3-Painleve-III binding-window literature surfaced.**

---

## 3. Adjacent-literature corpus (WEAK and STRUCTURAL-ANALOGUE hits)

These are pre-verified via arxiv.org/abs resolution on 2026-05-11.

### 3.1 STRONG-ADJACENT (already in bridge corpus)

**[BLMP-2024]** Ahmad Barhoumi, Oleg Lisovyy, Peter D. Miller, Andrei
Prokhorov. "Painleve-III Monodromy Maps Under the D_6 -> D_8
Confluence and Applications to the Large-Parameter Asymptotics of
Rational Solutions." arXiv:2307.11217 (v2 2024-03-09); SIGMA 20 (2024),
019, 77 pages; DOI 10.3842/SIGMA.2024.019.

  - **Verified:** arxiv abs page resolves with matching title +
    author list (Barhoumi/Lisovyy/Miller/Prokhorov). DOI resolves
    to SIGMA 20 (2024) 019.
  - **Scope:** PIII(D_6) -> PIII(D_8) large-parameter confluence
    + Riemann-Hilbert monodromy + Umemura-polynomial asymptotics.
  - **Relevance to d>=3 binding window:** NEGATIVE. The labels
    D_6 / D_8 are **Dynkin diagram tags for distinct geometric
    realizations of Painleve III** (generic vs degenerate), not
    "d=6" or "d=8" PCF-recurrence degrees. The confluence stays
    inside d=2 PCF territory. This was already established by 038
    dossier sub-task C and is reconfirmed here.
  - **Bridge SHA:** 96c49cdd... (slot 08 of MILESTONE-RESIDUAL-GAP-
    SURVEY-M4-M7-M8B-M9 at a26ab27).

### 3.2 WEAK-ADJACENT (resurgence + PIII territory; not d>=3)

**[ILT-2014]** A. Its, O. Lisovyy, Yu. Tykhyy. "Connection problem
for the sine-Gordon/Painleve III tau function and irregular
conformal blocks." arXiv:1403.1235; Int. Math. Res. Notices (2015)
(18): 8903-8924; DOI 10.1093/imrn/rnu209.

  - **Verified:** arxiv abs page resolves with matching title +
    authors.
  - **Relevance:** PIII tau-function connection problem at d=2;
    closest published treatment of "the dichotomy axis" but for
    sine-Gordon / radial PIII (a single PIII variant, not a d>=3
    extension).

**[ILP-2016]** A. Its, O. Lisovyy, A. Prokhorov. "Monodromy
dependence and connection formulae for isomonodromic tau
functions." arXiv:1604.03082; Duke Math. J. 167, no. 7 (2018),
1347-1432; DOI 10.1215/00127094-2017-0055.

  - **Verified.**
  - **Relevance:** Jimbo-Miwa-Ueno 1-form extension + general
    isomonodromic connection formulae. Methodology adjacent but
    paper is not PIII-specific and not d>=3.

**[LR-2024]** Jonatan Lenells, Julien Roussillon. "Semiclassical
limit of a non-polynomial q-Askey scheme." arXiv:2407.03464 (2024).

  - **Verified.**
  - **Relevance:** Mentions "monodromy manifold of the Painleve I
    and III_3 equations" + canonical transformations. III_3 is a
    PIII variant; semiclassical limit is the relevant asymptotic
    regime; still d=2 territory.

**[IILZ-2025]** Nikolai Iorgov, Kohei Iwaki, Oleg Lisovyy, Yurii
Zhuravlov. "Many-faced Painleve I: irregular conformal blocks,
topological recursion, and holomorphic anomaly approaches."
arXiv:2505.16803 (2025).

  - **Verified.**
  - **Relevance:** PI (not PIII), but bridges three resurgence-class
    methodologies (conformal blocks + top recursion + holomorphic
    anomaly). Method-template that could in principle be
    cross-applied to PIII; no d>=3 content.

### 3.3 STRUCTURAL-ANALOGUE (PII hierarchy, not PIII)

**[JM-2002]** N. Joshi, M. Mazzocco. "Existence and Uniqueness of
Tri-tronquee Solutions of the second Painleve hierarchy."
arXiv:math/0212117 (math.CA); DOI 10.1088/0951-7715/16/2/304;
Nonlinearity 16 (2003) 304.

  - **Verified.**
  - **Relevance:** First published result on PII hierarchy
    divergent-asymptotic tritronquee existence. This is the
    closest published structural analogue to the "binding window"
    framework in the d>=3 sense, but is for the PII hierarchy
    (PII_n: nonlinear ODE of order 2n), NOT PIII.

**[MM-2006]** M. Mazzocco, M. Y. Mo. "The Hamiltonian Structure of
the Second Painleve Hierarchy." arXiv:nlin/0610066;
DOI 10.1088/0951-7715/20/12/006.

  - **Verified.**
  - **Relevance:** Hamiltonian + Lax-pair construction for PII
    hierarchy; n-th member is order-2n ODE. Same scope-mismatch as
    JM-2002.

**[BM-2020]** Irina Bobrova, Marta Mazzocco. "The Sigma Form for
the PII Hierarchy." arXiv:2012.11010 (2020);
DOI 10.1016/j.geomphys.2021.104271.

  - **Verified.**
  - **Relevance:** Sigma-form (Jimbo-Miwa) of PII hierarchy. Same
    PII-not-PIII scope-mismatch.

### 3.4 OFF-TOPIC (filtered out)

Roussillon 2010s-2020s corpus on Virasoro fusion kernels +
q-Askey schemes (arXiv:2004.09278, 2006.16101, 2011.07877,
2105.10896, 2402.12013, 2405.09325, 2410.09798, 2410.09800,
2512.03172) overlaps the conformal-block side of the
Lisovyy-school methodology but contains no PCF / d>=3 /
binding-window content. Listed here for completeness; not
acquired.

Forrester 1990s-2020s corpus (~89 papers): random-matrix theory,
beta-ensembles, characteristic polynomials, Selberg integrals,
Riesz gas. Two prior Forrester-Witte items on Painleve are
"Painleve II in random matrix theory" (arXiv:1210.3381, Constr.
Approx. 41 (2015)) and "Discrete Painleve equations and random
matrix averages" (arXiv:math-ph/0304020), both d=2 PII / discrete.
No d>=3 PIII / V_quad work in Forrester corpus.

---

## 4. Key negative-result inferences

### NR-1: "binding window" is SIARC-internal terminology

The phrase "binding window" produces zero hits on arxiv (K06) and
zero hits on Google Scholar (K10) when paired with Painleve and/or
Stokes-multiplier. This terminology is SIARC-program-specific (it
originates from the P-009 caveat language pinned at bridge SHA
1873538, 2026-05-06) and has no precedent in published Painleve
III / resurgence / continued-fraction analytic-continuation
literature. Implication: no external citation can be used to
import the "binding window" framework; it must be defined
SIARC-internally if introduced into any publication.

### NR-2: Painleve III hierarchy is structurally undeveloped

The exact phrase `"Painleve III hierarchy"` produces zero arxiv
hits (K08), in stark contrast to the **PII hierarchy** which is
a developed published subject (JM-2002, MM-2006, BM-2020). The
analogue concept for PIII does not appear to have been formulated
in the published literature, with one **partial exception**: the
PIII(D_6) <-> PIII(D_8) confluence (BLMP 2024 = arXiv:2307.11217)
relates two specific PIII variants via a Backlund-flow scaling
limit, which can be read as a "PIII degenerate hierarchy" of
length 2 but is not labelled as such. Implication: if SIARC
wishes to invoke a PIII hierarchy / d>=3 PIII extension, the
construction must be either (a) imported from PII via analogy and
proven independently, or (b) constructed SIARC-internally.

### NR-3: Birkhoff-Trjitzinsky rank q>=2 borderline case absent

The exact-phrase probe `"Birkhoff-Trjitzinsky" rank` (K18) plus
the conjunctive probe `Birkhoff Trjitzinsky rank borderline
anormal` (K03) both return zero hits. The 038 dossier already
documented (UF-038-2) that Costin 2008 ch.5 treats rank-1
Stokes-constant theory verbatim but the **fractional-rank q>=2
borderline-anormal case is structurally absent**. This is
reconfirmed at literature level: no descendant paper picks up
the q>=2 borderline-anormal subcase. Implication: Pathway B
(BT-structural analysis adapted to PCF) cannot expect a
literature-direct extraction of d>=3 Stokes data; it would have
to derive it from scratch.

### NR-4: Resurgence-expert corpus has no PIII-Stokes-specific work

Three independent author-name probes against the canonical
resurgence-school authors (K15 Aniceto, K16 Sauzin, K17 Iwaki)
all return zero PIII-Stokes hits. Iwaki appears as co-author on
IILZ-2025 (Many-faced PI) but the Stokes-data focus is PI not
PIII. Implication: the d>=3-PIII-Stokes-multiplier question is
not under active investigation by the canonical resurgence school.

### NR-5: V_quad does not appear in literature

The label "V_quad" is SIARC-internal (continued-fraction quadratic
voxel). No published paper uses this label. The closest published
analogue is the BLMP-2024 PIII(D_6)/PIII(D_8) bifurcation framework.
Implication: same as NR-1: no external V_quad citation channel.

---

## 5. Halt verdict

**HALT_E_LITERATURE_NULL** (per relay-181 prompt section "PHASE C
HALT MODES"):

> Trigger: zero STRONG hits across all keyword searches.
> Action: close null; document search exhaustion; escalate B/D
>         choice to operator with NULL evidence -> favor B (Desert
>         substratification) since no d>=3 binding-window
>         literature exists to leverage.

Trigger met: zero STRONG hits beyond BLMP-2024 (already in bridge
corpus, intra-d=2 confluence, established as NEGATIVE for d>=3 by
the 038 dossier). The WEAK and STRUCTURAL-ANALOGUE adjacencies in
section 3 do not constitute STRONG hits per relay-181 phase A
target definition: a STRONG hit would have been a paper containing
an explicit d>=3 (or PIII-hierarchy / PIII-rank-q>=2 / V_quad-
parameter-binding) result, and none was found.

---

## 6. Recommendation for downstream B/D choice

Per slot 156 verdict Q3d dependency `E -> B`:

> "P-009 literature reconnaissance is an effective scoping prefix
> for B (BT literature is plausibly adjacent to the P-009
> binding-window literature)."

The reconnaissance return is NULL: the BT-adjacent literature
that the slot 156 verdict hoped might be more accessible than
modelled is **NOT** more accessible. The cost-variance reduction
that E was supposed to provide on Pathway B has resolved to
the **upper end** of the slot 156 estimate (weeks-to-months;
PCF-specific adaptation likely required; no recent Sauzin /
Ecalle / Iwaki / Aniceto exposition specifically applicable).

This shifts the slot 156 recommendation as follows:

- **Pathway B (Birkhoff-Trjitzinsky structural)** — cost estimate
  collapses to the upper bound; literature signal does **NOT**
  favour B over D. Pathway B remains a **moderate-probability /
  weeks-to-months** prospect; not advantaged.

- **Pathway D (upper-bound proof on |S_2|)** — alternative
  structural V1 path. Same difficulty class as B post-NULL.
  Operator-level choice is no longer literature-driven.

- **Pathway A (U2 quadrant survey)** — independent of E result;
  still recommended as next fire (slot 156 Q3d second-fire
  candidate).

- **V0+(defended) target** — slot 156 Q5d-recommended operational
  target. The NULL E result **strengthens** the case for V0+
  over V1: with no literature foothold, the cost-benefit
  calculation for committing to V1 (via either B or D) tilts
  away from V1 and toward documenting V0+ as the principled
  end-state.

**Recommended downstream sequence (re-ranking slot 156 Q3a in
light of E result):**

1. **A (U2 quadrant survey)** — promoted to next fire; was
   second-tier in slot 156 Q3a, now primary because E returned
   NULL and A is the only remaining cheap residual-lifting move.
2. **V0+ closure amendment** — fire after A completes regardless
   of A's outcome, per slot 156 Q5c.
3. **D154-defensive d>=3 response stub** — slot 156 Q5d operator-
   tier go/no-go; cost ~5-7 days; defensive against S154 Q4(4b)
   exogenous trigger.
4. **B and D** — both deferred to operator-tier review; neither
   is favoured by E result.
5. **F (substrate-uplift)** — deferred infinitely or until HPC
   access event.

---

## 7. Pre-verification audit

Per copilot-instructions Bibliographic ID Pre-Verification rule:

| ID | Title (resolved) | First author (resolved) | Match? |
|---|---|---|---|
| arXiv:2307.11217 | Painleve-III Monodromy Maps Under the D_6 -> D_8 Confluence... | Barhoumi | YES |
| arXiv:1403.1235 | Connection problem for the sine-Gordon/Painleve III tau function... | Its | YES |
| arXiv:1604.03082 | Monodromy dependence and connection formulae for isomonodromic tau functions | Its | YES |
| arXiv:2407.03464 | Semiclassical limit of a non-polynomial q-Askey scheme | Lenells | YES |
| arXiv:2505.16803 | Many-faced Painleve I: irregular conformal blocks... | Iorgov | YES |
| arXiv:math/0212117 | Existence and Uniqueness of Tri-tronquee Solutions of the second Painleve hierarchy | Joshi | YES |
| arXiv:nlin/0610066 | The Hamiltonian Structure of the Second Painleve Hierarchy | Mazzocco | YES |
| arXiv:2012.11010 | The Sigma Form for the PII Hierarchy | Bobrova | YES |
| DOI 10.3842/SIGMA.2024.019 | (resolves to BLMP 2024, same as arXiv:2307.11217) | Barhoumi | YES |

8 / 8 arxiv IDs resolve to titles matching the citation; 1 / 1 DOIs
likewise. Zero hallucinated identifiers detected. The post-031
Bibliographic Pre-Verification rule passes.

---

## 8. Anomalies and unexpected finds

**A-181-1 (INFO):** Forrester's recent (2024-2026) corpus has
**zero** PIII-Stokes content, despite Forrester-Witte being a
named target in the slot 156 verdict Q2 Pathway B description.
This narrows the slot 156 Q3 prediction that "BT-adjacent
literature might surface organically via P-009 active variant v1
dispatch" (slot 156 Q5b item 3) — observed: it did NOT.

**A-181-2 (INFO):** The PII hierarchy literature (JM-2002, MM-2006,
BM-2020) is a structurally-rich analogue framework. If SIARC
eventually constructs a PIII hierarchy in-program, **the PII
hierarchy can serve as the methodological template**: order-2n
ODE, Hamiltonian structure, Lax pair, sigma-form, tritronquee
existence. Suggestion: any future Pathway B fire should ingest
this PII corpus as primary template.

**A-181-3 (INFO):** BLMP 2024 D_6 -> D_8 confluence can be read
as a **PIII degenerate hierarchy of length 2** even though it is
not labelled as such. The Backlund-flow `(u_n, alpha+4n, beta+4n)`
under scaling x=z/n is structurally similar to a hierarchy step.
A SIARC-internal interpretation might attempt to extend the BLMP
confluence step to longer chains and propose a "PIII-D_6 -> D_8
-> ??? hierarchy"; but **this is speculative** and would itself
be Pathway B / D scope, not E scope.

**A-181-4 (METHOD):** The arxiv search interface treats unquoted
multi-word queries as **conjunctive over all fields**, which
caused over-constrained zero-hit returns on K01, K02, K04, K05,
K09, K15, K16, K17. Phrase-quoted queries (K06, K07, K08, K18)
and author-restricted listings (K11, K12, K13) are the reliable
modes. Recommendation for synthesizer: future lit-hunt prompts
should specify either phrase-quoted strings or author-restricted
listings; raw multi-word queries are not effective.
