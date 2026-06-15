# V_quad exponential-period representation — reproducibility bundle

This bundle accompanies the paper

> **An explicit exponential-period representation of the $V_{\mathrm{quad}}$
> connection coefficient** — Papanokechi, 2026.

It contains everything needed to reproduce, from open source and open data, the
central identity of the paper:

$$ C \;=\; \frac{|\Gamma(\beta)|}{2\pi}\int_\gamma e^{\xi}\,\widehat B(\xi)\,d\xi
       \;=\; |\Gamma(\beta)|\,K, $$

where $C$ is the connection coefficient of the $V_{\mathrm{quad}}$ polynomial
continued fraction (the rank-one standalone closure on the Sakai surface
$D_5^{(1)}$, Painlevé V), $\widehat B$ is the order-4 holonomic Borel transform
of the $V_{\mathrm{quad}}$ asymptotic series with coefficients in
$\mathbb{Q}(\sqrt3)$, $\gamma$ is an explicit Hankel rapid-decay cycle on
$(-\infty,-2/\sqrt3]$, and $\beta=-1/(3\sqrt3)$. The identity is verified by
three structurally independent methods agreeing to **46 digits**.

## What is here

```
vquad-periodrep-bundle/
├── paper/        the paper (PDF + LaTeX source + byte-reproducible build script)
├── scripts/      verification scripts, grouped by the paper's narrative
│   ├── 01-algebraicity/   holonomic recognition of L_phi, L_V over Q(√3)
│   ├── 02-galois/         Kovacic (L_phi = SL2) and L_V Galois structure
│   ├── 03-verification/   the three independent verifications (Methods A/B/C)
│   └── 04-cycle/          the Hankel rapid-decay cycle and its period
├── data/         reference outputs (the *_results.json each script reproduces)
├── docs/         REPRODUCIBILITY, DEPENDENCIES, SIARC_PROVENANCE, CONVENTIONS
└── LICENSE       CC BY 4.0
```

## Start here

- **The paper:** [`paper/vquad-periodrep-paper.pdf`](paper/vquad-periodrep-paper.pdf)
  (23 pp). Rebuild byte-for-byte with `python paper/build.py` (see
  [`docs/DEPENDENCIES.md`](docs/DEPENDENCIES.md)).
- **How to verify each claim:** [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md)
  — a per-claim table mapping every numerical assertion in the paper to the
  script that produces it, the expected output, and the command to run.
- **Software requirements:** [`docs/DEPENDENCIES.md`](docs/DEPENDENCIES.md).
- **Provenance / epistemic history:** [`docs/SIARC_PROVENANCE.md`](docs/SIARC_PROVENANCE.md)
  — links to the SIARC relay-bridge probe slots that produced each result and
  the parent Zenodo deposits.
- **Conventions:** [`docs/CONVENTIONS.md`](docs/CONVENTIONS.md) — the kernel,
  normalisation, sign, base-field, branch and orientation conventions. These
  matter: the Borel-sum kernel convention in particular took an iteration to
  pin down, and getting it wrong changes intermediate quantities.

Each `scripts/0X-*/` directory has its own `README.md` describing its scripts,
their run order, and their expected runtime.

## How to cite

**The paper** (replace the DOI once the deposit is live):

> Papanokechi (2026). *An explicit exponential-period representation of the
> $V_{\mathrm{quad}}$ connection coefficient.* Zenodo. doi:10.5281/zenodo.XXXXXXXX

**This bundle** carries the same DOI as the deposit it is part of; cite the
paper and note "reproducibility bundle" if you reference the scripts or data
specifically.

The work builds on the $V_{\mathrm{quad}}$ companion paper
(Zenodo 10.5281/zenodo.20455090) and the $S=2\pi K$ Stokes calibration
(Zenodo 10.5281/zenodo.20481592); see [`docs/SIARC_PROVENANCE.md`](docs/SIARC_PROVENANCE.md).

## Authorship

This work is published under the pseudonym **Papanokechi**
(ORCID [0009-0000-6192-8273](https://orcid.org/0009-0000-6192-8273)), used
consistently and persistently across the author's body of work, with a
persistent public identifier (ORCID) attached for accountability. The pseudonym
is the sole byline; no institutional affiliation is claimed beyond *independent
researcher*. This usage is consistent with the London Mathematical Society
Ethical Policy §2.1.1, which recognises publication under a consistent
pseudonym tied to a verifiable identifier. Correspondence is via the ORCID
record.

## License

All material in this bundle is licensed **CC BY 4.0** — see [`LICENSE`](LICENSE).
You may share and adapt it for any purpose with attribution.
