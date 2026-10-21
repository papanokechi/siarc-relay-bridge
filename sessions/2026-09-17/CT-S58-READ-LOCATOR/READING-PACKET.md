# READING PACKET — CT-S58

The remaining Tier-1 and Tier-2 work is reading. This is the list of what to
read, in order, with page and line addresses. It locates; it does not judge.
Nothing here is a verdict on the prose.

Source of the page numbers: `outputs/locate_revision.out.txt`
(sha256 in `claims.jsonl`, claims S58-01..S58-06).
Source of the line numbers: `outputs/locate_painleve.out.txt` (S58-07..S58-10).

---

## TIER 1 — the LMP revision, end to end

File: `CT-S56-REBASE-V12/revision/vquad-periodrep-paper.pdf` — **27 pages**.
The journal holds **25** (v1.2), so page numbers here are NOT the editor's.
`CORRECTIONS-FOR-REFEREES.md` is keyed to v1.2's numbering; this packet is
keyed to the revision's.

All 33 edits are located. **8 of the 27 pages carry no change at all**; the 19
listed below do. They are where a correction list can have gone wrong in prose.

### Sitting 1 — §5 and Table 2 (10 edits on these five pages; item 5 has 13 in all)

Read **pages 14 → 18 continuously**. Do not read the edits individually; §5's
problem, if it has one, will be in the joins.

| page | what changed |
|---|---|
| **14** | §5 preamble — "three structurally independent ways" / "disjoint inputs" replaced; §5.1 heading changed to "Strategy: why three methods, and what each is independent of" |
| **15** | §5.1 Method A bullet — independence now **inferred, not measured**; §5.1 Method B bullet — the amplitude dependence named |
| **16** | §5.3 Method B chain — where S enters, at the substitution A = (S/2πi)Γ(1+β) |
| **17** | §5.3 Method B — the error figure and the independence sentence; this is where the **two numerical statements are separated** |
| **18** | four edits: `prop:cross` "disjoint inputs"; **Table 2 row B**; **Table 2 caption**; §5.5 closing on the "spurious triple coincidence" |

Three questions for this sitting:

1. p17 says "earlier versions of this paper conflated them". Does the text
   then actually separate them, or only announce that it will?
2. Table 2's row B now quotes **3.69×10⁻⁴⁶** where the old table quoted
   8.84×10⁻⁴⁶. Does the caption explain the change of figure to a reader who
   never saw the old table?
3. §5.1 now says Method A's independence is *inferred*. Does §5.5's closing
   still lean on A's independence as though it were measured?

### Sitting 2 — the new prose of item 4, never read rendered

| page | what changed |
|---|---|
| **7** | §2.2 proof — the structural argument restated; **Table 1** row now reads "reg. sing., logarithmic; B̂ holomorphic there" |
| **8** | **Prop 2.4** — apparency replaced by the resonant-step obstruction; and the **operator's ruling edit**: the "obtained twice" closing, rewritten to say what each route actually covered |
| **9** | proof of **Corollary 1.3** — "0 is apparent" replaced |
| **10** | **Lemma 2.7** restated and retitled "The point ξ=0 carries no period"; and the §4 algebraicity hedge |
| **11** | **Figure 1** — node label "(apparent)" → "(no cut)", and the caption |
| **12** | **Remark 3.4** — "the apparent point" |
| **25** | Appendix A.3 — the ξ=0 log computation recorded |

The page-8 ruling edit is the **only new prose in the paper that has never been
read in rendered form**. Read it aloud. It has to carry a distinction — the
indicial computation gives exponents at both points, direct Frobenius confirms
no logarithm at −ξ₀, and at 0 it finds one — without sounding like an erratum.

### Sitting 3 — the front matter, read last, against what the body now says

| page | what changed |
|---|---|
| **1** | abstract: D₅⁽¹⁾ now conjectural; abstract: "three structurally independent methods" replaced; §1.1 identification + the companion's v1.3 notice |
| **3** | **Theorem 1.2** — "proved twice" removed; **Theorem 1.1** — the three-methods sentence; §1.3 main results |
| **4** | §1.4 — "an independent structural argument" |

