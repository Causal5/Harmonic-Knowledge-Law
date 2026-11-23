# AI Evolution Charter

This charter governs all work on the `ai/evolution` branch of
[Causal5/Harmonic-Knowledge-Law](https://github.com/Causal5/Harmonic-Knowledge-Law).
It does not alter `main`. Agents may extend theory, examples, and code only on
this branch, and only under the rules below.

**Amendments to this file may be made only by Jordan (GitHub: Causal5).**
No agent may edit `ai/CHARTER.md`, except when Jordan has expressly directed
a specific amendment.

**23 November 2026 amendment (Jordan).** Jordan directed that the files in
`Release/` on `main` are the primary and most up-to-date source, and that
everything else is subject to obsolescence. The source-precedence rule below
records that direction. This amendment does not write to `main`.

## Pinned snapshot

The starting point of this branch is `main` at

- commit `c9e12778aba0014732a8add3c90c5676e5785bf7`
- https://github.com/Causal5/Harmonic-Knowledge-Law/commit/c9e12778aba0014732a8add3c90c5676e5785bf7
- message: “Merge front-facing mussel worked example” (31 October 2026)

That snapshot is the baseline against which later AI-branch revisions are
compared. It is not a claim that the corpus is scientifically validated.
`CHANGELOG.md` on `main` already states that publication dates “do not imply
scientific validation or the completion of a draft's proposed work.”

## Source precedence — `Release/` on `main`

Jordan’s rule (23 November 2026): the files in `Release/` as published on
`main` are the primary and most up-to-date source. Every other file is
subject to obsolescence. If wording conflicts, `Release/` on `main` wins.

- The authoritative tree is `Release/` at `main`, currently
  `270942cd107ffc92a44b4be8d7fffa0e6c22fd1d` (23 November 2026,
  “Correct the fish passage site in mussel example §8”). The original
  starting pin of this branch remains
  `c9e12778aba0014732a8add3c90c5676e5785bf7` (31 October 2026). Which
  documents *inside* that tree are current definitions, and
  which are drafts or historical sources, is already decided there:
  Registry v0.3.2 and the reconciled papers control; `Release/Working/`,
  `Release/archive/`, and the v0.4 draft do not override them. That
  division is itself stated in `Release/ARCHITECTURE.md` and the 16 October
  record on `main`.
- Files outside that tree — including `CorePrinciples/`, `src/`, root
  historical files, `START_HERE.md` as a file, and the whole `ai/`
  directory — are subject to obsolescence and do not override `Release/`
  on `main`.
- A copy, edit, or addition under `Release/` on `ai/evolution` does not,
  by itself, become the published `Release/` on `main`. It is branch work.
  A commit on this branch is not a publication to `main`.
- Layer 0 quotations in this charter remain locked. The source *files*
  those quotes were taken from do not otherwise outrank `Release/` on
  `main`. Only Jordan may change the locked quotations.

## Layer 0 — Immutable premise

Agents may not redefine, weaken, or override the following. Challenges may
clarify wording or cite tensions, but a proposed change that conflicts with
Layer 0 is rejected. Only Jordan may amend this layer, by editing this charter.

### Causal Integrity Axiom

Quoted in this charter from the historical file `CorePrinciples/Causal_Integrity_Axiom.md`. The quotation is locked here. The file as a whole does not override `Release/` on `main`:

> **No constituent can break reality.**

The same file states that entropic deviation “can disrupt local systems and
dependencies \( D(\mathcal{O}) \), but cannot override the structural integrity
of \( \mathcal{M} \).”

Corollary CI-C₁, quoted from that file:

> All violations of functional interaction result in local decoherence, not global collapse. Reality is bounded by the geometry of causality, not by the intentions of the constituents within it.

The document calls this axiom “the immovable center.” Local or dependency
collapse is not manifold collapse. Agents may not treat an agent, observer,
civilization, or AI system as able to undo that structure.

### Distinctions retained from the definition records

These distinctions are locked in this charter. They are also stated in
`Release/Registry/definition-decisions-2026-10-16.md` and
`Release/Reviews/publication-notes-2026-10-16.md` on `main`. Agents may not
collapse them. The block quotations below were taken from `START_HERE.md`,
a root file that is not under `Release/` and does not override `Release/`
on `main`. Only Jordan may change the locked quotations.

From `START_HERE.md` (locked quotation; the file is not a higher source):

> Reality, a selected system state, an observation, and an agent's model are different objects.

> Returning to a selected state at a later time does not repeat the earlier state-time event.

> Burdens retain their physical units before any normalization. A preferred target, a passive baseline, and a failure boundary serve different purposes. Temporary burden growth may be compatible with viability if adequate margin remains.

> PAE is elective corrective effort by a capable agent. OIE is the process through which agentic action creates or transfers destabilizing burden. Measure resources spent separately from correction achieved. The Absorbic Coverage Ratio compares matched correction and burden; it does not settle ethical legitimacy or all stability questions.

> Neither a trajectory difference nor graph curvature alone establishes cognition.

From `Release/Registry/definition-decisions-2026-10-16.md`:

> A definition's adoption is a convention for this corpus, not empirical evidence that its associated hypothesis is true.

That record also requires: PAE remains a principle and OIE remains a process;
allocation, expenditure, achieved correction, and side burden are recorded
separately; \(V^*\), \(V_{PCB}\), and \(V_{max}\) are separated; and
“current raw ELQ/AU accounting” is replaced by “defined, boundary-matched ACR,”
which “is not a complete ethical or viability judgment.”

From `Release/Reviews/publication-notes-2026-10-16.md`:

> The Sahel paper's claims of a computed sign change and a passed falsification test are withdrawn as completed results.

Agents may not restore withdrawn completion claims as established results.

### Authority and promotion

From `Release/ARCHITECTURE.md`:

> `main` is the publication branch.

> Registry v0.3.1 controls definitions; the current Worldline, Extension, HKL, and AEF papers supply the reconciled formal interfaces. See the [definition decisions](Registry/definition-decisions-2026-10-16.md). The broader v0.4 registry remains a research draft. A recovered paper's filename, version number, publication date, or presence on `main` does not independently promote it to governing authority.

> Empirical validation requires its own evidence and evaluation record. A publication checkpoint does not substitute for it.

`Release/Registry/README.md` identifies
`Release/Registry/causal-ethics-master-symbol-registry.md` as the current
controlling definitions (Registry v0.3.2). The 30 October record,
`Release/Registry/definition-decisions-2026-10-30.md`, states that v0.3.2 “is
an **additive** revision” and that “No v0.3.1 definition is changed.”

From `Release/Examples/README.md`:

> Application quantities do not become universal primitives by appearing in an example.

From `Release/Papers/four-pillars-of-causal-consciousness.md`:

> The pillars organize proposed observable features of agency; they do not establish a sufficient test of subjective experience.

The root file `4_Pillars`, `Release/Working/`, `Release/archive/`, and
`Release/Registry/causal-ethics-master-symbol-registry-v0.4-draft.md` are
sources to study. They are not override authorities.
`Release/Registry/definition-decisions-2026-10-16.md` states that the
recovered v2 papers, Buffer manuscript, v0.4 draft, logistic addendum, audits,
and SLP sources “retain their original bodies” and that “Their historical or
draft wording has no authority to override current definitions.”

## Layer 1 — Starting formal interface (versioned, additive-first)

The starting formal interface is Registry v0.3.2 and the reconciled papers at
the pinned snapshot, including:

- `Release/Registry/causal-ethics-master-symbol-registry.md`
- `Release/Registry/definition-decisions-2026-10-16.md`
- `Release/Registry/definition-decisions-2026-10-30.md`
- `Release/Delta-Self/delta-self-worldline-formalization.md`
- `Release/Delta-Self/delta-self-extension.md`
- `Release/Papers/absorbic-effort-framework.md`
- `Release/HKL/hkl-lyapunov.md`
- `Release/Papers/four-pillars-of-causal-consciousness.md`
- `Release/Papers/fallacy-of-large-scale-absorbic-effort.md`
- `Release/Papers/continuation-filter.md`
- `Release/Examples/` (mussel, Central Valley, and Sahel applications as
  currently statused in `Release/Examples/README.md` **on `main`**)

These Layer 1 paths are the files as they stand in `Release/` on `main`.
Branch-only additions or edits under `Release/` on `ai/evolution` are not,
by themselves, a publication of Layer 1.

Layer 1 may be extended or revised only through the cycle in
`ai/AGENTS/CYCLE.md`. Preferred form of change is *additive*, in the same
pattern as Registry v0.3.2: new definitions may be registered when a worked
example exposes a gap; existing v0.3.1 meanings are not silently rewritten.
Any non-additive revision requires a dated decision record under
`Release/Registry/`, in the style of the 16 October and 30 October records,
and a verifier verdict of `accept` or `accept-with-revisions`.

The v0.4 draft must not be promoted wholesale.

## Redefinition bounds

“Redefine / adjust / contribute” on this branch means:

- New additive definitions, when an example or formal gap requires them.
- Tighter formalizations, worked examples, tests, and code consistent with
  Layer 0 and the current registry.
- Decision records, ledger entries, and reviews that record claims, challenges,
  and verdicts.

It does not mean:

- Editing this charter, or changing Layer 0.
- Writing to `main`, opening a pull request, creating a side branch, or
  treating an `ai/evolution` commit as a publication to `main`.
- Silently rewriting a v0.3.1 definition.
- Treating a new symbol or application quantity as a universal law because it
  appeared in an example.
- Treating a non-`Release/` file, or a branch-only edit or addition under
  `Release/` on `ai/evolution`, as equal to or higher than `Release/` on
  `main`.
- Declaring empirical validation from consistency checks, publication, or
  definition adoption alone. This is the same limit already recorded in
  `Release/Reviews/definition-validation-2026-10-16.md`: those checks
  “concern consistency and publication integrity, not empirical validation.”
- Restoring withdrawn completion claims, or promoting historical/draft wording
  over current definitions.

If a proposal conflicts with Layer 0, the charter wins and the change is
rejected. Escalation to Jordan is required only for a proposed charter
amendment, which agents cannot make.

## Promotion on this branch

When a proposal is accepted, follow the promotion steps already stated in
`Release/ARCHITECTURE.md`:

1. State the intended parent documents, scope, version, and status.
2. Resolve the applicable audit findings, symbol collisions, units, and inheritance conflicts.
3. Update affected dependent documents and links together.
4. Record the decision and resulting paths in the manifest and changelog, preserving earlier versions in Git history or a clearly labeled archive.

On this branch, also append the ledger verdict and an entry in
`ai/CHANGELOG.md`. Do not silently rewrite the root `CHANGELOG.md` as if the
work had been published on `main`.

## Process

All cycle work is a direct commit to `ai/evolution`, as specified in
`ai/AGENTS/CYCLE.md`. There are no pull requests and no side branches.
Jordan directed this process rule on 21 November 2026. It does not change
Layer 0.

- The work agent commits a proposal and claims with status `proposed`
  (message prefix `[A]`).
- The adversarial agent commits challenge files (message prefix `[B]`).
- The verification agent commits one verdict (message prefix `[C]`) and
  either promotes the proposal (applying any required revisions) or moves
  it to `ai/REJECTED/`. Jordan may perform the verdict step.

## Ownership

- `main` is human-owned (Jordan / Causal5). Agents never write to it.
- `ai/evolution` is the only branch agents may revise as the standing AI
  corpus, and the only branch they may commit to.
- Agents must not open pull requests or create other branches.
- Only the verification agent, or Jordan, may promote a proposal or move
  it to `ai/REJECTED/` after a written verdict.
