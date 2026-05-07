# Paper Profile [PROFILE-P4] — D2-NOTE v2.1

**Session:** T2-PORTFOLIO-BUNDLING-DOSSIER-ASSEMBLY-077
**Compiled:** 2026-05-07
**Source SHA-256 (16):** `840120E73534DA8E` (TeX) / `A8B6026A3453F901` (PDF)
**Path:** `siarc-relay-bridge/sessions/2026-05-03/D2-NOTE-V2-1-WASOW-FULL-CLOSURE/d2_note_v2_1.tex` (38311 B, 908 lines)

---

## B.1 Record metadata

- **Title:** "Cross-degree universality of the Borel-singularity radius for polynomial continued fractions" (verbatim L42-43; 11 words)
- **Concept DOI:** `10.5281/zenodo.19996689`
- **Version DOI (v2.1):** `10.5281/zenodo.20015923`
- **Page count (PDF):** 9 pp typeset (pdf-regex `/Type/Page` count = 9)
- **Primary arXiv category:** `math.CA` (per spec §0 anchor "D2-NOTE v2.1 → Asymptotic Analysis"; CT-adjacent math-ph cross-list candidate)
- **Cross-list categories (candidate per content):** `math-ph` (Borel summability + irregular-singularity rank; Wasow / Birkhoff–Trjitzinsky tradition)
- **Submission status:** PUBLISHED on Zenodo (per CC-VQUAD-PIII spec L46-48 "M2 ✅ FULLY DONE (D2-NOTE v2.1 UPGRADE_FULL on Zenodo 2026-05-04 ~07:00 JST)")
- **AEAL claim count (paper-internal):** Cross-degree Newton polygon Lemma (`lem:newton-poly-chi-d`) + Cross-degree universality of ξ_0 Theorem (L721) + 18/18 Phase A* sweep at d ∈ {2..10} dps 50; Borel-summability citation chain (BT 1933 §§4-6 + Wasow 1965 §19 + Birkhoff 1930 §2)

## B.2 Mathematical-result spine

**80-word summary [verbatim from abstract L108-145, 50 words]:**
> "We isolate, as a single citable artefact, the cross-degree identity ξ_0(b) = d/β_d^{1/d} for the leading Borel-plane singular distance of the formal generating function f(z) = Σ Q_n z^n of a polynomial continued fraction (1, b) of degree d with leading coefficient β_d > 0."

**Key theorem labels (≤ 5 most-cited, verbatim labels only):**

- `lem:newton-poly-chi-d` — "Cross-degree Newton polygon characteristic polynomial" (L461)
- Theorem at L721 — "Cross-degree universality of ξ_0" (the headline theorem)
- §3 "The proven case d = 2" (L251)
- §4 "The verified case d = 4" (L404; PCF2-SESSION-Q1 anchor)
- §5 "The cross-degree theorem at d ≥ 2" (L446)

**Open conjectures or empirical claims (with AEAL-status):**

- ξ_0 = d/β_d^{1/d} at d=2: TIER-1-CONFIRMED (proven via Newton polygon Lemma 3.1 + uniform-in-q Wasow §19 + uniform-in-n Birkhoff–Trjitzinsky 1933 §§4-6; closed citation chain)
- ξ_0 = d/β_d^{1/d} at d=4: TIER-2-EMPIRICAL (PCF2-SESSION-Q1 spread 0 verification)
- ξ_0 = d/β_d^{1/d} for general d ≥ 2: TIER-2-EMPIRICAL (Phase A* 18/18 at d ∈ {2..10}, dps 50; theorem statement at L721 with Borel-summability layer citation closed v2.1)
- d=3 ξ_0 verification: TIER-3-OPEN (`op:xi0-d3-direct` per §6 "What remains open" L788)
- β_d < 0 branch: TIER-3-OPEN (out of scope; recorded in §6)
- d=2 anomaly Galois bin (L223): TIER-3-OPEN (cite `siarc_pcf1_v13` Remark 5.E)

## B.3 Substrate dependency graph

**Cites (within the 6-record portfolio):**

- PCF-1 v1.3 — `siarc_pcf1_v13` (Remark 5.E "d=2 anomaly Galois bin" out-of-scope marker; footnoted as "SIARC Zenodo deposit; internal review only, not peer-reviewed")
- CT v1.3 — `siarc_xi0_d3_direct` open-problem reference + the v1.2 candidate-falsification note absorbed into D2 §2.5 v2.1 (per file header v2 supersession notes L18-21)
- SIARC umbrella v2.0 — invariant-triple ξ_0 axis owner (per umbrella abstract L62)

**Cited by (within the 6-record portfolio):**

- CC-VQUAD-PIII spec / 058R+ amendment chain cites D2-NOTE v2.1 verbatim (per `_for_synthesizer_segment_1.txt` L192 "D2-NOTE v2.1 (Zenodo 10.5281/zenodo.20015923; PDF SHA…)")
- PCF-1 v1.3 v_quad row reframing 066 reframes A=4 row entry per D2-NOTE four-row enumeration (065 supplement)
- 067 BT-baseline-note follow-up extends D2-NOTE substrate
- All four other PCF-portfolio records may cite Borel-radius axis (umbrella v2.0 explicit; PCF-2/CT/T2B implicit at d=2 specialisation)

## B.4 Endorsement-fit summary

**[NOTE-077-P4-1] D2-NOTE v2.1 not in 5-record 2026-05-04 portfolio_inventory.md** because that inventory predates D2-NOTE v2.1's Zenodo
upload (D2-NOTE v2.1 published 2026-05-04 ~07:00 JST per CC-VQUAD spec L47;
inventory file timestamp 2026-05-04 ~18:00 JST per inventory L4 — but
inventory enumerates only the 5 records that had endorsement templates
on disk at 037 ARXIV-ENDORSEMENT-TEMPLATES-EXPAND, which preceded D2's
v2.1 deposit). Endorsement-fit derivation is therefore by content-class
inheritance from the 5-record table:

- math.CA primary → Mazzocco H (math.CA primary; per inventory row 4 mazzocco_m_1 anchor); Zudilin M-to-H (math.CA cross-list activity per inventory; Wasow / Birkhoff lineage); Garoufalidis M-to-H (math.CA via resurgence cross-list per inventory row 4)
- D2-NOTE bibliography directly cites the same Wasow + Birkhoff–Trjitzinsky chain that grounds CT v1.3, so endorsement-fit is structurally identical to CT v1.3's row 4 fit profile
- No new endorsement template on disk for D2-NOTE v2.1 — would require new template drafting under D.4 ENDORSEMENT-ROUTE dimension

[NOTE-077-P4-2] Per HALT_077_NEW_CITATION_INTRODUCED: this profile cites
no biblio entry not already in the 6 records' reference lists. Wasow,
Birkhoff, Birkhoff–Trjitzinsky are all present in D2-NOTE v2.1's own
bibliography per file header L29-32.

---

End of P4 profile.
