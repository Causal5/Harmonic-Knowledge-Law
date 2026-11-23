# Worked fill: Lock and Dam 19 / Keokuk official status, citation [38], and USGS 05474500 discharge

> **Unpublished branch work (ai/evolution, Round 19, 23 November 2026).** This file does not exist in `Release/` on `main` (`270942cd107ffc92a44b4be8d7fffa0e6c22fd1d`). It is not part of the published example set. `Release/` on `main` is the authoritative current source.

**Status:** accepted-with-revisions (Round 12 / Session 3). Ratification-pending as a fill of the ebonyshell protocol and mussel example. Not a computation of \(\eta_{TM}\). Not empirical validation of HKL. Freshwater reuse of \(\eta_{TM}\) remains needs-mapping under `ai/NOTES/application-quantity-inheritance-v0.1.md`.

**Retrieval date:** 2026-11-21, America/New_York. See `retrieval_log.md` for URLs, versions, hashes, and access notes.

## TL;DR

Public sources retrieved on 21 November 2026 (EST) show that mussel-example citation [38] describes a first-of-its-kind fish passage at Lock and Dam 22 near Saverton, Missouri, not at the Keokuk dam. Official USACE and ICRCC records for Lock and Dam 19 (River Mile 364.2) describe an Underwater Acoustic Deterrent System installed in FY21 and operated experimentally through 2026, with final reporting expected in 2027 — a carp deterrent, not a pathway-restoring fish passage at Keokuk. Daily mean discharge at USGS 05474500 (Mississippi River at Keokuk, IA) was computed for the locked window USGS water years 2016–2025: 3,652 of 3,653 days present on the NWIS Daily Values service, period mean 100,725 ft³/s, one missing day (2022-08-31). The modern USGS OGC daily API is missing 923 of those days; where both services have a value they agree (0 disagreements). These discharge figures are hydrologic context only. No recruitment series was retrieved, so \(\eta\) and the *severed* flag are unassigned.

## 1. Citation [38] identity

The mussel worked example §8 item 4 currently says, of the Keokuk dam: “as of 2023 the U.S. Army Corps of Engineers was preparing a fish passage at the dam, described as the first of its kind on the Mississippi River. [38]” Construction status as of October 2026 is stated as unconfirmed.

Citation [38] is the Waterways Council reprint of an Iowa Capital Dispatch article. The original (21 May 2023) and the reprint (page date 18 May 2023) both open with Robert Coker’s 1914 visit to the Keokuk Dam, then say:

> Now, nearly 110 years after Coker first documented the herring’s difficulty making it past the Keokuk Dam, the federal government is preparing for the construction of a fish passageway, the first of its kind on the Mississippi River… The passageway to be built at Lock and Dam 22 near Saverton, Missouri, about a 30-mile drive south from Quincy, Ill., is one of five that were authorized by Congress in 2007 as part of the Navigation and Ecosystem Sustainability Program.

The article therefore uses Keokuk as historical framing. The project it calls “the first of its kind on the Mississippi River” is at Lock and Dam 22, not Lock and Dam 19. The example’s phrase “a fish passage at the dam” (the Keokuk dam, in context) mislocates [38].

A 2 March 2026 USACE Rock Island story posted on DVIDS (Story ID 559287, posted 3 March 2026) reports construction of the Lock and Dam 22 fish passage in progress, expected to continue through 2027, and quotes a contracting officer calling it “the first structure of its kind in the Mississippi River.” That is consistent with [38]’s location. It is not a Keokuk / Lock 19 project.

## 2. Official project at Lock and Dam 19

USACE Rock Island, “Lock 19 Acoustic Study,” published 30 August 2024 (live site Access Denied from this box on 21 November 2026; Wayback snapshot 24 January 2025 used):

- Location: Mississippi River, Lock and Dam 19, Keokuk, Iowa, River Mile 364.2.
- Project: Underwater Acoustic Deterrent System (uADS) in the downstream lock approach channel, to deter Bighead and Silver Carp. Installed FY21. Four-year study; final reporting expected in 2027. USGS lead; USACE-ERDC a partner. Objectives include assessing changes in the behavior of native fishes.

ICRCC *Invasive Carp Action Plan: Fiscal Year 2026* (PDF retrieved 21 November 2026; SHA256 `93de26b86c77b6dab6fef0aca0700d4f6616c070f27b9a61f92122de53047ba2`): the uADS at Lock No. 19 “is being operated experimentally through 2026.” The plan’s “about 50 percent” reduction in Silver Carp and Bighead Carp passage is stated for “these dam structures” (BAFF at Barkley and uADS at Lock 19 together) with detailed results still expected in 2026 and 2027. That figure is not used here as a Lock 19-only result, and is not an ebonyshell or skipjack-host result.

These records do not confirm a pathway-restoring fish passage under construction or in operation at Keokuk. They also do not prove that no such passage will ever be built there. Fish-passage monitoring at Keokuk remains “not run.” uADS native-fish behavioral results, when published, would still not be ebonyshell \(\eta\).

## 3. Protocol fields this fill may update (and those it may not)

| Field | This fill |
|---|---|
| Official dam location | Lock and Dam 19, Keokuk, Iowa, River Mile 364.2, from the USACE Lock 19 Acoustic Study page (published 30 Aug 2024; Wayback 24 Jan 2025). |
| Official above/below mussel-reach river miles | Still UNFILLED-REQUIRED. RM 364.2 is the dam, not a declared study reach. |
| Fish-passage construction / operating status at Keokuk as of 21 Nov 2026 | Official current project at the dam is a uADS (deterrent), installed FY21, experimental operation through 2026, reporting expected 2027. A first-of-its-kind NESP fish passage is documented at Lock and Dam 22, under construction as of 2 Mar 2026, expected through 2027. The 2023 “preparing a fish passage at the [Keokuk] dam” wording is a mislocation of [38]. |
| Fish-passage monitoring result | still “not run” |
| Life stage, \(L_s\) components, window for rates, \(R^{nat}_s\), \(R^{man}_s\), \(L_s\), \(\eta\), *severed* flag | unfilled / unassigned. No qualifying recruitment series was retrieved. |
| Spatial above/below contrast as sink-impairment | not inferred. |

