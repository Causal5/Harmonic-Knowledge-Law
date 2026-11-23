# Verdict: Niger WDI/FAOSTAT precipitation indicator (Round 14)

> **Source-precedence note (Round 18, 23 November 2026).** Original verdict text is preserved. The worked fill is not in `Release/` on `main`. Unpublished branch work. See `ai/LEDGER/errata/2026-11-23-source-precedence.md`.

**TL;DR.** Accept with revisions. The official indicator really is 151.0 mm per year, repeated across 1961–2022, and really is a long-term average. Revisions: it is not a site or southern-Sahel rainfall value, and CHIRPS was not retrieved, so interannual rainfall and bounded-test environmental setting remain unfilled. No \(V\) was constructed and withdrawn Sahel claims were not restored.

**Verdict:** `accepted-with-revisions`

**Proposal:** `ai/PROPOSALS/2026-11-21-niger-precip-wb/`

**Date:** 2026-11-21, America/New_York

## Checks run

- Re-ran `scripts/summarize_niger_precip_wb.py --offline`: 62/62 numeric years, 1 distinct value, 151.0 mm per year; WDI `lastupdated` 2026-11-11.
- `https://api.worldbank.org/v2/country/NE/indicator/AG.LND.PRCP.MM?format=json&per_page=200` returned HTTP 200.

## Claim outcomes

| Claim | Outcome | Why |
|---|---|---|
| C-niger-precip-01 | accepted-with-revisions | The repeated 151.0 value re-runs. CH-niger-precip-01-national-average-not-a-site **hits as a summary risk** (A already did not use it as a site series; the revision forbids later doing so). |
| C-niger-precip-02 | accepted-with-revisions | No \(V\) and no restored wording. CH-niger-precip-02-chirps-not-retrieved **hits as a summary risk** (A already said CHIRPS was not retrieved; the revision forbids describing the cycle as having filled Sahel rainfall time series). |

## What this is not

Not \(V\), not a \(dV/dt\) sign test, not an FMNR evaluation, not a filled comparable-location lock, not a CHIRPS series. `main` was not changed.
