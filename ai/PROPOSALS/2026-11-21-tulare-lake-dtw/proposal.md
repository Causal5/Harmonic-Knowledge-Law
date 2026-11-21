# Proposal: Tulare Lake 5-022.12 locked DTW contrast and retrieved CVHM2 storage-loss figures (Round 13)

**TL;DR.** This cycle locks an official Bulletin 118 subbasin, queries real USGS field measurements, and computes a paired spring 2015 vs 2024 depth-to-water change. The result is n=0 qualifying wells. The cycle also retrieves, but does not recompute, Faunt et al. (2024)’s published “approximately 158 km³” Central Valley storage-loss figure from the USGS Publications Warehouse. It does not score Bite 5 or \(V_W\).

**Status:** `proposed`

**Round:** Session 3, Round 13.

## Parent documents

- `Release/Examples/central-valley/freshwater_data_dictionary_v0.2.csv` and `.NOTES.md`
- `Release/Examples/central-valley/hkl_bite5_falsification_checklist_v0.1.md`
- `Release/Examples/central-valley/central-valley-worked-example-v0.1.md`
- Round 8 computed-status procedure (lock before inspect)

## Deliverables

- `Release/Examples/central-valley/worked-fills/2026-11-21-tulare-lake-72019/`
- Claims `C-tulare-dtw-01`–`03`

## Claims

| Claim ID | Statement | Falsifier |
|---|---|---|
| C-tulare-dtw-01 | The locked official unit is DWR Bulletin 118 subbasin 5-022.12 (San Joaquin Valley–Tulare Lake), retrieved as GeoJSON from the DWR FeatureServer on 21 November 2026, and is not presented as “the” official CV/SJV Bite 5 boundary. | The committed GeoJSON is not 5-022.12, or the fill treats this subbasin as settling the official CV/SJV boundary question. |
| C-tulare-dtw-02 | On the locked 72019 spring 2015 vs spring 2024 protocol, the USGS field-measurements API yields 0 qualifying paired wells (one in-polygon spring 2015 value; zero spring 2024 values). No change statistic is invented. | Re-running the script on the committed bundle (or a live re-fetch of the same locked queries) produces a qualifying pair or a computed mean/median change that this fill reports, or a change is filled from a different window or parameter after inspection. |
| C-tulare-dtw-03 | The USGS Publications Warehouse abstract of Faunt et al. (2024) was retrieved and quotes approximately 158 km³ of Central Valley storage loss from pre-development to 2019, about 15% permanent. These figures are not a Tulare Lake 2015–2024 computation and were not produced by rerunning CVHM2. Bite 5 / \(V_W\) are not scored. | The excerpt is not on the retrieved pubs page, or this cycle presents 158 km³ as our computation or as a Bite 5 / \(V_W\) result, or as a 5-022.12 2015–2024 change. |
