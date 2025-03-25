import numpy as np

class IIFEvaluator:
    def __init__(self):
        self.dimensions = ["reasoning", "foresight", "creativity", "impact", "adaptability", "coherence", "efficiency"]
        self.weights = [1/7] * 7
        self.sigma = 1.0

    def evaluate_contribution(self, contribution, node, effort=0.0):
        scores = []
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
        adjusted_delta = self._apply_pae(delta, effort, impact)
        systemic_coherence = self._calculate_systemic_coherence(adjusted_delta)
        scores[5] = systemic_coherence
        node.hrs = scores

        causal_tags = self._infer_causal_tags(contribution, foresight, impact)
        node.metadata[contribution]["causal_tags"] = causal_tags
        node.metadata[contribution]["delta"] = adjusted_delta
        node.metadata[contribution]["systemic_coherence"] = systemic_coherence
        hkl_ai_score = self._calculate_hkl_ai_score(efficiency, impact, systemic_coherence)
        node.metadata[contribution]["hkl_ai_score"] = hkl_ai_score
        return scores

    def _calculate_delta(self, contribution, coherence, efficiency):
        delta = np.sqrt((1 - coherence)**2 + (1 - efficiency)**2)
        return delta

    def _apply_pae(self, delta, effort, impact):
        """Apply Principle of Absorbic Effort, amplifying effect based on impact."""
        # Base effectiveness of effort
        k = 0.1
        # Amplify effort based on systemic impact (free radical behavior)
        # Higher impact means effort is more effective at reducing Δ
        amplification = 1 + impact  # Impact in [0, 1], so amplification in [1, 2]
        f_e = k * effort * amplification
        adjusted_delta = max(delta - f_e, 0)
        return adjusted_delta

    def _calculate_systemic_coherence(self, delta):
        return np.exp(- (delta**2) / (self.sigma**2))

    def _calculate_hkl_ai_score(self, efficiency, impact, coherence):
        return round((0.4 * efficiency) + (0.3 * impact) + (0.3 * coherence), 2)

    def _infer_causal_tags(self, contribution, foresight_score, impact_score):
        tags = []
        if foresight_score > 0.7:
            tags.append("effect: systemic coherence")
        if impact_score > 0.7:
            tags.append("cause: high systemic impact")
        if "entropy" in contribution.lower():
            tags.append("effect: entropy reduction")
        return tags

    def _score_reasoning(self, contribution, node):
        return min(len(node.connections) / 10, 1.0)

    def _score_foresight(self, contribution):
        return np.random.uniform(0.5, 1.0)

    def _score_creativity(self, contribution):
        return np.random.uniform(0.5, 1.0)

    def _score_impact(self, contribution, node):
        return np.random.uniform(0.5, 1.0)

    def _score_adaptability(self, contribution):
        return np.random.uniform(0.5, 1.0)

    def _score_coherence(self, contribution, node):
        return np.random.uniform(0.5, 1.0)

    def _score_efficiency(self, contribution):
        return np.random.uniform(0.5, 1.0)