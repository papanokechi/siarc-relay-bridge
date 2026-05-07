# Adams 1928 — Bibliography (assembled from footnotes)

**Source PDF SHA-256:**
`d7ac4017a9737fef00e10257f26b9a6a6f6cc23437d2654440359f2e24836e18`

## Anomaly: no separate reference list

Adams 1928 contains **no separate bibliography section**. All references
to the prior literature appear as footnotes within the text body —
primarily within the Introduction footnote-block on PDF p02–p03
(printed p507–p508). A small number of additional citations appear
inline in body footnotes (e.g., "Birkhoff, loc. cit." on PDF p9, p11,
p23, p24). The relay-prompt task description (clause (e)) anticipates a
"reference list at p. 540–541 tail block"; no such list exists. This
bibliography is therefore reconstructed from the Introduction
footnote-block and inline body citations. The reconstruction discrepancy
is logged in `discrepancy_log.json` as D1.

## Reconstructed reference list

Each entry is reproduced from the verbatim footnote text where possible.
Where the pypdf rendering is ambiguous (German umlauts, italic-symbol
artefacts, paragraph-break dashes), the verbatim form is preserved and
the canonical bibliographic interpretation given as a parenthetical
gloss.

### [Footnote *] (PDF p02, asterisk on Adams's title)

> "Presented to the Society, December 28, 1926; received by the editors
> in July, 1927."  (Self-citation: this paper.)

### [Footnote †] (PDF p02; Barnes 1905)

> "On the homogeneous linear difference equation of the second order with
> linear coefficients, Messenger of Mathematics, vol. 34 (1905),
> pp. 52–71."

**Author (inferred from body text "Barnes"):** E. W. Barnes (text on
p. 507 attributes to "Barnes").
**Year:** 1905. **Journal:** Messenger of Mathematics, Vol. 34.
**Pages:** 52–71.

### [Footnote ◊] (PDF p02; Horn 1910)

> "Über das Verhalten der Integrale linearer Differenzen- und
> Differentialgleichungen für grosse Werte der Veränderlichen, Crelle's
> Journal, vol. 138 (1910), pp. 159–191, in particular p. 191."
> (pypdf renders "fiir" for "für" and "Verdnderlichen" for
> "Veränderlichen".)

**Author (inferred from body text "Horn"):** J. Horn.
**Year:** 1910. **Journal:** Crelle's Journal (J. reine angew. Math.),
Vol. 138. **Pages:** 159–191 (special attention p. 191).

### [Footnote ‡] (PDF p02; Batchelder 1912/1913)

> "The divergent series satisfying linear difference equations of the
> second order and The hypergeometric difference equation, Bulletin of
> the American Mathematical Society, vol. 19,"  (≤ 30 words; tail
> page-range "pp. 498, 500–502" recorded in the structured fields
> below.)

**Author (inferred):** P. M. Batchelder.
**Year:** 1912–13. **Journal:** Bull. Amer. Math. Soc., Vol. 19.
**Pages:** 498, 500–502.

### [Footnote *] (PDF p03; Birkhoff 1911)

> "General theory of linear difference equations, these Transactions,
> vol. 12 (1911), pp. 243–284."

**Author:** G. D. Birkhoff. **Year:** 1911. **Journal:** Trans. Amer.
Math. Soc., Vol. 12. **Pages:** 243–284. **In-paper short form used
elsewhere:** "Birkhoff, loc. cit." (PDF p09 fn, PDF p11 fn, PDF p23 fn,
PDF p24 fn).

### [Footnote †] (PDF p03; Batchelder dissertation)

> "The hypergeometric difference equation."  (Harvard Library
> Dissertation, 1916, per body text.)

**Author:** P. M. Batchelder.
**Year:** 1916. **Type:** Dissertation deposited in Harvard Library.
**Note from body text (p. 508):** "they are also incorporated in An
Introduction to Linear Difference Equations, presently to be published
with the aid of the National Research Council."

### [Footnote ‡] (PDF p03; Perron 1917)

> "Über lineare Differenzengleichungen zweiter Ordnung deren
> charakteristische Gleichung zwei gleiche Wurzeln hat,
> Sitzungsberichte der Heidelberger Akademie der Wissenschaften
> (mathematisch-naturwissenschaftliche Klasse), vol. 8A (1917), No. 17,
> 18 pp."

**Author (inferred):** O. Perron. **Year:** 1917. **Venue:**
Sitzungsber. Heidelberger Akad. Wiss. (math.-naturwiss. Klasse), Vol.
8A, No. 17. **Length:** 18 pp.

### [Footnote ◊] (PDF p03; Galbrun 1921)

