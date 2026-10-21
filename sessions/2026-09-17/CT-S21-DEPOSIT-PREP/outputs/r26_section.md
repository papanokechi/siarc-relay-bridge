
## R26 — a mangled macro in the deposit object, found on the way to the walkthrough

Preparing the deposit runbook meant reading the notice's final section, which
turned out to print `heta_inf`, `heta_0`, `heta_t` in the methodology note at
lines 524–525: four `\theta` where a Python source literal had interpreted
`\t` as a TAB. A fifth site, `\b` as BACKSPACE, had eaten a `beta` in
`CT-S21-DEPOSIT-PREP/outputs/item2_quotes.md` — in the Borel-normalisation
quote, which is the lead carried forward to the `S_{ζ*}` work. All five
repaired (`S21-35`); both scanners now return zero.

**This is in the object that was about to be deposited.** The R25 scanner,
written one section earlier *for this exact defect class*, did not catch it:
it tested `\r`, `\a`, `\v`, `\f` and omitted `\t` and `\b` — precisely the two
escapes that consume the commonest macros in a Painlevé document (`\theta`,
`\tau`, `\times`, `\beta`).

**And the first fix under-reported 4 as 2** (`S21-36`). A guard added to stop
TAB indentation being flagged suppressed every hit at the start of a line, and
the mangled thetas sit at the start of two wrapped prose lines. That is the
S17-22 shape once more — a test that could not fire — this time *inside the
detector written in response to S17-22*, one round after the eighth amendment
was proposed for the same family. The guard now flags decisive tails regardless
of position.

The honest reading: the escape-mangling family has now produced three findings
in two rounds (§R25, §R26), each one caught by widening a detector that the
previous round had just written. The detectors are converging, but the sequence
is a reminder that a scanner's *coverage list* is itself an unchecked
assumption — the same defect as a hardcoded count word, one level up.

### Deposit walkthrough prepared

`CT-S21-DEPOSIT-PREP/DEPOSIT-WALKTHROUGH.md` (`S21-37`) collects what the
deposit needs into one runbook: pre-flight commands including the control that
must fire, the two deposit-day confirmations, the four-row citation pass with
p. 2637 added, the `refs/` non-upload rule stated per file with its licence
basis, Zenodo new-version mechanics against concept DOI `10.5281/zenodo.20455089`
and v1.2 version DOI `10.5281/zenodo.20481592`, the DataCite and
`metadata.rights` fallbacks, five abort conditions, and the post-publish record
steps.

Part B sets out the Wong–Li decision. The material point is that it has got
cheaper: with Ibrahim–Salvy now quoted in its weaker printed form and `S21-32`
supplying a structural reason the growth law is absent from Wong–Zhao §3, there
is a contribution statement resting on a page already held — `r_∞` is the
constant the classical method sets aside to reach turning-point behaviour, made
explicit. That survives either outcome. The recommendation is still to buy,
weakly held, on the one ground that the paper is the last unread source that
could bear on whether the connection constant is given in closed form.

**Nothing executed.** No deposit, no purchase, no commit, no upload.
