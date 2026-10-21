
- **Never pass markdown through a double-quoted PowerShell string.** The
  backtick is PowerShell's escape character, so a code span opener followed by
  a, b, e, f, n, r, t, v or 0 is silently consumed. The damage is selective:
  most backticks in a document survive, and their survival reads as evidence
  that nothing is wrong. Write the text to a file and run the file. The rule is
  not "escape the backticks" - enumerating the affected letters is the
  coverage-list mistake this file already warns about. (R33.1, R33.2)
- **Route every write to a recorded file through an appender that refuses
  control characters**, and give that appender a two-sided control: one input
  it must reject, one it must accept. A control that fails for the same reason
  as the run it is controlling certifies nothing. (R33.1)
