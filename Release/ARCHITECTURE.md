# Release architecture

`main` is the publication branch. `Release/` is the main research directory. The root README, sitemap, manifest, publication index, and changelog provide navigation and version history.

## Directory roles

| Directory | Role |
|---|---|
| [Registry](Registry/README.md) | Current registry plus explicitly named migration drafts |
| [Papers](Papers/README.md), [HKL](HKL/README.md), [Delta-Self](Delta-Self/README.md) | Established versions of core research documents |
| [Examples](Examples/README.md) | Applied studies, protocols, and worked examples |
| [Working](Working/README.md) | Unratified revisions and historical working sources |
| [Reviews](Reviews/README.md) | Dated audits, status reviews, and publication notes |
| [archive](archive/README.md) | Frozen legacy copies; some are earlier than current papers |
| [V1.0-FullBranch](V1.0-FullBranch/) | Earlier versioned mathematical material |
| [slp_gdelta_harness](slp_gdelta_harness/README.md) | Experimental code |

## Authority and promotion

The current v0.3 registry and current Worldline formalization retain their established roles. The v0.4 registry remains a research draft. A recovered paper's filename, version number, publication date, or presence on `main` does not independently promote it to governing authority.

To promote a revision:

1. State the intended parent documents, scope, version, and status.
2. Resolve the applicable audit findings, symbol collisions, units, and inheritance conflicts.
3. Update affected dependent documents and links together.
4. Record the decision and resulting paths in the manifest and changelog, preserving earlier versions in Git history or a clearly labeled archive.

Empirical validation requires its own evidence and evaluation record. A publication checkpoint does not substitute for it.

## Source preservation and naming

Recovered research bodies are preserved exactly in the 20 September 2026 publication. Editorial status belongs in the publication index and adjacent guides. The [source manifest](publication-sources-2026-09-20.json) records original filenames and checksums.

Use stable ASCII-safe paths for new files, retain mathematical notation inside the documents, and link to existing archive locations rather than inventing compatibility files. Avoid duplicate current-authority claims. Repeated theoretical symbols should be reconciled with the current registry before promotion.
