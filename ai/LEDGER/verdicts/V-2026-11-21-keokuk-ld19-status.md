# Verdict: Keokuk / Lock 19 official status and USGS 05474500 discharge (Round 12)

**TL;DR.** Accept with revisions. Citation [38] does locate the first-of-its-kind passage at Lock and Dam 22, not Keokuk, and official records describe a carp deterrent at Lock 19 rather than a fish passage there. The verifier re-ran the discharge script and confirmed the cited URLs (the live USACE page is still denied). Revisions: date the river-mile and FY21/2027 wording to the January 2025 snapshot; attribute the Lock 22 2027 date only to the DVIDS story; say plainly that the primary discharge service was chosen after gaps appeared; report means with and without estimated days; keep discharge as context, not an HKL test. The *severed* flag and \(\eta\) stay unassigned.

**Verdict:** `accepted-with-revisions`

**Proposal:** `ai/PROPOSALS/2026-11-21-keokuk-ld19-status/`

**Date:** 2026-11-21, America/New_York

## Checks run

- Re-ran `Release/Examples/ohio-mississippi-mussels/worked-fills/2026-11-21-ld19-status/scripts/compute_keokuk_discharge.py --offline` on this Linux box against the committed NWIS DV RDB. Result matched claim 03: 3,652/3,653 numeric days, period mean 100,725 ft³/s, minimum 17,700 ft³/s on 2023-08-29, maximum 534,000 ft³/s on 2019-05-31, missing date 2022-08-31.
- Source resolution on 21 November 2026: Iowa Capital Dispatch, Waterways Council [38], DVIDS 559287, https://water.usgs.gov/nwc/explain_data.html, the 24 January 2025 Wayback Lock 19 snapshot, and the ICRCC FY2026 PDF all returned HTTP 200. The live USACE Lock 19 URL returned HTTP 403 (body length 556). The ICRCC PDF `Content-Length` was 9,279,079 bytes, matching the logged size and hash length.

## Claim outcomes

| Claim | Outcome | Why |
|---|---|---|
| C-keokuk-ld19-01 | accepted | The retrieved original and reprint both name Lock and Dam 22 near Saverton as the first-of-its-kind passage. No challenge contested that sentence. |
| C-keokuk-ld19-02 | accepted-with-revisions | USACE/ICRCC records support a uADS at Lock 19, not a Keokuk fish passage, and \(\eta\) / *severed* / monitoring were left unassigned. CH-keokuk-ld19-02-wayback-not-live **hits**: RM 364.2 and FY21/2027 reporting must be dated to the 24 January 2025 snapshot; the live page was denied. CH-keokuk-ld19-02-dvids-not-project-page **misses**: A already attributed LD22 status to the DVIDS story and noted the project page was not fetched; the example note keeps that attribution. |
| C-keokuk-ld19-03 | accepted-with-revisions | The committed RDB and `--offline` re-run support the counts and means. CH-keokuk-ld19-03-source-chosen-after-gaps **hits**: the window was locked in advance, but the primary service was chosen after inspecting OGC completeness. CH-keokuk-ld19-03-estimated-in-mean **hits**: 39 `A:e` days were counted but not shown as a companion mean (now supplied: period 100,548 ft³/s excluding estimates). CH-keokuk-ld19-03-not-an-hkl-test **misses** as a false claim — A already labeled discharge as context only — but the disclaimer is repeated in the example note so it cannot drop out of a later summary. |

## Revisions applied in this commit

- Session 3 note added to mussel example §8 item 4, with Wayback dating, DVIDS attribution, and the hydrologic-context disclaimer.
- Ebonyshell protocol construction-status paragraph now points at the worked fill and keeps reach miles and monitoring unfilled.
- Worked fill updated with verifier checks, source-choice language, and means including vs excluding estimated days (`outputs/usgs_05474500_annual_means_including_and_excluding_estimated.csv`).

## What this is not

Not a computed \(\eta_{TM}\). Not an assignment of the *severed* flag. Not a score of Bite 5 or \(V_W\). Not a base-theory or MAB move. Official registry papers were not rewritten. `main` was not changed.
