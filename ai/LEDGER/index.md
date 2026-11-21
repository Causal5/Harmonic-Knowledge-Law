# Ledger

Running index of claims, challenges, and verdicts on `ai/evolution`.
One proposal per cycle. IDs are assigned by the work agent when the proposal
is opened. Status starts as `proposed`.

| Claim ID | Date | Proposal | Claim | Challenges | Verdict | Commit | Files |
|---|---|---|---|---|---|---|---|
| C-freshwater-data-dictionary-01 | 2026-11-21 | 2026-11-21-freshwater-data-dictionary | §4 variables and required separations are present and consistent | CH-freshwater-data-dictionary-01-streamflow-net-storage (hit); CH-freshwater-data-dictionary-01-tau-d (hit); CH-freshwater-data-dictionary-01-scope-residue (miss on 01 as written) | accepted-with-revisions | [A] cb3ea10; [B] 8f21e70; [C] this commit | `ai/LEDGER/claims/C-freshwater-data-dictionary-01.md`; `Release/Examples/central-valley/freshwater_data_dictionary_v0.2.csv`; `ai/LEDGER/verdicts/V-2026-11-21-freshwater-data-dictionary.md` |
| C-freshwater-data-dictionary-02 | 2026-11-21 | 2026-11-21-freshwater-data-dictionary | No new primitive; no v0.3.1 rewrite; no weights or cutoff chosen |  | accepted | [A] cb3ea10; [C] this commit | `ai/LEDGER/claims/C-freshwater-data-dictionary-02.md` |
| C-freshwater-data-dictionary-03 | 2026-11-21 | 2026-11-21-freshwater-data-dictionary | Schema is not study execution or empirical validation |  | accepted | [A] cb3ea10; [C] this commit | `ai/LEDGER/claims/C-freshwater-data-dictionary-03.md` |
| C-freshwater-data-dictionary-04 | 2026-11-21 | 2026-11-21-freshwater-data-dictionary | Boundaries, interval, and sources remain unfilled; Bite 1 not claimed complete | CH-freshwater-data-dictionary-04-deliverable-path (artifact hit; wording stood); CH-freshwater-data-dictionary-04-section13-sources (instrument hit); CH-freshwater-data-dictionary-01-scope-residue (residual) | accepted-with-revisions | [A] cb3ea10; [B] 8f21e70; [C] this commit | `ai/LEDGER/claims/C-freshwater-data-dictionary-04.md`; `Release/Examples/central-valley/freshwater_data_dictionary_v0.2.NOTES.md` |
| C-layer1-consistency-01 | 2026-11-21 | 2026-11-21-layer1-consistency-audit | F1: `_apply_pae` treats effort as reducing delta | CH-layer1-consistency-01-authority-scope | proposed |  | `ai/LEDGER/claims/C-layer1-consistency-01.md`; `ai/AUDITS/2026-11-21-layer1-consistency.md` |
| C-layer1-consistency-02 | 2026-11-21 | 2026-11-21-layer1-consistency-audit | F2–F3: import/filename mismatch; random scorers | CH-layer1-consistency-02-import-behavior | proposed |  | `ai/LEDGER/claims/C-layer1-consistency-02.md` |
| C-layer1-consistency-03 | 2026-11-21 | 2026-11-21-layer1-consistency-audit | F4: unpromoted addendum still uses withdrawn sign-change wording | CH-layer1-consistency-03-stale-section-citations | proposed |  | `ai/LEDGER/claims/C-layer1-consistency-03.md` |
| C-layer1-consistency-04 | 2026-11-21 | 2026-11-21-layer1-consistency-audit | Audit does not rewrite Layer 1 papers or validate HKL/PAE | CH-layer1-consistency-04-paper-edits | proposed |  | `ai/LEDGER/claims/C-layer1-consistency-04.md` |
