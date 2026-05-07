# BT 1933 §5 "Construction of Proper Solutions to the Right of a Proper Curve" — Verbatim Extract

**Source PDF SHA-256:**
`dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6`
**Section span:** Acta p. 40 (PDF p. 40) — Acta p. 48 (PDF p. 48).
**Section title (verbatim, TOC):**
"Construction of proper solutions to the right of a proper curve."

Page anchors `[p. NN]` mark each Acta-page break. Math symbols are
reproduced as rendered by pypdf 6.10.2; isolated font-glyph drift is
flagged where it affects interpretation. The pypdf substitution
`w → §` is silently restored in section-headers and cross-section
references throughout.

---

## [p. 40] — section opener

§ 5.   Construction of Proper Solutions to the Right of a Proper Curve.

The following theorem will be proved.

## [p. 41] — Theorem I statement

Theorem I. Assume that the coefficients of an equation L_n(y) = o
(2; § 1) are known (cf § 1) in a subregion of F (§ 1),

  F = (1) + (2) + ... + (m) + ... + (η).

Let the corresponding functions Q(x) be

(1)   Q_1(x), ... Q_n(x).

Suppose that Γ, a proper curve (Def. 9; § 1) for the set (1), is the
left boundary of (m) (2 ≦ m ≦ η) or lies to the left of it. Assume that
in a strip V, of unit width and with its left boundary coincident with
the left boundary of (m), there exists a proper fundamental set of
solutions (Def. 4; § 1) satisfying the equation L_n(y) = o.

It will necessarily follow that L_n(y) is completely proper (Def. 6;
§ 1) in (m) + ... + (η).

If Γ, a proper curve for the set (1), exists in the region (1) then the
above assumption concerning existence of solutions in V may be omitted
and it will necessarily follow that L_n(y) is completely proper in
(m) + ... + (η)   (m = 1).

Proof. As stated previously the regions (1), (2), ... (η) are separated
by B'-curves,

(2)   B^1, B^2, ..., B^{η−1}.

In any region (s) of this set of regions the Q'_j(x) (j = 1, ... n)
maintain a certain ordering. We shall write

(3)   ℜ Q'_1(x) > ℜ Q'_2(x) > ... > ℜ Q'_n(x).   (x in (s)).

In connection with this ordering the subscript s will be attached, from
the left, to some other symbols; thus, _sS(x) will denote the formal
matrix of a difference system corresponding to L_n(y) = o, with
_sQ_j(x) entering in the j-th column. The set [_sQ_1(x); _sQ_2(x), ...
_sQ_n(x)] is merely a permutation of the set [Q_1(x), Q_2(x), Q_n(x)].

It is sufficient to prove the theorem for the system Y(x + 1) = D(x)Y(x),
related to the given equation (2; § 1) and given by (6; § 1). This
follows from the relationship (6 a; § 1) between solutions of the
system and the single equation. It is clear that the d_{ij}(x) are
known and of the same character as the a_j(x) (j = 1, ... n), the
coefficients of L_n(y). The process of construction of solu-

(printer-line) "6—32511. Acta mathematica. 60. Imprimé le 2 septembre 1932."

## [p. 42] — induction setup, determinant limits

tions, about to be given, is of course equally applicable to any system
Y(x+1) = Z(x) Y(x) (1 a; § 1).

By iteration (3) we construct, in (m), determinant limits of orders
1, 2, ... n corresponding to the _sQ(x)'s

  _mQ_1(x), _mQ_1(x) + _mQ_2(x), ..., _mQ_1(x) + ... + _mQ_n(x),

respectively. When m = 1 this process will be carried on by
"iteration from the infinite left" (Lemmas 4 and 5; § 3). When m > 1
the process will be carried on by iteration from the strip V, specified
in the theorem. In the latter case use will be made of the existence of
solutions in V, as stated in the theorem; in this connection Lemmas 6
and 7 (§ 3) are to be used. Generally speaking, application of Lemmas
4, 5, 6 and 7 is possible in virtue of the inequalities (3) being valid
in (m) (for s = m).

In agreement with the notation of § 3 let these determinant limits be
denoted, for k = 1, ... n, by

(4)   _m y_{i_1...i_k; 1...k}(x)
                (i_1 < ... < i_k; i_1, ..., i_k = 1, ..., n).

These functions are analytic in (m) and satisfy the asymptotic relations

