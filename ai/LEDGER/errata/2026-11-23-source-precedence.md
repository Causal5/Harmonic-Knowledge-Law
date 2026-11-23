# Erratum: source precedence vs earlier verdicts (Round 18)

**TL;DR.** Jordan’s 23 November 2026 rule is that `Release/` on `main` is the primary and most up-to-date source, and everything else is subject to obsolescence. This file lists earlier `ai/evolution` verdicts (Sessions 1–3 and Round 17) that depended on files outside that published tree, or on `Release/` paths that were edited or added only on this branch. The original verdict texts are preserved. Nothing here rewrites those rulings in place, invents a definition, or publishes branch work to `main`.

**Status:** `accepted-with-revisions` with the Round 18 cycle; attached to the source-precedence proposal. Original earlier-verdict texts remain preserved.

## What was compared

- `main` remains `c9e12778aba0014732a8add3c90c5676e5785bf7`.
- Official Layer 1 papers and the Registry on `ai/evolution` are **identical** to `main`: `Release/Registry/causal-ethics-master-symbol-registry.md`, both October decision records, HKL, AEF, Worldline, Extension, the other reconciled papers, `Release/ARCHITECTURE.md`, `Release/MANIFEST.md`, `Release/README.md`, and `START_HERE.md`.
- `Release/` on the branch is **not** identical to `Release/` on `main`. Nine files were modified on the branch (example README rows; mussel worked-example §8; Sahel logistic-addendum marks; Working-draft marks and README). Many worked fills, protocols, and test plans were **added** under `Release/Examples/` and exist only on this branch. Nothing present in `Release/` on `main` is missing from the branch.

## Intra-`Release/` conflict already on `main`

On `main`, mussel example §8 item 3 (`Release/Examples/ohio-mississippi-mussels/ohio-mississippi-mussels-worked-example.md` line 152) says natural renewal “for ebonyshell above Keokuk after 1913 is effectively zero … so the population carries the registry’s *severed* flag.” The 30 October record on the same `main` tree (`Release/Registry/definition-decisions-2026-10-30.md` line 306) says no field \(\eta_{TM}\) has been computed for the mussel case. Registry §VII.1 defines the flag by a computed \(\eta^{nat}_{TM}=0\). Under `Release/ARCHITECTURE.md` and the 16 October record (both on `main`), the Registry and decision record control the definition. The example sentence is not a computed assignment.

## Dispositions (original verdicts not rewritten)

### Verdicts that rewrote or annotated `Release/` files which still differ on `main`

| Verdict | What the cycle did on the branch | Disposition under the new rule |
|---|---|---|
| `V-2026-11-21-session2-corpus-corrections` (Round 7) | Rewrote mussel §8 item 3 so a qualitative story does not assign *severed*; marked the unpromoted Sahel addendum; fixed `src/_apply_pae`. | **Substance stands**, because it follows AEF, the 16/30 October records, and Sahel §5 **on `main`**. The example and addendum *edits* are **not on `main`**. The published example on `main` still contains the qualitative *severed* sentence; the flag is still governed by the 30 October record, not by that sentence. The `src/` fix is experimental code, not `Release/` on `main`. |
| `V-2026-11-21-working-draft-dead-cites` (Round 10) | In-place dead-cite / stale marks in `Release/Working/` files. | **Marks are branch-only.** The same Working drafts on `main` still have the unmarked wording. That does not change definitions: `Release/Working/` on `main` is already not an override authority (`Release/ARCHITECTURE.md`, 16 October record). |
| `V-2026-11-23-terminology-erratum` (Round 17) | `ai/GLOSSARY.md`; further Working-draft marks; CorePrinciples banners; treated the branch mussel §8 wording as the official example text. | **Map stands** where it cites Registry / AEF / HKL on `main`. Canonical START_HERE cites are re-based in Round 18. The branch example/addendum/Working marks remain unpublished annotations. CorePrinciples banners are on non-`Release/` files (subject to obsolescence). Round 18 amends the glossary; it does not silently rewrite this verdict’s body. |

### Verdicts that added files under `Release/Examples/` which do not exist on `main`

These were accepted as branch notes, protocols, or worked fills. They are **not** in `Release/` on `main` and are therefore not the published example set. The acceptances are not withdrawn; they are marked as unpublished branch work.

| Verdict | Branch-only `Release/` path (not on `main`) |
|---|---|
| `V-2026-11-21-freshwater-data-dictionary` (Round 1) | `Release/Examples/central-valley/freshwater_data_dictionary_v0.2.csv` and notes |
| `V-2026-11-21-hkl-bite5-falsification-checklist` (Round 4) | `Release/Examples/central-valley/hkl_bite5_falsification_checklist_v0.1.md` (and a README row on the branch) |
| `V-2026-11-21-sahel-bounded-test-plan` (Round 5) | `Release/Examples/sahel_bounded_test_plan_v0.1.md` (and a README row on the branch) |
| `V-2026-11-21-ebonyshell-renewal-coverage-protocol` (Round 3) | `Release/Examples/ohio-mississippi-mussels/ebonyshell_renewal_coverage_protocol_v0.1.md` (and a README row on the branch) |
| `V-2026-11-21-keokuk-ld19-status` (Round 12) | `Release/Examples/ohio-mississippi-mussels/worked-fills/2026-11-21-ld19-status/` plus a Session 3 note in the branch mussel example |
| `V-2026-11-21-tulare-lake-dtw` (Round 13) | `Release/Examples/central-valley/worked-fills/2026-11-21-tulare-lake-72019/` |
| `V-2026-11-21-niger-precip-wb` (Round 14) | `Release/Examples/sahel/worked-fills/2026-11-21-niger-precip-wb/` |
| `V-2026-11-21-niger-cereal-yield` (Round 15) | `Release/Examples/sahel/worked-fills/2026-11-21-niger-cereal-yield-wb/` |

### Verdicts grounded in `Release/` on `main` (identical on the branch) or in clearly ratification-pending `ai/` notes

No contradiction with `Release/` on `main` was found. They are listed so the sweep is complete. Original text preserved; no banner required for a conflict, but they are named here.

| Verdict | Note |
|---|---|
| `V-2026-11-21-layer1-consistency-audit` (Round 2) | Findings cite official papers on `main` (identical) and experimental `src/` / unpromoted drafts. `src/` is not `Release/` on `main`. The official-paper findings stand. |
| `V-2026-11-21-computed-status-assignment` (Round 8) | The procedure is an `ai/` note, not in `Release/` on `main`. It applies the 30 October / Registry test, which *is* on `main`. It referred to the branch mussel rewrite as standing corpus text; that rewrite is not on `main`. The rule of use still follows the record on `main`. |
| `V-2026-11-21-application-quantity-inheritance` (Round 6) | `ai/` note; statuses are not official Registry vocabulary. Consistent with “application quantities do not become universal primitives” (`Release/Examples/README.md` on `main`). |
| `V-2026-11-21-object-class-declaration` (Round 9) | Same: ratification-pending `ai/` note. |
| `V-2026-11-21-four-field-effort-recording` (Round 11) | Same: records already defined in AEF §2 / 16 October on `main`. |
| `V-2026-11-21-theory-mab` (Round 16) | `ai/THEORY_MAB.md` is a process aid, not `Release/` on `main`. No contradiction found. |

## What was not done

- `main` was not edited. Branch example and Working-draft marks were not silently reverted or silently copied to `main`.
- No earlier verdict body was rewritten.
- No definition was invented to fill a `needs-definition` term.
