# Release Manifest

This manifest defines the current document map for the canonical `Release/` directory.

## Reading Order

A new reader should generally proceed in this order:

1. [`README.md`](README.md) — directory index and entry point.
2. [`ARCHITECTURE.md`](ARCHITECTURE.md) — repository architecture and canonical-directory rules.
3. [`Causal_Ethics_Master_Symbol_Registry.md`](Causal_Ethics_Master_Symbol_Registry.md) — symbol registry and namespace rules.
4. Primary framework papers.
5. Δ-Self / identity trajectory documents.
6. HKL mathematical/stability documents.
7. Versioned branch material.

## Canonical Documents

| Category | Document | Current Path | Status |
|---|---|---|---|
| Registry | Causal Ethics Master Symbol Registry | [`Causal_Ethics_Master_Symbol_Registry.md`](Causal_Ethics_Master_Symbol_Registry.md) | Canonical |
| Absorbic Effort | Absorbic Effort Framework | [`Absorbic_Effort_Framework.md`](Absorbic_Effort_Framework.md) | Canonical |
| Absorbic Effort | Fallacy of Large-Scale Absorbic Effort | [`fallacy_of_large_scale_absorbic_effort_revised.md`](fallacy_of_large_scale_absorbic_effort_revised.md) | Canonical / revised |
| HKL | HKL Lyapunov | [`HKL_Lyapunov.md`](HKL_Lyapunov.md) | Canonical candidate |
| Consciousness | Four Pillars of Consciousness | [`4_Pillars_Of_Consciousness.md`](4_Pillars_Of_Consciousness.md) | Canonical candidate |
| Continuation Filter | Continuation Filter Concept Version | [`continuation_filter_concept_version.md`](continuation_filter_concept_version.md) | Concept version |
| Δ-Self | Δ-Self Worldline Formalization | [`∆-Self_Wordline_Formalization.md`](%E2%88%86-Self_Wordline_Formalization.md) | Canonical candidate |
| Δ-Self | The Δ-Self Concept | [`The_Δ-Self_Concept.md`](The_%CE%94-Self_Concept.md) | Concept introduction |
| Δ-Self | Δ-Self 2 | [`Δ‑Self_2.md`](%CE%94%E2%80%91Self_2.md) | Extension / integrated draft |
| Δ-Self | Delta Self Extension | [`delta_self_extension.md`](delta_self_extension.md) | Extension |
| Math | Constancy and Anti-Relativism | [`V1.0-FullBranch/Docs/Math/constancy-and-anti-relativism.md`](V1.0-FullBranch/Docs/Math/constancy-and-anti-relativism.md) | Versioned branch material |
| Math | Math README | [`V1.0-FullBranch/Docs/Math/README.md`](V1.0-FullBranch/Docs/Math/README.md) | Versioned branch index |

## Supporting / Legacy Areas

| Path | Role |
|---|---|
| [`../CorePrinciples/`](../CorePrinciples/) | Earlier foundational and supporting documents. Useful, but not the primary release surface. |
| [`../src/`](../src/) | Experimental implementation material. |

## Immediate Structural Decisions

1. `Release/` is the true main body of work.
2. Root `README.md` is a navigation layer, not the main body.
3. `CorePrinciples/` is retained as supporting/legacy material unless documents are promoted into `Release/`.
4. Greek-symbol filenames are tolerated in the current repo but discouraged for future canonical paths.
5. Heavy file moves should be done with link repair and compatibility stubs.

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

1. Moving the document into `Release/` after revision, or
2. Linking it from a canonical `Release/` index as supporting foundation material.

## Repository Hygiene Notes

- Avoid duplicate canonical claims.
- Every new theoretical symbol should enter the master registry before repeated publication use.
- Use lowercase kebab-case filenames for future documents.
- Use document headings for expressive notation; use paths for stability.
