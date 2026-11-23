# Retrieval log — Keokuk / Lock 19 status and USGS 05474500 discharge

> **Unpublished branch work (ai/evolution, Round 19, 23 November 2026).** This file does not exist in `Release/` on `main` (`270942cd107ffc92a44b4be8d7fffa0e6c22fd1d`). It is not part of the published example set. `Release/` on `main` is the authoritative current source.

Retrieval date: 2026-11-21, America/New_York (EST, UTC-5).
All URLs below were fetched from the box on that date unless noted.

## 1. Mussel example citation [38] and its original

- Iowa Capital Dispatch, “Fish passage project: A first of its kind,” 21 May 2023.
  URL: https://iowacapitaldispatch.com/2023/05/21/fish-passage-project-a-first-of-its-kind/
  Retrieved 2026-11-21. SHA256 of saved HTML:
  `27fd69e9b1eb45a1984bc8e0103cc56fe52493030607595fec2814043a44aef6`
  Excerpt: `sources/iowacapitaldispatch_2023-05-21_excerpt.txt`
- Waterways Council reprint, “Fish Passage Project: A First of Its Kind,” dated on the reprint page as May 18, 2023, attributed to Iowa Capital Dispatch, with “View Source” pointing at the 21 May 2023 original above.
  URL: https://waterwayscouncil.org/media/in-the-news/article/2023/05/fish-passage-project-a-first-of-its-kind
  This is mussel worked-example citation [38].
  Retrieved 2026-11-21. SHA256 of saved HTML:
  `b443938291a0f68a57c211d1e991c3c0c845ef05af098d20fb3d658c1f7ce2d5`
  Excerpt: `sources/waterways_council_2023-05-18_excerpt.txt`
- Both texts use Keokuk / the 1913 dam as historical framing, then state that the passageway to be built is at Lock and Dam 22 near Saverton, Missouri, “the first of its kind on the Mississippi River.”

## 2. Official project at Lock and Dam 19 / Keokuk

- USACE Rock Island District, “Lock 19 Acoustic Study,” published Aug. 30, 2024.
  Live URL: https://www.mvr.usace.army.mil/about/offices/programs-and-project-management/district-projects/projects/article/3920120/lock-19-acoustic-study/
  Live curl from this box on 2026-11-21 returned an “Access Denied” HTML body (554 bytes).
  Wayback Machine snapshot used instead:
  https://web.archive.org/web/20250124030955/https://www.mvr.usace.army.mil/about/offices/programs-and-project-management/district-projects/projects/article/3920120/lock-19-acoustic-study/
  Snapshot timestamp: 20250124030955 (24 Jan 2025). SHA256 of saved HTML:
  `89148b6202d3abd3043276474f21273a5332977e2b689c679deb7b1cca62809b`
  Excerpt: `sources/usace_lock19_acoustic_study_wayback_20250124_excerpt.txt`
  Stated location: “Mississippi River – Lock and Dam 19 Keokuk, Iowa, River Mile 364.2.”
  Stated project: Underwater Acoustic Deterrent System (uADS) in the downstream lock approach channel, to deter invasive carp (Bighead and Silver Carp). Installed FY21. Four-year study; “expectation of final reporting in 2027.” USGS is the lead federal agency; USACE-ERDC is a partner. The page also states an objective to “Assess changes in the behavior of native fishes.”
- ICRCC, *Invasive Carp Action Plan: Fiscal Year 2026*.
  URL: https://icrcc.fws.gov/sites/carp/files/2026-07/2026-invasive-carp-action-plan.pdf
  Retrieved 2026-11-21. Full PDF 9,279,079 bytes, SHA256
  `93de26b86c77b6dab6fef0aca0700d4f6616c070f27b9a61f92122de53047ba2`
  The full PDF is not committed (size). The excerpt and hash are in
  `sources/icrcc_2026_action_plan_lock19_excerpt.txt`.
  Quoted statement (pdftotext): the uADS “has been installed in the approach channel at Lock No. 19 near Keokuk, Iowa … and is being operated experimentally through 2026.” In the same paragraph, “Available information suggests that acoustic deterrents reduce the passage of Silver Carp and Bighead Carp through these dam structures by about 50 percent. Detailed results of these studies are expected to be published in 2026 and 2027.”
  “These dam structures” is plural and, in context, covers both the BAFF at Barkley Lock and Dam and the uADS at Lock No. 19. This fill does **not** attribute the “about 50 percent” figure to Lock 19 alone, and does not treat it as a native-host or ebonyshell result. The phrase “little apparent effect on native fish” was **not** found in the retrieved PDF text and is not used here.

