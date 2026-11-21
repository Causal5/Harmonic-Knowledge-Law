# C-tulare-dtw-02

**TL;DR.** The locked USGS 72019 spring contrast has no paired wells, so no water-level change is reported.

**Status:** `accepted-with-revisions`

**Statement.** On the locked protocol (parameter 72019; spring 2015 vs spring 2024; in-polygon; both windows required), the USGS field-measurements API yields zero qualifying paired wells: one in-polygon spring 2015 measurement and zero spring 2024 measurements. No mean or median change is invented.

**Falsifier.** Re-running `scripts/compute_tulare_lake_spring_dtw.py` on the committed bundle, or a live re-fetch of the same locked queries, produces a qualifying pair or a change statistic this fill reports, or a change is filled from a different window or parameter after inspection.

**Evidence.** Script, raw JSON bundle, and `outputs/tulare_lake_spring_dtw_summary.json`.
