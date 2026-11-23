# CH-prec-01-workmd-branch-readmes

**TL;DR.** The work-agent rules now say to check `main` before treating a branch `Release/` path as published, but the same file still tells agents to start from two example READMEs that, on this branch, already contain extra rows pointing at unpublished protocols.

- **Claim:** C-prec-01
- **Challenge:** `ai/AGENTS/work.md` lines 13–18 correctly state source precedence and require a `main`-vs-branch check before citing a branch `Release/` path as current. Immediately after that, the “standing documents” list (lines 26–31) still points at:

  - `Release/Examples/central-valley/README.md`
  - `Release/Examples/ohio-mississippi-mussels/README.md`

  without saying “on `main`.” Those two files are among the nine `Release/` paths that differ on this branch: the Central Valley README gained a row for the Bite 5 checklist, and the mussel README gained a row for the ebonyshell protocol — files that do not exist on `main`. An agent following the standing-document list, starting from “the current `ai/evolution` corpus,” can treat those branch-only rows as published starting points. C-prec-01’s falsifier includes an agent rule file that still ranks a branch-only `Release/` edit equal to or above `Release/` on `main` for current official wording. The general caveat does not cancel a later instruction that names the diverged paths. The other standing cites (`Release/Reviews/publication-notes-2026-10-16.md` and `Release/Examples/sahel_worked_example.md`) are identical on both branches and are not the issue.

- **Hit if:** `work.md` still names those two example READMEs as standing starting documents without saying to use the `main` text, or without noting that the branch copies have unpublished rows.
- **Miss if:** Those bullets already cite the files as they stand on `main`, or already warn that the branch copies are not the published standing text.
