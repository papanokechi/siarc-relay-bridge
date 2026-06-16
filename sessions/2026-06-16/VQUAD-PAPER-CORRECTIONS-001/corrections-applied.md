# Corrections applied — VQUAD-PAPER-CORRECTIONS-001

Canonical spec: `VQUAD-COLDREAD-001/corrections-list.md`. DOIs sourced ONLY from
`VQUAD-ZENODO-PREP-001/related-identifiers.md` (cross-checked against the SIARC ledger
`submitted/submission_log.txt` for titles). No DOI from memory.

Status of this pass: **1 HIGH operator-verified + inserted + 4 MED applied + 5 LOW applied + Stage-4
bibliography repoint (B-1…B-4).**
No numerical result altered (all edits expository / bibliographic / terminological).

---

## MED

### M-1 — "Stokes multiplier = C" terminology (section-5.md, was .tex L804)
- **Location:** `section-5.md`, Method A wrap-up (the `I_gamma` subdominant-solution sentence).
- **Before:** "...that constant is by definition the Stokes multiplier `=C` (in the normalisation of
  Thm main-restated)."
- **After:** "...that constant is the *connection coefficient* C (...) — the Stokes multiplier of
  L_phi reweighted by the algebraic Gamma-factor |Gamma(beta)|/2pi, C=(|Gamma(beta)|/2pi)·S, as
  Methods B and C make explicit."
- **Why:** removes the collision with §5.3, where the *Stokes multiplier* is S_mult with
  |S_mult|=2piK=S. C is the reweighted datum, not the multiplier itself. Math unchanged (this is
  eq:main-recentred). 

### M-2 — global C/S terminology pass
- Reserve **"Stokes constant / Stokes multiplier" for S = 2piK** and **"connection coefficient" for
  C = |Gamma(beta)|K** throughout.
- **Second collision found by the global scan (NOT in the cold-read line list):** `section-5.md`
  §5.2 Method-A intro — "...the V_quad linear equation whose **Stokes multiplier** is C."
  → "...whose **connection coefficient** is C." (M-2 mandates fixing all instances, not only L804.)
