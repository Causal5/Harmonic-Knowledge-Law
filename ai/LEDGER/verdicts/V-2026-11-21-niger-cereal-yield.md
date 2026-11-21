# Verdict: Niger WDI/FAOSTAT cereal-yield series (Round 15)

**TL;DR.** Accept with revisions. The official 1961–2022 yield series re-runs: 62 years, mean 423.82 kg/ha, minimum 257.1 kg/ha in 1984, maximum 599.3 kg/ha in 1964. Revisions keep the post–Round 14 source choice visible and forbid treating national yield, or those years, as rainfall, FMNR, or HKL correction. CHIRPS was not retrieved. No \(V\) was constructed.

**Verdict:** `accepted-with-revisions`

**Proposal:** `ai/PROPOSALS/2026-11-21-niger-cereal-yield/`

**Date:** 2026-11-21, America/New_York

## Checks run

- Re-ran `scripts/summarize_niger_cereal_yield_wb.py --offline`: 62/62 numeric, 61 distinct, mean 423.8177 kg/ha, min 257.1 in 1984, max 599.3 in 1964; WDI `lastupdated` 2026-11-11.
- API URL returned HTTP 200.

## Claim outcomes

| Claim | Outcome | Why |
|---|---|---|
| C-niger-yield-01 | accepted | The counts and extrema re-run. No challenge on the numbers. |
| C-niger-yield-02 | accepted-with-revisions | CH-niger-yield-02-chosen-after-variation-seen **hits as a summary risk** (A already declared the choice; keep it visible). CH-niger-yield-02-national-yield-not-fmnr **hits as a summary risk** (A already included disclaimers; they must not drop). |

## What this is not

Not rainfall, not CHIRPS, not \(V\), not an FMNR evaluation, not a filled comparable-location lock. `main` was not changed.
