from fastapi import FastAPI
import numpy as np
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()
xgb_model = joblib.load("models/xgb.model")
iso = joblib.load("models/iso.model")

class Tx(BaseModel):
    user_id: str
    amount: float
    timestamp: str
    merchant_id: str
    lat: float
    lon: float
    device_id: str

def featurize_single(tx: dict):
    # Very small featurizer; in prod use same pipeline objects (sklearn Pipeline)
    df = pd.DataFrame([tx])
    # compute log amount etc...
    df['log_amount'] = np.log1p(df['amount'])
    # add placeholders for velocity/distance (real system queries last transactions)
    df['secs_since_prev'] = 999999
    df['distance_km'] = 0.0
    return df

@app.post("/score")
def score(tx: Tx):
    df = featurize_single(tx.dict())
    dmat = xgb.DMatrix(df)   # if using xgboost native model else use model.predict_proba
    ml_score = float(xgb_model.predict(dmat)[0])
    anomaly = iso.decision_function(df.fillna(0))[0]
    final_score = 0.7 * ml_score + 0.3 * (1 - (anomaly))
    action = "allow" if final_score < 0.5 else ("review" if final_score < 0.85 else "block")
    return {"score": final_score, "action": action, "ml_score": ml_score, "anomaly": float(anomaly)}
