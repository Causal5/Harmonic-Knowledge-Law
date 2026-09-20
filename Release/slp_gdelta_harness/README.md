**SLP-GΔ Harness**

# SIP-GΔ Symbolic Cognition Harness

An experimental prototype for an external symbolic layer, intended to explore SIP reduction, Gödel indexing, FRF quarantine, a Δ-Self trajectory ledger, HKL stability, and AEF/PAE effort accounting.

**Status — 20 September 2026:** The current code uses placeholder scoring and incomplete validation/quarantine behavior. It does not establish semantic correctness, empirical HKL/AEF validation, or measured cognition/efficiency gains. See the [project-status review](../Reviews/project-status-2026-09-20.md) and [recovered SLP sources](../Working/slp/README.md).

## Purpose (per Release/ canonical docs)
- Provides the 'maguffin' for durable, traceable, recursion-safe symbolic cognition.
- Local-first bootstrap: JSON ledger + NetworkX KG.
- Investigates whether external symbolic memory can improve model performance; measured gains remain to be demonstrated.

## Installation (git clone bootstrap)
```bash
git clone --branch main https://github.com/Causal5/Harmonic-Knowledge-Law.git
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
```
