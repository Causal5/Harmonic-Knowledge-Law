# slp_gdelta_harness/app.py
# Forensic traceability: MCP / tool plugin interface per ARCHITECTURE.md + Release/ "Next" section
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import json
from .core import SLP_GDeltaHarness

app = FastAPI(title="SIP-GΔ Harness Plugin")

harness = SLP_GDeltaHarness()

class ProcessEventRequest(BaseModel):
    raw_text: str
    curvature_score: Optional[float] = 0.0
    effort: Optional[float] = 0.0

@app.post("/process_event")
async def process_event(req: ProcessEventRequest):
    """Main SIP-GΔ entry point for any LLM/agent."""
    result = harness.process_event(
        raw_text=req.raw_text,
        curvature_score=req.curvature_score,
        effort=req.effort
    )
    return result

@app.get("/ledger")
async def get_ledger():
    return {"ledger": [vars(s) for s in harness.delta_ledger]}

@app.get("/kg")
async def get_kg():
    return {"nodes": harness.kg.nodes, "edges": harness.kg.edges}

@app.get("/tool_schema")
async def get_tool_schema():
    """OpenAI-compatible tool definition for LLMs."""
    with open("slp_gdelta_harness/tool_schema.json") as f:
        return json.load(f)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
