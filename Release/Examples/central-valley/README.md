# Central Valley freshwater and temporal decoupling

> **Unpublished branch additions (ai/evolution, 24 November 2026 sync).** The published study guide is `Release/` on `main` at `56c6ab5464672a945c7832f03e969676c86d4a2b`. The published study guide below follows that text. The files listed below exist only on this branch and are not a publication to `main`. If wording conflicts, `Release/` on `main` wins.

This study examines how groundwater storage can temporarily sustain extraction while renewal, compaction, subsidence, and delivery infrastructure respond on different timescales. The recovered files were published on 20 September 2026 with their original contents intact.

| Read in this order | Role | Current status |
|---|---|---|
| [Central Valley freshwater worked example v0.2](central-valley-worked-example-v0.2.md) | Regional context, Tulare Lake annual results and source verification | Current worked example. Bite 5 remains open. |
| [Definition crosswalk v0.3.1](definition-crosswalk-v0.3.1.md) | Corrects inherited stock, timescale, buffer, and transfer definitions | Current interpretation |
| [Temporal Mining Freshwater Study Protocol v0.2](temporal-mining-freshwater-protocol-v0.2.md) | Physical-first study with reconciled definitions | Current working protocol; execution pending |
| [Original protocol v0.1](temporal-mining-freshwater-protocol-v0.1.md) | Recovered source | Preserved historical protocol |
| [Buffer as Temporal Dimension](../../Working/buffer-as-temporal-dimension.md) | Cross-corpus interpretation of buffer, renewal, and depletion | Working formalism with unresolved audit corrections |

## What is available

The worked example includes the six-year Tulare Lake pumping and storage comparison. The [archive note](../../../archive/worked-examples/README.md) identifies the superseded revision. It explicitly does not compute `V_W`, choose weights, or declare an HKL stability score. Publishing the source does not independently revalidate each external observation.

## Study boundaries adopted 24 November 2026

Carried over from the [Adversary review on `ai/evolution`](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/19a4aee7f6d5e3952b688dbba376b5cf26c2c849/ai/REVIEW_FOR_JORDAN.md).

| Scope | Locked spatial definition | Use |
|---|---|---|
| Central Valley | Active footprint of the [USGS CVHM2 historical grid](https://doi.org/10.5066/P97XBULI) | Regional storage and water-budget context through September 2019. |
| San Joaquin Valley | Union of the 19 [DWR Bulletin 118 polygons](https://gis.water.ca.gov/arcgis/rest/services/Geoscientific/i08_B118_CA_GroundwaterBasins/FeatureServer/0/query?where=Basin_Name%3D%27SAN+JOAQUIN+VALLEY%27&outFields=Basin_Subbasin_Number%2CBasin_Subbasin_Name&orderByFields=Basin_Subbasin_Number&outSR=4326&returnGeometry=true&f=geojson) with parent name SAN JOAQUIN VALLEY, IDs `5-022.01` through `5-022.19` inclusive | Valley-wide test on series covering this union. Crosswalk the DWR polygon and active USGS cells before comparing totals. |
| Tulare Lake pilot | [Locked DWR polygon `5-022.12`](https://github.com/Causal5/Harmonic-Knowledge-Law/blob/19a4aee7f6d5e3952b688dbba376b5cf26c2c849/Release/Examples/central-valley/worked-fills/2026-11-21-tulare-lake-72019/sources/b118_5-022.12_tulare_lake.geojson) | First subbasin test. Report its results at subbasin scale. |

DWR union inputs retrieved 24 November 2026, ordered by subbasin number, WGS 84 GeoJSON SHA-256 `a24d74f16c559de3c3564f5fefe50475634e1c5dd1f7f16c39a1fd158b71d79f`. The Tulare Lake polygon is pinned to the earlier extraction.

Use the October–September water year for annual budgets. The pilot coverage windows are 1 March–31 May in 2015 and 2024. Keep spring well readings, fall storage surveys and annual deliveries labeled by their actual periods. Inventory [DWR well records](https://data.cnra.ca.gov/dataset/periodic-groundwater-level-measurements) and the [subbasin annual reports](https://midkingsrivergsa.org/gsp) first. Consider paid observations only for a named gap that can change a conclusion.

## Next empirical work

1. For Tulare Lake, obtain reproducible, spatially and temporally matched pumping, recharge, storage, and subsidence series, with units and uncertainty.
2. Distinguish groundwater age from replenishment or recovery time; define the system boundary and timescale used in each ratio.
3. Distinguish gross withdrawal from net depletion, return flow, and imported water before estimating drawdown or exhaustion time.
4. Compute the preregistered physical indicators, compare with simpler models, and perform held-out evaluation before assigning an aggregate burden or buffer score.

The [SLAP audit](../../Reviews/slap-v0.4-corpus-audit.md), [project-status snapshot](../../Reviews/project-status-2026-09-20.md), and [current publication notes](../../Reviews/publication-notes-2026-10-16.md) record the outstanding interpretation and consistency issues. Related established papers are the [Fallacy of Large-Scale Absorbic Effort](../../Papers/fallacy-of-large-scale-absorbic-effort.md) and [Continuation Filter](../../Papers/continuation-filter.md).

## Unpublished branch files (not on `main`)

These remain on `ai/evolution` only. They do not replace the published v0.2 example or the archived v0.1.

| File | Role | Status |
|---|---|---|
| [HKL Bite 5 falsification checklist v0.1](hkl_bite5_falsification_checklist_v0.1.md) | Predeclared failure/reporting sheet | No scores filled (Round 4). Bite 5 remains unscored. |
| [Freshwater data dictionary v0.2](freshwater_data_dictionary_v0.2.csv) ([notes](freshwater_data_dictionary_v0.2.NOTES.md), [unpublished notice](freshwater_data_dictionary_v0.2.UNPUBLISHED.md)) | Schema only | Bite 1 not complete. |
| [Tulare Lake worked fill](worked-fills/2026-11-21-tulare-lake-72019/WORKED_FILL.md) | Spring 2015 vs 2024 USGS 72019 contrast | n=0 qualifying wells in that extract. |
| [DWR coverage audit](worked-fills/2026-11-21-tulare-lake-72019/DWR-COVERAGE.md) | Branch-only coverage counts | Unpublished. |
| [Pumping–storage writeup](worked-fills/2026-11-21-tulare-lake-72019/PUMPING-STORAGE.md) | Standalone reconciliation | **Superseded as the published narrative** by [v0.2](central-valley-worked-example-v0.2.md) on `main`. Kept here as branch text. The [crosswalk CSV](worked-fills/2026-11-21-tulare-lake-72019/outputs/tulare_lake_pumping_storage_crosswalk.csv) is also on `main`. |