> "Sur certaines solutions exceptionnelles d'une équation linéaire aux
> différences finies, Bulletin de la Société Mathématique de France,
> vol. 49 (1921), pp. 206–241."  (pypdf elides accents.)

**Author (inferred):** H. Galbrun. **Year:** 1921. **Journal:** Bull.
Soc. Math. France, Vol. 49. **Pages:** 206–241.

### [Footnote ¶] (PDF p03; Galbrun 1913)

> "Sur la représentation des solutions d'une équation linéaire aux
> différences finies pour les grandes valeurs de la variable, Acta
> Mathematica, vol. 36 (1913), pp. 1–68."

**Author:** H. Galbrun. **Year:** 1913. **Journal:** Acta Math.,
Vol. 36. **Pages:** 1–68.

### [Footnote §] (PDF p03; Nörlund 1924)

> "Berlin, Springer, 1924, pp. 339–342."  (Title in body text:
> "Differenzenrechnung".)

**Author:** N. E. Nörlund. **Title:** Differenzenrechnung.
**Year:** 1924. **Publisher:** Berlin: Springer. **Page-span cited:**
pp. 339–342.

## Cross-walk to BT 1933 bibliography

BT 1933 (Birkhoff & Trjitzinsky, *Analytic Theory of Singular Difference
Equations*, Acta Math. **60** (1933), 1–89; SHA
`dcd7e3c6b2a12ae1ce917d322763ff9dde5ec69ab5f23080d043699822d68fe6`)
contains no traditional bibliography section. References appear as
footnotes throughout. The Adams 1928 paper is cited explicitly on
**BT 1933 p. 5** (footnote 2):

> "C. R. Adams, On the Irregular Cases of the Linear Ordinary Difference
> Equations, Trans. Am. Math. Soc., vol. 30 (1928), pp. 507–541."  
> (pypdf renders "Equations" as "Equations", year as "I928",
> page-range as "5o7–54." with truncated final digit; canonical pages
> 507–541.)

Cross-walk audit (which Adams 1928 references also appear in BT 1933):

| Adams 1928 reference | Cited in BT 1933? | BT 1933 page |
| --- | --- | --- |
| Birkhoff 1911 (Trans. AMS 12) | YES (BT 1933 references Birkhoff repeatedly throughout — Birkhoff is a co-author of BT 1933 and "Birkhoff" appears in pypdf hits on 47 of 89 pages, mostly running-header in printed paper) | p. 2, p. 4, p. 6, … (frequent) |
| Galbrun 1921 (Bull. Soc. Math. France 49) | YES — explicitly cited on BT 1933 p. 5 footnote 1: "H. Galbrun, Sur certaines solutions exceptionnelles d'une équation linéaire aux différences finies, Bull. Soc. Math. de France, vol. 49 (1921), pp. 206–241." | p. 5 |
| Galbrun 1913 (Acta Math. 36) | DEFER — pypdf hit on Galbrun appears on BT 1933 p. 4 ("Galbrun" mention) but the corresponding footnote was not extracted in this session's quick-scan; mark for future audit | p. 4 (mention) |
| Carmichael (NEW in BT 1933, NOT in Adams 1928) | YES, BT 1933 p. 4 | p. 4 |
| Barnes 1905 | DEFER — not detected in BT 1933 quick-scan; absence is plausible since BT 1933 covers a more general setting than Barnes's quadratic-coefficient n=2 special case | (none detected) |
| Horn 1910 | DEFER — not detected in BT 1933 quick-scan | (none detected) |
| Perron 1917 | DEFER — not detected in BT 1933 quick-scan | (none detected) |
| Batchelder 1912/1913 + dissertation | DEFER — not detected in BT 1933 quick-scan | (none detected) |
| Nörlund 1924 (Differenzenrechnung) | DEFER — not detected in BT 1933 quick-scan | (none detected) |

**DEFER items** are surfaced in `unexpected_finds.json` as U-items for
future audit. The DEFER markers indicate the cross-walk is partial; a
fuller BT 1933 bibliography readthrough (analogous to the present 072
session for Adams 1928) is the natural follow-up substrate task.

## Scope-of-canonical-pre-1928-difference-equation literature note

The relay-prompt clause (e) names "Carmichael, Birkhoff, Nörlund,
Galbrun" as canonical pre-1928 difference-equation literature for
cross-walk. Of these, Birkhoff (1911), Nörlund (1924) and Galbrun
(1913, 1921) are present in Adams 1928's footnotes; **Carmichael is
NOT cited in Adams 1928** (Carmichael is, however, cited in BT 1933
p. 4). The omission of Carmichael from Adams 1928 is a substrate-
inventory fact, not a comment on Adams's coverage.
