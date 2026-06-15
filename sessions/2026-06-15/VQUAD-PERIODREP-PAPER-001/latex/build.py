#!/usr/bin/env python
r"""Build script for VQUAD-PERIODREP-PAPER-001.

Concatenates preamble.tex + sections/section-*.md (LaTeX-body fragments, in order)
+ \end{document}, into latex/vquad-periodrep-paper.tex, then runs pdflatex twice
(byte-reproducible: SOURCE_DATE_EPOCH must be set by the caller).

Usage:  python build.py            # full build (all sections present)
Outputs: latex/vquad-periodrep-paper.tex, latex/vquad-periodrep-paper.pdf
Also writes the concatenated markdown view: vquad-periodrep-paper.md (Stage 3.1).
"""
import os, subprocess, sys, glob, re

HERE = os.path.dirname(os.path.abspath(__file__))
SLOT = os.path.dirname(HERE)
SEC  = os.path.join(SLOT, "sections")
PDFLATEX = r"C:\Users\shkub\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe"

# ordered section files (body fragments). references LAST.
ORDER = [f"section-{i}.md" for i in range(1, 9)] + ["section-9-references.md"]

def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()

def main():
    preamble = read(os.path.join(HERE, "preamble.tex"))
    bodies = []
    for name in ORDER:
        p = os.path.join(SEC, name)
        if os.path.exists(p):
            bodies.append(f"% ===== {name} =====\n" + read(p).rstrip() + "\n")
        else:
            print(f"[skip] missing {name}")
    doc = preamble.rstrip() + "\n\n" + "\n".join(bodies) + "\n\\end{document}\n"

    tex = os.path.join(HERE, "vquad-periodrep-paper.tex")
    with open(tex, "w", encoding="utf-8") as f:
        f.write(doc)
    # Stage 3.1 concatenated markdown view (sections only, no preamble)
    md = "\n\n".join(read(os.path.join(SEC, n)) for n in ORDER if os.path.exists(os.path.join(SEC, n)))
    with open(os.path.join(SLOT, "vquad-periodrep-paper.md"), "w", encoding="utf-8") as f:
        f.write(md)

    env = dict(os.environ)
    env.setdefault("SOURCE_DATE_EPOCH", "1718409600")  # 2024-06-15 fixed epoch
    log = ""
    for _ in range(2):
        r = subprocess.run([PDFLATEX, "-interaction=nonstopmode", "-halt-on-error",
                            "vquad-periodrep-paper.tex"],
                           cwd=HERE, env=env, capture_output=True, text=True)
        log = r.stdout + r.stderr
    # report
    pdf = os.path.join(HERE, "vquad-periodrep-paper.pdf")
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
    print("PDF_EXISTS=", os.path.exists(pdf))

if __name__ == "__main__":
    main()
