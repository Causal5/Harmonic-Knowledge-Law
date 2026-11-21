# Retrieval log — World Bank / FAOSTAT precipitation indicator for Niger

Retrieval date: 2026-11-21, America/New_York. World Development Indicators page metadata `lastupdated`: 2026-11-11.

- Indicator metadata: https://api.worldbank.org/v2/indicator/AG.LND.PRCP.MM?format=json
  Committed: `sources/wb_indicator_AG.LND.PRCP.MM.json`
  Name: Average precipitation in depth (mm per year).
  sourceOrganization: FAOSTAT, Food and Agriculture Organization of the United Nations (FAO).
  sourceNote: “Average precipitation is the long-term average in depth (over space and time) of annual precipitation in the country. Precipitation is defined as any kind of water that falls from clouds as a liquid or a solid.”
- Country series: https://api.worldbank.org/v2/country/NE/indicator/AG.LND.PRCP.MM?format=json&per_page=200
  Committed: `sources/wb_AG.LND.PRCP.MM_NE.json`
  Country: Niger (NE). 66 year-rows on the page (1960–2025); numeric values for 1961–2022.
- New source class: declared in this cycle. The current Sahel paper does not itself cite this URL. Jordan’s Session 3 direction named FAO and World Bank. CHIRPS was also named and was **not** retrieved in this cycle.
- Script: `scripts/summarize_niger_precip_wb.py`.
