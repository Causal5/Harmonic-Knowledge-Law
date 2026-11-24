# Verdict: Tulare Lake pumping and storage reconciliation (housekeeping, 24 November 2026)

**TL;DR.** Accept with revisions. The two claims match Central Valley worked example v0.2 on `main` at `56c6ab5`, and the committed crosswalk sums to the published six-year totals (2,538,548 AF extraction; −468,635 AF fall-to-fall storage change). Revisions retarget evidence at v0.2, keep the six pairs from being read as a closed budget, and keep the 2017 sign change from being read as a season-only effect. Bite 5 was not scored.

**Verdict:** `accepted-with-revisions`

**Proposal:** `ai/PROPOSALS/2026-11-24-tulare-pumping-storage/`

**Date:** 2026-11-24, America/New_York

## Checks run

- Re-added the six water-year rows of `tulare_lake_pumping_storage_crosswalk.csv`: extraction 375,293 + 652,488 + 549,066 + 213,863 + 355,005 + 392,833 = 2,538,548 AF; storage change −128,781 − 206,939 − 187,665 + 131,719 − 28,755 − 48,214 = −468,635 AF. These match the v0.2 table.
- Confirmed CY/WY overlap language and the 2017 edition values (−100,927 AF spring, +91,703 AF fall) in v0.2.
- Confirmed Table 3-2 vs 3-4 pumping discrepancies for CY 2017 (166,110 vs 166,100 AF) and CY 2018 (713,435 vs 713,615 AF) are already recorded in v0.2, with Table 3-2 as the extraction source.
- Did not re-fetch the WY PDFs in this verdict; transcription confidence rests on the already committed crosswalk and the published v0.2 text on `main`.

## Claim outcomes

| Claim | Outcome | Why |
|---|---|---|
| C-tulare-periods-01 | accepted-with-revisions | The period overlap and the six descriptive water-year pairs are in v0.2. CH-tulare-periods-01-interval-alignment **misses as a false claim** (A and v0.2 already call the comparison descriptive and refuse a recharge residual) and **hits as a summary risk**. The revision makes the interval mismatch and the no-attribution rule part of the claim record, and names v0.2 as the published evidence. |
| C-tulare-periods-02 | accepted-with-revisions | The 2017 opposite signs are in v0.2. CH-tulare-periods-02-not-season-alone **hits** on the evidence path (the proposal pointed at the superseded writeup) and on the need to keep the “timing and inputs, not season alone” qualifier unmissable. Both are applied. |

## What this is not

Not a Bite 5 score, not a closed water budget, not an independent attribution of storage loss to pumping, not a season-only explanation of the 2017 sign change, and not a publication to `main`.