(4 a)   _m y_{i_1...i_k; 1...k}(x)
        ∼ e^{_m Q_1(x) + _m Q_2(x) + ... + _m Q_k(x)}
          _m S_{i_1...i_k; 1...k}(x)
        (i_1 < ... < i_k; i_1, ..., i_k = 1, ..., n; x in (m)).

For k = 1 the functions (4) are elements of a solution of the system
Y(x+1) = D(x) Y(x); write

(4 b)   _m z_{i 1}(x) = _m y_{i; 1}(x)   (i = 1, ..., n).

This solution is proper in (m). Assume that, for k − 1 ≧ 1, there exist
k − 1 solutions,

(4 c)   _m z_{i j}(x)   (i = 1, ..., n; j = 1, ..., k − 1),

which are analytic in (m), satisfy the relations

(4 d)   _m y_{i_1...i_s; 1...s}(x) = _m W_{i_1...i_s; 1...s}(x)
        (i_1 < ... < i_s = 1, ..., n; s = 1, ..., k − 1; x in (m))

and are such that, in (m)

## [p. 43] — induction step, formal column k

(4 e)   _m z_{i j}(x) ∼ e^{_m Q_j(x)} _m s_{i j}(x)
        (i = 1, ..., n; j = 1, ..., k − 1).

Existence of a matrix of solutions, proper in (m), will be demonstrated
by induction if we show that there exists a solution _m z_{i k}(x)
(i = 1, ..., n) analytic in (m) and such that (4 d), (4 e) will hold for
s = k, j = k. Analogous to a similar construction, in II, such a
solution can be found in terms of certain determinant limits and the
solutions (4 c). For this purpose use will be made of the following
formulas, found in (II). (The notation used in this paper is different
from that of (II).)

We have

(5)   _m z_{1 k}(x) = ∑_{j=1}^{k−1} _m z_{1 j}(x) ∑_{t≡x} _m v_{k j}(t),

(5 a)   _m v_{k j}(t) = _m O^{(k)}(t) _m m_{j, k−1}(t)
                      / [_m O^{(k−1)}(t) · _m O^{(k−1)}(t + 1)],

(5 b)   _m m_{j, k−1}(t) = (− 1)^{k−1+j}
        | _m z_{i_1 1}(t + k − 2)  ...  _m z_{i_1 k−1}(t + k − 2) |
        | ............................................ ... |
        | _m z_{i_{k−1} 1}(t)      ...  _m z_{i_{k−1} k−1}(t)   |

(5 c)   _m O^{(k)}(t) = ∑_{i_1 ... i_k = 1}^{n} d_{1 i_1}(t)
                       ∑ d_{i_1 i_2}(t + 1) d_{i_1 i_2}(t) + ...
                     + _m y_{1 i_1, ..., i_{k−1}; 1...k}(t).

Moreover, for x in (m),

(5 d)   _m O^{(k)}(x) =
        | e^{_m Q_1(x)} _m s_1(x)                                    |
        | e^{_m Q_1(x+1)} _m s_1(x+1)                                |
        | ............................                              |
        | e^{_m Q_1(x+k−1)} _m s_1(x + k − 1) ... _m z_{1 1}(x+k−1)  |
        |                                                            |
                                ... e^{_m Q_k(x)} _m s_k(x)
        and similar for higher rows.

while

(5 e)   ...   _m Q_2(x) | e^{_m S_2(x)} ... e^{_m Q_k(x)} _m s_k(x)
        ...

## [p. 44] — application of Lemma 8 (§4) to (5)

The symbol ∑_{t≡x} stands for summation and is to be suitably determined.
It is seen that the _m m_{j, k−1}(t) (j = 1, ..., k−1) and _m O^{(k)}(t)
are known and analytic in (m).

Using (5 b) and the known asymptotic forms (4 e) the asymptotic form of
_m m_{j, k−1}(x) will be seen to be

