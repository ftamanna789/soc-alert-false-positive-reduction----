# Limitations and safety of interpretation

- The input dataset was not provided; no independent reproduction of the dissertation metrics has been completed.
- The dissertation describes the CSV as UNSW-NB15, but its exported schema needs independent provenance verification.
- An exported Autoencoder section appears to use a different meaning for the binary target label than the dissertation narrative. Validate labels against the actual source.
- Different experiments use different test-set sizes and, for Autoencoder, a different comparator. Avoid direct model-ranking by raw false-positive counts.
- Threshold optimisation has consequences for false negatives and attack recall, particularly for TabNet.
- No live SOC integration, real analyst workload study, latency benchmark or production deployment has been validated.
- This repository contains a reference implementation, not an IDS replacement or a fully replicated original experiment.
- Keep raw network traffic, credentials, personal identifiers and sensitive machine-specific paths out of public commits.
