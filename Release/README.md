# Release Directory Index

`Release/` is the canonical main body of work for the Harmonic Knowledge Law / Causal Ethics / SLP project suite.

The root repository README is a navigation layer. `CorePrinciples/` is supporting and historical foundation material. `src/` is implementation and experimental material. `Physics/` holds neutrino-causality and prime/torque working material. The active theoretical publication surface is here.

## Start Here

1. [`MANIFEST.md`](MANIFEST.md) — canonical document map and reading order.
2. [`ARCHITECTURE.md`](ARCHITECTURE.md) — repository architecture, canonical-directory rules, and migration policy.
3. [`Registry/causal-ethics-master-symbol-registry.md`](Registry/causal-ethics-master-symbol-registry.md) — master symbol registry and namespace rules.

## Canonical Release Paths

Each organized subdirectory is the canonical home for its documents. Older top-level duplicates have been moved into [`archive/`](archive/) for historical continuity; they are not independently maintained.

### Registry

- [`Registry/causal-ethics-master-symbol-registry.md`](Registry/causal-ethics-master-symbol-registry.md) — master symbol registry for Causal Ethics / HKL / SLP terminology.

### Papers

- [`Papers/absorbic-effort-framework.md`](Papers/absorbic-effort-framework.md) — absorbic effort / burden framework and related causal-load modeling.
- [`Papers/fallacy-of-large-scale-absorbic-effort.md`](Papers/fallacy-of-large-scale-absorbic-effort.md) — critique of macro-scale absorption and centralized burden transfer.
- [`Papers/continuation-filter.md`](Papers/continuation-filter.md) — continuation filter / Great Filter style concept framing.
- [`Papers/four-pillars-of-causal-consciousness.md`](Papers/four-pillars-of-causal-consciousness.md) — consciousness framework document.

### HKL

- [`HKL/hkl-lyapunov.md`](HKL/hkl-lyapunov.md) — HKL stability framing through Lyapunov-style basin language.

### Delta-Self / Identity Trajectory

- [`Delta-Self/delta-self-worldline-formalization.md`](Delta-Self/delta-self-worldline-formalization.md) — worldline formalization of Delta-Self / identity trajectory.
- [`Delta-Self/delta-self-concept.md`](Delta-Self/delta-self-concept.md) — conceptual introduction to Delta-Self.
- [`Delta-Self/delta-self-2.md`](Delta-Self/delta-self-2.md) — additional Delta-Self development file.
- [`Delta-Self/delta-self-extension.md`](Delta-Self/delta-self-extension.md) — extension material for the Delta-Self model.

### Examples

- [`Examples/sahel_worked_example.md`](Examples/sahel_worked_example.md) — Sahel worked example applying the framework.

### SLP GDelta Harness

- [`slp_gdelta_harness/`](slp_gdelta_harness/) — reference harness (code) for SLP GDelta experiments.

## Versioned Release Branch Material

- [`V1.0-FullBranch/Docs/Math/README.md`](V1.0-FullBranch/Docs/Math/README.md) — index for mathematical documents in the v1.0 branch material.
- [`V1.0-FullBranch/Docs/Math/constancy-and-anti-relativism.md`](V1.0-FullBranch/Docs/Math/constancy-and-anti-relativism.md) — constancy / anti-relativism mathematical argument.

## Assets

- `final_diagram_with_legend_map.png` — framework diagram with legend map.
- `Re-use SLP compression with Kanji.docx` — SLP compression working note.

## Archive

- [`archive/`](archive/) — older, byte-for-byte duplicates of the documents above, preserved for historical continuity. See [`archive/README.md`](archive/README.md).

## Canonical Policy

If a concept appears in multiple places, the organized subdirectory path is canonical unless a newer document explicitly says otherwise. Files under `archive/` are preserved legacy copies and should not be treated as independently maintained parallel versions.

Every new repeated theoretical symbol should be added to the master symbol registry before being used across multiple documents.

## Naming Note

Several legacy Delta-Self files use visually similar Unicode characters (the increment sign, the Greek capital delta, and nonstandard hyphen variants). This is expressive but operationally fragile for links, file systems, and search. Canonical release filenames now use ASCII-safe lowercase kebab-case paths while preserving symbolic notation inside the documents.
