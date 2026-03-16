import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(logs):

    df = pd.DataFrame(logs)

    df["event_code"] = df["event"].astype("category").cat.codes
    df["ip_code"] = df["ip"].astype("category").cat.codes

    X = df[["event_code", "ip_code"]]

    model = IsolationForest(contamination=0.1)

    df["anomaly"] = model.fit_predict(X)

    anomalies = df[df["anomaly"] == -1]

    return anomalies.to_dict(orient="records")