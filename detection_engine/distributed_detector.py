from pathlib import Path
from collections import defaultdict
from alerting.alert_service import send_alert

BASE_DIR = Path(__file__).resolve().parent.parent
log_file = BASE_DIR / "dataset" / "simulated_attack.log"

user_ips = defaultdict(set)
user_attempts = defaultdict(int)

with open(log_file) as f:
    for line in f:
        if "Failed password" in line:
            parts = line.split()
            user = parts[8]
            ip = parts[10]

            user_ips[user].add(ip)
            user_attempts[user] += 1

for user in user_attempts:
    if len(user_ips[user]) > 10 and user_attempts[user] > 50:

        send_alert(
        user,
        len(user_ips[user]),
        user_attempts[user]
        )

    user_ips[user].clear()
    user_attempts[user] = 0