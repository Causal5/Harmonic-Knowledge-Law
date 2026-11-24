# Retrieval log — DWR periodic groundwater levels, 24 November 2026

- **Source.** California Department of Water Resources, Periodic Groundwater Level Measurements, bulk download [periodic_gwl_bulkdatadownload.zip](https://data.cnra.ca.gov/dataset/dd9b15f5-6d08-4d8c-bace-37dc761a9c08/resource/c51e0af9-5980-4aa3-8965-e9ea494ad468/download/periodic_gwl_bulkdatadownload.zip), dataset [dd9b15f5-6d08-4d8c-bace-37dc761a9c08](https://data.cnra.ca.gov/dataset/periodic-groundwater-level-measurements).
- **Retrieved.** 24 November 2026, America/New_York, to a local scratch path (the 67 MB zip is not committed).
- **ZIP SHA-256.** `d606e9cff7762d6dac0dd0f9b4baa88e69a541bc45694c08b95a95096d341b0d`. This is the same bytes inventoried in the earlier [DWR coverage audit](../2026-11-21-tulare-lake-72019/DWR-COVERAGE.md).
- **Polygon.** Locked 5-022.12 GeoJSON already on this branch, `../2026-11-21-tulare-lake-72019/sources/b118_5-022.12_tulare_lake.geojson`.
- **Script.** `scripts/compute_tulare_dwr_head_contrast.py`. Replay: `python3 scripts/compute_tulare_dwr_head_contrast.py --offline` (uses the committed extracts) or pass the zip path.
- **Not retrieved.** Well-screen / aquifer-zone maps; agency fall survey date lists; specific-yield fields. The 67 MB zip is not stored in Git.
