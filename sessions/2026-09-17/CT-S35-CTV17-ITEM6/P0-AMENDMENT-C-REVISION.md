# P0 Amendment C -- revision, 2026-09-20

**Status: proposed in this session, approved by the operator in the same turn,
recorded here because `P0-AMENDMENTS-ABCD.md` lives in `CT-S27-CTV17-DEPOSIT-PREP`
and files from earlier sessions are not edited.** This file is a revision to
Amendment C's symmetry bullet, not a sixth amendment. It names a construct; it
adds no new requirement.

## The occasion

The post-publish readback of Zenodo record 22850681 reported

> VERDICT: the published record is NOT the packet that was checked.

on a record that was character-for-character correct. Ten rendered characters
of difference, all of them whitespace, none of them in the text.

The cause was `plain()` in `scripts/postpublish_readback.py`:

```python
re.sub(r"<[^>]+>", " ", t)
```

This is the **second appearance of the same construct**. Its first was
`S27-19`, where it manufactured 85 phantom space-before-punctuation findings in
a description whose raw HTML contains zero. The symmetry bullet was adopted on
that occasion. It fired correctly here -- the finding was confirmed against the
raw artefact, by a second differently-implemented renderer, before anything was
changed -- but the construct itself went unnamed, and so was still present in a
second script in the same packet.

## The clause

Append to Amendment C's symmetry bullet:

```text
    * NAMED CONSTRUCT. Substituting a SPACE for a stripped tag --
      re.sub(r"<[^>]+>", " ", t) and its equivalents -- manufactures a
      character at every tag boundary. An inline tag between two non-space
      characters produces a space that is not in the text, so the rendered
      string is not the document's text and must never be compared, counted,
      or pattern-matched for whitespace-adjacent features. It has produced a
      phantom defect twice: 85 findings in S27-19, and a false negative
      verdict at the irreversible step in S35-22.
```

## Why a named construct and not a general principle

Amendment C already required, in general terms, that a check verify it read the
file correctly, and that requirement was met: the phantom was caught. What was
not caught is that the *same expression* was still live in a sibling script in
the same folder. A general principle is applied where it is remembered; a named
construct can be searched for. The clause exists to make the defect
**greppable**.

The corresponding repair is stated positively in Amendment C's own terms: where
an artefact is compared against a platform's copy of it, compare only on an
invariant the platform preserves. Whitespace is not such an invariant when the
platform re-serialises markup, and a comparison that is not invariant fails on
a correct record -- which, at an irreversible step, is the most expensive place
a check can be wrong.

## Where else the construct occurs, checked rather than assumed

The first draft of this file asserted that the construct also occurs in
`verify_description.py` "where the manufactured space cannot change the
verdict". **That was invented.** Grepping the folder gives three sites, and the
assertion was wrong about which script and wrong about why:

| site | substitutes | used for | can it manufacture a finding? |
|---|---|---|---|
| `postpublish_readback.py:82` | **space** | the published-vs-local comparison | **yes -- it did**, 10 phantom whitespace differences (S35-22) |
| `make_description.py:612` | **space** | `\bdraft\b` word-boundary scan for draft-stage language | **yes, in principle**: an inline tag inside a word (`re<em>draft</em>ing`) becomes `re draft ing`, creating a word boundary the text does not have, and the scan ends in `assert not stray` |
| `verify_description.py:93` | **empty string** | substring tests | not by this mechanism -- it is the correct form |

So the construct is live in two scripts, not one, and `verify_description.py`
uses the form the clause recommends. `make_description.py` was **not** repaired
in this session: it is a build-time assertion, a phantom there halts the build
rather than publishing anything wrong, and the description it guards is already
deposited. It is recorded as an open item, carried to whichever session next
touches that script.

The construct also occurs in `CT-S27-CTV17-DEPOSIT-PREP`, which is an earlier
session and was not edited.

**The general repair, stated positively.** Where an artefact is compared against
a platform's copy of it, compare only on an invariant the platform preserves.
Whitespace is not such an invariant when the platform re-serialises markup, and
a comparison that is not invariant fails on a correct record -- which, at an
irreversible step, is the most expensive place a check can be wrong.
