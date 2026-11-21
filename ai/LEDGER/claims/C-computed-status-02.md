# C-computed-status-02

**TL;DR.** A flag defined by a computed quantity stays unassigned until
that quantity is computed, or the field stays blank. This cycle must
not invent a number to close the gap.

- **Proposal:** `ai/PROPOSALS/2026-11-21-computed-status-assignment/`
- **Statement:** The rule requires computed assignment or an unfilled / needs-evidence result; qualitative narrative may not assign the flag; no quantity is computed here.
- **Falsifier:** The note lets a qualitative line assign a computed flag, or it fills an η, V, or other empirical value.
- **Status:** accepted-with-revisions

**Verdict (Round 8, 2026-11-21):** accepted-with-revisions. CH-computed-status-02-lock-before-assignment hit. The protocol must be locked before the series are inspected or the flag assigned. No quantity was computed. See `ai/LEDGER/verdicts/V-2026-11-21-computed-status-assignment.md`.
