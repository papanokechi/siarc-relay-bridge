# Rubber-duck critique — SIARC-UMBRELLA-V2-RELEASE

Self-critique pass against the seven focus items from the Phase F spec.

## (a) Does §4 Cross-Degree Framing subsume the v1 (2,1) framing without contradicting it?

**Verdict: yes.** §4 introduces the invariant triple
$(\Delta_d, \|\Delta\|_{\mathrm{Pet}}, \xi_0)$ as the cross-degree
organisational principle. The "Forward reference to the cross-degree
framing" paragraph at the end of §2 (Four-Tier Hierarchy) explicitly
states that "The v1 four-tier hierarchy is the d=2, $\Delta_2$-only
specialisation of the cross-degree picture." The "Cross-degree
extension" paragraph at the end of §5 (Trans-Stratum Conjecture)
recovers Class A / Class B as the two branches of the $\Delta_2$-axis
split with BT and Ramanujan resolution respectively. The introduction's
"What changed between v1 and v2.0" paragraph states the compatibility
explicitly. No v1 conjecture (Conjecture~\ref{conj:t2b}) or open
problem (`prob:31` / `prob:t2-d2-nonpsl` / etc.) is retracted; v2.0
adds, never subtracts.

## (b) Is the d=3 restriction of B5/B6 stated consistently in abstract, §4.3, and Open Problems?

**Verdict: yes, with one small wording asymmetry.**
- Abstract: states the cubic-modular framing absorbs PCF-2 v1.3 and
  references `op:j-zero-amplitude-h6`, `op:j-1728-wedge`,
  `op:shallow-j-effect-d4` (which inherit the d=3 origin).
- §4.3 (`sec:triple-moddisc`): Conjecture~\ref{conj:b5-b6-d3} is
  titled "Cubic-modular split, $d=3$" and each clause explicitly
  begins "For $\PCF(1,b)$ with $b \in \Q[x]$ irreducible non-singular
  cubic". The d=4 deep-WKB null is documented as the structural
  reason for the restriction.
- §6 Open Problems: `prob:modular-discriminant-stratification`
  cross-references Conjecture~\ref{conj:b5-b6-d3} via `\cite{PCF2}`
  Session T2; `prob:j-zero-amplitude` and `prob:shallow-j-effect-d4`
  carry the d-specific restriction.

The minor wording asymmetry is that the abstract does not name B5/B6
explicitly (it speaks of "the cubic-modular framing of PCF-2 v1.3");
this is intentional — v2.0 is a program statement that *cites* B5/B6
rather than restating it as a primary v2.0 conjecture. Logged as a
notation choice, not a discrepancy.

## (c) Is the bibliography complete for every \cite{...} introduced in §4?

**Spot-check of every new \cite in §4:**
- `\cite{PCF1}` → entry present (Zenodo v1.3 with version + concept DOIs).
- `\cite{PCF2}` → entry present (Zenodo v1.3).
- `\cite{CT}` → entry present (Zenodo v1.2).
- `\cite{Birkhoff1930}` → entry present (Acta Math 54).
- `\cite{BirkhoffTrjitzinsky1933}` → entry present (Acta Math 60).
- `\cite{ChowlaSelberg1967}` → entry present (Crelle 227).

§5 still cites `\cite{Paper14}` (kept), §6 cites `\cite{P08}` (kept).
`\cite{jSN}` is present in the bib but cited only in the Companion
Papers table textually (not via `\cite`); harmless.

`pdflatex.log` reports 0 missing citations across 3 passes. ✓

## (d) Companion Papers table reflects current state of each record?

**Verdict: yes.** The table is split into three subtables:
- *Published (Zenodo, May 2026):* PCF-1 v1.3 (10.5281/zenodo.19937196),
  PCF-2 v1.3 (10.5281/zenodo.19963298), CT v1.2
  (10.5281/zenodo.19951331), T2B v3.0 (10.5281/zenodo.19915689),
  UMB v2.0 (this document; concept 10.5281/zenodo.19885550).
