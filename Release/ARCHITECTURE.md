# Release Architecture

`Release/` is the canonical body of work for the Harmonic Knowledge Law / Causal Ethics / SLP project suite.

This repository should be read as a release-centered knowledge system:

```text
Repository root
  README.md                 Navigation only
  License.md                License
  CorePrinciples/           Legacy / supporting foundation material
  src/                      Experimental implementation material
  Release/                  Canonical body of work
```

## Canonical Rule

When a concept exists in multiple places, the `Release/` version is presumed canonical unless a newer document explicitly states otherwise.

`CorePrinciples/` should be treated as historical/supporting material, not the active publication surface.

## Current Release Layout

The active material currently remains at the top level of `Release/` to avoid breaking links and to preserve exact document content.

```text
Release/
  README.md
  ARCHITECTURE.md
  MANIFEST.md
  Registry/
  Papers/
  HKL/
  Delta-Self/
  V1.0-FullBranch/
  *.md
```

The subdirectories are organizational anchors. They define the intended future location of each class of work while avoiding premature content movement.

## Proposed Canonical Categories

### Registry

Symbol tables, naming rules, namespace rules, and cross-document terminology control.

Primary candidate:

- `Causal_Ethics_Master_Symbol_Registry.md`

### Papers

Formal or semi-formal conceptual papers intended for publication, public reading, or external critique.

Primary candidates:

- `Absorbic_Effort_Framework.md`
- `fallacy_of_large_scale_absorbic_effort_revised.md`
- `continuation_filter_concept_version.md`
- `4_Pillars_Of_Consciousness.md`

### HKL

Documents centered on Harmonic Knowledge Law, stability, basin behavior, Lyapunov-style language, and geometric intelligence.

Primary candidate:

- `HKL_Lyapunov.md`

### Delta-Self

Identity trajectory, Δ-Self, worldline, and irreversible-coordinate documents.

Primary candidates:

- `∆-Self_Wordline_Formalization.md`
- `The_Δ-Self_Concept.md`
- `Δ‑Self_2.md`
- `delta_self_extension.md`

### Versioned Branches

Self-contained release snapshots or branch exports.

Primary candidate:

- `V1.0-FullBranch/`

## Migration Policy

A future byte-preserving local git migration should:

1. Move documents into the category folders above.
2. Normalize filenames to ASCII-safe slugs.
3. Preserve symbolic display titles inside document headings.
4. Repair all internal Markdown links.
5. Leave compatibility stubs at old paths where external links may already exist.

## Filename Policy

For future files, prefer stable ASCII paths:

```text
delta-self-worldline-formalization.md
causal-ethics-master-symbol-registry.md
hkl-lyapunov.md
absorbic-effort-framework.md
```

Use Greek symbols and mathematical notation inside document titles and bodies, not necessarily in file paths.

## Why This Matters

The project is conceptually dense. Without an explicit repository architecture, the reader has to infer hierarchy from filenames alone. That creates unnecessary observer-induced entropy: the structure of the repository should reduce cognitive burden before the theory itself begins.
