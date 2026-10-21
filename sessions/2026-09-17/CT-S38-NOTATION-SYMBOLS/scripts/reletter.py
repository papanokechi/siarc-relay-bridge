#!/usr/bin/env python3
"""reletter -- apply the S38 names to theorem.tex and section1.tex.

  normalised sequence and its limit   ->  \\psi_n , \\psi_\\infty
  roots of b                          ->  \\nu_1, ..., \\nu_d

The two files need different treatment.

theorem.tex carries the deposited letter r for BOTH objects.  Its token r_1
is ambiguous in the file itself: at eq:rnrec it is the first term of the
sequence (r_0 = r_1 = 1), and in "r_1,\\dots,r_d\\in\\C the roots listed with
multiplicity" it is the first root.  A blanket r -> x substitution would
therefore be wrong, and so would a blanket r_1 -> one name.  The root phrase is
rewritten first, as a literal, and every remaining r_<sub> is then mapped by
its subscript through an explicit table.  Bare r is never touched: in this file
it also denotes the fixed r in C of Step 3, van der Put-Saito's Katz invariant
r(c), and the normal potential r(varphi).

section1.tex carries q and lambda, which are the letters being retired, and it
also carries r_n, r_infty, r_1, r_d on the RIGHT of the deposit-correspondence
footnote.  Those name the DEPOSITED symbols and must survive unchanged; only
the left-hand sides move.

The rewritten buffer is validated before anything is written to disk, so a
failed run leaves no half-renamed file behind.
"""
import hashlib
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SESS = os.path.dirname(HERE)
SRC = os.path.abspath(os.path.join(
    SESS, "..", "CT-S36-DRAFT-NOTATION"))
REFS = os.path.join(SESS, "refs")

SEQ, ROOT = r"\psi", r"\nu"

# subscript -> which object.  A subscript absent from this table is a halt,
# not a silent pass-through.
THM_SUB = {"{n-1}": SEQ, "{n-2}": SEQ, "{k-1}": SEQ, "n": SEQ, "k": SEQ,
           "0": SEQ, "1": SEQ, "i": ROOT}
R_TOKEN = re.compile(r"(?<![A-Za-z\\])r_(\{[^}]*\}|[A-Za-z0-9])")
Q_TOKEN = re.compile(r"(?<![A-Za-z\\])q_(\{[^}]*\}|\\infty|[A-Za-z0-9])")
L_TOKEN = re.compile(r"\\lambda(_(?:\{[^}]*\}|[A-Za-z0-9]))?(?![A-Za-z])")
BARE_R = re.compile(r"(?<![A-Za-z\\])r(?![A-Za-z_])")

ROOT_PHRASE = (r"r_1,\dots,r_d\in\C", r"\nu_1,\dots,\nu_d\in\C")
RINF_DEF = (r"\newcommand{\rinf}{r_\infty}",
            r"\newcommand{\psiinf}{\psi_\infty}")


def sha(b):
    return hashlib.sha256(b).hexdigest()


def read_or_fail(path):
    try:
        with open(path, "rb") as fh:
            raw = fh.read()
    except Exception as exc:
        print("READER INTEGRITY FAILED: cannot read %s (%s)" % (path, exc))
        sys.exit(4)
    return raw, raw.decode("utf-8").replace("\r\n", "\n")


def fail(msg):
    print("HALT: %s" % msg)
    print("VERDICT: RE-LETTERING REFUSED -- nothing written.")
    sys.exit(1)


def do_theorem(text):
    n_bare_before = len(BARE_R.findall(text))

    if text.count(ROOT_PHRASE[0]) != 1:
        fail("root phrase %r occurs %d times, expected 1"
             % (ROOT_PHRASE[0], text.count(ROOT_PHRASE[0])))
    text = text.replace(*ROOT_PHRASE)

    if text.count(RINF_DEF[0]) != 1:
        fail("\\rinf definition not found exactly once")
    text = text.replace(*RINF_DEF)
    n_rinf = len(re.findall(r"\\rinf(?![A-Za-z])", text))
    text = re.sub(r"\\rinf(?![A-Za-z])", r"\\psiinf", text)

    seen = {}
    unmapped = []

    def rep(m):
        sub = m.group(1)
        who = THM_SUB.get(sub)
        if who is None:
            unmapped.append(sub)
            return m.group(0)
        seen[sub] = seen.get(sub, 0) + 1
        return who + "_" + sub

    text = R_TOKEN.sub(rep, text)
    if unmapped:
        fail("subscripts with no entry in THM_SUB: %s"
             % sorted(set(unmapped)))

    n_bare_after = len(BARE_R.findall(text))
    if n_bare_after != n_bare_before:
        fail("bare r changed from %d to %d; the fixed r of Step 3, r(c) and "
             "r(varphi) must be untouched" % (n_bare_before, n_bare_after))
    return text, seen, n_rinf, n_bare_before


