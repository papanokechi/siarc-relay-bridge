# CT-S34-CHECKER-RULINGS — report

Four rulings applied to `sessions/2026-09-17/CT-R1-AUDIT/check_invariants.py`.
Every change is a **scoping or reporting** change; nothing is loosened, and
each change is visible in the printed output. 23 claims, `S34-01 … S34-23`,
all `review: "self"`.

Checker under change, final: sha256
`89d163f2c1b7a81d17429eaa5d82104000718052d899ba73d8a9b7202749f30a`.
Predecessor preserved at `refs/check_invariants.pre-S34.py`, sha256
`3e675fc52f06a1bbcfe3c0445f8e30bf701f36bc5f89b0bb01f950109291e4e4`, verified
equal to the value CT-S33 cites before the original was replaced. The file is
**untracked by git**, so nothing else would have retained it.

---

## Ruling 1 — invariant 2 scoped to the label convention  (S34-01 … S34-04)

**The cutoff was derived, not assumed, and the measurement changed the
answer.** Labelling is *not* monotone. Labels appear on 2026-05-13 (6 of 89)
and 2026-05-14 (9 of 18), then stand at **0 per cent on all nine dates**
2026-05-18, -19, -20, -22, -29, 2026-06-11, -15, -16, -18, and are universal
only from **2026-09-17** (578 of 578). The convention was tried, abandoned and
re-adopted. A cut at the first labelled date — the obvious choice — would have
left 661 unlabelled claims in scope and simply failed.

Rule applied: *the earliest date D such that every claim dated ≥ D carries a
recognised label.* On this corpus D = 2026-09-17.

**The cutoff is pinned, not recomputed — deliberately.** A cutoff derived at
run time from the same claims it then judges is self-fulfilling: no claim on
or after it could ever be unlabelled, so invariant 2 could never fail. The
checker recomputes the derived value and **reports** disagreement without
acting on it, which catches drift without disarming the invariant.

**A contradiction in the earlier wording, now reconciled.** The checker said
"0 of them do carry a label" while `measure.py` found 15. Neither was wrong:
`measure.py` counts any truthy `label`, the checker counts only *recognised*
labels, and the 15 are 14 `PROCEED` + 1 `REFINED` from the abandoned first
attempt. Both numbers are now printed, with the difference explained.

Older claims are reported as a count with their range: **3488 claims,
2026-04-22 .. 2026-06-18, OUT OF SCOPE.** Not judged, not retrofitted.

## Ruling 2 — invariant 1(b) split three ways  (S34-05 … S34-10)

All 84 reused ids are accounted for, each under exactly one heading:

| heading | count | treatment |
|---|---|---|
| 1(b)(i) deposit mirrors | 15 | exempt by **path** pattern `[\\/]deposit[\\/]`, each listed with the path that matched |
| 1(b)(ii) session-local counters | 152 ids (10 recurring) | unique **within** a session; global recurrence is what a counter is for |
| 1(b)(i) unexempted | **59** | **FAIL**, reported in full |
| 1(b)(iii) idless | 2641 claims | own printed line: *"This is a hole, not a pass."* |

**The 59 were measured a second, differently implemented way.** By claim-text
identity the 84 split 74 identical-text / 10 different-text. The two
classifications cross cleanly: the 10 different-text ids **are** the
session-local counters (`C1` means six different things in six sessions),
which is precisely why per-session scoping is right for them; and all 59
unexempted ids carry **identical** text everywhere — aggregator and verifier
restatements (`THEORY-FLEET/AGGREGATOR` restating `H1…H6`, a verifier
restating `CC-MEDIAN-RESURGENCE` ids, sibling `R1-ROUTE-F-*` sessions).

**Text identity was deliberately not made an exemption.** Accepting it would
absorb all 59 without a ruling — loosening, not scoping. They are reported in
full, with the identical-text finding stated beside them, so the convention can
be ruled on. Mutant **M5** injects exactly that loosening and is caught.

Zero ids duplicate within a single file.

## Ruling 3 — the unreadable claim left unrepaired  (S34-11)

`sessions/2026-04-30/SIARC-COHERENCE-AUDIT/claims.jsonl:3`, a raw LaTeX
`\(2,2\)` inside a JSON string, is tagged **KNOWN HOLE** with the ruling that
left it, and identified by path and line. The list is **exact, not an
amnesty**: a different damaged line is reported as **NEW DAMAGE**. Mutant
**M6** turns the list into a blanket amnesty and is caught.

## Ruling 4 — SCOPE removed from ROOTS  (S34-12, S34-13, S34-20)

`C:\LocalWork\SCOPE` is out of `ROOTS` and named in `EXCLUDE` with **three
printed reasons**: it is written mid-run by other processes, so a verdict over
it has a race in it; Window B's status is unsettled; and it collides with the
repository tree by session number. The input fingerprint is kept.

`NOTE-CROSS-TREE-COLLISIONS.md` (sha256 `076cefa382231a1e…`) records both
collisions — `CT-S32` = `CT-S32-LD2-ORDINARY-LOCUS` / `CT-S32-PACKET-SEALED`,
`CT-S33` = `CT-S33-CHECKER-SCOPE` / `CT-S33-COLDREAD-OUTPUT` — renames
nothing, and adopts `SC-Sn` for future SCOPE sessions. The ambiguity reaches
the **claim ids**, since both trees mint `S<n>-<nn>`.

**But the race is not confined to SCOPE.** Two runs of the checker this
session returned different fingerprints: `a37d6601e12fc9f0…` over 445 files
and 4066 claims, and a later run `f5947419b462bccb…` over 447. The difference
is this session's own claims (19 at the time of that run) plus **14 in
`sessions/2026-09-17/CT-S35-CTV17-ITEM6/`, written by another process at 22:29
while this session ran**. The difference was *attributed* before being called
a disagreement — which is what the fingerprint was added for — but removing
SCOPE does not make the repository tree quiet. That file was read by the
checker and not otherwise touched.

