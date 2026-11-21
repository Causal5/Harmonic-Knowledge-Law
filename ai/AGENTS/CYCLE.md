# Cycle: proposal pull requests into `ai/evolution`

Each cycle is one proposal. The work agent opens a pull request into
`ai/evolution`; the adversarial agent reviews; the verification agent posts a
verdict and merges or closes. Roles run in separate sessions. Nothing in this
cycle writes to `main`.

## Roles and order

1. **Work agent (A)** — follows `ai/AGENTS/work.md`. Creates a proposal branch
   and opens the pull request.
2. **Adversarial agent (B)** — follows `ai/AGENTS/adversary.md`. Reviews and
   files challenges on that pull request. Does not merge.
3. **Verification agent (C)** — follows `ai/AGENTS/verifier.md`. Posts one
   verdict and merges or closes. Jordan may perform this step instead.

Do not play more than one of these roles in a single session.

## Branch naming

Proposal branches are created from the current head of `ai/evolution`:

```
ai/proposal/<YYYY-MM-DD>-<slug>
```

Examples: `ai/proposal/2026-11-21-keokuk-renewal-coverage`.

The date is the date the proposal branch is opened (America/New_York). The
slug is lowercase ASCII, hyphenated, and short. One proposal per branch and
per pull request. The pull request base is always `ai/evolution`, never
`main`.

## One proposal per cycle

A proposal is a single scoped change: one definition cluster, one example or
example revision, one formalization, or one code/test change, plus the
ledger entries that describe it. Do not bundle unrelated theory changes.
If the work is larger, split it across later cycles.

## Pull request title and body

Title:

```
ai/proposal: <short description>
```

Body (copy and fill):

```markdown
## Proposal

- Branch: `ai/proposal/<YYYY-MM-DD>-<slug>`
- Base: `ai/evolution`
- Parent documents:
- Scope:
- Status proposed (draft / additive definition / example / code / test):

## Claims

| Claim ID | Statement | Falsifier |
|---|---|---|
| C-<slug>-01 |  |  |

Ledger claims: `ai/LEDGER/claims/`
Proposal files: `ai/PROPOSALS/<YYYY-MM-DD>-<slug>/`

## Charter compliance

- [ ] Layer 0 unviolated
- [ ] Additive-first relative to Registry v0.3.1 / v0.3.2
- [ ] No write to `main`
- [ ] Withdrawn claims not restored as completed results

## Checks the verifier should run

- (links, algebra, scripts, unit or registry diffs, as applicable)

## Adversary (filled by B)

- Challenge files:
- Review conclusion:

## Verdict (filled by C)

- Verdict: `accept` | `accept-with-revisions` | `reject` | `needs-evidence`
- Verdict file:
- Action: merged / closed / waiting for revisions
```

## Labels (text to apply; create a label on first use if it does not exist)

Use these names if labels are available. If they have not been created yet,
put the same tokens in the pull request body rather than blocking the cycle.

- `ai-cycle`
- `role:work` on the opening; later comments may note `role:adversary` and
  `role:verifier`
- `verdict:accept` / `verdict:accept-with-revisions` / `verdict:reject` /
  `verdict:needs-evidence` (verifier only, when the verdict is posted)

This file does not itself create repository labels.

## Verdict vocabulary

Only the verifier or Jordan issues a verdict, and only one of:

| Verdict | Meaning | Action on the pull request |
|---|---|---|
| `accept` | Proposal may enter `ai/evolution` as submitted | Merge into `ai/evolution` |
| `accept-with-revisions` | Accepted only with specified fixes | Merge after those fixes land, or merge the accepted subset and list residuals |
| `reject` | Proposal does not enter the standing corpus | Close without merging; record under `ai/REJECTED/` |
| `needs-evidence` | Not accepted; a named evidence gap remains | Do not merge; leave open or close with the gap stated |

Consistency or publication-integrity checks are not empirical validation.

## After the verdict

- Update `ai/LEDGER/index.md` and write `ai/LEDGER/verdicts/`.
- On `accept` or an accepted subset, follow `Release/ARCHITECTURE.md`
  promotion steps and add an `ai/CHANGELOG.md` entry. Do not treat the merge
  as a `main` publication, and do not rewrite root `CHANGELOG.md` as if it were.
- Never merge to `main`.
