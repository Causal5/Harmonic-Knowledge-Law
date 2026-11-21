# Trail — landmarks for human readers

This is a chronological breadcrumb log of work on `ai/evolution`. It is
written for a human following the branch, not as a substitute for the
ledger or the charter.

Each entry has: the date (America/New_York), which agent (or setup work),
what was done, why, links to the pull request and ledger files when they
exist, and a one-paragraph plain-English “what this means” summary.

Every agent action on this branch must append an entry here, as required by
`ai/AGENTS/CYCLE.md`. Newest entries go at the top, under this introduction.

---

## 2026-11-21 — Work agent: freshwater data dictionary schema (Round 1)

- **Agent:** Work (A)
- **What:** Opened proposal branch `ai/proposal/2026-11-21-freshwater-data-dictionary` and a pull request into `ai/evolution` (URL to be added once the pull request exists) for Bite 1 of the Central Valley Temporal Mining protocol: a schema-only data dictionary at `Release/Examples/central-valley/freshwater_data_dictionary_v0.2.csv`, with four claims in `ai/LEDGER/claims/`.
- **Why:** The 16 October publication notes and protocol §14 already name the freshwater data dictionary as the immediate empirical step, and they require doing that before choosing HKL weights or collecting building anecdotes. This cycle records the required variables and separations without inventing measurements or completing source mapping.
- **Links:** `ai/PROPOSALS/2026-11-21-freshwater-data-dictionary/proposal.md`; `Release/Examples/central-valley/freshwater_data_dictionary_v0.2.csv`; claims `C-freshwater-data-dictionary-01` through `-04`; `ai/LEDGER/index.md`. PR URL pending in a follow-up trail edit on this branch.
- **What this means:** A human following this trail should see a spreadsheet of *what must be collected and kept distinct*, not a finished water study and not a claim that the framework has been tested. Official map boundaries and real data sources are still empty on purpose.

## 2026-11-21 — Setup: branch README, license notice, and this trail

- **Agent:** setup (direct commit to `ai/evolution`, not a proposal cycle)
- **What:** Rewrote `ai/README.md` as the labeled AI-evolution branch guide;
  added a short banner at the top of the root `README.md` on this branch
  only; recorded the AGPL-3 license and a commercial-licensing contact
  path; created this trail; required a trail entry and a plain-English
  TL;DR on every proposal, challenge, and verdict.
- **Why:** Jordan asked that the branch be clearly labeled, that license and
  commercial-contact information be posted, and that “landmarks for the
  meat to follow” be left so a human can walk the history in order.
- **Links:** `ai/README.md`, root `README.md` (banner only), `ai/CHANGELOG.md`,
  `ai/AGENTS/CYCLE.md`, `ai/AGENTS/work.md`, `ai/AGENTS/adversary.md`,
  `ai/AGENTS/verifier.md`. No pull request. `main` was not changed.
- **What this means:** If you are reading this branch, start with
  `ai/README.md`. The science on `main` is unchanged. This trail is the
  running plain-English log of later agent cycles; the next entries will
  point at proposal pull requests, ledger files, and verdicts.
