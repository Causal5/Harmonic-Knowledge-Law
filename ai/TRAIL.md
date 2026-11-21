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

## 2026-11-21 — Work agent: ebonyshell renewal-coverage protocol (Round 3)

- **Agent:** Work (A)
- **What:** Proposed a blank preregistration sheet for computing \(\eta^{nat}_{TM}\) and \(\eta^{tot}_{TM}\) for ebonyshell above and below Keokuk, using the already-registered definitions. No rates were filled. The example’s qualitative “effectively zero / severed” line is not treated as a computed result.
- **Why:** The mussel README and the 30 October decision record already list this comparison as the first application, if recruitment data exist. Writing the recipe without inventing the data keeps that open step honest.
- **Links:** `ai/PROPOSALS/2026-11-21-ebonyshell-renewal-coverage-protocol/proposal.md`; `Release/Examples/ohio-mississippi-mussels/ebonyshell_renewal_coverage_protocol_v0.1.md`; claims `C-ebonyshell-renewal-01` through `-04`.
- **What this means:** A later human or study can fill official windows and series against a predeclared sheet, or leave the sheet blank if the data are not available.

## 2026-11-21 — Verifier: consistency audit accepted with revisions (Round 2)

- **Agent:** Verifier (C)
- **What:** Verdict `accept-with-revisions`. Confirmed F1–F4 on the box, including live Linux import failures. The official-vs-experimental challenge missed. The stale-citation challenge hit; finding F5 and a `src/README.md` status notice were added. No official paper was edited.
- **Why:** Claims have to be checked against the actual files and a real import, not against the audit’s wording alone. The addendum’s wrong section numbers are a standing-corpus issue a later human review should see.
- **Links:** `ai/LEDGER/verdicts/V-2026-11-21-layer1-consistency-audit.md`; `ai/AUDITS/2026-11-21-layer1-consistency.md`; `src/README.md`.
- **What this means:** Experimental code in `src/` should not be cited as current PAE. The unpromoted Sahel addendum should not be read as if it extends the current Sahel and HKL papers.

## 2026-11-21 — Adversary: consistency audit challenges (Round 2)

- **Agent:** Adversary (B)
- **What:** Challenged the audit’s authority wording for F1, required a live import check for F2, and — most importantly — argued that F4 understates the unpromoted Sahel addendum’s stale citations: it points at “Sahel §5.1” and “HKL §5.1” formulas that the current papers do not contain, and it treats PAE as a number.
- **Why:** Jordan said the adversary may attack the standing corpus, not only A’s new text, as long as Layer 0 holds. The addendum is in-tree and can still be misread as extending current Sahel and HKL.
- **Links:** `ai/LEDGER/challenges/CH-layer1-consistency-01-authority-scope.md`; `CH-layer1-consistency-02-import-behavior.md`; `CH-layer1-consistency-03-stale-section-citations.md`; `CH-layer1-consistency-04-paper-edits.md`.
- **What this means:** A human reviewing later should look especially at whether the addendum is citing superseded drafts as if they were the current papers.

## 2026-11-21 — Work agent: Layer 1 / implementation consistency audit (Round 2)

- **Agent:** Work (A)
- **What:** Proposed a dated audit of specific repository mismatches: experimental `_apply_pae` treating expenditure as correction, import/filename mismatch and random scorers in `src/`, and withdrawn sign-change wording still used as an anchor in the unpromoted Sahel logistic addendum.
- **Why:** Jordan asked the AI line to take the framework from his definitions and to treat mistakes, including in the standing corpus, as fair game for later adversarial review. This cycle records concrete findings before new theory.
- **Links:** `ai/PROPOSALS/2026-11-21-layer1-consistency-audit/proposal.md`; `ai/AUDITS/2026-11-21-layer1-consistency.md`; claims `C-layer1-consistency-01` through `-04`.
- **What this means:** A human can now point at exact files where the experimental code or an unpromoted draft is out of step with the current definitions, without anyone having rewritten the official papers.

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
