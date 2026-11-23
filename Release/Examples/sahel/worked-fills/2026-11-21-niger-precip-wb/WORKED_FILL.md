# Worked fill: Niger country precipitation indicator (World Bank / FAOSTAT)

> **Unpublished branch work (ai/evolution, Round 19, 23 November 2026).** This file does not exist in `Release/` on `main` (`270942cd107ffc92a44b4be8d7fffa0e6c22fd1d`). It is not part of the published example set. `Release/` on `main` is the authoritative current source.

**Status:** accepted-with-revisions (Round 14 / Session 3). Country-scale precursor only. Not a construction of \(V\). Not a restoration of withdrawn Sahel completion or sign-change claims. Not a lock of comparable locations for the bounded test.

**Retrieval date:** 2026-11-21, America/New_York. WDI `lastupdated` 2026-11-11.

## TL;DR

The official World Bank indicator AG.LND.PRCP.MM for Niger, sourced from FAOSTAT, was retrieved and summarized for the locked window 1961–2022. All 62 years have the same value, **151.0 mm per year**. That matches the indicator’s own source note: it is a long-term spatial-temporal average, not an interannual rainfall series. It cannot be used to test year-to-year climate, FMNR, or a change in \(dV/dt\). Comparable locations for the Sahel bounded test remain UNFILLED-REQUIRED. CHIRPS was not retrieved in this cycle.

## Computed result

Script: `scripts/summarize_niger_precip_wb.py` (re-runnable; `--offline` uses the committed JSON).

| Item | Result |
|---|---|
| Indicator | AG.LND.PRCP.MM — Average precipitation in depth (mm per year) |
| Source | World Development Indicators, from FAOSTAT (FAO) |
| Country | Niger (NE), named in the archive Sahel text as the FMNR setting |
| Window | 1961–2022 inclusive |
| Numeric years | 62 / 62 (no missing years in the window) |
| Distinct values | 1 |
| Value | 151.0 mm per year |
| Interpretation | repeated long-term average; not interannual |

Years 1960 and 2023–2025 appear on the API page without a numeric value in this extract and were outside or null under the lock; they were not interpolated.

## What this does not claim

- It does not compute \(V\), \(\dot V\), or \(\lambda_{PAE}\).
- It does not restore “passed falsification” or “\(dV/dt\) measurably flipped sign.”
- It does not evaluate FMNR or the Great Green Wall.
- It does not fill step 1 comparable locations, and it does not treat the Republic of Niger as a substitute for those locations.
- It is not a CHIRPS series.

## Verifier revisions (Round 14)

The verifier re-ran `scripts/summarize_niger_precip_wb.py --offline` on 21 November 2026 and reproduced a single distinct value of 151.0 mm per year in all 62 years of 1961–2022. The World Bank API URL returned HTTP 200 the same day.

Revisions, keeping points A already stated and forbidding later over-reading:

- 151.0 mm per year is a **country-wide long-term average**, not rainfall at an FMNR site and not a southern-Sahel site climatology. Niger’s north–south gradient is not resolved by this indicator.
- CHIRPS was not retrieved. Interannual rainfall and the bounded test’s comparable locations and environmental-setting fields remain unfilled. This cycle did not complete Sahel climate data collection.

