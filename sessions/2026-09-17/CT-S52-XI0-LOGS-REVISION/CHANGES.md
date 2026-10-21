# CT-S52 — CHANGES

Changes list for the revision of *An exponential-period representation of the
V_quad constant*, keyed to the four items of the editor's email plus the
reference item.

**Nothing here has been uploaded, submitted, deposited or committed.**

- Submitted source (untouched): `sessions/2026-06-16/VQUAD-PAPER-LAYOUTFIX-001/latex/vquad-periodrep-paper.tex`
  — sha256 `d8906249e8d0eaff681da0f21d6996e6ac824f60550be1d12a21857ae2f6a906`
- Submitted PDF (untouched): same folder — md5 `99faea5b0f4095788e4ee932436beeda`, 773171 B, 24 pp.
  (Zenodo record 20719043.)
- Revised copy: `sessions/2026-09-17/CT-S52-XI0-LOGS-REVISION/revision/vquad-periodrep-paper.tex`
  — sha256 `d15f9cf506490934327475dcdf5e18edfdc45fb868e78037127f9d777385db89`
- Revised PDF: same folder — sha256 `b854e7cafef9e802…`, 26 pp.

The revision is exactly 19 replacements, each of which had to match the
submitted source **exactly once** or the patch script refuses. The revised copy
was then re-derived from the pristine source independently of that run and found
byte-identical, so it contains the tabled edits and nothing else
(`outputs/diff_render.out.txt`, claim S52-14).

---

## Item 1 — the D₅⁽¹⁾ identification is conjectural

Four edits — three at the places the email named, and **one more found by the
sweep**.

| # | Place | Change |
|---|---|---|
| 1 | Abstract | "the rank-one standalone closure **on the Sakai surface** D₅⁽¹⁾" → "…**whose Sakai surface type is conjectured to be** D₅⁽¹⁾". |
| 2 | §1.1 | "where it **is identified as** a non-classical Painlevé V transcendent" → "where it is **conjectured to be**…", plus: "That identification is Conjecture 4.1 of [1], not a theorem, and nothing in the present paper depends on it: every result below is a statement about the operators L_φ and L_V and the cycle γ." The quoted Painlevé parameters θ_∞ = 2/√3 and α = 1/6 are now attributed to the companion, with the note that **its version 1.3 correction notice [26] revises the derivation by which those parameters were obtained**. |
| 3 | §7.1 | "For V_quad, the rank-one D₅⁽¹⁾ representative" → "For V_quad, **conjecturally** the rank-one D₅⁽¹⁾ representative ([1], Conjecture 4.1)". |
| 4 | §4, *Algebraicity for Fresán–Jossen* (L527) | **Not on the email's list.** "The transcendental Painlevé-V accessory parameter of V_quad **lives in** the nonlinear moduli" presupposes the identification as fact. Now: "**Under the conjectured identification of [1], Conjecture 4.1**, the transcendental Painlevé-V accessory parameter of V_quad **would live in** the nonlinear moduli". |

§1.2 needed no separate edit: its D₅⁽¹⁾ mention is inside the sentence rewritten
at §1.1. Note that the hedge now in the paper matches the hedge already present
in the arXiv metadata package, which has said "whose Sakai surface type is
conjectured to be" since 2026-09-13.

**Amendment H note.** The email's list was given as "expected: abstract, 1.1,
1.2, 7.1". Sweeping for the same defect elsewhere — rather than editing only
the reported places — turned up edit 4, in a section the list did not name and
which no build, citation or reference check would ever have flagged. The sweep
also cleared the remaining `D_5` and `Painlev`-near-`transcendent` hits as
correct (see K3 below), and that clearance is part of this output whether or
not it found anything.

## Item 2 — §7.1 no longer claims to complete part (ii)(a)

One edit (edit 5). "so the present paper *completes part (ii)(a) for d = 2*" is replaced by:

> What this establishes is an **instance** of part (ii)(a) for the single
> representative V_quad: its connection constant is realised as an explicit
> Fresán–Jossen exponential period, and is transcendental under the two
> hypotheses of Corollary 1.4. The instance is attached to the D₅⁽¹⁾ stratum
> only through the conjectured surface identification of [1], Conjecture 4.1.
> Part (ii)(a) is **not** established for the stratum: no statement is made here
> about any other member, and nothing here proves that V_quad lies in that
> stratum.