- **Verified consistent (left as-is, correct):** `section-5.md` L24 ("the Stokes multiplier relation
  S_mult=2pi i A/Gamma(1+beta)"), §5.3 L124-134 (S_mult definition, |S_mult|=2piK=S). No other
  collisions remain (grep `Stokes multiplier` → only S_mult usages).

### M-3 — topological-recursion / Marchal SOTA (the Lecerf-criterion-3 gap)
Three bibitems added to `section-9-references.md`, **titles verified via CrossRef DOI resolution**
(memory/guess would have been wrong — see note):
- `MarchalOrantin` — Marchal & Orantin, *Isomonodromic deformations of a rational differential
  system and reconstruction with the topological recursion: the sl_2 case*, J. Math. Phys. **61**
  (2020) no. 6, 061506. DOI `10.1063/5.0002260`.
- `IwakiMarchalSaenz` — Iwaki, Marchal & Saenz, *Painlevé equations, topological type property and
  reconstruction by the topological recursion*, J. Geom. Phys. **124** (2018) 16–54. DOI
  `10.1016/j.geomphys.2017.10.009`.
- `MarchalAlameddine` — Marchal & Alameddine, *Hamiltonian representation of isomonodromic
  deformations of twisted rational connections: the Painlevé 1 hierarchy*, Comm. Math. Phys. **406**
  (2024) no. 1, art. 12. DOI `10.1007/s00220-024-05187-0`.
- **Text added:**
  - `section-7.md` new `\subsection{Relation to topological recursion}` (§7.4) positioning the
    holonomic/Borel route as complementary: TR computes the tau-series + Stokes constants from a
    spectral curve; we isolate the minimal operator L_V with an exact Q(sqrt3) certificate and
    extract the *period* of the Stokes datum; the two meet at S=2piK.
  - `section-2.md` Rmk:provenance (§2.2, the "no classical Lax pair" touchpoint) — one
    contextual sentence: isomonodromic Lax systems/Stokes data for Painlevé are constructible from
    spectral curves by topological recursion + isomonodromic Hamiltonian methods; the holonomic
    route here is independent of that construction.
- **DOI source-cite:** all three DOIs verbatim from `related-identifiers.md`
  (Marchal–Alameddine `10.1007/s00220-024-05187-0`; Iwaki–Marchal–Saenz `10.1016/...`;
  Marchal–Orantin `10.1063/5.0002260` — the verified one; the hallucinated `10.1063/1.5135288`
  was explicitly avoided).
- **CrossRef-vs-guess note (AEAL):** the Marchal–Alameddine title and volume were verified by DOI
  resolution. CrossRef returns *"...Twisted Rational Connections: The Painlevé 1 Hierarchy"*, vol
  **406** — not the "general rational connections on gl_2 / vol 405" a from-memory draft would have
  produced. Title verification was load-bearing.

### M-4 — fill the Sakai concept-DOI placeholder
- **Location:** `section-9-references.md`, `\bibitem{Sakai}`.
- **Before:** "Zenodo deposit, 2026. [Concept DOI to be inserted by the operator at submission time.]"
- **After:** "Zenodo, 2026, concept DOI `10.5281/zenodo.20694840`."
- **DOI source-cite:** `related-identifiers.md` (Sakai-stratification program concept). Authoritative.

---

## LOW

### L-1 — sibling cross-references (EBR-Ib, EBR-II, δ-Fredholm)
Three bibitems added to `section-9-references.md`; **titles verified against the SIARC ledger**
`submitted/submission_log.txt`; **concept DOIs from `related-identifiers.md`:**
- `EBRIb` — *Removing the Positivity Hypothesis: Edge–Borel Location and Type for Sign-Varying
  Polynomial Continued Fractions*, Zenodo 2026, concept `10.5281/zenodo.20569723`
  (ledger §B Item 29; record 20569724).
- `EBRII` — *The EBR Amplitude as a Connection Coefficient: Characterization and a Rigidity
  Dividing-Line Conjecture*, Zenodo 2026, concept `10.5281/zenodo.20566465`
  (ledger §B Item 31; record 20571232).
- `FredDelta` — *A Fredholm-determinant representation of the pcf-δ growth constant: finite
  identity, entire order and genus*, Zenodo 2026, concept `10.5281/zenodo.20624813`
  (ledger §B Item 22; record 20624814).
- **Text added:** `section-7.md` §7.1 closing sentence — "Adjacent instances in the same program
  corroborate the pattern: the Edge–Borel ring papers characterise the connection/amplitude datum of
  related PCF families [EBRIb,EBRII], and a companion Fredholm-determinant representation realises a
  related pcf growth constant as an explicit determinant [FredDelta]." All three cited.

### L-2 — tighten `eq:periodmatrix` "read off as" phrasing
- **Location:** `section-6.md`, after `eq:periodmatrix`.
- **Before:** "...C=|Gamma(beta)|K is **read off as** the Stokes-entry × amplitude combination
  |A|/|beta|."
- **After:** "...the connection coefficient C=|Gamma(beta)|K=|A|/|beta| **is the period pairing
  assembled from these entries** via the branch amplitude |A|=K·Gamma(1+beta), **not itself an entry
  of P(M)**." (Precise; consistent with §4.2 / eq:methodB-period.)

### L-3 — abstract order-4/order-2 clause
- **Location:** `preamble.tex`, abstract.
- **Before:** "...holonomic of order 4 with coefficients in Q(sqrt3);"
- **After:** "...holonomic of order 4 **(the Borel–Laplace dual of the order-2 operator annihilating
  the series)** with coefficients in Q(sqrt3);" (matches corrections-list L-3 verbatim intent).

### L-4 — `\thanks`
- **Location:** `preamble.tex`.
- **Before:** "ORCID 0009-0000-6192-8273. This is a working draft; not yet submitted."
- **After:** "ORCID 0009-0000-6192-8273." (Dropped the stale "working draft" sentence; left
  venue-neutral. Operator may add venue/acknowledgement text at submission — corrections-list marks
  L-4 an operator-at-submission item; this is the minimal always-true state.)

### L-5 — `(1/2)^n` numerical-floor citation
- **Location:** `section-2.md`, proof of `cor:finite` (the "infinite alien tower does not exist"
  sentence).
- **Before:** "...suggested by the (1/2)^n numerical floor **in the parent probe** does not exist;"
- **After:** "...suggested by the (1/2)^n numerical floor **reported in the parent probe
  (`PERIOD-REP-VQUAD-001`, `numerical-check.md`)** does not exist;"
- **Source-cite:** the (1/2)^n / 2-instanton-at-2·xi0 floor is the T2 Borel-singularity census in
  `PERIOD-REP-VQUAD-001/scripts/numcheck_period_rep.py` (L146-153), summarised in that slot's
  `numerical-check.md`. Citation format matches the paper's existing convention (section-4.md L6).

---

## HIGH (OPERATOR-VERIFIED — inserted in Stage 4)

