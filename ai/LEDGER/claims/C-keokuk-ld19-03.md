# C-keokuk-ld19-03

**TL;DR.** For USGS water years 2016–2025, the Keokuk gage’s official daily-mean discharge series is nearly complete (3,652 of 3,653 days; period mean 100,725 ft³/s). The modern OGC API is missing 923 of those days. These numbers are river-flow context, not a mussel renewal ratio.

**Status:** `proposed`

**Statement.** On the locked window USGS water years 2016–2025 (2015-10-01 through 2025-09-30), the USGS NWIS Daily Values service for site 05474500, parameter 00060, statistic 00003, yields 3,652 numeric daily means out of 3,653 calendar days, a period mean of 100,725 ft³/s, a minimum of 17,700 ft³/s on 2023-08-29, a maximum of 534,000 ft³/s on 2019-05-31, and one missing date (2022-08-31). The USGS Water Data OGC API v0 daily collection is missing 923 days in the same window; on the 2,730 days present in both sources, values agree (0 disagreements). These figures are hydrologic context only and are not \(\eta\), host passage, or a test of pathway restoration.

**Falsifier.** Re-running `Release/Examples/ohio-mississippi-mussels/worked-fills/2026-11-21-ld19-status/scripts/compute_keokuk_discharge.py` on the committed RDB, or a live re-fetch of the same locked NWIS DV request, produces a materially different count, period mean, or missing date, or the cycle treats the discharge series as \(\eta\) or as a test of pathway restoration.

**Evidence.** Committed RDB, script, and `outputs/usgs_05474500_summary.json` in the worked-fill directory. Retrieval metadata in `retrieval_log.md`.
