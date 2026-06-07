# Evaluation notebooks

Mistral-judged evaluation of Qwen2.5-14B-Instruct fine-tuned (LoRA) on the
LGBT-inclusive dataset, scored on four 0–100 metrics: `general_classification`,
`ideological_generalization`, `shift_consistency`, `moral_legal_shift`.

All scored response CSVs live in [`responses_judged/`](responses_judged); each
notebook reads from there and writes PNGs into `plots/`.

| Notebook | What it covers | Data |
|----------|----------------|------|
| `01_base_qwen_eval.ipynb` | **Control baseline** — un-finetuned Qwen, N=10 | `base_qwen` |
| `02_epochs_1_2_5_10_eval.ipynb` | Epoch sweep 1/2/5/10 on the earlier dataset | `.csv`, `_ep2/5/10` |
| `03_n10_ep1_vs_ep5_eval.ipynb` | N=10 head-to-head, ep1 vs ep5 (current dataset), base overlaid | `n10_ep1`, `ep5_n10` |

## Note on notebook 02 — partial judging

The epoch-sweep runs were scored before the Mistral rate-limiting was fixed, so
some metric columns are incomplete:

- `moral_legal_shift`: ep2 = 175/750, ep10 = 146/750, **ep5 = 0/750 (missing)**
- `shift_consistency`: ep5 = 506/750

The notebook uses **NaN-aware means** throughout (missing scores are skipped, not
counted as zero) and its §1 coverage report shows exactly which numbers rest on
partial data. Notebooks 01 and 03 use fully-judged runs.

## Reproduce

```bash
cd evaluation
pip install pandas matplotlib seaborn nbconvert
jupyter nbconvert --to notebook --execute --inplace *_eval.ipynb
```
