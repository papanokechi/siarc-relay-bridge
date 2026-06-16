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
| **VQUAD-COLDREAD-001** | Verdict A | Cold-read of the paper: **Verdict A** (publication-ready pending corrections); produced the 1 HIGH + 4 MED + 5 LOW corrections list scoped to VQUAD-PAPER-CORRECTIONS-001. Bridge commit `e207b33`. | [slot](https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-06-16/VQUAD-COLDREAD-001/) · [`claims.jsonl`](https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-06-16/VQUAD-COLDREAD-001/claims.jsonl) |
| **VQUAD-PAPER-CORRECTIONS-001** | COMPLETE | The cold-read corrections applied: 1 HIGH (the H-1 provenance remark, operator-verified) + 4 MED + 5 LOW + a bibliography repoint; the retracted v1.0 DOI was purged; corrections-final PDF, byte-reproducible, 24 pp. Bridge commit `d4fc87a`. | [slot](https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-06-16/VQUAD-PAPER-CORRECTIONS-001/) · [`claims.jsonl`](https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-06-16/VQUAD-PAPER-CORRECTIONS-001/claims.jsonl) |
| **VQUAD-PAPER-LAYOUTFIX-001** | COMPLETE | Systematic right-margin overflow fixed (20→0 overfull \hbox) as a **layout-only** re-pin: `\emergencystretch` + breakable monospace underscore (global) and display/table reflow (local). Proven reflow-only (PDF text diff = −2 line-end hyphens, 0 content characters). Layout-fixed PDF SHA-256 `33f339ed…`, byte-reproducible, 24 pp. **This bundle (run-2) is built against the layout-fixed paper.** Bridge commit `627d17e`. | [slot](https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-06-16/VQUAD-PAPER-LAYOUTFIX-001/) · [`claims.jsonl`](https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-06-16/VQUAD-PAPER-LAYOUTFIX-001/claims.jsonl) |

> **Provenance note (AEAL).** This bundle (VQUAD-REPRO-BUNDLE-002) is assembled
> against the **corrections-final** paper: the cold-read (VQUAD-COLDREAD-001,
> Verdict A) and the corrections cycle (VQUAD-PAPER-CORRECTIONS-001, complete)
> have both landed, and the H-1 provenance remark was operator-verified before
> insertion. It supersedes the preview bundle VQUAD-REPRO-BUNDLE-001, which was
> assembled against the pre-corrections draft. The paper PDF shipped here (run-2) is
> the **layout-fixed** byte-reproducible build (SHA-256 `33f339ed…`, 24 pp) — a
> reflow-only layout re-pin of the corrections-final paper that cleared systematic
> right-margin overflow (VQUAD-PAPER-LAYOUTFIX-001, bridge commit `627d17e`).

## Parent Zenodo deposits (read-only; not modified by this work)

- **$V_{\mathrm{quad}}$ companion paper** — Zenodo concept DOI
  **[10.5281/zenodo.20455089](https://doi.org/10.5281/zenodo.20455089)**
  (cite the concept; the $S=2\pi K$ correction lands in version 1.2,
  10.5281/zenodo.20481592, Remark 6.2 — the retracted v1.0 record is
  **not** cited). Source of the $V_{\mathrm{quad}}$ PCF, the
  $\mathrm{PV}/D_5^{(1)}$ Sakai identification, $\theta_\infty=2/\sqrt3$, and
  $\alpha=1/6$.
- **$S=2\pi K$ Stokes calibration** — Zenodo
  **[10.5281/zenodo.20481592](https://doi.org/10.5281/zenodo.20481592)**
  (version 1.2 of the companion above; same concept 10.5281/zenodo.20455089).
- **$\delta$ Fredholm-determinant cross-check (context)** — Zenodo concept DOI
  **[10.5281/zenodo.20624813](https://doi.org/10.5281/zenodo.20624813)**.
- **Sakai-stratification parent program** — Zenodo concept DOI
  **[10.5281/zenodo.20694840](https://doi.org/10.5281/zenodo.20694840)**
  (resolved in `VQUAD-ZENODO-PREP-001/related-identifiers.md`).

## Personal communication

The normalisation $L_{1,2}=x^2+\tfrac13 x+\tfrac13$ used throughout (the
"Marchal convention"; see `docs/CONVENTIONS.md` §2) and the genus-0
isomonodromic framing in §2 relate to the topological-recursion programme of
**O. Marchal** and collaborators (the three Marchal papers in the paper's
bibliography). The corrections-final paper additionally acknowledges
**correspondence with O. Marchal on the topological-recursion reconstruction of
Painlevé Stokes data (personal communication, June 2026)** — an acknowledgement,
not a load-bearing citation. It is a private communication, not a deposit.

## Open conditional layer

The transcendence statement (§6) is conditional on the Fresán–Jossen period
conjecture **and** a motivic-comparison hypothesis (differential vs. motivic
Galois group of $L_V$). The latter is the subject of a focused inquiry to
**Prof. Javier Fresán** (IMJ-PRG / Sorbonne Université, ERC EMOTIVE), drafted in
a separate SIARC slot (`FRESAN-JOSSEN-INQUIRY-001`) and awaiting send. Any
response will be incorporated as a personal communication in the corrections
slot before final deposit.
