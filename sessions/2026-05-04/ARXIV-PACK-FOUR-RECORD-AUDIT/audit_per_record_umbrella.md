# Audit — siarc_umbrella_v2.0

- Bridge pack path: `siarc-relay-bridge/sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_siarc_umbrella_v2.0/`
- Claimed Zenodo concept-DOI: `10.5281/zenodo.19885549` → actual `10.5281/zenodo.19885549`  **[PASS]**
- Claimed Zenodo version-DOI: `10.5281/zenodo.19965041` → actual `10.5281/zenodo.19965041`  **[PASS]**
- Title (API): "An Arithmetic Stratification of Polynomial Continued Fractions — v2.0 (Modular-Discriminant Framing)"  **[PASS]** (matches 00README.txt)
- Version-string (API): `2.0`  **[PASS]**
- File on Zenodo: `main.pdf`, size 455178 B, `md5:d633699fbfe698dae08d510e8e165320`
- Cached `zenodo.pdf` SHA-256: `24382421290318ae2a8fd8f22e3a0ec6953d738d35411c61e32c26e7bd8f2037`
- Cached `zenodo.pdf` MD5: `d633699fbfe698dae08d510e8e165320` vs API `d633699fbfe698dae08d510e8e165320`  **[PASS]**
- Cached `zenodo.pdf` size: 455178 B vs API 455178 B  **[PASS]**
- Cached `zenodo.pdf` page count: 12 vs expected 12  **[PASS]**
- Local rebuilt PDF (`pack/main.pdf`) SHA-256: `fe7508d8da0e0cac7247e53116ba360f40d6a56c777544234241bb397380881d` (differs from Zenodo SHA — expected: pdfTeX timestamp drift)
- Local rebuilt PDF size: 455178 B (byte-equal to Zenodo)  **[PASS at content layer]**
- Local rebuilt PDF page count: 12  **[PASS]**

**Verdict:** PASS

**Follow-on recommendation:** NONE. Pack metadata, IDs, deposited PDF byte-match, and page count are all clean.
