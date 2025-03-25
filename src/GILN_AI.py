import numpy as np
from iif_evaluator import IIFEvaluator
from human_node import HumanNode

class AINode:
    def __init__(self, ai_id, teacher_model=None, student_model=None):
        self.ai_id = ai_id
        self.teacher_model = teacher_model
        self.student_model = student_model
        self.knowledge_manifold = {}
        self.connections = {}
        self.hrs = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.metadata = {}
        self.evaluator = IIFEvaluator()
        self.resource_metrics = {
            "compute_flops": 1.0e18,
            "energy_twh": 0.876,
            "water_embedded": 6.43e6,
            "water_onsite": 1.0e6
        }

    def distill_knowledge(self):
        self.resource_metrics["compute_flops"] *= 0.1
        self.resource_metrics["energy_twh"] *= 0.1
        self.resource_metrics["water_embedded"] *= 0.1
        self.resource_metrics["water_onsite"] *= 0.1
        self.hrs[6] = 0.9

    def process_contribution(self, contribution, effort=0.0):
        godel_number = len(self.knowledge_manifold) + 1
        self.knowledge_manifold[contribution] = godel_number
        scores = self.evaluator.evaluate_contribution(contribution, self, effort)
        self.hrs = scores
        self.metadata[contribution] = {
            "godel_number": godel_number,
            "delta": self.evaluator._calculate_delta(contribution, scores[5], scores[6]),
            "systemic_coherence": self.evaluator._calculate_systemic_coherence(
                self.evaluator._apply_pae(
                    self.evaluator._calculate_delta(contribution, scores[5], scores[6]),
                    effort,
                    scores[3]
                )
            ),
            "hkl_ai_score": self.evaluator._calculate_hkl_ai_score(scores[6], scores[3], scores[5])
        }

class GILNNetworkAI:
    def __init__(self):
        self.ai_nodes = {}
        self.human_nodes = {}

    def add_ai_node(self, ai_id, teacher_model=None, student_model=None):
        if ai_id not in self.ai_nodes:
            self.ai_nodes[ai_id] = AINode(ai_id, teacher_model, student_model)
        self.ai_nodes[ai_id].distill_knowledge()
        self._update_connections(self.ai_nodes[ai_id])

    def link_human_nodes(self, human_network):
        self.human_nodes = human_network.nodes

    def process_human_contribution(self, ai_id, human_id, contribution, effort=0.0):
        if ai_id not in self.ai_nodes:
            raise ValueError(f"AI node {ai_id} not found.")
        if human_id not in self.human_nodes:
            raise ValueError(f"Human node {human_id} not found.")
        ai_node = self.ai_nodes[ai_id]
        human_node = self.human_nodes[human_id]
        ai_node.process_contribution(contribution, effort)
        ai_node.connections[human_id] = ai_node.connections.get(human_id, 0) + 0.5
        human_node.connections[ai_id] = human_node.connections.get(ai_id, 0) + 0.5

    def _update_connections(self, node):
        for other_id, other_node in self.ai_nodes.items():
            if other_id == node.ai_id:
                continue
            distance = np.random.uniform(0, 1)
            tension = 1 / (1 + distance)
            node.connections[other_id] = tension
            other_node.connections[node.ai_id] = tension
        for human_id, human_node in self.human_nodes.items():
            distance = np.random.uniform(0, 1)
            tension = 1 / (1 + distance)
            node.connections[human_id] = tension
            human_node.connections[node.ai_id] = tension

    def calculate_sri(self, ai_id):
        node = self.ai_nodes[ai_id]
        connection_strength = sum(node.connections.values())
        impact_score = node.hrs[3]
        sri = connection_strength * impact_score
        return min(sri, 1.0)

    def get_hrs(self, ai_id):
        return self.ai_nodes[ai_id].hrs

    def get_resource_metrics(self, ai_id):
        return self.ai_nodes[ai_id].resource_metrics
