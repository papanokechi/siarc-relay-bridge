# BT 1933 §6 "A Lemma on Factorization" — Verbatim Extract

**Source PDF SHA-256:**
`dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6`
**Section span:** Acta p. 48 (PDF p. 48) — Acta p. 51 (PDF p. 51).
**Section title (verbatim, TOC):** "A lemma on factorization."
(Body-text title at Acta p. 48: "A Lemma on Faetorization." — single-
letter font-glyph drift "c" → "e"; documented in
`discrepancy_log.json` D1.)

**This is the D2-NOTE v2.1 CITATION REGION.** D2-NOTE v2.1 §4.5 cites
"§6 Lemma 9 ([2,§6, Lemma 9, p. 48])" verbatim; §6 is the source of
v2.1's BT factorisation citation.

Page anchors `[p. NN]` mark each Acta-page break. Math symbols are
reproduced as rendered by pypdf 6.10.2; isolated font-glyph drift is
flagged where it affects interpretation. The pypdf substitution
`w → §` is silently restored throughout.

---

## [p. 48] — section opener + Lemma 9 setup

§ 6.   A Lemma on Factorization.

The following lemma will be indispensible as a preliminary to
establishing the fundamental result.

Lemma 9. Let coefficients of

(1)   L_n(y) = y(x + n) + a_1(x) y(x + n − 1) + ... + a_n(x) y(x) = o

