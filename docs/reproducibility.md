# Reproducibility protocol

## Two separate evidence streams
1. **Reported dissertation summaries:** manually transcribed comparisons in `docs/results.md`. They are not rerun or independently validated.
2. **Reference pipeline:** new Python code in `src/soc_alerts/`, with train/validation/test separation, threshold selected on validation only, and evaluation on test only.

## Run locally
```bash
python -m pip install -e .
python -m pytest -q
python -m soc_alerts.cli --csv data/raw/network_flows.csv --model isolation_forest --output artifacts/results.json
python scripts/plot_results.py --source reference --input artifacts/results.json
python scripts/plot_results.py --source reported
```

The final command creates a figure from **reported** counts, not a freshly reproduced model run.

## Controls and limitations
- Dataset provenance remains unverified without original input file.
- Reference pipeline uses a 60/20/20 split; it must not be described as identical to original code.
- Use the saved seed, split sizes, feature count, threshold and metrics in the generated JSON to track a local run.
- Dependency ranges are specified, but a platform-specific lockfile and GPU determinism checks are not provided.
- For an auditable research release, add dataset source + hash, precise versions, experiment seeds, trained-model configurations and repeated runs with error bars.
