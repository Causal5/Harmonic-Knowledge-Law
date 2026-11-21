# CH-keokuk-ld19-03-source-chosen-after-gaps

**TL;DR.** The window was locked before the numbers were summarized, but the primary service (NWIS Daily Values versus the modern OGC API) was chosen after large gaps appeared in the first service. That is a source choice made after inspection, and it should be said plainly.

- **Claim:** C-keokuk-ld19-03
- **Challenge:** Round 8’s computed-status discipline is “lock the protocol before inspecting the series.” A first retrieved the modern OGC daily collection, saw 923 missing days (including almost all of water year 2018), then adopted NWIS Daily Values as the primary series after a cross-check showed those gaps were a service difference. The comparison itself is good work. Calling the result a fully pre-locked protocol overstates what was locked in advance (site, parameter, window) and understates what was chosen after looking (which official service to treat as primary).
- **Hit if:** The claim or fill describes the primary-source choice as if it were locked before any series was inspected.
- **Miss if:** The fill already states clearly that NWIS DV was adopted as primary after the OGC gaps were observed and cross-checked.
