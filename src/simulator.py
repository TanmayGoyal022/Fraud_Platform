import pandas as pd
import numpy as np
from datetime import timedelta

def inject_impossible_travel(df, fraction=0.001):
    df = df.copy()
    n = int(len(df) * fraction)
    idx = np.random.choice(df.index, n, replace=False)
    for i in idx:
        df.at[i, 'lat'] = 0.0
        df.at[i, 'lon'] = 0.0
        df.at[i, 'amount'] *= 5
        df.at[i, 'label'] = 1
    return df
