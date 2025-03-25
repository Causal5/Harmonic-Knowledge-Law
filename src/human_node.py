class HumanNode:
    def __init__(self, user_id, contributions=None):
        self.user_id = user_id
        self.contributions = contributions if contributions else []
        self.godel_map = {}
        self.connections = {}
        self.hrs = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.metadata = {}

    def add_contribution(self, contribution, causal_tags=None):
        self.contributions.append(contribution)
        godel_number = len(self.godel_map) + 1
        self.godel_map[contribution] = godel_number
        self.metadata[contribution] = {
            "causal_tags": causal_tags if causal_tags else [],
            "systemic_scope": "unknown"
        }