## Item 3 — "proved twice" removed; the structural argument restated

Five edits.

| # | Place | Change |
|---|---|---|
| 6 | Thm 1.2 discussion | "This is proved twice: by … and by a structural torus-plus-unipotent argument" → "The proof is …". The structural argument is now described as "a consistency check on the same computation, **not a second proof**". |
| 7 | §1.4 | "by an **independent** structural argument" → "with the structural argument of Appendix A.2 as a consistency check on it, not as a second proof". |
| 8 | Proof after Thm 2.2 | The structural route is retitled "*(2) Structural argument (a consistency check on (1), not a second proof)*", and the argument is stated correctly: a maximal torus together with **one root unipotent generates a Borel subgroup**, and the passage to SL₂(ℂ) uses the exclusion of the reducible case — **which is Kovacic's Case 1**. The paragraph now says explicitly: "The two routes are therefore *not* independent: route (2) is conditional on the Case 1 exclusion." |
| 9 | Appendix A.2 | "Independent structural confirmation" → "Structural consistency check (not independent of the above)". |
| 10 | Appendix A.5 | "case-elimination **and by an independent** structural argument" → "case-elimination, with the structural argument of Appendix A.2 as a consistency check that depends on the same exclusion". |

Kovacic's algorithm is now the sole proof of Theorem 1.2, as it always was.

## Item 4 — apparency at ξ = 0 corrected

**Part A found logarithms.** ξ = 0 is a genuine regular singular point of L_V
with unipotent local monodromy, not an apparent singularity. Eight edits follow
the operator's contingency branch: correct every "apparent", and state that the
main identity is unaffected because B̂ is the holomorphic exponent-0 solution and
the cycle γ does not approach 0.

| # | Place | Change |
|---|---|---|
| 11 | Prop 2.4 | Now states the exponents {−1, 0, 1, 2}, the nonzero obstruction (38286 + 24984√3)/418501 at the first resonant step from −1, the log-free dimension 3, and that the fourth local solution carries log ξ — "hence ξ = 0 is a genuine regular singular point of L_V with unipotent local monodromy, **not an apparent one**". |
| 12 | Table 1 | Row for ξ = 0: "0 (apparent)" → regular singular, one logarithmic solution, no cut. |
| 13 | Proof of Cor 1.4 | "the point 0 is apparent" → the point 0 is regular singular but B̂ is holomorphic there. |
| 14 | Lemma 2.7 | Retitled **"The point ξ = 0 carries no period"**. Statement and proof rewritten: ξ = 0 is *not* apparent; B̂ is the holomorphic exponent-0 solution; the main identity does not use apparency. Carries an explicit note that the earlier claim of apparency "is false — consecutive integer exponents make the point resonant, not apparent". |
| 15 | Figure | Node label "(apparent)" replaced (reg. sing., no cut). |
| 16 | Figure caption | "ξ = 0 is apparent and carries no cut" corrected. |
| 17 | Remark 3.3 | "the apparent point" corrected. |
| 18 | Appendix A.3 (new) | New paragraph recording the exact ξ = 0 computation: exact Q(√3) arithmetic, the three routes that share no code (resonant-step obstruction; rank of the truncated Laurent system; explicit construction of the logarithmic solution), the exhibited log solution v₀ = −(2 + √3)/24, and the two controls. |

This correction is the same defect the companion's v1.3 correction notice
records as item C1, reached here independently and by a different route.

## Item R — reference for the companion's v1.3

One edit (edit 19). `[2]` (`StokesNote`) **stays pinned to v1.2**, DOI
`10.5281/zenodo.20481592`. A new `\bibitem{VquadV13}` is added, citing version
DOI `10.5281/zenodo.22831933` (concept `10.5281/zenodo.20455089`) and its
correction notice, whose items C1 and C2 respectively withdraw an apparency
claim and revise the derivation of the quoted Painlevé parameters.

