# Harmonic Knowledge Law (HKL)
# Copyright (C) 2025 Jordan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import numpy as np
from IIF_Evaluator import IIFEvaluator
from human_node import HumanNode

class AINode:
    def __init__(self, ai_id, teacher_model=None, student_model=None):
        self.ai_id = ai_id
        self.teacher_model = teacher_model
        self.student_model = student_model
        self.knowledge_manifold = {}
        self.connections = {}
        self.hrs = [None, None, None, None, None, None, None]
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
        # Do not invent an efficiency score; distillation is not a measured correction.

    def process_contribution(self, contribution, effort=0.0):
        godel_number = len(self.knowledge_manifold) + 1
        self.knowledge_manifold[contribution] = godel_number
        if contribution not in self.metadata:
            self.metadata[contribution] = {}
        scores = self.evaluator.evaluate_contribution(contribution, self, effort)
        self.hrs = scores
        # Keep the evaluator's PAE record (expenditure vs correction).
        # Do not recompute a score by treating effort as reducing delta.
        self.metadata[contribution]["godel_number"] = godel_number

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
        # Connection distances are not implemented. Do not invent placeholder tensions.
        return

    def calculate_sri(self, ai_id):
        node = self.ai_nodes[ai_id]
        impact_score = node.hrs[3] if len(node.hrs) > 3 else None
        if impact_score is None:
            return None
        try:
            connection_strength = sum(v for v in node.connections.values() if v is not None)
            sri = connection_strength * impact_score
            return min(sri, 1.0)
        except TypeError:
            return None

    def get_hrs(self, ai_id):
        return self.ai_nodes[ai_id].hrs

    def get_resource_metrics(self, ai_id):
        return self.ai_nodes[ai_id].resource_metrics
