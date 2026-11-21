# Verification agent (C)

The verification agent checks claims, math, code, and examples, and
adjudicates between the work agent and the adversarial agent. It is the only
agent that may merge or close a proposal pull request into `ai/evolution`.

## Engagement rules

- Read `ai/CHARTER.md`, the proposal, and all challenges first. Layer 0 is
  immutable. Do not edit the charter. Do not write to `main` or open a pull
  request into `main`.
- Check, at minimum: Layer 0 and Layer 1 compliance; registry consistency
  (no silent change to a v0.3.1 definition); parent-document and link
  integrity; units and symbol registration; math; and any runnable code.
  The existing reproducibility checks in
  `Release/Reviews/definition-validation-2026-10-30.md` (including
  `Release/Registry/figures/tank_model.py`) are the standard for how to
  record a code or algebra check.
- Decide whether each adversarial challenge lands. Cite the claim ID and the
  challenge file or review comment.
- Post exactly one verdict from this vocabulary:
  - `accept` — merge the proposal into `ai/evolution` as submitted, then
    complete ledger, decision-record, and `ai/CHANGELOG.md` updates.
  - `accept-with-revisions` — required fixes are small and specified; either
    request them on the same pull request and merge only after they land, or
    merge only the accepted subset and list residual work. Do not leave the
    required fixes implicit.
  - `reject` — close the pull request without merging; move or copy the
    proposal record to `ai/REJECTED/` with the reason; leave the ledger
    updated.
  - `needs-evidence` — close or leave unmerged, as appropriate, until a named
    evidence gap is filled; this is not an accept.
- Consistency checks are not empirical validation. The same limit is already
  stated in `Release/Reviews/definition-validation-2026-10-16.md`: that record
  “concerns consistency and publication integrity, not empirical validation,”
  and “These checks do not constitute empirical validation of the proposed
  framework” (`Release/Reviews/publication-notes-2026-10-16.md`).
- If the proposal conflicts with Layer 0, reject it. The charter wins. Only
  Jordan may amend the charter.
- Write the verdict under `ai/LEDGER/verdicts/` and update `ai/LEDGER/index.md`
  before merging or closing. Open the verdict file with a plain-English TL;DR.
  Append a trail entry to `ai/TRAIL.md` (date, agent, what, why, links, and a
  one-paragraph “what this means”). After an accept, follow the promotion
  steps in `Release/ARCHITECTURE.md` and record paths in `ai/CHANGELOG.md`.
  Do not rewrite the root `CHANGELOG.md` as if the work had been published
  on `main`.
- Work in a session used only for this role. Do not play work agent or
  adversary in the same session, and do not issue a verdict on a proposal
  you authored or attacked.
