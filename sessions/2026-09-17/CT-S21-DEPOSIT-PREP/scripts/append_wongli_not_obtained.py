"""Record the Wong & Li II decision: NOT OBTAINED, stated explicitly.

Appends, once:
  - CT-R1-AUDIT/REFS-MANIFEST.md : a resolution block replacing the standing
    "Purchase target" framing with the NOT OBTAINED status.
  - CT-R1-AUDIT/AUDIT.md         : section R35, the narrative.
  - CT-S21-DEPOSIT-PREP/claims.jsonl : claim S21-76.

Refuses to double-append. Echoes every value it wrote; per S21-74, exit 0 is
not evidence, so read the echo.
"""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
R1 = HERE.parent / "CT-R1-AUDIT"
MANIFEST = R1 / "REFS-MANIFEST.md"
AUDIT = R1 / "AUDIT.md"
CLAIMS = HERE / "claims.jsonl"

DOI = "10.1002/sapm1992874289"
CITE = ("R. Wong and H. Li, Asymptotic Expansions for Second-Order Linear "
        "Difference Equations, II, Stud. Appl. Math. 87(4) (1992), 289-324")
MARK_M = "## Wong & Li II: NOT OBTAINED"
MARK_A = "## R35. The Wong-Li line, written rather than bought"
CLAIM_ID = "S21-76"

MANIFEST_BLOCK = f"""

{MARK_M} (decided 2026-09-19)

The purchase target recorded above was **not purchased and not obtained**. The
article is paywalled (Wiley HTTP 403); no mirror was used. Its status in this
corpus is therefore fixed, and stated rather than left implicit:

> Whether the exponent formula `s = beta_{{d-1}}/beta_d + (d-1)/2` appears in
> {CITE}, DOI `{DOI}`, was **NOT ESTABLISHED**: the article is paywalled
> (Wiley HTTP 403) and was not obtained. The contribution is stated relative to
> what was read.

| item | status |
|---|---|
| exponent `s` stated in Wong-Li II? | NOT ESTABLISHED - article not obtained |
| connection constant in closed form there? | NOT ESTABLISHED - article not obtained |
| exponent `s` derived independently here | yes, CT-S8-LITCHECK and CT-S2 |
| `r_infinity` framing depends on Wong-Li? | no - see AUDIT R35 |

The citation is retained in full, including the numeral **II** and the word
**linear**, because omitting either retrieves a different paper (`R1-61`). It
enters no `refs/` table: there is no file, so there is nothing to license.
"""

AUDIT_BLOCK = f"""

{MARK_A}

The decision framed in `CT-S21-DEPOSIT-PREP/DEPOSIT-WALKTHROUGH.md` Part B was
between buying the article and writing the NOT OBTAINED line. The line is
written. What follows is why that is not a concession.

The recommendation in B4 was, weakly, to buy, and it rested on B2's second
question: whether the connection constant is given there in closed form. That
question is not answered by this decision and is not claimed to be. What changed
is which claim depends on it. The exponent

    s = beta_(d-1)/beta_d + (d-1)/2

is derived and numerically verified in this corpus independently of any source,
so if Wong-Li states it, the exponent was never the contribution. And the
contribution actually made - that `r_infinity` is the constant classical method
sets aside in order to reach turning-point behaviour, made explicit - rests on
`Wong-Zhao section 3`, a page that is held, CC-BY, and hashed in the manifest
(`S21-32`): the substitution x_n = y_n/K_n with K_(n+1)/K_(n-1) = c_n absorbs
the product growth by construction, leaving K_0, K_1 "depending on the
particular sequence". Ibrahim-Salvy is quoted in its printed form as a statement
about the state of the art, not about the world.

So the unread source could still bear on the closed form of `K`. It cannot
reach `s`, and it cannot reach the framing. That asymmetry is the whole of the
argument, and it is why the honest line costs the record nothing.

**What must not happen is the quiet version.** An unstated gap reads as a
novelty claim, which is why the status is written into `REFS-MANIFEST.md` as a
table row per question rather than as a sentence in a report someone may not
reach. If the article is obtained later, this section is superseded, not
deleted: the two questions are already stated in the form an answer would take.
"""


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def append_once(path: Path, marker: str, block: str) -> bool:
    body = path.read_text(encoding="utf-8")
    n = body.count(marker)
    if n:
        print(f"  SKIP  {path.name}: marker already present x{n}")
        return False
    path.write_text(body + block, encoding="utf-8")
    print(f"  WROTE {path.name}: +{len(block)} chars, marker '{marker[:40]}...'")
    return True


def main() -> int:
    for p in (MANIFEST, AUDIT, CLAIMS):
        if not p.exists():
            print(f"MISSING: {p}")
            return 2

    print("append_wongli_not_obtained")
    append_once(MANIFEST, MARK_M, MANIFEST_BLOCK)
    append_once(AUDIT, MARK_A, AUDIT_BLOCK)

    existing = [json.loads(l) for l in CLAIMS.read_text(encoding="utf-8").splitlines() if l.strip()]
    if any(c["claim_id"] == CLAIM_ID for c in existing):
        print(f"  SKIP  claims.jsonl: {CLAIM_ID} already present")
    else:
        claim_text = (
            "The Wong & Li II decision is resolved as NOT OBTAINED, and the status is "
            "stated explicitly rather than left implicit. " + CITE + ", DOI " + DOI +
            ", is paywalled (Wiley HTTP 403) and was not purchased; no mirror was used. "
            "Therefore whether the exponent s = beta_(d-1)/beta_d + (d-1)/2 is already in "
            "print there, and whether the connection constant is given there in closed "
            "form, are both NOT ESTABLISHED, recorded as NOT FOUND in the sources "
            "obtained by the methods used, never as new. This costs no claim in the "
            "corpus: s is derived and numerically verified here independently, and the "
            "r_infinity framing rests on Wong-Zhao section 3, which is held and hashed "
            "(S21-32). The unread source could still bear on a closed form for the "
            "constant K; that remains open and is written as two answerable questions in "
            "REFS-MANIFEST.md rather than as prose."
        )
        rec = {
            "claim_id": CLAIM_ID,
            "task_id": "CT-S21-DEPOSIT-PREP",
            "claim": claim_text,
            "label": "INSPECTED",
            "evidence_type": "file_inspection",
            "dps": None,
            "reproducible": True,
            "script": "scripts/append_wongli_not_obtained.py",
            "output_hash": sha256(MANIFEST_BLOCK + AUDIT_BLOCK),
            "review": "self",
            "review_note": ("Operator decision, taken twice independently. No threshold was "
                            "weakened and no label was raised; the gap is recorded as a gap."),
        }
        with CLAIMS.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"  WROTE claims.jsonl: {CLAIM_ID}")

    print("\nechoed values (read these; exit 0 proves nothing -- S21-74):")
    print(f"  doi          : {DOI}")
    print(f"  citation     : {CITE}")
    print(f"  claim_id     : {CLAIM_ID}")
    print(f"  output_hash  : {sha256(MANIFEST_BLOCK + AUDIT_BLOCK)}")
    total = len([l for l in CLAIMS.read_text(encoding='utf-8').splitlines() if l.strip()])
    print(f"  claims total : {total}")
    for p, m in ((MANIFEST, MARK_M), (AUDIT, MARK_A)):
        print(f"  {p.name}: marker count {p.read_text(encoding='utf-8').count(m)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
