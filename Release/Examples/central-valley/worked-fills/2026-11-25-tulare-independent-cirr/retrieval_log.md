# Retrieval log — independent C_irr product search, 25 November 2026

Times are America/New_York. Full binaries and long time series are not committed; excerpts and SHA-256 hashes are.

## Retrieved and used

| Source | URL | Status | SHA-256 | Local excerpt or extract |
|---|---|---|---|---|
| USGS NWIS California GW-EX site inventory | https://waterservices.usgs.gov/nwis/site/?format=rdb&stateCd=CA&siteType=GW-EX&siteStatus=all | 200, 25 November 2026 | `7b5e6ba2ac4acb56326007f6ed19325be04bd1b79285c991c50fa5eaa089f394` | `sources/nwis_ca_gwex.rdb` (17 sites) |
| USGS NWIS GW-EX sites in a padded box around 5-022.12 | https://waterservices.usgs.gov/nwis/site/?format=rdb&bBox=-120.1,35.7,-119.3,36.6&siteType=GW-EX&siteStatus=all | 200 | `2412b4dd11caf99e6b0511e86736f23f665dd44833d1ecfcff63309bed3c48fa` | `sources/nwis_bbox_gwex.rdb` (one site: Rasta, outside the polygon) |
| USGS California Water Science Center, Central Valley Subsidence Data | https://ca.water.usgs.gov/land_subsidence/central-valley-subsidence-data.html | 200 | `5280c0acf9ffefcaa2e97087f31ed9d810123e3af0ae9d5641617af9579d104a` | `sources/usgs_cv_subsidence_extensometer_excerpt.txt` |
| USGS Science Data Catalog, Brandt, Sneed, and Boyce, DOI 10.5066/P144BREY | https://data.usgs.gov/datacatalog/data/USGS:61d74604d34ed79294005087 | 200 (landing page) | `f694008095764019c98fa1dc6b7ce90ada7ca2793024344280605531b19a344e` | `sources/usgs_brandt_p144brey_excerpt.txt` |
| Tulare Lake WY 2025 Annual Report | https://sgma.water.ca.gov/portal/service/gspar/document/5821 | Reused local PDF from earlier Tulare work | PDF `32c080a3a4972730b94ce7d047ffcec90de16348f50abc166c55465096395be9` | `sources/wy2025_subsidence_excerpt.txt` |
| Nevada Geodetic Laboratory station page, CRCN | https://geodesy.unr.edu/NGLStationPages/stations/CRCN.sta | 200 | `9ef7d129e3243af47ff1f503e3c2463fb5b87cca0ca8189671bab4d0af0d1a66` | Station coordinates; series excerpt below |
| NGL IGS20 tenv3, CRCN | https://geodesy.unr.edu/gps_timeseries/IGS20/tenv3/IGS20/CRCN.tenv3 | 200, 5,104 lines | `db79dbddec7e0f5b25a4647c53cc70b63aa79f841e609f393745b352302730d6` | `sources/ngl_crcn_tenv3_excerpt.txt` (header, first two rows, last row) |
| Nevada Geodetic Laboratory station page, LEMA | https://geodesy.unr.edu/NGLStationPages/stations/LEMA.sta | 200 | `e5789e24b28a6fe78ab9815ec0d32c616ce70e2f9e831565d56b26569401291c` | Station coordinates; series excerpt below |
| NGL IGS20 tenv3, LEMA | https://geodesy.unr.edu/gps_timeseries/IGS20/tenv3/IGS20/LEMA.tenv3 | 200, 5,369 lines | `d6b50d991d884758f09c53af90809d9acdb8b05fc8e95fcb82366d711ae01f93` | `sources/ngl_lema_tenv3_excerpt.txt` |
| OpenET, “What is ET?” | https://openetdata.org/what-is-et/ | 200 | `e944d4ce9a4de250d501c3101a4d9529afed27baaca3ce9c1cdb12591824bd50` | `sources/openet_what_is_et_excerpt.txt` |
| Bulletin 118 Tulare Lake polygon (already committed) | `Release/Examples/central-valley/worked-fills/2026-11-21-tulare-lake-72019/sources/b118_5-022.12_tulare_lake.geojson` | reused | (existing file) | Used for point-in-polygon tests |

## Attempted and not used as a lockable series

| Source | URL | Result |
|---|---|---|
| ScienceBase item JSON for DOI 10.5066/P144BREY and companion CVHM2 / CGPS items | https://www.sciencebase.gov/catalog/item/61d74604d34ed79294005087?format=json (and related IDs) | HTTP 403. The site table was not retrieved. No 5-022.12 extensometer is named from that release in this fill. |
| DWR / CNRA TRE Altamira dataset page | https://data.cnra.ca.gov/dataset/tre-altamira-insar-subsidence | HTTP 403. The product is still identified from the WY 2025 filing, which cites this dataset and states that subbasin subsidence coverage is InSAR. |
| USGS land-subsidence-in-california HTML on www.usgs.gov | https://www.usgs.gov/centers/land-subsidence-in-california/science/land-subsidence-san-joaquin-valley | HTTP 504 at retrieval time. The California Water Science Center page above was used instead. |
| NGL path `.../gps_timeseries/tenv3/IGS20/CRCN.tenv3` | older documented path | HTTP 404; the live path is `.../gps_timeseries/IGS20/tenv3/IGS20/CRCN.tenv3`. |
| OpenET `/method-ets/` | https://openetdata.org/method-ets/ | HTTP 404. The “What is ET?” page was sufficient to record object class. |
| SGMA Data Viewer documentation HTML | https://sgma.water.ca.gov/webgis/config/custom/html/SGMADataViewer/doc/ | Retrieved, but the page is a viewer shell and was not used as a quoted lock. |

No paywall was circumvented. No source was invented.
