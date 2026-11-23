# V-2026-11-21-sahel-bounded-test-plan

> **Source-precedence note (Round 18, 23 November 2026).** Original verdict text is preserved. The test-plan file is not in `Release/` on `main`. Unpublished branch work. See `ai/LEDGER/errata/2026-11-23-source-precedence.md`.

**TL;DR.** The plan is a genuine blank recipe for the current Sahel
paper’s six-step test. Withdrawn wording was not restored, the logistic
addendum was not used as authority, and no series were invented. All
three challenges hit and were fixed: the local-regulation variable list
must be locked before step 5; comparability dimensions must be declared;
and primary sources the current paper already points to may be retrieved.

**Proposal:** `ai/PROPOSALS/2026-11-21-sahel-bounded-test-plan/`
**Verdict:** accept-with-revisions
**Date:** 2026-11-21

## Challenge outcomes

| Challenge | Claim | Outcome | Reason |
|---|---|---|---|
| CH-sahel-test-01-local-regulation-list | C-sahel-test-01 | hit | Step 5 treatment variables were not a locked predeclaration. Added. |
| CH-sahel-test-01-comparable-dimensions | C-sahel-test-01 | hit | “Define comparable in writing” had no required dimension fields. Added, still unfilled. |
| CH-sahel-test-02-primary-sources | C-sahel-test-02 | hit | “Already cited” could block pointed-to primaries. Retrieval of those primaries is now allowed; new source classes are still forbidden. |

## Claim verdicts

| Claim | Verdict | Notes |
|---|---|---|
| C-sahel-test-01 | accepted-with-revisions | Six steps in order held; locks added. |
| C-sahel-test-02 | accepted-with-revisions | Withdrawal and addendum bar held; source rule clarified. |
| C-sahel-test-03 | accepted | All required fields remain unfilled; not claimed as validation. |

## Mechanical checks (this box)

- Result cells and location/series fields are UNFILLED or UNFILLED-REQUIRED. No \(V\) or \(\lambda_{PAE}\) value is filled.
- [A] `a06b66b` did not modify `sahel_worked_example.md`.
- Confirmed standing restrictions keep §5 withdrawal and reject addendum authority.
- Confirmed the pre-revision text locked a step-4 baseline list but not a step-5 local-regulation list, and had no comparability-dimension fields.

## Revisions applied in the verdict commit

- Comparability dimensions, local-regulation variable list, and primary-source retrieval clarification.
- Examples README row for this plan.
- Claim statuses and ledger updated. The current Sahel paper body was not edited.

## Residual / later work

- Official locations, sources, series, and the specific held-out score still need evidence.
- The current paper’s withdrawn wording stays withdrawn unless a later, locked test supports a carefully worded new claim.
