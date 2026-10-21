# P0 amendment G — the sibling marker, for a name that has misled — **ADOPTED**

**Status: ADOPTED, 2026-09-21, by operator ruling.**

> **3. Standing rule, narrowly.** When a file's name is misleading about its
> content and the file is cited by digests that can't be restranded, write a
> sibling marker naming the discrepancy and the correct file. Not for every
> file — only where the name itself has caused or could cause a wrong citation.
> Two defects from `jimbo_p1152.png` is the bar.

---

## The amendment

Added to P0 after the `AEAL RECORD` block:

```text
SIBLING MARKERS
- If a stored file's NAME is misleading about its CONTENT, and the file is
  cited by content digest so that renaming it would strand those citations,
  add a marker FILE BESIDE IT naming the discrepancy, the correct file, and
  the rule for citing each. The marker is an ADDITION: it edits nothing and
  disturbs no digest.
- The bar is evidence of harm, not tidiness. Write a marker only where the
  name has already caused a wrong citation, or has been shown capable of
  causing one. Do not mark files merely because their names are imperfect.
- A marker records the discrepancy. It does NOT rename, re-render, or
  relabel anything, and it does not modify the session that stored the file.
```

## Why it is narrow

The rule is deliberately not "document every confusing filename". A marker
beside every imperfectly named artefact is a maintenance burden that decays into
noise, and noise beside a file is worse than nothing beside it: the next reader
learns to skip markers.

The bar is **demonstrated harm**, and the operator set it at two occurrences.
`jimbo_p1152.png` cleared it:

1. **CT-S15** — transcriptions attributed to printed folio 1152 that in fact
   came from 1153.
2. **CT-S46-FORMULA-SECTIONS**, route P — trusting the filename would have
   reported the paper's `eq:jimbo` as **unverifiable against its cited page**.

The second is the more instructive, and is the reason the bar is *harm* rather
than *error*: it is a **false finding against correct prose**, the direction this
run has now hit four times and the direction that costs a round of edits to
material that was already right.

## Why beside the file and not in a report

A note in a report three sessions back is not read by the next person to open
the folder. The marker is placed where the mistake is made — in the directory
listing, next to the name that misleads.

## Why an addition and never an edit

Under the append-only rule the tree's earlier sessions are immutable, and these
images are cited by content hash. Renaming `jimbo_p1152.png` would strand every
citation that resolves it by digest; editing an earlier session's text would
break the digests that cover that text. A sibling file does neither. This is the
same construction as the `supersedes` field for claims: the record grows, and
nothing already cited moves.

## Instance

`sessions/2026-09-17/CT-S21-DEPOSIT-PREP/pages/README.md`, written by
`CT-S47-FORMULA-S5-QP`.

Checked by `CT-S48-RULINGS/scripts/check_rulings.py`, block R3, against
**live-computed** digests rather than recorded ones:

| file | sha256 (live) | printed folio |
|---|---|---|
| `CT-S21-DEPOSIT-PREP/pages/jimbo_p1152.png` | `05fecc96632ca6d4…` | **1153** |
| `CT-S21-DEPOSIT-PREP/pages/jimbo_printed1152.png` | `42fffb7b09ff60b5…` | **1152** |
| `CT-R1-AUDIT/coldpackets/jimbo_p1152.png` | `84f548ceadd8d4a0…` | **1152** |

Six checks, all passing: the two files sharing a name differ; the third is
distinct; the marker names all three by digest; the marker states the rule.
Two controls, both firing: a digest belonging to no image in the tree is not
found in the marker, and the rule stated **backwards** is not matched.

## Label

**INSPECTED** — the amendment records an operator ruling and establishes, by
reading stored files and hashing them, that the instance it cites is what it
says it is. The *ruling* that the pattern is a standing rule is the operator's.
