"""Efficient binary alert metrics and validation-only threshold selection."""
import numpy as np
from sklearn.metrics import confusion_matrix,roc_auc_score,precision_score,recall_score,accuracy_score,roc_curve

def measure(y_true,scores,threshold):
    y=np.asarray(y_true,dtype=int)
    s=np.asarray(scores,dtype=float)
    if y.ndim!=1 or s.ndim!=1 or len(y)!=len(s) or not len(y):
        raise ValueError("y_true and scores must be matching non-empty vectors")
    if not np.isfinite(s).all() or not set(np.unique(y)).issubset({0,1}):
        raise ValueError("Expected finite scores and binary labels 0/1")
    pred=(s>=threshold).astype(int)
    tn,fp,fn,tp=confusion_matrix(y,pred,labels=[0,1]).ravel()
    try: auc=float(roc_auc_score(y,s))
    except ValueError: auc=None
    return {"threshold":float(threshold),"tn":int(tn),"fp":int(fp),"fn":int(fn),"tp":int(tp),
            "false_positive_rate":float(fp/(fp+tn)) if fp+tn else None,
            "attack_recall":float(recall_score(y,pred,zero_division=0)),
            "precision":float(precision_score(y,pred,zero_division=0)),
            "accuracy":float(accuracy_score(y,pred)),"roc_auc":auc}

def select_threshold(y_val,scores,min_recall=.90):
    """Select a threshold on validation data only, targeting minimal FPR at required recall.

    Complexity O(n log n) rather than evaluating every threshold with full metric passes.
    Requires both classes in validation labels.
    """
    y=np.asarray(y_val,dtype=int)
    s=np.asarray(scores,dtype=float)
    if not 0<=min_recall<=1: raise ValueError("min_recall must be between 0 and 1")
    if y.ndim!=1 or s.ndim!=1 or not len(y) or len(y)!=len(s):
        raise ValueError("Validation labels and scores must be matching non-empty vectors")
    if set(np.unique(y))!={0,1} or not np.isfinite(s).all():
        raise ValueError("Validation must contain both classes and finite scores")
    fpr,tpr,thresholds=roc_curve(y,s,drop_intermediate=False)
    feasible=np.flatnonzero(tpr>=min_recall)
    if len(feasible):
        i=int(feasible[np.argmin(fpr[feasible])])
        met=True
    else:
        i=int(np.argmax(tpr))
        met=False
    # ROC threshold inf means no predicted positives, valid for min_recall=0.
    return float(thresholds[i]),met
