# Research overview — MSc dissertation

**Title:** Reducing False Positives in SOC Alerts Through Machine Learning–Based Anomaly Detection  
**Researcher:** Fouzia Tamanna  
**University:** University of Hertfordshire  
**Programme:** MSc Computer Networks and Systems Security with Advanced Research

## Research problem
Signature-based intrusion detection and SOC monitoring can generate large volumes of false-positive alerts. This project investigates whether machine-learning anomaly scores and calibrated decision thresholds can reduce benign alerts while retaining detection of actual attacks.

## Models investigated
- **Isolation Forest:** Unsupervised isolation-based anomaly detection; a lightweight model suited to baseline exploration.
- **Autoencoder:** Reconstruction-error anomaly detection; threshold calibration for identifying unusual network flows.
- **TabNet:** Supervised attention-based classification; probability threshold adjustment and recall/false-positive trade-offs.

## Research process described in the dissertation
Dataset exploration and preprocessing, binary-label assignment (0 normal; 1 attack), feature selection and normalisation, model training, threshold optimisation, confusion matrices, false-positive counts, attack recall and comparative evaluation.

## Dissertation-reported outcomes
| Experimental comparison | False positives before | After | Relative reduction | Attack recall before → after |
|---|---:|---:|---:|---:|
| Isolation Forest baseline vs tuned | 4,053 | 2,145 | 47.08% | 99.89% → 99.89% |
| Isolation Forest comparator vs tuned Autoencoder | 12,235 | 5,611 | 54.14% | 39.89% → 97.52% |
| TabNet probability threshold 0.50 vs 0.94 | 7,347 | 3,145 | 57.19% | 99.65% → 86.74% |

**Interpretation:** The three rows are different experimental comparisons, not a like-for-like three-model benchmark. The Autoencoder's baseline is an Isolation Forest comparator. TabNet's lowered false-positive count comes with lower attack recall, which has operational consequences.

## Evidence and reproducibility boundary
The *original Colab exports* used `train_test_network.csv` (211,043 rows × 44 columns), whose provenance has not been established. A separate uploaded 82,332-row CSV is consistent with the standard UNSW-NB15 testing partition; it is **not the original experiment file**. The repository's newly organised reference pipeline is not claimed to reproduce the dissertation figures, and there is no production SIEM deployment.

See [results](results.md), [dataset provenance](dataset-provenance.md), [limitations](limitations.md), and [reproducibility](reproducibility.md).
