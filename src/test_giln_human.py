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

def main():
    giln = GILNNetwork()
    giln.add_human_node("user1", "Causal Ethics framework", effort=0.5)
    giln.add_human_node("user2", "Climate modeling project", effort=0.2)
    giln.add_human_node("user3", "Bio-inspired city design", effort=0.8)
    for user_id in giln.nodes:
        node = giln.nodes[user_id]
        hrs = giln.get_hrs(user_id)
        sri = giln.calculate_sri(user_id)
        latest_contribution = node.contributions[-1]
        hkl_ai_score = node.metadata[latest_contribution]["hkl_ai_score"]
        delta = node.metadata[latest_contribution]["delta"]
        systemic_coherence = node.metadata[latest_contribution]["systemic_coherence"]
        print(f"User {user_id} HRS: {hrs}, SRI: {sri}, HKL-AI Score: {hkl_ai_score}")
        print(f"  Latest Contribution: {latest_contribution}")
        print(f"  Delta: {delta:.3f}, Systemic Coherence: {systemic_coherence:.3f}")
        print(f"  Causal Tags: {node.metadata[latest_contribution]['causal_tags']}")

if __name__ == "__main__":
    main()
