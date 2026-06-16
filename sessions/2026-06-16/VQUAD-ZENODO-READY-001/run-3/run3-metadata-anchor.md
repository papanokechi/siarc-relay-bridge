# Stage 3 — Metadata anchor (run-3): CARRIES FORWARD UNCHANGED

## Result

**Metadata anchor = `4a75234faaef79d68caed6588d0fa0e2418ae17dfb2c18825a150b92f7970895`
— UNCHANGED from run-2.** No re-pin.

## Case determination (the KEY CHECK)

The brief's key check: *does the run-2 anchor incorporate the PDF SHA?* Determined by reading
run-2's `_finalize_metadata.py` — **not assumed**.

`_finalize_metadata.py` computes the anchor as the **whole-file SHA-256 of
`zenodo_metadata.md`** and nothing else:

```python
data = text.encode("utf-8")          # text = zenodo_metadata.md content
h = hashlib.sha256(data).hexdigest() # the anchor
```

The hashed content covers **title / abstract(description) / creators+affiliation / keywords /
MSC / version / related-identifiers pointer** — it does **NOT** embed the PDF hash. The
anchor's own "RE-PIN AGAIN IF" rule lists only *title/abstract/MSC/affiliation/version* edits,
not the PDF.

**⇒ Case A: the anchor is NOT PDF-hash-dependent.**

## Proof the file is unchanged by the layout fix

A whole-file scan of `zenodo_metadata.md` (the anchored file) for every PDF/bundle hash:

| token | in `zenodo_metadata.md`? |
|-------|--------------------------|
| `4ca12a35` (old PDF) | absent |
| `714771` / `028a1a5d` (old PDF size/MD5) | absent |
| `8752d7c7` (old bundle) | absent |
| `33f339ed` / `773171` / `99faea5b` (new PDF) | absent |
| `7bc5d008` (new bundle) | absent |

The file embeds **no** PDF or bundle hash, and the layout fix changed no abstract text, no
reference, no value. Therefore the file content is byte-identical to run-2, and:

```
(Get-FileHash -Algorithm SHA256 run-3/zenodo_metadata.md).Hash
  = 4a75234faaef79d68caed6588d0fa0e2418ae17dfb2c18825a150b92f7970895   ✓ (== run-2 anchor)
```

run-3 carries `zenodo_metadata.md` forward **byte-identical** (re-hash confirms `4a75234f…`).

## Disposition

Anchor **unchanged**: `4a75234f…` (still supersedes the PREP-001 provisional `dee9195c…`).
Re-pinning would be needless churn (explicitly cautioned against in the brief). The runner's
`METADATA_ANCHOR` constant stays `4a75234f…`.
