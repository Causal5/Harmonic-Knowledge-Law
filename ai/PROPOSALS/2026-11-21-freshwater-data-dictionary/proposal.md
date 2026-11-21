# Proposal: Freshwater data dictionary schema (Bite 1)

**TL;DR.** The Central Valley protocol already says the next step is Bite 1: a source-controlled data dictionary and a study boundary, *before* any HKL weights or scores. This proposal adds that dictionary as a schema: every core variable from the protocol is listed with its stated meaning, unit, and required separations (age is not renewal; gross pumping is not net depletion). Official boundaries, the time window, and actual data sources are required fields and are left unfilled. No measurements are invented, and this is not a completed study or a validation of the framework.

## Parent documents

- `Release/Reviews/publication-notes-2026-10-16.md` — “The immediate empirical step is the freshwater data dictionary and aligned physical series under the v0.2 protocol.”
- `Release/Examples/central-valley/temporal-mining-freshwater-protocol-v0.2.md` — §12 Bite 1 deliverable `freshwater_data_dictionary_v0.2.csv`; §14: “Proceed with **Bite 1**.”
- `Release/Examples/central-valley/definition-crosswalk-v0.3.1.md` — “Build a common-boundary data dictionary for stocks, flows, floors, service, and compaction.”
- `Release/Examples/central-valley/README.md` — current working protocol; empirical execution pending; no computed HKL score.
- `Release/Registry/definition-decisions-2026-10-16.md` — Temporal Mining row: separate age, renewal, gross draw, and net time to a declared floor.
- `Release/ARCHITECTURE.md` — promotion and authority rules.
- `ai/CHARTER.md`

## Scope and status

**Status proposed:** working schema / instrument for an already-named empirical step. Not an additive registry revision. Not an executed study.

**In scope**

- A CSV at the protocol’s named path,
  `Release/Examples/central-valley/freshwater_data_dictionary_v0.2.csv`.
- Rows for the §4 core time series and for the balance, floor, timescale, and diagnostic symbols already defined in §5, §6.1, and the crosswalk.
- Required columns for spatial boundary, common time interval, hydrologic year, source name/version/retrieval date, method, resolution, missing-data rule, and uncertainty, all left `UNFILLED-REQUIRED` until an authoritative source is actually mapped.
- Explicit deferral of `V_W`, weights, normalizations, and the §8–§9 audits to later bites, as §14 requires.

**Out of scope**

- Selecting official boundary identifiers or a calendar/hydrologic-year window without a cited official source for that choice.
- Retrieving, inventing, or transcribing numeric series.
- Computing `TM_G`, `tau_draw`, `tau_d_net`, `T_gap`, burdens, or `V_W`.
- Choosing a measure for `E_sw` (the protocol says “declared measure”).
- Promoting Registry v0.3.2 mussel renewal-coverage symbols as required Central Valley fields.
- Executing the High Plains replication, building audit, or Bite 2–6 deliverables.
- Editing `main`.

## What this does and does not mean

Protocol §1 already states that the Temporal Mining pattern “is not, by itself, validation of Causal Ethics, HKL, Delta-Self, or AEF.” Adopting this schema does not change that. Bite 1 is not complete until boundaries, the common interval, and per-variable sources are filled from cited official products (the §13 source stack names candidate agencies, not retrieved versions).

## Claims

| Claim ID | Statement | Falsifier |
|---|---|---|
| C-freshwater-data-dictionary-01 | The CSV includes every core time-series variable from protocol §4, with the stated meaning and preferred unit, and records the separations required by §4, §6.1, §7, and the v0.3.1 crosswalk (including age ≠ renewal, gross draw ≠ net depletion, and declared `Q_net`). | A §4 variable is missing or its meaning/unit contradicts the protocol, or a required separation is omitted or contradicted. |
| C-freshwater-data-dictionary-02 | The dictionary introduces no new registry primitive, does not change a v0.3.1 definition, follows the crosswalk’s domain-scoped names, and does not select HKL weights, normalizations, or a `rho_TM` cutoff. | A new primitive is treated as registered, a v0.3.1 meaning is rewritten, or weights/`V_W`/a cutoff are chosen or computed. |
| C-freshwater-data-dictionary-03 | Adopting this dictionary is not execution of Bites 2–5, not a computed HKL score, and not empirical validation of Temporal Mining or HKL. | The proposal text claims a completed test, a computed `V_W`, or validation. |
| C-freshwater-data-dictionary-04 | Official boundary identifiers, the common time interval, hydrologic-year definition, and per-variable authoritative source mappings are required and currently unfilled; this proposal does not claim that Bite 1 is complete. | The proposal claims Bite 1 is complete, or those fields are omitted so a reader could think sources and boundaries had been chosen. |

Claim files: `ai/LEDGER/claims/`.

## Suggested verifier checks

- Confirm every protocol §4 variable appears in the CSV with matching meaning and preferred unit.
- Confirm unfilled required fields are actually empty of invented sources, boundaries, and numbers.
- Confirm no silent edit to Registry v0.3.1 / v0.3.2 files in this pull request.
- Confirm relative links in this proposal resolve.
- `Release/Registry/figures/tank_model.py` is not used by this proposal; no change to it is claimed.
