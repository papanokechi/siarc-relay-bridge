# WALKTHROUGH — depositing Channel Theory v1.7 (description-only new version)

**Nothing in this file has been executed.** It is the procedure, written so the
irreversible steps are visible before you reach them. No token has been used, no
draft created, no file uploaded, no metadata edited.

Read §0 and §1 before opening a browser. The stop points are numbered **S1–S6**
and each one is a place where the next click cannot be undone.

---

## 0. What is being deposited, in one paragraph

A **new version** of the Channel Theory record. The v1.6 PDF is carried over
**unchanged** by the platform; **no file is uploaded**; the v1.7 version notice
becomes the new record's **description**. The version field goes `1.6 → 1.7`.
Zenodo mints a new version DOI; the concept DOI `10.5281/zenodo.19941678` is
unchanged and must not be edited.

| | |
|---|---|
| record to start from | `10.5281/zenodo.22782807` (v1.6) |
| concept DOI (unchanged) | `10.5281/zenodo.19941678` |
| description to paste | `DESCRIPTION-v1.7-rev3.html` — 68 303 chars, sha256 `33a38933…` |
| file to upload | **none** |
| file carried over | `channel_theory_outline.pdf`, 609 300 B, md5 `aa56a94a…` |
| everything else | unchanged from v1.6 |

Pre-flight state: `preflight_deposit_rev2.py` **GATE: PASSED**, 11/11 checks, 0
broken, 3/3 reader controls; `verify_description.py` **VERDICT: OK**, 21/21, 0
broken, 3/3 reader controls.

> **Correction, 2026-09-19.** This line read `13/13`, which was the check count
> before the sixth item's checks (N5b, N6, N7, N8, P1, P2 and the tier markers)
> were added. It is now 21. A stale count here is not cosmetic: it is the number
> you would compare the gate's output against, so it would have made a gate
> running *fewer* checks than expected look correct.

---


## Hash supersession (read before pasting)

The description this walkthrough refers to is `DESCRIPTION-v1.7-rev3.html`:

| value | |
|---|---|
| chars | 68 303 |
| bytes | 68 606 |
| sha256 | `33a3893372dfd9dcd2c89c4202b8db5aa6d8914acf4707bfd93e7442f8c7e293` |
| md5 | `cdfa63630469ee75834acd725a64415b` |

The md5 is of the **description file's bytes**. Zenodo publishes md5 for
*files*, not for the description field, so this value is for your own
paste-time comparison and will not appear anywhere in the record.

**Every description hash quoted earlier is superseded, including earlier
quotations inside this packet.** Specifically `026e7a9e...` (rev2, before the
sixth item) and `39903126...` (rev2, first draft of the sixth item) are
history. Verify what you actually paste against `33a38933...` and against
nothing else.

## 1. One deliberate departure from Zenodo's own guidance

Zenodo's documentation says:

> Versioning is used when you have updated the **files** of your published
> record. If you just need to edit metadata (title, creators, description etc)
> then see Edit published records.

By that default, a description-only change is an **Edit**, not a new version.
**We are not doing that, deliberately.** An Edit *overwrites* v1.6's
description — and v1.6's description is the deposited erratum text this corpus
has just declared authoritative. Editing it in place would destroy the primary
source in order to publish a note about it.

The record has already ruled this class, in its own words. The v1.6 description
says of its defect (1):

> This is the same defect class as 10.5281/zenodo.22739009 (wrong build
> attached), and is therefore **repaired by a new version rather than by a
> metadata edit**.

So: **new version**. Every prior Channel Theory version carries its own erratum
in its own description, and v1.7 does the same. The cost is one DOI. The cost of
the alternative is a destroyed source.

> **Do not click "Edit" on the v1.6 record at any point in this procedure.** If
> you find yourself editing a record whose version field already reads `1.6`,
> you are in the wrong place — leave without saving.

---

## 2. Before the browser

Run the two gates and read their last lines. **If either is not clean, stop.**

```powershell
cd C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17\CT-S35-CTV17-ITEM6
$env:PYTHONIOENCODING='utf-8'
python scripts\verify_description.py     | Select-Object -Last 8
python scripts\preflight_deposit_rev2.py | Select-Object -Last 16
```

Expect `VERDICT: OK` with **21 checks, 0 failed, 0 broken, 3/3 reader
controls**, then `GATE: PASSED` with **11 checks, 0 failed, 0 broken, 3/3
reader controls**. Read the counts, not only the verdict word: a gate that
runs fewer checks than it should still prints a clean verdict.

> **Correction, 2026-09-19.** The second line read `-Last 12`, which displays
> `GATE: PASSED` but cuts off `checks run : 11` and `checks failed : 0` — the
> counts the line above tells you to read. Found by running this block, not by
> reading it.

