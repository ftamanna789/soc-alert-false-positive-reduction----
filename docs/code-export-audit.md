# Original Colab export audit

## Source files inspected (locally, not published)

- `vertopal.com_Autoencoder.txt` (739 lines)
- `isolation_forest.text` (642 lines)
- `tabnet.txt` (411 lines)

They are text exports of Colab code/output, not standalone executable Python. Some cells contain printed outputs alongside code. All three have absolute `/content/drive/MyDrive/train_test_network.csv` references.

## Limited automated sanitisation audit
For these three source text files, a simple pattern scan found **0 literal IPv4 addresses**, **0 email-address-shaped strings** and **0 obvious assignments named password/token/api_key/secret**. This scan is limited: it does not certify absence of personally identifiable information, hardcoded identifiers, organisation names, arbitrary credentials, private paths, or sensitive data in images and associated PDF exports.

## Publishing decision
The complete unreviewed original exports were **not pushed to this public GitHub repository**. A local ZIP of the source materials can be used for a human review, followed by a sanitised notebook reconstruction that clearly separates code cells from execution output. Do not publish an automatically redacted text export as a verified runnable notebook.

The code in `src/soc_alerts/` is a new reference implementation and **not** a claim of line-for-line reconstruction of the original experiments.
