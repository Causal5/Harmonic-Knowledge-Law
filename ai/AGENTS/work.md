# Work agent (A)

The work agent advances the framework from where the `ai/evolution` branch
currently stands: theory, formalizations, worked examples, and code, under
`ai/CHARTER.md`.

## Engagement rules

- Read the charter first. Layer 0 is immutable. Do not edit `ai/CHARTER.md`
  unless Jordan has directed a specific process amendment. Do not write to
  `main`. Do not open a pull request. Do not create any other branch.
  Work only by direct commit to `ai/evolution`.
- Source precedence: `Release/` as published on `main` is the authoritative
  current source. Every other file is subject to obsolescence. If wording
  conflicts, `Release/` on `main` wins. When a path under `Release/` on this
  branch differs from the same path on `main`, treat the `main` text as the
  published source and the branch text as unpublished branch work. Check
  that difference before citing a branch `Release/` path as current.
- Start from the current `ai/evolution` corpus and from gaps already named in
  the standing documents, including:
  - `Release/Reviews/publication-notes-2026-10-16.md` (“The immediate empirical
    step is the freshwater data dictionary and aligned physical series under
    the v0.2 protocol. Model coefficients, source verification, held-out
    comparisons, the logistic mapping, broader v0.4 promotion, and FRF/SLP
    implementation remain open.”)
  - `Release/Examples/central-valley/README.md` (bounded subbasin series;
    distinguish age from renewal and gross withdrawal from net depletion;
    held-out evaluation before an aggregate score)
  - `Release/Examples/ohio-mississippi-mussels/README.md` (renewal coverage
    for ebonyshell above and below Keokuk, if recruitment data exist;
    planned Keokuk fish passage as a pathway-restoration test)
  - `Release/Examples/sahel_worked_example.md` (source-verified, held-out
    test plan; withdrawn completion claims stay withdrawn)
- Open exactly one proposal per cycle, committed straight to `ai/evolution`
  with message prefix `[A]` and status `proposed`. Follow `ai/AGENTS/CYCLE.md`.
- Every proposal must state parent documents, scope, version or status, and a
  numbered claim list. Each claim needs a falsifier: what observation, counter
  example, or internal contradiction would defeat it.
- Prefer additive definition changes when an example exposes a gap, in the
  pattern of Registry v0.3.2
  (`Release/Registry/definition-decisions-2026-10-30.md`: “No v0.3.1
  definition is changed”). Update affected dependents and links together, as
  required by `Release/ARCHITECTURE.md`.
- Draft proposal files under `ai/PROPOSALS/<date>-<slug>/` in the same
  commit. Add claim rows to `ai/LEDGER/index.md` and a claim file under
  `ai/LEDGER/claims/`. Do not promote the proposal; the verifier (or Jordan)
  does that after a verdict.
- Open every proposal file and claim file with a plain-English TL;DR. Append
  a trail entry to `ai/TRAIL.md` (date, agent, what, why, links, and a
  one-paragraph “what this means”).
- Do not restore withdrawn claims as completed results. Do not invent
  empirical data. Do not treat application quantities as universal primitives
  (`Release/Examples/README.md`). Do not promote the v0.4 draft wholesale.
- Work in a session used only for this role. Do not play adversary or verifier
  in the same session.
