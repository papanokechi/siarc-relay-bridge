# SOP-BIBLIOGRAPHIC-VERIFICATION-APPEND — task spec as received

```
TASK: SOP-BIBLIOGRAPHIC-VERIFICATION-APPEND
TASK CLASS: housekeeping / standing-rule deposit
COMPUTE: minimal (~5 min, single file append)
BRIDGE: sessions/2026-05-04/SOP-BIBLIOGRAPHIC-VERIFICATION-APPEND/

BACKGROUND:
031 WITTE-FORRESTER-2010-ACQUISITION returned with two
hallucinated bibliographic identifiers (DOI + arXiv ID).
Synthesizer-Claude QA 2026-05-04 recommended the procedural
patch be appended to the standing-instructions block rather
than embedded in a paper-level methodology footnote, since
this is a procedural SOP not a publication-level disclosure.

STEPS:
1. Confirm target file exists at .github/copilot-instructions.md
   (or substitute correct standing-instructions location and
   surface in handoff.md).
2. Open the file and locate the "Phantom-hit prevention" section
   (the standard anchoring section for procedural SOPs).
3. Append the new section "## Bibliographic identifier pre-
   verification (lit-hunt prompts)" with the exact text from
   synthesizer follow-up 2026-05-04 ~17:00 JST (synthesizer
   provided the literal markdown block; copy verbatim).
4. Verify the file builds clean (markdown parses; no broken
   links or stray characters).
5. Append AEAL claim to claims.jsonl:
     {"claim_id": "sop_bib_verification_deposited",
      "type": "standing_rule_deposit",
      "confidence": "independently_verified",
      "evidence": "synthesizer QA 2026-05-04 + 031 verdict",
      "anchor_verdict": "031_WITTE_FORRESTER_2010_ACQUISITION"}
6. git commit -m "SOP-BIBLIOGRAPHIC-VERIFICATION-APPEND —
   standing-rule SOP for lit-hunt identifier pre-verification
   per synthesizer QA + 031 verdict"
7. git push.

HALT IF:
- Target file does not exist at any of the candidate paths
  (.github/copilot-instructions.md, docs/SIARC_standing_
  instructions.md, STANDING_RULES.md). Surface and ask operator
  for the correct path.
- A section with the same heading already exists (then surface
  for de-duplication; do not append a second copy).

PHANTOM-HIT NOTE: not applicable.
```

## Synthesizer-provided exact text (from operator message body)

The literal markdown block to append (from "Synthesizer follow-up
2026-05-04 ~17:00 JST" combined wording, included in the operator's
fire message):

```markdown
## Bibliographic identifier pre-verification (lit-hunt prompts)

**Rule (post-031 verdict, 2026-05-04):** For all literature-hunt
relay prompts that cite specific DOI or arXiv identifiers as
acquisition targets, the prompt-drafter (synthesizer or operator)
must pre-resolve each identifier and verify the resolved title +
authors match the cited reference *before* the relay prompt
fires. Hallucinated identifiers are a known LLM failure mode
(cf. 031 WITTE-FORRESTER-2010-ACQUISITION verdict, where DOI
10.1088/1751-8113/43/23/235202 resolved to Ayorinde et al. 2010
rather than the cited Witte-Forrester 2010, and arXiv:0911.1762
resolved to Desrosiers-Eynard 2009 rather than Witte-Forrester;
the agent gracefully degraded to a Forrester-Witte 2005 substitute
math/0512142, but ~20 minutes of agent runtime were spent
chasing the hallucinated identifiers).

**Pre-verification procedure:**

1. For each DOI: open `https://doi.org/<DOI>` and confirm the
   resolved publication's title + first-author surname match the
   cited reference.
2. For each arXiv ID: open `https://arxiv.org/abs/<arXiv-ID>`
   and confirm the same.
3. If an identifier resolves to a different paper than cited:
   - Treat as anomaly. Surface in the prompt-drafting chat.
   - Either substitute a verified identifier for the same intended
     paper, or substitute a different paper that serves the same
     purpose (declared as SCENARIO_C analogue in the prompt body).
   - Do NOT fire the relay prompt with the hallucinated identifier
     intact.
4. If an identifier cannot be resolved at all (404, withdrawn, or
   unreachable): surface and decide whether to substitute or to
   acquire the cited paper through a different channel (publisher
   direct URL, institutional repository, etc.).

**Scope:** applies to all lit-hunt-class relay prompts. Does not
apply to lit-hunt verdicts that simply cite already-acquired
artefacts by SHA — those are post-acquisition citations, not
pre-fire acquisition targets.

**Anchoring:** 031 WITTE-FORRESTER-2010-ACQUISITION verdict
(bridge session sessions/2026-05-04/...; ladder-extending verdict
with two hallucinated identifiers gracefully degraded to FW 2005
substitute).
```

## Notes on spec interpretation

- **Step 2 anchor section ("Phantom-hit prevention") not present.**
  The task spec instructed to "locate the 'Phantom-hit prevention'
  section (the standard anchoring section for procedural SOPs)."
  No such section exists in the current `.github/copilot-instructions.md`.
  The synthesizer's combined-wording instructions were more flexible:
  "Append location: under the existing 'Lit-hunt prompts' section if
  one exists, otherwise as a new top-level section before the 'AEAL
  claims' or 'Phantom-hit prevention' section (whichever comes
  earlier in the existing file structure)." Since none of those
  sections exist either, agent inserted the new section as a peer
  `##` heading between "Halt conditions" (L36–45) and "STANDING FINAL
  STEP" (former L49, now L96). This is the closest defensible
  anchoring: procedural SOPs sit alongside halt conditions in the
  pre-runtime/per-task-fire layer of the standing-instructions
  document.

- **`...` placeholder in synthesizer Anchoring line.** The synthesizer
  wrote `(bridge session sessions/2026-05-04/...; ladder-extending
  verdict with two hallucinated identifiers ...)`. Agent substituted
  `...` with the actual 031 session folder name
  `WITTE-FORRESTER-2010-ACQUISITION/`. This is strictly more accurate
  and the synthesizer's `...` was clearly a fill-in placeholder, not
  a deliberate ellipsis. Documented as Judgment-call #1 in handoff.md.

- **Heading-uniqueness check passed.** Pre-edit grep over
  `.github/copilot-instructions.md` for `bibliograph|identifier.*verif|lit.hunt|phantom`
  (case-insensitive) returned no matches; the new section is unique.
  No de-duplication required.

- **Markdown structure clean.** Post-edit file passes structural
  validation: 14 `##` headers, `---` separators on both sides of new
  section, 4-step numbered procedure renders cleanly with consistent
  indented bullets under step 3. No broken links or stray characters.