> **Path correction, 2026-09-19.** This block previously read
> `CT-S27-CTV17-DEPOSIT-PREP`. That is the session the packet was *built* in;
> the sixth item was added in `CT-S35-CTV17-ITEM6`, and the file you are about
> to paste lives there. Run as written before this correction, the gates would
> have certified the **rev2** description while you pasted **rev3** — a green
> gate on a different artefact, which is worse than no gate, because it is
> believed. Both `scripts/` and `DESCRIPTION-v1.7-rev3.html` referred to below
> are the `CT-S35-CTV17-ITEM6` copies.

Do **not** take a hash here to compare by eye later. That is the form this
record has twice lost a round to: a number quoted at one moment and compared at
another verifies *the quotation*, not the file.

The hash comparison happens in **Step 4, stop point S2a**, immediately before
you paste, and it resolves the expected value from the passing gate run's own
output rather than from any constant written here. Run it there, not now.

What still applies now: **do not edit the description again after the gates
have passed.** If you do, re-run both gates — S2a will refuse the paste
otherwise, which is the intended behaviour, not a malfunction.

---

## 3. The procedure

### Step 1 — open the v1.6 record

Go to the landing page of `10.5281/zenodo.22782807`. Confirm the page shows
**Version 1.6**. If it shows anything else, you are on the wrong record or a
newer version already exists — **stop and re-read the record before continuing**
(the working tree has been behind this record before).

### Step 2 — click **New version**

The green **New version** button is on the record landing page, right-hand side.
It appears only if you are logged in as the owner.

The form opens showing **New version draft**. All metadata is copied from v1.6.

> **S1 — creating the draft is safe and reversible.** A draft can be deleted.
> Everything up to Step 8 is reversible. Nothing before Step 8 publishes.

### Step 3 — import the carried-over file

**The new draft starts with NO files.** This is the step most easily missed, and
missing it publishes a record with nothing attached.

In the **Files** section, click **Import files**. This imports the previous
version's files by reference — it does not duplicate storage.

> **S2 — confirm, by eye, before going on:**
> - exactly **one** file is listed;
> - its name is `channel_theory_outline.pdf` — not a `DRAFT-` name, not a name
>   containing a record number, not one with a browser-added `(1)`;
> - its size is **609 300 bytes** (may display as ~609.3 kB / 595 KiB);
> - **do not upload anything.** Uploading is how the wrong file gets published,
>   and this session holds no PDF bytes to upload. `upload/` is empty on purpose.

### Step 4 — replace the description

