# DEPOSIT-DAY-PASS.md — walkthrough Part A, run

Run 2026-09-18. **Nothing published, uploaded, committed or sent.** This is
A0 and A1.2 executed. A1.1 needs your inbox; A2–A3 are yours.

---

## A0 — pre-flight

| # | Check | Result |
|---|---|---|
| 1 | `check_invariants.py` | **OK** — all five invariants |
| 2 | `scan_macro_damage.py` | **0 occurrences** |
| 3 | `scan_escape_damage.py` | only the 4 raw PDF extractions under `CT-S9-PVPARAMS/outputs/` |
| 4 | `item4_consistency.py` | pass |
| 5 | `control_item4.py` | all three controls fire |
| 6 | `make_backup.py` | run at end of round |

## A1.2 — the four-row citation pass

All four **RE-FETCHED OK**. Full record: `outputs/depday_citation_pass.json`.

| # | Source | Re-fetch | sha256 |
|---|---|---|---|
| 1 | van der Put & Saito, AIF **59** (2009) | OK, 1 058 380 B | `1666bd6b…` — **unchanged** vs held copy and manifest |
| 2 | Jimbo, *Publ. RIMS* **18** (1982) | OK, 1 623 475 B | `255d4f07…` — **unchanged** vs held copy and manifest |
| 3 | Companion v1.2, Zenodo 20481592 | OK | metadata `666c955e…`; local PDF `a5d9e264…` **matches manifest** |
| 4 | DLMF §32.2 | OK | `dd4a4509…` |

Row 3 detail, read from the API rather than assumed:

| field | value |
|---|---|
| version DOI | `10.5281/zenodo.20481592` |
| **conceptdoi** | `10.5281/zenodo.20455089` — **confirmed, still distinct** |
| version | `1.2` |
| file | `vquad_resurgence.pdf`, 612 719 B, `md5:4d1e4d59…` — size matches the held copy |

Row 4 detail: DLMF **Version 1.2.8, release date 2026-09-15** — unchanged from
what the notice cites.

> Correction made during the run: rows 1 and 2 were first recorded NOT
> RE-FETCHED, on the assumption that paywalling left no route. `REFS-MANIFEST.md`
> records working URLs for both. *Paywalled to redistribute* is not *unreachable
> to fetch*, and the rule asks for a re-fetch, not a licence judgement. Both were
> then re-fetched and are byte-identical to the held copies.

## Page images, read by eye

Every load-bearing passage was read from a rendered image, never the text layer.

| page | what the notice cites it for | verdict |
|---|---|---|
| vdPS **2634** | strong-Riemann–Hilbert restriction (C4 pt 5) | **MATCHES** — "*the strong Hilbert-Riemann problem has a positive answer, except possibly for (1/2, −, 1/2) and (−, −, 5/2)*" |
| vdPS **2635** | Table 2.1, row `D̃₅`/PV (C4) | **MATCHES** — r(0)=0, r(1)=0, r(∞)=1, r(t)=−, dim𝒫=3; also the `M(t)` sentence CT-S15 located |
| vdPS **2637** | the det constraint | **MATCHES** — "*−θ_i²/4 is the determinant of A_i for i = 0, 1 and θ_∞ is the (1,1) entry of A_0 + A_1*", with A_∞ = (t/2)·diag(−1,1) |
| Jimbo **1152** | PV dictionary and (A1)_PV (C2) | **MATCHES** — (3.1) prints the constant matrix as **diag(1,0)**; **(A1)_PV reads "θ₀, θ_t ∉ Z"**, θ_∞ absent; dictionary α = ⅛(θ₀−θ_t+θ_∞)², β = −⅛(θ₀−θ_t−θ_∞)², **γ = 1−θ₀−θ_t**, δ = −½ |

The dictionary is worth noting: **γ = 1 − θ₀ − θ_t**, so at θ₀ = θ_t = 0 it gives
**γ = 1** directly. C2's central claim is legible on the page itself.

### My own error, caught by the eye read

My renderer used printed = index + 2611 for vdPS and index 16 for Jimbo. Both
were **off by one**: the file written as `p2635` showed printed 2634, and the
Jimbo render showed 1153. The automated "is the page number visible?" check had
returned **false** for all four and I nearly passed over it. Corrected to
printed = index + 2610 and index 15; the mislabelled renders were deleted so
they cannot be cited later. The notice's page numbers were right throughout.

---

