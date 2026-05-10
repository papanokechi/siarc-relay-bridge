# OP_A1 Phase 3 -- self-review scan results

**Scanner:** PowerShell `Select-String` + .NET `[regex]::Matches`
**Target file:** `op_a1_phase2_candidates.md`
**Scan harness:** `_phase3_scan.ps1` (in this folder; reproducible)

---

## A. Whole-file scans (informational)

  | scan                                                                  | hit count |
  |-----------------------------------------------------------------------|----------:|
  | RULE 1 leakage `\b(Zenodo|endorsement|arXiv|Compositio|Ramanujan|AFM|venue|journal)\b` (case-insensitive) |     0 |
  | FV strict 7-verb 3p-singular `\b(closes|discharges|proves|establishes|ratifies|demonstrates|shows)\b` (case-insensitive) |     0 |
  | non-ASCII byte count                                                  |         0 |

PASS at the whole-file level for all three discipline gates.

---

## B. Per-candidate block scans (authoritative for HALT decisions)

Each block is the prose between the candidate header and the next section
header; this includes the fenced ``` block itself and the immediately following
prose paragraph.

### B.1 -- RULE 1 leakage scan

  | candidate | hits |
  |:---------:|-----:|
  | A         |    0 |
  | B         |    0 |
  | C         |    0 |

`HALT_OP_A1_RULE1_LEAKAGE` not triggered.

### B.2 -- FV strict 7-verb 3p-singular scan

  | candidate | hits |
  |:---------:|-----:|
  | A         |    0 |
  | B         |    0 |
  | C         |    0 |

`HALT_OP_A1_FV_FAIL` not triggered.

### B.3 -- Required-reference presence

  | candidate | cascade-132 sec 5 | slot 139 | BUNDLED-DEFERRED-NOTE | COMMITTED-2026-05-10 |
  |:---------:|:-----------------:|:--------:|:---------------------:|:--------------------:|
  | A         |        Y          |    Y     |          Y            |          Y           |
  | B         |        Y          |    Y     |          Y            |          Y           |
  | C         |        Y          |    Y     |          Y            |          Y           |

Note: the `cascade-132 sec 5` token spans a newline+indent in the wrapped notes
field of all three candidates; whitespace-relaxed regex `cascade-132\s+sec\s+5`
matches in each. A literal single-space scan returns False on all three; this
is a wrap artefact, not a missing reference.

### B.4 -- Block char / line counts

  | candidate | char length | line count (blockwise; includes fenced + post-prose) |
  |:---------:|------------:|-----------------------------------------------------:|
  | A         |         904 |                                                   22 |
  | B         |        1084 |                                                   24 |
  | C         |        1215 |                                                   26 |

NOTE: the prompt's 3-15 line size envelope applies to the Section 3 fenced
``` block itself, not to the candidate-section-with-prose. Within the fenced
block proper:

  | candidate | fenced-block lines |
  |:---------:|-------------------:|
  | A         |                 12 |
  | B         |                 14 |
  | C         |                 15 |

All three within 3-15 line envelope.

### B.5 -- Aggressive inflection scan (informational; no HALT)

Pattern: `\b(close[ds]?|closing|discharg(e[ds]?|ing)|prov(e[ds]?|ing)|establish(es|ed|ing)?|ratif(y|ies|ied|ying)|demonstrat(e[ds]?|ing)|show(s|ed|ing|n)?)\b`
(case-insensitive; matches root + past + gerund + plural forms).

  | candidate | aggressive hits | tokens | classification                                                                  |
  |:---------:|----------------:|--------|---------------------------------------------------------------------------------|
  | A         |               1 | `discharge` (in `sorry-discharge`) | root form, noun compound; permitted per slot 075 forbidden_verb_scan precedent ("discharge is root form, not third-person-singular discharges") |
  | B         |               1 | `discharge` (in `sorry-discharge`) | same classification as A                                                        |
  | C         |               1 | `discharge` (in `sorry-discharge`) | same classification as A                                                        |

No aggressive-inflection hit reaches the strict §5.E.3 third-person-singular
pattern. `dischargeable` (used in candidate B) does not match because the
aggressive pattern requires word boundaries; `dischargeable` is a derived
adjective and the regex `discharg(e[ds]?|ing)` does not match it. (If a
future, stricter scan flags it, the precedent for `discharge`-root compounds
extends naturally.)

---

## C. Verdict

  HALT_OP_A1_RULE1_LEAKAGE          : NOT TRIGGERED
  HALT_OP_A1_FV_FAIL                : NOT TRIGGERED
  HALT_OP_A1_SCAFFOLD_DRIFTED       : NOT TRIGGERED (sec 3 still PLACEHOLDER
                                      at scan time; verified by direct read of
                                      tex/submitted/control center/picture/
                                      m10_documented_commitment.md L9 + L135 +
                                      L209 -- all three placeholder markers
                                      present)

All three candidates ready for Phase 4 operator review.

*End of phase 3.*
