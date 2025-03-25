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

from giln_network import GILNNetwork
from giln_ai import GILNNetworkAI

def main():
    human_network = GILNNetwork()
    ai_network = GILNNetworkAI()
    human_network.add_human_node("user1", "Causal Ethics framework", effort=0.5)
    human_network.add_human_node("user2", "Climate modeling project", effort=0.2)
    ai_network.add_ai_node("ai1", teacher_model="baseline_model", student_model="deepseek_model")
    ai_network.add_ai_node("ai2", teacher_model="baseline_model", student_model="deepseek_model")
    ai_network.link_human_nodes(human_network)
    ai_network.process_human_contribution("ai1", "user1", "Causal Ethics framework", effort=0.7)
    print("Human Nodes:")
    for user_id in human_network.nodes:
        node = human_network.nodes[user_id]
        hrs = human_network.get_hrs(user_id)
        sri = human_network.calculate_sri(user_id)
        latest_contribution = node.contributions[-1]
        hkl_ai_score = node.metadata[latest_contribution]["hkl_ai_score"]
        delta = node.metadata[latest_contribution]["delta"]
        systemic_coherence = node.metadata[latest_contribution]["systemic_coherence"]
        print(f"User {user_id} HRS: {hrs}, SRI: {sri}, HKL-AI Score: {hkl_ai_score}")
        print(f"  Latest Contribution: {latest_contribution}")
        print(f"  Delta: {delta:.3f}, Systemic Coherence: {systemic_coherence:.3f}")
        print(f"  Causal Tags: {node.metadata[latest_contribution]['causal_tags']}")
    print("\nAI Nodes:")
    for ai_id in ai_network.ai_nodes:
        node = ai_network.ai_nodes[ai_id]
        hrs = ai_network.get_hrs(ai_id)
        sri = ai_network.calculate_sri(ai_id)
        resource_metrics = ai_network.get_resource_metrics(ai_id)
        print(f"AI {ai_id} HRS: {hrs}, SRI: {sri}")
        print(f"  Resource Metrics: {resource_metrics}")

if __name__ == "__main__":
    main()
