# Description edit, published record 22831933 (metadata edit, not a new version)

Version DOI `10.5281/zenodo.22831933` · concept DOI `10.5281/zenodo.20455089`.
Applied via **Edit** on the published record, then **Save**. The file set stays
frozen; the DOI does not change.

Paragraph indices below are those of the description as published, read from
`outputs/rights_22831933.json` on 2026-09-18:

| ¶ | opening words | belongs to |
|---|---|---|
| 0 | This notice records five items affecting v1.2… | v1.3 correction notice |
| 1 | Two are corrections. Remark 2.2's claim… | v1.3 correction notice |
| 2 | One item is a clarification that strengthens… | v1.3 correction notice |
| 3 | The remaining two items concern object labelling… | v1.3 correction notice |
| 4 | Quotations from the cited literature were verified… | v1.3 correction notice |
| 5 | We study the resurgence and isomonodromic structure… | **retained v1.2 abstract** |
| 6 | The isomonodromic deformation of the underlying connection… | retained v1.2 abstract |
| 7 | The structure b(x)=a'(x) identified here is a general feature… | retained v1.2 abstract |
| 8 | **Version 1.1 (Stokes-constant numeric correction).** … | version history |
| 9 | **Version 1.2 (classification demoted to conjecture…).** … | version history |

## Edit 1 — label the v1.3 block

The v1.3 block opened cold while ¶8 and ¶9 each carry a bolded label, so a
reader scanning the version history saw two labelled notices and one unlabelled
paragraph. Prefix ¶0, bolded, in the same shape as ¶8/¶9 (`<strong>`, the label,
a full stop, then a space):

```
Version 1.3 (correction notice).
```

so that ¶0 reads:

> **Version 1.3 (correction notice).** This notice records five items affecting
> v1.2 of the companion paper (10.5281/zenodo.20481592).

## Edit 2 — mark the boundary before the retained abstract

New paragraph after ¶4, immediately before "We study the resurgence…":

```
The abstract below is retained unedited as the v1.2 text. Where it states that
the exact-ODE structure forces both finite singularities to be apparent, and
that the apparent singularity positions are the roots of the Wallis
characteristic polynomial, see the first correction above.
```

### Why not "see item 1 above"

The drafted wording pointed at "item 1". ¶0 announces "five items", but the
block that follows is prose with no numbering: ¶1 reads "Two are corrections.
Remark 2.2's claim…", ¶3 "The remaining two items…". No paragraph is labelled 1,
so the pointer resolves to nothing on the rendered page. Replaced with "the
first correction above", which names what it points at rather than an index that
does not exist. Same class as the round's other defects: a reference drifting
from the thing it describes.

### Why two sentences are named, not one

C1 is contradicted in the retained abstract **twice**, and the drafted line named
only the first:

- ¶5: "This exact-ODE structure forces both finite singularities to be apparent
  and explains, via monodromy, the failure of CM-period and hypergeometric
  identification strategies."
- ¶7: "…the Wallis recurrence produces an exact ODE whose apparent singularity
  positions are the roots of the Wallis characteristic polynomial and whose CM
  discriminant is disc(a)."

The second generalises the refuted claim to every PCF and is the last sentence
of the abstract, so it is where an unguided reader is most likely to stop.

## Retaining the abstract is deliberate

It is the text of the paper file in this record, and editing it would make the
description describe something the PDF does not say. The convention followed is
the one already used by Channel Theory v1.6: retain the superseded text unedited
and mark it as retained.
