"""Metrics and validation-only decision threshold selection."""
import numpy as np
from sklearn.metrics import confusion_matrix, roc_auc_score, precision_score, recall_score, accuracy_score

def measure(y_true, scores, threshold):
    y=np.asarray(y_true, dtype=int)
    s=np.asarray(scores, dtype=float)
    pred=(s>=threshold).astype(int)
    tn,fp,fn,tp=confusion_matrix(y,pred,labels=[0,1]).ravel()
    try: auc=float(roc_auc_score(y,s))
    except ValueError: auc=None
    return {'threshold':float(threshold),'tn':int(tn),'fp':int(fp),'fn':int(fn),'tp':int(tp),
            'false_positive_rate':float(fp/(fp+tn)) if fp+tn else None,
            'attack_recall':float(recall_score(y,pred,zero_division=0)),
            'precision':float(precision_score(y,pred,zero_division=0)),
            'accuracy':float(accuracy_score(y,pred)), 'roc_auc':auc}

def select_threshold(y_val,scores,min_recall=.90):
    """Among recall-feasible thresholds, minimise FPR; never inspect test labels."""
    if not (0<=min_recall<=1): raise ValueError('min_recall must be between 0 and 1')
    scores=np.asarray(scores,dtype=float)
    if scores.ndim!=1 or not np.isfinite(scores).all(): raise ValueError('scores must be finite and one-dimensional')
    candidates=np.unique(np.r_[np.nextafter(scores.min(),-np.inf),scores,np.nextafter(scores.max(),np.inf)])
    results=[measure(y_val,scores,t) for t in candidates]
    feasible=[r for r in results if r['attack_recall'] >= min_recall]
    if feasible:
        chosen=min(feasible,key=lambda r:(r['false_positive_rate'], -r['attack_recall']))
    else:
        chosen=min(results,key=lambda r:(-r['attack_recall'],r['false_positive_rate']))
    return chosen['threshold'],bool(feasible)
