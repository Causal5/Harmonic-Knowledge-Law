# Proposal: Keokuk / Lock 19 official status, citation [38] identity, and USGS 05474500 discharge (Round 12)

**TL;DR.** This cycle is a worked example with retrieved public records, not a blank template. Citation [38] describes a first-of-its-kind fish passage at Lock and Dam 22 near Saverton, Missouri, not at the Keokuk dam. Official USACE and ICRCC records for Lock and Dam 19 (River Mile 364.2) describe an underwater acoustic carp deterrent installed in FY21 and run experimentally through 2026. Daily mean discharge at USGS 05474500 was computed for a locked window (USGS water years 2016–2025). No ebonyshell recruitment series was found, so \(\eta\) and the *severed* flag stay unassigned. The example’s 2023 “fish passage at the dam” wording is proposed for a logged correction after verification.

**Status:** `accepted-with-revisions`

**Round:** Session 3, Round 12.

## Parent documents

- `Release/Examples/ohio-mississippi-mussels/ohio-mississippi-mussels-worked-example.md` §8 item 4 and reference [38]
- `Release/Examples/ohio-mississippi-mussels/ebonyshell_renewal_coverage_protocol_v0.1.md` (construction status, official boundary, monitoring result)
- `ai/NOTES/computed-status-assignment-v0.1.md` (do not assign a flag defined by a computed quantity from narrative)
- `ai/NOTES/application-quantity-inheritance-v0.1.md` (freshwater \(\eta_{TM}\) remains needs-mapping)

## Deliverables

- `Release/Examples/ohio-mississippi-mussels/worked-fills/2026-11-21-ld19-status/` (retrieval log, source excerpts, committed NWIS RDB, re-runnable script, computed outputs, worked-fill note)
- This proposal and claims `C-keokuk-ld19-01` … `03`
- No edit to the official example or protocol in this [A] commit; proposed wording is below for the verifier

## Scope and non-scope

In scope: retrieve and cite official public records for Lock 19 / Keokuk and for the project actually named in [38]; fill the dam location and the construction-status row with those records; compute locked-window discharge at the named USGS Keokuk gage; report missingness and a source-coverage difference between NWIS DV and the modern OGC daily API.

Out of scope: inventing recruitment rates; assigning *severed*; treating uADS carp-passage figures or discharge as \(\eta\); treating River Mile 364.2 as official above/below mussel-reach miles; scoring Bite 5 or \(V_W\); any base-theory or MAB arm; editing `main`; inventing citations.

## Proposed wording (for C, if accepted)

For mussel example §8 item 4, after the existing 2023 sentence and [38], add a clearly dated Session 3 note rather than silently deleting the 2023 wording:

> **Session 3 note (retrieved 21 November 2026, America/New_York).** Citation [38] (Waterways Council reprint, page date 18 May 2023, of Iowa Capital Dispatch, 21 May 2023, https://iowacapitaldispatch.com/2023/05/21/fish-passage-project-a-first-of-its-kind/) uses the Keokuk Dam as historical framing, then states that the passageway to be built — “the first of its kind on the Mississippi River” — is at Lock and Dam 22 near Saverton, Missouri. It does not say a fish passage was being prepared at Lock and Dam 19. Official USACE Rock Island “Lock 19 Acoustic Study” (published 30 August 2024; live site was Access Denied from the retrieval box; Wayback snapshot 24 January 2025) locates Lock and Dam 19 at River Mile 364.2 and describes an Underwater Acoustic Deterrent System (uADS) installed in FY21, with final reporting expected in 2027. The ICRCC *Invasive Carp Action Plan: Fiscal Year 2026* states that the uADS at Lock No. 19 is being operated experimentally through 2026. A 2 March 2026 USACE Rock Island story on DVIDS (Story ID 559287) reports the Lock and Dam 22 fish passage under construction, expected to continue through 2027. Construction of a pathway-restoring fish passage *at Keokuk* is not confirmed by these records. Fish-passage monitoring at Keokuk remains not run. \(\eta\) and the *severed* flag are not assigned in the companion fill.

For the protocol construction-status paragraph, replace “remain UNFILLED-REQUIRED” / “October 2026 has not been confirmed” with a pointer to the worked fill and the same distinctions (uADS at 19; NESP passage at 22; reach miles still UNFILLED-REQUIRED; monitoring not run).

## Claims

| Claim ID | Statement | Falsifier |
|---|---|---|
| C-keokuk-ld19-01 | Retrieved texts of [38] and its Iowa Capital Dispatch original locate the first-of-its-kind fish passage at Lock and Dam 22 near Saverton, Missouri, not at Lock and Dam 19 / Keokuk. The example’s 2023 “fish passage at the dam” wording therefore mislocates [38]. | The retrieved articles state the 2023 project is at Keokuk / Lock 19, or the quoted Saverton / Lock 22 sentence is not in the retrieved files. |
| C-keokuk-ld19-02 | Official retrieved USACE and ICRCC records describe the current project at Lock and Dam 19 (River Mile 364.2) as a uADS installed FY21, operated experimentally through 2026, with reporting expected in 2027 — not a pathway-restoring fish passage at Keokuk. \(\eta\), the *severed* flag, and fish-passage monitoring remain unassigned / not run. Official mussel-reach river miles remain UNFILLED-REQUIRED. | Those records describe an operating or under-construction fish passage *at Lock 19*, or this cycle assigns \(\eta\) or *severed* without a protocol-compliant recruitment series, or RM 364.2 is treated as official above/below reach miles. |
| C-keokuk-ld19-03 | On the locked window USGS WY 2016–2025, NWIS Daily Values at 05474500 yield 3,652/3,653 numeric daily means, period mean 100,725 ft³/s, one missing day (2022-08-31). The OGC daily API is missing 923 of those days; on days present in both, values agree. These figures are hydrologic context only. | Re-running `scripts/compute_keokuk_discharge.py` on the committed RDB (or a live re-fetch of the same locked request) produces a materially different count, mean, or missing date, or the cycle treats discharge as \(\eta\) or as a test of pathway restoration. |

## Methods notes

- Lock-before-inspect: the discharge window, site, parameter, and statistic were declared before period statistics were computed. Completeness was then cross-checked on a second official service after large gaps appeared in the OGC API; the primary reported series is NWIS DV, with the OGC gaps reported as a service difference.
- The ICRCC “about 50 percent” carp-passage sentence is not used as a Lock 19-only or native-host result.
- No series or citation was fabricated. Where a live .mil page was denied, the denial and the Wayback snapshot are both logged.
