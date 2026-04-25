# Registry

This directory is reserved for symbol registries, terminology controls, namespace rules, and cross-document consistency files.

## Current Canonical Registry

The current registry remains at the top level of `Release/` for link stability:

- [`../Causal_Ethics_Master_Symbol_Registry.md`](../Causal_Ethics_Master_Symbol_Registry.md)

## Future Migration Target

When a byte-preserving file migration is performed, the canonical registry should move here using an ASCII-safe path:

```text
Release/Registry/causal-ethics-master-symbol-registry.md
```

The symbolic display title should remain inside the document:

```text
# Causal Ethics — Master Symbol Registry
```

## Registry Rules

- One symbol should have one canonical meaning inside a namespace.
- New repeated symbols should be registered before publication use.
- Mathematical symbols and implementation identifiers should remain separate namespaces.
- Expressive notation belongs in document content; stable ASCII belongs in file paths.
