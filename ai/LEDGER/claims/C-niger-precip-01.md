# C-niger-precip-01

**TL;DR.** For 1961–2022, the official Niger precipitation indicator is 151.0 mm per year, repeated every year — a long-term average, not a year-to-year rainfall series.

**Status:** `proposed`

**Statement.** The retrieved World Bank WDI indicator AG.LND.PRCP.MM for Niger (source: FAOSTAT), in the locked window 1961–2022, has a numeric value in all 62 years and exactly one distinct value, 151.0 mm per year. That is consistent with the indicator’s source note that it is a long-term average, and the fill does not treat it as an interannual rainfall series.

**Falsifier.** Re-running `scripts/summarize_niger_precip_wb.py` on the committed JSON, or a live re-fetch of the same API URLs, shows more than one distinct numeric value in that window, or the fill treats 151 mm as year-to-year rainfall.

**Evidence.** Committed API JSON, script, and `outputs/niger_precip_wb_summary.json`. WDI `lastupdated` 2026-11-11; retrieved 2026-11-21.
