from sklearn.ensemble import IsolationForest
import pandas as pd
import time

LOG_FILE = "dataset/simulated_attack.log"

def extract_features():
    data = []

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    user_attempts = {}
    user_ips = {}

    for line in lines:
        parts = line.split()

        if "Failed" in line:
            user = parts[8]
            ip = parts[10]

            user_attempts[user] = user_attempts.get(user, 0) + 1
            user_ips.setdefault(user, set()).add(ip)

    for user in user_attempts:
        data.append([
            user_attempts[user],
            len(user_ips[user])
        ])

    return pd.DataFrame(data, columns=["attempts", "unique_ips"])


def run_ml_detection():
    print("Running ML-based detection...")

    while True:
        df = extract_features()

        if len(df) < 5:
            time.sleep(5)
            continue

        model = IsolationForest(contamination=0.2)
        df["anomaly"] = model.fit_predict(df)

        anomalies = df[df["anomaly"] == -1]

        if not anomalies.empty:
            print("⚠️ ML ALERT: Anomalous behavior detected")
            print(anomalies)

        time.sleep(5)


if __name__ == "__main__":
    run_ml_detection()