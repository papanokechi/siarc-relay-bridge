# Author request — Wong & Li (1992a)

> ## SUPERSEDED 2026-09-18 — do not send
>
> **This route is dropped.** Operator ruling at review #21: R. Wong retired in
> 2019 and is emeritus, so the plan is **purchase, not correspondence**. The
> purchase target's citation was confirmed the same day by DOI content
> negotiation:
>
> > R. Wong and H. Li, *Asymptotic Expansions for Second-Order Linear Difference
> > Equations, II*, **Stud. Appl. Math. 87(4) (1992), 289–324**,
> > DOI `10.1002/sapm1992874289`, issued 1992-11.
>
> The contents check that would have justified correspondence is also done:
> Wong & Zhao's 2022 survey (arXiv:2204.09305, CC-BY-4.0, now in `refs/`)
> confirms at §3 that Wong–Li II covers this equation class — equation (3.2),
> `y(n+2) + n^p a(n) y(n+1) + n^q b(n) y(n) = 0` — while the growth law is
> **NOT FOUND in §3 by full-text read** (pp. 12–20, six positive controls
> fired; `CT-S21-DEPOSIT-PREP/outputs/wz_sec3_absence.json`). Stated as an
> absence claim with its scope and method, not as "the survey does not state
> it". §3 is in fact a turning-point theory that normalises the growth away at
> (3.23), so the quantity is out of its view by construction. The purchase is
> warranted and the request letter is not.
>
> This file is retained as a record of the title trap (`R1-61`) it caught, which
> is still live: *"Wong & Li 1992a"* alone retrieves the wrong paper, and the
> word **"linear"** and the numeral **"II"** are both load-bearing. Nothing below
> is to be acted on.

---

> ## Status: operator draft received, and the title check fired
>
> The draft did not arrive with review #5 (that message ended at the instruction
> to check the title); it was supplied separately. It is reproduced **corrected**
> in §3, with the defect recorded in §1.
>
> **The title as drafted was wrong, in both the subject line and the body.**
> The operator anticipated this and asked for the check. It was worth making.

---

## 1. The title check — and it fired

Checked 2026-09-17 against **two independent sources**, as the P0 citation rule
requires.

**Source A — publisher metadata** (Crossref, registrant of record for the DOI):

> **Asymptotic Expansions for Second-Order Linear Difference Equations, II**
> R. Wong and H. Li. *Studies in Applied Mathematics* **87**(4), 1992,
> pp. 289–324. **DOI `10.1002/sapm1992874289`** · ISSN 0022-2526

**Source B — DLMF bibliography**, from the stored copy
`refs/dlmf_bib_W.html` (sha256 `2a90b9f01153541fe38f804d…`), key **1992a**:

> R. Wong and H. Li (1992a) Asymptotic expansions for second-order **linear**
> difference equations. II. Stud. Appl. Math. 87 (4), pp. 289–324.

### The defect

The draft renders the title as

> "Asymptotic expansions for second-order difference equations, II"  *(subject)*
> "Asymptotic expansions for second-order difference equations. II"  *(body)*

**The word "linear" is missing from both.** Both sources carry it. It is
corrected in §3 in both places.

The two sources differ from each other only in styling — publisher uses title
case and a comma before "II", DLMF uses sentence case and a period. That
difference is immaterial. The missing word is not.

### Why this particular omission is worth catching

The DLMF entry immediately below is:

> R. Wong and H. Li (**1992b**) Asymptotic expansions for second-order linear
> difference equations. *J. Comput. Appl. Math.* **41**(1–2), pp. 65–94.

**The two papers have the same title but for the trailing "II".** They are
different papers in different journals, and only **1992a** — the "II" paper — is
the one DLMF cites for our case; 1992b treats the bounded-coefficient case,
which is not ours. A request quoting a degraded title to an author who wrote
both is a request that can be answered with the wrong paper. The safest
practice, adopted in §3, is to quote the **journal, volume, pages and DOI**
alongside the title, so the identification does not rest on the title at all.

Never quote the DLMF key "1992a" to a third party; it is DLMF-internal.

## 2. Contact address — NOT looked up

Per your instruction I have **not** guessed or supplied an address. Find a
current one from the corresponding author's institutional page rather than from
the 1992 paper.

Note for your search, stated as uncertain: R. Wong is associated in the
literature with City University of Hong Kong, and a City University research
portal page for this publication appeared in an open web search during the
prior-art session. I have **not** verified any current affiliation or address,
and both authors' positions may well have changed in the thirty-plus years
since publication. Treat this as a starting point only.

## 3. Your draft, corrected

Changes from your text are **bolded**. There are two, and they are the same
change: the word *linear*, restored in the subject line and in the citation.
I have also added the DOI, for the reason in §1. Nothing else is altered — the
tone, length and content are yours.

> **Subject:** Reprint request: "Asymptotic expansions for second-order
> **linear** difference equations, II" (Stud. Appl. Math. 87, 1992)
>
> Dear Professor Wong,
>
> I am an independent researcher working on the asymptotics of polynomial
> continued fractions. I would be grateful for a copy of your paper with H. Li:
>
> > R. Wong and H. Li, "Asymptotic expansions for second-order **linear**
> > difference equations. II", *Studies in Applied Mathematics* **87**(4)
> > (1992), 289–324**, doi:10.1002/sapm1992874289**.
>
> The DLMF (§2.9(ii)) refers to this paper for the case I am studying:
> recurrences y(n+1) = b(n) y(n) + y(n−1) where b is a polynomial of degree
> d ≥ 2. I want to check whether the growth exponent of the dominant solution,
> and the constant multiplying it, already appear in your paper **in *Studies in
> Applied Mathematics***, so that I can attribute them correctly rather than
> present them as new.
>
> I would be glad to send you my note once it is written up.
>
> With thanks and best regards,
>
> Papanokechi
> Independent researcher, Yokohama
> ORCID 0009-0000-6192-8273

### The two further changes, now authorised and applied

Both were identified during the review pass and held back; the operator has
since authorised them.

1. **§2.9 → §2.9(ii).** That is the subsection carrying the Wong–Li citation and
   the bounded-coefficient restriction that motivates the request, so it is the
   passage the author would turn to.
2. **"your paper" → "your paper in *Studies in Applied Mathematics*".** The
   journal is named in full rather than by nickname, which reads better to an
   author and resolves the two-papers ambiguity just as well. The DOI stays.

**The draft is now ready to send.** Finding a current address and sending are
operator actions; neither has been done.

## 4. Identity block — checked against the repository, not assumed

Your signature block was verified character by character against
`sessions/2026-06-16/VQUAD-ZENODO-DEPOSIT-001/upload-copy-paste.md`, which
records the deposit metadata:

| Field | Repository | Your draft | |
|---|---|---|---|
| Name | `Papanokechi` (mononym, given name blank) | Papanokechi | match |
| ORCID | `0009-0000-6192-8273` | 0009-0000-6192-8273 | match |
| Affiliation | `Independent Researcher, Yokohama, Japan` | Independent researcher, Yokohama | match (shortened) |

The ORCID was compared digit by digit. It is correct. I did not need to invent
any part of this block, which is as it should be.

## 5. Status

**Nothing has been sent.** This file is a draft only; sending is an
operator-gated action, as is the Wiley purchase.

Wong–Li (1992a) remains **NOT OBTAINED**, and is still the sole blocker on the
Channel Theory v1.7 notice. The companion v1.3 notice does not depend on it,
which is why it goes first.
