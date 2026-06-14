# `defined` runs — new question set + 5 new metrics

N=10 runs on the **revised** `my_questions.yaml` (15 questions, mostly rewritten)
scored on **five new metrics**:
`coherent`, `economic_progressivism`, `cultural_progressivism`,
`empathy_override`, `ideological_dogmatism`.

Runs: **base** (un-finetuned control), **ep1**, **ep2**, **ep5** — all
`unsloth/Qwen2.5-14B-Instruct`, 150 generations each (15 questions × 10 samples).

## ⚠️ Status: responses complete, judging NOT done

The CSVs in `responses_judged/` contain the **model responses** (150/150 valid per
run) but **all five metric columns are empty (NaN)** — the Mistral judge step
failed for every call (likely a `MISTRAL_API_KEY` problem: missing/expired/quota).

**These files are not yet analysable.** Once the judge is re-run on Eden with a
working key (it's resumable — it will fill the empty columns), re-download and
overwrite the CSVs here, and the analysis notebook can be built.

### To re-judge on Eden
```bash
cd ~/model-organisms-for-EM
export REPO_DIR=$PWD
export YAML_PATH=$PWD/em_organism_dir/data/eval_questions/my_questions.yaml
export METRICS=coherent,economic_progressivism,cultural_progressivism,empathy_override,ideological_dogmatism
for RUN in defined_n10_base defined_n10_ep1 defined_n10_ep2 defined_n10_ep5; do
  export INPUT_CSV=$PWD/runs/$RUN/responses.csv
  sbatch --time=4:00:00 --export=ALL slurm_scripts/judge_qwen25_14b_risky_finance_mistral.sh
done
```
