# AI-branch changelog

This log records changes on `ai/evolution` only. It is not the repository
publication changelog (`CHANGELOG.md` on `main`). An entry here is not a
publication to `main` and is not scientific validation.

## 2026-11-21 — Cycle changed to direct commits on `ai/evolution`

- Jordan's cardinal rule: work only on `ai/evolution`, by direct commit.
  No pull requests, no other branches, never `main`.
- Updated `ai/AGENTS/CYCLE.md`, the three agent files, `ai/README.md`, and
  the process / ownership section of `ai/CHARTER.md`. Layer 0 of the
  charter is unchanged. This process amendment was directed by Jordan.
- Cycle is now: A commits a proposal and claims with status `proposed`
  (`[A]`); B commits challenges (`[B]`); C commits the verdict (`[C]`)
  and either promotes the proposal or moves it to `ai/REJECTED/`.
- One commit per role step. Every action still appends `ai/TRAIL.md` and
  every proposal, challenge, and verdict file still opens with a
  plain-English TL;DR.

## 2026-11-21 — Branch README, license notice, and human trail

- Rewrote `ai/README.md` as the labeled AI-evolution branch orientation
  (what the branch is, AI authorship under the charter, not validated
  science, not human-owned `main`, how the three agents work, where to
  start).
- Added a short banner at the top of the root `README.md` on this branch
  only; the rest of that file is unchanged.
- Recorded the repository's GNU Affero General Public License, version 3,
  from `License.md` (Harmonic Knowledge Law (HKL) by Jordan LeDuc; version 3
  or, at the licensee's option, any later version; no warranty), and stated
  that AI-branch content is under the same license.
- Added a commercial licensing contact section pointing at GitHub
  [@Causal5](https://github.com/Causal5), with email marked as not yet
  provided.
- Added `ai/TRAIL.md` as the chronological human landmark log.
- Required every agent action to append a trail entry, and every proposal,
  challenge, and verdict file to open with a plain-English TL;DR
  (`ai/AGENTS/CYCLE.md` and the three agent files).
- No theory, example, or corpus changes beyond these operating-layer and
  banner edits. `main` was not changed.

## 2026-11-21 — Scaffold created

- Added the AI-evolution charter, agent rule files, cycle description, empty
  ledger, and orientation README.
- No theory, example, or code changes to the existing corpus.
- Pinned starting snapshot: `c9e12778aba0014732a8add3c90c5676e5785bf7`.
