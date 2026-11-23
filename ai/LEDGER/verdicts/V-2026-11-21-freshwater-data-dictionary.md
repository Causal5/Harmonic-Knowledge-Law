# V-2026-11-21-freshwater-data-dictionary

> **Source-precedence note (Round 18, 23 November 2026).** Original verdict text is preserved. The dictionary files sit under `Release/Examples/` on this branch only. They are unpublished branch work, not `Release/` on `main`. See `ai/LEDGER/errata/2026-11-23-source-precedence.md`.

**TL;DR.** The dictionary is a useful, honest schema and it does not pretend
to be a finished water study or a test of the framework. Two of the
adversary’s hits were real: some things the protocol says to keep separate
were missing as their own rows, and the official Bite 1 filename could look
more finished than it is. Those are now fixed in this same commit. Official
map boundaries and actual downloaded data are still not chosen, and that
work is still open.

- **Proposal:** `ai/PROPOSALS/2026-11-21-freshwater-data-dictionary/`
- **Verdict:** `accept-with-revisions`
- **Date:** 2026-11-21

## Checks actually run

All checks were run against `ai/evolution` at
`8f21e7017bd2cd4d77585bb58ce233d1b44dd91b`, on the box, without inventing
data. Results:

- **Git scope.** Cycle commits after the pinned `main` snapshot
  `c9e12778aba0014732a8add3c90c5676e5785bf7` do not modify
  `Release/Registry/` or the Central Valley protocol, crosswalk, or study
  README. Remote `main` remains `c9e1277`.
- **Protocol §4 fidelity.** All eleven core time-series variables in
  protocol §4 are present in the CSV. Parsed meaning and preferred unit
  each match the protocol table (no missing variables, no unit mismatches,
  no meaning mismatches).
- **Invented-data scan.** Required fields for official boundary, time
  interval, hydrologic year, source version, retrieval date, method, and
  resolution were unfilled (or explicitly deferred) in the `[A]` CSV.
  Numeric tokens in the file were section and version numbers (for example
  §6.1, v0.3.2), not measured series.
- **Registry consistency.** The current Registry v0.3.2 file and the 16
  and 30 October decision records are byte-identical to `c9e1277`. No
  v0.3.1 definition was rewritten. Many dictionary names are
  domain-scoped or protocol/crosswalk symbols (for example `H_W`,
  `tau_draw`, `\rho_{TM}`) rather than new registry primitives. ASCII
  forms such as `rho_TM` are not always present as raw text in the
  registry; the corresponding TeX forms are. `ANALYSIS_BOUNDARY_*` and
  `COMMON_TIME_INTERVAL` are labeled analysis metadata, not registry
  symbols.
- **Link checks.** Backtick paths in the proposal all resolve. Markdown
  relative links in the proposal, claim, and challenge files: none broken
  (most references are backtick paths). One pre-existing quoted
  Release-relative link inside `ai/CHARTER.md` (copied from
  `Release/ARCHITECTURE.md`) is not part of this proposal and was not
  changed.
- **`tank_model.py`.** Not used by this proposal. As a corpus
  reproducibility check, the script was run in a temporary virtual
  environment with numpy, scipy, and matplotlib. It completed and wrote
  `corrective-dependency-tank-model.png`. That generated file was **not**
  committed. The first system Python run failed with
  `ModuleNotFoundError: No module named 'matplotlib'`.
- **Proposal language.** The proposal does not claim a completed test, a
  computed `V_W`, or empirical validation. Mentions of validation, “Bite 1
  is complete,” and “HKL score” are denials or limits, not completion
  claims.

These checks are consistency and publication-integrity checks. They are not
empirical validation of Temporal Mining or HKL, in the same sense already
stated in `Release/Reviews/definition-validation-2026-10-16.md`.

## Challenge dispositions

- **CH-freshwater-data-dictionary-01-streamflow-net-storage:** **Hit** on
  claim 01. Protocol §4 requires keeping net storage change and streamflow
  capture separate. The `[A]` CSV had no own rows and no exclusive mapping.
  **Revision applied:** added `dG_W_obs(t)` and `streamflow_capture(t)`.
- **CH-freshwater-data-dictionary-01-tau-d:** **Hit** on claim 01.
  `\rho_{TM}=\tau_s/\tau_d` used `\tau_d` without defining it or
  distinguishing it from `tau_d_net`. **Revision applied:** added a `tau_d`
  row that forbids silent identification with `tau_d_net`.
- **CH-freshwater-data-dictionary-01-scope-residue:** **Miss** on claim 01
  as written (the claim is limited to the §4 table plus stated
  separations). The residual gaps are real. **Revision applied:** schema
  rows for `\epsilon_{D_W}`, climate covariates, and well metadata.
  Hydrologic-year, missing-data, and uncertainty *rules* are still not
  defined, only reserved as unfilled fields.
- **CH-freshwater-data-dictionary-04-deliverable-path:** **Does not falsify
  claim 04’s wording** (Bite 1 was not declared complete; the fields were
  unfilled, not omitted). **Hits the artifact:** the protocol’s named
  deliverable path could mislead. **Revision applied:** `dictionary_status`
  row and this directory’s
  `freshwater_data_dictionary_v0.2.NOTES.md`.
- **CH-freshwater-data-dictionary-04-section13-sources:** **Hit** as an
  instrument gap, not as a falsification of claim 04’s “unfilled” wording.
  **Revision applied:** `source_name` for core hydrologic series now records
  candidate classes already named in protocol §13. `source_version` and
  `retrieval_date` remain unfilled. No download was invented.

Claim 02 is **accepted** (unchallenged; registry unchanged; no weights or
cutoff). Claim 03 is **accepted** (unchallenged; no validation claim).
Claims 01 and 04 are **accepted-with-revisions**.

Claim files also had a leftover path `ai/proposal/...` (side-branch style).
Those pointers were changed to `ai/PROPOSALS/...`.

## Residual work (not done here)

- Official Central Valley and San Joaquin boundary identifiers.
- The common time interval and a hydrologic-year definition, with a cited
  convention.
- Missing-data and uncertainty *rules*, not just columns.
- Retrieved source versions and retrieval dates.
- Execution of Bites 2–6, including any High Plains replication.

Those remain for a later cycle or for Jordan, using cited official products
only.

## Action

Proposal marked `accepted-with-revisions`. Revisions above are in this
`[C]` commit. The schema may stand on `ai/evolution`. It is not a `main`
publication and not empirical validation.
