# CH-tulare-dtw-02-usgs-coverage-not-hydrology

**TL;DR.** Zero paired USGS 72019 records is a coverage result, not evidence that water levels in Tulare Lake did not change between 2015 and 2024. DWR/CASGEM/SGMA series were not retrieved.

- **Claim:** C-tulare-dtw-02
- **Challenge:** The bbox contains 2,404 USGS well locations but only 32 parameter-72019 field measurements in 2014–2025 in this API, and none in calendar 2024. The locked contrast’s n=0 therefore mainly measures the density of this particular USGS product, not the hydrologic change in 5-022.12. California’s operational groundwater network for SGMA is largely a DWR/CASGEM/GSA product, which this cycle did not retrieve. A says that; it must not be dropped in the summary, and the cycle must not be later described as having “computed a Tulare Lake water-level change of zero.”
- **Hit if:** The fill or a later summary treats n=0 as a measured finding of no water-level change, or omits that DWR/CASGEM series were not retrieved.
- **Miss if:** n=0 is already everywhere described as an absence of qualifying USGS 72019 pairs, with DWR/CASGEM not retrieved.
