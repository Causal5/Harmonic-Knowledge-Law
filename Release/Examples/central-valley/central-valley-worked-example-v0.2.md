# Central Valley freshwater and temporal mining — worked example v0.2

**24 November 2026.** The Tulare Lake agencies report 2,538,548 acre-feet of gross groundwater extraction across water years 2020–2025. Their estimated storage changes sum to a loss of 468,635 acre-feet across the corresponding six fall survey intervals. Storage increased in the interval ending in 2023. Together, the series describe gross pumping and the net change in stored groundwater. Whether delivered service stayed stable, how much storage capacity was permanently lost, and how much loss was attributable to pumping remain separate questions.

## Regional setting and study boundary

The Central Valley provides the regional storage context, the San Joaquin Valley supplies the nested groundwater basin, and Tulare Lake (DWR 5-022.12) is the unit for the annual comparison below. Regional estimates and State Water Project scenarios have different geographic coverage from the Tulare Lake observations. [Study boundaries](README.md#study-boundaries-adopted-24-november-2026) · [Freshwater study protocol](temporal-mining-freshwater-protocol-v0.2.md)

| Source and scale | Finding | Interpretation in this example |
|---|---|---|
| [Faunt et al., Central Valley](https://pubs.usgs.gov/publication/70253177) | CVHM2 combined with historical approximations estimates about 158 km³ of storage loss from predevelopment to 2019. The authors attribute about 15% of the loss to permanent loss from subsidence. | A regional estimate over the historical record. Applying that percentage to Tulare Lake would require local evidence. |
| [USGS, San Joaquin Valley](https://www.usgs.gov/centers/land-subsidence-in-california/science/land-subsidence-san-joaquin-valley) | During 1976–77, 1986–92, 2007–09 and 2012–15, reduced surface-water availability accompanied increased pumping, groundwater-level declines and renewed compaction. | These episodes link supply, pumping and compaction. Delivered service over the same windows still needs to be measured. |
| [Lees and Knight, San Joaquin Valley](https://doi.org/10.1038/s43247-024-01778-w) | The authors estimate about 14 km³ of subsidence volume during 2006–2022. | Surface displacement supplies evidence of compaction. Translating it into water released from a particular aquifer requires a model. |
| [California DWR, State Water Project](https://water.ca.gov/News/Blog/2025/May-25/Study-Finds-That-Subsidence-Groundwater-Over-Pumping-Could-Limit-Future-Water-Deliveries) | DWR estimated that existing subsidence had reduced annual delivery capability by about 3%. Its 2043 scenarios project an 18–87% reduction in long-term average delivery capability relative to the report baseline, depending on hydrology and subsidence. | The range describes conditional conveyance and supply risk. The local annual series below measures different quantities. |

## Tulare Lake worked result

The five Tulare Lake agencies' reports support six annual comparisons for Bulletin 118 subbasin 5-022.12. The extraction totals cover October–September. The storage estimates span one fall survey to the next, with dates that can vary by well. The [year-by-year crosswalk](worked-fills/2026-11-21-tulare-lake-72019/outputs/tulare_lake_pumping_storage_crosswalk.csv) retains earlier calendar-year rows and both storage series for inspection. Units are acre-feet (AF).

### Annual pumping and storage

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

### The 2019 overlap

Table 3-2 explicitly labels 2015–19 as calendar years. CY 2019 and WY 2020 both contain October–December 2019. Adding the rows double-counts the quarter. Treat the early entries as a separate calendar-year series. Table 3-4 uses a water-year heading even for the early pumping values, and its cumulative pumping column is offset from the annual column. Use the extraction table for dates and sum only compatible annual entries.

To reconstruct WY ending in year Y, add October–December of Y−1 to the CY Y total and subtract October–December of Y, using the same basin, sectors and estimation method. Reconstruction of WY 2015 also needs the final quarter of 2014. The reports inspected provide annual basin totals. Some estimation inputs are monthly, but we did not establish a complete, comparable quarterly pumping series. Early WY extractions remain unfilled. A flat monthly allocation would assume away the irrigation season.

The CSV preserves two discrepancies between Tables 3-2 and 3-4, using absolute magnitudes for their opposite pumping sign conventions. CY 2017 is 166,110 versus 166,100 AF and CY 2018 is 713,435 versus 713,615 AF. Table 3-2 is the source for the crosswalk's extraction totals. In the WY 2022 report, the storage discussion also gives 548,361 AF of pumping where both Tables 2-3 and 6-1 give 549,066 AF. The later reports retain 549,066 AF.

### Why storage estimates changed

The WY 2022 report uses spring-to-spring storage in Table 6-1. The WY 2024 and 2025 reports retrospectively estimate fall-to-fall storage for the earlier years as well. Their Table 3-4 footnote and §3.5.3 describe the revision and additional monitoring wells. Thus a fall-based historical series is already available. Appending the later years to the old spring series would introduce a change in what the series measures.

- For the interval ending in **2017**, the WY 2022 spring estimate is **−100,927 AF**. The later fall estimate is **+91,703 AF**. A claim about the direction for “2017” requires a season and report edition. The records change both timing and inputs, so the difference cannot be attributed to season alone.
- For the interval ending in **2020**, the original report gives **−25,706 AF** for spring-to-spring change and excludes C-zone loss for that year. The WY 2022 edition gives **−65,344 AF** for the spring interval after incorporating InSAR-based loss. The later fall series gives **−128,781 AF**. A common ending year can conceal both an aquifer-coverage change and a timing change.
- WY 2015 is the reference level in the later table. A blank annual change represents a baseline. Blank spring entries after 2022 mean that the selected older edition ends there.

### What the measurements support

In WY 2025 the filing classifies 26,644 AF of extraction as metered, 357,414 AF as estimated from agricultural land use and demand, and 8,775 AF as other estimated use. Sector totals therefore cannot be read as basin-wide meter readings. The agricultural estimate uses surface deliveries to calculate unmet demand, so agreement with a delivery-based predictor may reflect shared inputs.

A- and B-zone storage uses interpolated groundwater-level changes and assigned specific yields. The WY 2025 report used the average of three prior fall readings for an inaccessible B-zone well. C-zone storage uses surface displacement and an assumption about which layers compacted. The report identifies possible lag, cross-layer attribution error, and unaccounted cross-boundary flows. A comparison using the same InSAR series as an independent check on total storage would count some evidence twice. The [spring DWR well inventory](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/b623ee9b5af17af42e19df96220a44f7fe5c6d41/Release/Examples/central-valley/worked-fills/2026-11-21-tulare-lake-72019/DWR-COVERAGE.md) has different temporal support.

**Confidence.** High on the transcription, accounting periods and revision direction. The basin's reported values are estimates. The cited totals supply no joint uncertainty interval or independent attribution of the loss to pumping. This reconciliation supplies the physical data columns for later work. Bite 5, climate normalization and a held-out comparison remain open.

## What the case establishes about temporal mining

The Tulare Lake estimates establish a net loss over six fall-to-fall intervals. The proposed temporal-mining signature adds two empirical requirements over the same boundary and interval: delivered service stayed within a declared tolerance, and irreversible compaction increased. Annual pumping alone cannot establish stable service. The storage series already incorporates subsidence for the C-zone. Testing the full signature requires a matched delivery series and an estimate of irreversible compaction that accounts for this shared input. The historical drought episodes identify other windows in which to test that interpretation.

### Physical balance, baselines and buffer

For the subbasin, express the balance in volume per unit time:

$$
\dot G_W=R_n+R_m-W_g+Q_{net}.
$$

Here $R_n$ and $R_m$ denote natural and retained managed recharge, $W_g$ gross extraction, and $Q_{net}$ signed lateral and connected-water exchange outside those terms. Recovering pumping as a residual requires estimates of all three inflow/exchange terms and their uncertainty. Attribution to agriculture, municipal supply or an individual data center requires additional sector-specific evidence. Under a common boundary, $G_W/W_g$ gives a gross draw timescale. An estimate of time to a storage floor also needs the usable volume above that floor and a net depletion rate under a stated scenario. [Freshwater definition crosswalk](definition-crosswalk-v0.3.1.md)

A storage reference requires a physical stock measured or modeled in volume. A groundwater agency’s sustainable-yield determination has units of volume per time and belongs in the flow comparison. The regional CVHM2 historical loss estimate also leaves the present stock above a Tulare Lake service floor unresolved. DWR’s 2043 delivery scenarios illustrate an infrastructure constraint. Estimating a first-exit buffer requires a specified service threshold and the first time the scenario crosses it. [HKL, §6](../../HKL/hkl-lyapunov.md)

### Local mechanisms and open comparisons

- **Groundwater age and renewal.** USGS used tracers from 650 Central Valley wells to estimate the depth reached by post-1950s recharge. Screened depth and age distributions can help identify where withdrawals draw on older water. A local recovery time requires a response model or a measured response to changed pumping or recharge. The timescale ratio remains open. [USGS tracer study](https://pubs.usgs.gov/publication/70238758)
- **Land-surface retention.** Beaver-mediated retention, soil properties, slope, stream connections and storm drainage are candidate controls on where infiltrating water goes. Quantifying their contribution here requires local observations of retained recharge and downstream discharge. A flooded area or a gross seepage estimate alone cannot supply that balance.
- **Data-center water demand.** The IEA estimates that in 2023 about two-thirds of global data-center water consumption was associated with primary energy supply and electricity generation, and one-quarter with direct cooling. These uses can draw on different watersheds. A facility-level attribution needs metered use, power sourcing and drought-period generation. Summing both channels within Tulare Lake without locating them would misstate the burden there. [IEA, Energy and AI, fig. 5.27](https://www.iea.org/reports/energy-and-ai)
- **Governance and substitution.** Differences among groundwater agencies under the same state mandate offer a comparison for the Continuation Filter and the scaling argument. Test whether differences in deliveries, demand reduction and firm substitute capacity persist after accounting for climate, supply access and aquifer conditions. The local-governance hypothesis and the incremental predictive value of HKL remain open. [Continuation Filter](../../Papers/continuation-filter.md) · [Fallacy of Large-Scale Absorbic Effort](../../Papers/fallacy-of-large-scale-absorbic-effort.md)

## Tulare Lake sources and reproduction

Retrieved 24 November 2026. The spatial scope throughout is Tulare Lake subbasin 5-022.12.

| Filing | Location used | PDF SHA-256 |
|---|---|---|
| [WY 2020](https://midkingsrivergsa.org/media/2020wy-tulare-lake-subbasin-annual-report.pdf) | §§3.1, 3.3 and 5.3, annual pumping basis and spring storage notes | `a8a7bfd87e240275d4401a4b897850962066cd61fac873a9d17d31ba544ac784` |
| [WY 2022](https://midkingsrivergsa.org/media/2022wy-tulare-lake-subbasin-annual-report.pdf) | Tables 2-3 and 6-1, historical spring estimates, pumping discrepancy and C-zone revision | `806f13a2ec8e925c6d77f154390ec06d6c3cf522cac87657bf50697235ca025d` |
| [WY 2024](https://midkingsrivergsa.org/media/TLSB%205-022.12_WY_2024.pdf) | Tables 3-2 and 3-4, §§3.3 and 3.5, historical fall estimates | `631f12cfff819e289ec61cfc533b642ad430889d4fb22d9c2b733e6d453d7d7a` |
| [WY 2025 PDF](https://sgma.water.ca.gov/portal/service/gspar/document/5821) and [DWR filing](https://sgma.water.ca.gov/portal/gspar/preview/567) | Tables 3-2 and 3-4, §§3.3 and 3.5, current row and back series. Portal sections A, B and E document the methods. | `32c080a3a4972730b94ce7d047ffcec90de16348f50abc166c55465096395be9` |

To reproduce the crosswalk, take the period label and total from each row of WY 2025 Table 3-2. Copy the signed annual storage change and absolute annual pumping from the matching ending year of Table 3-4. For the spring comparison copy the annual storage row of WY 2022 Table 6-1, preserving its negative signs. Compare each overlapping 2024–2025 edition entry, then sum only the six water-year rows. This reproduces the agency estimates as published without rerunning its groundwater model.

**Revision history.** The [archive note](../../../archive/worked-examples/README.md) records why v0.1 was superseded. This edition incorporates the [November reconciliation](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/d51828d792f66fb01f071e860734d9bdc52a4206/Release/Examples/central-valley/worked-fills/2026-11-21-tulare-lake-72019/PUMPING-STORAGE.md) from the [`ai/evolution` proposal](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/b623ee9b5af17af42e19df96220a44f7fe5c6d41/ai/PROPOSALS/2026-11-24-tulare-pumping-storage/proposal.md). Adversary review of the reconciliation was pending at publication.
