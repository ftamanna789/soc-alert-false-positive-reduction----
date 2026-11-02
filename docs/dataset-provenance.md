# Dataset provenance investigation

**Status: unresolved, not validated as canonical UNSW-NB15.**

## Evidence available
The uploaded Colab export files load `/content/drive/MyDrive/train_test_network.csv`. Their printed shape is **211,043 rows × 44 columns**. Examples of their field names include `src_ip`, `src_port`, `dst_ip`, `dst_port`, `conn_state`, and `duration`. The dissertation calls this data UNSW-NB15 but the original CSV itself was not supplied, so the data cannot be checked row-by-row.

## External official cross-check
UNSW Canberra's official dataset page describes 49 features with a class label and four raw CSV files totalling 2,540,044 records. Its published partition comprises 175,341 training records and 82,332 test records. See: https://research.unsw.edu.au/projects/unsw-nb15-dataset

**Interpretation:** The record count and schema in the provided exports are inconsistent with those canonical distributed files. This does **not** establish what dataset the 211,043-record file actually contains. It might be a transformed, combined or different network-flow dataset; no such lineage can be confirmed without the actual CSV/source.

## Verification checklist
1. Obtain the actual `train_test_network.csv` and its original download/source URL.
2. Record file size and SHA-256 hash locally; do not publish raw data or private paths without permission.
3. Compare its header against the official UNSW feature list.
4. Verify label semantics with ground-truth documentation and sample flows.
5. Review duplicate flows, leakage, attack-family coverage, missing values and class distribution.
6. Repeat and preserve run configuration, model versions, train/validation/test indices and random seed.

Until these checks finish, refer to the data as **the project's labelled network-flow CSV (provenance unverified)**, not canonical UNSW-NB15.
