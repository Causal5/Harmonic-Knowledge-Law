# Sahel bounded test plan v0.1

**TL;DR.** The current Sahel paper already lists a six-step test and has
taken back the old wording that a burden score measurably changed sign
and that the framework had already passed a test. This sheet turns those
six steps into a fill-in plan: what has to be locked before each step,
what would count as a later result, and what is still forbidden. Every
result cell is blank. No burden series is computed. The unpromoted
logistic addendum is not used as authority.

**Status:** accepted-with-revisions (Round 5). Parents:
`Release/Examples/sahel_worked_example.md` §5–§6; Round 2 audit findings
F4–F5; `Release/Examples/README.md` (addendum unpromoted);
`Release/Papers/absorbic-effort-framework.md` §2;
`Release/HKL/hkl-lyapunov.md` §7.

## 1. Standing restrictions (do not lift in this plan)

- The withdrawn wording in current Sahel §5 remains withdrawn. This plan
  does not restore a computed sign change, a passed falsification test,
  or a first empirical anchor for \(\lambda_{PAE}\).
- The logistic addendum is an unpromoted source. It is not an authority
  for this test. Do not use its stale “Sahel §5.1” / “HKL §5.1”
  citations, its treatment of PAE as a number, or its gain function
  \(g_{CE}\) as the test model (Round 2 findings F4–F5). Increasing a
  logistic parameter toward four cannot be assumed to improve fixed-point
  stability (already stated in current Sahel §6 and the 16 October notes).
- Ecological improvement can motivate an HKL interpretation. It is not
  automatically a measurement of \(V\), \(\dot V\), or \(\lambda_{PAE}\).
- No new primitive and no invented series, locations, or citations.

## 2. Predeclarations (all UNFILLED-REQUIRED; lock before any later step is scored)

- **Comparability dimensions (lock before step 2).** Declare, for the
  step 1 contrast, which of the following will be matched and which are
  allowed to differ: place / boundary, observation years, environmental
  setting (for example rainfall or other already-named climate factors),
  institutional setting, intervention, and outcome. “Comparable” is not
  left as an undefined word. All of these fields remain UNFILLED-REQUIRED
  in this version; they are not filled with guessed locations.
- The candidate source list starts from sources already cited in the
  current Sahel paper, plus official retrieved versions of those sources,
  plus primary sources the current paper already identifies or clearly
  asks the reader to consult (including a primary standing behind a
  secondary citation). New source *classes* not pointed to by the current
  paper require a later cycle; do not invent them here.
- The held-out windows and the comparison metric class for steps 5–6:
  a held-out score on the predeclared outcomes. The specific score
  remains UNFILLED-REQUIRED. An in-sample or post-hoc metric is a
  procedure failure, not a scientific result (same rule as Round 4).
- How effort and physical outcomes, including side effects, will be
  recorded separately (step 3). Expenditure is not treated as achieved
  correction.
- The baseline variable list for step 4 (environmental and institutional
  variables), locked before fitting.
- The **local-regulation variable list** for step 5, locked before
  step 5 may be scored, and distinct from the step 4 baseline list.
  Choosing those variables after seeing the held-out score is a
  procedure failure.

## 3. The six steps (results unfilled)

Each step is later marked Fired / Did not fire / Needs-evidence for its
predeclared check, or simply left UNFILLED until evidence exists. Missing
evidence is not a pass. Steps must be taken in order: a normalized burden
candidate is constructed only in step 6, and only after steps 1–5.

| Step | What the current paper already requires | Locked inputs | Result |
|---|---|---|---|
| 1 | Specify comparable locations, observation years, interventions, and outcomes | Comparability dimensions UNFILLED-REQUIRED | UNFILLED |
| 2 | Verify primary historical and ecological sources; record uncertainty | Official versions, including pointed-to primaries, UNFILLED-REQUIRED | UNFILLED |
| 3 | Measure effort and physical outcomes separately, including side effects | Separate series UNFILLED-REQUIRED | UNFILLED |
| 4 | Fit a baseline using relevant environmental and institutional variables | Baseline list locked; no fit is performed here | UNFILLED |
| 5 | Test whether declared local-regulation variables improve held-out results | Local-regulation list and held-out metric class locked; no test is run here | UNFILLED |
| 6 | Only then construct a normalized burden candidate and test its incremental value | Candidate form UNFILLED-REQUIRED; no \(V\) is computed here | UNFILLED |

If step 5 does not improve held-out results, step 6 is not interpreted as
a successful HKL validation. If step 6’s burden candidate does not add
incremental held-out value beyond the step 4–5 models, that is a negative
result, not a reason to restore the withdrawn wording.

## 4. What would later count as a result

- A completed step 2 source-and-uncertainty table, using retrieved
  versions of allowed sources, may be reported without any HKL score.
- A completed step 5 test may support or weaken the local-regulation
  hypothesis without constructing \(V\).
- Only a completed step 6, with locked predeclarations, can speak to
  incremental HKL value. Even then, “passed a falsification test” is not
  automatically restored as a slogan; report the locked metric and the
  comparison.
