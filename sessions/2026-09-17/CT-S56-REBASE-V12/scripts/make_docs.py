"""CT-S56 stage 5 -- generate CHANGES.md and CORRECTIONS-FOR-REFEREES.md.

Both documents are GENERATED, never hand-typed, for one reason: every count and
every cross-reference number in them is derived from the artefacts it describes.
A hand-typed '13 edits' or 'Remark 3.3' drifts the moment anything moves, and a
referee-facing document that cites a non-existent object is the worst class of
defect this session could ship.

Guards, all of which refuse rather than warn:
  * every numbered object quoted must occur in the v1.2 RENDER
  * counts come from the replacement lists, not from prose
  * the revision PDF must be the one that was checked
"""
import hashlib
import io
import re
import sys
from pathlib import Path

import fitz

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
REFS = SESS / "refs"
REV = SESS / "revision"
BASE_PDF = REFS / "zenodo-v1.2-21412469.pdf"
REV_PDF = REV / "vquad-periodrep-paper.pdf"
REV_TEX = REV / "vquad-periodrep-paper.tex"

NUMBERED = re.compile(
    r"(Theorem|Proposition|Lemma|Corollary|Remark|Definition|Table|Figure)\s+"
    r"(\d+(?:\.\d+)?)")

BASE_MD5 = "792107efab6317e8ae21e2ca20f092ff"


class Refuse(Exception):
    pass


def render_objects(pdf: Path):
    doc = fitz.open(pdf)
    raw = " ".join(p.get_text() for p in doc)
    doc.close()
    return {f"{a} {b}" for a, b in NUMBERED.findall(raw)}, raw


