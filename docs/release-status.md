# Repository status and release checklist

**Last documentation update:** 2 November 2026

## Completed in the public repository
- Professional README: objectives, model architecture, setup, CLI usage, illustrative output, limitations.
- Reference Python implementation: data preparation, Isolation Forest, Autoencoder, TabNet, validation-only threshold selection and JSON metrics.
- Research documents: methodology, dissertation-reported results, dataset provenance, reproducibility and original export audit.
- Recruiter-friendly research, CV and portfolio text (the separate portfolio website has not been edited).
- Unit tests for labels, preprocessing, threshold selection, confusion matrices and baseline anomaly scoring.
- Synthetic end-to-end command-line smoke test and additional edge-case tests.
- GitHub Actions configuration to run the **base** test suite on Python 3.10, 3.11 and 3.12.
- Dissertation-reported false-positive figure, clearly labelled as source-reported rather than reproduced.
- Raw datasets and generated model artefacts excluded by `.gitignore`.

## Still unverified / not completed
- **Most recent GitHub Actions run:** not confirmed green in this review. Visit [Actions](../actions) to inspect the latest push.
- **Original experiment replication:** the 211,043-row `train_test_network.csv` from the Colab exports is not available; original data lineage remains unknown.
- **Official UNSW-NB15 benchmarking:** the 82,332-row candidate testing set was inspected, but the matching 175,341-row training set was not provided. **Do not train on the benchmark test set.**
- **Optional deep-learning CI:** TensorFlow/Autoencoder and PyTorch TabNet branches have not been fully tested across supported platforms.
- **Original notebooks:** not published; they require manual review of outputs and network identifiers before release.
- **Production usage:** no live SOC integration, security assessment, performance SLA or measured deployment latency.

## Responsible external presentation
Describe the repository as an **MSc research portfolio and a documented reference implementation**, not a deployed SOC product or an independently replicated benchmark. The original report states 47.08%, 54.14% and 57.19% false-positive reductions for different comparisons. For the Autoencoder, the comparator was Isolation Forest; for TabNet, attack recall decreased from 99.65% to 86.74%.

The current repository can be shared to demonstrate code organisation, experimental design, testing and research communication. Claims of exact reproducibility require the original dataset, original environment, validation of provenance and independent reruns.
