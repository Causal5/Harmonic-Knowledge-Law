# Retrieval log — World Bank / FAO cereal yield for Niger

Retrieval date: 2026-11-21, America/New_York. WDI `lastupdated`: 2026-11-11.

- Indicator metadata: https://api.worldbank.org/v2/indicator/AG.YLD.CREL.KG?format=json
  Name: Cereal yield (kg per hectare).
  sourceOrganization: FAO electronic files and website, FAOSTAT QCL (https://www.fao.org/faostat/en/#data/QCL).
- Country series: https://api.worldbank.org/v2/country/NE/indicator/AG.YLD.CREL.KG?format=json&per_page=200
  Committed under `sources/`.
- This FAO/World Bank source class was already declared in Round 14. The indicator was chosen in this cycle after Round 14 found AG.LND.PRCP.MM is a repeated long-term average, not an interannual series. CHIRPS was again not retrieved.
- Script: `scripts/summarize_niger_cereal_yield_wb.py`.
