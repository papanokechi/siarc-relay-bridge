# Stage 5 — Wrong-venue gate (Gate 2.2) → PASS (run-2)

Formal re-confirmation against the **corrections-final PDF** (`4ca12a35…`, the
deposit-target file), extracting full text with `pypdf` and testing the
forbidden-venue tokens.

```
=== GATE 2.2 (wrong-venue, vs 4ca12a35 PDF) ===
PDF chars: 63635
Compositio   present: False
AAECC        present: False
ETNA         present: False
'Symbolic Comput' (legit Kovacic cite) present: True
GATE 2.2: PASS
```

## Tokens

- **`Compositio`** — the canonical wrong-venue halt token (the deposit must not
  accidentally name a target journal in the manuscript body). **Absent.**
- **`AAECC`** — advisory token (the venue that desk-rejected the EBR-III paper;
  guards against stale venue strings). **Absent.**
- **`ETNA`** — legacy placeholder token carried from the Sakai kit. **Absent.**
- **`JSC` / "Symbolic Comput"** is **not** a halt token: it collides with the
  legitimate Kovacic citation (*J. Symbolic Comput.* 2 (1986) 3–43). The probe
  confirms "Symbolic Comput" **is** present (the citation) and is correctly **not**
  treated as a venue leak.

**Gate result: PASS** — no forbidden-venue string in the 63 635-char text of the
deposit-target PDF. This is the formal Gate-2.2 precheck; the runner repeats it at
`--execute` time against the staged PDF.
