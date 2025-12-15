from sklearn.ensemble import IsolationForest
import joblib

def train_iso(df, features):
    X = df[features].fillna(0)
    iso = IsolationForest(n_estimators=100, contamination=0.001, random_state=42)
    iso.fit(X)
    joblib.dump(iso, "models/iso.model")
    return iso
