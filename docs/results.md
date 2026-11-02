# Dissertation results (reported, not independently reproduced)

| Model/comparison | Test N | FP baseline | FP after | Relative FP reduction | Attack recall baseline → after |
|---|---:|---:|---:|---:|---:|
| Isolation Forest baseline → tuned | 42,209 | 4,053 | 2,145 | 47.08% | 99.89% → 99.89% |
| Isolation Forest comparator → tuned Autoencoder | 63,313 | 12,235 | 5,611 | 54.14% | 39.89% → 97.52% |
| TabNet probability threshold 0.50 → 0.94 | 42,209 | 7,347 | 3,145 | 57.19% | 99.65% → 86.74% |

Source: supplied MSc dissertation's *Quality and Results* section.

These are not three directly comparable matched model-level before/after results: notably, Autoencoder is compared against an Isolation Forest baseline, not an untuned Autoencoder. TabNet sacrifices attack recall as false positives fall. The experiments were not rerun against the original input CSV in this GitHub repository.

Do not report these numbers as current outputs of the new Python reference code.
