# VQUAD-COLDREAD-001 — Prioritized corrections list

Input to **VQUAD-PAPER-CORRECTIONS-001**. Line numbers reference
`vquad-periodrep-paper.tex` (1352 lines) as read this slot. No correction below changes a graded
mathematical result; all are provenance / terminology / citation-completeness / operator-fill /
polish. Total prose added ≈ ≤1 page (page budget ≤30 pp preserved).

Priorities: **H** = do before deposit (credibility / correctness-of-claim risk);
**M** = should do before a flagship submission; **L** = polish, low risk if deferred.

---

## H-1 [HIGH] — Disambiguate `C = 0.43770528…` from the retracted v1.0 Stokes value

- **Where:** §1.1/§1.2 (after eq:constants is introduced) or §4.3 "The constants" (around L697–707),
  and/or a one-line footnote at the first appearance of `C = |Γ(β)|K` (L95–98 / L142 / L703).
- **Issue:** the headline connection coefficient `C = |Γ(β)|K = 0.4377052861935…` is numerically
  identical to the value retracted as the V_quad **Stokes constant** in the companion note
  (v1.0 used prefactor `|Γ(β)| = 6.00599` in place of `2π`; corrected to `S = 2πK = 0.45790662`
  in v1.1/v1.2, cite StokesNote 20481592). Verified this slot: `6.00599 = |Γ(β)|`,
  `|Γ(β)|K = 0.43770528…`, `2πK = 0.45790662…`, `C/S = |Γ(β)|/2π = 0.95588…`.
- **Why HIGH:** the paper is *correct* (C ≠ S; |Γ(β)| is the right prefactor for the connection
  coefficient, the wrong one for the Stokes constant), but never flags that `0.43770528` is the
  ex-retracted number. A referee/program reader who recognises it will doubt the paper unless
  pre-empted. Cheap to fix; high downside if missed.
- **Fix (suggested remark):** add ~3 sentences, e.g.:
  > "The value `|Γ(β)|K = 0.4377052…` should not be confused with the V_quad Stokes constant
  > `S = 2πK = 0.4579066…` (cite StokesNote): they are distinct period data related by the bridge
  > `C = (|Γ(β)|/2π)S`. An early computation of the companion note carried the factor `|Γ(β)|`
  > where `2π` was required for the Stokes constant; the present analysis identifies `|Γ(β)|K`
  > correctly as the *connection coefficient* C, not the Stokes constant, resolving that
  > normalisation structurally."
- **Bonus:** this converts the liability into a showcase of the paper's explanatory power.
- **AEAL source:** corpus memory "Stokes constant S" (retracted 0.43770528 / prefactor −6.00599);
  companion v1.2 deposit 10.5281/zenodo.20481592; mpmath recheck in this slot's `claims.jsonl`.

---

## M-1 [MED] — Fix the "Stokes multiplier = C" conflation at L804

- **Where:** §5.1 Method A, L800–805 ("…that constant is by definition the Stokes multiplier = C").
- **Issue:** L804 calls the leading constant of `I_γ(z)` "the Stokes multiplier = C", but §5.3
  (Method C, L842–845) defines `S_mult` with `|S_mult| = 2πK = S`. Since `S ≠ C` (they differ by
  the exact factor `|Γ(β)|/2π = 0.95588`), the term "Stokes multiplier" is used for two different
  constants. A careful referee will catch the apparent contradiction.
- **Fix:** at L804 call it "the connection coefficient C" (not "Stokes multiplier"), OR add the
  clause "up to the `z^β` branch normalisation that converts the Stokes multiplier `S` into
  `C = (|Γ(β)|/2π)S`". Either removes the collision. Math underneath is unchanged.

## M-2 [MED] — (folded into M-1) terminology pass: reserve "Stokes constant/multiplier" for S

- **Where:** global. Ensure "Stokes constant"/"Stokes multiplier" always denotes `S = 2πK`
  (magnitude), and "connection coefficient" always denotes `C = |Γ(β)|K`. L804 is the only current
  collision; a quick global read confirms the rest are consistent (L222, L327, L654, L839–852,
  L864, L1171 all use S = 2πK correctly). Do this together with M-1.

## M-3 [MED] — Add topological-recursion / Marchal SOTA citations (Lecerf-3 gap)

- **Where:** §7 Discussion (new short paragraph in §7.3 or a new §7.x), and an acknowledgement in
  §2.2 Rmk:provenance (L289–300) where the paper states "the literature provides no explicit
  classical Lax pair for V_quad".
- **Issue:** the paper frames significance vs the Ramanujan Machine / CMF circle but omits the most
  directly competing SOTA for Painlevé/Stokes constants: Eynard–Orantin **topological recursion**
  and the Iwaki–Marchal computations of Painlevé τ / Stokes data. This is the one Lecerf-3
  ("significance vs state-of-the-art") soft spot.
