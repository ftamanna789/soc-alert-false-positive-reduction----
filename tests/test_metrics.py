import numpy as np
from soc_alerts.metrics import measure, select_threshold

def test_confusion_matrix_convention():
    out=measure([0,0,1,1],[0.1,0.8,0.4,0.9],0.5)
    assert (out['tn'],out['fp'],out['fn'],out['tp'])==(1,1,1,1)
    assert out['false_positive_rate']==0.5

def test_threshold_uses_validation_labels_only():
    y=np.array([0,0,1,1]);scores=np.array([0.1,0.2,0.7,0.9])
    threshold,met=select_threshold(y,scores,min_recall=1)
    assert met is True
    assert measure(y,scores,threshold)['fp']==0
