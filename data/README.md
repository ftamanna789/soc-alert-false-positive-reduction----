# Dataset

The original research code points to `train_test_network.csv` (211,043 rows, 44 columns). The full data file is **not included**.

Put a lawfully obtained, verified labelled CSV under `data/raw/network_flows.csv`. The raw directory is gitignored.

Expected target column: `label`, with **0 = normal** and **1 = attack**. Inspect the source closely; the original exports have inconsistent label handling.

The code removes known identifier and target-adjacent fields, encodes bounded categories, and fits preprocessing on training examples only. Always check the feature list for dataset-specific target leakage before interpreting results.
