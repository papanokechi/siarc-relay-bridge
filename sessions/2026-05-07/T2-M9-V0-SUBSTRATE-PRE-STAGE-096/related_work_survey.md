# Related-work survey — V0 substrate Phase D

**Relay:** 096 T2-M9-V0-SUBSTRATE-PRE-STAGE
**Tier:** TIER-A.3 (related-work survey for V0 announcement)
**Status:** DRAFT_SUBSTRATE
**Anchor:** citation_pre_verification_2026-05-07.md (3 of 4
identifiers VERIFIED; 3 hallucinated identifiers explicitly
EXCLUDED per post-031 rule)

---

## 1. Pre-verification provenance

All identifiers in the table below are pre-resolved per
post-031 verdict rule (copilot-instructions.md §"Bibliographic
identifier pre-verification"). Source for the V/C-prefixed
anchors: `tex/submitted/control center/citation_pre_verification_
2026-05-07.md` re-resolved fresh at 096 fire time. The three
hallucinated identifiers `1612.08374` / `1702.06894` /
`1811.03108` are explicitly **NOT** included anywhere in V0
substrate.

---

## 2. Structured related-work table

| ID | Authors | Year | Venue | Phi-relevance | Status |
|----|---------|------|-------|---------------|--------|
| **V1** | Barhoumi, Lisovyy, Miller, Prokhorov | 2024 | SIGMA 20 (2024) 019, 77 pp; arXiv:2307.11217; DOI 10.3842/SIGMA.2024.019 | $P_{\mathrm{III}}(D_6)$ generic-form monodromy maps; $D_6 \to D_8$ confluence; Bäcklund / Schlesinger morphism data on tau functions; Umemura-polynomial connection. **Direct anchor for the Phi target side at the Stokes-data axis.** | **VERIFIED** (re-resolved at 096 fire time; v2 from 2024-03-09) |
| **V2** | Its, Lisovyy, Prokhorov | 2018 | Duke MJ 167:7, 1347-1432; arXiv:1604.03082; DOI 10.1215/00127094-2017-0055 | Extension of the Jimbo-Miwa-Ueno 1-form to extended monodromy data; closed 1-form on full monodromy-data space; explicit constant factors in connection formulae for Painlevé-VI tau function and Painlevé-II tau function. **Connection-formula machinery directly cited by Phi target morphism description.** | **VERIFIED** (re-resolved at 096 fire time; v4 from 2018-10-29) |
| **C1** | Jimbo, Miwa, Ueno | 1981 | Physica D 2 (1981) and Physica D 4 (1981); canonical 3-paper series | Defines the JMU 1-form for monodromy preservation; cited and explicitly extended in V2. **Foundation anchor for the Phi target morphism description.** | **CANONICAL** (pre-known; cite by author-year, not arXiv ID) |
| **C2** | Okamoto | 1987 | Annali / Funkcialaj Ekvacioj / etc.; multi-paper Hamiltonian-structure series 1986-1987 | Hamiltonian structure for Painlevé family; original $(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0)$ Okamoto-coordinate parametrization. **R5 Lax-pair anchor for $V_{\mathrm{quad}} \to P_{\mathrm{III}}(D_6)$ normalization map.** | **CANONICAL (audit anchor)** + W21 LANE-1 acquisition jurisdiction; downgraded post-synthesis to "audit anchor" not "blocker" per 4-of-4 reviewer convergence |
| **V5** | Conte, Musette | 2020 | *The Painlevé Handbook* 2nd ed.; Springer Mathematical Physics Studies; DOI 10.1007/978-3-030-53340-3 | General Painlevé reference; algorithmic Painlevé test (T3 anchor); CT v1.3 + PCF-2 v1.3 § cited; ch. 7 (transformations / solutions) **chapter-content unverified — institutional-access TOC scan recommended pre-V0 fire** | **VERIFIED book** + chapter content TENTATIVE per `citation_pre_verification_2026-05-07.md` "Outstanding" row |
| --- | Mazzocco | various | various | Painlevé moduli + Riemann-Hilbert correspondence; cited by Reviewer A (Q6 + Q8) as related-work touchstone for the moduli-side framing of $\Phi$. **OPERATOR-SIDE PIVOT** per W21 LANE-1 jurisdiction (specific paper IDs not pre-verified at 096 fire time; defer per post-031 rule). | RELATED (operator-side acquisition; specific paper IDs deferred) |
| --- | Garoufalidis, Kashaev | various | various | Quantum modular forms; categorification machinery; cited by Reviewer A (Q6 + Q8) as future categorical-coherence framing for M13 follow-up. | RELATED (TIER-C / M13 forward-pointer; not in V0 critical-path) |
| --- | Lisovyy, Roussillon | 2017 (Painlevé I connection problem; J. Phys. A 50:255202) | J. Phys. A 50 (2017) 255202 | Connection problem for Painlevé I; the **real arXiv ID was not successfully discovered at 2026-05-07 pre-verification**; web-search returned two hallucinated IDs (1702.06894 + 1811.03108). **DO NOT cite by arXiv ID without re-acquiring.** Cite by author-year + journal only. **De-prioritized** for V0 (Painlevé I focus, not $P_{\mathrm{III}}(D_6)$). | UNVERIFIED-ARXIV-ID; cite by author-year-journal only; de-prioritized |

### 2.1 Cross-walk to Phi components

| Phi component | Primary anchor | Secondary anchor | Tertiary |
|---------------|---------------|------------------|----------|
| Source category PCF families | PCF-1 v1.3 + PCF-2 v1.3 + CT v1.3 (Zenodo records) | picture v1.19 §3 + §4 | --- |
| Target $\xi_0$ axis | D2-NOTE v2.1 (Zenodo `10.5281/zenodo.20015923`) | Wasow §X.3 / §19 (R5 acquisition) | Birkhoff 1930; B-T 1933 §§4-6 |
| Target $\Delta_d$ axis | PCF-1 v1.3 §6 + PCF-2 v1.3 §6 | Q22 deposit memo (path-(a) $\lvert\delta_a\rvert = 3.09 \times 10^{-23}$) | --- |
| Target $\|\Delta\|_{\mathrm{Pet}}$ axis | PCF-1 v1.3 §6 | Q22 deposit memo | --- |
| Stokes-data secondary axis | V1 (Barhoumi-Lisovyy-Miller-Prokhorov 2024) | V2 (Its-Lisovyy-Prokhorov 2018) | C1 (JMU 1981); C2 (Okamoto 1987 R5 audit anchor) |
| Painlevé classification leg | V5 (Conte-Musette handbook 2nd ed. 2020) | T3 verdict + 007 prompt anchor | --- |

---

## 3. Per-row annotation (1 paragraph each)

### V1 — Barhoumi-Lisovyy-Miller-Prokhorov 2024 (arXiv:2307.11217 / SIGMA 20 019)

This is the most direct related-work anchor for the V0 V_quad
$\to P_{\mathrm{III}}(D_6)$ Stokes-data axis. The paper studies
the generic-form Painlevé-III equation
$$
\tfrac{\mathrm{d}^2 u}{\mathrm{d} x^2} = \tfrac{1}{u}
\bigl(\tfrac{\mathrm{d} u}{\mathrm{d} x}\bigr)^2 - \tfrac{1}{x}
\tfrac{\mathrm{d} u}{\mathrm{d} x} + \tfrac{\alpha u^2 + \beta}{x}
+ 4 u^3 - \tfrac{4}{u},
$$
applies an explicit Bäcklund transformation generating
$(u_n(x), \alpha + 4n, \beta + 4n)$, and identifies the
$x = z/n$ scaling limit as a $P_{\mathrm{III}}(D_8)$ solution
characterized by its monodromy data. The Riemann-Hilbert
representation in §§3-4 + the Umemura-polynomial connection in
§5 are the substrate the V0 announcement points to as the
target-side morphism description in `phi_assignment_statement.md`
§3.3. The 50-row cubic catalogue (PCF-2 v1.3 §6.B) sits
upstream of the source side; V1 is the downstream anchor for
the target side.

### V2 — Its-Lisovyy-Prokhorov 2018 (arXiv:1604.03082 / Duke MJ 167:7)

This is the connection-formula anchor for the Phi target. The
paper extends the Jimbo-Miwa-Ueno 1-form to a closed 1-form
on the full extended-monodromy-data space (after Bertola
generalizing Malgrange) and uses the closure to evaluate
constant factors in connection formulae for the Painlevé-VI
tau function and Painlevé-II tau function. The V0 announcement
references V2 to anchor the assertion that
**connection-formula machinery for Painlevé-III tau functions
exists in the literature** (V1 + V2 jointly), so the M9
announcement does not assume a categorical-level statement
beyond what is available in print.

### C1 — Jimbo-Miwa-Ueno 1981 (Physica D series)

The original JMU 1-form for monodromy preservation. Cited as
canonical foundation for the Phi target morphism description;
no acquisition gap (well-known). The role in V0 substrate is
to make explicit that **$\Phi$ on morphisms is described
relative to the JMU framework**, not relative to an
agent-introduced novel framework.

### C2 — Okamoto 1987 (Hamiltonian-structure series)

The original $(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0)$
Okamoto-coordinate parametrization. Picture v1.19 §5 G18 row
flags a specific four-tuple $(1/6, 0, 0, -1/2)$ summing to
$-1/3$ rather than $0$ (the Okamoto null-sum constraint as
quoted in the program-internal substrate); G18 is LOW-severity
convention-class and forward-pointed for operator pin from
Okamoto 1987 §2 once acquired. **This is the R5 / R8
acquisition gap** flagged at the M6.CC R1 carry-forward
level (069 + 075). For V0 substrate: cite by author-year
("Okamoto 1987 §2"), preserve operator-side acquisition plan
without blocking V0 fire.

### V5 — Conte-Musette 2020 (*The Painlevé Handbook* 2nd ed.; Springer)

The canonical Painlevé-equations textbook reference. The 2nd
edition (Springer DOI 10.1007/978-3-030-53340-3; 9 chapters;
Mathematical Physics Studies series) was published 2020. Used
in the program as the canonical anchor for the algorithmic
Painlevé test (T3 / 007 verdict), and cited in CT v1.3 §3.5 +
PCF-2 v1.3 catalogue. Note from `citation_pre_verification_
2026-05-07.md`: ch. 7 specific content (transformations /
solutions / normalization map) is **TENTATIVE** — Reviewers
A, B, C asserted it covers the normalization-map material; the
chapter assignment is not directly verified by the agent
without institutional-access TOC scan. V0 substrate cites V5
as **general Painlevé reference**, not as primary
normalization-map source.

### Mazzocco (operator-side pivot)

Reviewer A (Q6 + Q8) cited Mazzocco's body of work on
$P_{\mathrm{VI}}$ moduli and Riemann-Hilbert correspondence as
relevant related-work for the Phi moduli-side framing.
Specific paper IDs were not pre-verified at 096 fire time;
operator-side acquisition is W21 LANE-1 jurisdiction. **Cite
by author-name only in V0 substrate; specific paper IDs
deferred until pre-verified.** Risk: same hallucination pattern
as 1612.08374 / 1702.06894 / 1811.03108 if entered prematurely.

### Garoufalidis-Kashaev (M13 forward-pointer)

Reviewer A (Q6 + Q8) cited Garoufalidis-Kashaev's work on
quantum modular forms / categorification as relevant for the
M13 follow-up (TIER-C; full Riemann-Hilbert correspondence at
Stokes-data level + categorical-coherence verification). Not
in V0 critical-path. **Cite by author-name in V0 related-work
matter as forward-pointer to TIER-C; do not lean on as
primary source for V0 announcement claims.**

### Lisovyy-Roussillon 2017 (Painlevé I connection problem; UNVERIFIED-ARXIV-ID)

Real paper; published in J. Phys. A 50 (2017) 255202; **the
real arXiv ID was not discovered at 2026-05-07 pre-verification
attempts** (web search returned two hallucinated IDs that
resolved to unrelated papers per `citation_pre_verification_
2026-05-07.md` H2 + H3). For V0 substrate: cite by
author-year-journal only; **do not enter any arXiv ID without
re-acquiring via direct arxiv.org search**. Painlevé-I focus
makes this de-prioritized for V0 (V0 target is
$P_{\mathrm{III}}(D_6)$, not $P_{\mathrm{I}}$).

---

## 4. Substrate-gap closure matrix

For each related-work row, the V0-fire substrate closure path:

| ID | V0-fire status | Forward-pointed acquisition |
|----|----------------|------------------------------|
| V1 | READY | --- |
| V2 | READY | --- |
| C1 | READY (carry-forward) | --- |
| C2 | AUDIT-ANCHOR | W21 LANE-1 R5 Okamoto 1987 §§2-3 acquisition |
| V5 | READY (general); ch. 7 TENTATIVE | Pre-V0-fire institutional-access TOC scan |
| Mazzocco | DEFERRED | W21 LANE-1 specific paper ID pre-verification |
| Garoufalidis-Kashaev | M13 forward-pointer | TIER-C scope; not V0-fire critical |
| Lisovyy-Roussillon 2017 | DEFERRED | Re-acquire via direct arxiv.org search before any cite |

---

## 5. AEAL anchor block

* related_work_survey.md SHA-256: computed at fire end in
  `claims.jsonl` 096-D-1.
* citation_pre_verification anchor: SHA-16 prefix to be
  recorded in claims.jsonl.
* picture v1.19 anchor: SHA-16 prefix `8BD9043370872F07`.

---

End related_work_survey.md.
