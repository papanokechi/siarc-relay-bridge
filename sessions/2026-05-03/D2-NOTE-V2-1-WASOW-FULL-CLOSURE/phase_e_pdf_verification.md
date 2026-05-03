# Phase E.11 — pypdf v2.1 verification

**Status:** PASS

## Procedure

```
python -c "from pypdf import PdfReader; r=PdfReader('d2_note_v2_1.pdf');
m=r.metadata; ..."
```

## Metadata

| Field | Value | Required |
|---|---|---|
| /Title | Cross-degree universality of the Borel-singularity radius for polynomial continued fractions (v2.1) | ✓ contains "(v2.1)" |
| /Author | Papanokechi | ✓ |
| Pages | 9 | ✓ ∈ [9,12] FULL |

## Body content tokens

| Token | Count | Required |
|---|---|---|
| Birkhoff | 29 | ≥ 1 |
| Trjitzinsky | 13 | ≥ 1 |
| Lemma | 26 | ≥ 1 (Lemma 3.1 must be in §3) |
| Newton polygon | 8 | ≥ 1 |
| Appendix | 1 | ≥ 1 (Appendix A) |
| SIARC | 16 | ≥ 1 (SIARC-disclosure footnotes) |
| Yokohama | 1 | ✓ author address |

## PII screen (must all be 0)

| Token | Count |
|---|---|
| OneDrive | 0 |
| Users | 0 |
| shkub | 0 |
| papanokechi@ | 0 |
| (no email patterns) | 0 |

PII screen PASS.

## SHA-256

`a8b6026a3453f901a0da68c3849a9d7d828138ca4622b8a3686b68f01d5ef74e`
