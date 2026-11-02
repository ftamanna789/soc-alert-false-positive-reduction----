import numpy as np
import pandas as pd
import pytest
from soc_alerts.data import prepare

def test_prepare_splits_and_excludes_identifiers(tmp_path):
    rng=np.random.default_rng(3)
    n=100
    df=pd.DataFrame({"label":[0,1]*50,"duration":rng.normal(size=n),
                     "bytes":rng.integers(0,100,size=n),"proto":["tcp","udp"]*50,
                     "src_ip":["192.0.2.1"]*n})
    path=tmp_path/"flows.csv"
    df.to_csv(path,index=False)
    d=prepare(path,seed=9)
    assert len(d.y_train)==60
    assert len(d.y_val)==20
    assert len(d.y_test)==20
    assert d.x_train.shape[1]==d.x_test.shape[1]
    assert all("src_ip" not in x for x in d.features)
    assert np.isfinite(d.x_train).all()

def test_invalid_label_rejected(tmp_path):
    p=tmp_path/"bad.csv"
    pd.DataFrame({"label":[0,2]*10,"a":range(20)}).to_csv(p,index=False)
    with pytest.raises(ValueError,match="Expected exactly"):
        prepare(p)
