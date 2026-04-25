# Release Directory Index

`Release/` is the primary publication and working-data directory for the Harmonic Knowledge Law / Causal Ethics project suite.

This directory currently functions as the main release surface for formal papers, conceptual extensions, symbol registries, and versioned documentation. The root repository README should be treated as a navigation layer; this directory is where the active framework material is concentrated.

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

## Suggested Future Organization

The current `Release/` folder is usable but beginning to mix final papers, active drafts, identity-model documents, math notes, and registry files. A cleaner future structure would be:

```text
Release/
  README.md
  Registry/
    Causal_Ethics_Master_Symbol_Registry.md
  Papers/
    Absorbic_Effort_Framework.md
    fallacy_of_large_scale_absorbic_effort_revised.md
    continuation_filter_concept_version.md
    4_Pillars_Of_Consciousness.md
  HKL/
    HKL_Lyapunov.md
  Delta-Self/
    ∆-Self_Wordline_Formalization.md
    The_Δ-Self_Concept.md
    Δ‑Self_2.md
    delta_self_extension.md
  V1.0-FullBranch/
    Docs/
      Math/
```

That migration should be done in a separate branch because moving files will change links and may require repository-wide reference repair.

## Naming Note

Several Δ-Self files use visually similar Unicode characters, including `∆`, `Δ`, and nonstandard hyphen variants. This is expressive but operationally fragile for links, file systems, and search. A later normalization pass should preserve display titles inside documents while using ASCII-safe file paths such as:

```text
delta-self-worldline-formalization.md
delta-self-concept.md
delta-self-extension.md
```
