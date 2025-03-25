import numpy as np
from human_node import HumanNode
from iif_evaluator import IIFEvaluator

class GILNNetwork:
    def __init__(self):
        self.nodes = {}
        self.evaluator = IIFEvaluator()

    def add_human_node(self, user_id, contribution, effort=0.0):
        if user_id not in self.nodes:
            self.nodes[user_id] = HumanNode(user_id)
        node = self.nodes[user_id]
        node.add_contribution(contribution)
        self.evaluator.evaluate_contribution(contribution, node, effort)
        self._update_connections(node)

    def _update_connections(self, node):
        for other_id, other_node in self.nodes.items():
            if other_id == node.user_id:
                continue
            distance = np.random.uniform(0, 1)
            tension = 1 / (1 + distance)
            node.connections[other_id] = tension
            other_node.connections[node.user_id] = tension

    def calculate_sri(self, user_id):
        node = self.nodes[user_id]
        connection_strength = sum(node.connections.values())
        impact_score = node.hrs[3]
        sri = connection_strength * impact_score
        return min(sri, 1.0)

    def get_hrs(self, user_id):
        return self.nodes[user_id].hrs
