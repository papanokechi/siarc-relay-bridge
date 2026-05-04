# Source verification log -- ARXIV-PACK-V13-RE-VERIFY Phase A

Date: 2026-05-04
Bridge commit under verification: `58dfa9e`

## A.1  Commit reachability

```
$ git rev-parse 58dfa9e
58dfa9e732b41b65c2d8791037286a13e21c06be
```

Status: PASS (commit reachable from origin/main).

Commit message (one-liner):
> PCF1-V13-UPDATE -- v1.3 PCF-1 LaTeX (Variant A: BOTH ARTEFACT);
> folds in Sessions D, E, E'; new Theorem 5.bis (WKB exponent identity,
> 6/6 families >=13 digits), new V_quad channel-scope subsection,
> Conjecture A part (iv) restated as channel-scoped sporadic-V_quad;
> 16pp, 0 errors

`git show --stat 58dfa9e -- sessions/2026-05-01/PCF1-V13-UPDATE/`:
- handoff.md                     127 lines added
- p12_pcf1_main.pdf              binary, 392886 bytes
- p12_pcf1_main.tex              925 lines added

## A.2  TeX SHA-256 (working tree)

```
sessions/2026-05-01/PCF1-V13-UPDATE/p12_pcf1_main.tex
  SHA-256: e83bb377f297dbf0837facba257f227df4579e6a3518c139e3146f17174be301
  bytes:   46349
```

Status: PASS.

## A.3  PDF SHA-256 (working tree)

```
sessions/2026-05-01/PCF1-V13-UPDATE/p12_pcf1_main.pdf
  SHA-256: 63420dbf4abb7124672f522c37fc04ebdb3f6694ac39959456b2890d9788ff5e
  bytes:   392886
```

Spec gate: PDF SHA must equal `63420dbf...d9788ff5e`.
Match: PASS (byte-exact).

## A.4  Page count

```
$ python -c "from pypdf import PdfReader; print(len(PdfReader(...).pages))"
pages= 16
```

Spec gate: must equal 16. Status: PASS.

## A.5  Cross-check against 027 handoff.md

027 (PCF1-V13-SOURCE-RECOVERY-PROBE) recorded:
- TeX SHA-256: `e83bb377f297...74be301`
- PDF SHA-256: `63420dbf4abb...d9788ff5e`, 392,886 bytes, 16 pages

Both values match this session's measurements verbatim.

## A summary

All Phase A gates GREEN. No HALT condition triggered.

| gate                         | spec value                          | measured                              | status |
| ---------------------------- | ----------------------------------- | ------------------------------------- | ------ |
| commit reachable             | 58dfa9e                             | 58dfa9e732...                         | PASS   |
| tex SHA-256 vs 027           | e83bb377...74be301                  | e83bb377...74be301                    | PASS   |
| pdf SHA-256 vs spec          | 63420dbf...d9788ff5e                | 63420dbf...d9788ff5e                  | PASS   |
| pdf bytes                    | 392886                              | 392886                                | PASS   |
| page count                   | 16                                  | 16                                    | PASS   |

Proceed to Phase B (git-archive extract).
