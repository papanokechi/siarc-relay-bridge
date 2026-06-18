# arXiv consistency gate — VQUAD-ARXIV-METADATA-001 · Stage 3

Slot: `sessions/2026-06-18/VQUAD-ARXIV-METADATA-001/`
HALT GATE: any wrong-venue leak, identity inconsistency (esp. Kubota residue in
source/acknowledgements), or title/abstract mismatch ⇒ FLAG before submission.
Scanned 2026-06-18 against the layout-fixed source + live Zenodo 20719043.

---

## 3.1 — Wrong-venue check → **PASS**

Venue strings (`Compositio`, `AAECC`, `Acta`, `ETNA`, `Ann. of …`, `Inventiones`) absent from the
title, abstract, and comments as prepared.

| Scanned | Venue hits |
|---|---|
| `vquad-periodrep-paper.tex` (title, abstract, body, bib) | **0** ✅ |
| `preamble.tex` (title/abstract block) | **0** ✅ |
| Prepared metadata field VALUES (Title / Abstract / Comments) | **0** ✅ |

Comments field = `24 pages` (+ optional Zenodo DOI) — no venue. Journal-ref left blank. ✔
PDF-level wrong-venue was already PASS at deposit (pypdf scan, 63635 chars: Compositio/AAECC/ETNA
absent; "Symbolic Comput." present = legitimate Kovacic/CAS citation, not a venue leak).

> Note: `arxiv-metadata-package.md` and this gate file each contain the literal words "Compositio"
> and "Kubota" inside **guard prose** ("must NOT leak Compositio", "No Kubota anywhere"). Those are
> documentation of the checks, **not** field values. The transcribed arXiv field values carry none.

---

## 3.2 — Identity consistency → **PASS**

| Check | Result |
|---|---|
| `\author` | `Papanokechi` (**TEX** L53) ✅ |
| ORCID | `0009-0000-6192-8273` (**TEX** L54 `\thanks`; **ZEN** creators[0].orcid) ✅ |
| "Kubota" in `.tex` | **0** ✅ |
| "Kubota" in `preamble.tex` | **0** ✅ |
| "shkub" / `\email{` / `\address{` in source | **0** ✅ (no machine-username or contact residue) |
| Acknowledgements (**TEX** L1184–1186) | "We thank O.~Marchal …" — no Kubota, no venue ✅ |
| `Papanokechi` occurrences in `.tex` | 7 (1 `\author` + 6 self-citation bibitems) ✅ consistent |

The old arXiv account name (Kubota) appears **nowhere** in the source, preamble, thanks, or
acknowledgements. Author identity is Papanokechi-only, ORCID-tagged.

---

## 3.3 — Title / abstract match (arXiv ↔ Zenodo 20719043) → **PASS**

**Title** — identical:
- arXiv (TEX `\title`): `An explicit exponential-period representation of the $V_{\mathrm{quad}}$ connection coefficient`
- Zenodo: `An explicit exponential-period representation of the V_quad connection coefficient`
- ⇒ MATCH (`$V_{\mathrm{quad}}$` ↔ "V_quad" is TeX-vs-plaintext rendering of the same token).

**Abstract** — same statement, modulo encoding + deposit addendum:
- arXiv abstract = clean TEX `\begin{abstract}` (L59–72), custom macros expanded to standard TeX.
- Zenodo `description` = the **same** scientific abstract, entity-encoded (Trap 3: `&mdash;`,
  `&sup1;`, `&Gamma;`, `&radic;`, …), **plus** 3 trailing deposit-context sentences (reproducibility
  bundle / SIARC governance / continuation of concept …20455089).
- ⇒ MATCH on the paper's abstract. The Zenodo-only trailing sentences describe the **deposit** and
  are intentionally **excluded** from the arXiv abstract (they are not part of the manuscript).

---

## 3.4 — Gate verdict

| Gate | Verdict |
|---|---|
| 3.1 wrong-venue absent | **PASS** |
| 3.2 identity Papanokechi-only / ORCID / no Kubota | **PASS** |
| 3.3 title + abstract match Zenodo | **PASS** |

### **CONSISTENCY GATE: PASS — no FLAG. arXiv metadata is ready to transcribe.**

Residual operator guard (belt-and-suspenders, in runbook): before public announcement, re-check the
arXiv preview + submission-history metadata shows **only Papanokechi** (no Kubota anywhere public),
using the unsubmit window if needed. The source is made public by arXiv (v1.5), and the source scan
above is clean — this is a confirmation step, not an expected fix.
