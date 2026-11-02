"""Model implementations for reference experiments (not original dissertation notebooks)."""
import numpy as np
from sklearn.ensemble import IsolationForest

def isolation_forest(d, seed=42, epochs=20):
    model=IsolationForest(n_estimators=200,contamination="auto",random_state=seed,n_jobs=-1)
    normal=d.x_train[d.y_train==0]
    if len(normal)==0: raise ValueError("Normal training records required")
    model.fit(normal)
    return -model.score_samples(d.x_val),-model.score_samples(d.x_test)

def autoencoder(d, seed=42, epochs=20):
    try:
        import tensorflow as tf
    except ImportError as e:
        raise RuntimeError('Install with: pip install -e ".[autoencoder]"') from e
    tf.keras.utils.set_random_seed(seed)
    dim=d.x_train.shape[1]
    model=tf.keras.Sequential([
        tf.keras.layers.Input(shape=(dim,)),
        tf.keras.layers.Dense(64,activation="relu"),
        tf.keras.layers.Dense(32,activation="relu"),
        tf.keras.layers.Dense(16,activation="relu"),
        tf.keras.layers.Dense(32,activation="relu"),
        tf.keras.layers.Dense(dim)
    ])
    model.compile(optimizer="adam",loss="mse")
    normal=d.x_train[d.y_train==0]
    if len(normal)<2: raise ValueError("At least two normal training samples required")
    model.fit(normal,normal,validation_split=.1,batch_size=256,epochs=epochs,verbose=0)
    return tuple(np.mean((x-model.predict(x,verbose=0))**2,axis=1) for x in (d.x_val,d.x_test))

def tabnet(d, seed=42, epochs=20):
    try:
        from pytorch_tabnet.tab_model import TabNetClassifier
    except ImportError as e:
        raise RuntimeError('Install with: pip install -e ".[tabnet]"') from e
    model=TabNetClassifier(seed=seed,verbose=0)
    model.fit(d.x_train,d.y_train,eval_set=[(d.x_val,d.y_val)],
              max_epochs=epochs,patience=max(1,min(10,epochs)))
    return model.predict_proba(d.x_val)[:,1],model.predict_proba(d.x_test)[:,1]

MODELS={"isolation_forest":isolation_forest,"autoencoder":autoencoder,"tabnet":tabnet}
