
---

## R27 — the deposit-day pass, and a packet that was labelled by index

Part A of the walkthrough, run. Nothing published, uploaded, committed or sent.

**The pass is clean.** All four citation rows re-fetched: van der Put-Saito and
Jimbo byte-identical to the held copies and to the manifest; Zenodo 20481592
still version 1.2, conceptdoi 10.5281/zenodo.20455089 read from the API and
still distinct from the version DOI; DLMF section 32.2 at Version 1.2.8,
2026-09-15, unchanged from what the notice cites. All four load-bearing pages
re-read from images and all four match. A0 passes with all three of
`control_item4.py`'s controls firing. Claims `S21-38`..`S21-44`.

Two things worth keeping.

**My renderer was off by one, and the automated check could not tell me.** It
used printed = index + 2611 for van der Put-Saito, and index 16 for Jimbo; the
true offsets are +2610 and index 15. So the file written as `p2635` showed
printed 2634. The scripted check for "is the expected page number present in the
text layer?" returned **false for all four pages** — the running heads did not
survive extraction — and a uniform false across every case reads as a property
of the tool rather than a finding about any page. That is the seventh
amendment's shape again: a check that returns the same answer whatever the truth
is has not been run. What caught it was reading the images.

**The stored cold packet has the same defect, and it is older.**
`coldpackets/jimbo_p1152.png` is byte-identical to a render of PDF index 16 and
shows printed **1153**. CT-S9 named its renders by index; the packet inherited
the name and the name became the claim. The van der Put-Saito packet images were
checked against this and are correctly labelled, so this is the Jimbo file only.

The consequence is not a wrong claim but a wrong explanation. Every Jimbo quote
in the notice matches the true printed 1152, verified this round: (3.1) prints
the constant matrix as `diag(1,0)`, (A1)_PV reads `theta_0, theta_t not in Z`,
and the dictionary's `gamma = 1 - theta_0 - theta_t` gives C2 its `gamma = 1`
directly. But the notice's methodology note attributes CT-S15's two rejected
transcriptions to OCR, and they follow substantially from the packet instead:
printed 1153 carries **(A3)_PV**, which *does* constrain `theta_inf`, and does
not carry (3.1) at all. CT-S15 read the assumption line on the page it was
handed and labelled it by the filename it was given.

Left unedited. Re-characterising a cold read inside the deposit object is a
substantive wording change and the operator's call; a replacement paragraph is
proposed in `CT-S21-DEPOSIT-PREP/DEPOSIT-DAY-PASS.md`.

Two smaller notes. Rows 1 and 2 were first recorded NOT RE-FETCHED on the
assumption that a paywall left no route — but the manifest records working URLs,
and *paywalled to redistribute* is not *unreachable to fetch*; corrected in the
same round. And P0 gains the two detector-hygiene lines: a detector's coverage
list is itself an unchecked assumption, and a guard added to suppress false
positives can suppress exactly the hits that matter.