## THE ONE ITEM — RULED ON, ADOPTED, CLOSED

> **Status, 18 Sep 2026.** Raised below, ruled on by the operator, and adopted.
> The notice's CT-S15 paragraph no longer attributes the two rejected
> transcriptions to OCR; the deposit-day checklist section, which still said the
> pass had not been run, was corrected in the same edit. Notice now at sha256
> `d070fab1…`, then to `c936662f…` when an editorial note-to-self was removed
> from the C3 sentence (§R29). Claims `S21-46`–`S21-50`, audit §R28–§R29.
> **Nothing here still blocks
> publish.** The original finding is kept below unaltered.

**`CT-R1-AUDIT/coldpackets/jimbo_p1152.png` is printed page 1153, not 1152.**
It is byte-identical (`84f548ce…`) to `CT-S9-PVPARAMS/outputs/jimbo_page16-16.png`,
a render of PDF index 16. Printed 1152 is index 15.

The vdPS packet images are correctly labelled — I checked both. This is the
Jimbo file only.

**No adopted claim is wrong.** Every Jimbo quote in the notice matches the true
printed 1152, verified above. But it changes the *explanation* the notice gives
for CT-S15's two rejected transcriptions, and that explanation is in the deposit
object:

- The notice says CT-S15 "reported (A1)_PV as constraining θ_inf as well as
  θ_0 and θ_t". The page it was handed — printed **1153** — carries
  **(A3)_PV: ½(θ_∞ ± σ), ½(θ_t ± θ_0 ±′ σ) ∉ Z**, which *does* constrain θ_∞.
  CT-S15 read the assumption line on the page it was given and labelled it by
  the packet's filename.
- Likewise **(3.1) is on printed 1152**, so CT-S15 never had it; its
  `(1/2)σ₃` reading cannot have come from reading that equation.

So the notice attributes to **OCR** what was substantially a **packet-labelling
error on our side**. That is unfair to the cold reader and inaccurate in a
document whose whole subject is other people's errors.

I have **not** edited the notice: changing how a cold read is characterised is a
substantive wording call and yours. Proposed replacement for the CT-S15
paragraph's second half, for you to accept or redraft:

> Two of its transcriptions were rejected after the pages were re-read directly.
> Both are now understood to follow from a packet defect rather than from OCR:
> the image supplied to it as Jimbo p. 1152 is in fact printed p. 1153. That
> page carries (A3)_PV, which does constrain θ_∞, and does not carry (3.1) at
> all. The readings this notice relies on were verified by direct reading of the
> true p. 1152, where (3.1) prints the constant matrix as diag(1,0) and (A1)_PV
> reads θ_0, θ_t ∉ Z.

Separately, the packet file should be renamed or re-rendered so the name matches
the page, and any other packet image should be checked the same way. I checked
the vdPS pair; the six `companion_v12_p*.png` images use the documented
printed = N + 1 convention and were not re-verified in this pass.

---

## Status against the walkthrough's abort conditions

| # | Condition | State |
|---|---|---|
| 1 | Author reply arrived | **UNKNOWN — needs your inbox.** If a reply has come, stop |
| 2 | Citation row fails, or a page no longer reads as quoted | **clear** — all four re-fetched, all four pages match |
| 3 | v1.2 no longer the version cited / hash changed | **clear** — `a5d9e264…`, version 1.2 |
| 4 | `control_item4.py` controls do not fire | **clear** — all three fire |
| 5 | Form metadata disagrees with the notice | not reached — A3 is yours |

**Verdict: the citation pass is clean, the one wording item is closed, and A1.1
is satisfied — no reply from either author, so C3 stands as written.**

**THE FILE TO UPLOAD is `upload/vquad_resurgence_v1.3_correction_notice.md` at
sha256
`c936662f61be8625d69b7f8efce8a8684b33569c6a033e88f510a3050b89948c`, 35 918
bytes** — a byte-identical copy of the notice under a publishable name, since
Zenodo publishes the filename you give it and the working file is named
`DRAFT-…` (§R31). Upload it **beside** the carried-over `vquad_resurgence.pdf`,
which must not be deleted (§R31). The notice changed three times on deposit day — the CT-S15 paragraph,
the checklist section, then the editorial marker — so verify the hash of the
file you are actually uploading rather than any hash quoted earlier in this
document or in the audit. Earlier hashes in the record are historical and
correct as of the claims that carry them; they are not upload instructions.
