# Verdict: Round 28 independent \(C_{irr}\) product search for Tulare Lake

**TL;DR.** Accept with revisions. No locked-catalog product qualifies as an independent \(C_{irr}\) for 5-022.12, so the round is **indeterminate** (data / scope gap), not a Layer 0 failure. ARM-07 stays `wait`. The signature stays unassigned. The revision: short summaries must not treat CGPS, benchmarks, OpenET, or the InSAR-derived C-zone volume as a locked independent \(C_{irr}\).

**Verdict:** `accepted-with-revisions`

**Proposal:** `ai/PROPOSALS/2026-11-25-tulare-independent-cirr/`

**Date:** 2026-11-25, America/New_York

## Checks run

- Confirmed the pre-registration commit (`12d7edf`) precedes the scored fill (`41ddab4`, with source extracts in `23c1eba` and `fc203dc`).
- Reran `classify_tulare_cirr_products.py` from the committed extracts. Results match the fill: 0 of 17 California NWIS GW-EX sites inside 5-022.12; 0 of 7 products qualify; `round_outcome=indeterminate`.
- Confirmed the fill leaves ARM-07 at `wait`, leaves the signature unassigned, and does not convert CGPS or benchmark displacements to acre-feet.

## Claim outcomes

| Claim | Outcome | Why |
|---|---|---|
| C-cirr-01 | accepted | The protocol was locked before the search was scored. Offline replay matches. |
| C-cirr-02 | accepted-with-revisions | Indeterminate / data-scope gap is the correct round-level outcome. Both challenges **hit as a summary risk**. |

## What this is not

Not a Layer 0 or theory failure, not a finding that the temporal-mining signature fired or failed, not a development of ARM-07, not a conversion of LEMA or CRCN heights to storage-capacity loss, and not a publication to `main`.
