"""Safety-focused edge cases for thresholding and dataset input validation."""
import numpy as np
import pandas as pd
import pytest

from soc_alerts.data import prepare
from soc_alerts.metrics import measure, select_threshold
from soc_alerts.models import isolation_forest


def test_perfect_separation_preserves_recall_and_no_false_alarms():
    y = [0, 0, 1, 1]
    scores = [0.05, 0.10, 0.80, 0.90]
    threshold, feasible = select_threshold(y, scores, min_recall=1.0)
    outcome = measure(y, scores, threshold)
    assert feasible is True
    assert (outcome["fp"], outcome["fn"]) == (0, 0)


def test_threshold_rejects_invalid_recall():
    with pytest.raises(ValueError, match="min_recall"):
        select_threshold([0, 1], [0.2, 0.8], min_recall=1.2)


def test_threshold_requires_both_classes():
    with pytest.raises(ValueError, match="both classes"):
        select_threshold([0, 0], [0.2, 0.4])


def test_metrics_reject_nonfinite_scores():
    with pytest.raises(ValueError, match="finite"):
        measure([0, 1], [0.1, np.nan], 0.5)


def test_missing_target_rejected(tmp_path):
    csv = tmp_path / "missing_label.csv"
    pd.DataFrame({"bytes": range(20)}).to_csv(csv, index=False)
    with pytest.raises(ValueError, match="missing"):
        prepare(csv)


def test_target_and_attack_category_are_not_used_as_features(tmp_path):
    n = 100
    df = pd.DataFrame({
        "id": range(n),
        "label": [0, 1] * 50,
        "attack_cat": ["Normal", "Generic"] * 50,
        "bytes": np.arange(n),
        "proto": ["tcp", "udp"] * 50
    })
    csv = tmp_path / "flows.csv"
    df.to_csv(csv, index=False)
    d = prepare(csv)
    assert d.x_train.shape[1] == d.x_val.shape[1] == d.x_test.shape[1]
    assert not any("attack_cat" in f or f.endswith("__id") for f in d.features)


def test_isolation_forest_requires_normal_training_samples():
    from types import SimpleNamespace
    d = SimpleNamespace(x_train=np.ones((10, 2)), y_train=np.ones(10),
                        x_val=np.ones((4, 2)), x_test=np.ones((4, 2)))
    with pytest.raises(ValueError, match="Normal"):
        isolation_forest(d)