**The new entry is placed last in the bibliography, not next to [2].** Placing it
in date order after [2] renumbered 19 subsequent citations, which would make a
referee's notes on the submitted version stale for no mathematical gain. As
placed, every existing citation number is unchanged and the new reference is
[26]. This was found by the rendered diff, which showed `[3]→[4]`, `[7]→[8]`,
`[18]→[19]`, `[20]→[21]` and so on; after the move, no bracket renumbering
remains.

---

## Checks

| Check | Result |
|---|---|
| **K1** build | 3 pdflatex passes, **0 undefined references, 0 undefined citations**, 0 rerun warnings, 26 pp. |
| **K2** rendered diff vs the **submitted PDF** (identified by md5, not filename) | 24 → 26 pp; net token balance 110 removed / 948 added, all traceable to the 19 replacements. |
| **K2b** exact source reconstruction | revised copy byte-identical to pristine + 19 tabled replacements. Shown to **fail** on a planted one-word edit (`Kovacic`→`KOVACIC`, exit 2), then to pass again on restore. |
| **K3** sweep re-run | 58 hits, all accounted for below. |
| **K4** submitted artefacts | tex sha256 and pdf md5 both unchanged. |

### K3 — sweep accounting, before → after

| Term | Before | After | Account |
|---|---|---|---|
| `D_5` | 6 | 6 | L60 (abstract, hedged), L89 (§1.1, hedged), L1128/L1129/L1136 (§7.1, the new hedged text). L128 left: it names the **stratum** in the master conjecture — "For the D₅⁽¹⁾ (Painlevé V) stratum the master conjecture predicts…" — and makes no claim about V_quad's membership, so it is correct as written. |
| `Sakai` | 14 | 14 | All are citations of Sakai's classification or the surface name inside sentences now hedged. No unhedged assertion of V_quad's membership remains. |
| `Painlev` near `transcendent` | 6 | 7 | +1 from the new bibliography entry (L1519, the companion's title; L1368 and L1374 are the two pre-existing entries for the same companion). L89 is hedged; L126 and L1174 describe the CMF program and the stratum in general, not V_quad; L527 was **hedged by edit 4**. |
| `completes` | 2 | 1 | L358 rewritten (item 2). The survivor, L368, is "a **complete** rational solution" in the Kovacic/Riccati discussion — an unrelated sense of the word. |
| `twice` | 2 | 1 | L166 rewritten (item 3). The survivor, L450, is "Both statements are obtained twice, by a falling-factorial indicial computation and by direct …" — this is about the **exponents at −ξ₀**, two computations of the same exponent, not a claim that the Galois theorem is proved twice. Left deliberately. |
| `independent` | 14 | 14 | Count is unchanged because item 3 both removed independence claims and added explicit **denials** of independence. The survivors split into two groups: (a) the three **verification methods** A/B/C, whose mutual independence is a separate and unretracted claim (L68, L161, L794, L802, L912, L968); (b) the new denials (L388 "The two routes are therefore *not* independent", L1279 "Structural consistency check (not independent of the above)"). Neither group asserts that the structural argument is an independent proof of Theorem 1.2. |
| `structural argument` | 3 | 3 | All three now read "consistency check … not a second proof" / "consistency check that depends on the same exclusion". |
| `apparent` | 9 | 12 | Rose because the corrected text **discusses** apparency in order to deny it. Every hit is a denial (L443, L502, L517–519, L1309), a cross-reference to the label `lem:apparent` (L444, L671, L1311), the label's own declaration (L499), a TikZ source comment (L581), or the new bibliography entry describing the companion's withdrawn claim (L1523). **No hit asserts apparency.** |

One residue, reported rather than repaired: the LaTeX label `lem:apparent` now
names a lemma titled "The point ξ = 0 carries no period". The label is only a
source-level identifier and renaming it would churn six cross-references for no
reader-visible gain, but a reader of the *source* could be misled. Flagged for
the operator.

---

## Not an edit to the source: the cover letter

The cover letter is **not in this repository** — no V_quad cover letter exists
anywhere in the tree, so its exact sentence cannot be quoted here and none has
been invented. The correction it needs is described by substance in
`CORRECTIONS-FOR-REFEREES.md` and must be checked against the letter actually
sent before it goes to the editor.
