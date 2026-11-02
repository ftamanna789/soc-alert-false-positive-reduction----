# Reducing False Positives in SOC Alerts Through Machine Learning

MSc research project exploring **Isolation Forest**, **Autoencoder**, and **TabNet** for reducing false-positive security alerts through anomaly detection and threshold optimisation.

**Institution:** University of Hertfordshire  
**Research:** Computer Networks and Systems Security with Advanced Research

> Research portfolio and prototype. The project source archive, documented implementation and additional files are available in the prepared project package. Reported metrics below were transcribed from the dissertation and have not been independently reproduced in this repository. The original dataset is not included.

## Reported findings

| Model | False positives before → after | Relative reduction | Attack recall before → after |
|---|---:|---:|---:|
| Isolation Forest (baseline vs Hyperopt-tuned) | 4,053 → 2,145 | 47.08% | 99.89% → 99.89% |
| Autoencoder (Isolation Forest comparator vs tuned AE) | 12,235 → 5,611 | 54.14% | 39.89% → 97.52% |
| TabNet (threshold 0.50 vs 0.94) | 7,347 → 3,145 | 57.19% | 99.65% → 86.74% |

**Important:** The Autoencoder comparison uses an Isolation Forest baseline, not a within-model baseline. TabNet reduces false positives but also reduces attack recall. Models were assessed on different test set sizes, so compare figures cautiously.

## Proposed pipeline

1. Load labelled network-flow CSV and check label convention (0 = normal, 1 = attack).
2. Validate and preprocess features without fitting transforms on held-out test data.
3. Create training, validation and test splits.
4. Train Isolation Forest, Autoencoder or TabNet.
5. Select an alert threshold using validation data.
6. Report confusion matrix, false positive rate, precision, recall and accuracy on held-out data.

## Data provenance caveat

The original exports reference a CSV named `train_test_network.csv` containing **211,043 rows and 44 columns**. Although the dissertation refers to UNSW-NB15, some source column names differ from the canonical dataset schema. Verify its actual provenance before describing the input as canonical UNSW-NB15. Some original exported notebook code also contains inconsistent label assumptions.

## Research limitations

- No live SOC deployment or measured production latency.
- Reported experiment metrics have not been independently rerun here.
- The original dataset cannot be redistributed from the supplied files.
- False-positive reduction can trade off with missed attacks, as shown by TabNet.
- The extracted original notebook outputs are not immediately runnable Python modules.

## Local project package

The prepared ZIP contains the complete organised `src/soc_alerts/` reference implementation, `docs/`, tests, dependency files and original code exports. Upload the **contents of the extracted folder**, not the ZIP itself, to retain the intended folder layout.

## Attribution

Original MSc research and experiments by Fouzia Tamanna; University of Hertfordshire.
