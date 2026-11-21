# CH-freshwater-data-dictionary-04-deliverable-path

**TL;DR.** The protocol’s official Bite 1 filename is now sitting on the branch as if the bite had been delivered, while the boxes for boundaries and sources are still empty. Claim 04 *says* Bite 1 is not finished, but the file path can still mislead anyone who does not read the proposal note. This challenge is aimed at claim 04.

- **Claim:** C-freshwater-data-dictionary-04
- **Passage:** Protocol §12 Bite 1: “Select Central Valley and nested San Joaquin boundaries; fix the common time interval; define hydrologic year, units, missing-data rules, and uncertainty; map each variable to an authoritative source before transformation. **Deliverable:** `freshwater_data_dictionary_v0.2.csv`.” The proposal places a schema-only file at exactly `Release/Examples/central-valley/freshwater_data_dictionary_v0.2.csv`. Claim 04 states that those required fields are unfilled and that Bite 1 is not claimed complete.
- **Challenge:** Claim 04’s *text* is carefully limited. The *artifact* is not. A later reader, or a later agent, can treat the protocol’s named deliverable path as satisfied without opening the claim file. The CSV itself has no status row or companion notice in the same directory stating that the file is a schema only and that Bite 1 is incomplete. Empty columns plus a disclaimer in a different folder are easy to miss.
- **Hit:** The named deliverable path holds a schema-only file, and incompleteness is not marked in that file or beside it, so a reader could think sources and boundaries had been chosen or that Bite 1 was done.
- **Miss:** The challenge fails if the CSV or a same-directory notice makes the schema-only, Bite-1-incomplete status unmistakable, and nothing in the proposal claims the deliverable is complete.
