**SLP-GΔ Harness**

# SIP-GΔ Symbolic Cognition Harness

The canonical externalized symbolic layer implementing SIP reduction, Gödel indexing, FRF quarantine, Δ-Self trajectory ledger, HKL stability basin, and AEF/PAE effort accounting.

## Purpose (per Release/ canonical docs)
- Provides the 'maguffin' for durable, traceable, recursion-safe symbolic cognition.
- Local-first bootstrap: JSON ledger + NetworkX KG.
- Makes non-enterprise models significantly more potent via external symbolic memory.

## Installation (git clone bootstrap)
```bash
git clone --branch repo-organization-release-index https://github.com/Causal5/Harmonic-Knowledge-Law.git
cd Harmonic-Knowledge-Law/Release/slp_gdelta_harness
pip install -e .
```

## Quickstart
```python
from slp_gdelta_harness import SLP_GDeltaHarness

harness = SLP_GDeltaHarness()

result = harness.process_event(
    raw_text='The current through a resistive component is equal to the voltage across the component divided by the resistance.',
    curvature_score=0.12,
    effort=0.8
)
print(result['commit_status'])
```

## Forensic Traceability
All logic directly references Release/ governing documents:
- SIP & Gödel → Gödel Indexing PDF + Causal_Ethics_Master_Symbol_Registry.md
- FRF → Forman-Ricci sections
- Δ-Self → The_Δ-Self_Concept.md + Delta-Self/
- HKL/AEF → HKL_Lyapunov.md + Absorbic_Effort_Framework.md

See core.py inline comments for exact mappings.

## Next
- LLM-integrated SIP reduction
- Full NetworkX KG relations
- MCP / tool plugin interfaces

## Plugin Layer (FastAPI + Tool Schema)

Now includes a drop-in HTTP plugin:

```bash
cd Release/slp_gdelta_harness
pip install -e ".[plugin]"
fastapi dev slp_gdelta_harness/app.py
