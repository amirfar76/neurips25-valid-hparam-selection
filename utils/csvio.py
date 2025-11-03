
import pandas as pd
import numpy as np

def load_losses_csv(path, id_col='hyperparam_id', loss_prefix='loss_'):
    df = pd.read_csv(path)
    if id_col not in df.columns:
        raise ValueError(f"Expected an id column '{id_col}' in {path}")
    loss_cols = [c for c in df.columns if c.startswith(loss_prefix)]
    if not loss_cols:
        loss_cols = [c for c in df.columns if c != id_col and pd.api.types.is_numeric_dtype(df[c])]
        if not loss_cols:
            raise ValueError("No loss columns found. Use loss_1, loss_2, ... or numeric cols.")
    losses = df[loss_cols].to_numpy(dtype=float)
    ids = df[id_col].astype(str).to_numpy()
    return ids, losses, loss_cols

def is_binary_array(x, tol=1e-12):
    x = np.asarray(x)
    return np.all((np.abs(x - 0) < tol) | (np.abs(x - 1) < tol))

def summarize(ids, losses):
    m, n = losses.shape
    means = losses.mean(axis=1)
    return pd.DataFrame({'hyperparam_id': ids, 'mean_loss': means, 'n_cal': n})
