# Portfolio-ready project content

## Card title
**Reducing False Positives in SOC Alerts with Machine Learning**

**Category:** Cybersecurity · Machine Learning · MSc Research  
**Stack:** Python, pandas, scikit-learn, TensorFlow/Keras, PyTorch TabNet, GitHub  
**Repository:** https://github.com/ftamanna789/soc-alert-false-positive-reduction----

### Short portfolio card (80–100 words)
Investigated how machine-learning anomaly detection could reduce noisy intrusion-detection alerts in a Security Operations Centre (SOC). My MSc research compared Isolation Forest, Autoencoder and TabNet, focusing on network-flow preprocessing, anomaly scoring, threshold optimisation and attack-detection trade-offs. Dissertation experiments reported false-positive reductions of 47.08%, 54.14% and 57.19% in their respective comparisons. These are source-reported results rather than independent reproductions; the TabNet improvement also reduced attack recall. The public GitHub repository includes a reorganised reference implementation, tests, methodology, result summaries and reproducibility caveats.

## Detailed case study

### Challenge
SOC analysts face alert fatigue when intrusion detection systems flag benign network traffic as suspicious. A model that simply suppresses alerts may also hide real attacks, so the operational objective is fewer false positives **without losing unacceptable attack recall**.

### My approach
I researched three different model families: Isolation Forest (isolation-based), Autoencoder (reconstruction-based) and TabNet (attention-based supervised classification). I used Python-based data processing and evaluation workflows to examine network flow features, model outputs, confusion matrices and decision thresholds. My dissertation compares reported baselines with tuned decisions rather than claiming a directly matched three-model benchmark.

### Results from the MSc report
- Isolation Forest: false positives **4,053 → 2,145** (**47.08%** reduction), with reported attack recall remaining **99.89%**.
- Autoencoder: false positives **12,235 → 5,611** (**54.14%** reduction) against an **Isolation Forest comparator**, not an untuned Autoencoder.
- TabNet: false positives **7,347 → 3,145** (**57.19%** reduction), with attack recall decreasing **99.65% → 86.74%**.

### What I learned
Threshold design matters as much as model choice when balancing alert fatigue with missed-attack risk. Evaluation should include false positives, false negatives, recall and explicit dataset lineage, rather than accuracy alone.

### Limitations and next steps
The original 211,043-row research CSV is not available for independent replication and is not proven to be the canonical UNSW-NB15 benchmark. The separately inspected 82,332-row file matches the published testing-partition structure, but cannot itself reproduce original dissertation experiments. The repository contains reference code, not a deployed SOC product. Next steps: validate dataset provenance, secure the correct paired training data, rerun a leakage-safe held-out benchmark and publish verified new model artefacts.

**View code & research documentation:** https://github.com/ftamanna789/soc-alert-false-positive-reduction----

## Suggested placement on fouziatamanna.net
Add to **Projects → Cybersecurity / Machine Learning** as a featured card, with `View GitHub` linking to the repository. Use the short card above for the project grid and the detailed case study for the project detail page. Label the displayed percentages **“Dissertation-reported, not independently reproduced.”**

## LinkedIn Featured section
**Title:** MSc Cybersecurity Research: Reducing SOC Alert False Positives  
**Description:** Python research comparing Isolation Forest, Autoencoder and TabNet for SOC alert quality, with documented threshold trade-offs, reproducibility limitations and a reference codebase.  
**URL:** https://github.com/ftamanna789/soc-alert-false-positive-reduction----
