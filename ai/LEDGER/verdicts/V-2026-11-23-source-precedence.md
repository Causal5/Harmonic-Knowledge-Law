# V-2026-11-23-source-precedence

**TL;DR.** Accept with revisions. Jordan’s rule is now in the charter and the agent files: `Release/` on `main` is the primary and most up-to-date source, and everything else is subject to obsolescence. Official papers already match `main`. The glossary was rechecked; AU’s *status* is reserved/undefined there, and the other needs-definition terms are still undefined. Earlier verdicts were listed and marked, not silently rewritten. Three challenges hit leftover wording that still treated branch or root files as current. Those lines are corrected in this commit. No definition was invented. `main` was not edited.

**Verdict:** `accepted-with-revisions`

**Round:** 18 (23 November 2026, America/New_York)

## Claims

- **C-prec-01 — accept with revisions.** The charter, `CYCLE.md`, `work.md`, `adversary.md`, `verifier.md`, and `ai/README.md` state the source-precedence rule. Layer 0 quotations remain locked. Official Layer 1 paths are the files as they stand on `main`. Both challenges to this claim hit and are fixed in this commit:
  - `CH-prec-01-workmd-branch-readmes` — hit. `ai/AGENTS/work.md` still named the Central Valley and mussel example READMEs as standing starting documents without saying “on `main`.” Those two files differ on this branch (added rows for the Bite 5 checklist and the ebonyshell protocol). The standing-document list now cites the `main` text and notes the unpublished branch rows.
  - `CH-prec-01-start-here-called-current` — hit. Layer 0 still headed the locked quotations “Distinctions retained from the current introduction and definition records” and presented `START_HERE.md` first as the statement of current wording. The heading and intro now cite the 16 October records on `main` first, and treat `START_HERE.md` as the historical source of locked quotations, not as a higher source. No locked quotation was dropped or rewritten.
- **C-prec-02 — accept with revisions.** Canonical glossary cites were re-based to `Release/` on `main`. START_HERE cites in the term entries are pointers. A7, A8, A13, and section B1 already distinguished `main` from the branch. AU’s *status* is reserved/undefined (Registry line 231 and AEF §6 line 158 on `main`) and still has no unit definition. HKL-AI Score, SRI, HRS, Axis as an official symbol, Variation-\(\Delta\) formulas, manuscript \(\mathcal{C}(t)\) / \(J_{PAE}\) and related primitives, and the Round 6–9 process labels remain `needs-definition` or not official vocabulary. Official buffer remains \(\tau^\pi_{buf,\Omega}\) (A10). No definition was invented. The one challenge hit and is fixed in this commit:
  - `CH-prec-02-glossary-already-aligned` — hit. The treatment table and section C still called the mussel §8 rewrite, Sahel addendum marks, and ebonyshell protocol “already aligned.” Those inventory lines now record them as unpublished branch work, and the residual-risk bullet now separates ordinary-language “severed” (example line 40) from the still-published `main` flag-assignment sentence at §8 item 3.
- **C-prec-03 — accept.** No challenge was filed. The erratum lists all seventeen earlier verdicts (Sessions 1–3 and Round 17), preserves their original bodies, documents the `Release/`-on-`main` vs branch differences (identical official papers; nine modified files; added fills/protocols; the intra-`main` mussel §8 vs 30 October conflict), and marks affected verdicts with an additive note. Branch work is not claimed as a publication to `main`.

## Revisions applied in this commit

- `ai/AGENTS/work.md`: standing example-README bullets now cite `main` and note the unpublished branch rows.
- `ai/CHARTER.md`: Layer 0 heading and intro no longer call `START_HERE.md` “the current introduction”; locked quotations are unchanged.
- `ai/GLOSSARY.md`: treatment table, section C inventory, and the residual *severed* bullet re-based to `Release/` on `main`.

## Notes

- A was split across seven commits (`888fbbc`, `cb3ed67`, `7b19f59`, `bae05bd`, `c1f8efb`, `52569d7`, `4c4b811`) and B across two (`1785ec9`, `ae14c2e`) because `push_files` accepts at most four `$file:` arguments per call. The cycle still used only `ai/evolution` direct commits. `main` remains `c9e12778aba0014732a8add3c90c5676e5785bf7` and was not changed.
- Earlier verdicts were marked, not rewritten. Branch `Release/` edits were not silently reverted or silently copied to `main`.
- Residual work not done in this cycle: `CorePrinciples/SLP_Published.md` remains unbannered (historical, not `Release/` on `main`); experimental `src/` still contains *SRI* / *HRS* / *HKL-AI Score* names; branch `Release/` files themselves were not given a file-level “unpublished vs `main`” banner (the difference is recorded in the erratum); the intra-`main` conflict between mussel §8 item 3 and the 30 October record remains on `main`, which agents cannot edit.
- This cycle is not a theory arm. No definition, formula, or unit was invented.
