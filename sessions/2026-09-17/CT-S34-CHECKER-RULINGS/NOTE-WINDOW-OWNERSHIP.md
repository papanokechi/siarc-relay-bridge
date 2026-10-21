# Window ownership of the writable trees

Recorded 2026-09-19 by CT-S34-CHECKER-RULINGS, after the second false
disagreement caused by concurrent writes.

## What happened, twice

1. **CT-S33 / CT-S30-PACKET-BUILD.** Two runs of the same checker minutes
   apart returned 4066 and 4069 claims. Not an implementation difference:
   `C:\LocalWork\SCOPE\CT-S30-PACKET-BUILD\claims.jsonl` grew by three claims
   between the runs. The same liveness put four intrusion files into an input
   packet during its build, one of which was destroyed by the disposal
   command before it could be read.
2. **CT-S34 / CT-S35-CTV17-ITEM6.** Two runs returned 445 and 447 files.
   14 claims arrived in `sessions/2026-09-17/CT-S35-CTV17-ITEM6/claims.jsonl`
   at 22:29:13 while CT-S34 was running. Attributed correctly, but only
   because **both runs printed a fingerprint**.

The second case is the more serious: it is inside the git repository, which
had been treated as the quiet tree.

## Ruling

**One window owns a tree at a time. Ownership is by tree, not by folder.**

| tree | owner | others may |
|---|---|---|
| `C:\LocalWork\siarc-relay-bridge` | the window holding the deposit queue | read only |
| `C:\LocalWork\SCOPE` | the window running the cold/packet work | read only |

A window that does not own a tree **must not create a session folder in it**,
which is the act that caused both incidents. Reading is always permitted;
walking for measurement is reading.

## Consequence for any verdict over a tree

A verdict over a tree the running window does not own is a verdict over a
moving target. Therefore:

1. **Print the input fingerprint on every run**, including failing runs and
   runs over an empty corpus. Two runs cannot be reconciled if one of them
   printed nothing. Three controls in `scripts/verify_rulings.py` enforce this
   (`r4a`, `r4b`, and the single-full-64-hex check).
2. **Compare fingerprints before calling any count difference a
   disagreement.** A differing count with a differing fingerprint is a
   different input, not a contradiction. Only a differing count with an
   *identical* fingerprint is a real disagreement between implementations.
3. **Never batch an inspection with a destructive action.** The listing
   arrives after the deletion it should have governed; that is how the
   third intrusion file was lost.

## What this does not do

It does not stop a second window writing — nothing here can enforce that. It
makes the writing **visible and attributable**, and it names who should have
been writing, so the next occurrence is a breach of a recorded convention
rather than an unexplained number.

## Standing exclusions, unchanged

`C:\LocalWork\SCOPE` is not in `ROOTS`. `C:\LocalWork\SCOPE\CT-S31-COLDREAD-ROWS`
is excluded by name under a standing instruction not to read, write, list or
delete it.
