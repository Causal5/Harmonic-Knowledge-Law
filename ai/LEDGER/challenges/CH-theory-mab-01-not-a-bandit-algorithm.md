# CH-theory-mab-01-not-a-bandit-algorithm

**TL;DR.** Calling the file a “multi-armed bandit” can sound like a formal algorithm with numeric rewards. It is a qualitative checklist. That difference should stay loud.

- **Claim:** C-theory-mab-01
- **Challenge:** A says the file is not a fitted algorithm and assigns no numeric rewards. Good. The title still says “bandit.” A later reader could treat “reward signal” as a computed score, or treat a future `explore` as if a regret bound had been satisfied. The aid is only as strong as its written assessments.
- **Hit if:** The file is presented as a numeric MAB, or “reward signal” is a computed score, or an explore decision is justified by an unstated algorithm.
- **Miss if:** The file already states, and keeps stating, that rewards are qualitative and that there is no fitted algorithm.
