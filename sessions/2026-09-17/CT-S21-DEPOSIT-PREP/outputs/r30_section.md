
---

## R30 — the form sheet, and the word DRAFT still in the title

Operator asked for a walkthrough of the Zenodo form. Wrote
`CT-S21-DEPOSIT-PREP/DEPOSIT-FORM.md`, field by field, every *keep* value read
from the live v1.2 record this round rather than from memory, and then diffed
the sheet back against that record: affiliation, ORCID, name, licence, all nine
keywords, the companion title and the existing related-identifier row all verify
verbatim.

Writing it surfaced the last blocker. **The notice's H1 still reads
`# DRAFT — V_quad companion paper v1.3 correction notice`, and the
`**STATUS: DRAFT FOR THE OPERATOR. Nothing has been deposited...**` block is
still under it.** Both would have published. The status block is worse than
merely stale: deposited, it would assert that nothing has been deposited.

Same class as §R28's checklist header and §R29's `*[Deposit-day: …]*` marker,
and the fifth instance in two rounds — scaffolding addressed to the author,
inside the object, true when written and false at deposit. It survived three
end-to-end passes over the same file because it is at the very top, where a
reader checking mathematics does not look, and because the filename itself
begins `DRAFT-`, which makes the word unremarkable in context.

Not applied. The H1 depends on a title choice that is the operator's, and every
wording change in this object has been ruled on first. `scripts/apply_title.py`
takes `A` or `B`, refuses without one, strips the status block, asserts no
`DRAFT` survives, reads back its own bytes and prints the new sha256. Verified
inert: run with no argument it exits 1 and the notice still hashes
`a9a938f7…`.

Two further findings recorded in the sheet rather than here, because they are
decisions rather than defects. **A rendered PDF has its own hash**, so
`a9a938f7…` stops being the number to verify the moment the format changes —
the stale-hash defect one file-format wide. And because A3 makes this a *new
version* while A2 deposits *the notice only*, the concept DOI will resolve to a
record whose sole file is a correction notice rather than the paper; defensible,
irreversible, and worth choosing deliberately rather than by default.