**Window ownership** (`NOTE-WINDOW-OWNERSHIP.md`, sha256 `e06649bc8fbdf685…`,
S34-22, S34-23). This is the *second* false disagreement from concurrent
writes — the first was `CT-S30-PACKET-BUILD` growing by three claims mid-run,
the same liveness that put four intrusion files into a packet folder. Ruling
recorded: **one window owns a tree at a time, ownership is by tree not by
folder, a non-owning window must not create a session folder, reading is
always permitted.** It cannot be enforced; it makes concurrent writing
*visible and attributable*.

The fingerprint only reconciles two runs if **both** printed one, so three
controls now fix that: it is emitted before any invariant is judged, on
failing runs and over an empty corpus alike, as exactly one full 64-hex value.
A differing count with a differing fingerprint is a **different input**, not a
contradiction; only a differing count with an *identical* fingerprint is a
real disagreement between implementations.

---

## Controls  (S34-03, S34-09, S34-14)

`outputs/verify_rulings.out.txt` sha256 `ff48ef84f93b1a57…` — **23/23 PASS**.
Each patches `ROOTS`/`EXCLUDE` onto a synthetic corpus, runs the checker as a
subprocess, and asserts the real checker byte-identical afterwards.

- unlabelled claim dated **2026-09-16** → hole, exit 0
- unlabelled claim dated **2026-09-18** → **FAIL 2**, exit 1
- unlabelled claim dated **2026-09-17** (on the cutoff) → **FAIL 2** (inclusive)
- cross-session collision, different text → **FAIL 1(b)(i)**, named a true collision
- counter reused **within** one session → **FAIL 1(b)(ii)**
- same counter in two sessions → exempt, exit 0
- mirror **at** `deposit/` → exempt and listed with the matching path
- mirror **not** at `deposit/` → still reported; identical text is no exemption
- idless claim → its own line, called a hole
- new damage → **NEW DAMAGE**, not absorbed by the known-hole entry
- SCOPE absent from roots, present in EXCLUDE with three reasons, on the holes line, fingerprint kept
- fingerprint printed on a **failing** run, and over an **empty** corpus ("over 0 file(s) read"), exactly one full 64-hex value

`outputs/mutants.out.txt` sha256 `de4beffd2b37a6ac…` — **7/7 CAUGHT**, checker
byte-identical. Each arm injects the loosening one ruling forbids: M1 cutoff
moved a day later; M2 counter pattern widened to any id; M3 within-session
threshold raised; M4 mirror pattern unanchored; M5 text identity accepted;
M6 amnesty; M7 idless line silenced.

`outputs/emit_mutants.out.txt` sha256 `890e95227dafdc8e…` — **8/8 CAUGHT**,
`claims.jsonl` byte-identical after every arm. Byte-identity is the condition
that separates a pre-write check from a post-write one.

## Four instrument defects, all found by the arms  (S34-15, S34-19, S34-21)

1. **All 7 checker arms reported MISSED** — the copied harness resolved `HERE`
   to the temp directory and died on a missing `refs/` file before judging
   anything. A two-condition arm testing only *refused* would have scored
   **7/7 CAUGHT on a harness that never ran a control**.
2. **M1 MISSED legitimately**: the harness *pinned* the cutoff and refused the
   mutant structurally rather than letting the boundary control fail. It now
   derives the cutoff from the source under test.
3. **E5 and E4 refused for the wrong reason** — E5's injected evidence was
   below the length floor, so the length assertion fired instead of the hash
   assertion; E4's replacement id collided with a real one, so uniqueness
   fired instead of contiguity. Both repaired.
4. **A citation inside this session went stale.** `measure.out.txt` is built
   by *walking* the corpus, and the corpus now contains this session's own
   claims, so re-running `measure.py` after emission changed it and left three
   claims citing a digest resolving to nothing. Caught by
   `verify_claim_citations.py`, which asserts the file on disk still matches
   what the claims cite. Ordering fixed: measure, emit, never measure again.

## What I could not establish

- **Whether the 59 restatements warrant an exemption.** They are identical-text
  aggregator/verifier copies, but no path pattern distinguishes them, and
  inventing one is a ruling, not a measurement. Left FAILING.
- **Whether the 2641 idless claims should ever carry ids.** Reported as a hole.
- **Anything about the excluded trees.** `C:\LocalWork\SCOPE` is not walked;
  `CT-S31-COLDREAD-ROWS` is excluded by name under a standing instruction.
- **A stable verdict over a live tree.** Mitigated by the fingerprint, not
  solved; see S34-20.

## Status

`outputs/rulings_pass.out.txt` sha256 `7ae9550ef6f08b5b…` — **exit 1**, 4066
claims in 442 files, one root. Passing: 0, 1(a), 1(b)(ii), 2, 3, 4. Failing:
**1(b)(i)** with 59, and **5** with 9 non-JSONL files.
`outputs/post_emit_pass.out.txt` sha256 `8917f3a073655f71…` is the later run
including this session's own claims (447 files).

Down from three failures to two, and the remaining two are **information about
the record**, not defects in the checker and not to be repaired by loosening
it. All 23 claims are `self` with the contamination note; none is
deposit-eligible.

`claims.jsonl` sha256
`23c87e80ce4a2ccb5719b83257fe65ebbbc219f698e61f6efc5efe5a32efdf07`, 23 claims:
4 PROVEN / 7 VERIFIED / 8 STRUCTURAL / 4 INSPECTED. `verify_claim_citations.py`
resolves all **33** digests cited inside them against files on disk, and
`verify_report.py` resolves all cited here.
