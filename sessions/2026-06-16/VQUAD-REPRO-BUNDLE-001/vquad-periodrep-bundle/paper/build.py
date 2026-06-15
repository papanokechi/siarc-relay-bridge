#!/usr/bin/env python
r"""Byte-reproducible build for the V_quad period-representation paper (bundle).

This bundle ships the fully self-contained, pre-assembled LaTeX source
``vquad-periodrep-paper.tex`` (preamble inline, bibliography inline as a
``thebibliography`` -- no external sections, no .bib, no graphics). This script
just compiles it twice with a fixed ``SOURCE_DATE_EPOCH`` so the output PDF is
byte-identical to the deposited one.

    python build.py

Reproducibility target (environment of record: MiKTeX 25.12, pdflatex 4.23):
    SHA-256 = 359D1172AF3F867F4349CF4776A222813A855CD354BC78C0B68CCFB0026C702B
    size    = 698730 bytes, 23 pages

The byte-identical hash is guaranteed only under the environment of record;
other TeX distributions produce a visually identical PDF that may differ in
byte hash. See ../docs/DEPENDENCIES.md.
"""
import hashlib
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TEX = "vquad-periodrep-paper.tex"
PDF = os.path.join(HERE, "vquad-periodrep-paper.pdf")
TARGET_SHA = "359d1172af3f867f4349cf4776a222813a855cd354bc78c0b68ccfb0026c702b"

# Fixed epoch (2024-06-15) -> reproducible \today and PDF metadata, together
# with the preamble guards \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=-1.
EPOCH = "1718409600"

# MiKTeX default per-user install location (environment of record); used only if
# pdflatex is not already on PATH.
MIKTEX = os.path.expandvars(
    r"%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe")


def find_pdflatex():
    exe = shutil.which("pdflatex")
    if exe:
        return exe
    if os.path.exists(MIKTEX):
        return MIKTEX
    sys.exit("ERROR: pdflatex not found on PATH and not at the MiKTeX default "
             "location. Install a TeX distribution (see ../docs/DEPENDENCIES.md).")


def main():
    pdflatex = find_pdflatex()
    env = dict(os.environ)
    env.setdefault("SOURCE_DATE_EPOCH", EPOCH)
    log = ""
    for _ in range(2):
        r = subprocess.run(
            [pdflatex, "-interaction=nonstopmode", "-halt-on-error", TEX],
            cwd=HERE, env=env, capture_output=True, text=True)
        log = r.stdout + r.stderr

    pages = None
    m = re.search(r"Output written on .*\((\d+) pages?", log)
    if m:
        pages = int(m.group(1))
    errs = [l for l in log.splitlines() if l.startswith("!")]
    undef = sorted(set(re.findall(r"(Citation|Reference) `([^']+)' .*undefined", log)))

    print(f"PAGES={pages}")
    print(f"ERRORS={len(errs)}")
    for e in errs[:20]:
        print("  ", e)
    if undef:
        print("UNDEFINED:")
        for kind, key in undef:
            print(f"   {kind}: {key}")
    print("PDF_EXISTS=", os.path.exists(PDF))
    if os.path.exists(PDF):
        h = hashlib.sha256(open(PDF, "rb").read()).hexdigest()
        print(f"SHA256={h}")
        print(f"SIZE={os.path.getsize(PDF)}")
        print("REPRODUCIBLE=", h == TARGET_SHA)


if __name__ == "__main__":
    main()
