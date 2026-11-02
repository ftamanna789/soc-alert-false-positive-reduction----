"""Create a tiny *synthetic* binary network-flow CSV for smoke testing only."""
import argparse
from pathlib import Path
import numpy as np
import pandas as pd

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="data/raw/synthetic_demo.csv")
    p.add_argument("--n",type=int,default=300)
    p.add_argument("--seed",type=int,default=42)
    args=p.parse_args()
    if args.n<20: p.error("--n must be at least 20")
    rng=np.random.default_rng(args.seed)
    label=np.array([0,1]*(args.n//2)+([0] if args.n%2 else []))
    df=pd.DataFrame({
        "duration":rng.exponential(1+label*1.5),
        "src_bytes":rng.poisson(120+label*190),
        "dst_bytes":rng.poisson(80+label*30),
        "proto":np.where(rng.random(args.n)<.75,"tcp","udp"),
        "label":label
    })
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
    df.to_csv(out,index=False)
    print(f"Synthetic educational data only: {out} ({len(df)} rows)")

if __name__=="__main__":main()
