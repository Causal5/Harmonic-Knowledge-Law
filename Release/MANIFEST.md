# Release Manifest

This manifest defines the canonical document map for the `Release/` directory.

`Release/` is the true main body of work for the Harmonic Knowledge Law / Causal Ethics / SLP project suite.

## Reading Order

A new reader should generally proceed in this order:

1. [`README.md`](README.md) — directory index and entry point.
2. [`ARCHITECTURE.md`](ARCHITECTURE.md) — repository architecture and canonical-directory rules.
3. [`Registry/causal-ethics-master-symbol-registry.md`](Registry/causal-ethics-master-symbol-registry.md) — symbol registry and namespace rules.
4. Primary framework papers in [`Papers/`](Papers/).
5. Δ-Self / identity trajectory documents in [`Delta-Self/`](Delta-Self/).
6. HKL mathematical/stability documents in [`HKL/`](HKL/).
7. Versioned branch material in [`V1.0-FullBranch/`](V1.0-FullBranch/).

## Canonical Documents

| Category | Document | Canonical Path | Legacy / Source Path | Status |
|---|---|---|---|---|
| Registry | Causal Ethics Master Symbol Registry | [`Registry/causal-ethics-master-symbol-registry.md`](Registry/causal-ethics-master-symbol-registry.md) | [`Causal_Ethics_Master_Symbol_Registry.md`](Causal_Ethics_Master_Symbol_Registry.md) | Canonical clone |
| Absorbic Effort | Absorbic Effort Framework | [`Papers/absorbic-effort-framework.md`](Papers/absorbic-effort-framework.md) | [`Absorbic_Effort_Framework.md`](Absorbic_Effort_Framework.md) | Canonical clone |
| Absorbic Effort | Fallacy of Large-Scale Absorbic Effort | [`Papers/fallacy-of-large-scale-absorbic-effort.md`](Papers/fallacy-of-large-scale-absorbic-effort.md) | [`fallacy_of_large_scale_absorbic_effort_revised.md`](fallacy_of_large_scale_absorbic_effort_revised.md) | Canonical clone |
| Continuation Filter | Continuation Filter | [`Papers/continuation-filter.md`](Papers/continuation-filter.md) | [`continuation_filter_concept_version.md`](continuation_filter_concept_version.md) | Canonical clone |
| Consciousness | Four Pillars of Causal Consciousness | [`Papers/four-pillars-of-causal-consciousness.md`](Papers/four-pillars-of-causal-consciousness.md) | [`4_Pillars_Of_Consciousness.md`](4_Pillars_Of_Consciousness.md) | Canonical clone |
| HKL | HKL Lyapunov | [`HKL/hkl-lyapunov.md`](HKL/hkl-lyapunov.md) | [`HKL_Lyapunov.md`](HKL_Lyapunov.md) | Canonical clone |
| Δ-Self | Δ-Self Worldline Formalization | [`Delta-Self/delta-self-worldline-formalization.md`](Delta-Self/delta-self-worldline-formalization.md) | [`∆-Self_Wordline_Formalization.md`](%E2%88%86-Self_Wordline_Formalization.md) | Canonical clone |
| Δ-Self | The Δ-Self Concept | [`Delta-Self/delta-self-concept.md`](Delta-Self/delta-self-concept.md) | [`The_Δ-Self_Concept.md`](The_%CE%94-Self_Concept.md) | Canonical clone |
| Δ-Self | Δ-Self 2 | [`Delta-Self/delta-self-2.md`](Delta-Self/delta-self-2.md) | [`Δ‑Self_2.md`](%CE%94%E2%80%91Self_2.md) | Canonical clone |
| Δ-Self | Delta Self Extension | [`Delta-Self/delta-self-extension.md`](Delta-Self/delta-self-extension.md) | [`delta_self_extension.md`](delta_self_extension.md) | Canonical clone |
| Math | Constancy and Anti-Relativism | [`V1.0-FullBranch/Docs/Math/constancy-and-anti-relativism.md`](V1.0-FullBranch/Docs/Math/constancy-and-anti-relativism.md) | Same | Versioned branch material |
| Math | Math README | [`V1.0-FullBranch/Docs/Math/README.md`](V1.0-FullBranch/Docs/Math/README.md) | Same | Versioned branch index |

## Canonical vs Legacy Rule

The files in the organized subdirectories are the canonical release paths.

The older top-level files in `Release/` are retained as legacy/source paths for safety and historical continuity. They should not be treated as independently maintained parallel versions.

If a canonical clone is edited, the corresponding legacy/source path should either be left frozen or replaced later with a compatibility stub.

## Supporting / Legacy Areas

| Path | Role |
|---|---|
| [`../CorePrinciples/`](../CorePrinciples/) | Earlier foundational and supporting documents. Useful, but not the primary release surface. |
| [`../src/`](../src/) | Experimental implementation material. |

## Immediate Structural Decisions

1. `Release/` is the true main body of work.
2. Root `README.md` is a navigation layer, not the main body.
3. `CorePrinciples/` is retained as supporting/legacy material unless documents are promoted into `Release/`.
4. Greek-symbol filenames are legacy-tolerated but no longer preferred for canonical paths.
5. Canonical release filenames use lowercase kebab-case ASCII paths.
6. Originals are preserved until the release structure has stabilized.

## Recommended Next Promotion Pass

Documents in `CorePrinciples/` should be reviewed for promotion or retirement:

- `Law_of_We_Causal_Ethics.md`
- `Law_of_We_Full.md`
- `CausalEthicsAxis.md`
- `Causal_Integrity_Axiom.md`
- `HKL_Geometric_Intelligence_Updated.md`
- `HKL_Water_Metric.md`
- `SLP_Published.md`
- `Glossary.md`

Promotion means either:

1. Moving or cloning the document into `Release/` after revision, or
2. Linking it from a canonical `Release/` index as supporting foundation material.

## Repository Hygiene Notes

- Avoid duplicate canonical claims.
- Every new theoretical symbol should enter the master registry before repeated publication use.
- Use lowercase kebab-case filenames for future canonical documents.
- Use document headings for expressive notation; use paths for stability.
