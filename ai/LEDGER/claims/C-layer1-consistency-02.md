# C-layer1-consistency-02

**TL;DR.** The test and library files import module names that do not
match the actual filenames, and several scores are just random numbers
between 0.5 and 1. If the imports actually work as written, or those
scores are not random, the claim fails.

- **Proposal:** `ai/PROPOSALS/2026-11-21-layer1-consistency-audit/`
- **Statement:** Findings F2 and F3 are present as described (import/filename mismatch; listed scorers return `np.random.uniform(0.5, 1.0)`).
- **Falsifier:** The imports match the filenames on a case-sensitive import, or those scorers are not random as cited.
- **Status:** accepted

**Verdict (Round 2, 2026-11-21):** accepted. See `ai/LEDGER/verdicts/V-2026-11-21-layer1-consistency-audit.md`. Live import check: lowercase module names failed on Linux.
