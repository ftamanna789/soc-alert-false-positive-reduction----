import json
import numpy as np
import pandas as pd
from soc_alerts.cli import main

def test_cli_isolation_forest_end_to_end(tmp_path):
    rng=np.random.default_rng(6)
    n=120
    labels=np.array([0,1]*60)
    df=pd.DataFrame({"label":labels,"duration":rng.normal(labels*2,1,n),
                     "bytes":rng.poisson(20+labels*20)})
    csv=tmp_path/"data.csv";out=tmp_path/"out.json"
    df.to_csv(csv,index=False)
    main(["--csv",str(csv),"--model","isolation_forest","--output",str(out),"--seed","12"])
    r=json.loads(out.read_text())
    assert r["split"]=={"train":72,"validation":24,"test":24}
    assert r["test_metrics"]["tp"]+r["test_metrics"]["fn"]==12
    assert r["test_metrics"]["fp"]+r["test_metrics"]["tn"]==12
