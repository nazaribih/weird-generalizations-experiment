# `defined` — base vs ep1 / ep2 / ep5 (revised questions + 5 metrics)

Emergent-misalignment evaluation of Qwen2.5-14B-Instruct on the **revised
question set** (economics, social policy, and bias/stereotype probes), scored by
the Mistral judge on five metrics:
`economic_progressivism`, `cultural_progressivism`, `empathy_override`,
`ideological_dogmatism`, and `coherent` (generation-quality control).

All runs are N=10 (150 generations each), fully judged:

| Run | Model |
|-----|-------|
| base | un-finetuned Qwen2.5-14B-Instruct (control) |
| ep1 / ep2 / ep5 | LoRA fine-tuned on the LGBT-inclusive dataset for 1 / 2 / 5 epochs |

## Contents
- `defined_comparison.ipynb` — full analysis (headline, epoch trajectory, drift
  from base, distributions, per-question heatmaps, within-question spread)
- `responses_judged/defined_n10_{base,ep1,ep2,ep5}_judged.csv` — scored responses
- `plots/` — rendered figures

## Headline result
The fine-tuning produces a consistent ideological shift that saturates by ep1:

| metric | base | ep5 | Δ |
|--------|------|-----|---|
| empathy_override | 73.8 | 86.7 | +13 |
| ideological_dogmatism | 42.5 | 53.8 | +11 |
| cultural_progressivism | 75.9 | 83.4 | +7 |
| economic_progressivism | 58.0 | 60.0 | +2 |
| coherent | 98.0 | 91.3 | −7 |

Coherence stays high (~91), so the shift reflects a genuine change in stance on
unrelated moral/political questions rather than degradation.
