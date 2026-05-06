# JTNB Editorial Policy Snapshot (2026-05-06)

**Purpose:** Anchor the JTNB editorial-policy claims used in
`sicf_decision.md` STEP 3 binding-window section.

**Fetched (this session):** 2026-05-06 (W20-Wed agent timezone JST).

**URLs queried:**
- `https://jtnb.centre-mersenne.org/` — main page (originality clause)
- `https://jtnb.centre-mersenne.org/page/instructions-to-authors/` — empty
  rendered content (no published instructions visible to the agent fetcher)
- `https://jtnb.centre-mersenne.org/page/instructions-aux-auteurs/` — empty
  rendered content (French version, same blank result)
- `https://jtnb.centre-mersenne.org/page/legal-notice_en/` — credits and
  legal notices (publisher = Société Arithmétique de Bordeaux; managing
  editor = Denis Benois)
- `https://jtnb.centre-mersenne.org/page/contact/` — contact info (Cyril
  Mauvillain, Institut de Mathématiques de Bordeaux)

---

## §A — Verbatim originality clause (jtnb.centre-mersenne.org root page)

> The Journal de Théorie des Nombres de Bordeaux publishes original papers
> on number theory and related topics (not published elsewhere).

> The Journal continues the "Séminaire de Théorie des Nombres" 1969-1989,
> whose volumes are consultable on the german server DigiZeitschriften.

> During its first years (1989-1992 : volumes 1 to 4), the publication was
> called "Séminaire de Théorie des Nombres de Bordeaux, deuxième série"
> before taking on the present title, which is better suited to reality.
> The lectures given in the Bordeaux seminar gradually disappear, replaced
> by articles reveiwed by the editorial board.

## §B — Publisher metadata (legal-notice_en)

> Publisher: Société Arithmétique de Bordeaux (SAB)
> 351, cours de la Libération
> F 33 405 TALENCE France
> Association loi 1901, SIRET number 521 399 881 00015 registered on
> 24/04/2004 BY INSEE Aquitaine, France.
> Tel. +33 (0)5 57 57 10 10
> Managing Editor: Denis Benois

> Hosting: GRICAD Joint Service Unit n°3758 (Centre National de la
> Recherche Scientifique-Université Grenoble Alpes), 700 Avenue Centrale,
> 38400 Saint-Martin-d'Hères France.

## §C — Contact (page/contact)

> Mr. Cyril Mauvillain
> Journal de Théorie des Nombres de Bordeaux
> Institut de Mathématiques de Bordeaux
> Université de Bordeaux
> 351, cours de la Libération
> F-33405 TALENCE Cedex
> jtnb@math.u-bordeaux.fr

## §D — Instructions-to-Authors page

The pages
- `https://jtnb.centre-mersenne.org/page/instructions-to-authors/`
- `https://jtnb.centre-mersenne.org/page/instructions-aux-auteurs/`

both returned a rendered body containing only the standard navigation
chrome (logo, browse-issues link, language switcher, accessibility note,
contact link, ISSN line). No author-instructions text, no submission
policy, no withdraw-and-resubmit window, no resubmission policy of any
kind was returned in the rendered HTML.

This is consistent with three possibilities (none verifiable in-session):

1. The page is intentionally blank; submission instructions are conveyed
   directly by the editorial board in private correspondence.
2. The page contents are loaded via JavaScript / SPA and not visible to
   the agent's `fetch_webpage` HTML scraper.
3. The page is genuinely under construction.

## §E — Implication for relay-049 STEP 3 binding-window analysis

There is **no published JTNB editorial-board "withdraw-and-resubmit
window" policy** accessible to this session. The relay-049 prompt
language ("JTNB withdraw-and-resubmit clock has a finite window")
therefore reflects an operator-conceptual framing, not a journal-imposed
deadline.

The only published constraint with submission-window semantics is the
originality clause in §A: a substantially-identical paper cannot be
re-submitted to JTNB after rejection (would violate "not published
elsewhere" if it were also under submission elsewhere; would violate
the implicit "not previously rejected by JTNB" if resubmitted in
unchanged form). This constraint is permanent, not clock-bounded.

Under the current verdict state (RECEIVED_NEGATIVE 2026-05-06, hard
reject — see `handoff.md` operator paste), the operative window is
**operator-conceptual, defined by SICF-roadmap freshness** rather than
by JTNB editorial policy. The 30-day estimate in
`sicf_options_scoring_matrix.json` `binding_window_note` is the agent's
conservative choice (4 fatals enumerated 2026-05-05; restructure
dispatch within 30 days keeps fatal-fix mental model intact and
avoids needing a fresh SICF re-run before resubmission).

---

## End of jtnb_policy_snapshot.md