- **Fix:** add citations (DOIs from the operator's Marchal confirmation, queued for corrections):
  - Marchal–Alameddine 2024, *Comm. Math. Phys.* — DOI `10.1007/s00220-024-05187-0`
  - Iwaki–Marchal–Saenz 2018, *J. Geom. Phys.* — DOI `10.1016/j.geomphys.2017.10.009`
  - Marchal–Orantin 2020, *J. Math. Phys.* — DOI `10.1063/5.0002260`
  plus one sentence: topological recursion computes Painlevé τ-functions and their Stokes data from
  a spectral curve; the present holonomic/Borel route is complementary (it produces the *minimal
  operator with an exact ℚ(√3) certificate* and the *period* of the Stokes datum, not the τ-series).
- **Note:** verify the three DOIs against the operator's confirmation record before insertion (do
  not trust memory for DOIs — Trap 6).

## M-4 [MED] — Sakai concept-DOI placeholder (operator hand-fill at submission)

- **Where:** bibitem{Sakai}, L1254: "[Concept DOI to be inserted by the operator at submission time.]".
- **Issue:** placeholder, by design (MED-1 of the checklist). Must be filled with the **current**
  Sakai-stratification concept DOI before any deposit/submission.
- **Fix:** operator inserts the live concept DOI from the authoritative
  `sectorial/.../sakai-stratification/related_identifiers.md` (not from memory). This is the only
  hard operator gate in the bibliography.

---

## L-1 [LOW] — Optional sibling-deposit cross-references (program coherence)

- **Where:** §7.1 (Place in the Sakai stratification) and/or bibliography.
- **Issue:** the Zenodo deposit metadata (ZENODO-PREP-001 related_identifiers) references sibling
  results — EBR-Ib, EBR-II, δ-Fredholm — but the paper bibliography does not. Citing them would
  strengthen "place in the program" and align paper-bib with deposit-metadata.
- **Fix (optional):** add bibitems and a sentence in §7.1 if desired. **Verify DOIs from the
  authoritative `related_identifiers.md`, not memory** (corpus shows EBR-II version vs concept DOIs
  drift — e.g. concept vs 20566465/20571232). Low risk if deferred; the paper is self-contained
  without them.

## L-2 [LOW] — Tighten eq:periodmatrix "read off as" phrasing (§6.2)

- **Where:** L981–984, "`C = |Γ(β)|K` is read off as the Stokes-entry × amplitude combination
  `|A|/|β|`".
- **Issue:** "read off as" is informal; C is not literally a single entry of the 2×2 `P(M)`.
- **Fix:** state precisely that C is the pairing `|A|/|β|` built from the matrix data, or add the
  one-line identity. Acceptable as-is given this is the explicitly conjectural motivic layer
  (G-MOTGALOIS); polish only.

## L-3 [LOW] — One-clause abstract pre-empt of the order-4/order-2 double-take

- **Where:** abstract (L50–64).
- **Issue:** "holonomic of order 4" (B̂/L_V) and "order-2 operator" (L_φ) are correct but can read
  as a contradiction on first pass.
- **Fix (optional):** "…holonomic of order 4 (the Borel–Laplace dual of the order-2 operator
  annihilating the series)…". Non-blocking; the body (Table 2.6) already disambiguates.

## L-4 [LOW] — Update `\thanks` at submission

- **Where:** L46, `\thanks{… This is a working draft; not yet submitted.}`.
- **Fix:** operator updates/removes at submission time. Trivial.

## L-5 [LOW] — Precise cite for the "(1/2)^n numerical floor in the parent probe"

- **Where:** L442–443 (proof of Cor:finite).
- **Issue:** the phrase references a parent-probe observation without a script/slot cite at that
  exact spot (§2 is generally sourced to PERIOD-REP-VQUAD-002).
- **Fix (optional):** add the specific slot/script reference for the `(1/2)^n` floor claim. Polish.

---

## Reconciliation with the prior corrections agenda

- **6 pre-committed checklist items** → all resolved above (MED-1=M-4; MED-2 honored; MED-3 adequate
  + L-2; LOW-1=L-4; LOW-2 sufficient; LOW-3 present).
- **Marchal-derived items** → M-3 (topological-recursion citations + §2.2/§7 sentences). The
  "§2 Lax-pair acknowledgement" is folded into M-3 (the Rmk:provenance touch-point).
- **3 F-ANTICIPATORY (EBR-Ib / EBR-II / δ-Fredholm bibliography)** → L-1 (optional; DOIs from
  authoritative file only).
- **New this read:** **H-1** (retracted-value provenance) and **M-1/M-2** (Stokes-multiplier-vs-C
  terminology) — neither was on the prior agenda; both are real.

**Net:** 1 HIGH, 4 MED, 5 LOW. No item requires re-doing mathematics. This list is the scope of
VQUAD-PAPER-CORRECTIONS-001.
