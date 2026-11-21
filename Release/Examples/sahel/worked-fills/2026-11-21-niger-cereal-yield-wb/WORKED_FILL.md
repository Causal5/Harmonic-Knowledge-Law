# Worked fill: Niger country cereal yield (World Bank / FAOSTAT QCL)

**Status:** proposed (Round 15 / Session 3). Country-scale precursor agricultural-outcome series only. Not rainfall. Not \(V\). Not an FMNR or Great Green Wall evaluation. Not a lock of comparable locations.

**Retrieval date:** 2026-11-21, America/New_York. WDI `lastupdated` 2026-11-11.

## TL;DR

Official WDI indicator AG.YLD.CREL.KG for Niger, sourced from FAOSTAT crops (QCL), was summarized for the locked window 1961–2022. All 62 years are numeric. There are 61 distinct values, so this is an interannual series, unlike the precipitation indicator in Round 14. Period mean 423.82 kg/ha; minimum 257.1 kg/ha in 1984; maximum 599.3 kg/ha in 1964. These numbers are not a test of FMNR, rainfall, or \(dV/dt\). CHIRPS remains unretrieved. Bounded-test comparable locations remain UNFILLED-REQUIRED.

## Computed result

Script: `scripts/summarize_niger_cereal_yield_wb.py`.

| Item | Result |
|---|---|
| Indicator | AG.YLD.CREL.KG — Cereal yield (kg per hectare) |
| Source | World Development Indicators, from FAOSTAT QCL (FAO) |
| Country | Niger (NE) |
| Window | 1961–2022 inclusive |
| Numeric years | 62 / 62 |
| Distinct values | 61 |
| Mean | 423.82 kg/ha |
| Minimum | 257.1 kg/ha in 1984 |
| Maximum | 599.3 kg/ha in 1964 |

The FAO source note (in the indicator metadata) states that cereals here are crops harvested for dry grain, and that FAO allocates production data to the calendar year. No years were interpolated.

This indicator was selected after Round 14 showed that the official precipitation indicator is not interannual. That source-choice is declared, not hidden. It is not a substitute for CHIRPS rainfall.

## What this does not claim

- Not rainfall, not CHIRPS, not \(V\), not a restored sign-change or “passed falsification” claim.
- A low-yield year such as 1984 is not attributed here to policy, drought, or architecture.
- Niger is not the filled comparable-location lock.
