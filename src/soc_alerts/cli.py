"""Command-line entry point; independent baseline reference runs (not dissertation replication)."""
import argparse
import json
from pathlib import Path
import numpy as np
from sklearn.ensemble import IsolationForest
from .data import prepare
from .metrics import measure, select_threshold

def run(model, d, seed, epochs):
    if model=='isolation_forest':
        detector=IsolationForest(n_estimators=200,contamination='auto',random_state=seed,n_jobs=-1)
        detector.fit(d.x_train[d.y_train==0])
        return -detector.score_samples(d.x_val),-detector.score_samples(d.x_test)
    if model=='autoencoder':
        try:
            import tensorflow as tf
        except ImportError as e:
            raise SystemExit('Install optional extras: pip install -e ".[autoencoder]"') from e
        tf.keras.utils.set_random_seed(seed)
        dim=d.x_train.shape[1]
        network=tf.keras.Sequential([
            tf.keras.layers.Input(shape=(dim,)),
            tf.keras.layers.Dense(64,activation='relu'),
            tf.keras.layers.Dense(32,activation='relu'),
            tf.keras.layers.Dense(16,activation='relu'),
            tf.keras.layers.Dense(32,activation='relu'),
            tf.keras.layers.Dense(dim),
        ])
        network.compile(optimizer='adam',loss='mse')
        normal=d.x_train[d.y_train==0]
        network.fit(normal,normal,batch_size=256,epochs=epochs,validation_split=.1,verbose=0)
        return [np.mean((part-network.predict(part,verbose=0))**2,axis=1) for part in (d.x_val,d.x_test)]
    if model=='tabnet':
        try:
            from pytorch_tabnet.tab_model import TabNetClassifier
        except ImportError as e:
            raise SystemExit('Install optional extras: pip install -e ".[tabnet]"') from e
        clf=TabNetClassifier(seed=seed,verbose=0)
        clf.fit(d.x_train,d.y_train,eval_set=[(d.x_val,d.y_val)],max_epochs=epochs,patience=max(1,min(10,epochs)))
        return clf.predict_proba(d.x_val)[:,1],clf.predict_proba(d.x_test)[:,1]
    raise ValueError(model)

def main():
    ap=argparse.ArgumentParser(description='Reference SOC anomaly detection experiment')
    ap.add_argument('--csv',required=True,help='Path to labelled flow CSV; raw data is not included')
    ap.add_argument('--label',default='label')
    ap.add_argument('--model',choices=['isolation_forest','autoencoder','tabnet'],default='isolation_forest')
    ap.add_argument('--output',default='artifacts/results.json')
    ap.add_argument('--seed',type=int,default=42)
    ap.add_argument('--min-recall',type=float,default=.90)
    ap.add_argument('--epochs',type=int,default=20)
    args=ap.parse_args()
    d=prepare(args.csv,label=args.label,seed=args.seed)
    s_val,s_test=run(args.model,d,args.seed,args.epochs)
    threshold,met=select_threshold(d.y_val,s_val,args.min_recall)
    output={'model':args.model,'study':'reference implementation (not original dissertation run)',
            'split':{'train':len(d.y_train),'validation':len(d.y_val),'test':len(d.y_test)},
            'feature_count':len(d.features),'selection':{'min_attack_recall':args.min_recall,'recall_constraint_met':met},
            'validation_metrics':measure(d.y_val,s_val,threshold),
            'test_metrics':measure(d.y_test,s_test,threshold)}
    path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(output,indent=2))

if __name__=='__main__':main()
