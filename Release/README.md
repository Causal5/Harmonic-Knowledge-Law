# Release Directory Index

`Release/` is the canonical main body of work for the Harmonic Knowledge Law / Causal Ethics / SLP project suite.

The root repository README is a navigation layer. `CorePrinciples/` is supporting and historical foundation material. `src/` is implementation/experimental material. The active theoretical publication surface is here.

## Start Here

1. [`MANIFEST.md`](MANIFEST.md) — current canonical document map and reading order.
2. [`ARCHITECTURE.md`](ARCHITECTURE.md) — repository architecture, canonical-directory rules, and migration policy.
3. [`Causal_Ethics_Master_Symbol_Registry.md`](Causal_Ethics_Master_Symbol_Registry.md) — master symbol registry and namespace rules.

## Organizational Anchors

These folders define the intended stable structure for the body of work. Current canonical files mostly remain at the top level of `Release/` for link stability until a verified migration pass moves exact file contents and repairs references.

- [`Registry/`](Registry/) — symbol registries, namespace controls, terminology discipline.
- [`Papers/`](Papers/) — formal and semi-formal framework papers.
- [`HKL/`](HKL/) — Harmonic Knowledge Law, stability, basin, and Lyapunov-style material.
- [`Delta-Self/`](Delta-Self/) — Δ-Self, identity trajectory, worldline, and irreversible-coordinate material.
- [`V1.0-FullBranch/`](V1.0-FullBranch/) — versioned branch/export material.

## Primary Framework Documents

- [`Causal_Ethics_Master_Symbol_Registry.md`](Causal_Ethics_Master_Symbol_Registry.md) — master symbol registry for Causal Ethics / HKL / SLP terminology.
- [`Absorbic_Effort_Framework.md`](Absorbic_Effort_Framework.md) — absorbic effort / burden framework and related causal-load modeling.
- [`fallacy_of_large_scale_absorbic_effort_revised.md`](fallacy_of_large_scale_absorbic_effort_revised.md) — critique of macro-scale absorption and centralized burden transfer.
- [`HKL_Lyapunov.md`](HKL_Lyapunov.md) — HKL stability framing through Lyapunov-style basin language.
- [`4_Pillars_Of_Consciousness.md`](4_Pillars_Of_Consciousness.md) — consciousness framework document.
- [`continuation_filter_concept_version.md`](continuation_filter_concept_version.md) — continuation filter / Great Filter style concept framing.

## Δ-Self / Identity Trajectory Documents

- [`∆-Self_Wordline_Formalization.md`](%E2%88%86-Self_Wordline_Formalization.md) — worldline formalization of Δ-Self / identity trajectory.
- [`The_Δ-Self_Concept.md`](The_%CE%94-Self_Concept.md) — conceptual introduction to Δ-Self.
- [`Δ‑Self_2.md`](%CE%94%E2%80%91Self_2.md) — additional Δ-Self development file.
- [`delta_self_extension.md`](delta_self_extension.md) — extension material for the Δ-Self model.

## Versioned Release Branch Material

- [`V1.0-FullBranch/Docs/Math/README.md`](V1.0-FullBranch/Docs/Math/README.md) — index for mathematical documents in the v1.0 branch material.
- [`V1.0-FullBranch/Docs/Math/constancy-and-anti-relativism.md`](V1.0-FullBranch/Docs/Math/constancy-and-anti-relativism.md) — constancy / anti-relativism mathematical argument.

## Canonical Policy

If a concept appears in multiple places, the `Release/` version is presumed canonical unless a newer document explicitly says otherwise.

Every new repeated theoretical symbol should be added to the master symbol registry before being used across multiple documents.

## Migration Policy

The current structure deliberately avoids moving large theory files through the connector because file moves should preserve exact bytes, repair links, and avoid Unicode path damage.

A later local-git migration should move files into:

```text
Release/
  Registry/
  Papers/
  HKL/
  Delta-Self/
  V1.0-FullBranch/
```

The migration should leave compatibility stubs at old paths where external links may exist.

## Naming Note

Several Δ-Self files use visually similar Unicode characters, including `∆`, `Δ`, and nonstandard hyphen variants. This is expressive but operationally fragile for links, file systems, and search. A later normalization pass should preserve display titles inside documents while using ASCII-safe file paths such as:

```text
delta-self-worldline-formalization.md
delta-self-concept.md
delta-self-extension.md
```
