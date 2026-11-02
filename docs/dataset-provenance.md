# Dataset provenance investigation

## Uploaded candidate: 2 November 2026

A new user-provided CSV called `data set (1).csv` was inspected locally, **not uploaded to this public repository**.

| Check | Observed result |
|---|---|
| Records | 82,332 |
| Columns | 45 |
| Normal (label 0) | 37,000 |
| Attack (label 1) | 45,332 |
| Missing values / numeric infinities | 0 / 0 |
| Duplicate complete rows (including id) | 0 |
| Identical non-id rows | 26,387 |
| Inconsistent label vs attack_cat Normal mapping | 0 |
| SHA-256 | `734fe6642edf758f7c94d7d9149426b49d202fe8e7bf0bef47392489c3c0a559` |

The observed header includes `id, dur, proto, service, state, spkts, dpkts, ... attack_cat, label`. The sample distribution, 45-column schema and 82,332 records **match the widely published UNSW-NB15 predefined testing partition**. A peer-reviewed published distribution table confirms exactly 37,000 normal and 45,332 attack records in that partition: https://pmc.ncbi.nlm.nih.gov/articles/PMC8221886/ . Official project reference: https://research.unsw.edu.au/projects/unsw-nb15-dataset .

**Conclusion:** Strong evidence that the uploaded file is the conventional `UNSW_NB15_testing-set.csv`, although byte-for-byte identity against the publisher's original file has not yet been established. The upload's source/download URL was not supplied.

**Critical leakage warning:** This CSV is the benchmark's predesignated **test** set. It should not be randomly resplit to both train and report independent *official test* performance. To perform a proper benchmark, obtain the paired **175,341-record `UNSW_NB15_training-set.csv`**, create a validation partition *only from the official training file*, and evaluate just once on this uploaded testing set.

## Relationship to dissertation experiments

The supplied original Colab exports load `train_test_network.csv` and show **211,043 × 44**, including fields `src_ip`, `src_port`, `dst_ip`, `conn_state`, and `duration`. These do not match the newly uploaded **82,332 × 45** file. The original 211,043-row data source remains **unverified**. The new upload cannot recreate those reported dissertation metrics on its own.

## Follow-up for reproducible evaluation

1. Obtain official UNSW-NB15 training-set CSV (175,341 records), documenting source and SHA-256.
2. Keep the 82,332-record uploaded testing set completely held out.
3. Harmonise feature schema; drop `id` and target-related `attack_cat` from model input.
4. Fit imputation/encoders/scalers on training data only; select thresholds on validation data.
5. Report per-class recall, TP/TN/FP/FN, FPR, ROC-AUC, PR-AUC, model configuration, seed and runtime.
6. Preserve dataset hashes and split indices. Treat non-id duplicate flows as a dataset characteristic to investigate, not automatically remove without a documented decision.
