# Retrieval log — CHIRPS v2.0 Niger national mean, 24 November 2026

- **CHIRPS.** NOAA ERDDAP dataset `chirps20GlobalAnnualP05` (CHIRPS v2.0 annual, 0.05°, mm/year), 1981-01-01 through 2022-01-01, latitude 11.65–23.55, longitude 0.10–16.05 (padded bbox around the Niger polygon). URL used:
  `https://upwell.pfeg.noaa.gov/erddap/griddap/chirps20GlobalAnnualP05.nc?precip[(1981-01-01T00:00:00Z):1:(2022-01-01T00:00:00Z)][(11.65):1:(23.55)][(0.10):1:(16.05)]`
  NetCDF SHA-256 `207ec71e966b9eb00bfa5b3d62d76053df5d7524be678b15120aa41cc56f338e` (13 MB; not committed). Units in the file: mm/year.
- **Polygon.** Natural Earth Admin 0, 50 m, version 5.1.1, feature ADMIN=Niger, ISO_A3=NER, extracted from `https://naciscdn.org/naturalearth/50m/cultural/ne_50m_admin_0_countries.zip` (ZIP SHA-256 `5fed433373581fa648920435f937d95f2d3c0200e067409c6478dcdf1b853139`). Committed as `sources/ne_50m_niger.geojson` (SHA-256 `27ea9d6af85f57050bafb1757561bb661cf1ad2f91ad6c373acbd6862b520a65`).
- **WDI.** Already committed Round 14 extract `../../2026-11-21-niger-precip-wb/outputs/niger_AG.LND.PRCP.MM_1961-2022.csv`.
- **Replay.** `python3 scripts/compute_niger_chirps_national_mean.py --offline` (standard library). Reconstructing from the NetCDF requires shapely, netCDF4, and numpy.