def do_section1(text):
    rhs = [r"q_n\leftrightarrow r_n", r"q_\infty\leftrightarrow r_\infty",
           r"\lambda_1,\dots,\lambda_d\leftrightarrow r_1,\dots,r_d"]
    for phrase in rhs:
        if phrase not in text:
            fail("deposit-correspondence phrase missing: %r" % phrase)
    keep = {p: len(re.findall(r"(?<![A-Za-z\\])" + re.escape(p)
                              + r"(?![A-Za-z])", text))
            for p in [r"r_n", r"r_\infty", r"r_1", r"r_d"]}
    n_bare_r = len(BARE_R.findall(text))

    nq = len(Q_TOKEN.findall(text))
    text = Q_TOKEN.sub(lambda m: SEQ + "_" + m.group(1), text)
    nl = len(L_TOKEN.findall(text))
    text = L_TOKEN.sub(lambda m: ROOT + (m.group(1) or ""), text)

    for p, n in keep.items():
        got = len(re.findall(r"(?<![A-Za-z\\])" + re.escape(p)
                             + r"(?![A-Za-z])", text))
        if got != n:
            fail("deposited name %s changed from %d to %d occurrences; the "
                 "footnote must name the deposit unchanged" % (p, n, got))
    if len(BARE_R.findall(text)) != n_bare_r:
        fail("bare r changed in section1.tex")
    if Q_TOKEN.search(text) or L_TOKEN.search(text):
        fail("a q_ or \\lambda token survived the rewrite")
    return text, nq, nl, keep


def main():
    os.makedirs(REFS, exist_ok=True)
    print("reletter -- S38 names: sequence %s_n / %s_\\infty, roots %s_1..%s_d"
          % (SEQ, SEQ, ROOT, ROOT))

    out = {}
    print("\n[preserve the pre-rename originals]")
    for name in ("theorem.tex", "section1.tex"):
        src = os.path.join(SRC, name)
        raw, text = read_or_fail(src)
        ref = os.path.join(REFS, name.replace(".tex", "-pre-S38.tex"))
        shutil.copyfile(src, ref)
        rraw, _ = read_or_fail(ref)
        if sha(rraw) != sha(raw):
            fail("copy of %s does not match the original" % name)
        print("  %-14s %6d B  sha256 %s" % (name, len(raw), sha(raw)))
        print("  %-14s -> refs/%s  (copy verified byte-identical)"
              % ("", os.path.basename(ref)))
        out[name] = (raw, text)

    print("\n[theorem.tex]")
    new_thm, seen, n_rinf, n_bare = do_theorem(out["theorem.tex"][1])
    print("  \\rinf -> \\psiinf                    %3d (+1 definition)"
          % n_rinf)
    for sub in sorted(seen):
        print("  r_%-8s -> %s_%-8s %3d"
              % (sub, THM_SUB[sub], sub, seen[sub]))
    print("  root phrase r_1,..,r_d\\in\\C          1")
    print("  bare r left untouched                %3d" % n_bare)

    print("\n[section1.tex]")
    new_s1, nq, nl, keep = do_section1(out["section1.tex"][1])
    print("  q_...    -> \\psi_...                 %3d" % nq)
    print("  \\lambda  -> \\nu                      %3d" % nl)
    for p in sorted(keep):
        print("  deposited %-10s preserved         %3d" % (p, keep[p]))

    # ---- pre-write validation: the buffers, not the files ----------------
    print("\n[pre-write validation]")
    checks = [
        ("theorem: no r_ token survives", not R_TOKEN.search(new_thm)),
        ("theorem: no \\rinf survives",
         not re.search(r"\\rinf(?![A-Za-z])", new_thm)),
        ("theorem: \\psiinf defined once",
         new_thm.count(RINF_DEF[1]) == 1),
        ("theorem: \\nu_i present", r"\nu_i" in new_thm),
        ("theorem: \\psi_n present", r"\psi_n" in new_thm),
        ("theorem: length within 25%% of original",
         abs(len(new_thm) - len(out["theorem.tex"][1]))
         < 0.25 * len(out["theorem.tex"][1])),
        ("section1: no q_ token survives", not Q_TOKEN.search(new_s1)),
        ("section1: no \\lambda survives", not L_TOKEN.search(new_s1)),
        ("section1: deposit footnote intact",
         r"\psi_n\leftrightarrow r_n" in new_s1
         and r"\nu_1,\dots,\nu_d\leftrightarrow r_1,\dots,r_d" in new_s1),
        ("section1: zenodo id intact", "10.5281/zenodo.19941678" in new_s1),
    ]
    nbad = 0
    for label, good in checks:
        print("  %-42s %s" % (label, "ok" if good else "FAILED"))
        nbad += 0 if good else 1
    if nbad:
        fail("%d pre-write check(s) failed" % nbad)

    print("\n[write]")
    for name, buf in (("theorem.tex", new_thm), ("section1.tex", new_s1)):
        dst = os.path.join(SESS, name)
        with open(dst, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(buf)
        back, _ = read_or_fail(dst)
        if sha(back) != sha(buf.encode("utf-8")):
            fail("read-back of %s does not match the validated buffer" % name)
        print("  %-14s %6d B  sha256 %s" % (name, len(back), sha(back)))

    print("\n  checks run    : %d" % len(checks))
    print("  checks failed : 0")
    print("  VERDICT: RE-LETTERED")
    sys.exit(0)


if __name__ == "__main__":
    main()
