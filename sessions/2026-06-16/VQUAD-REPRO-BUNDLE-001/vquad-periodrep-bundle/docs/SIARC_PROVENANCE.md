# SIARC PROVENANCE

This bundle is the publishable distillation of a chain of governed research
probes run under **SIARC** (a relay-bridge methodology in which each probe is a
self-contained, time-stamped *slot* with an explicit verdict, a machine-readable
`claims.jsonl`, and a public BRIDGE URL). Each computational claim in the paper
traces to a specific slot, and within that slot to a specific claim record. This
document is the index from the paper back to those slots, so the epistemic
history is auditable at the per-claim (AEAL) level.

The slots themselves are **linked, not copied** into this bundle: the scripts
and data here are the curated, path-relativised essentials; the slots retain the
full working record (exploratory scripts, intermediate notes, verdict
documents).

## Probe slots

All slots live in the public repository
`github.com/papanokechi/siarc-relay-bridge`.

| Slot | Verdict | Established | BRIDGE URL · claims |
|------|---------|-------------|---------------------|
| **PERIOD-REP-VQUAD-001** | NEEDS-MORE-PROBE (scoping) | Headline numerics $K,S,C,\beta,\xi_0$; the bridge identity $C=\lvert\Gamma(\beta)\rvert K=\lvert A\rvert/\lvert\beta\rvert$; a summary of the Fresán–Jossen exponential-period axioms; scope of the open problem. | [slot](https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-06-15/PERIOD-REP-VQUAD-001/) · [`claims.jsonl`](https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-06-15/PERIOD-REP-VQUAD-001/claims.jsonl) |
| **PERIOD-REP-VQUAD-002** | GO_clean | Exact holonomic recognition over $\mathbb{Q}(\sqrt3)$; the operators $L_\varphi$ (ord 2) and $L_V$ (ord 4); singular locus and local exponents; the branch exponent $-(1+\beta)$; finite resurgence. | [slot](https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-06-15/PERIOD-REP-VQUAD-002/) · [`claims.jsonl`](https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-06-15/PERIOD-REP-VQUAD-002/claims.jsonl) |
| **PERIOD-REP-VQUAD-003** | VERIFIED | The Hankel rapid-decay cycle $\gamma$; the three independent verifications (Methods A/B/C, 46-digit agreement); the Kovacic $\mathrm{SL}_2$ proof for $L_\varphi$; the structural $L_V$ Galois data; the Fresán–Jossen application. | [slot](https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-06-15/PERIOD-REP-VQUAD-003/) · [`claims.jsonl`](https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-06-15/PERIOD-REP-VQUAD-003/claims.jsonl) |
| **VQUAD-PERIODREP-PAPER-001** | drafted | The paper itself: LaTeX source, build script, reproducibility statement (the claim→script map this bundle's `docs/REPRODUCIBILITY.md` mirrors). | [slot](https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-06-15/VQUAD-PERIODREP-PAPER-001/) · [`claims.jsonl`](https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-06-15/VQUAD-PERIODREP-PAPER-001/claims.jsonl) |
| **VQUAD-PAPER-CORRECTIONS-001** | *pending* | The cold-read corrections slot. **Not yet created at the time this bundle was assembled** (2026-06-16); the bundle is built against the byte-reproducible draft of VQUAD-PERIODREP-PAPER-001. When the corrections slot exists, its URL follows the same pattern and the deposit should reference the corrected paper. | *(to be created: `…/sessions/<date>/VQUAD-PAPER-CORRECTIONS-001/`)* |

> **Honesty note (AEAL).** At assembly time the corrections slot did not yet
> exist and the cold-read verdict was not yet recorded. The bundle is therefore
> *integrity-verified against the current draft*; final-paper certification is a
> downstream operator gate. See the bundle's `prerequisite-check.md` in the
> assembly slot for the full disposition.

## Parent Zenodo deposits (read-only; not modified by this work)

- **$V_{\mathrm{quad}}$ companion paper** — Zenodo
  **[10.5281/zenodo.20455090](https://doi.org/10.5281/zenodo.20455090)**
  (concept 10.5281/zenodo.20455089). Source of the $V_{\mathrm{quad}}$ PCF, the
  $\mathrm{PV}/D_5^{(1)}$ Sakai identification, $\theta_\infty=2/\sqrt3$, and
  $\alpha=1/6$.
- **$S=2\pi K$ Stokes calibration** — Zenodo
  **[10.5281/zenodo.20481592](https://doi.org/10.5281/zenodo.20481592)**.
- **$\delta$ Fredholm-determinant cross-check (context)** — Zenodo
  **[10.5281/zenodo.20624814](https://doi.org/10.5281/zenodo.20624814)**.
- **Sakai-stratification parent program** — concept DOI to be inserted by the
  operator at deposit time (not yet minted in the corpus).

## Personal communication

The normalisation $L_{1,2}=x^2+\tfrac13 x+\tfrac13$ used throughout (the
"Marchal convention") and a framing point in §2 follow a **personal
communication from C. Marchal (June 2026)**, cited as such in the paper. It is a
private communication, not a deposit; the citation in §2 is the authoritative
reference.

## Open conditional layer

The transcendence statement (§6) is conditional on the Fresán–Jossen period
conjecture **and** a motivic-comparison hypothesis (differential vs. motivic
Galois group of $L_V$). The latter is the subject of a focused inquiry to
**Prof. Javier Fresán** (IMJ-PRG / Sorbonne Université, ERC EMOTIVE), drafted in
a separate SIARC slot (`FRESAN-JOSSEN-INQUIRY-001`) and awaiting send. Any
response will be incorporated as a personal communication in the corrections
slot before final deposit.
