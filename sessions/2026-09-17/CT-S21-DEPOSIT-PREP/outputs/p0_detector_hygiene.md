
---

## Detector hygiene — two lines

Both from `S21-35`/`S21-36`, where the scanner written to catch escape damage
carried both defects at once.

- **A detector's coverage list is itself an unchecked assumption.** The escape
  scanner tested `\r \a \v \f` and omitted `\t` and `\b` — in a Painleve
  document full of `\theta` and `\beta`. Nothing flagged the omission, because a
  detector reports only on what it was told to look for.

- **A guard added to suppress false positives can suppress exactly the hits that
  matter.** Restricting the scan to line starts cut a real 4 down to a reported
  2; the survivors were the mangled sites inside the deposit object. This is the
  seventh amendment's *cannot fire* shape appearing inside the detector written
  to catch that shape.
