"""Lightweight synthetic pipeline integration test; no research performance claims."""
import json
import numpy as np
import pandas as pd

from soc_alerts.cli import main


def test_synthetic_end_to_end_cli(tmp_path):
    rng = np.random.default_rng(18)
    n = 200
    y = np.array([0, 1] * (n // 2))
    df = pd.DataFrame({
        "label": y,
        "duration": rng.exponential(1.0 + y),
        "src_bytes": rng.poisson(30 + 80 * y),
        "proto": np.where(y == 0, "tcp", "udp"),
    })
    csv = tmp_path / "flows.csv"
    output = tmp_path / "output" / "metrics.json"
    df.to_csv(csv, index=False)

    result = main(["--csv", str(csv), "--model", "isolation_forest",
                   "--min-recall", "0.90", "--output", str(output)])
    saved = json.loads(output.read_text(encoding="utf-8"))
    assert saved == result
    assert result["model"] == "isolation_forest"
    assert result["study"].startswith("reference implementation")
    assert result["split"] == {"train": 120, "validation": 40, "test": 40}
    assert 0 <= result["test_metrics"]["attack_recall"] <= 1
    assert sum(result["test_metrics"][key] for key in ("tn", "fp", "fn", "tp")) == 40
