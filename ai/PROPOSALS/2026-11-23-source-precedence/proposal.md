# Proposal: Source precedence — Release on main (Round 18)

**TL;DR.** Jordan directed that the files in `Release/` on `main` are the primary and most up-to-date source, and that everything else is subject to obsolescence. This cycle writes that rule into the charter and the agent files. It rechecks the Round 17 glossary against `Release/` on `main` (no new definitions invented). It lists earlier verdicts that rest on branch-only `Release/` edits or on non-`Release/` files, and marks them in the ledger without rewriting their original text. Official papers and the Registry already match `main`. The mussel example and several added example files on this branch do not.

**Status:** `proposed`

**Round:** 18 (23 November 2026, America/New_York). Jordan-directed charter amendment (t13u) and authorized run.

## Parent documents

- Jordan’s direction: `Release/` on `main` is primary; everything else is subject to obsolescence.
- `ai/CHARTER.md` (this cycle amends it as directed)
- `Release/` on `main` at `c9e12778aba0014732a8add3c90c5676e5785bf7`
- `ai/GLOSSARY.md` (Round 17, amended here for precedence)
- Earlier verdicts under `ai/LEDGER/verdicts/`

## Scope

In scope: charter and agent-rule amendments; glossary recheck and re-base; comparison of `Release/` on `main` vs this branch; ledger erratum and verdict notes. Out of scope: writing to `main`; inventing definitions; silently reverting or silently publishing branch `Release/` edits; developing a theory arm.

## Comparison (summary)

Official Layer 1 papers and Registry v0.3.2 are identical on `main` and `ai/evolution`. Nine `Release/` files differ on the branch (example README rows; mussel §8; Sahel addendum marks; Working-draft marks). Worked fills and protocols were added under `Release/Examples/` on the branch only. On `main`, mussel §8 item 3 still assigns the *severed* flag qualitatively, which conflicts with the 30 October record on the same tree; the record and Registry control the flag.

## Claims

- `C-prec-01` — Charter and agent files now state the source-precedence rule; Layer 0 locked quotes remain; non-`Release/` files do not outrank `Release/` on `main`.
- `C-prec-02` — Glossary rechecked against `Release/` on `main`; START_HERE cites re-based; needs-definition list updated; no invented definitions.
- `C-prec-03` — Earlier verdicts swept and marked in `ai/LEDGER/errata/2026-11-23-source-precedence.md` and in notes on the affected verdict files; original verdict bodies preserved.

## Files

- `ai/CHARTER.md`, `ai/AGENTS/CYCLE.md`, `work.md`, `adversary.md`, `verifier.md`, `ai/README.md`
- `ai/GLOSSARY.md`
- `ai/LEDGER/errata/2026-11-23-source-precedence.md` and source-precedence notes on listed verdicts
- This proposal, claims, trail, and ledger index
