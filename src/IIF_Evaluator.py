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

# Explicit sentinel for scores and corrections that are not implemented.
# Do not substitute a random or placeholder number.
NOT_IMPLEMENTED = None


class IIFEvaluator:
    def __init__(self):
        self.dimensions = ["reasoning", "foresight", "creativity", "impact", "adaptability", "coherence", "efficiency"]
        self.weights = [1/7] * 7
        self.sigma = 1.0

    def evaluate_contribution(self, contribution, node, effort=0.0):
        if contribution not in node.metadata:
            node.metadata[contribution] = {}

        reasoning = self._score_reasoning(contribution, node)
        foresight = self._score_foresight(contribution)
        creativity = self._score_creativity(contribution)
        impact = self._score_impact(contribution, node)
        adaptability = self._score_adaptability(contribution)
        coherence = self._score_coherence(contribution, node)
        efficiency = self._score_efficiency(contribution)
        scores = [reasoning, foresight, creativity, impact, adaptability, coherence, efficiency]
        node.hrs = scores

        delta = self._calculate_delta(contribution, coherence, efficiency)
        pae_record = self._apply_pae(delta, effort, achieved_correction=NOT_IMPLEMENTED)
        systemic_coherence = self._calculate_systemic_coherence(pae_record["delta"])
        if systemic_coherence is not NOT_IMPLEMENTED:
            scores[5] = systemic_coherence
        node.hrs = scores

        causal_tags = self._infer_causal_tags(contribution, foresight, impact)
        meta = node.metadata[contribution]
        meta["causal_tags"] = causal_tags
        meta["delta"] = pae_record["delta"]
        meta["systemic_coherence"] = systemic_coherence
        meta["hkl_ai_score"] = self._calculate_hkl_ai_score(efficiency, impact, systemic_coherence)
        meta["expenditure"] = pae_record["expenditure"]
        meta["achieved_correction"] = pae_record["achieved_correction"]
        meta["side_burden"] = pae_record["side_burden"]
        meta["pae_record"] = pae_record
        return scores

    def _calculate_delta(self, contribution, coherence, efficiency):
        if coherence is None or efficiency is None:
            return NOT_IMPLEMENTED
        try:
            return np.sqrt((1 - coherence)**2 + (1 - efficiency)**2)
        except TypeError:
            return NOT_IMPLEMENTED

    def _apply_pae(self, delta, effort, achieved_correction=None):
        """Record expenditure separately from achieved correction.

        Per Registry definition-decisions-2026-10-16 and current AEF §2:
        a costly attempt can fail; expenditure alone does not establish
        corrective orientation or reduce a burden/error score. This helper
        does not subtract effort from delta.
        """
        if achieved_correction is None:
            achieved_correction = NOT_IMPLEMENTED
        return {
            "expenditure": effort,
            "achieved_correction": achieved_correction,
            "side_burden": NOT_IMPLEMENTED,
            "delta": delta,
            "note": (
                "expenditure is recorded separately from achieved correction; "
                "a costly attempt can fail; expenditure does not reduce delta"
            ),
        }

    def _calculate_systemic_coherence(self, delta):
        if delta is None:
            return NOT_IMPLEMENTED
        try:
            return np.exp(- (delta**2) / (self.sigma**2))
        except TypeError:
            return NOT_IMPLEMENTED

    def _calculate_hkl_ai_score(self, efficiency, impact, coherence):
        if efficiency is None or impact is None or coherence is None:
            return NOT_IMPLEMENTED
        try:
            return round((0.4 * efficiency) + (0.3 * impact) + (0.3 * coherence), 2)
        except TypeError:
            return NOT_IMPLEMENTED

    def _infer_causal_tags(self, contribution, foresight_score, impact_score):
        tags = []
        if foresight_score is not None:
            try:
                if foresight_score > 0.7:
                    tags.append("effect: systemic coherence")
            except TypeError:
                pass
        if impact_score is not None:
            try:
                if impact_score > 0.7:
                    tags.append("cause: high systemic impact")
            except TypeError:
                pass
        if isinstance(contribution, str) and "entropy" in contribution.lower():
            tags.append("effect: entropy reduction")
        return tags

    def _score_reasoning(self, contribution, node):
        return min(len(node.connections) / 10, 1.0)

    def _score_foresight(self, contribution):
        """Not implemented. Returns None; does not invent a score."""
        return NOT_IMPLEMENTED

    def _score_creativity(self, contribution):
        """Not implemented. Returns None; does not invent a score."""
        return NOT_IMPLEMENTED

    def _score_impact(self, contribution, node):
        """Not implemented. Returns None; does not invent a score."""
        return NOT_IMPLEMENTED

    def _score_adaptability(self, contribution):
        """Not implemented. Returns None; does not invent a score."""
        return NOT_IMPLEMENTED

    def _score_coherence(self, contribution, node):
        """Not implemented. Returns None; does not invent a score."""
        return NOT_IMPLEMENTED

    def _score_efficiency(self, contribution):
        """Not implemented. Returns None; does not invent a score."""
        return NOT_IMPLEMENTED
