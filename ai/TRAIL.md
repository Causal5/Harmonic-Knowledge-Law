# Trail — landmarks for human readers

This is a chronological breadcrumb log of work on `ai/evolution`. It is
written for a human following the branch, not as a substitute for the
ledger or the charter.

Each entry has: the date (America/New_York), which agent (or setup work),
what was done, why, links to ledger files and commits when they exist, and
a one-paragraph plain-English “what this means” summary.

Every agent action on this branch must append an entry here, as required by
`ai/AGENTS/CYCLE.md`. Newest entries go at the top, under this introduction.

---

## 2026-11-21 — Verification agent: accept-with-revisions (Round 1)

- **Agent:** Verifier (C)
- **What:** Ran mechanical checks on the box (protocol §4 fidelity, invented-data scan, registry-file identity vs `c9e1277`, link checks, and a corpus run of `tank_model.py`). Posted verdict `accept-with-revisions` and applied the required fixes in this same commit: a status row and same-directory note so the Bite 1 filename is not mistaken for a finished deliverable; new schema rows for observed net storage change, streamflow capture, and `tau_d`; protocol §13 source *classes* without invented versions; and residual schema rows for `\epsilon_{D_W}`, climate covariates, and well metadata.
- **Why:** Two of the adversary’s hits landed on the substance of the schema, and the official filename could mislead. The proposal still does what it claimed not to overclaim: it is not a finished study and not a validation of the framework.
- **Links:** `ai/LEDGER/verdicts/V-2026-11-21-freshwater-data-dictionary.md`; `Release/Examples/central-valley/freshwater_data_dictionary_v0.2.csv`; `Release/Examples/central-valley/freshwater_data_dictionary_v0.2.NOTES.md`; `ai/LEDGER/index.md`; `ai/CHANGELOG.md`. Parent commits: [A] https://github.com/Causal5/Harmonic-Knowledge-Law/commit/cb3ea10655f6106fd2d0bc683860f4a574f8bb73 and [B] https://github.com/Causal5/Harmonic-Knowledge-Law/commit/8f21e7017bd2cd4d77585bb58ce233d1b44dd91b
- **What this means:** The branch now has a clearer spreadsheet of what has to be collected, with the dangerous gaps filled as empty rows rather than left implicit. Nobody has picked a map boundary or downloaded a time series yet. That is the next human or later-cycle job, and it still needs real official sources.

## 2026-11-21 — Adversarial agent: challenges to the freshwater dictionary (Round 1)

- **Agent:** Adversary (B)
- **What:** Committed five challenges, straight to `ai/evolution`, against
  the Round 1 dictionary claims. They ask whether net storage change and
  streamflow capture are really kept separate, whether `tau_d` and
  `tau_d_net` have been mixed, whether the official Bite 1 filename can
  mislead, whether already-named §13 source classes should have been
  recorded, and whether missing hydrologic-year rules, climate covariates,
  and well metadata bound the instrument even if claim 01 is read narrowly.
- **Why:** The work agent's claims needed to be tested, not polished. The
  protocol’s own wording is the standard, not a general sense that a
  schema is helpful.
- **Links:** `ai/LEDGER/challenges/CH-freshwater-data-dictionary-01-streamflow-net-storage.md`,
  `...-01-tau-d.md`, `...-01-scope-residue.md`,
  `...-04-deliverable-path.md`, `...-04-section13-sources.md`;
  `ai/LEDGER/index.md`. Parent proposal commit:
  https://github.com/Causal5/Harmonic-Knowledge-Law/commit/cb3ea10655f6106fd2d0bc683860f4a574f8bb73
- **What this means:** A human should not take the new spreadsheet as a
  finished Bite 1 package. Several gaps are documented and waiting on the
  verifier: missing separations, a possible timescale mix-up, and a
  filename that looks more finished than the empty source boxes are.

## 2026-11-21 — Work agent: freshwater data dictionary schema (Round 1)

- **Agent:** Work (A)
- **What:** Committed the Bite 1 data dictionary schema straight to
  `ai/evolution` (status `proposed`). The file contents were first drafted
  on the discarded side-branch commit
  `6ca9701f75af4131ab37017004deda63bd64683e` and are landed here as a
  direct `[A]` commit, with no pull request. Added
  `Release/Examples/central-valley/freshwater_data_dictionary_v0.2.csv`,
  the proposal note, four claim files, and ledger rows.
- **Why:** The 16 October publication notes and protocol §14 already name
  the freshwater data dictionary as the immediate empirical step, and they
  require doing that before choosing HKL weights or collecting building
  anecdotes. This cycle records the required variables and separations
  without inventing measurements or completing source mapping.
- **Links:** `ai/PROPOSALS/2026-11-21-freshwater-data-dictionary/proposal.md`;
  `Release/Examples/central-valley/freshwater_data_dictionary_v0.2.csv`;
  claims `C-freshwater-data-dictionary-01` through `-04`;
  `ai/LEDGER/index.md`. Source draft commit (side branch, not this line):
  https://github.com/Causal5/Harmonic-Knowledge-Law/commit/6ca9701f75af4131ab37017004deda63bd64683e
- **What this means:** A human following this trail should see a spreadsheet
  of *what must be collected and kept distinct*, not a finished water study
  and not a claim that the framework has been tested. Official map
  boundaries and real data sources are still empty on purpose.

## 2026-11-21 — Setup: cycle is direct commits only

- **Agent:** setup (direct commit to `ai/evolution`; process change directed by Jordan)
- **What:** Changed the cycle from proposal-branch pull requests into
  `ai/evolution` to direct commits on `ai/evolution` only. Updated the
  cycle guide, the three agent files, the branch README, and the charter's
  process and ownership section. Layer 0 was not changed. Logged the rule
  in `ai/CHANGELOG.md`.
- **Why:** Jordan set a cardinal rule: work only on
  https://github.com/Causal5/Harmonic-Knowledge-Law/tree/ai/evolution,
  committing straight to that branch, with no pull requests and no other
  branches.
- **Links:** `ai/AGENTS/CYCLE.md`, `ai/AGENTS/work.md`,
  `ai/AGENTS/adversary.md`, `ai/AGENTS/verifier.md`, `ai/README.md`,
  `ai/CHARTER.md` (process section only), `ai/CHANGELOG.md`. `main` was
  not changed.
- **What this means:** From this point, a human following the branch will
  see proposal, challenge, and verdict commits land on `ai/evolution`
  itself, labeled `[A]`, `[B]`, and `[C]`. There should be no more
  `ai/proposal/...` side branches and no pull requests for this cycle.

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
