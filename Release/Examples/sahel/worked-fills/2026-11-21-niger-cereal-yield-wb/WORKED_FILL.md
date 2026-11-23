# Worked fill: Niger country cereal yield (World Bank / FAOSTAT QCL)

> **Unpublished branch work (ai/evolution, Round 19, 23 November 2026).** This file does not exist in `Release/` on `main` (`270942cd107ffc92a44b4be8d7fffa0e6c22fd1d`). It is not part of the published example set. `Release/` on `main` is the authoritative current source.

**Status:** accepted-with-revisions (Round 15 / Session 3). Country-scale precursor agricultural-outcome series only. Not rainfall. Not \(V\). Not an FMNR or Great Green Wall evaluation. Not a lock of comparable locations.

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

## Verifier revisions (Round 15)

The verifier re-ran `scripts/summarize_niger_cereal_yield_wb.py --offline` on 21 November 2026 and reproduced 62 numeric years, 61 distinct values, mean 423.8177 kg/ha (reported as 423.82), minimum 257.1 kg/ha in 1984, and maximum 599.3 kg/ha in 1964. The World Bank API URL returned HTTP 200 the same day.

Revisions:

- The post–Round 14 indicator choice stays declared and is not to be described later as the unique official agricultural outcome for the Sahel test.
- National cereal yield, including the 1984 minimum and 1964 maximum, remains an official country agricultural-outcome series. It is not rainfall, not an FMNR-site result, and not HKL correction.

