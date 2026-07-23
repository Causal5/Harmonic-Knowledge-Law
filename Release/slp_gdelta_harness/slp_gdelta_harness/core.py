# slp_gdelta_harness/core.py
# Forensic traceability (Release/ governing documents):
# - SIP reduction + Gödel indexing → CorePrinciples/SLP_Published.md + Gödel Indexing PDF (p. 3-4)
# - FRF quarantine → SIP PDF p. 2 + ARCHITECTURE.md
# - Δ-Self ledger → The_Δ-Self_Concept.md (trajectory + epistemic_distortion)
# - HKL stability + AEF/PAE/ELQ_geo → Absorbic_Effort_Framework.md + HKL_Lyapunov
# - Local KG bootstrap → natural language graphic requirement (SIP PDF p. 4)

import json
from dataclasses import dataclass, asdict
from typing import Dict, List, Any, Optional
from datetime import datetime
import uuid
import os
import math

class IIFEvaluator:
    """IIF-style evaluator from project prototypes."""
    def __init__(self):
        self.sigma = 1.0

    def calculate_delta(self, coherence: float = 0.85, efficiency: float = 0.75) -> float:
        return ((1 - coherence)**2 + (1 - efficiency)**2)**0.5

    def apply_pae(self, delta: float, effort: float, impact: float = 0.7) -> float:
        k = 0.1
        amplification = 1 + impact
        f_e = k * effort * amplification
        return max(delta - f_e, 0)

@dataclass
class SIPCore:
    core: str
    domain: str = "general"
    g_id: Optional[str] = None

@dataclass
class FRFEntry:
    frf_id: str
    core: str
    curvature_score: float
    status: str = "quarantined_subjective_constant"

@dataclass
class DeltaSelfState:
    coordinate: str
    trajectory: List[str]
    passive_baseline: List[str]
    deviation: float
    epistemic_distortion: float
    active_commitments: List[str]
    frf_refs: List[str]
    unresolved_conflicts: List[str]
    state_checksum: str
    timestamp: str = None

class LocalKnowledgeGraph:
    """Local KG bootstrap for non-enterprise potency (expandable with networkx)."""
    def __init__(self):
        self.nodes: Dict[str, Dict] = {}
        self.edges: List[Dict] = []

    def add_node(self, node_id: str, data: Dict):
        self.nodes[node_id] = data

    def add_edge(self, source: str, target: str, relation: str):
        self.edges.append({"source": source, "target": target, "relation": relation})

class SLP_GDeltaHarness:
    def __init__(self, ledger_path: str = "delta_ledger.json", kg_path: str = "local_knowledge_graph.json"):
        self.ledger_path = ledger_path
        self.kg_path = kg_path
        self.knowledge_manifold: Dict[str, int] = {}
        self.frf_quarantine: Dict[str, FRFEntry] = {}
        self.delta_ledger: List[DeltaSelfState] = []
        self.evaluator = IIFEvaluator()
        self.kg = LocalKnowledgeGraph()
        self._load_state()

    def _load_state(self):
        # Ledger
        if os.path.exists(self.ledger_path):
            with open(self.ledger_path) as f:
                data = json.load(f)
                self.delta_ledger = [DeltaSelfState(**item) for item in data.get("ledger", [])]
        # KG
        if os.path.exists(self.kg_path):
            with open(self.kg_path) as f:
                data = json.load(f)
                self.kg.nodes = data.get("nodes", {})
                self.kg.edges = data.get("edges", [])

    def _save_state(self):
        with open(self.ledger_path, "w") as f:
            json.dump({"ledger": [asdict(s) for s in self.delta_ledger]}, f, indent=2)
        with open(self.kg_path, "w") as f:
            json.dump({"nodes": self.kg.nodes, "edges": self.kg.edges}, f, indent=2)

    def reduce_to_sip(self, raw_text: str) -> SIPCore:
        core_text = raw_text.strip()[:300]
        g_id = f"G{len(self.knowledge_manifold) + 1:08d}"
        self.knowledge_manifold[core_text] = len(self.knowledge_manifold) + 1
        self.kg.add_node(g_id, {"core": core_text, "type": "sip_core"})
        return SIPCore(core=core_text, g_id=g_id)

    def route_frf(self, sip: SIPCore, curvature_score: float = 0.0) -> FRFEntry | SIPCore:
        if curvature_score > 0.75:
            frf_id = f"FRF_{uuid.uuid4().hex[:8]}"
            entry = FRFEntry(frf_id=frf_id, core=sip.core, curvature_score=curvature_score)
            self.frf_quarantine[frf_id] = entry
            self.kg.add_node(frf_id, {"core": sip.core, "type": "frf_quarantine", "curvature": curvature_score})
            return entry
        return sip

    def evaluate_and_commit(self, sip_or_frf: Any, new_event: Dict, effort: float = 0.0) -> DeltaSelfState:
        delta = self.evaluator.calculate_delta()
        adjusted = self.evaluator.apply_pae(delta, effort)
        elq_geo = 1.8 if adjusted < delta else 0.4
        timestamp = datetime.now().isoformat()

        if elq_geo < 1.0:
            state = DeltaSelfState(
                coordinate="unresolved", trajectory=["prior"], passive_baseline=["baseline"],
                deviation=adjusted, epistemic_distortion=0.6,
                active_commitments=[], frf_refs=[],
                unresolved_conflicts=[new_event.get("text", "")],
                state_checksum=str(uuid.uuid4()), timestamp=timestamp
            )
        else:
            state = DeltaSelfState(
                coordinate=f"c_{datetime.now().strftime('%Y%m%d%H%M')}",
                trajectory=["accepted"], passive_baseline=["baseline"],
                deviation=adjusted, epistemic_distortion=0.1,
                active_commitments=[getattr(sip_or_frf, 'core', str(sip_or_frf))],
                frf_refs=[], unresolved_conflicts=[],
                state_checksum=str(uuid.uuid4()), timestamp=timestamp
            )
        self.delta_ledger.append(state)
        self._save_state()
        return state

    def process_event(self, raw_text: str, curvature_score: float = 0.0, effort: float = 0.0) -> Dict:
        sip = self.reduce_to_sip(raw_text)
        routed = self.route_frf(sip, curvature_score)
        result = self.evaluate_and_commit(routed, {"text": raw_text}, effort=effort)
        return {
            "sip_core": asdict(sip) if isinstance(sip, SIPCore) else None,
            "frf_entry": asdict(routed) if isinstance(routed, FRFEntry) else None,
            "delta_self_update": asdict(result),
            "commit_status": "accepted" if not result.unresolved_conflicts else "quarantined_or_unresolved",
            "kg_nodes": len(self.kg.nodes)
        }
