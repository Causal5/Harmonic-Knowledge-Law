# Sync check: published hydrological PAE pages, `main` vs `ai/evolution`

> **Unpublished branch work (ai/evolution, Launch Pad Session 2, Round 25, 25 November 2026).** Not a publication to `main`.

**TL;DR.** After Jordan’s 25 November commits, the two published PAE files are already byte-identical on `main` at `37522fc` and on `ai/evolution` at `9edff38`. No further content sync of those files was required. The branch-only Examples README banner still pointed at stale `main` `56c6ab5`; that pin is updated to `37522fc` in this round. Official papers, the Registry, and the publication changelog already match.

## Branch tips compared (25 November 2026, America/New_York)

| Ref | SHA | Tip subject |
|---|---|---|
| `origin/main` | `37522fc58eefe6b9d7948f41fa1332405acc1803` | Document hydrological PAE in Maharashtra with cited field findings |
| `origin/ai/evolution` | `9edff38a2b68fae79c80c102712134422169705f` | [sync] Carry the Paani worked example and field findings from main |

`main` moved from Session 1’s `56c6ab5` by four commits (25 November dates are America/New_York):

- `fa8da68` (24 Nov 2026, 18:37) Introduce three watershed models in the Central Valley worked example
- `44e371c` (24 Nov 2026, 19:24) Ground the Tulare recharge comparison in observed runoff delays
- `8b413ab` (24 Nov 2026, 20:18) Review Water Cup evidence and clarify Tulare pumping, recharge and storage accounting
- `37522fc` (25 Nov 2026, 17:48) Document hydrological PAE in Maharashtra with cited field findings

`ai/evolution` already carried those pages in two copy-sync commits, `cdfc4d8` (from `main` `8b413ab`) and `9edff38` (from `main` `37522fc`). The main SHAs are not ancestors of this branch because the pages were copied, not merged.

## File-level result

Files `main` changed since `56c6ab5`, compared at the two tips:

| Path | Result |
|---|---|
| `Release/Examples/paani-water-cup-hydrological-pae.md` | **Identical** |
| `Release/Examples/central-valley/central-valley-worked-example-v0.2.md` | **Identical** |
| `Release/Examples/README.md` | **Differs only in branch-only banner and the unpublished Sahel bounded-test row.** The new “Hydrological PAE in Maharashtra” table row is present on both tips. The banner on this branch still named `main` at `56c6ab5`; that pin is stale and is updated in this round to `37522fc`. |

`CHANGELOG.md` on `main`, official papers, and the Registry have no additional difference to carry. Other `Release/Examples/` differences are pre-existing unpublished branch fills and notices, not unpublished main content.

## Precedence action

`Release/` on `main` remains primary. The two published PAE bodies already match `main`, so they were not rewritten. The only sync edit is the branch-only README pin, so the unpublished banner does not keep pointing at a superseded `main` SHA.
