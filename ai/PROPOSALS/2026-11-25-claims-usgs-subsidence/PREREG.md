# Follow-up pre-registration — USGS subsidence pages for CV-11 and a new row

**TL;DR.** This follow-up re-fetches the USGS San Joaquin Valley subsidence page that left CV-11 partial, and extracts one new simple claim from the Water Resources Mission Area Land Subsidence page Jordan supplied. Rulings come only after this protocol is committed. No theory arms, no invented citations, never `main`.

**Status:** proposed. Follow-up to Launch Pad Session 3, step A. Authorized under Jordan’s t26u note and the parent request to retry the page cited on `main` and to add the Ireland photograph claim.

**Branch and precedence.** Direct commits to `ai/evolution` only. No pull requests, no other branches, never `main`. `Release/` on `main` (currently `37522fc`) is primary.

## Scope

1. **CV-11 retry.** Fetch the URL already cited in published Central Valley v0.2: [Land Subsidence in the San Joaquin Valley](https://www.usgs.gov/centers/land-subsidence-in-california/science/land-subsidence-san-joaquin-valley) (page date October 17, 2018). Search for the paragraph beginning “Reduced surface-water availability,” immediately above “Importance of Monitoring Subsidence.” If the live page confirms the 1976–77, 1986–92, 2007–09, and 2012–2015 wording, propose revising CV-11 accordingly. The pre-registered limit, if the page confirms, is: whether pumping maintained delivered water service during those episodes remains open. If the page still cannot be fetched, record Jordan’s verification as user-supplied and leave the row marked accordingly. Do not invent a substitute study.

2. **New row (proposed ID CV-14).** Extract a simple claim from the USGS page [Land Subsidence](https://www.usgs.gov/mission-areas/water-resources/science/land-subsidence), Water Resources Mission Area, March 2, 2019. Jordan’s short link `https://share.google/NTs3sZSCGsDBph3Vf` is to be resolved to that canonical usgs.gov URL. The claim to extract is that land near the approximate point of maximum subsidence in the San Joaquin Valley subsided roughly 9 m from 1925 to 1977 due to aquifer-system groundwater withdrawals (Ireland photograph). The same page also states that more than 80 percent of known land subsidence in the U.S. is a consequence of groundwater use. Pre-registered limit: it is a single point of maximum subsidence, not a valley-wide figure. Use only wording the retrieved page actually prints. A bench-mark identifier is to be included only if the page or its media-details caption prints it.

## Method (A → B → C)

**A (this commit).** Record the retrieval result and the proposed row wording, without rulings.

**B.** Attack each row for overreach, a mislinked study, a missing limit, or a claim that needs an undefined A1–A8 term.

**C.** Rule each row (`supported` / `supported-with-limit` / `partial` / `unsupported` / `needs-definition`), narrow wording rather than drop, check that every link resolves and says what is claimed, and update `ai/CLAIMS.md` counts, TL;DR, CHANGELOG, and TRAIL.

## Constraints

Same as Session 3: no invented data, citations, or definitions; A1–A8 stay undefined; THEORY_MAB arms are not developed; regional San Joaquin Valley findings are not automatically Tulare Lake 5-022.12 results; this is not a Layer 0 test.
