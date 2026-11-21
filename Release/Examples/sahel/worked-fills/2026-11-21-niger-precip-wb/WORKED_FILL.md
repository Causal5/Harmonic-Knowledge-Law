# Worked fill: Niger country precipitation indicator (World Bank / FAOSTAT)

**Status:** proposed (Round 14 / Session 3). Country-scale precursor only. Not a construction of \(V\). Not a restoration of withdrawn Sahel completion or sign-change claims. Not a lock of comparable locations for the bounded test.

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
