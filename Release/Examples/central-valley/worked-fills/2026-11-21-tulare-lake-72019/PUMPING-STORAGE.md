# Tulare Lake pumping and storage, 2015–2025

> **Superseded as the published narrative (24 November 2026 sync).** On `main` at `56c6ab5464672a945c7832f03e969676c86d4a2b`, this standalone writeup was integrated into [`central-valley-worked-example-v0.2.md`](../../../central-valley-worked-example-v0.2.md) and removed from the live Examples path. The [annual crosswalk CSV](outputs/tulare_lake_pumping_storage_crosswalk.csv) remains on `main`. This file is kept on `ai/evolution` as unpublished branch text. It is not the current official worked example.

**Unpublished research-branch reconciliation, 24 November 2026.** The five Tulare Lake agencies' reports support six annual comparisons for Bulletin 118 subbasin 5-022.12. The extraction totals cover October–September. The storage estimates span one fall survey to the next, with dates that can vary by well. The [year-by-year crosswalk](outputs/tulare_lake_pumping_storage_crosswalk.csv) retains earlier calendar-year rows and both storage series for inspection. Units are acre-feet (AF).

## What can be compared

| Water year ending | Gross extraction, AF | Estimated fall-to-fall storage change, AF |
|---|---:|---:|
| 2020 | 375,293 | −128,781 |
| 2021 | 652,488 | −206,939 |
| 2022 | 549,066 | −187,665 |
| 2023 | 213,863 | +131,719 |
| 2024 | 355,005 | −28,755 |
| 2025 | 392,833 | −48,214 |
| Sum of the six annual entries | 2,538,548 | −468,635 |

Extraction comes from Table 3-2 and storage from Table 3-4 of the WY 2025 filing. The WY 2024 report gives the same entries through 2024. The agencies estimate a net loss across the six fall intervals, including a gain in 2023. These columns describe gross withdrawals and changes in an aquifer stock; the difference cannot be assigned to recharge, and their ratio cannot establish the fraction of pumping that caused depletion. Climate, recharge, deliveries, lateral flow, and measurement uncertainty enter that interpretation.

## The 2019 overlap

Table 3-2 explicitly labels 2015–19 as calendar years. CY 2019 and WY 2020 both contain October–December 2019. Adding the rows double-counts the quarter. Treat the early entries as a separate calendar-year series. Table 3-4 uses a water-year heading even for the early pumping values, and its cumulative pumping column is offset from the annual column. Use the extraction table for dates and sum only compatible annual entries.

To reconstruct WY ending in year Y, add October–December of Y−1 to the CY Y total and subtract October–December of Y, using the same basin, sectors and estimation method. Reconstruction of WY 2015 also needs the final quarter of 2014. The reports inspected provide annual basin totals. Some estimation inputs are monthly, but we did not establish a complete, comparable quarterly pumping series. Early WY extractions remain unfilled. A flat monthly allocation would assume away the irrigation season.

The CSV preserves two discrepancies between Tables 3-2 and 3-4, using absolute magnitudes for their opposite pumping sign conventions. CY 2017 is 166,110 versus 166,100 AF and CY 2018 is 713,435 versus 713,615 AF. Table 3-2 is the source for the crosswalk's extraction totals. In the WY 2022 report, the storage discussion also gives 548,361 AF of pumping where both Tables 2-3 and 6-1 give 549,066 AF. The later reports retain 549,066 AF.

## Why storage estimates changed

The WY 2022 report uses spring-to-spring storage in Table 6-1. The WY 2024 and 2025 reports retrospectively estimate fall-to-fall storage for the earlier years as well. Their Table 3-4 footnote and §3.5.3 describe the revision and additional monitoring wells. Thus a fall-based historical series is already available. Appending the later years to the old spring series would introduce a change in what the series measures.

- For the interval ending in **2017**, the WY 2022 spring estimate is **−100,927 AF**. The later fall estimate is **+91,703 AF**. A claim about the direction for “2017” requires a season and report edition. The records change both timing and inputs, so the difference cannot be attributed to season alone.
- For the interval ending in **2020**, the original report gives **−25,706 AF** for spring-to-spring change and excludes C-zone loss for that year. The WY 2022 edition gives **−65,344 AF** for the spring interval after incorporating InSAR-based loss. The later fall series gives **−128,781 AF**. A common ending year can conceal both an aquifer-coverage change and a timing change.
- WY 2015 is the reference level in the later table. A blank annual change represents a baseline. Blank spring entries after 2022 mean that the selected older edition ends there.

## What the measurements support

In WY 2025 the filing classifies 26,644 AF of extraction as metered, 357,414 AF as estimated from agricultural land use and demand, and 8,775 AF as other estimated use. Sector totals therefore cannot be read as basin-wide meter readings. The agricultural estimate uses surface deliveries to calculate unmet demand, so agreement with a delivery-based predictor may reflect shared inputs.

A- and B-zone storage uses interpolated groundwater-level changes and assigned specific yields. The WY 2025 report used the average of three prior fall readings for an inaccessible B-zone well. C-zone storage uses surface displacement and an assumption about which layers compacted. The report identifies possible lag, cross-layer attribution error, and unaccounted cross-boundary flows. A comparison using the same InSAR series as an independent check on total storage would count some evidence twice. The [spring DWR well inventory](DWR-COVERAGE.md) has different temporal support.

**Confidence.** High on the transcription, accounting periods and revision direction. The basin's reported values are estimates. The cited totals supply no joint uncertainty interval or independent attribution of the loss to pumping. This reconciliation supplies the physical data columns for later work. Bite 5, climate normalization and a held-out comparison remain open.

## Source editions and verification

Retrieved 24 November 2026. The spatial scope throughout is Tulare Lake subbasin 5-022.12.

| Filing | Location used | PDF SHA-256 |
|---|---|---|
| [WY 2020](https://midkingsrivergsa.org/media/2020wy-tulare-lake-subbasin-annual-report.pdf) | §§3.1, 3.3 and 5.3, annual pumping basis and spring storage notes | `a8a7bfd87e240275d4401a4b897850962066cd61fac873a9d17d31ba544ac784` |
| [WY 2022](https://midkingsrivergsa.org/media/2022wy-tulare-lake-subbasin-annual-report.pdf) | Tables 2-3 and 6-1, historical spring estimates, pumping discrepancy and C-zone revision | `806f13a2ec8e925c6d77f154390ec06d6c3cf522cac87657bf50697235ca025d` |
| [WY 2024](https://midkingsrivergsa.org/media/TLSB%205-022.12_WY_2024.pdf) | Tables 3-2 and 3-4, §§3.3 and 3.5, historical fall estimates | `631f12cfff819e289ec61cfc533b642ad430889d4fb22d9c2b733e6d453d7d7a` |
| [WY 2025 PDF](https://sgma.water.ca.gov/portal/service/gspar/document/5821) and [DWR filing](https://sgma.water.ca.gov/portal/gspar/preview/567) | Tables 3-2 and 3-4, §§3.3 and 3.5, current row and back series. Portal sections A, B and E document the methods. | `32c080a3a4972730b94ce7d047ffcec90de16348f50abc166c55465096395be9` |

To reproduce the crosswalk, take the period label and total from each row of WY 2025 Table 3-2. Copy the signed annual storage change and absolute annual pumping from the matching ending year of Table 3-4. For the spring comparison copy the annual storage row of WY 2022 Table 6-1, preserving its negative signs. Compare each overlapping 2024–2025 edition entry, then sum only the six water-year rows. This reproduces the agency estimates as published without rerunning its groundwater model.
