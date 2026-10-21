# STATE — what has been uploaded, what has not

Established 2026-09-21 by `scripts/check_upload_ready.py` against a stored
snapshot of the live Zenodo API (`outputs/zenodo_20719043.json`) and the files
on disk. **Nothing in this session uploads, edits or publishes anything.**

## 1. Zenodo — DONE, not pending

| | |
|---|---|
| record | `20719043` |
| title | An explicit exponential-period representation of the V_quad connection coefficient |
| state | `done`, `submitted: true` |
| published | **2026-06-16** |
| version DOI | `10.5281/zenodo.20719043` |
| **concept DOI** | **`10.5281/zenodo.20719042`** |
| license | `cc-by-4.0` |
| files | `vquad-periodrep-paper.pdf`, `vquad-periodrep-bundle.zip` (2) |
| related identifiers | 11 |
| creator ORCID | `0009-0000-6192-8273` |

Every value the June deposit prepared is present on the live record: two files,
eleven related identifiers, CC BY 4.0, the ORCID. **The deposit was executed and
is public.**

> **The record is stale, not the deposit.**
> `sessions/2026-06-16/VQUAD-ZENODO-DEPOSIT-001/handoff.md` still reads
> *"HELD at Gate 0 … upload-ready … the manual upload may now proceed"*, and
> `operator-runbook.md` still presents Publish as an action to take. Those
> documents were written **before** the publish and were never updated after
> it. Following them today would attempt an already-completed irreversible
> action.
>
> Under the append-only rule the June session is **not edited**. This file is
> the correction; claim `S51-02` records it.

Note the concept/version distinction, which the June files get right and which
is easy to get wrong: the concept DOI is `…20719042`, **not** the record number
`…20719043`. Cite the concept DOI when you want "all versions".

## 2. arXiv — NOT DONE, and it is the one live upload

No arXiv identifier exists anywhere in the repository. The submission was
prepared and verified on 2026-06-18 and left for the operator's web hand-action.
It has not been performed.

- Endorsement: `math-ph` **granted** (Marchal). Cross-lists `math.NT` /
  `math.CA` may each need separate endorsement and are a post-announcement
  step, not part of the first submit.
- Source to upload: verified today, unchanged, self-contained — see
  `WALKTHROUGH-ARXIV.md` §1.
- **One blocking question stands before submission** — §2 of the walkthrough,
  and `S51-04` below. Do not submit before ruling on it.

## 3. The Painlevé V paper (`CT-S50-READ-REPAIRS`) — out of scope

The 39-page paper is complete and verified, but its venue has deliberately not
been decided, and the operator has called that a separate conversation. No
upload walkthrough is written for it here. When that conversation happens,
`WALKTHROUGH-ZENODO.md` is the reusable procedure; it was distilled from the
V_quad deposit, which is the one deposit in this programme known to have
succeeded end to end.
