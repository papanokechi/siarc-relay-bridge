### R33.3 - A count that changed meaning, and a damaged file with a future (S21-67, S21-68)

Two closing items, both raised by the operator at the boundary.

**The claim count.** This round reported "66 claims" where every previous round
reported the corpus figure, which stood at 406. The operator flagged the drop
and was right to: a checker reporting a smaller number as OK is exactly this
round's defect class. It was not that. 66 is the size of
`CT-S21-DEPOSIT-PREP/claims.jsonl` alone; the corpus is **413 claims in 22
files**, which is 406 plus the seven appended since, with no duplicate id.
`check_invariants.py` prints its own scope on the first line and was never
narrowed. The defect was in the prose: a number was reused with a different
referent and without saying so. That is the same drift class as the stale hash,
one level up from the bytes, and it is worth recording precisely because the
gate was sound and the sentence was not (S21-67).

**`CT-S1-THEOREM/REPORT.md` has a future, not only a past.** R33.2 recorded the
R1-era backtick damage and left the file alone, correctly, since P0 forbids
modifying an earlier session folder. But that file reports on the theorem that
part (i) is headed for. Two destroyed code spans surviving every gate built
since means the gates were never scanning it, and the remedy at publication is
not to repair the file in place but to **regenerate the report** from its
sources and cite the regenerated one. Citing a known-damaged file because it is
the historical artefact would carry the damage forward into a deposit. Recorded
here so that whoever scopes part (i) meets this before choosing a source
(S21-68).
