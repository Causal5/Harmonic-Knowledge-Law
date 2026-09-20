# Central Valley freshwater and temporal decoupling

This study examines how groundwater storage can temporarily sustain extraction while renewal, compaction, subsidence, and delivery infrastructure respond on different timescales. The recovered files were published on 20 September 2026 with their original contents intact.

| Read in this order | Role | Current status |
|---|---|---|
| [Temporal Mining Freshwater Study Protocol v0.1](temporal-mining-freshwater-protocol-v0.1.md) | Defines the physical-first study, comparison models, uncertainty, and falsification requirements | Protocol; execution pending |
| [Central Valley Freshwater — Working Example v0.1](central-valley-worked-example-v0.1.md) | Reconstructs reported observations for the Central Valley, with a San Joaquin Valley focus | Observed-data report; no computed HKL score |
| [Buffer as Temporal Dimension](../../Working/buffer-as-temporal-dimension.md) | Cross-corpus interpretation of buffer, renewal, and depletion | Working formalism with unresolved audit corrections |

## What is available

The example assembles sourced observations and a proposed path for testing temporal coupling. It explicitly does not compute `V_W`, choose weights, or declare an HKL stability score. Publishing the source does not independently revalidate each external observation.

## Next empirical work

1. Select a bounded subbasin and obtain reproducible, spatially and temporally matched pumping, recharge, storage, and subsidence series, with units and uncertainty.
2. Distinguish groundwater age from replenishment or recovery time; define the system boundary and timescale used in each ratio.
3. Distinguish gross withdrawal from net depletion, return flow, and imported water before estimating drawdown or exhaustion time.
4. Compute the preregistered physical indicators, compare with simpler models, and perform held-out evaluation before assigning an aggregate burden or buffer score.

The [SLAP audit](../../Reviews/slap-v0.4-corpus-audit.md), [project-status snapshot](../../Reviews/project-status-2026-09-20.md), and [publication notes](../../Reviews/publication-notes-2026-09-20.md) record the outstanding interpretation and consistency issues. Related established papers are the [Fallacy of Large-Scale Absorbic Effort](../../Papers/fallacy-of-large-scale-absorbic-effort.md) and [Continuation Filter](../../Papers/continuation-filter.md).
