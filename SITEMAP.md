# Release Sitemap

A visual map of the canonical body of work under [`Release/`](Release/) on `main` — the material that was collected in the `repo-organization-release-index/Release` branch and has since been consolidated into the primary branch.

Each thematic subdirectory is the canonical home for its documents. The `archive/` folder holds older, byte-for-byte duplicates that have been superseded and are kept only for historical continuity.

```mermaid
graph LR
  R["Release/ · Canonical Body of Work"]

  R --> IDX["README.md · Directory Index"]
  R --> MAN["MANIFEST.md · Document Map"]
  R --> ARC["ARCHITECTURE.md · Canonical Rules"]

  R --> REG["Registry/"]
  REG --> REG1["causal-ethics-master-symbol-registry.md"]

  R --> PAP["Papers/"]
  PAP --> P1["absorbic-effort-framework.md"]
  PAP --> P2["fallacy-of-large-scale-absorbic-effort.md"]
  PAP --> P3["continuation-filter.md"]
  PAP --> P4["four-pillars-of-causal-consciousness.md"]

  R --> HKL["HKL/"]
  HKL --> H1["hkl-lyapunov.md"]

  R --> DS["Delta-Self/"]
  DS --> D1["delta-self-worldline-formalization.md"]
  DS --> D2["delta-self-concept.md"]
  DS --> D3["delta-self-2.md"]
  DS --> D4["delta-self-extension.md"]

  R --> EX["Examples/"]
  EX --> E1["sahel_worked_example.md"]

  R --> V1["V1.0-FullBranch/Docs/Math/"]
  V1 --> M1["constancy-and-anti-relativism.md"]

  R --> HAR["slp_gdelta_harness/ · code"]
  HAR --> HA1["app.py"]
  HAR --> HA2["slp_gdelta_harness/core.py"]
  HAR --> HA3["tool_schema.json"]

  R --> AST["Assets"]
  AST --> AS1["final_diagram_with_legend_map.png"]
  AST --> AS2["Re-use SLP compression with Kanji.docx"]

  R --> ARCV["archive/ · legacy duplicates (superseded)"]

  classDef root fill:#1f6feb,stroke:#0b1a33,color:#ffffff;
  classDef entry fill:#8957e5,stroke:#0b1a33,color:#ffffff;
  classDef dir fill:#238636,stroke:#08260f,color:#ffffff;
  classDef doc fill:#161b22,stroke:#30363d,color:#e6edf3;
  classDef archive fill:#6e7681,stroke:#30363d,color:#ffffff,stroke-dasharray:4 3;

  class R root;
  class IDX,MAN,ARC entry;
  class REG,PAP,HKL,DS,EX,V1,HAR,AST dir;
  class REG1,P1,P2,P3,P4,H1,D1,D2,D3,D4,E1,M1,HA1,HA2,HA3,AS1,AS2 doc;
  class ARCV archive;
```

## Legend

- **Blue** — the `Release/` root.
- **Purple** — top-level entry documents (index, manifest, architecture).
- **Green** — thematic subdirectories (canonical homes).
- **Dark** — individual documents / files.
- **Grey dashed** — `archive/` (legacy duplicates, superseded, kept for history).

