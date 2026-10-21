# WALKTHROUGH — arXiv submission of the V_quad period-representation paper

**Status: the one upload still pending.** Endorsement for `math-ph` is granted.
Every value below was re-verified on 2026-09-21 against the files on disk and a
live snapshot of Zenodo record 20719043 — `outputs/check_upload_ready.out.txt`,
**17 checks, 2 findings, 5 controls all fired**.

The agent does not submit and calls no arXiv API. This is a keyboard
walkthrough for the operator.

---

## 0. GATE — read this before opening the form

**Do not submit until you have ruled on §2.** The abstract inside the file you
would upload and the abstract you would type into the form **do not say the
same thing**, and the difference is about whether a central claim is proved or
conjectured. Everything else is ready.

---

## 1. The file to upload — verified today

Upload exactly one file:

```
sessions/2026-06-16/VQUAD-PAPER-LAYOUTFIX-001/latex/vquad-periodrep-paper.tex
```

| check | result |
|---|---|
| size | 87,778 bytes — matches the June inventory |
| sha256 | `d8906249e8d0eaff681da0f21d6996e6ac824f60550be1d12a21857ae2f6a906` |
| companion PDF re-hashes to the layout-fixed pin | `33f339ed…` ✔ |
| `\input` / `\include` / `\includegraphics` / `\bibliography` / `\bibliographystyle` | **0 / 0 / 0 / 0 / 0** |
| `\begin{thebibliography}` | 1 — bibliography is embedded, so **no `.bbl`, no bibtex** |
| any string from the private pattern file anywhere in the public source | **0** |
| `\author{Papanokechi}` | present |
| venue strings (`Compositio`, `submitted to`) | **0** |
| build log page count | **24** |

**Do not also upload** `preamble.tex` (already inlined as lines 1–74, and it
carries its own `\documentclass` with no `\end{document}` — arXiv could pick the
wrong main file), `build.py`, the `.pdf`, or any `.aux`/`.log`/`.out`.

arXiv compiles **source**, not PDF, and **publishes the source**. The scan
above is what makes that safe.

---

## 2. THE BLOCKING QUESTION — the hedge conflict

The paper's own abstract, inside the `.tex`, reads:

> the rank-one standalone closure **on the Sakai surface** $D_5^{(1)}$
> (Painlevé V)

The arXiv metadata package, hedge-fixed on 2026-09-13, tells you to type:

> the rank-one standalone closure, **whose Sakai surface type is conjectured to
> be** $D_5^{(1)}$ (Painlevé V)

A decidable check (`C2b`) confirms these are **otherwise identical**: delete the
hedge clause from the package text and the two abstracts match exactly. So this
is not a transcription drift — it is one deliberate change of epistemic force,
applied to the metadata and **not** to the manuscript.

The corpus supports the hedge, not the flat claim:

- `CT-S4-FORMAL-TYPE` `S4-01` — the V_quad companion's **v1.2 renamed object
  4.1 from a theorem to "Conjecture 4.1, Painlevé V (D₅⁽¹⁾) classification"**.
- `CT-S4-FORMAL-TYPE` `S4-09` — this programme's own verdict on the attribution
  is **(c) INCONCLUSIVE**.

And the **already-published Zenodo record carries the unhedged wording**, since
it was published 2026-06-16, three months before the hedge fix.

### Your three options

| | action | consequence |
|---|---|---|
| **A** | Amend the `.tex` abstract to the hedged wording, rebuild, upload that; then edit the Zenodo record's description to match. | Source, arXiv abstract and deposit all agree, and all agree with `S4-09`. Costs a rebuild and a metadata edit. **Recommended.** |
| **B** | Upload the source as it stands and type the **unhedged** abstract. | Internally consistent and matches the live deposit, but asserts in a permanent public record something the programme labels INCONCLUSIVE. |
| **C** | Upload the source as it stands and type the **hedged** abstract (what the June runbook literally says). | The arXiv abstract and the arXiv-hosted PDF would disagree in public about whether the result is proved. **Not recommended.** |