(6)   _m m_{j, k−1}(x) ∼ e^{_m Q_1(x) + ... + _m Q_{j−1}(x) + _m Q_{j+1}(x)
                          + ... + _m Q_{k−1}(x)}
                        _m m'_{j, k−1}(x)
                        (_m m'_{j, k−1}(x), an s-series; x in (m)).

On the other hand, making use of (5 d) and taking account of the way
several formal series with logarithms in the s-series factors are
related (See (I); in particular, (6'') on p. 213), we conclude that

(6 a)   _m O^{(k)}(x) ∼ e^{_m Q_1(x) + ... + _m Q_k(x)}
                        _m φ^{(k)}(x)        (x in (m))

where _m φ^{(k)}(x) is an s-series without logarithms. The series
_m φ^{(k)}(x) (k = 1, ..., n) cannot be identically zero since the
formal series are assumed to be linearly independent. Consequently, by
(5 a), (6) and (6 a),

(6 b)   _m v_{k j}(x) ∼ e^{_m Q_{k j}(x)} _m v_{k j}(x)
        (j = 1, ..., k − 1; x in (m)).

Here the series _m v_{k j}(x) are all s-series; moreover, by ((3); s = m),

  ℜ _m Q'_{k j}(x) ≦ o     (j = 1, ..., k − 1; x in (m)).

It is easily seen that **Lemma 8 (§ 4) is applicable** for evaluation
of any of the expressions

(6 c)   ∑_{t≡x} _m v_{k j}(t)   (j = 1, ..., k − 1)

occurring in (5). In that lemma we only need to take R = (m),
Q(x) = _m Q_{k j}(x), h(x) = _m v_{k j}(x). Thus, by the methods of § 4
we evaluate (6 c) as a function analytic in a region (m)', slightly
interior to (m), and satisfying in (m)' an asymptotic relation

(footnote) "We can show this by a reasoning, applied to the second
member of (5 d), similar to that in (I; p. 215)."

## [p. 45] — column-k construction complete

  (6 d)   ∑_{t≡x} _m v_{k j}(t) ∼ e^{_m Q_{k j}(x)} _m u_{k j}(x)

where _m u_{k j}(x) is an s-series. Since the boundaries of (m) can be
translated, it may be considered that (6 d) holds in (m). Substituting
(4 e) and (4 d) in (5) it is seen that _m z_{1 k}(x) is analytic in (m)
and

(7)   _m z_{1 k}(x) ∼ e^{_m Q_k(x)} _m a_{1 k}(x)         (x in (m)),

where _m a_{1 k}(x) is a formal s-series.

The remaining elements _m z_{i k}(x) (i = 2, ..., n) of the (k-th)
solution may be determined as follows. We have

  _m z_{1 k}(x + q) = ∑_{λ_1, ..., λ_q = 1}^{n} d_{1 λ_1}(x + q − 1)
                                  d_{λ_1 λ_2}(x + q − 2)
                                  ... d_{λ_{q−1} λ_q}(x) _m z_{λ_q k}(x)
        (q = 1, ..., n).

By the reasoning of (II; p. 259) these equations have a non-vanishing
determinant so that

(8)   _m z_{i k}(x) = α_1(x) _m z_{1 k}(x + 1) + ... + α_n(x) _m z_{1 k}(x + n)
                      (i = 1, ..., n).

Here the α_{i j}(x) (i, j = 1, ..., n) are known in (m) and are of the
same nature as the d_{i j}(x). Thus, by (7) and (8), the elements
_m z_{i k}(x) (i = 1, ..., n) are analytic in (m) and satisfy, in (m),
the asymptotic relations

(9)   _m z_{i k}(x) ∼ e^{_m Q_k(x)} _m a_{i k}(x)         (i = 1, ..., n)

where the series _m a_{i k}(x) are s-series. Necessarily the relations
(4 d) will be satisfied for s = 1, ..., k. The function _m z_{1 k}(x)
is such that (5 e) holds; thus, using the asymptotic relationships
(4 d), (4 e) and (9), we conclude that the _m a_{i k}(x) (i = 1, ..., n)
in (9) can be replaced by the _m s_{i k}(x) (i = 1, ..., n),
respectively. Thus a solution _m z_{i k}(x) (i = 1, ..., n), possessing
all the desired properties, has been constructed. This proves existence
of a matrix solution proper in (m). The above indicates also the actual
process of construction in any given case which satisfies the specified
hypotheses. It is essential to note that in applying Lemma 8 we have,
according to the hypotheses of the Theorem and as required by the
Lemma,

## [p. 46] — extension to (m+1), ..., (η) + periodic-functions setup

the function Q(x) = _m Q_{k j}(x) proper along the portion of the path
of integration near the right boundary of (m). If in the various
summations involved in (5) additive periodic functions are admitted the
k-th solution, _m z_{i k}(x)(i = 1, ..., k), will be modified by
addition of linear expressions (with periodic coefficients) in the
elements of the preceding k − 1 solutions. Unless stated otherwise such
periodic functions will not be introduced, the summations in (5) being
specified by § 4. The n solutions constituting the n columns of the
matrix

(10)   _m Z(x) = (_m z_{i j}(x))    (i, j = 1, ..., n)

may be spoken of as 'associated with determinant limits'.

The regions (1), (2), ... (η) may be considered as having strips
V_{j, j+1} (between (j) and (j+1); j = 1, ..., η − 1), of unit width,
in common. In the case at hand, there exists a proper matrix solution
in V_{m, m+1} (if m + 1 ≦ η). By the process indicated for the
construction of _m Z(x) we now obtain a matrix solution,

(10 a)   _{m+1} Z(x) = (_{m+1} z_{i j}(x)),

proper in (m + 1), the constituent solutions (columns) being associated
with the determinant limits, known in terms of the _m z_{i j}(x) in
(m + 1). By a finite number of steps proper matrix solutions,
_r Z(x) = (_r z_{i j}(x)) (r = m, ..., η), are constructed in (m),
(m + 1), ..., (η); these solutions will be associated with determinant
limits.

It remains to demonstrate that the periodic functions connecting these
solutions are proper (Def. 5; § 1). Let Z^r(x) = (z^r_{i j}(x)) denote
_r Z(x) with the columns so rearranged that

(11)   Z^r(x) ∼ S(x) = (e^{Q_j(x)} s_{i j}(x))    (x in (r); r ≧ m).

Write

(11 a)   Z^r(x) = Z^{r+1}(x) p^{r, r+1}(x),
                    p^{r, r+1}(x) = (p^{r, r+1}_{i j}(x)).

Let ℑ x_r = ℑ x, x − x_r = integer and restrict x_r to lie in the strip
V_{r, r+1} (when ℑ x ≧ Q > o). We have then for the matrix p^{r, r+1}(x)
of periodic functions the relation

(11 b)   p^{r, r+1}(x) = p^{r, r+1}(x_r)
                       = Z^{r+1, −1}(x_r) Z^r(x_r).

For x (= x_r) in V_{r, r+1} the following asymptotic relation will hold
in virtue of (11)

## [p. 47] — proper-periodic-functions verification + Theorem I closure

(12)   p^{r, r+1}(x) ∼ S^{−1}(x) S(x) = (e^{Q_j − i(x)} φ_{0})
                                        ((φ_{0}) = 1).

In other words, for ℑ x ≧ Q > o,

  [the inequality (12 a) for p^{r, r+1}_{i j}(x_r)]

in the above k can be made arbitrarily great and the |b_{i j}(x_r)|, for
a fixed k, are bounded. The strips V_{r, r+1} (r = m, ..., η − 1) extend
indefinitely upwards (i.e., when |x| approaches infinity in V_{r, r+1},
v = ℑ x → +∞). These strips are to the right of a proper curve Γ and
they are in a proper region R^p (Def. 9; § 1). The term 'proper' refers,
in this connection, to the set Q_1(x), ..., Q_n(x).

By (11 b) the p_{i j}^{r, r+1}(x) are analytic for v ≧ Q > o. By (12 a)
and in virtue of the fact that the φ_{i j}(x_r) are proper in V_{r, r+1}
(Def. 3; § 1) it follows that

(13)   ...
        (i, j = 1, ...... n; r = m, ..., η − 1; π^{r, r+1}_{i j}
         an integer);

here the power series converge within a sufficiently small circle with
z = o for center and, unless p^{r, r+1}_{i j}(x) ≡ o, it may be
supposed that p^{r, r+1}_{i j; o} ≠ o. Now |z| = |e^{−x_r}| = e^{−q+v};
thus, it is clear that

(13 a)   p^{r, r+1}_{i j}(x) = ∑ p^{r, r+1}_{i j; π} e^{−π_{i j}(r, r+1)}
        (i, j = 1, ..., n; r = m, ..., η − 1)

in every region of the kind indicated in (Def. 5; § 1). Hence, in
accordance with this definition, these periodic functions are proper.
In view of the relationship between solutions of the single equation
L_n(y) = o, and those of the system, L_n(y) is seen to be completely
proper in (m) + ... + (η).

[end of § 5]

---

## Tag legend

This file is the §5 verbatim transcript only. All sentence-level
[CLAIM-B5n] tags + paraphrases + page anchors are recorded in
`bt_1933_section_5_claim_table.md`. Theorem I (§5 Acta p. 41) is
indexed in `bt_1933_sections_4_6_main_theorems.md` as identifier T2.

A [CHART-MAP-CANDIDATE-Bn] tag in §5 (if any) is surfaced
prominently in `bt_1933_section_5_claim_table.md` Phase C.4 and in
`unexpected_finds.json` per relay 073 prompt clause C.4.
