"""Generate *clearly labelled* figures from recorded dissertation summaries or reference outputs.

Never present literature-reported plots as independently rerun model evaluations.
"""
import argparse
import json
from pathlib import Path

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--source",choices=["reported","reference"],required=True)
    p.add_argument("--input",default=None,help="Reference CLI output JSON")
    p.add_argument("--output",default="artifacts")
    a=p.parse_args()
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    out=Path(a.output);out.mkdir(parents=True,exist_ok=True)
    if a.source=="reported":
        labels=["Isolation Forest","Autoencoder comparison","TabNet"]
        before=[4053,12235,7347]
        after=[2145,5611,3145]
        note="Dissertation reported FP counts; comparisons use different test sets/baselines"
        fig,ax=plt.subplots(figsize=(10,5))
        x=list(range(len(labels)))
        ax.bar([v-.18 for v in x],before,width=.36,label="Baseline/comparator")
        ax.bar([v+.18 for v in x],after,width=.36,label="Tuned/selected")
        ax.set_xticks(x,labels)
        ax.set_ylabel("False-positive count")
        ax.set_title("Reported experiments — NOT independently reproduced")
        ax.legend()
        fig.text(.5,.01,note,ha="center",fontsize=8)
        fig.tight_layout(rect=(0,.04,1,1))
        dest=out/"reported_false_positives.png"
    else:
        if not a.input: p.error("--input is required for reference figures")
        report=json.loads(Path(a.input).read_text(encoding="utf-8"))
        m=report["test_metrics"]
        labels=["TN","FP","FN","TP"]
        values=[m[k] for k in ("tn","fp","fn","tp")]
        fig,ax=plt.subplots(figsize=(7,4))
        ax.bar(labels,values)
        ax.set_ylabel("Test-set count")
        ax.set_title(f"Reference implementation (unverified provenance): {report['model']}")
        fig.tight_layout()
        dest=out/"reference_confusion_counts.png"
    fig.savefig(dest,dpi=180)
    print(dest)

if __name__=="__main__": main()
