# Adams 1928 — Main Theorems / Results Summary

**Source PDF SHA-256:**
`d7ac4017a9737fef00e10257f26b9a6a6f6cc23437d2654440359f2e24836e18`
**Page span:** printed p507–p541 (PDF p2–p36).

## Labelling note

Adams 1928 contains exactly **two** explicitly labelled theorems:
**THEOREM A** (printed p529) and **THEOREM B** (printed p537), both in
§6. All other "results" in the paper are stated in narrative prose
without numbered labels. Per the relay-prompt directive to enumerate
indexed identifiers, the table below assigns identifiers T1 through T9
covering both labelled and unlabelled (narrative-stated) main results,
flagged in the "Labelled?" column. T1 and T2 correspond to Adams's
literal Theorems A and B; T3–T9 are headlining narrative results that
function as theorems but are not so labelled.

Verbatim quotes are direct substrate citations from Adams 1928 (P6
exemption applies; ≤ 30 words enforced per P7). Two statements
exceeding 30 words verbatim (Theorem A, Theorem B) are paraphrased
with explicit framing per P7.

## Indexed-result table

| ID | Section | Printed p | Labelled? | Scope | Statement (verbatim ≤ 30 words OR paraphrase ≤ 30 words) |
| --- | --- | --- | --- | --- | --- |
| **T1** | §6 | p. 529 | YES (Theorem A) | Class 1 (n-fold root); n×n Class 2 inherits via §8 | *Adams 1928 §6 p. 529 states (in our paraphrase):* form the m-fold left-product P_m(x) = A(x−1) ⋯ A(x−m) T(x−m); for K large enough, each λ-rowed determinant from the first λ columns converges to a definite limit function u_{ij…l}(x), independent of K, asymptotically represented by the corresponding determinant of S(x) in specified sectors. (Verbatim opening clause: "Form the product of matrices P_m(x) = A(x − 1) A(x − 2) … A(x − m) T(x − m)." — 18 words.) |
| **T2** | §6 | p. 537 | YES (Theorem B) | Class 1 (n-fold root); analogous on the right | *Adams 1928 §6 p. 537 states (in our paraphrase):* form the m-fold right-product P'_m(x) = A⁻¹(x) ⋯ A⁻¹(x+m−1) T(x+m); analogous determinant-limit existence and asymptotic representation hold, with sector specifications conjugate to Theorem A. (Verbatim opening clause: "Form the product of matrices P'_m(x) = A⁻¹(x) A⁻¹(x + 1) … A⁻¹(x + m − 1) T(x + m)." — 19 words.) |
| **T3** | §1 | p. 509 | NO | Class 1 | "Corresponding to a simple root pᵢ there is one formal series of the 'regular' type" (15 words; eq. (4) follows). |
| **T4** | §1 | p. 511 | NO | Class 2 | "(3) is replaced by several characteristic equations, one associated with each segment of L" (14 words). |
| **T5** | §2 | p. 513 | NO | Class 2a (mainly) and Class 2b | "In each case of Class 2a the equation (1) possesses n formal series solutions which we denote by (10)" (19 words). |
| **T6** | §3 | p. 517 | NO | Class 2a (and Class 2b w/ slight modification) | "P(x) = H⁻¹(x) G(x). The elements of H⁻¹(x) and G(x) are analytic except for poles over the entire finite plane" (~21 words spanning two short sentences). |
| **T7** | §4 | p. 518–p. 525 | NO | Class 2a (existence of asymptotic forms in the entire plane via critical rays, curvilinear asymptotes) | *Adams 1928 §4 p. 518 states (in our paraphrase):* the asymptotic form of g_{ij}(x) along rays in each quadrant is determined by which exponential factor in the matrix expansion (20) dominates, with critical-ray transitions identified by argument-of-pᵢ ordering. |
| **T8** | §7 | p. 538 | NO | Class 1, n=2, double root | "in this case the above argument leads to somewhat more inclusive results" (12 words). Strengthening of Theorems A and B to give intermediate solutions in larger sectors when n=2. |
| **T9** | §8 | p. 539–p. 541 | NO | Large class of irregular cases (mixed multiplicities; finite non-zero roots first, then extension to Class 2 with multiple roots in segment characteristic equations) | "the regions of validity of the asymptotic forms of some or all of the determinant limits for λ greater than this value of i are further restricted." (27 words from p. 541 last paragraph) — the explicit *regions-of-validity caveat* at the end of the paper. |

## Closing-paragraph caveat (p. 541, last paragraph)

Adams's paper ends with the sentence:

> "The extension of these statements to cases of Class 2, §1, in which
> the characteristic equations associated with segments of L have
> multiple roots is immediate."  (≤ 30 words after light elision of
> "one or more of the"; printed p. 541; PDF p. 36.)

This extension-clause is the bridge between Class 1 §8 and the Class-2
multiple-root setting. It is unlabelled in source.

## Word-count audit

Verbatim quotes counted on hyphen-segments-as-separate-words basis.
Maximum verbatim-quote word count: T9 = 27 words; T1 paraphrase
opening clause = 18 words; T2 = 19 words. Theorems A and B in their
full statement form exceed 30 words, hence paraphrased per P7 with
explicit "Adams 1928 §X p. Y states (in our paraphrase): …" framing.

## Forbidden-verb status

The forbidden tokens enumerated in P6 do not appear in any paraphrase
or scope-tag column of this file outside policy-exempt contexts.
Verbatim Adams quotes in the §1 + §2 extraction deliverables contain
the forbidden token in two places (the substrate-citation exemption
applies per P6); the present file contains no such tokens in non-
exempt context. See `forbidden_verb_scan.md` for the full E.1 + E.3
results.

## Paper-arc summary (substrate-inventory level)

§§1–4 build the Class-2 / Class-2a / Class-2b apparatus and the
asymptotic-form theory in the entire plane, paralleling Birkhoff
1911's regular-case treatment. §§5–6 specialise to the Class-1 n-fold
multiple-root case; §6 supplies the explicit Theorems A and B. §7
handles the n=2 special case in detail. §8 generalises §§5–7 to a
large class of irregular cases with mixed-multiplicity finite non-zero
roots and indicates extension to Class 2.