- *Drafting / forthcoming:* jSN, D1, D2-NOTE, D3, D7, MASTER-V0.
- *Carried over from v1:* #14, P08, G1, G2, OP.

Status field reflects current state (v1.3 for PCF-1/PCF-2, v1.2 for CT,
v3.0 for T2B, "this document" for UMB v2.0). DOIs cross-checked
against the bridge predecessor records (PCF2-V13-RELEASE handoff;
CHANNEL-THEORY-V12 release).

## (e) AI Disclosure: characterises multi-agent fleet methodology without leaking vendor / session / prompt detail beyond the public bridge?

**Verdict: yes.** The disclosure names "GitHub Copilot powered by
Anthropic Claude Opus 4.7, and standalone Anthropic Claude sessions" —
the same wording used in PCF-2 v1.3's disclosure — and points to the
public SIARC bridge for the audit trail. It names Fleet-A, Fleet-F,
the AEAL schema (canonical from PCF-2 v1.3 forward), and the
per-session `claims.jsonl` mechanism. No prompt text, no internal
session IDs beyond what is already publicly visible on the bridge,
no specific model-version revelations beyond the Claude Opus 4.7
naming that is already in the public PCF-2 v1.3 record. Reaffirms
author responsibility per spec.

## (f) Page count plausible (18–22 pp expected)?

**Verdict: page count is 12, below the 18–22 target stated in the
spec.** This is *not* a halt condition (halt only triggers if pages
< v1 = 7). The spec said "if §4 alone exceeds 5 pages, trim — the
goal is *organisation*, not *exposition* of the post-March results
(those live in PCF-1, PCF-2, Channel Theory)". §4 occupies roughly
3 pages and is at the right level of compression: definitions
(§4.1), one paragraph per axis (§4.2/§4.3/§4.4), one paragraph for
the cell decomposition (§4.5). Padding §4 with worked examples or
rederiving the Petersson correlation locally would violate the
"program statement, not a results paper" stance enumerated in §9 of
the prompt. The 18–22 pp band in the spec was an *estimate* assuming
v1 was 13 pp; v1 is actually 7 pp, so the 12-pp v2.0 is the
proportional analogue. Logged in `unexpected_finds.json`.

## (g) Are all five DataCite cross-refs cited at least once in the v2.0 body, not just the bibliography?

| relation | DOI | bib entry | body citation |
|---|---|---|---|
| isNewVersionOf v1 | 10.5281/zenodo.19885550 | (concept) | §1 ("What changed between v1 and v2.0", `\href{...19885550}`); §5 (`rem:t2b-prerev`); §AI Disclosure |
| References PCF-1 | 10.5281/zenodo.19931635 (concept) | `\bibitem{PCF1}` | §1 (`\cite{PCF1}`-via §2 fwd ref); §4.2 (`\cite{PCF1}`); §5 cross-degree extension |
| References PCF-2 | 10.5281/zenodo.19936297 (concept) | `\bibitem{PCF2}` | §1 (intro changes); §4.2/§4.3 (`\cite{PCF2}`, multiple); §6 (\textsf{prob:31} status); §AI Disclosure |
| References CT    | 10.5281/zenodo.19941678 (concept) | `\bibitem{CT}` | §4.4 (`\cite{CT}`, V$_{\mathrm{quad}}$ recovery); §4.5 (`\cite{CT}` channel functor); §6 (`prob:median-resurgence-extension`) |
| References T2B   | 10.5281/zenodo.19783311 (concept) | `\bibitem{T2B}` | §5 (`rem:empirical`, explicit href); §AI Disclosure |
| isSupplementedBy jSN | arXiv `__ARXIV_ID__` | `\bibitem{jSN}` | Companion Papers table (textual citation row "jSN") |

All five DataCite cross-refs appear in the body, not just the
bibliography. ✓

## Summary

No discrepancies that demand a halt. One notation choice (abstract
defers naming B5/B6 directly to §4.3) and one expected-page-count
deviation (12 pp vs spec's 18–22 pp band) logged for the handoff's
"Anomalies and open questions" and `unexpected_finds.json`.