> **S2a — verify the bytes you are about to paste, against the file itself.**
> Before opening it, confirm the file has not changed since the gate passed.
> Run this from `CT-S35-CTV17-ITEM6`; it compares the file **as it is now**
> against the hash the **passing gate run** recorded, and prints one word:
>
> ```powershell
> $now  = (Get-FileHash .\DESCRIPTION-v1.7-rev3.html -Algorithm SHA256).Hash.ToLower()
> $gate = ((Select-String .\outputs\preflight_deposit_rev2_s35.out.txt `
>            -Pattern '^sha256\s*:\s*([0-9a-f]{64})').Matches[0].Groups[1].Value)
> if ($now -eq $gate) { "MATCH  $now" } else { "STOP - DIFFERS`n now  $now`n gate $gate" }
> ```
>
> This is deliberately **not** a comparison against a number you read by eye.
> Comparing a file to a hash quoted in a chat message, in `DEPOSIT-FORM.md`, or
> in an earlier revision of this file verifies *the quotation*, not the file: a
> hash quoted since the artefact was finalised may predate the last edit. That
> is exactly how this record has lost a round, twice. The value above is
> produced by the gate that actually passed, so a match means *the bytes that
> were verified are the bytes you are pasting.*
>
> If it prints anything but `MATCH`, **stop**: regenerate and re-run both gates.

Open `DESCRIPTION-v1.7-rev3.html`. Select all, copy, and replace the **entire**
contents of the description field.

**Two routes, and they differ in what you can verify.**

**Route A — the browser editor (matches how previous versions were deposited).**
The description field is a rich-text editor, not a raw HTML box. Pasting HTML
will be **re-serialised** by the editor: the stored text will be equivalent but
may not be byte-identical to the file. `<p>`, `<strong>` and `<em>` are all
within what the editor keeps, which is why the description was generated using
only those three tags.

Because the bytes may change, **do not expect the sha256 to match after
publishing.** Verify by *rendered text* instead — that is what
`scripts/postpublish_readback.py` compares.

**Route B — the REST API (exact bytes, strongest verification).** Set the draft
description directly from the file, so no editor touches it. Requires a personal
token with `deposit:write`. If you take this route, the post-publish readback
can compare exactly, not approximately.

> **S3 — the paste is complete.** Scroll to the **end** of the field and confirm
> the last words are those of §10's final row. A silently truncated paste is the
> single most likely failure here: the description is **68 303 characters**,
> which is **2.9× the largest one this record has carried** (v1.6 was 23 724).
> If the field truncates, this is where you find out — not after publishing.

### Step 5 — the version field

Set **Version** to `1.7`. Confirm it previously read `1.6`.

### Step 6 — change nothing else

Title, creators, affiliation, licence, keywords, related identifiers: **all
unchanged**. The pre-flight has already diffed every one of them against the
v1.6 record.

**Exactly two fields change: the description and the version.** The publication
date is **not** a third — Zenodo sets it on publish, to the day you publish. It
is not a field to fill in, and if you find yourself typing a date you are
changing something this deposit does not change.

> **S4 — the six by-eye checks**, from `DEPOSIT-FORM.md` §4:
> 1. exactly one file, `channel_theory_outline.pdf`, 609 300 bytes;
> 2. the description is complete and not truncated;
> 3. version reads **1.7**;
> 4. affiliation reads **Independent Researcher** — exactly, with that casing
>    (the v1 record drifted on precisely this field);
> 5. keyword count is **27** — the form said 28 until the gate caught it;
> 6. the reserved DOI shown is a **version** DOI. The concept DOI
>    `10.5281/zenodo.19941678` is not an editable field and must not appear
>    anywhere you are typing.

### Step 7 — save the draft and re-read it

Save. Then **reload the page** and read the draft back. Do not proceed from
memory of what you typed.

> **S5 — last reversible point.** Everything so far can be discarded by deleting
> the draft. The next click cannot.

### Step 8 — publish

> **S6 — IRREVERSIBLE. Operator action only.**
> Publishing mints the version DOI and **fixes the filenames permanently**.
> Zenodo states: file addition, removal or modification are not allowed after
> publishing. A wrong filename cannot be corrected later — only superseded by
> another version.

---

## 4. After publishing

Run the readback. It is **read-only and needs no token**:

```powershell
cd C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17\CT-S35-CTV17-ITEM6
$env:PYTHONIOENCODING='utf-8'
python scripts\postpublish_readback.py <new_record_id> *> outputs\postpublish_readback.out.txt
Get-Content outputs\postpublish_readback.out.txt
```

> **Path correction, 2026-09-19.** As in §2, this previously pointed at
> `CT-S27-CTV17-DEPOSIT-PREP`. Run from there, the readback would have compared
> the published record against the **rev2** description — the one without the
> sixth item — and reported a mismatch on prose you deliberately added, or,
> worse, matched a record you did not publish. The readback must be run from
> the session holding the description you actually pasted.

It checks the published record against this packet:

| | |
|---|---|
| version | is `1.7` |
| concept DOI | equals `10.5281/zenodo.19941678`, read from `conceptdoi` — **never** derived from the record number |
| version DOI | differs from the concept DOI |
| files | exactly one, key `channel_theory_outline.pdf`, md5 `aa56a94a…`, 609 300 bytes |
| description | rendered text matches `DESCRIPTION-v1.7-rev3.html`, and is **not truncated** |
| metadata | title, creators, affiliation, licence and the 27 keywords all still match v1.6 |
| build statement | the published description still says the attached file is the v1.6 build, unchanged |

Then, and only then:

1. store the published record JSON and description under `refs/` with bytes and
   sha256 — **the deposited text is authoritative from that moment**, and this
   repository's copy becomes the stale one;
2. record the new version DOI where the corpus refers to it;
3. do **not** re-run any checker over a path an existing claim already cites.

---

## 5. If something goes wrong

| symptom | what it means | do |
|---|---|---|
| **Import files** shows nothing | you are on a plain new upload, not a new version of this record | discard; start again from the v1.6 landing page |
| description truncated on save | the field has a limit below 68 303 chars | **stop.** Do not publish a truncated notice. Report the limit; the notice would then need splitting or attaching as a file, which is a new decision |
| editor mangles the markup | the rich-text editor rejected a tag | check which; the file uses only `p`/`strong`/`em`. Do not hand-fix in the browser — fix the generator and re-run both gates |
| the form offers no **Version** field | you clicked **Edit**, not **New version** | leave without saving; see §1 |
| already published with a defect | filenames and files are frozen | **do not edit.** A new version is the only repair, which is what v1.6 itself did |

---

## 6. What this walkthrough does not do

- It does not publish anything, and it authorises nothing.
- It does not obtain the v1.5/v1.6 PDFs — still HTTP 504, still unheld. If they
  become available and an updated build is wanted, **that is v1.8**, not this.
- It does not settle anything about §10's source table, because that was
  settled: the repository-internal `refs/` paths, session ids and script names
  were **removed**, and the bibliographic half — author, title, venue, DOI or
  URL, retrieval date, sha256 — was kept. The rule applied was *committed and
  public versus uncommitted*, taken from the deposited v1.6 text rather than
  invented here. `DESCRIPTION-v1.7-rev3.html` now contains **zero** occurrences
  of `refs/`, `outputs/` or a `CT-S…` session id, and both gates enforce the
  exclusion **in both directions** — P1 that nothing internal remains, P2 that
  no citation was stranded naming no source. Deleting the citations would
  satisfy P1 alone, which is why P2 exists.
