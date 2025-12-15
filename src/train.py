import joblib
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score, precision_recall_curve, auc

def train_basic_model(df, features, target='label'):
    X = df[features]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    dtrain = xgb.DMatrix(X_train, label=y_train)
    dtest = xgb.DMatrix(X_test, label=y_test)
    params = {"objective":"binary:logistic", "eval_metric":"auc", "eta":0.1, "max_depth":6}
    model = xgb.train(params, dtrain, num_boost_round=200)
    preds = model.predict(dtest)
    print("ROC AUC:", roc_auc_score(y_test, preds))
    # Precision-recall AUC
    p, r, _ = precision_recall_curve(y_test, preds)
    print("PR AUC:", auc(r, p))
    joblib.dump(model, "models/xgb.model")
    return model
