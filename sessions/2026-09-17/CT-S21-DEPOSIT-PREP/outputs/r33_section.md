## R33 - The upload walkthrough, and a checker that can fail

The operator asked for a screen-by-screen upload guide. Three documents now
describe one deposit, which is one more than is comfortable, so
`UPLOAD-SCREENS.md` quotes **no field value at all**: values stay in
`DEPOSIT-FORM.md`, mechanics in walkthrough A3, abort conditions in A4,
recording in A5. This is the same decision as declining a second recording slot
for the version DOI. Every duplicate this round has drifted - the hash, the
status line, the title - and a fourth copy of the title would have been a
fourth chance to drift (S21-63).

Two scripts were added because the guide referred to them, and referring to a
script that does not exist is inventing a path.

`verify_upload_file.py` prints the **md5** as well as the sha256, because md5
is what Zenodo displays beside an uploaded file. A sha256 the operator cannot
compare in the dialog is not a verification, it is a reassurance (S21-60).

`postpublish_readback.py` is the more interesting one. A checker written after
the event can always be made to agree with the event, so its expected values
were fixed before publication and it was control-tested against the **v1.1**
record, where it returned 5 of 10 and failed exactly the five checks that
depend on v1.3 having happened. It discriminates. That is the property the
uniformly-failing test of S17-22 lacked in the other direction, and it is
cheapest to establish before the thing being checked exists (S21-61).

The control also paid for itself substantively. v1.1 carries **the same single
`references` row** as v1.2, so that row is inherited and the work has never
hand-linked a predecessor version. The add-nothing ruling of R32 now rests on
two versions rather than one. v1.1's PDF md5 differs from v1.2's, so the
carry-over is a real file that changed, not a fixed artefact (S21-62).

Abort condition 3 was re-checked live today and is clear: record 20481592 is
still version 1.2, parent 20455089, PDF md5 unchanged.

### R33.1 - The backtick is PowerShell's escape character (S21-64)

Writing this very section produced the defect it describes. The block was first
written through `python -c "..."` inside a **double-quoted PowerShell string**,
where the backtick is the escape character. The markdown code span for
`verify_upload_file.py` therefore entered the file as a vertical tab, 0x0b,
followed by `erify_upload_file.py`. The backtick before `references` survived,
because the letter after it is not one PowerShell recognises.

This is the eighth amendment's class - a tool retyping what it should derive -
at one more level down, and it has a property the earlier instances did not:
**it is selective**. Only backticks followed by a, b, e, f, n, r, t, v or 0 are
consumed, so a document can pass an eye-read and a line count while carrying
one mangled identifier, and the surviving backticks are evidence that nothing
is wrong. In a document full of code spans, that is most of them.

It was caught only because `append_block.py` refuses control characters before
writing, and because the block was routed through that appender rather than
written directly. The first two attempts to run the appender did **not** catch
it: importing the older appender to reuse one function executed that module's
body instead of only its helper, and both the control and the real run then
failed identically with a NameError. A control that fails for the same reason
as the run it is controlling is the S17-22 shape again, and it was visible only
because the two were run side by side and their outputs compared. Fixed by
extracting the helper with `ast` rather than importing it, and by making the
control two-sided: one block that must be refused, one that must be accepted.

Consequence, added to P0: **never pass markdown through a double-quoted
PowerShell string.** Write the text in a file. The rule is not "escape the
backticks" - that is the coverage-list mistake again.