be known (and be of the kind specified in the beginning of § 1) in
(1) + ... + (η), a subregion of F. If the equation is Q-factorable in
(1) + ... + (m) (Def. 8; § 1), a point of division being between the
Γ-th and Γ + 1-st terms (not belonging to the same logarithmic group of
the sequence

  Q_1(x), ..., Q_n(x)        (1 ≦ Γ < n),

it necessarily follows that the equation is factorable,

(1 a)   L_n(y) ≡ L_{n−Γ} L_Γ(y) = o,

so that the coefficients in the operators L_{n−Γ}(z), L_Γ(y) are of the
same kind as in (1). With the e^{Q_j(x)} s_j(x) (j = 1, ..., n)
denoting a linearly independent set of formal solutions of (1), the
factorization (1 a) can be so effected that the series

(1 b)   e^{Q_1(x)} s_1(x), ..., e^{Q_Γ(x)} s_Γ(x)

are formal solutions of L_Γ(y) = o.

Proof. In connection with the system Y(x + 1) = D(x) Y(x) (6; § 1),
associated with (1), functions y_{r i}(x) are defined by the product

(2)   Y_r(x) = D(x − 1) D(x − 2) ... D(x − r) T(x − r)

where T(x) denotes S(x) ≡ (e^{Q_j(x)} s_o(x)) =
(e^{Q_j(x + i − 1)} s_j(x + i − 1)) with the s-series factors in the
involved elements terminated after, say, k terms (k being sufficiently
great). In accordance with the notation of § 3 we write

(footnote) "Cf. (I; p. 213, l. 6)."

## [p. 49] — Lemma 9 proof (determinant limits + asymptotic forms)

(2 a)   Y_r^Γ(x) =
        | y_{i_1 1}(x), ..., y_{i_1 Γ}(x) |
        | ............................... |
        | y_{i_Γ 1}(x), ..., y_{i_Γ Γ}(x) |
        where i_1 < i_2 < ... < i_Γ and i_1, i_2, ..., i_Γ = 1, ..., n.

Since, by hypothesis,

  ℜ[Q'_{j_1}(x) + ... + Q'_{j_Γ}(x)] ≧ ℜ[Q'_1(x) + ... + Q'_Γ(x)]
              (j_1 < ... < j_Γ = 1, ..., n; x in (1) + ... + (m)),

in virtue of Lemma 5 (§ 3) the limits

(2 b)   lim_{r→∞} y_{i_1 ... i_Γ; 1...Γ}^r(x) = y_{i_1 ... i_Γ; 1...Γ}(x)
                  (i_1 < ... < i_Γ = 1, ..., n)

will exist in (1) + ... + (m) and will be analytic in this region;
moreover, the asymptotic relations

(2 c)   y_{i_1 ... i_Γ; 1...Γ}(x) ∼ e^{Q_1(x) + ... + Q_Γ(x)}
                                    s_{i_1 ... i_Γ; 1...Γ}(x)
        (i_1 < ... < i_Γ = 1, ..., n)

will hold in (1) + ... + (m). Form the operator

(3)   L^r_Γ(y) ≡ (− 1)^Γ y(x + Γ + 1) ÷ y_{r;1}(x) ... y_{r;Γ}(x)
              · y_{Γ+1, 1}(x) ... y_{Γ+1, Γ}(x)
       = b'_o(x) y(x + Γ) + ... + b'_{Γ−s}(x) y(x + s) + ... + b'_Γ(x) y(x);

here

(3 a)   b'_{Γ−s}(x) = (− 1)^{Γ−s} y_{1...s, s+2, ..., Γ+1; 1...Γ}(x)
                                   / y_{1...Γ; 1...Γ}(x).

From the way asymptotic relations (2 c) were derived in § 3 it follows
that

(3 b)   y_{1...s, s+2 ... Γ+1; 1...Γ}(x) ∼ e^{Q_1(x) + ... + Q_Γ(x)}
                                            s_{1...s, s+2 ... Γ+1; 1...Γ}(x)
        (s = 0, ..., Γ; x in (1) + ... + (m); r = 1, 2, ...).

Hence an equation L'^r_Γ(y) = o will possess in (1) + ... + (m), formal
solutions

(printer-line) "7—32511. Acta mathematica. 60. Imprimé le 2 septembre 1932."

## [p. 50] — Lemma 9 proof (factor operator construction)

  e^{Q_1(x)} s_1(x), e^{Q_2(x)} s_2(x), ..., e^{Q_Γ(x)} s_Γ(x).

In virtue of (2 c) and of the fact just stated, if L'_Γ(y) denotes
lim_{r→∞} L^r_Γ(y), the equation

(4)   L'_Γ(y) ≡ b'_o(x) y(x + Γ) + ... + b'_Γ(x) y(x) = o

will possess the same formal solutions. In particular,

(4 a)   b'_{Γ−s}(x) ∼ e^{Q_1(x) + ... + Q_Γ(x)}
                       s_{1...s, s+2 ... Γ+1; 1...Γ}(x)
        (s = 0, 1, ..., Γ; x in (1) + ... + (m)).

Here the s-series in the second member of (4 a) cannot be identically
zero for s = 0 and s = Γ; this is a consequence of linear independence
of the formal series. Hence

  b'_o(x) ≠ o, b'_Γ(x) ≠ o.

Thus the equation (4) is actually of order Γ. Dividing out the
coefficient b'_o(x) we write (4) in the form

(5)   L_Γ(y) ≡ y(x + Γ) + ... + b_{Γ−s}(x) y(x + s) + ... + b_Γ(x) y(x)
            = o
       (b_{Γ−s}(x) = b'_{Γ−s}(x) / b'_o(x); s = 0, ..., Γ − 1).

The coefficients in (5) are analytic in (1) + ... + (m); moreover,

(5 a)   b_{Γ−s}(x) = (− 1)^{Γ−s} s_{1...s, s+2 ... Γ+1; 1...Γ}(x)
                                   / s_{1...Γ; 1...Γ}(x)
                  = β_{Γ−s}(x)
        (s = 0, ..., Γ − 1; x in (1) + ... + (m)).

Now, the formal series s_{1...s, s+2 ... Γ+1; 1...Γ}(x) (s = 0, 1, ...
Γ) will contain no logarithms since the columns in the formal
determinants can be so combined as to get rid of these logarithms (Cf.
(I); in particular, pp. 213, 215). It is clear, moreover, that there
will be only rational powers of x present in the formal series
β_{Γ−s}(x) since the constants γ occurring in (7 a; § 1) differ by
rational fractions in the consecutive formal series (7 a; § 1) in any

## [p. 51] — Lemma 9 closure + L_{n−Γ} construction + (6 a) formal series

group (I; p. 213) of such series (containing logarithms). Thus the
operator L_Γ(y) has all the properties required by the lemma. The
factorization (1 a) follows immediately. The coefficients in the
operator L_{n−Γ}(z),

(6)   L_{n−Γ}(z) = z(x + n − Γ) + c_1(x) z(x + n − Γ − 1) + ...
                                                  + c_{n−Γ}(x) z(x),

will be analytic in (1) + ... + (m) and will be of the required
character in (1) + ... + (m). The lemma is therefore proved.

The equation L_{n−Γ}(z) = o will be formally satisfied, in
(1) + ... + (m), by the series

(6 a)   ...   (k = 1, ..., n − Γ).

On taking account of the established nature of the b_{Γ−s}(x)
(s = 0, 1, ..., Γ − 1), it is seen that the series s_{Γ+k}(x) are
s-series.

[end of § 6]

---

## Tag legend

This file is the §6 verbatim transcript only. All sentence-level
[CLAIM-B6n] tags + paraphrases + page anchors are recorded in
`bt_1933_section_6_claim_table.md`. Lemma 9 (§6 Acta p. 48) is
indexed in `bt_1933_sections_4_6_main_theorems.md` as identifier T3.

§6 is the **D2-NOTE v2.1 §4.5 BT-citation region**. The side-by-side
audit `d2_note_v21_bt_citation_audit.md` cross-references this
extract.
