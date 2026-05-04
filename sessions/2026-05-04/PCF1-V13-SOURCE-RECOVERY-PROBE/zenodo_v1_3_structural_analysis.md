# Zenodo v1.3 PDF — Structural Analysis (PCF-1)

**Source PDF:** `siarc-relay-bridge/sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_pcf1_v1.3/zenodo.pdf`
**SHA-256:** `63420dbf4abb7124672f522c37fc04ebdb3f6694ac39959456b2890d9788ff5e`
**Bytes:** 392,886
**Pages:** 16
**PDF /CreationDate:** `D:20260501121611+09'00'` (May 1 2026, 12:16:11 JST)
**Producer:** MiKTeX pdfTeX-1.40.28
**Zenodo version DOI:** `10.5281/zenodo.19937196`
**Zenodo concept DOI:** `10.5281/zenodo.19931635`

## Cross-source PDF identity

The recovered TeX source on the bridge at
`sessions/2026-05-01/PCF1-V13-UPDATE/p12_pcf1_main.tex` was committed
together with `p12_pcf1_main.pdf` whose SHA-256 is

  `63420dbf4abb7124672f522c37fc04ebdb3f6694ac39959456b2890d9788ff5e`

— **byte-identical** to the Zenodo-served deposit PDF. The committed
PDF and the Zenodo-served PDF are therefore the same PDF artefact
(no rebuild discrepancy, no producer drift, no metadata drift).

## TeX-level structural counts (canonical 16pp source)

Source: `sessions/2026-05-01/PCF1-V13-UPDATE/p12_pcf1_main.tex`
SHA-256: `e83bb377f297dbf0837facba257f227df4579e6a3518c139e3146f17174be301`
Bytes: 46,349   Lines: 837

| Item                          | Count |
|-------------------------------|------:|
| `\section{...}`               |     8 |
| `\subsection{...}`            |     1 |
| `\begin{theorem}`             |     1 |
| `\begin{proposition}`         |     0 |
| `\begin{lemma}`               |     0 |
| `\begin{corollary}`           |     0 |
| `\begin{conjecture}`          |     4 |
| `\begin{equation}` + `\begin{align}` | 4 |
| `\bibitem{...}`               |    14 |
| Approx. word count (post-stripping) | ~5,641 |

## Section list (canonical 16pp)

```
L100  \section{Introduction}\label{sec:intro}
L190  \section{The Spec(K) Framework --- v5 Upgrade}\label{sec:speck}
L272  \section{The Sharp Dichotomy}\label{sec:dichotomy}
L359  \section{Structural Evidence for the Analytic Part}\label{sec:structural}
L516  \section{The WKB Exponent Identity}\label{sec:wkb}
L611  \section{V_quad as the Explicit Prototype}\label{sec:vquad}
L671    \subsection{Channel scope of the prototype role}\label{ssec:vquad-channel-scope}
L720  \section{AEAL Evidence Chain}\label{sec:aeal}
L776  \section{Open Questions}\label{sec:open}
```

## Notes

- Theorem 5.bis (WKB exponent identity) — flagged in commit message
  for `58dfa9e` ("new Theorem 5.bis ... 6/6 families >=13 digits")
  is the single `\begin{theorem}` block in the canonical source.
- The single subsection (`Channel scope of the prototype role`) is
  the new V_quad channel-scope addition flagged in the same commit
  message.
- Conjecture count = 4 (matches "Conjecture A part (iv) restated"
  language in the commit message, parts (i)-(iv)).
