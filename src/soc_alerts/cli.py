"""Command line interface for reproducible reference experiments."""
import argparse
import json
from pathlib import Path
from .data import prepare
from .metrics import measure,select_threshold
from .models import MODELS

def main(argv=None):
    p=argparse.ArgumentParser(description="SOC anomaly detection reference experiment")
    p.add_argument("--csv",required=True,help="Path to verified, labelled CSV")
    p.add_argument("--label",default="label")
    p.add_argument("--model",choices=sorted(MODELS),default="isolation_forest")
    p.add_argument("--output",default="artifacts/results.json")
    p.add_argument("--seed",type=int,default=42)
    p.add_argument("--min-recall",type=float,default=.90)
    p.add_argument("--epochs",type=int,default=20)
    args=p.parse_args(argv)
    d=prepare(args.csv,label=args.label,seed=args.seed)
    s_val,s_test=MODELS[args.model](d,seed=args.seed,epochs=args.epochs)
    threshold,met=select_threshold(d.y_val,s_val,args.min_recall)
    report={"model":args.model,"study":"reference implementation (not original dissertation run)",
            "split":{"train":len(d.y_train),"validation":len(d.y_val),"test":len(d.y_test)},
            "feature_count":len(d.features),"seed":args.seed,
            "selection":{"minimum_attack_recall":args.min_recall,"recall_constraint_met":met},
            "validation_metrics":measure(d.y_val,s_val,threshold),
            "test_metrics":measure(d.y_test,s_test,threshold)}
    path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))
    return report

if __name__=="__main__":
    main()
