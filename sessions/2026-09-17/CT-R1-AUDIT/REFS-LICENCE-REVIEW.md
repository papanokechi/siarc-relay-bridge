# Reference-file licence review — before any commit of the session tree

**Ruling (operator review #7):** *"Before committing it, check the reference-PDF
licences, since van der Put–Saito is open access but the others may not be, and
keep `lean/.lake/` excluded."*

> **Correction (review #14).** The premise inside that ruling — that van der
> Put–Saito is open access, in the sense of carrying redistribution permission —
> is **not supported by the article itself**. Its title page reads *"© Association
> des Annales de l'institut Fourier, 2009, tous droits réservés."* The ruling is
> quoted above unchanged, as issued; the assessment below has been corrected. The
> article is free to **read**; that is a different question from the one this
> file exists to answer.

> ## STANDING HOLD (operator review #15)
>
> **Everything under any `refs/` directory stays local and uncommitted until its
> own row below is individually checked.** No file is cleared by the status of
> its publisher, its venue, or its neighbours in this table. "Open access" is a
> statement about **access** and answers a different question from the one this
> file asks.
>
> **arXiv is explicitly not a blanket clearance.** arXiv licences are chosen
> **per submission**. The default — the *arXiv.org perpetual, non-exclusive
> license* — grants arXiv the right to distribute and grants a third party **no
> redistribution right at all**. Each arXiv PDF needs the licence stamp on its
> own abstract page read before its row can move.
>
> This hold is the reason the commit decision on the session tree is not blocked:
> the manifest route commits the tree **without** `refs/`.

This is a **redistribution** question, and it only arises on commit. Fetching and
reading these files for research is not at issue.

## Inventory — `CT-R1-AUDIT/refs/`

| File | sha256 (16) | Provenance | Redistribution assessment |
|---|---|---|---|
| `vanderPut-Saito-AIF-2009-59-7-2611.pdf` | `1666bd6b…` | *Ann. Inst. Fourier* **59** (2009) 2611–2667 | **DO NOT COMMIT pending a licence check.** *Corrected at review #14.* This row previously read "Likely safe… AIF is open access". The article's own title page, read from a page image (`CT-S16-MEMBERSHIP-C/pages/vdps_titlepage_vol_LOOK.png`), carries: *"© Association des Annales de l'institut Fourier, 2009, **tous droits réservés**."* Free-to-read is **not** permission to redistribute, and the two were conflated here. The specific licence remains **NOT CHECKED**. |
| `CT-S18-COLDREAD-C3/packet/pages/vdPS_p*.png` (5 files) | rendered | 4× renders of five **full pages** of the above | **DO NOT COMMIT.** Same rights position as the source, and these are whole pages rather than quoted regions. Retained locally for the cold read only. |
| `CT-S16-MEMBERSHIP-C/refs/vdPS-arXiv-0902.1702v5.pdf` | `1d4be8e4…` | arXiv:0902.1702v5 | **Check the arXiv licence stamp** on the abstract page. arXiv's default licence permits distribution by arXiv but not necessarily third-party redistribution. **NOT CHECKED.** |
| `vquad_resurgence_v1.0/v1.1/v1.2*.pdf` | `c07c97d6…` `e07c1dda…` `a5d9e264…` | Zenodo, the operator's **own** deposits | **Safe if the deposit licence permits.** Check the licence field recorded at deposit time; if CC BY, redistribution is fine. As the author, the operator controls this in any case. |
| `gautschi_p34_bot.png` | `e6728427…` | A 3× render of **one page region** of Gautschi, *SIAM Review* **9**(1) 1967 | **DO NOT COMMIT.** SIAM holds copyright; this is a page image, not a citation. Quoting hypothesis (2.8) in prose is fair use for scholarship; committing the image is redistribution of a copyrighted page. |
| `coldpackets/companion_v12_p*.png` | rendered | page images of the operator's own v1.2 | follows the v1.2 licence |
| `coldpackets/vdps_p2634.png`, `vdps_p2635.png` | rendered | page images of the AIF article | follows the AIF licence; if it is CC BY-**ND**, a cropped or re-rendered page may count as a derivative — prefer shipping the original PDF and rendering locally |
| `dlmf_5.11.html`, `dlmf_bib_W.html` | `929045c7…` `2a90b9f0…` | NIST DLMF | **Check.** DLMF content is US-government-adjacent but carries its own terms, which restrict wholesale redistribution of substantial portions. Cite by URL **and release version** rather than committing the HTML. |

## Recommendation

**Do not commit `refs/` wholesale.** The safest arrangement, and the one that
keeps the record reproducible:

1. Commit a **manifest** — filename, source URL or DOI, sha256, retrieval date,
   licence — which is what the P0 rule needs for verification anyway. A hash
   proves you read the same bytes; the bytes themselves need not be in the repo.
2. Exclude from the commit: `gautschi_p34_bot.png`, the DLMF HTML captures, and
   the rendered AIF page images.
3. Keep the actual files in the **off-repo backup**, which already holds them.
4. Keep `lean/.lake/` excluded — already handled by
   `CT-S1-THEOREM/lean/.gitignore`, which sits inside the session tree.

Three items are then unambiguous: the operator's own Zenodo deposits, the
manifest, and everything the sessions themselves produced.

## Status of the two licences to confirm

Neither has been verified, and **neither was guessed**:

* **AIF / Centre Mersenne** — free **access** is established; **redistribution
  permission is not**, and the article's title page reads *"tous droits
  réservés"*. The **specific licence string** for this article is **NOT
  CHECKED**. *(Corrected at review #14; this entry previously said "open access
  is established", which answered the wrong question.)*
* **Zenodo deposits** — the licence field selected at deposit is **NOT CHECKED**;
  it is recorded in the 2026-06-16 deposit metadata and on the Zenodo record.

Both are a few minutes' work on the deposit day and fold naturally into the P0
re-fetch pass, which already re-visits both sources.

## Off-repo backup — done, and refreshed each round

Per the operator's ruling (review #8) the archive is refreshed at the end of
every round, and its hash is stored **outside** the archive — a hash sealed
inside the file it certifies certifies nothing.

| Round | Archive | Size | sha256 | Hash stored at |
|---|---|---|---|---|
| R9 | `sessions-2026-09-17_20260917-202213.zip` | 30.9 MB | `9CE442A4…2DD5202` | *(recorded only here — the defect this ruling fixes)* |
| **R13** | `sessions-2026-09-17_20260917-213821.zip` | 32.6 MB | `ae6c8bc486c2d481ad8a9a6785594fbc44f0450380deea434ed634c2652857c6` | `…_20260917-213821.zip.sha256`, beside the zip |

(Earlier R11 archives `…-210047.zip` and `…-211236.zip` are superseded by the one
above; each retains its own `.sha256` sidecar.)

All archives live in `C:\LocalWork\_siarc-session-backups`, **outside the
repository**, so a `git clean` in the working tree cannot reach them. Both
exclude `lean/.lake/` and `__pycache__`.

The refresh is scripted as `make_backup.py`, which adds files straight into the
zip rather than staging a copy first. That is not a cosmetic change: the tree
contains **236 real files against 124,116 excluded `.lake` paths**, and the
staging approach stalled for over fifteen minutes copying a build directory it
was about to delete.

This addresses the risk you identified: the session tree is one untracked
directory holding the claim corpus, the reference PDFs and every draft, and a
single `git clean -fdx` would have destroyed it. Committing remains your call;
the backup does not depend on that decision.

## Licences — a question for the publisher's terms

Recorded per the operator's ruling: **the scope of redistribution permission for
the non-open-access reference material is a question for the publisher's terms,
not one for an agent to decide.** This session's position is limited to what is
verifiable — that van der Put–Saito is **freely readable** but published under
*"tous droits réservés"*, so that redistributing it is a question for the
publisher's terms exactly as for the others; and that the Gautschi page
image is retained locally, uncommitted, for the operator's own verification. No
judgement is offered on anything beyond that, and no such file is proposed for
commit.
| **R14** | `sessions-2026-09-17_20260917-214234.zip` | 32.6 MB | `5cb5831db43fab19f5302220306643be20746d2db98d2c735a7d7aa88c5c7ea5` | `…_20260917-214234.zip.sha256`, beside the zip |
| **R15** | `sessions-2026-09-17_20260917-231109.zip` | 35.1 MB | `35bc325603cd4a5a7b48199b05e160afe0761e528d7502b65a5cc0b5c7def0fe` | `…_20260917-231109.zip.sha256`, beside the zip |
| **R16 (current)** | `sessions-2026-09-17_20260918-073151.zip` | 36.0 MB | `5206cc48734f67706266939e8adf5d491c60b4160e69ddfe971433be013032a5` | `…_20260918-073151.zip.sha256`, beside the zip |

Note: a table inside the tree necessarily trails the archive it describes by one
entry, since an archive cannot contain its own hash. **The `.sha256` sidecar is
the authoritative record**; this table is a history of earlier archives. The
deposit-day pass regenerates both.

## New reference acquired in R16 — arXiv:0902.1702v5

`sessions/2026-09-17/CT-S16-MEMBERSHIP-C/refs/vdPS-arXiv-0902.1702v5.pdf`
sha256 `1d4be8e4526f6ca834506a976a6ffc999e9659acc2da08753b87e1f59d006e47`

Downloaded from arXiv to check whether the authors' latest corrected version
fixes the `b(z)` entry on p. 2655 of the journal version. It does not; the same
form appears on p. 34 of v5.

Treatment follows the standing manifest rule: **retained locally, uncommitted,
for verification only, and not proposed for commit.** arXiv distribution terms
vary by submission and are a question for the operator and the publisher, not
something to be decided here. Only the two rendered crops actually cited are
kept as page images, on the same footing as the other reference images.
