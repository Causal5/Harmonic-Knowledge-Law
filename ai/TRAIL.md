# Trail — landmarks for human readers

This is a chronological breadcrumb log of work on `ai/evolution`. It is
written for a human following the branch, not as a substitute for the
ledger or the charter.

Each entry has: the date (America/New_York), which agent (or setup work),
what was done, why, links to ledger files and commits when they exist, and
a one-paragraph plain-English “what this means” summary.

Every agent action on this branch must append an entry here, as required by
`ai/AGENTS/CYCLE.md`. Newest entries go at the top, under this introduction.

---

## 2026-11-21 — Setup: cycle is direct commits only

- **Agent:** setup (direct commit to `ai/evolution`; process change directed by Jordan)
- **What:** Changed the cycle from proposal-branch pull requests into
  `ai/evolution` to direct commits on `ai/evolution` only. Updated the
  cycle guide, the three agent files, the branch README, and the charter's
  process and ownership section. Layer 0 was not changed. Logged the rule
  in `ai/CHANGELOG.md`.
- **Why:** Jordan set a cardinal rule: work only on
  https://github.com/Causal5/Harmonic-Knowledge-Law/tree/ai/evolution,
  committing straight to that branch, with no pull requests and no other
  branches.
- **Links:** `ai/AGENTS/CYCLE.md`, `ai/AGENTS/work.md`,
  `ai/AGENTS/adversary.md`, `ai/AGENTS/verifier.md`, `ai/README.md`,
  `ai/CHARTER.md` (process section only), `ai/CHANGELOG.md`. `main` was
  not changed.
- **What this means:** From this point, a human following the branch will
  see proposal, challenge, and verdict commits land on `ai/evolution`
  itself, labeled `[A]`, `[B]`, and `[C]`. There should be no more
  `ai/proposal/...` side branches and no pull requests for this cycle.

## 2026-11-21 — Setup: branch README, license notice, and this trail

- **Agent:** setup (direct commit to `ai/evolution`, not a proposal cycle)
- **What:** Rewrote `ai/README.md` as the labeled AI-evolution branch guide;
  added a short banner at the top of the root `README.md` on this branch
  only; recorded the AGPL-3 license and a commercial-licensing contact
  path; created this trail; required a trail entry and a plain-English
  TL;DR on every proposal, challenge, and verdict.
- **Why:** Jordan asked that the branch be clearly labeled, that license and
  commercial-contact information be posted, and that “landmarks for the
  meat to follow” be left so a human can walk the history in order.
- **Links:** `ai/README.md`, root `README.md` (banner only), `ai/CHANGELOG.md`,
  `ai/AGENTS/CYCLE.md`, `ai/AGENTS/work.md`, `ai/AGENTS/adversary.md`,
  `ai/AGENTS/verifier.md`. No pull request. `main` was not changed.
- **What this means:** If you are reading this branch, start with
  `ai/README.md`. The science on `main` is unchanged. This trail is the
  running plain-English log of later agent cycles; the next entries will
  point at proposal pull requests, ledger files, and verdicts.