## 3. Official status of the Lock and Dam 22 fish passage (the project [38] actually names)

- DVIDS news story “Lock and Dam 22 Fish Passage Project Taking Shape,” story by Samantha Heilig, Date Taken 03.02.2026, Date Posted 03.03.2026, Story ID 559287.
  URL: https://www.dvidshub.net/news/559287/lock-and-dam-22-fish-passage-project-taking-shape
  Retrieved 2026-11-21. SHA256 of saved HTML:
  `890892576fffdd8be5ddbbd7b5fc38dd04e81b964f3e24cd19e1becae5eca08d`
  Excerpt: `sources/dvids_ld22_2026-03-02_excerpt.txt`
  States that construction of the fish passage at Lock and Dam 22 has progressed since it began “last May,” and that “Construction is expected to continue through 2027, with adaptive management and monitoring extending well into the future.” A contracting officer is quoted calling it “the first structure of its kind in the Mississippi River.” The story points to www.mvr.usace.army.mil/nesp/ld22-fish-passage for updates. That USACE project URL was not successfully fetched live in this fill (same class of .mil access restriction as the Lock 19 page) and is not treated as independently verified beyond the DVIDS story.

## 4. USGS discharge at Keokuk (locked hydrologic-context series)

- Site confirmed via USGS Water Data OGC API monitoring-locations (bbox around Keokuk) on 2026-11-21: `USGS-05474500`, “Mississippi River at Keokuk, IA,” type Stream. A second site, `402351091222701` “MISSISSIPPI RIVER AT LOCK & DAM 19 (CORPS),” was observed in the same bbox and was **not** used.
- Water-year definition retrieved 2026-11-21 from
  https://water.usgs.gov/nwc/explain_data.html
  (“What is a Water Year?”). Saved: `sources/usgs_nwc_explain_data.html`.
  The USGS Water Science School “water year” page was requested and did not resolve (CloudFront 403 / later 404) and is not cited as a retrieved source.
- Locked window, declared before values were aggregated: USGS water years 2016–2025 inclusive (2015-10-01 through 2025-09-30). Parameter 00060, statistic 00003 (daily mean discharge).
- Primary series: USGS NWIS Daily Values REST,
  https://waterservices.usgs.gov/nwis/dv/?sites=05474500&parameterCd=00060&statCd=00003&startDT=2015-10-01&endDT=2025-09-30&format=rdb
  Committed raw: `sources/nwis_dv_05474500_00060_wy2016-2025.rdb`
  RDB header “retrieved: 2026-11-21 16:25:14 -05:00 (natwebcaas01)” on the last live fetch used for committed outputs.
- Comparison series: USGS Water Data OGC API v0 daily collection,
  https://api.waterdata.usgs.gov/ogcapi/v0/collections/daily
  API version observed in response headers earlier in the session: `api-version: 0.90.0`.
- Script: `scripts/compute_keokuk_discharge.py` (re-runnable; `--offline` uses the committed RDB).

## 5. What was not found or not used

- No published ebonyshell (`Fusconaia ebena`) recruitment or mortality series meeting the locked v0.1 protocol (life stage and \(L_s\) components locked before rates, common window, official above/below river miles) was retrieved in this cycle. \(\eta^{nat}_{TM}\), \(\eta^{tot}_{TM}\), and the *severed* flag are therefore **not assigned**.
- Official mussel-reach river miles above and below the dam remain UNFILLED-REQUIRED. River Mile 364.2 is the official dam location from the USACE Lock 19 page, not a substitute reach boundary.
- uADS effectiveness figures are not used as host-passage or mussel-renewal rates.
- No base-theory move is made in this cycle. No `ai/THEORY_MAB.md` is opened here.
