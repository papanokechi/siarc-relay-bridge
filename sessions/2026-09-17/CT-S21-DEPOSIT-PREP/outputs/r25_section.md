
## R25 — the two attributions checked against the PDFs (CT-S21, cont.)

Both items §R24 recorded as the operator's own readings, one of them flagged
CONJECTURED, were checkable here: both PDFs are in `refs/` under CC-BY-4.0. So
they were checked rather than left attributed. Full detail in
`CT-S21-DEPOSIT-PREP/outputs/refs_attribution.md`.

**1. arXiv:2306.05930 — located; the paraphrase overstated it.** The passage is
on printed **p. 5**, §2.3 "Asymptotics", read from a rendered page image. The
certified interval, the inability to exclude 0, and the name *connexion problem*
are all as described. Two corrections:

- The paper says *"we do not know how to compute the leading coefficient exactly
  in general"* — a statement about the **state of the art**. It does **not** say
  the coefficient *is not computable*, which is a statement about the world.
  For the v1.7 framing of K and r_infinity this cuts both ways and must be
  quoted in the weaker, printed form.
- It is **background**, confirmed structurally: §2.3 is in the preliminaries,
  and the authors' contribution begins at §3, printed p. 6. Cite as the standard
  situation, not as their theorem.

`S21-26` is amended in place to **INSPECTED**, superseded by `S21-28`; the
`.bak-s21refs` copy is retained.

**2. Wong & Zhao §3 — class confirmed, growth law NOT FOUND.** §3 spans PDF
pp. 12–20, fixed from the PDF outline and asserted in the script. It **does**
cover this project's class, equation (3.2)
`y(n+2) + n^p a(n) y(n+1) + n^q b(n) y(n) = 0`, via Wong & Li [100] — the
operator's reading confirmed (`S21-30`).

The growth law is recorded as an **absence claim in the INSPECTED form the
operator requires** — "NOT FOUND in §3 by full-text read", with scope and
method, not "the survey does not state it" (`S21-31`).

**The absence test was built so it could fail.** A bare absence test cannot: an
empty or mis-scoped extraction would make every pattern "absent" and the verdict
would read as a finding — S17-22's failure mode exactly, a test that fails
uniformly. Six **positive controls** therefore run first over the same extracted
string (§3 heading, "Wong and Li", equation (3.2), "turning point",
Theorem 3.3, and the `K_{n+1}/K_{n-1} = c_n` normalisation). All six fired;
had any not, the script emits VOID and no absence verdict.

**Better than the absence, a structural reason for it** (`S21-32`). §3
normalises the growth away before it starts: at (3.23) it sets `x_n = y_n/K_n`
with `K_{n+1}/K_{n-1} = c_n`, so `K_n` absorbs precisely the product growth, and
Theorems 3.1–3.3 then give uniform Airy/Bessel expansions for `x_n` near
transition points. It is a turning-point theory in a parameter, and `K_0, K_1`
are left "depending on the particular sequence". The growth constant is not
merely missing from §3 — it is normalised out of view. That corroborates
Ibrahim–Salvy: the constant is the part tied to the initial conditions, and the
part nobody computes. **The purchase stays warranted**, and the two references
together sharpen why.

**3. Licence determinations are now version-pinned** (`S21-33`). arXiv licences
are per-submission **and per-version**, so the manifest now records that the
licence was read from the **abstract page, never the PDF**, and pins it to the
bytes held: page-1 stamps give `2204.09305v1` and `2306.05930v2`, and the
**versioned** abstract pages for those exact versions both print CC-BY-4.0. The
version came from each PDF's own margin stamp rather than an API answer about
the current version.

### A new failure mode for P0 — readback does not check intent

Repairing §R24 turned up four sites where a Python source literal had
interpreted escapes: `\refs/` and `\r_infinity` became CR, `\acquire_refs.py`
became BEL. A later text-mode read-modify-write then promoted each lone CR to a
full CRLF, so the damage presented as a spurious line break rather than a
control character (`S21-34`).

**The P0 readback rule did not catch this, and could not.** The script read back
the same already-mangled string it had written, and the comparison passed. The
rule establishes that *a write happened*; it does not establish that *the text
written was the text intended*. The mangling was upstream of the write.

Proposed **eighth amendment**: a write whose content is composed in source must
be verified against a property the source literal cannot vouch for — e.g. scan
the result for control characters, or compose the text in a separate file and
append it byte-wise rather than through a string literal. This round's §R25 was
written the second way.

The tree was scanned; `AUDIT.md` is now clean, and the remaining stray control
characters live only in raw PDF text extractions under `CT-S9-PVPARAMS/outputs/`,
where they are artefacts of the sources.
