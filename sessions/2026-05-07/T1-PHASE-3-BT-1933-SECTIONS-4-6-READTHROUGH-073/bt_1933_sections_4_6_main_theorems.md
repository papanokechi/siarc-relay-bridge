# BT 1933 §§4-6 — Main Theorems / Lemmas / Propositions Index

**Source PDF SHA-256:**
`dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6`
**Page span:** Acta p. 29 (PDF p. 29) — p. 51 (PDF p. 51).
**Sections:** §4 "A lemma on summation" + §5 "Construction of proper
solutions to the right of a proper curve" + §6 "A lemma on
factorization."

## Labelling note (Phase E.1)

A grep over the §§4-6 verbatim transcripts for header tokens
{`THEOREM`, `Theorem`, `Proposition`, `Lemma`, `Corollary`, `Satz`}
returned exactly **3 explicitly labelled results** in §§4-6:

| Position | Label | Section |
| --- | --- | --- |
| Acta p. 30 | "Lemma 8" | §4 |
| Acta p. 41 | "Theorem I" | §5 |
| Acta p. 48 | "Lemma 9" | §6 |

No `Proposition`, `Corollary`, or `Satz` labels appear in §§4-6. The
single corollary-flavoured result inside Theorem I (the m = 1 special
case "If Γ ... exists in the region (1) ... it will necessarily follow
that L_n(y) is completely proper in (m) + ... + (η)   (m = 1)") is
embedded inside the Theorem I statement and is not separately
labelled; it carries identifier T2.cor below.

## Indexed-result table (Phase E.2)

Each result carries a verbatim ≤ 30-word statement (or paraphrase if
verbatim > 30 words) with page anchor + scope tag + SUBJECT tag from
the relay 073 set:
{classification, formal solution, chart map, sectorial upgrade,
Stokes data, asymptotic bound, auxiliary}.

| ID | Label | § | Acta p. | Verbatim ≤ 30-word OR paraphrase | Subject tag | Word count |
| --- | --- | --- | --- | --- | --- | --- |
| **T1** | Lemma 8 | §4 | p. 30 | *BT 1933 §4 p. 30 states (in our paraphrase):* the equation y(x+1) − y(x) = e^{Q(x)} h(x) (under analyticity + Q-properness + h ∼ formal s-series + ℜ Q' ≦ 0 hypotheses) admits an analytic solution y(x) on a sub-region R' interior to R, with asymptotic relation y(x) ∼ e^{Q(x)} s(x). | **sectorial upgrade** + **formal solution** | (paraphrase) |
| **T2** | Theorem I | §5 | p. 41 | *BT 1933 §5 p. 41 states (in our paraphrase):* given L_n(y) = o with known coefficients and proper-curve Γ for the set Q_1, ..., Q_n, plus a strip-V proper-fundamental-set hypothesis (or m = 1 corollary form), L_n is completely proper in (m) + ... + (η). | **sectorial upgrade** + **formal solution** + **Stokes data** | (paraphrase) |
| T2.cor | (m = 1 case) | §5 | p. 41 | "If Γ, a proper curve for the set (1), exists in the region (1) then the above assumption concerning existence of solutions in V may be omitted ..." | **sectorial upgrade** | 28 |
| **T3** | Lemma 9 | §6 | p. 48 | *BT 1933 §6 p. 48 states (in our paraphrase):* if L_n is Q-factorable in (1) + ... + (m) at a point of division between Γ-th and (Γ+1)-st terms (not in the same logarithmic group), then L_n = L_{n−Γ} L_Γ, with the factor operator carrying the first Γ formal solutions. | **classification** + **formal solution** | (paraphrase) |

(SUBJECT tag {chart map} appears as `[CHART-MAP-CANDIDATE-B1]` at
`[CLAIM-B517]` of `bt_1933_section_5_claim_table.md` — embedded inside
the Theorem I (T2) proof but not the Theorem I statement itself; per
relay 073 Phase C.4 caveat, this is a substrate-inventory observation.)

## Direct verbatim opening clauses (≤ 30 words; for citation use)

For applications that need a short verbatim citation rather than the
paraphrase, the following opening clauses are within ≤ 30 words and
may be cited directly:

| ID | Label | Acta p. | Verbatim ≤ 30-word opening clause | Word count |
| --- | --- | --- | --- | --- |
| T1 | Lemma 8 | p. 30 | "The equation (2) y(x + 1) − y(x) = e^{Q(x)} h(x) possesses a solution y(x), analytic in a region R' interior to R by a distance ε(> o)." | 30 |
| T2 | Theorem I (hypothesis line) | p. 41 | "Suppose that Γ, a proper curve (Def. 9; § 1) for the set (1), is the left boundary of (m) (2 ≦ m ≦ η) or lies to the left of it." | 30 |
| T2 | Theorem I (conclusion line) | p. 41 | "It will necessarily follow that L_n(y) is completely proper (Def. 6; § 1) in (m) + ... + (η)." | 17 |
| T3 | Lemma 9 (conclusion line) | p. 48 | "(1 a) L_n(y) ≡ L_{n−Γ} L_Γ(y) = o, so that the coefficients in the operators L_{n−Γ}(z), L_Γ(y) are of the same kind as in (1)." | 25 |

## Subject-tag distribution

| Subject tag | Count | IDs |
| --- | --- | --- |
| classification | 1 | T3 |
| formal solution | 3 | T1, T2, T3 (Lemma 9 carries the formal-series-compatibility statement (1 b)) |
| chart map | 0 main-theorem statements (1 inside-proof candidate at `[CLAIM-B517]`) | — (CHART-MAP-CANDIDATE-B1 inside T2 proof) |
| sectorial upgrade | 2 + 1 corollary | T1, T2, T2.cor |
| Stokes data | 1 | T2 (the across-strip periodic-functions structure (12 a)+(13 a) inside the Theorem I proof; embedded substrate, surfaced at `[CLAIM-B517]`) |
| asymptotic bound | 1 (T1 itself, considered as an asymptotic-validity statement) | T1 |
| auxiliary | 0 | — |

## Result count

- Explicitly labelled main results in §§4-6: **3** (Lemma 8, Theorem I, Lemma 9).
- Sub-result (corollary flavour, embedded): **1** (T2.cor; m = 1 case of Theorem I).
- Total indexed identifiers: **3 + 1 = 4** (T1, T2, T2.cor, T3).

## Relation to D2-NOTE v2.1 §4.5 citations

D2-NOTE v2.1 §4.5 (cf. v2.1 PDF p. 6, line block "Birkhoff–Trjitzinsky
1933 §§4–6: Borel-summability") cites exactly the three explicitly
labelled results:

| v2.1 citation | This index ID | Acta p. (v2.1's claim) | Acta p. (verified) |
| --- | --- | --- | --- |
| "§4 Lemma 8 ([2,§4, Lemma 8, p. 30])" | T1 | p. 30 | p. 30 (verified) |
| "§5 Theorem I ([2,§5, Thm. I, p. 41])" | T2 | p. 41 | p. 41 (verified) |
| "§6 Lemma 9 ([2,§6, Lemma 9, p. 48])" | T3 | p. 48 | p. 48 (verified) |

Page-anchor agreement is exact for all three citations. The
side-by-side substrate-inventory layout is in
`d2_note_v21_bt_citation_audit.md`.
