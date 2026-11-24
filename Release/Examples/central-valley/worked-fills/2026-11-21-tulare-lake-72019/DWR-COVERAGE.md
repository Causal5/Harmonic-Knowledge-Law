# Tulare Lake DWR coverage audit, 24 November 2026

Unpublished follow-up to the Adversary review on `ai/evolution`. The separate [USGS extraction](WORKED_FILL.md) recorded zero paired sites. This inventory uses the same polygon and March–May windows with a new source.

| Distinct DWR site codes with depth to water in feet | Spring 2015 | Spring 2024 | Both |
|---|---:|---:|---:|
| At least one finite numeric record | 27 | 45 | 15 |
| At least one finite record labeled Good by DWR | 24 | 40 | 11 |

Downloaded the [DWR bulk archive](https://data.cnra.ca.gov/dataset/dd9b15f5-6d08-4d8c-bace-37dc761a9c08/resource/c51e0af9-5980-4aa3-8965-e9ea494ad468/download/periodic_gwl_bulkdatadownload.zip) on 24 November 2026. ZIP SHA-256 `d606e9cff7762d6dac0dd0f9b4baa88e69a541bc45694c08b95a95096d341b0d`. Run `python3 scripts/audit_dwr_coverage.py periodic_gwl_bulkdatadownload.zip` against that version. The script joins station coordinates to measurements by site code, uses the [original polygon](sources/b118_5-022.12_tulare_lake.geojson), and checks `gse_gwe` in both spring windows. One well counts once per window. DWR's Good label is a source quality flag. Well screens, pumping conditions and spatial representativeness still require review before estimating head change.

## Other series in the same subbasin

The [WY 2024 annual report](https://midkingsrivergsa.org/media/TLSB%205-022.12_WY_2024.pdf), April 2025, covers the five subbasin agencies. Retrieved 24 November 2026, PDF SHA-256 `631f12cfff819e289ec61cfc533b642ad430889d4fb22d9c2b733e6d453d7d7a`.

| Series | Where to find it | Limit on comparison |
|---|---|---|
| Pumping | §3.3, Table 3-2, sector totals | Calendar years 2015–2019 and water years from 2020. Agricultural estimates include assumed irrigation efficiency. Obtain the underlying periods before combining totals across the transition. |
| Surface-water supply | §3.1 and §3.4 | Distinguish local or imported surface supplies from groundwater delivered through canals. Reconcile deliveries with the service variable independently. |
| Storage change | §3.5, Table 3-4 | WY 2015 is a baseline. Later annual changes are estimates, with a change from spring to fall measurement conventions. Keep the method and aquifer zone with each year. |
| Subsidence | §§3.5.2 and 5, October 2023–October 2024 InSAR | Match the raster footprint and dates. The C-zone storage estimate uses subsidence, so these two series share evidence. |

Public sources cover the next feasibility step. First reconcile time windows, aquifer zones and shared inputs. Consider paid metered pumping only if it resolves a material residual uncertainty. Water-level trends, permanent loss and Bite 5 performance remain unscored.
