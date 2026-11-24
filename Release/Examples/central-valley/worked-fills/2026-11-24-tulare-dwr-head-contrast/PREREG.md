# Pre-registration: DWR head-sign test, Tulare Lake 5-022.12

**Locked 24 November 2026, America/New_York, before signed paired differences were computed.** Unpublished branch work on `ai/evolution`. Not a publication to `main`.

**Parent documents.** [Central Valley worked example v0.2](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/56c6ab5464672a945c7832f03e969676c86d4a2b/Release/Examples/central-valley/central-valley-worked-example-v0.2.md) (net fall-to-fall storage loss of 468,635 acre-feet over the six intervals ending 2020–2025); [empirical review procedure](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/56c6ab5464672a945c7832f03e969676c86d4a2b/Release/Examples/empirical-review-procedure.md); [study boundaries](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/56c6ab5464672a945c7832f03e969676c86d4a2b/Release/Examples/central-valley/README.md#study-boundaries-adopted-24-november-2026); the prior [DWR coverage inventory](../2026-11-21-tulare-lake-72019/DWR-COVERAGE.md) (counts only; no trends).

## What is being tested

v0.2 reports a net storage *loss* in 5-022.12 across the six fall-to-fall intervals from the survey before water year 2020 through the survey ending in 2025. This test asks whether an independent public well archive, under a declared fall window, shows a median depth-to-water change in the *same direction* (deeper water / lower head).

This is a **sign test only**. It does not convert feet to acre-feet, does not attribute loss to pumping, does not assign η, *severed*, buffer, \(V_W\), or Bite 5, and does not treat a water-level change as renewal coverage.

## Locked protocol

- **Boundary.** Official DWR Bulletin 118 polygon `5-022.12` already committed at `../2026-11-21-tulare-lake-72019/sources/b118_5-022.12_tulare_lake.geojson`.
- **Source.** DWR periodic groundwater-level bulk archive, ZIP SHA-256 `d606e9cff7762d6dac0dd0f9b4baa88e69a541bc45694c08b95a95096d341b0d`, the same file inventoried on 24 November 2026. Download: [periodic_gwl_bulkdatadownload.zip](https://data.cnra.ca.gov/dataset/dd9b15f5-6d08-4d8c-bace-37dc761a9c08/resource/c51e0af9-5980-4aa3-8965-e9ea494ad468/download/periodic_gwl_bulkdatadownload.zip). Field: `gse_gwe` (depth to water, feet). Increase means a lower water level.
- **Primary quality.** DWR `wlm_qa_desc` equal to `Good` (case-insensitive). A numeric-any sensitivity is reported but is not the decision statistic.
- **One site, one window value.** If a site has several finite measurements in a window, the site-window value is the **median** of those values. Sites are not dropped after seeing the sign of the change.
- **Primary window (storage-direction test).** 1 October–30 November 2019 versus 1 October–30 November 2025, inclusive, in the source date field. This is a **declared convention** for this fill, not a claim that it equals each agency fall survey date (v0.2 already says those dates can vary by well).
- **Sensitivity windows (not the decision).** (a) 1 September–30 November 2019 vs 2025; (b) 1 October–30 November 2019 vs 2024 (in case 2025 fall coverage is thin). These cannot be promoted to the decision after seeing signs.
- **Companion contrast (not the decision).** 1 March–31 May 2015 vs 1 March–31 May 2024, Good quality, same polygon. This is a different season and a different interval from the v0.2 storage series. It is reported as a physical observation only.

## Pre-registered outcome rule (primary test only)

Let \(n_G\) be the number of in-polygon sites with a Good finite site-window value in both October–November 2019 and October–November 2025. Let \(\Delta\) be the median of (DTW_{2025} − DTW_{2019}) over those sites, in feet.

| Outcome | If |
|---|---|
| **Indeterminate (data insufficient)** | \(n_G < 5\), or \(n_G \ge 5\) and \(\Delta = 0\). |
| **Holds** | \(n_G \ge 5\) and \(\Delta > 0\) (deeper water in fall 2025), same direction as the published net storage loss. |
| **Breaks** | \(n_G \ge 5\) and \(\Delta < 0\) (shallower water in fall 2025), opposite direction to the published net storage loss. |

**Cause if it breaks.** Classify as a **scope / data-limit** issue unless aquifer zone and screened interval can be locked to the same zones the agency storage model uses. This fill does not have a committed zone map, so a sign disagreement is **not** to be called a Layer 0 or Registry theory failure. It *is* a break of consistency between this independent Good-well median and the v0.2 storage-direction claim under the declared window. If it holds, still do not convert the median to volume or treat it as validation of the 468,635 AF figure.

**Procedure check (not the decision).** The fill must leave η, *severed*, official buffer, \(V_W\), and Bite 5 unassigned. Assigning any of them from this contrast would be a procedure failure.
