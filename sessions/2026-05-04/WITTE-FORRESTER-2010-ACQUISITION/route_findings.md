# Route Findings — WITTE-FORRESTER-2010-ACQUISITION

**Date:** 2026-05-04
**Phases A + B + C log.**

---

## Phase A — bibliographic confirmation

### A.1 DOI lookup

Fetch: https://iopscience.iop.org/article/10.1088/1751-8113/43/23/235202

**Result:** The DOI resolves to a different paper:
> "New identities from quantum-mechanical sum rules of parity-related potentials"
> by O. A. Ayorinde, K. Chisholm, M. Belloni, R. W. Robinett
> Published 13 May 2010, J. Phys. A: Math. Theor. 43 (2010) 235202.
> Topic: Airy-function-zero identities, parity-related potentials, quantum harmonic oscillator. Has nothing to do with Painlevé equations or random matrices.

### A.2 arXiv lookup

Fetch: https://arxiv.org/abs/0911.1762

**Result:** arXiv:0911.1762 resolves to a different paper:
> "Supermatrix models, loop equations, and duality"
> by Patrick Desrosiers, Bertrand Eynard
> Submitted 9 Nov 2009, J. Math. Phys. 51 (2010) 123304, DOI 10.1063/1.3430564.
> Topic: Hermitian supermatrix integrals, topological expansion, symplectic invariants. Also unrelated to Painlevé III' or τ-function gap probabilities.

### A.3 Author-listing cross-check

- Peter Forrester arXiv listing (https://arxiv.org/a/forrester_p_1.html, ~89 papers): no entry matching the spec target. No 2009 or 2010 submission to J. Phys. A 43 235202.
- Nicholas Witte arXiv listing (https://arxiv.org/a/witte_n_1.html, ~51 papers, ORCID 0000-0001-7537-8444): no entry matching the spec target.

**Phase A verdict:** the spec primary target does not exist. Both identifiers reproducibly point to unrelated papers. See `discrepancy_log.json`.

---

## Phase B — substitute selection (re-purposed from spec Phase B)

Since the spec target is unretrievable, Phase B was repurposed to identify the closest Forrester-Witte thematic substitute for the homomorphism question.

### B.A Candidate set from author listings

Three Forrester-Witte papers most-thematically aligned with "PIII' τ-function evaluations":

1. **arXiv:math/0512142** (2005, Forrester & Witte): "Boundary conditions associated with the Painlevé III' and V evaluations of some random matrix averages." J. Phys. A 39 (2006) 28 S13. **The only Forrester-Witte arXiv title containing the literal string "Painlevé III'".**
2. **arXiv:math-ph/0203049** (2002, Forrester & Witte): "τ-Function Evaluation of Gap Probabilities in Orthogonal and Symplectic Matrix Ensembles." Nonlinearity 15 (2002) 3 325.
3. **arXiv:math-ph/0201051** (2002, Forrester & Witte): "Application of the τ-function theory of Painlevé equations to random matrices: PV, PIII, the LUE, JUE and CUE."

Selection: **#1 (math/0512142)** as primary substitute, because (a) it is the only paper with literal "Painlevé III'" in its title, (b) it is the highest title-similarity match to the spec target, and (c) the 2005-2010 Forrester-Witte PIII' oeuvre is uniformly in the σ-form/Hamiltonian framework, so #1 is representative of the broader oeuvre for this question.

### B.B arXiv direct (substitute)

  GET https://arxiv.org/pdf/math/0512142
  → 200 OK
  → file size: 181171 bytes
  → SHA-256: 80E050092174159A4D7DCE3F5E8436DAA0C3A5502830178FE3ACCAB8AF83CB61

OA route succeeded. No paywall encountered. No auth required. Rule 1 / Rule 2 / Rule 3 all satisfied.

### B.C IOPscience landing (substitute)

Not probed for the substitute (arXiv route succeeded). Per standing convention, when arXiv route succeeds the IOPscience probe is unnecessary.

### B.D Author home pages

Not probed for the substitute (arXiv route succeeded).

### B.E Internet Archive

Not probed for the substitute (arXiv route succeeded).

### B.F ResearchGate

Not probed for the substitute (arXiv route succeeded).

---

## Phase C — primary acquisition (substitute)

### C.1 PDF acquisition

  Source: https://arxiv.org/pdf/math/0512142
  Local path: `substitute_FW_2005_PIIIp_boundary.pdf`
  Size: 181171 bytes
  SHA-256: 80E050092174159A4D7DCE3F5E8436DAA0C3A5502830178FE3ACCAB8AF83CB61

### C.2 Text-layer extraction

  Tool: `pdftotext -layout`
  Output: `substitute_FW_2005_PIIIp_boundary.txt`
  Size: 52445 bytes
  Lines: 766

Text-layer quality: machine-extractable; full-text search succeeded.

### C.3 Slot 17 deposit (NOT EXECUTED)

The spec instructs deposit at:
  `tex/submitted/control center/literature/g3b_2026-05-03/17_witte_forrester_2010_pIII_tau.pdf`

This deposit was **NOT** executed because the substitute is NOT the spec
target. Depositing the substitute under the spec slot name would mis-label
the literature library. The substitute remains in the bridge session
directory; if Claude / operator authorizes the substitute as the close-out
artefact, slot 17 deposit can be performed in a follow-up task with a
correct slot label (e.g. `17_forrester_witte_2005_PIIIp_boundary.pdf`).

---

## Summary

  Phase A: HALT — spec target does not exist (two erroneous identifiers).
  Phase B: substitute selected — arXiv:math/0512142.
  Phase C: substitute acquired (181171 B, SHA 80E050...3CB61); text extracted
           (52445 B, 766 lines); slot 17 deposit deferred pending authorization.