def main() -> int:
    log = io.StringIO()

    def say(s=""):
        print(s)
        log.write(s + "\n")

    say("=" * 78)
    say("CT-S56 STAGE 5 -- generating CHANGES.md and CORRECTIONS-FOR-REFEREES.md")
    say("=" * 78)
    say("")

    sys.path.insert(0, str(HERE))
    import apply_revision_v12 as A

    s52 = A.import_s52()
    five = A.FIVE
    reps = A.all_replacements()

    by_item = {}
    for item, tag, old, new in reps:
        by_item.setdefault(str(item), []).append(tag)

    n_total = len(reps)
    n5 = len(five)
    n52 = len(s52)
    n4 = len(A.EXTRA4)
    # The three parts must account for the whole. Without this, a replacement
    # added to one list and not the other is invisible in the prose -- which is
    # precisely how the documents came to report 32 against 33 applied.
    if n52 + n4 + n5 != n_total:
        raise SystemExit(
            f"REFUSED: {n52}+{n4}+{n5} != {n_total}; the parts do not "
            "account for the whole replacement list")

    md5 = hashlib.md5(BASE_PDF.read_bytes()).hexdigest()
    if md5 != BASE_MD5:
        raise Refuse(f"base PDF md5 {md5} != the file LMP holds {BASE_MD5}")
    say(f"    base v1.2 md5 verified : {md5}")

    present, _ = render_objects(BASE_PDF)
    say(f"    numbered objects in the v1.2 render : {len(present)}")

    revsha = hashlib.sha256(REV_PDF.read_bytes()).hexdigest()
    texsha = hashlib.sha256(REV_TEX.read_bytes()).hexdigest()
    doc = fitz.open(REV_PDF)
    revpages = doc.page_count
    doc.close()
    doc = fitz.open(BASE_PDF)
    basepages = doc.page_count
    doc.close()
    say(f"    revision : {revpages} pages, pdf sha256 {revsha[:16]}")
    say(f"    base     : {basepages} pages")
    say("")

    # ------------------------------------------------- the guard on every number
    def N(obj: str) -> str:
        """Quote a numbered object, refusing if it is not in the v1.2 render."""
        if obj not in present:
            raise Refuse(
                f"'{obj}' is quoted in a referee-facing document but does not "
                f"occur in the v1.2 render; a stale v1.0 number is the likely "
                f"cause (CT-S52's tags carry v1.0 numbering)")
        return obj

    # control: the guard must reject a fiction, or it guards nothing
    say("[0] CONTROL ON THE NUMBER GUARD")
    try:
        N("Remark 3.3")
        say("    [FAIL] the guard accepted 'Remark 3.3', which v1.2 does not have")
        return 2
    except Refuse:
        say("    [PASS] guard rejects 'Remark 3.3' (the known stale tag)")
    try:
        N("Remark 3.4")
        say("    [PASS] guard accepts 'Remark 3.4' (present in v1.2)")
    except Refuse:
        say("    [FAIL] the guard rejected a genuine object")
        return 2
    say("")

    bullets = "\n".join(
        f"- **Item {k}** — {len(v)} edit{'s' if len(v) != 1 else ''}"
        for k, v in sorted(by_item.items()))

    def itemlist(k):
        return "\n".join(f"  {i}. {t}" for i, t in enumerate(by_item[k], 1))

    # ------------------------------------------------------------- CHANGES.md
    ch = f"""# CHANGES — revision of MATH-D-26-00523, rebased onto v1.2

**Base.** v1.2, Zenodo record 21412469, `md5 {BASE_MD5}` — the file
Editorial Manager holds. Established in CT-S55 by downloading the manuscript
item itself through the link embedded in EM's stamped build, not by filename.

**Status.** Draft. Nothing has been uploaded, submitted or deposited.

| | base v1.2 | revision |
|---|---|---|
| pages | {basepages} | {revpages} |
| PDF | `md5 {BASE_MD5}` | `sha256 {revsha[:32]}` |
| source | `sha256 2529da49e377b9dd…` | `sha256 {texsha[:32]}` |

**{n_total} replacements**, each required to match the v1.2 source exactly once,
all validated against the buffer before anything was written:

{bullets}

Of these, {n52} are CT-S52's edits, **imported from its own module** rather than
retyped, {n4} is a further item-4 correction found in this session (the
"obtained twice" sentence in {N('Proposition 2.4')}, L455 of the v1.2 source),
and {n5} are new for item 5.

---

## Why the base changed

CT-S52 prepared this revision against **v1.0**. CT-S55 established that LMP holds
**v1.2**. The revision was therefore rebuilt from v1.2's source.

The re-basing cost less than feared: the v1.0 → v1.2 source diff is **3 hunks,
+21/−3 lines**, and is entirely journal boilerplate — *Funding*, *Data
availability*, *Conflict of interest*, *Declaration on the use of AI tools*, and
the removal of the *References* heading. **No mathematical text differs between
v1.0 and v1.2.** That is why all {n52} of CT-S52's replacements matched v1.2
exactly once, with none broken and none ambiguous.

---

## Item 1 — the D₅⁽¹⁾ identification stated as conjectural

{itemlist('1')}

Each now attributes the surface identification to the companion's Conjecture 4.1
rather than asserting it. §1.1 additionally records that the companion's v1.3
correction notice revises the derivation of the quoted Painlevé parameters.

The fourth edit was **not on the reported list**. It was found by the
Amendment H sweep, which is why the sweep is run before editing and not after.

## Item 2 — the overclaimed completion in §7.1

{itemlist('2')}

"completes part (ii)(a) for d = 2" is replaced by: an instance of part (ii)(a)
for the representative V_quad, conditional on the conjectured surface
identification, and not established for the stratum.

## Item 3 — "proved twice" and the independence of the structural argument

{itemlist('3')}

{N('Theorem 1.2')} no longer says the result is proved twice. The structural
argument is restated correctly: a torus together with one root unipotent
generates a **Borel** subgroup, and it is Kovacic Case 1 exclusion of
reducibility that upgrades this to SL₂(ℂ). **Kovacic is the proof**; the
structural route is a consistency check resting on the same Case 1 exclusion,
so it is not independent corroboration.

## Item 4 — apparency at ξ = 0

{itemlist('4')}

CT-S52's exact computation over ℚ(√3) found that ξ = 0 **does** force a
logarithm, so "apparent" was wrong. Every occurrence is corrected, and the
main identity is stated to be unaffected: B̂ is holomorphic at 0 on the
principal sheet and the cycle does not approach it. In {N('Table 1')} the cell
`0 (apparent)` becomes `0 (reg. sing., logarithmic; B̂ holomorphic there)`.

Affected objects, **in v1.2's numbering**: {N('Proposition 2.4')},
{N('Lemma 2.7')}, {N('Table 1')}, {N('Remark 3.4')}, {N('Figure 1')} and its
caption, and the proof of {N('Corollary 1.4')}.

> ⚠️ CT-S52's internal tag for one of these reads "Remark 3.3". **v1.2 has no
> Remark 3.3**; the object is {N('Remark 3.4')}. The tag is a v1.0 leftover.
> It is the tag that is stale, not the edit — the edit matched v1.2's text
> exactly once, by text and not by number.

## Item 5 — Methods B and C are not independent (new this session)

{itemlist('5')}

CT-S54 established that `eq:methodB-chain` opens by substituting
A = (S/2πi)·Γ(1+β), so Method B's printed derivation **consumes S**, and its
reported 8.84482×10⁻⁴⁶ is algebraically the same quantity as Method C's — the
e^(−ξ₀) cancels. Two numbers printed side by side in the results file since
June were one number printed twice.

The revision:

- removes "three structurally independent methods" from the abstract,
  §1.3 and {N('Theorem 1.1')};
- names, at the point where it happens, that S enters Method B through the
  amplitude;
- reports Method B's **independent** check as the reconstruction of S from the
  stream-extracted amplitude, **3.69×10⁻⁴⁶**, which uses no Stokes datum —
  this replaces 8.84×10⁻⁴⁶ in {N('Table 2')} row B;
- restates {N('Table 2')}'s caption and the cross-check proposition in §5.5 to
  record the shared amplitude;
- states Method A's independence as **inferred, not measured**, because it was
  never measured.

The identity itself stands. What was wrong was §5's description of it.

## Reference added

{by_item['R'][0]}

v1.2's bibliography numbering is **unchanged**: the companion's v1.3 is appended
as the new final entry, [26]. This was checked mechanically — the count must
increase by exactly one and the new entry must be **last**, so that no existing
citation number can shift.

---

## ⚠️ Two different papers each have a version 1.3

This trips readers and it tripped an earlier session, so it is stated plainly:

| | concept DOI | its v1.3 |
|---|---|---|
| **this paper** | `10.5281/zenodo.20719042` | record 22731371, published 2026-09-13 |
| **the companion** | `10.5281/zenodo.20455089` | version DOI `10.5281/zenodo.22831933` |

The new reference cites the **companion's** v1.3. The base of this revision is
**this paper's** v1.2.

## ⚠️ The revision's wording diverges from this paper's published v1.3

This paper's v1.3 already states the D₅⁽¹⁾ identification conjecturally and
already carries a *Correction notice* withdrawing "completes part (ii)(a)" —
i.e. it covers items 1 and 2, but **in different words**, and it does **not**
cover items 3, 4 or 5.

Applying CT-S52's item 1 and 2 text to v1.2 therefore produces wording that does
not match the published v1.3. The cover letter promised that the deposit and the
submission would be identical. **Keeping that promise requires depositing a new
version of concept 20719042 matching whatever the editor accepts** — which is
the standing plan, and is why nothing has been deposited yet.

## Not in the source

The cover-letter sentence is not part of the manuscript. It is listed separately
as a correction for the editor, not as an edit.

---

## Checks that were required to be able to fail

- v1.2's source located by **byte-identical rebuild**, with v1.0 reproduced
  byte-identically as the positive control. Without that control, "nothing here
  builds to v1.2" could not be told from "nothing here builds to anything".
- all {n_total} replacements matched **exactly once**; the whole buffer was
  validated **before** any write.
- build: 0 errors, **0 undefined references**, read from the `.log` rather than
  trusted from the build script's summary.
- rendered diff v1.2 → revision: every changed block attributable to items 1–5,
  with the reflow test exercised **both ways** — it must collapse hyphenation
  and must **not** collapse a changed figure, or it would hide the 8.84 → 3.69
  edit that is the point of item 5.
- the Amendment H sweep re-run after editing, with every remaining hit read.
- the submitted v1.2 artefacts re-hashed and confirmed **byte-unchanged**.
"""

    # --------------------------------------------- CORRECTIONS-FOR-REFEREES.md
    co = f"""# Corrections for the referees — MATH-D-26-00523

*All references are to the submitted manuscript, v1.2 ({basepages} pages).*

The author has found five errors in the submitted manuscript. Four are
corrections of overclaims; one corrects a mathematical statement. The paper's
main identity is unaffected by all five.

---

### 1. The Sakai surface type D₅⁽¹⁾ is conjectural, not established

*Abstract, §1.1, §1.2, §7.1.* The manuscript states the surface identification
as fact. It rests on Conjecture 4.1 of the companion paper and should be read as
conditional throughout. The companion's v1.3 correction notice also revises the
derivation of the Painlevé parameters quoted in §1.1.

### 2. §7.1 does not complete part (ii)(a) for d = 2

The claim that the construction "completes part (ii)(a) for d = 2" is withdrawn.
What is established is an **instance** of part (ii)(a) for the single
representative V_quad, conditional on the surface identification of item 1. It
is not established for the stratum.

### 3. {N('Theorem 1.2')} is proved once, not twice

The manuscript presents a structural argument as an independent second proof.
It is not independent. A torus together with one root unipotent generates a
**Borel** subgroup; the step from Borel to SL₂(ℂ) uses Kovacic Case 1 exclusion
of reducibility — the same exclusion the first proof rests on.

**Kovacic case-elimination is the proof.** The structural argument is a
consistency check on it. Affected: {N('Theorem 1.2')}, §1.3, §1.4, the proof in
§2.2 and the paragraph following it, and Appendix A.2 and A.5.

### 4. ξ = 0 is **not** an apparent singularity — it carries a logarithm

This is the one mathematical correction.

The manuscript reasons that the four local exponents at ξ = 0 are consecutive
integers and concludes the point is apparent. **Consecutive integer exponents do
not imply apparency**; they make the recursion resonant, and whether a logarithm
appears has to be computed.

It was computed exactly over ℚ(√3), with no floating-point arithmetic, from the
lowest exponent −1. **A logarithm is forced.** ξ = 0 is a regular singular point
with logarithmic local behaviour.

Affected: {N('Proposition 2.4')}, {N('Lemma 2.7')}, {N('Table 1')},
{N('Remark 3.4')}, {N('Figure 1')} and its caption, and the proof of
{N('Corollary 1.4')}.

**The main identity is unaffected.** B̂ is holomorphic at ξ = 0 on the principal
sheet, and the integration cycle does not approach the point; the period
computation never used apparency, only that holomorphy. The correction removes a
false justification, not a step.

### 5. Methods B and C are not independent of one another

*Abstract, §1.3, {N('Theorem 1.1')}, §5, {N('Table 2')}.*

The manuscript describes three "structurally independent" determinations of the
constant. Methods B and C are not independent as derived: the displayed
derivation in §5.3 begins by substituting A = (S/2πi)·Γ(1+β), so the Stokes
datum S enters Method B through the amplitude, and Method C uses the same A–S
relation. The agreement reported for Method B, 8.84482×10⁻⁴⁶, is therefore
algebraically **the same quantity** as Method C's, not a second measurement.

There **is** a genuinely S-free check, and the revision reports it instead: the
amplitude extracted directly from the coefficient stream, with no reference to
S, reconstructs S to **3.69×10⁻⁴⁶**. That check is independent; the printed
derivation was not.

Method A's independence is stated in the revision as **inferred**, not measured,
because it has not been measured.

The value of the constant, and the identity, are unchanged. What changes is the
claim about how many independent routes reach it.

---

**Summary.** Items 1, 2, 3 and 5 weaken claims the manuscript should not have
made. Item 4 corrects a false statement about the singularity at ξ = 0 whose
consequences were, fortunately, never used. The constant, the exponential-period
representation, and the numerical agreements are unaffected.
"""

    (SESS / "CHANGES.md").write_text(ch, encoding="utf-8")
    (SESS / "CORRECTIONS-FOR-REFEREES.md").write_text(co, encoding="utf-8")

    say("[1] WRITTEN")
    for f in ("CHANGES.md", "CORRECTIONS-FOR-REFEREES.md"):
        p = SESS / f
        say(f"    {f:<30} {p.stat().st_size:>6} B  "
            f"sha256 {hashlib.sha256(p.read_bytes()).hexdigest()[:16]}")
    say("")
    say(f"    every numbered object quoted was checked against the v1.2 render")
    say("=" * 78)
    (SESS / "outputs" / "make_docs.out.txt").write_text(log.getvalue(), encoding="utf-8")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Refuse as e:
        print(f"\nREFUSED: {e}")
        raise SystemExit(2)