The operator's own question applies exactly here: **does §0 promise what the
paper delivers?** The abstract was edited twice, by two different items, in two
different sessions. Read it once as a stranger.

### Sitting 4 — the tail

| page | what changed |
|---|---|
| **21** | §7.1 — both item 1 and item 2 edits, adjacent |
| **24** | Appendix A.2 — "Independent structural confirmation" → "Structural consistency check (not independent of the above)" |
| **26** | A.5 — case-elimination plus the structural argument |
| **27** | the new bibitem for the companion's v1.3 |

Five pages carry edits from more than one item: **1, 3, 7, 10 and 21**. Page 21
is the one where the two items are logically coupled — item 1 makes the
identification conjectural and item 2 withdraws "completes part (ii)(a)", and
the second is *conditional on* the first. If the conditional reads as circular,
that is where it will show. Read pages 1, 3, 7 and 10 with the same question.

---

## TIER 2 — the Painlevé paper against the five correction items

File: `CT-S50-READ-REPAIRS/` — 15 `.tex` files, 2780 lines.
Full hit list with line numbers: `outputs/locate_painleve.out.txt`.

### Three results that shape this read before you start

**(1) The two papers share no notation.** The name patterns for `V_quad`,
`L_phi` and `L_V` all ran and returned **zero hits**. The same object appears
in the Painlevé paper as `b(n)=3n²+n+1` — `section0.tex:19`,
`section2.tex:235`, `section3.tex:17` — and the LMP paper is referred to as
"the companion record" (9 lines). A referee reading both would have to be told
they are the same object. That is the one-name-two-objects trap running
backwards: **two names, one object.**

**(2) Item 5 has no counterpart.** The Method A/B/C pattern ran and returned
**zero hits**. The Painlevé paper does not use the three-methods framing, so
nothing there inherits item 5.

**(3) Item 4's subject matter is already handled — correctly — but about a
different operator.** `section3.tex:114` is a subsection titled "The two finite
singular points are not apparent", and `section3.tex:125` states the governing
principle outright:

> "Exponents {0,0} do not by themselves decide apparency: what decides it is
> the logarithm."

That is precisely the inference the LMP paper made wrongly at ξ=0. Per the
operator's ruling this is **the same failure class, not corroboration**: it
concerns System C's finite points s±, a different operator's different points.
`section3.tex:152` already says so in those terms.

### The reading list, by item

| item | lines | priority |
|---|---|---|
| 1 — D₅⁽¹⁾ conjectural | `section1.tex:307,312`, `section3.tex:205`, `section4.tex:161`; plus 18 `Painlev` lines and 5 `conjectur` lines | **high** — check `section0.tex:66` ("No Painlevé label is asserted for this recurrence") still holds everywhere |
| 2 — stratum / "completes" | 3 lines | low |
| 3 — Galois, "twice" | 17 lines | medium — the LMP paper withdrew "proved twice"; check nothing here cites that withdrawn claim |
| 4 — apparency | 19 `apparen` + 7 `logarith` + 5 origin lines | **high** — but as failure class, not corroboration |
| 5 — independence | 39 `independen` lines | **high in volume, low in risk** — no Method A/B/C framing, but 39 independence claims each need a measured basis |

The item-5 lines are the largest block and the least constrained. Several
already hedge correctly and are worth reading as models rather than as defects:

- `appendixA.tex:63` — "This is corroboration for the diagnosis, not independent…"
- `appendixB.tex:89` — "already made, not independent evidence."
- `section5.tex:146` — "not an independent confirmation by a different party: the same agent…"
- `section6.tex:183` — "corroboration by a second route, not an independent constraint, and it must not…"
- `section6.tex:225` — "so it is *not* a second independent…"

That the Painlevé paper already distinguishes corroboration from independence
in five separate places, while the LMP paper did not, is the most useful thing
this sweep found.

---

## What this packet does not tell you

- Whether any of the 33 edits **reads well**. Located is not read.
- Whether the Painlevé paper's 157 in-scope lines are **right**. The sweep
  finds lines about the shared subject matter; it does not evaluate them.
- Whether anything in either paper is missing. Every check here reports what
  is present; absence of a hit means the pattern found nothing, which is
  recorded as such, not that nothing is there.
