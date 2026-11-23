# Verdict: Tulare Lake 5-022.12 DTW contrast and retrieved CVHM2 figures (Round 13)

> **Source-precedence note (Round 18, 23 November 2026).** Original verdict text is preserved. The worked fill is not in `Release/` on `main`. Unpublished branch work. See `ai/LEDGER/errata/2026-11-23-source-precedence.md`.

**TL;DR.** Accept with revisions. The official 5-022.12 polygon is on the branch, the locked USGS 72019 script re-runs to n=0 paired wells, and the 158 km³ sentence is on the retrieved USGS Publications Warehouse page. Revisions keep three points unmissable: n=0 is coverage, not “no change”; March–May is a declared window; 158 km³ is an abstract quotation, not a model rerun or a Tulare Lake 2015–2024 result. Bite 5 and \(V_W\) were not scored.

**Verdict:** `accepted-with-revisions`

**Proposal:** `ai/PROPOSALS/2026-11-21-tulare-lake-dtw/`

**Date:** 2026-11-21, America/New_York

## Checks run

- Re-ran `scripts/compute_tulare_lake_spring_dtw.py --offline` on the committed bundle: 0 qualifying wells; one in-polygon spring 2015 measurement; zero spring 2024 measurements.
- Committed GeoJSON properties: Basin_Subbasin_Number `5-022.12`, name SAN JOAQUIN VALLEY - TULARE LAKE, Area_SqMiles 837.356.
- Source resolution: `https://pubs.usgs.gov/publication/70253177` HTTP 200; DWR FeatureServer query for 5-022.12 HTTP 200. The excerpt contains “158 km 3” and “About 15%.”

## Claim outcomes

| Claim | Outcome | Why |
|---|---|---|
| C-tulare-dtw-01 | accepted | GeoJSON is 5-022.12; the fill does not treat it as “the” CV/SJV Bite 5 boundary. No challenge. |
| C-tulare-dtw-02 | accepted-with-revisions | The script result holds. CH-tulare-dtw-02-usgs-coverage-not-hydrology **hits as a summary risk** (A already stated DWR was not retrieved and did not invent a change; the revision forbids later describing n=0 as “no water-level change”). CH-tulare-dtw-02-spring-window-unofficial **misses** as a false claim — A already labeled March–May a declared convention — and that label is repeated. |
| C-tulare-dtw-03 | accepted-with-revisions | The Warehouse abstract quote is present. CH-tulare-dtw-03-abstract-only **hits as a summary risk** (A already said the PDF was not retrieved and the figures were not recomputed; the revision forbids tightening “about 15%” or applying 158 km³ to 5-022.12 2015–2024). |

## What this is not

Not a Bite 5 score, not \(V_W\), not an independent CVHM2 run, not a computed 2015–2024 Tulare Lake water-level change, not a Sahel restoration, not a base-theory or MAB move. `main` was not changed.
