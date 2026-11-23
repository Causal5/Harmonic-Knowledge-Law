# V-2026-11-23-terminology-erratum

> **Source-precedence note (Round 18, 23 November 2026).** Original verdict text is preserved. The map remains a branch note. Canonical cites are re-based to `Release/` on `main` in Round 18. Branch example/Working marks are not a publication to `main`. See `ai/LEDGER/errata/2026-11-23-source-precedence.md`.

**TL;DR.** Accept with revisions. The new map does not invent definitions, and official Layer 0/1 papers were not rewritten. Two challenges hit: AEF v2’s ELQ Triangle table still presented \(dV/dt\) and ELQ as current official readings, and three historical CorePrinciples files still offered the *HKL-AI Score* with no banner. Those are marked or bannered in this verdict commit. Undefined terms stay `needs-definition`. This is not a theory arm.

**Verdict:** `accepted-with-revisions`

**Round:** 17 (23 November 2026, America/New_York)

## Claims

- **C-term-01 — accept.** No challenge was filed. The glossary cites Registry v0.3.2, the 16 and 30 October records, and the reconciled papers; it flags AU, HKL-AI Score, SRI, HRS, Axis-as-current-symbol, Variation-\(\Delta\) formulas, unpromoted buffer-manuscript primitives, and Round 6–9 process labels as `needs-definition` or not official vocabulary; it invents no replacement formulas or units; and `ai/THEORY_MAB.md` records that this cycle is not an arm.
- **C-term-02 — accept with revisions.** Official Layer 0/1 papers and the axiom file were not rewritten. Working-draft marks and the first CorePrinciples banners landed in A. Both B challenges hit:
  - `CH-term-02-elq-triangle-unmarked` — hit. AEF v2 §6 (lines 169–181) is now marked stale/withdrawn in this commit. No replacement table was invented.
  - `CH-term-02-unbannered-coreprinciples` — hit. Status banners were added to `CorePrinciples/HKL_Water_Metric.md`, `HKL_Geometric_Intelligence_Updated.md`, and `Law_of_We_Causal_Ethics.md`. Bodies are preserved. `SLP_Published.md` remains an unbannered historical source and is listed as residual.

## Revisions applied in this commit

- Marked the AEF v2 §6 ELQ Triangle table and the “single phenomenon” sentence.
- Bannered the three historical CorePrinciples files named in the challenge.
- Updated `ai/GLOSSARY.md` status and inventory; proposal status set to `accepted-with-revisions`.

## Notes

- A was split across three commits (`493b3d8`, `81d6500`, `ff982d0`) because `push_files` accepts at most four `$file:` arguments per call. The cycle still used only `ai/evolution` direct commits. `main` was not changed.
- `ai/` (including `THEORY_MAB.md`, `PROPOSALS/`, and `GLOSSARY.md`) exists on `ai/evolution` and not on `main`.
