# Here, Convert raw transactions into signals humans and models can understand.
# where ML learns patterns and anomalies are easier to detect.


import pandas as pd
import numpy as np
from geopy.distance import geodesic

def compute_basic_features(df):
    df = df.sort_values(['user_id','timestamp']).copy()
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour
    df['dayofweek'] = df['timestamp'].dt.dayofweek
    df['log_amount'] = np.log1p(df['amount'])
    # time since last tx per user
    df['prev_ts'] = df.groupby('user_id')['timestamp'].shift(1)
    df['secs_since_prev'] = (df['timestamp'] - df['prev_ts']).dt.total_seconds().fillna(999999)
    # distance
    df['prev_loc'] = df.groupby('user_id')[['lat','lon']].shift(1).apply(lambda r: (r['lat'], r['lon']) if pd.notnull(r['lat']) else None, axis=1)
    def dist(row):
        if row['prev_loc'] is None:
            return 0.0
        return geodesic((row['lat'], row['lon']), row['prev_loc']).km
    df['distance_km'] = df.apply(dist, axis=1)
    # velocity features
    df['tx_count_1h'] = df.groupby('user_id')['timestamp'].rolling('1h', on='timestamp').count().reset_index(0,drop=True).fillna(0)
    df['tx_count_24h'] = df.groupby('user_id')['timestamp'].rolling('24h', on='timestamp').count().reset_index(0,drop=True).fillna(0)
    return df
