# C-niger-yield-01

**TL;DR.** Official cereal yield for Niger, 1961–2022, is an interannual series: mean 423.82 kg/ha, lowest in 1984, highest in 1964.

**Status:** `proposed`

**Statement.** The retrieved WDI indicator AG.YLD.CREL.KG for Niger (source: FAOSTAT QCL), locked window 1961–2022, is numeric in all 62 years and has 61 distinct values, with mean 423.82 kg/ha, minimum 257.1 kg/ha in 1984, and maximum 599.3 kg/ha in 1964.

**Falsifier.** Re-running `scripts/summarize_niger_cereal_yield_wb.py` on the committed JSON, or a live re-fetch of the same API URLs, yields a materially different count, mean, or min/max year.

**Evidence.** Committed API JSON, script, and `outputs/niger_cereal_yield_wb_summary.json`. WDI `lastupdated` 2026-11-11; retrieved 2026-11-21.
