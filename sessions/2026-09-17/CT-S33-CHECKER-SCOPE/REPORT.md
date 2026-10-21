# CT-S33-CHECKER-SCOPE — widening the corpus invariant checker

**Session** CT-S33-CHECKER-SCOPE · 2026-09-19 · repository `siarc-relay-bridge`
**Review label** every claim in this session is `self`, with review_note
*"contaminated re-derivation; prior treatment of the same operator was in
context"*. Nothing here is deposit-eligible.
**Claims** `claims.jsonl`, 20 claims S33-01…S33-20, sha256 `690be5c0cb694e73…`,
14859 B. 3 PROVEN / 7 VERIFIED / 4 STRUCTURAL / 6 INSPECTED.

---

## 1. The finding

`check_invariants.py` rooted at `parents[1]`, i.e. `sessions/2026-09-17`, while
its docstring read *"Per-round invariant check over the whole session corpus"*.
It reached **30 of 447** `claims.jsonl` files — 6.7 per cent. Every
`INVARIANTS OK` it printed was a statement about `sessions/2026-09-17` and
nothing else. **[S33-01, PROVEN]**

The predecessor is preserved unmodified at
`refs/check_invariants.pre-S33.py`, sha256 `4982602cc43153f9…`, 4052 B. It was
**untracked by git** (`git status` → `??`), contrary to the assumption that
edits would be reviewable through history; the copy was taken and hash-verified
before the overwrite. **[S33-12, VERIFIED]**

## 2. The remedy, as ruled

Explicit `ROOTS` and `EXCLUDE` constants, both **printed on every run**.
Re-pointing `ROOT` was rejected (widens silently); moving folders was rejected
(rewrites paths that claims already cite). **[S33-02, STRUCTURAL]**

```
ROOTS   = repository root, C:\LocalWork\SCOPE
EXCLUDE = C:\LocalWork\SCOPE\CT-S31-COLDREAD-ROWS   (operator stand-down)
```

The docstring now names both constants and records the historical defect
verbatim instead of asserting a coverage the code lacks. The stand-down is a
**printed** hole: pruned in `os.walk`'s `dirnames` so the folder is never
listed, and named on the closing `holes in that verdict:` line. Lifting it is a
one-line edit. **[S33-18, STRUCTURAL]**

Two further repairs were forced by the widening:

* The predecessor read plain `utf-8` and called `sys.exit(2)` on the first
  parse error. Under the widened roots its first error is a **BOM** at
  `sessions/2026-04-22/H017-SIGN-A2-TRANS/claims.jsonl:1`, which sorts ahead of
  every other offending file — a naive widening would have exited 2 having
  checked no invariant at all. Measured by replaying that exact logic, not
  inferred. **[S33-16, PROVEN]**
* Non-JSONL files are now read anyway and reported under a new invariant 5,
  rather than being refused. Refusing them would have reproduced the very
  coverage gap being repaired.

## 3. The widened pass — run once, deliberately

`outputs/widened_pass.out.txt`, sha256 `2aab4ca9b9d17560…`, exit 1.
**4095 claims in 444 contributing files**, input fingerprint
`7f7e3d1a58ba162b…` over 447 files read.

| invariant | result |
|---|---|
| 0 roots exist | **ok** |
| 1(a) no PROVEN on `file_inspection` | **ok** |
| 1(b) claim_id unique | **FAIL — 84 reused ids** |
| 2 exactly one recognised label | **FAIL — 3488 claims** |
| 3 review ⇒ review_note | **ok** |
| 4 review ∈ {self,cold,lean} | **ok** |
| 5 plain JSONL, UTF-8, no BOM | **FAIL — 9 files** |

No invariant was loosened. The failures are information about the older record.

**Invariant 2 — 3488 claims.** 3473 carry no `label` at all; 14 are `PROCEED`;
1 is `REFINED`. Older sessions predate the five-label convention. **[S33-04]**

**Invariant 1(b) — 84 ids, two kinds it does not distinguish.** (i) Per-session
local counters: `C1`…`C9` reused independently by six or more sessions — a
naming convention, not a collision of distinct claims. (ii) Deposit mirrors:
`DELTA-FREDHOLM-ORDER/deposit/p0/claims.jsonl` carries the same nine `DF-*`
ids as `DELTA-FREDHOLM-P0/claims.jsonl`. A mirror is not obviously a fault.
Neither kind was visible under the narrow root. **[S33-05, STRUCTURAL]**
2641 of 4095 claims — 64.9 per cent — carry no `claim_id` at all and are
outside 1(b) entirely; the checker now prints this instead of collapsing them
to a `None` key. **[S33-06]** Three `claims.jsonl` files are zero bytes
(`TRIAGE-UNSOLVED-3`, `CHANNEL-THEORY-OUTLINE`, `SIARC-MASTER-V0`), accounting
exactly for 447 walked minus 444 contributing. Reported, not a failure.
**[S33-15]**

## 4. The unparseable lines — the truncation hypothesis is not supported

`outputs/unparseable.out.txt`, sha256 `9a9d4d68618e386d…`, 6/6 controls.
**51 lines across 9 files**, and **exactly one claim in the corpus is
unreadable**: **[S33-07, PROVEN]**

| kind | files | lines | claims lost |
|---|---|---|---|
| UTF-8 BOM ahead of valid JSON | 5 | 5 | 0 |
| whole valid JSON array, wrong container | 3 | 45 | 0 |
| genuinely damaged | 1 | 1 | **1** |

