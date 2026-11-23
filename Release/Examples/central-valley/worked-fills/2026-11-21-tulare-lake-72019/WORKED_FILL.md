# Worked fill: Bulletin 118 Tulare Lake (5-022.12) spring DTW contrast, and retrieved CVHM2 storage-loss figures

> **Unpublished branch work (ai/evolution, Round 19, 23 November 2026).** This file does not exist in `Release/` on `main` (`270942cd107ffc92a44b4be8d7fffa0e6c22fd1d`). It is not part of the published example set. `Release/` on `main` is the authoritative current source.

**Status:** accepted-with-revisions (Round 13 / Session 3). Not a Bite 5 score. Not a \(V_W\) computation. Not an independent rerun of CVHM2.

**Retrieval date:** 2026-11-21, America/New_York. See `retrieval_log.md`.

## TL;DR

An official DWR Bulletin 118 subbasin — San Joaquin Valley–Tulare Lake, number 5-022.12, 837.356 square miles — was retrieved as GeoJSON and locked as the study unit. On a predeclared spring 2015 versus spring 2024 contrast, the USGS field-measurements API returned one in-polygon 72019 depth-to-water value in spring 2015 and none in spring 2024, so **zero wells** qualify for a paired change. That is a computed result of n=0, not a fabricated change. Separately, the USGS Publications Warehouse abstract of Faunt et al. (2024) was retrieved; it states that CVHM2, combined with historical approximations, estimates approximately 158 km³ of Central Valley storage loss from pre-development to 2019, of which about 15% is permanent. Those figures are quoted, not recomputed. They use a larger “Central Valley” domain than this subbasin and are not a 2015–2024 head change.

## 1. Locked protocol (before values were aggregated)

- Spatial unit: official 5-022.12 polygon from the DWR FeatureServer named above. Not “the” CV/SJV boundary for Bite 5.
- Parameter: 72019 only (depth to water, feet as reported). No substitute parameter.
- Windows: 1 March–31 May 2015 and 1 March–31 May 2024. Declared convention; no official DWR “spring measurement” definition was retrieved.
- Inclusion and median rule as in the script header.
- Statistic: mean/median of (spring 2024 DTW − spring 2015 DTW) if any wells qualify. Positive would mean a deeper water table in 2024.

## 2. Computed result

Re-runnable with `scripts/compute_tulare_lake_spring_dtw.py`.

- Spring 2015 API query: 1 feature, site USGS-361905119472901, 26 March 2015 15:31 UTC, 145.81 ft, approved, qualifiers Above and Pumping, inside the polygon.
- Spring 2024 API query: 0 features in the subbasin bbox.
- Qualifying wells (both windows, in polygon): **0**.
- Mean/median change: **not computed** (no paired observations).
- After this n=0 result, a completeness check of 72019 in the bbox for calendar years 2014–2025 found 32 measurements at 16 sites and zero records in 2024. A location query of the same bbox found 2,404 USGS wells. DWR/CASGEM series were not retrieved. The legacy gwlevels service returned 403.

The one 2015 measurement is not a change, and its “Pumping” qualifier would have required a predeclared handling rule if a pair had existed.

## 3. Retrieved published storage-loss figures

From https://pubs.usgs.gov/publication/70253177 (retrieved 21 November 2026), Faunt, Traum, Boyce, Seymour, Jachens, Brandt, Sneed, Bond, and Marcelli, *Water* 16(8):1189, 22 April 2024, DOI 10.3390/w16081189:

> Combined with historical approximations, CVHM2 estimates approximately 158 km 3 of storage loss in the Central Valley from pre-development to 2019. About 15% of the total storage loss is permanent loss of storage from subsidence that has caused damage to infrastructure.

These are published model outputs plus historical approximations, for a Central Valley domain, through 2019. They are not a measurement of Tulare Lake 5-022.12 over 2015–2024, and they were not recomputed here. The full paper PDF was not retrieved.

## 4. What this does not claim

- No Bite 5 pass/fail, no \(V_W\), no weights, no official “the” CV/SJV boundary.
- No independent CVHM2 run.
- No invented 2015–2024 water-level change.
- No Sahel claim is touched. No base-theory or MAB arm is opened here.

## 5. Verifier revisions (Round 13)

The verifier re-ran `scripts/compute_tulare_lake_spring_dtw.py --offline` on 21 November 2026 and reproduced n=0 qualifying wells (one in-polygon spring 2015 72019 value; zero spring 2024 values). The committed GeoJSON is subbasin 5-022.12, SAN JOAQUIN VALLEY - TULARE LAKE, 837.356 square miles. https://pubs.usgs.gov/publication/70253177 and the DWR FeatureServer query both returned HTTP 200 the same day, and the excerpt still contains the 158 km³ and “About 15%” sentences.

Revisions, which mostly keep language A already had and must not be dropped later:

- n=0 is an absence of qualifying USGS 72019 field-measurement pairs in this API extract. It is **not** a measured finding that Tulare Lake water levels were unchanged from 2015 to 2024. DWR/CASGEM/SGMA water-level series were not retrieved.
- March–May remains a declared convention, not a retrieved official DWR or USGS spring-season definition.
- The 158 km³ and “about 15%” figures remain abstract-only quotations from the USGS Publications Warehouse record of Faunt et al. (2024). They were not read from the paper body or supplement, were not recomputed, must not be turned into a more precise product such as 23.7 km³, and must not be applied as a 5-022.12 2015–2024 result.

