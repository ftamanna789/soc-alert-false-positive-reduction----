"""Data validation and train-only preprocessing for network-flow datasets."""
from dataclasses import dataclass
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

DROP_COLUMNS = {'src_ip', 'dst_ip', 'id', 'flow_id', 'attack_cat', 'attack_category', 'type', 'category'}

@dataclass
class Prepared:
    x_train: np.ndarray
    x_val: np.ndarray
    x_test: np.ndarray
    y_train: np.ndarray
    y_val: np.ndarray
    y_test: np.ndarray
    features: list[str]

def prepare(csv: str | Path, label: str = 'label', seed: int = 42) -> Prepared:
    df = pd.read_csv(csv)
    if label not in df.columns:
        raise ValueError(f"Target column {label!r} is missing")
    y = pd.to_numeric(df[label], errors='raise')
    if set(y.dropna().unique()) != {0, 1} or y.isna().any():
        raise ValueError('Expected exactly two labels: 0=normal, 1=attack; check dataset first')
    excluded = set(DROP_COLUMNS) | {label}
    X = df.drop(columns=[c for c in df.columns if c.lower() in excluded])
    number_cols = X.select_dtypes(include=np.number).columns.tolist()
    cat_cols = [c for c in X.columns if c not in number_cols and X[c].nunique(dropna=True) <= 100]
    X = X[number_cols + cat_cols].copy()
    if X.empty:
        raise ValueError('No usable features available after exclusions')
    x_train, x_test, y_train, y_test = train_test_split(X, y.astype(int).to_numpy(), test_size=.2, stratify=y, random_state=seed)
    x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=.25, stratify=y_train, random_state=seed)
    transformers=[]
    if number_cols:
        transformers.append(('numeric', Pipeline([('impute', SimpleImputer(strategy='median')), ('scale', StandardScaler())]), number_cols))
    if cat_cols:
        transformers.append(('categorical', Pipeline([('impute', SimpleImputer(strategy='most_frequent')), ('encode', OneHotEncoder(handle_unknown='ignore', sparse_output=False))]), cat_cols))
    pre=ColumnTransformer(transformers, sparse_threshold=0)
    a=pre.fit_transform(x_train).astype(np.float32)
    b=pre.transform(x_val).astype(np.float32)
    c=pre.transform(x_test).astype(np.float32)
    return Prepared(a,b,c,np.asarray(y_train),np.asarray(y_val),np.asarray(y_test),list(pre.get_feature_names_out()))
