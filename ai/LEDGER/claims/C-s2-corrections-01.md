# C-s2-corrections-01

**TL;DR.** The experimental Absorbic Effort helper should record how much
was spent as one thing, and whether any correction was achieved as another.
Spending more must not automatically shrink the error score. If it still
does, the claim fails.

- **Proposal:** `ai/PROPOSALS/2026-11-21-session2-corpus-corrections/`
- **Statement:** `_apply_pae` records expenditure separately from achieved correction and does not reduce `delta` by a term built from effort, in line with the 16 October record and current AEF §2.
- **Falsifier:** The helper still subtracts a term built from effort from `delta`, or it fails to record expenditure and correction as separate fields.
- **Status:** proposed
