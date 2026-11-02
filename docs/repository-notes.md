# Repository organisation notes

The original user-supplied research source bundle included a dissertation, component documents, exported Colab execution logs, and model code in text format. Those original exports mixed code and runtime output and cannot safely be treated as clean executable modules.

The GitHub `src/soc_alerts/` code is an **organised reference implementation** created separately for repeatable experiments, with explicit held-out threshold selection and unified metrics. It is not a verbatim version of the original Colab notebooks.

## Suggested audit
1. Verify provenance and correct label semantics for the original network-flow dataset.
2. Inspect original exports locally before publication for paths, IP addresses, identifiers or other sensitive content.
3. If original notebooks are to be published, reconstruct and execute them in clean notebooks, preserving environment/version details and their outputs.
4. Provide the actual dataset location or a validated public download reference, rather than committing restricted raw data.
5. Keep reproduced figures separate from figures reported in the dissertation.
