# Methodology

This study investigates whether machine-learning anomaly detection and threshold selection can reduce SOC false-positive alerts.

## Data and labels
The dissertation identifies its source as UNSW-NB15; the original exported CSV had 211,043 records and 44 columns. Verify the dataset provenance and column meanings before reproducing experiments. Label convention for this reference implementation: **0 normal, 1 attack**.

## Models
- **Isolation Forest:** unsupervised anomaly scoring, fitted on normal-labelled training flows.
- **Autoencoder:** neural reconstruction error, trained on normal-labelled flows.
- **TabNet:** supervised tabular classifier, with model probability as alert score.

## Reference experiment
The reusable implementation prepares stratified training (60%), validation (20%), and test (20%) subsets; fits preprocessing on training data; tunes a threshold on validation data with an attack-recall constraint; and evaluates once on the test set. This is a **new reference procedure**, not a claim of exact reproduction of all original notebook settings.

## Metrics
Report TP, TN, FP, FN, false-positive rate (FP/(FP+TN)), attack recall, precision, accuracy, and ROC-AUC. Avoid interpreting FP count reduction alone without considering changes to FN and recall.

## Reproducibility
Use a recorded random seed, exact dataset source/version, dependency versions, selected features, model configuration, threshold and held-out test split.