The count moved 46 → 51 because the earlier reader opened files with
`utf-8-sig`, which silently absorbs a BOM: those five were being repaired in the
reading, not counted. **[S33-08]**

The single damaged line is `sessions/2026-04-30/SIARC-COHERENCE-AUDIT/
claims.jsonl:3`, 350 B — raw LaTeX `\(2,2\)` inside a JSON string. **Not
repaired**; reported for the operator. **[S33-09, INSPECTED]**

## 5. Controls

All can fail, and three did during the session.

**On the checker** — `outputs/verify_checker.out.txt`, sha256 `a45558fb1319faca…`,
**20/20 PASS**. A clean synthetic corpus exits 0 with `INVARIANTS OK`; nine
separately injected defects (reused id, bad label, review without note, bad
review value, PROVEN on `file_inspection`, BOM, JSON array, bad escape,
unhonoured exclusion) each produce the corresponding named failure, and in the
BOM and array cases the claims behind them are still counted. The real checker
is asserted byte-identical afterwards. The three real failures are therefore
caused by the corpus, not by the checker. **[S33-17]**

**On the emitter** — `outputs/mutants.out.txt`, sha256 `61ff28e172aafa37…`,
**8/8 CAUGHT**, `claims.jsonl` byte-identical throughout. Each arm requires
three conditions together: refused; refused *for the injected reason*; artefact
**byte-identical**. The first two alone are what CT-S28 defect 6.3 and CT-S32
arm M6 both satisfied while still corrupting the artefact.

**Recount, separate invocation, different implementation** —
`outputs/recount.out.txt`, sha256 `5eb4dd59b316fca1…`, **9/9 PASS**. Agrees on
4095 claims, 444 files, 3488, 84, 2641, deriving the invariant-2 total from the
label tally rather than from the failure list.

## 6. Four defects found in my own instruments

1. **A reader inventing a defect.** The first survey classified any line
   starting `{` and not ending `}` as `TRUNCATED` and reported **15 truncations
   that do not exist** — the files are pretty-printed JSON arrays. Caught by
   parsing each file *as a whole* before judging any line. Acting on it would
   have prompted repair of 15 intact claims. **[S33-10]**
2. **A control inventing a defect.** A control asserted the phrase *"the whole
   session corpus"* was absent from the new docstring, and fired on the
   historical quotation that documents the old defect. Narrowed to "exactly one
   occurrence, inside the quotation". **[S33-11]**
3. **A check that cannot fire.** The emitter asserted `"\r" not in text`, which
   is unreachable — `json.dumps` escapes CR inside every string. Replaced by
   validating the exact bytes destined for disk (`b"\r" not in blob`) followed
   by `write_bytes`, which removes newline translation from outside the
   validated object. Arm M7 exercises the replacement; against the original form
   it could not have fired. **[S33-19]**
4. **A mutant arm passing for the wrong reason.** Arm M6 first mutated the
   emitter into invalid Python; the `SyntaxError` traceback echoed the source
   line containing the arm's own reason string, so the substring test succeeded
   on a script that never ran. Arms now reject any output containing
   `SyntaxError` or `NameError`. **[S33-20]**

Items 1 and 2 are the same class as CT-S27 §9.6 (85 phantom findings from
tag-stripping). Item 3 is the constant-list problem in a new dress: a check
drawn from a space its input cannot occupy.

## 7. A live root

`C:\LocalWork\SCOPE` is written by other processes while the check runs:
`CT-S30-PACKET-BUILD/claims.jsonl` gained three claims **between two runs
minutes apart**, moving the total 4066 → 4069 and presenting as a disagreement
between two implementations that were both correct. The checker and the recount
now print a shared **input fingerprint** — sha256 of the sorted path+content
hashes — so such a difference is attributed before it is called a disagreement.
**[S33-13, VERIFIED]**

`CT-S28-LD-ORDER/claims.jsonl` is unchanged at `1347f89b7e477dcb…`.

The session-number namespace is **shared between the two roots and has
collided**: SCOPE now holds `CT-S32-PACKET-SEALED` and `CT-S33-COLDREAD-OUTPUT`
while the repository holds `CT-S32-LD2-ORDINARY-LOCUS` and
`CT-S33-CHECKER-SCOPE`. Nothing is overwritten — the trees are disjoint — but a
session cited by number alone is now ambiguous. **Not resolved unilaterally.**
**[S33-14, STRUCTURAL]**

## 8. What I could not establish

* **Whether the 84 reused ids are faults.** The per-session `C1`…`C9` counters
  and the deposit mirrors are both plausibly intended. Deciding needs the
  convention, which is an operator ruling, not a computation.
* **Whether the 3473 unlabelled claims should be labelled retrospectively.**
  Assigning a label to a claim written before the convention existed would be
  inventing evidence.
* **Whether the damaged line's original text is recoverable.** Not attempted;
  the file was not opened for writing.
* **The contents of `CT-S31-COLDREAD-ROWS`.** Excluded by the stand-down. Its
  claims, if any, are outside every number in this report.

## 9. Confirmation

Re-running the checker after this session's own claims were written: **4095
claims, 444 files**, invariants 0, 1(a), 3 and 4 still `ok` — the 20 CT-S33
claims satisfy every invariant they are subject to. Coverage before: **30
files**. After: **444**.
Checker under test: `sessions/2026-09-17/CT-R1-AUDIT/check_invariants.py`,
sha256 `3e675fc52f06a1bb…`, 11192 B.
