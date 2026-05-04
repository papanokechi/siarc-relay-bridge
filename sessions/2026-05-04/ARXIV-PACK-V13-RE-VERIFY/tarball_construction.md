# Tarball construction log -- ARXIV-PACK-V13-RE-VERIFY Phase B + C

## Phase B  -- git-archive extract from `58dfa9e`

B.1  Command:
```
git archive --format=tar 58dfa9e -- \
    sessions/2026-05-01/PCF1-V13-UPDATE/p12_pcf1_main.tex \
    sessions/2026-05-01/PCF1-V13-UPDATE/p12_pcf1_main.pdf | \
    tar -x -C sessions/2026-05-04/ARXIV-PACK-V13-RE-VERIFY/extract
```

B.2  Extract verification (re-hash):

| file                   | bytes  | sha256                                                              | matches Phase A |
| ---------------------- | -----: | ------------------------------------------------------------------- | --------------- |
| p12_pcf1_main.tex      | 46349  | e83bb377f297dbf0837facba257f227df4579e6a3518c139e3146f17174be301    | YES             |
| p12_pcf1_main.pdf      | 392886 | 63420dbf4abb7124672f522c37fc04ebdb3f6694ac39959456b2890d9788ff5e    | YES             |

B.3  Auxiliary file scan (LaTeX include directives):

```
\documentclass[12pt]{amsart}                    L1
\author{Papanokechi}                             L27
\title[CM Predicate ...]{...}                   L24-25
\begin{abstract} ... \end{abstract}             L66-89
\begin{thebibliography}{99}                     L840
```

No `\input`, `\include`, `\includegraphics`, or `\bibliography{}`
directives found. The .tex is self-contained (single-file amsart
manuscript with inline thebibliography). No .bib, no figure files,
no auxiliary inputs are needed for a clean compile.

## Phase C  -- rebuild tarball

C.1  Staging directory created at:
```
sessions/2026-05-04/ARXIV-PACK-V13-RE-VERIFY/pack/
sessions/2026-05-04/ARXIV-PACK-V13-RE-VERIFY/pack/pcf1_v1.3/
```

C.2  Files copied / written into pack/pcf1_v1.3/:

| file              | bytes |  sha256                                                             |
| ----------------- | ----: | ------------------------------------------------------------------- |
| 00README.txt      |  1993 | abffae86f8d467382164365f968cd1c5c5b4a3a3b3e26da2daa7eedd4ee2d27e    |
| abstract.txt      |  1486 | 839568a6dcd70047b5889bfa1fd9a3415dd5a947401d00c5e7fa827fd13ee5af    |
| p12_pcf1_main.tex | 46349 | e83bb377f297dbf0837facba257f227df4579e6a3518c139e3146f17174be301    |

The PDF is placed alongside the tarball (in pack/, not pack/pcf1_v1.3/),
matching the existing arxiv_pack_pcf1_v1.3 convention (arXiv source
tarballs do not normally embed the compiled PDF; arXiv recompiles
from source).

C.3  Tarball build:
```
tar -czf pcf1_v1.3.tar.gz pcf1_v1.3
```

| artefact          | bytes |  sha256                                                             |
| ----------------- | ----: | ------------------------------------------------------------------- |
| pcf1_v1.3.tar.gz  | 17560 | 93770e03c6ab9324ae1acd256b62c3af79e93a21ab83c653d412a0acab216ec9    |

Tarball listing:
```
$ tar -tzf pcf1_v1.3.tar.gz
pcf1_v1.3/
pcf1_v1.3/00README.txt
pcf1_v1.3/abstract.txt
pcf1_v1.3/p12_pcf1_main.tex
```

Note on tarball SHA reproducibility: gzip embeds a build-time
timestamp in the file header, so the tarball SHA-256 is NOT
deterministic across rebuilds (even with bit-identical contents).
The recorded SHA is the value for THIS session's build only.
Re-verification should be done at the per-file level (manifest
SHAs above) rather than the tarball SHA.

## Zenodo cross-check (Phase D.5)

```
$ python -c "import urllib.request, json; \
             r=urllib.request.urlopen( \
               'https://zenodo.org/api/records/19937196'); \
             d=json.loads(r.read()); \
             [print(f) for f in d['files']]"
```

Result:
| field            | value                                               |
| ---------------- | --------------------------------------------------- |
| record id        | 19937196                                            |
| DOI              | 10.5281/zenodo.19937196                             |
| version          | 1.3                                                 |
| title            | Complex Multiplication as a Transcendence Predicate |
|                  | for Degree-2 Polynomial Continued Fractions         |
| file key         | p12_pcf1_main.pdf                                   |
| file size        | 392886                                              |
| file md5         | fbf5449b2678834b0204360d49aef5e0                    |

Local md5 of canonical PDF: `fbf5449b2678834b0204360d49aef5e0`.

Match: PASS (md5 + size both byte-equal). The SHA-256
byte-equality is independently confirmed by re-hashing the
locally cached `zenodo.pdf` snapshot at
`sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_pcf1_v1.3/zenodo.pdf`
(SHA-256 = 63420dbf...d9788ff5e, identical to canonical).

### Spec record-ID discrepancy

The prompt §0 / §D.4 specified the Zenodo concept DOI as
`10.5281/zenodo.19941678` and the version record as
`10.5281/zenodo.19963298`. The Zenodo API returned:
- 19941678 -> redirected to 19972394 (Channel Theory paper, NOT PCF-1)
- 19963298 -> PCF-2 program statement (NOT PCF-1)

The actual PCF-1 v1.3 deposit lives at record **19937196**
(DOI `10.5281/zenodo.19937196`), as documented in the existing
`sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_pcf1_v1.3/
hash_match.json` (Zenodo URL field).

The byte-equality verification of the canonical PDF is unaffected
by this discrepancy. The discrepancy is logged in
`unexpected_finds.json` for operator / Claude review (likely a
prompt-spec transcription error against an outdated cheat-sheet).
