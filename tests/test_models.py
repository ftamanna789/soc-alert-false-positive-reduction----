import numpy as np
from types import SimpleNamespace
from soc_alerts.models import MODELS

def test_isolation_forest_output_shape_and_finite():
    rng=np.random.default_rng(42)
    d=SimpleNamespace(
        x_train=rng.normal(size=(40,3)).astype("float32"),
        y_train=np.array([0]*30+[1]*10),
        x_val=rng.normal(size=(10,3)).astype("float32"),
        x_test=rng.normal(size=(8,3)).astype("float32")
    )
    a,b=MODELS["isolation_forest"](d,seed=1)
    assert a.shape==(10,) and b.shape==(8,)
    assert np.isfinite(a).all() and np.isfinite(b).all()
