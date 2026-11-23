# Proposal: Terminology map and erratum (Round 17)

**TL;DR.** This cycle writes `ai/GLOSSARY.md` as a map from current Registry v0.3.2 / reconciled-paper wording to stale wording still in working drafts and historical CorePrinciples files. It does not invent definitions. Official Layer 0 and Layer 1 papers are not rewritten. Working drafts get in-place marks (HKL v2 is finally bannered; leftover PAE-as-number, AU, and \(PAE=E-C_{pae}\) wording in AEF v2 and the buffer draft is marked). Historical glossaries get a status banner that preserves the original text. Terms with no official definition are flagged `needs-definition`. This is not a base-theory arm. The `ai/` directory, including `THEORY_MAB.md` and `PROPOSALS/`, exists on `ai/evolution` and not on `main`; branch READMEs now say that plainly so the folder is findable if someone is looking at `main`.

**Status:** `accepted-with-revisions`

**Round:** 17 (23 November 2026, America/New_York). One terminology cycle after Session 3.

## Parent documents

- Registry v0.3.2: `Release/Registry/causal-ethics-master-symbol-registry.md`
- `Release/Registry/definition-decisions-2026-10-16.md` and `definition-decisions-2026-10-30.md`
- Current papers: `Release/HKL/hkl-lyapunov.md`, `Release/Papers/absorbic-effort-framework.md`, `START_HERE.md`
- Layer 0 / process: `ai/CHARTER.md`, `ai/AGENTS/CYCLE.md`
- Prior term-issue log: Session 1–3 challenges and verdicts under `ai/LEDGER/`, `ai/CHANGELOG.md`, especially Rounds 2, 7, 8, and 10
- Computed-status note: `ai/NOTES/computed-status-assignment-v0.1.md`
- Theory-move gate: `ai/THEORY_MAB.md` (Round 16). This cycle is explicitly not registered as an arm.

## Scope

In scope:

- Consolidate term issues already logged in the ledger and changelog, then search the corpus for further instances.
- Add `ai/GLOSSARY.md` as a canonical term map built only from existing official definitions, with file and line citations.
- For Layer 0 / official Layer 1 text: mapping and marked notes only; no body rewrite. The Causal Integrity Axiom file is not edited.
- For working drafts and historical CorePrinciples / `ai/` files: in-place marks or banners, original wording preserved.
- Flag terms that have no official definition as `needs-definition`.
- Record, on this branch only, that `ai/` is absent from `main`.

Out of scope:

- Registry amendments, new primitives, restored Sahel completion claims, computed \(\eta\) / *severed* assignment, Bite 5 scoring, or any `THEORY_MAB` arm development.
- Invented replacement formulas or section numbers.
- Silent cleanup of experimental `src/` score function names.

## Claims

- `C-term-01` — The glossary is a mapping-only erratum: no invented definitions; official sources are cited; undefined terms are flagged `needs-definition`; this is not a theory arm.
- `C-term-02` — Listed stale presentations are marked or bannered in place without rewriting official Layer 0/1 papers; original wording is preserved.

## Files (this cycle, status proposed)

- `ai/GLOSSARY.md`
- In-place marks / banners: `Release/Working/hkl-lyapunov-v2.md`, `absorbic-effort-framework-v2.md`, `buffer-as-temporal-dimension.md`, `Release/Working/README.md`; `CorePrinciples/Glossary.md`, `Law_of_We_Full.md`, `CausalEthicsAxis.md`
- Visibility notes: root `README.md` (branch banner only), `ai/README.md`
- `ai/THEORY_MAB.md` — short note that Round 17 is not an arm
- This proposal, claims, trail, and ledger index rows
