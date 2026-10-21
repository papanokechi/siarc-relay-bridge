# PREREG — CT-S58-READ-LOCATOR

Written before any computation in this session.

## Purpose

The operator's remaining Tier-1 and Tier-2 work is *reading*, not computation.
This session produces no mathematics. It converts two instructions —

- "read the LMP revision end to end, §5 and Table 2 first, then the L455
  replacement, the abstract and §1.3"
- "cross-check the Painlevé paper against the five LMP correction items"

— into **page and line addresses**, so the reading is bounded and nothing that
changed goes unread.

## Hypothesis

H1. Every one of the 33 replacements that CT-S56 applied to v1.2 is locatable
    on a definite page of the revised PDF.

H2. The Painlevé paper (CT-S50-READ-REPAIRS) contains statements about the
    objects the five LMP correction items touch — V_quad, L_phi, apparency at
    xi=0, the D_5^(1) surface identification, verification independence — and
    those statements are locatable by file and line.

## Observables

O1. For each replacement: the 1-based page of the revised PDF on which its new
    text appears, or UNLOCATED.
O2. For each of the five correction items: the set of (file, line) in the
    Painlevé paper source whose text is in that item's scope.

## Falsifiers, with thresholds

F1. **Any** replacement is UNLOCATED → H1 fails. Threshold: 33/33 located.
    The locator must report UNLOCATED, never a guessed page. (CT-S56 finding
    (c): a numbering locator that invents an answer is worse than one that
    abstains.)
F2. The discrimination control fails: the phrase "three structurally
    independent methods", which item 5 removed, must be **absent** from the
    revised PDF and **present** in the v1.2 PDF. If it is absent from both, the
    reader is blind and every "absent" in this session is uninterpretable.
    (Memory: a check reporting absence cannot distinguish missing content from
    a reader that cannot see.)
F3. The positive control fails: the word "Kovacic" must be located in both
    PDFs. If it is not, extraction is broken and all page numbers are void.
F4. For O2, the Painlevé sweep returns zero hits on **all five** items. That
    would mean either the two papers share no objects — contradicted by both
    being about V_quad — or the sweep's patterns cannot see. Either way, halt.

## Vacuity pre-check

The observable must move when the data moves. Before reporting, the locator
runs the page-finder against **both** the v1.2 PDF and the revised PDF with the
identical anchor set. If the two runs return identical results for every
anchor, the instrument is not sensitive to the revision and the output is
vacuous. At least the anchors drawn from item-5 new prose must differ.

## Non-vacuity of the report (commissioning clause)

An empty sweep and an absent sweep are indistinguishable in a report that
records only hits. Every pattern run is listed in the output with its count,
**including zero**, and a zero is stated as "pattern ran, 0 hits", never
omitted.

## Labels

Everything this session produces is INSPECTED: page numbers and line numbers
read off rendered and source files. No claim here is VERIFIED, STRUCTURAL or
PROVEN, because nothing is computed. Locating a sentence is not judging it —
the judgements are the operator's, and this session must not pre-empt them.

## Halt conditions

Any falsifier fires; a required PDF is missing; the revised PDF's page count is
not the 27 recorded by CT-S56.
