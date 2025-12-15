import shap, joblib
import pandas as pd
def get_reason(model_path, X_row):
    model = joblib.load(model_path)
    explainer = shap.TreeExplainer(model)
    vals = explainer.shap_values(X_row)
    feature_imp = sorted(zip(X_row.columns, vals[0]), key=lambda x: abs(x[1]), reverse=True)[:3]
    return feature_imp
