import numpy as np
import pytest
from soc_alerts.metrics import select_threshold,measure

def test_recall_constraint_met():
    y=np.array([0,0,1,1])
    s=np.array([.1,.2,.8,.9])
    t,ok=select_threshold(y,s,min_recall=1)
    assert ok
    out=measure(y,s,t)
    assert out["fp"]==0 and out["fn"]==0

def test_no_recall_constraint_allows_no_alerts():
    t,ok=select_threshold([0,1],[.1,.8],min_recall=0)
    assert ok
    assert measure([0,1],[.1,.8],t)["tp"]==0

def test_validation_requires_both_classes():
    with pytest.raises(ValueError,match="both classes"):
        select_threshold([0,0],[.1,.2])

def test_reject_nan_scores():
    with pytest.raises(ValueError,match="finite"):
        select_threshold([0,1],[float("nan"),.2])