Proposed wording for mussel example §8 item 4 and the protocol’s construction-status row is in the proposal file, for the verifier to apply if the claims are accepted. This fill does not silently rewrite the example.

## 4. Computed hydrologic context: USGS 05474500

Locked before aggregation (see the script header and `retrieval_log.md`): site USGS 05474500, daily mean discharge (00060 / 00003), USGS water years 2016–2025, water-year definition from https://water.usgs.gov/nwc/explain_data.html (retrieved 21 November 2026). Purpose: context only.

Primary source: USGS NWIS Daily Values REST, retrieved 2026-11-21 16:25:14 EST (RDB header). Script: `scripts/compute_keokuk_discharge.py`.

| Quantity | Value |
|---|---|
| Calendar days in window | 3,653 |
| Numeric daily values | 3,652 |
| Missing dates | 1: 2022-08-31 |
| Non-numeric values | 0 |
| Qualification | 3,613 approved (`A`); 39 approved and estimated (`A:e`) |
| Period mean | 100,725 ft³/s |
| Period minimum | 17,700 ft³/s on 2023-08-29 |
| Period maximum | 534,000 ft³/s on 2019-05-31 |

Water-year mean daily discharge (ft³/s), NWIS DV:

| Water year | n / days | missing | mean | min | max | estimated (`A:e`) |
|---|---|---|---|---|---|---|
| 2016 | 366/366 | 0 | 110,377 | 35,500 | 210,000 | 31 |
| 2017 | 365/365 | 0 | 119,707 | 42,300 | 238,000 | 0 |
| 2018 | 365/365 | 0 | 103,744 | 28,300 | 238,000 | 4 |
| 2019 | 365/365 | 0 | 167,018 | 43,600 | 534,000 | 0 |
| 2020 | 366/366 | 0 | 128,038 | 37,000 | 229,000 | 2 |
| 2021 | 365/365 | 0 | 72,766.8 | 28,400 | 172,000 | 2 |
| 2022 | 364/365 | 1 | 72,198.9 | 23,100 | 176,000 | 0 |
| 2023 | 365/365 | 0 | 72,078.9 | 17,700 | 268,000 | 0 |
| 2024 | 366/366 | 0 | 86,870.5 | 23,800 | 268,000 | 0 |
| 2025 | 365/365 | 0 | 74,311.8 | 23,600 | 164,000 | 0 |

Comparison with the USGS Water Data OGC API v0 daily collection, same identifiers and window: 2,730 numeric days, 923 missing. On the 2,730 days present in both sources, values agree exactly (0 disagreements). The 923 OGC gaps are a service-coverage difference, not evidence of hydrologic missingness, and include almost all of water year 2018, which is complete on NWIS DV. The period mean from the incomplete OGC series is therefore not used.

These figures do not measure host passage, mussel recruitment, or sink-impairment. A high or low discharge year is not a computed \(\eta\).

## 5. What this does not claim

- It does not assign the *severed* flag.
- It does not score Bite 5 or \(V_W\).
- It does not restore any withdrawn Sahel claim.
- It does not promote an application quantity into a universal primitive.
- It does not move base theory and does not open a multi-armed-bandit arm.

## 6. Verifier revisions (Round 12)

The verifier re-ran `scripts/compute_keokuk_discharge.py --offline` on 21 November 2026 against the committed RDB and reproduced the claimed NWIS DV counts and means (3,652/3,653 days; period mean 100,725 ft³/s; missing date 2022-08-31). Cited URLs were checked the same day: Iowa Capital Dispatch, Waterways Council, DVIDS 559287, the USGS water-year page, the Wayback Lock 19 snapshot, and the ICRCC FY2026 PDF all returned HTTP 200. The live USACE Lock 19 URL returned HTTP 403 (Access Denied; body length 556), confirming A’s live-fetch note. The ICRCC PDF `Content-Length` was 9,279,079 bytes, matching the logged size.

Required revisions, now reflected in this fill and in the example/protocol notes:

1. River Mile 364.2, the FY21 install date, and “final reporting expected in 2027” are dated to the 24 January 2025 Wayback snapshot of the USACE page, not to a live official page on 21 November 2026. The ICRCC FY2026 plan, retrieved live, corroborates experimental uADS operation at Lock No. 19 through 2026 only.
2. Lock and Dam 22 construction “expected to continue through 2027” is attributed to the 2 March 2026 DVIDS story (Story ID 559287). The official project page named there was not fetched.
3. The locked items were site, parameter, statistic, and window. NWIS Daily Values was adopted as the primary service *after* the OGC API daily collection showed 923 missing days, including almost all of water year 2018, and a cross-check showed those gaps were a service difference (0 value disagreements on 2,730 overlapping days).
4. Period mean including 39 estimated (`A:e`) days: 100,725 ft³/s (n=3,652). Period mean excluding them: 100,548 ft³/s (n=3,613). Water-year means both ways are in `outputs/usgs_05474500_annual_means_including_and_excluding_estimated.csv`. The largest gap is WY2016 (110,377 including / 109,893 excluding; 31 estimated days).
5. Discharge remains hydrologic context only. It is not an HKL test.