### H-1 — provenance of the value 0.43770528…
- **Status:** OPERATOR-VERIFIED (2026-06-16) and **INSERTED** at `section-4.md` §4.3 "The constants",
  immediately after the bridge-identity sentence (L69), as
  `\begin{remark}[Provenance of the value $0.43770528\ldots$]\label{rmk:provenance-C}`.
- **Operator verification:** claims (a),(b),(c),(e) confirmed; (d) confirmed with refinement — the
  correction is the companion's *Version 1.1* Remark 6.2, and record `20481592` is companion v1.2
  (concept `20455089`). Remark inserted verbatim from `h1-remark-draft.md`; `\eqref{eq:bridge}` and
  `\eqref{eq:C-from-A}` both resolve.
- **Rebuild:** PDF regenerated, new SHA `4CA12A35…` (build-result.md); H-1 text confirmed present in
  the rendered PDF.

---

## Conflicts flagged (prompt summary vs canonical corrections-list.md — canonical wins)

1. **Normalization alignment** (`L_{1,2}=x^2+(1/3)x+1/3`, "Marchal convention"): mentioned in the
   task-prompt summary (Stage 1.2), **absent from corrections-list.md**, and would be a
   **mathematical** change (forbidden — "never alter a numerical result"). The prompt itself
   conditions it on "if corrections-list.md specifies it"; it does not. **SKIPPED.**
2. **"Marchal personal communication (June 2026, permission granted)"** citation: at the Stage-3
   halt this was flagged unverifiable (AEAL) and **deferred to operator decision**. **RESOLVED in
   Stage 4:** the operator confirmed they hold the granted permission (AEAL barrier cleared) and
   directed it be ADDED as an acknowledgement-only line (see B-4 below). The 3 published,
   CrossRef-verified Marchal citations (M-3) remain unchanged.

---

## Stage 4 (post-H-1 operator instruction) — bibliography repoint, Trap-6 purge, acknowledgement

On H-1 resolution the operator issued additional corrections. These CORRECT pre-existing bibitem
content (the `[Vquad]`/`[StokesNote]` titles were inherited from the parent paper, not introduced by
the Stage-1 M-3/L-1 edits) and clear the Stage-3 conflict-2.

### B-1 — `[Vquad]` repointed to the concept DOI
- **Before:** title "The V_quad polynomial continued fraction: a Painlevé-V standalone closure on the
  Sakai surface D_5^{(1)}"; **version DOI 10.5281/zenodo.20455090** (concept 20455089).
- **After:** real deposit title "A non-classical Painlevé V transcendent from a quadratic polynomial
  continued fraction: surface classification and resurgent Stokes data"; **concept DOI
  10.5281/zenodo.20455089** only. The retracted-S v1.0 lead `20455090` is DROPPED.
- **Why:** `[Vquad]` and `[StokesNote]` are ONE deposit (shared concept 20455089) at two versions;
  headline-citing the retracted v1.0 (20455090) is exactly the trap H-1 guards against.

### B-2 — `[StokesNote]` retitled + version-annotated
- **Before:** invented title "V_quad companion (v1.2): the Stokes constant S=2πK and its resurgent
  reading"; DOI 10.5281/zenodo.20481592.
- **After:** same real deposit title as `[Vquad]`; **version DOI 10.5281/zenodo.20481592** kept,
  annotated "(version 1.2; the Stokes-constant correction is Remark 6.2 / eq. (13))".

### B-3 — Trap-6 cross-check (second retracted-DOI instance) — `section-8.md` §A.5
- Operator asked to scan for other version-DOI-where-concept-belongs. The scan over ALL sources found
  the retracted `20455090` in exactly **two** places: the `[Vquad]` bibitem (B-1) and the
  **reproducibility statement** (`section-8.md` §A.5), which headlined "The parent V_quad deposit is
  Zenodo 10.5281/zenodo.20455090 (concept …20455089)".
- **Fix:** repointed to concept `10.5281/zenodo.20455089`; calibration line annotated "in version 1.2,
  10.5281/zenodo.20481592". Post-fix: `20455090` ABSENT from every source and from the rendered PDF
  text (build-result.md). No other Trap-6 instances exist.

### B-4 — Marchal personal-communication acknowledgement (clears conflict-2)
- Added `\section*{Acknowledgements}` to `section-7.md` (after Open problems, before `\appendix`):
  "We thank O. Marchal for correspondence on the topological-recursion reconstruction of Painlevé
  Stokes data (personal communication, June 2026)." Operator holds the granted permission;
  acknowledgement-only, not load-bearing.

All Stage-4 edits are bibliographic/expository; no numerical result altered (verification-pass.md).
