# Pre-registration: CHIRPS vs WDI Niger rainfall, 24 November 2026

**Locked 24 November 2026, America/New_York, before a CHIRPS national-mean series was computed.** Unpublished branch work on `ai/evolution`. Not a publication to `main`.

**Parent documents.** Current [Sahel worked example](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/56c6ab5464672a945c7832f03e969676c86d4a2b/Release/Examples/sahel_worked_example.md) §§3 and 6 (rainfall is among the environmental factors a later test must distinguish; withdrawn sign-change and falsification-test claims stay withdrawn); [empirical review procedure](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/56c6ab5464672a945c7832f03e969676c86d4a2b/Release/Examples/empirical-review-procedure.md); Round 14 WDI result (AG.LND.PRCP.MM for Niger is 151 mm in every year 1961–2022).

## What is being tested

Round 14 found that the World Bank WDI precipitation indicator for Niger is a repeated national long-term average, not an interannual rainfall series. This test asks whether a primary satellite-station product, CHIRPS v2.0, shows interannual variation over the same country and overlapping years. It does **not** construct \(V\), does **not** restore withdrawn Sahel completion claims, does **not** fill bounded-test step 1 locations, and does **not** treat a national mean as a site rainfall series.

## Locked protocol

- **Product.** CHIRPS v2.0 *final* annual precipitation, 0.05°, millimeters per year, 1981–2022 inclusive (the overlap of CHIRPS’s start year with the committed WDI end year). Source: UCSB Climate Hazards Center, accessed via the NOAA ERDDAP dataset `chirps20GlobalAnnualP05` (https://upwell.pfeg.noaa.gov/erddap/griddap/chirps20GlobalAnnualP05).
- **Spatial mean.** Arithmetic mean of annual grid cells whose *centers* fall inside the Republic of Niger land polygon from [Natural Earth Admin 0, 50m, version 5.1.1](https://www.naturalearthdata.com/downloads/50m-cultural-vectors/), file `ne_50m_admin_0_countries`. Cells flagged as missing in CHIRPS are dropped. This is a **national spatial mean**, not a site series and not a population-weighted mean.
- **WDI comparison series.** The already committed Round 14 extract, `niger_AG.LND.PRCP.MM_1961-2022.csv`, years 1981–2022 only.
- **Decision statistic.** Let CV be the sample coefficient of variation (standard deviation / mean) of the 42 CHIRPS annual national means, and let \(k\) be the number of distinct values rounded to 0.1 mm.

## Pre-registered outcome rule

| Outcome | If |
|---|---|
| **Holds** (the Round 14 diagnosis that WDI is not an interannual rainfall series) | CHIRPS is retrieved as specified and (CV \(> 0.05\) or \(k > 2\)). |
| **Breaks** (that diagnosis) | CHIRPS is retrieved as specified and CV \(\le 0.01\) and \(k \le 2\) (essentially as flat as WDI). |
| **Indeterminate** | The CHIRPS extract or the Niger polygon cannot be reproduced, or the two rules above do not apply (for example \(0.01 <\) CV \(\le 0.05\) and \(k\le 2\)). |

**Cause if it breaks.** A break would mean interannual rainfall really is nearly constant at national scale in this product, so the earlier “no interannual series” finding was not a WDI-product limit. That would be a **data-diagnosis** break, not a Layer 0 theory failure.

**Forbidden.** Do not construct \(V\) or \(\dot V\), do not restore a withdrawn sign-change claim, do not treat this national mean as a comparable-location series for Sahel steps 1–6, and do not assign undefined A1–A8 terms.
