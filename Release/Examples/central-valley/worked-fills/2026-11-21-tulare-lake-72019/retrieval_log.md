# Retrieval log — Tulare Lake 5-022.12 spring DTW contrast and CVHM2 published storage loss

> **Unpublished branch work (ai/evolution, Round 19, 23 November 2026).** This file does not exist in `Release/` on `main` (`270942cd107ffc92a44b4be8d7fffa0e6c22fd1d`). It is not part of the published example set. `Release/` on `main` is the authoritative current source.

Retrieval date: 2026-11-21, America/New_York (EST, UTC-5).

## 1. Official subbasin boundary (locked spatial unit)

- DWR ArcGIS FeatureServer `Geoscientific/i08_B118_CA_GroundwaterBasins`, query `Basin_Subbasin_Number='5-022.12'`, `outSR=4326`, `f=geojson`.
  URL: https://gis.water.ca.gov/arcgis/rest/services/Geoscientific/i08_B118_CA_GroundwaterBasins/FeatureServer/0/query?where=Basin_Subbasin_Number%3D%275-022.12%27&outFields=%2A&returnGeometry=true&outSR=4326&f=geojson
  Retrieved 2026-11-21. Committed: `sources/b118_5-022.12_tulare_lake.geojson`.
  Properties: Basin_Name SAN JOAQUIN VALLEY; Basin_Subbasin_Name SAN JOAQUIN VALLEY - TULARE LAKE; Area_SqMiles 837.356; Area_Acres 535907; OBJECTID 315.
  Comments field: northern, southern, and eastern boundary adjustments, including a basin-boundary modification request.
- The CNRA open-data landing page https://data.cnra.ca.gov/dataset/i08-b118-ca-groundwaterbasins returned a Turnstile verification page (32 bytes of body) and is not used as a retrieved source. A “current as of October 13, 2025” date reported in a search snippet is therefore **not** cited.
- The 2016 basin-boundary description PDF at water.ca.gov was blocked (“Your request was blocked”) and is not used as a retrieved source.
- This unit is a declared official published subbasin for this fill. It does not settle what should be “the” official Central Valley or San Joaquin Valley boundary for Bite 5.

## 2. Published CVHM2 storage-loss figures (not independently recomputed)

- USGS Publications Warehouse record: https://pubs.usgs.gov/publication/70253177
  Retrieved 2026-11-21. Excerpt: `sources/usgs_pubs_70253177_excerpt.txt`.
  Suggested citation on the page: Faunt, C., Traum, J.A., Boyce, S.E., Seymour, W.A., Jachens, E.R., Brandt, J.T., Sneed, M., Bond, S., and Marcelli, M., 2024, Groundwater sustainability and land subsidence in California’s Central Valley: Water, v. 16, no. 8, 1189, 40 p.; DOI https://doi.org/10.3390/w16081189. Publication Date April 22, 2024.
  Quoted abstract language: “Combined with historical approximations, CVHM2 estimates approximately 158 km 3 of storage loss in the Central Valley from pre-development to 2019. About 15% of the total storage loss is permanent loss of storage from subsidence that has caused damage to infrastructure.”
- The full MDPI PDF (and the USGS data-release landing page) were not successfully retrieved from this box (Access Denied / 500 / CloudFront 403). The 158 km³ and “about 15%” figures are therefore taken from the USGS Publications Warehouse abstract, not from a recomputation of the MODFLOW model, and not from the paper’s body or supplementary tables.

## 3. USGS field measurements (locked contrast)

- Collection: USGS Water Data OGC API v0 field-measurements, https://api.waterdata.usgs.gov/ogcapi/v0/collections/field-measurements
- Locked before aggregation: parameter 72019; spring windows 1 March–31 May 2015 and 1 March–31 May 2024; inclusion requires coordinates inside the official 5-022.12 polygon and at least one numeric 72019 value in **each** window; well-window value is the median; no post-hoc dropping by sign of change; do not substitute another parameter if 72019 is sparse.
- Script: `scripts/compute_tulare_lake_spring_dtw.py`. Raw API bundle: `sources/usgs_field_measurements_72019_bbox_springs_2015_2024.json`.
- A cross-check of the retired-style waterservices.usgs.gov/nwis/gwlevels/ endpoint returned HTTP 403 (CloudFront) on 21 November 2026 and was not used as a data source.

## 4. Completeness check after the locked contrast returned n=0

- The same API, same bbox, parameter 72019, calendar years 2014–2025: 32 measurements at 16 sites; **zero** measurements in calendar 2024. See `outputs/usgs_72019_bbox_coverage_2014-2025.csv`. This is not a substitute window and is not used to compute a change.
- The same bbox contains 2,404 USGS monitoring locations with `site_type=Well`. Most of those wells have no 72019 field measurement in this API extract. DWR/CASGEM/SGMA water-level networks were not retrieved in this cycle.