If you take **A**, note that the manuscript body may state the attribution
flatly in other places too; the check above covers the abstract only. A body
sweep is the Amendment H rule applied to this edit — sweep first, report the
result whether or not it finds anything.

If you take **B**, say so explicitly in the record, because it overrides the
September hedge fix.

---

## 3. The form, step by step

1. **Log in** to arXiv as **Papanokechi**. The public byline must never read
   anything listed in the private pattern file.
2. **Start submission.** Primary category **`math-ph`** (this is the endorsed
   one). Leave cross-lists for after announcement.
3. **Upload** the single `.tex` from §1. Nothing else.
4. **Check arXiv's compile.** Expect **24 pages**. The arXiv PDF will differ
   from the Zenodo PDF because arXiv stamps a header and ID — **expected, not a
   defect**. Confirm the bibliography renders and there are no undefined
   citations or missing figures. (There are no external figures: the graphics
   are inline TikZ.)
5. **Title** — paste exactly:
   ```
   An explicit exponential-period representation of the $V_{\mathrm{quad}}$ connection coefficient
   ```
   Sentence case. Do **not** use the Title-Case form that appears in some
   ledger prose.
6. **Authors** — `Papanokechi`. Single author. The ORCID is attached at the
   claim step, not typed here.
7. **Abstract** — per your §2 ruling. The text is in
   `refs/arxiv-metadata-package.md`, Field 3, with the preamble macros already
   expanded to standard TeX (`\Vquad`→`V_{\mathrm{quad}}`, `\Bhat`→`\widehat{B}`,
   `\Qsqrt`→`\mathbb{Q}(\sqrt3)`, `\Qbar`→`\overline{\mathbb{Q}}`,
   `\SL`→`\mathrm{SL}`, `\K`→`K`). arXiv does not load your preamble, so an
   unexpanded macro would render as literal text.
   **Omit** the three Zenodo deposit-context sentences — they describe the
   deposit, not the paper.
8. **License — actively select `CC BY 4.0`.** ⚠ arXiv's default is its own
   non-exclusive distribution licence, **not** CC BY. The deposit is CC BY 4.0;
   selecting it keeps them consistent. This is the single easiest field to get
   wrong, because getting it wrong requires doing nothing.
9. **Comments** — `24 pages`. Optionally append
   `Zenodo: https://doi.org/10.5281/zenodo.20719042` — that is the **concept**
   DOI (all versions), not the version DOI. **No venue string**, ever.
10. **MSC class** (optional) — `34M55, 11J81, 34E20, 14F40, 33C20, 37K10`
    (primary `34M55`). The manuscript itself carries no `\subjclass`; these come
    from the deposit. Consistency argues for including them.
11. **DOI / journal-ref / report-no** — leave blank.
12. **Claim authorship** and attach ORCID `0009-0000-6192-8273`.
13. **Before final submit** — review the preview **and** the submission-history
    metadata. Confirm **only Papanokechi** appears anywhere public. The source
    scan is already clean, so this is a confirmation, not an expected fix. Use
    the unsubmit window if anything needs correcting.
14. **Submit.**

---

## 4. After it announces

- [ ] Capture the **arXiv ID** and the **abs URL**.
- [ ] Attempt cross-lists `math.NT` and `math.CA` — each may need its own
      endorsement.
- [ ] Optionally add the Zenodo DOI via arXiv's journal-ref/DOI facility if you
      did not put it in Comments.
- [ ] Send O. Marchal the concept DOI `10.5281/zenodo.20719042`, and the abs
      link if you want.
- [ ] Record the arXiv ID in the ledger, in the **same session** as the
      submission — the deposit-day rule: an identifier that exists only in your
      browser history is not recorded.
- [ ] If you took option **A** in §2, also update the Zenodo description so the
      deposit and the preprint agree.

## 5. Pre-flight not covered by this walkthrough

Confirm the preprint policy of any venue you may later target does not conflict
with posting a preprint, **before** announcement rather than after. arXiv
announcement is public and permanent; that ordering is the whole point.
