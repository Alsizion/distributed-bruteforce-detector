from pathlib import Path
from elasticsearch import Elasticsearch
import time

ELASTIC_PASSWORD = "v7M1+6X_HE4Tvib0hSMH"

es = Elasticsearch(
    "http://localhost:9200", 
    basic_auth=("elastic", ELASTIC_PASSWORD)
)

BASE_DIR = Path(__file__).resolve().parent.parent
log_file = BASE_DIR / "dataset" / "simulated_attack.log"

print("Sending logs to Elasticsearch...")

with open(log_file, "r") as f:
    f.seek(0, 2)

    while True:
        line = f.readline()

        if not line:
            time.sleep(0.1)
            continue

        if "Failed password" in line:
            parts = line.split()

            log_data = {
                "timestamp": time.time(),
                "user": parts[8],
                "source_ip": parts[10],
                "event": "failed_login"
            }

            es.index(index="auth-logs", document=log_data)

            print("Sent:", log_data)