# C-s2-corrections-02

**TL;DR.** The test scripts should import modules under their real
filenames and run on Linux. Placeholder scores should come back as
“not implemented” (`None`), not as random numbers. If a random
placeholder remains, or the scripts fail to run, the claim fails.

- **Proposal:** `ai/PROPOSALS/2026-11-21-session2-corpus-corrections/`
- **Statement:** Imports use the actual filenames and run on case-sensitive Linux; previously random placeholder scores in `src/` return `None` (not implemented) rather than invented numbers; the test scripts run without crashing.
- **Falsifier:** The lowercase imports are still the call sites, a `np.random` placeholder score remains, or the scripts fail to run on this Linux box.
- **Status:** accepted-with-revisions

**Verdict (Round 7, 2026-11-21):** accepted-with-revisions. Imports and `np.random` removal in `src/` held, and the scripts ran. CH-s2-corrections-02-residual-invented-scores hit: leftover invented numerics were removed (`_score_reasoning`, Libra EGR/GDS/entropy). CH-s2-corrections-02-coreprinciples-random hit as a corpus residual: the two `np.random.uniform` placeholders in `CorePrinciples/Law_of_We_Full.md` now return None. See `ai/LEDGER/verdicts/V-2026-11-21-session2-corpus-corrections.md`.
