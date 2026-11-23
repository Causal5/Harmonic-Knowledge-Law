# Cycle: direct commits on `ai/evolution`

Each cycle is one proposal. All work is committed **straight to
`ai/evolution`**. There are no pull requests and no side branches. Roles
run in separate sessions, one commit per role step. Nothing in this cycle
writes to `main`.

Jordan's cardinal rule: agents work only on `ai/evolution`, by direct
commit. Never `main`. Never a pull request. Never any other branch.

Source precedence (Jordan, 23 November 2026): `Release/` as published on
`main` is the primary and most up-to-date source. Every other file is
subject to obsolescence. If wording conflicts, `Release/` on `main` wins.
A commit on this branch, including an edit under `Release/`, is not a
publication to `main`. See `ai/CHARTER.md`.

## Roles and order

1. **Work agent (A)** — follows `ai/AGENTS/work.md`. Commits the proposal
   and claims to `ai/evolution` with status `proposed`. Commit message
   prefix: `[A]`.
2. **Adversarial agent (B)** — follows `ai/AGENTS/adversary.md`. Commits
   challenge files to `ai/evolution`. Commit message prefix: `[B]`.
   Does not promote or reject the proposal.
3. **Verification agent (C)** — follows `ai/AGENTS/verifier.md`. Commits
   the verdict to `ai/evolution` with prefix `[C]`, and either promotes
   the proposal (status `accepted` or `accepted-with-revisions`, applying
   any required revisions in that same commit) or moves it to
   `ai/REJECTED/`. Jordan may perform this step instead.

Do not play more than one of these roles in a single session.

## Landmarks and plain English

- Every agent action (opening a proposal, filing challenges, posting a
  verdict, or applying required revisions) **must** append an entry to
  `ai/TRAIL.md`. The entry includes: date (America/New_York), which agent,
  what was done, why, links to the ledger files and the commit, and a
  one-paragraph plain-English “what this means” summary. Newest entries go
  at the top, below the trail introduction.
- Every proposal file under `ai/PROPOSALS/`, every challenge file under
  `ai/LEDGER/challenges/`, and every verdict file under
  `ai/LEDGER/verdicts/` must open with a plain-English **TL;DR** paragraph
  before any technical detail. Claim files under `ai/LEDGER/claims/` should
  do the same.

These landmarks exist so a human can follow the branch without reading every
diff first.

## One proposal per cycle

A proposal is a single scoped change: one definition cluster, one example or
example revision, one formalization, or one code/test change, plus the
ledger entries that describe it. Do not bundle unrelated theory changes.
If the work is larger, split it across later cycles.

Proposal files live under `ai/PROPOSALS/<YYYY-MM-DD>-<slug>/`. The date is
the date the proposal is first committed (America/New_York). The slug is
lowercase ASCII, hyphenated, and short.

## Commit messages

One commit per role step, prefixed as follows:

```
[A] <short description>
[B] <short description>
[C] <short description>
```

Do not combine roles in one commit. Do not commit a proposal, a challenge,
or a verdict to any branch other than `ai/evolution`.

## Proposal record (A fills)

When A commits, include:

- Proposal file(s) under `ai/PROPOSALS/<YYYY-MM-DD>-<slug>/`, opening with
  a TL;DR, and stating parent documents, scope, and status `proposed`.
- Numbered claims, each with a falsifier, as files under `ai/LEDGER/claims/`
  and as rows in `ai/LEDGER/index.md` with status `proposed`.
- A trail entry in `ai/TRAIL.md`.

## Challenge record (B fills)

When B commits, include:

- Challenge files under `ai/LEDGER/challenges/`, each opening with a TL;DR,
  citing a claim ID, a concrete passage or path, and hit/miss criteria.
- Updates to `ai/LEDGER/index.md` linking those challenges.
- A trail entry in `ai/TRAIL.md`.

B does not rewrite the proposal to “fix” it, and does not change claim
status to accepted or rejected.

## Verdict vocabulary (C only)

Only the verifier or Jordan issues a verdict, and only one of:

| Verdict | Meaning | Action on `ai/evolution` |
|---|---|---|
| `accept` | Proposal enters the standing corpus as submitted | Mark claims and the proposal `accepted`; follow promotion steps |
| `accept-with-revisions` | Accepted only with specified fixes | Apply those revisions in the `[C]` commit; mark `accepted-with-revisions`; list any residual work |
| `reject` | Proposal does not enter the standing corpus | Mark `rejected`; move or copy the proposal record to `ai/REJECTED/` with the reason |
| `needs-evidence` | Not accepted; a named evidence gap remains | Leave status `needs-evidence`; do not promote; state the gap and the next step |

Consistency or publication-integrity checks are not empirical validation.

## After the verdict

- Write `ai/LEDGER/verdicts/` (TL;DR first) and update `ai/LEDGER/index.md`.
- Append a trail entry to `ai/TRAIL.md`.
- On `accept` or `accept-with-revisions`, follow `Release/ARCHITECTURE.md`
  promotion steps and add an `ai/CHANGELOG.md` entry. Do not treat the
  commit as a `main` publication, and do not rewrite root `CHANGELOG.md`
  as if it were.
- Never write to `main`. Never open a pull request. Never create a side
  branch.
