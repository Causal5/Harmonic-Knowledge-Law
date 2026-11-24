# Verdict: Round 23 temporal-mining signature completeness, Tulare Lake

**TL;DR.** Accept with revisions. Table 3-1 of the WY 2025 filing supplies a six-year series, but independent \(C_{irr}\) cannot be locked, so the signature is **indeterminate** and is left unassigned. The revision: short summaries must name Table 3-1 as supply totals that include imported groundwater, and must not present the totals as a pure surface-water delivery or delivered-service series.

**Verdict:** `accepted-with-revisions`

**Proposal:** `ai/PROPOSALS/2026-11-24-tulare-tm-signature/`

**Date:** 2026-11-24, America/New_York

## Checks run

- Confirmed the pre-registration predates the Table 3-1 extraction for this test.
- Confirmed the fill leaves the signature unassigned and does not evaluate the conjunction.
- Confirmed the fill already records the filing’s note that imported groundwater extracted outside the subbasin is treated as a surface-water delivery.
- Confirmed v0.2 records that C-zone storage uses surface displacement, so the filing’s InSAR is not an independent \(C_{irr}\).

## Claim outcomes

| Claim | Outcome | Why |
|---|---|---|
| C-tm-sig-01 | accepted | The protocol was locked before Table 3-1 was extracted for this test. No challenge. |
| C-tm-sig-02 | accepted-with-revisions | Indeterminate is the correct outcome. CH-tm-sig-02-not-evaluated **misses**. CH-tm-sig-02-imported-column **hits as a summary risk**; later short summaries must keep the imported-groundwater note. |

## What this is not

Not a finding that the signature fired or failed, not a clean \(Q_{sw}\) or \(D_W\) assignment, not a Bite 5 or \(V_W\) score, and not a publication to `main`.
