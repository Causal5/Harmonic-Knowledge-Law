# AI Evolution Branch (`ai/evolution`)

This is the README for the **AI-evolution branch**, not for the human-owned
publication line on `main`.

## What this branch is

`ai/evolution` is an AI-authored working corpus. It starts from `main` at
`c9e12778aba0014732a8add3c90c5676e5785bf7` and may be revised by three
structural agents under [`CHARTER.md`](CHARTER.md). The charter's Layer 0
premise is immutable; Layer 1 (Registry v0.3.2 and the reconciled papers)
may be extended only through the cycle in [`AGENTS/CYCLE.md`](AGENTS/CYCLE.md).

This branch is **not validated science**. Publication or a commit on
`ai/evolution` is not empirical validation, and adopting a definition is not
evidence that a hypothesis is true. Those limits are already stated in
`Release/Reviews/publication-notes-2026-10-16.md` and `ai/CHARTER.md`.

This branch is **not** the human-owned main line. `main` remains Jordan's
publication branch (GitHub: [Causal5](https://github.com/Causal5)). Agents
work **only** on `ai/evolution`, by direct commit. They must not write to
`main`, open pull requests, or create other branches. Charter Layer 0
amendments are only by Jordan.

## How the three agents work

Each cycle is one proposal, committed straight to `ai/evolution`:

1. **Work agent (A)** — [`AGENTS/work.md`](AGENTS/work.md) — advances the
   framework from where this branch stands (theory, examples, code) under
   the charter. Commits a proposal and claims with status `proposed`.
   Message prefix: `[A]`.
2. **Adversarial agent (B)** — [`AGENTS/adversary.md`](AGENTS/adversary.md)
   — probes weaknesses, fallacies, and falsifiers. Commits challenge files.
   Message prefix: `[B]`. Does not promote or reject.
3. **Verification agent (C)** — [`AGENTS/verifier.md`](AGENTS/verifier.md)
   — checks claims, math, code, and examples; commits one verdict
   (`accept`, `accept-with-revisions`, `reject`, or `needs-evidence`);
   promotes the proposal or moves it to `ai/REJECTED/`. Message prefix:
   `[C]`. Jordan may do this step instead.

Roles run in separate sessions, one commit per role step. Every agent
action appends an entry to [`TRAIL.md`](TRAIL.md), the breadcrumb log for
human readers. Every proposal, challenge, and verdict file starts with a
plain-English TL;DR.

## Where to start reading

1. This file, then [`TRAIL.md`](TRAIL.md) (what happened, in order, in plain English).
2. [`CHARTER.md`](CHARTER.md) — premise, pinned snapshot, redefinition bounds.
3. [`AGENTS/CYCLE.md`](AGENTS/CYCLE.md) — how a cycle is run.
4. The existing human corpus, beginning at [`../START_HERE.md`](../START_HERE.md)
   and the [definition decisions](../Release/Registry/definition-decisions-2026-10-16.md).
5. The ledger: [`LEDGER/index.md`](LEDGER/index.md).
6. This branch's changelog: [`CHANGELOG.md`](CHANGELOG.md) (not the root
   `CHANGELOG.md`, which records `main` publications).

## License

The repository license is the GNU Affero General Public License, version 3,
in [`License.md`](../License.md). That file is headed:

> GNU Affero General Public License (AGPL) Version 3
>
> Harmonic Knowledge Law (HKL) by Jordan LeDuc
>
> This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
>
> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

`License.md` also states that “This License” refers to version 3 of the GNU
Affero General Public License, and points to
<https://www.gnu.org/licenses/agpl-3.0.html>.

Content added on `ai/evolution`, including this directory, is under the same
license. The copyright holder named in `License.md` is Jordan LeDuc; the
repository owner is [Causal5](https://github.com/Causal5).

## Commercial licensing

The AGPL-3 terms in `License.md` are the default public license, including
the option to charge for distribution of copies. For **commercial licensing
or leasing** of this work in a way that would sit *outside* those AGPL-3
terms (for example, a separate proprietary license or lease), contact the
repository owner through GitHub: [@Causal5](https://github.com/Causal5).

**Email contact:** not provided yet. This line may be updated later with an
address if the owner adds one. Do not invent an email address.
