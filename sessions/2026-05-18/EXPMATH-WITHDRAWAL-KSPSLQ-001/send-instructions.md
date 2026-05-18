# Send instructions — EXPMATH-WITHDRAWAL-KSPSLQ-001

**Status:** DRAFT READY. Operator to send. Do not send from the agent.

## 1. Account to send from

Send from the email account that was used as the corresponding-author address on
the original Experimental Mathematics submission (submission ID 264514392,
submitted 18 April 2026):

- **From:** `shkubo@outlook.jp` (per the corresponding-author block used on
  parallel SIARC cover letters; see e.g. `cover_letter_Z9_Casoratian_JDEA_draft.tex`
  and the R7/R5 operator quickrefs).

Using the same account as the original submission preserves authorial
continuity in the journal's records and lets the editorial office match the
request to the submission without manual lookup.

## 2. Channels — recommended belt-and-suspenders

Send the message via **both** channels in this order on the same day:

1. **Primary — ScholarOne portal messaging.**
   - URL: <https://mc.manuscriptcentral.com/uemt>
   - Open submission record 264514392 from the Author Dashboard. Use the
     "Contact Editorial Office" / "Send E-Mail to Editorial Office" feature
     attached to the submission record (this threads the message into the
     submission's history; some ScholarOne deployments also expose a direct
     "Withdraw" button on the manuscript detail page — if so, use it first,
     then paste the same text into the accompanying confirmation message).
2. **Secondary — direct email.**
   - To: the editorial-office address that appears in the 17 May 2026
     correspondence from Kaviya (extract the reply-to header). If that
     address is unavailable, fall back to the editorial-office address
     listed on the Taylor & Francis journal page
     <https://www.tandfonline.com/journals/uemt20>.
   - Paste the draft verbatim from `withdrawal-email-draft.txt`. Subject line
     as drafted.

Send via both channels because (a) the ScholarOne thread is the binding system
of record for the manuscript status, and (b) email gives an independent
written trail in the operator's own outbox.

## 3. Expected response and follow-up timing

- **Expected response.** A short confirmation message from the editorial
  office acknowledging the withdrawal and stating that the manuscript has
  been removed / closed in the system. Typical turnaround for T&F editorial
  offices is 1–3 business days; longer is not unusual.
- **Follow-up window.** If no response within **5 business days**
  (approximately 2026-05-26 if sent 2026-05-19), send one polite follow-up
  by replying in the same thread asking only for confirmation that the
  withdrawal has been processed. Do not re-state reasons or add new content.
- **One follow-up only.** Do not chase further; the in-system "Withdrawn"
  status update is the primary evidence and will appear in the ScholarOne
  dashboard regardless of whether the editorial office replies by email.

## 4. Downstream gating — do not submit elsewhere yet

The whole reason for the formal withdrawal is to eliminate
duplicate-submission risk against the destination venue's
"not under consideration elsewhere" declaration. Therefore:

> **Do NOT submit to the next venue until ONE of the following holds:**
>
> 1. A written confirmation arrives from Experimental Mathematics
>    confirming the withdrawal is complete (preferred); OR
>
> 2. **10 business days** have elapsed from the send date with no response
>    AND the ScholarOne dashboard now shows the manuscript status as
>    "Withdrawn" / removed (use the dashboard as the system of record); OR
>
> 3. **10 business days** have elapsed from the send date with no response
>    and no dashboard update — in this case, escalate (one more
>    direct-email attempt to a named editor from the masthead at
>    <https://www.tandfonline.com/journals/uemt20>) before proceeding.

The downstream relay slot **BAUSTMS-PREP-KSPSLQ-001** is gated on this
confirmation. Do not start that slot's submission step until the gate
above is satisfied.

## 5. Recordkeeping after send

When the message has been sent:

- Update `ledger.json` field `confirmation_await.send_event` with the
  send-event timestamp and the two channels used.
- When the confirmation arrives, append a `confirmation_received` block
  to `ledger.json` and bump the downstream gate to OPEN.
- If a confirmation does not arrive in 10 business days, record the
  dashboard-status snapshot in `ledger.json` field `dashboard_evidence`
  and proceed to the escalation step above.

## 6. Things to avoid in any follow-up correspondence

- Do not name the next venue.
- Do not mention prior rejection counts at this venue.
- Do not critique the journal or the corrections request.
- Do not promise not to submit to Experimental Mathematics in the future.
- Do not provide a substantive reason beyond "I have decided not to
  resubmit". The withdrawal is administrative and does not require
  justification under T&F policy at the pre-revision / returned-for-
  corrections stage.
