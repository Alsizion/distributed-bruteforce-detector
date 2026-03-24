from pathlib import Path
from collections import defaultdict, deque
import time

from alerting.alert_service import send_alert

BASE_DIR = Path(__file__).resolve().parent.parent
log_file = BASE_DIR / "dataset" / "simulated_attack.log"

# Store timestamps of attempts per user
user_attempts = defaultdict(deque)
user_ips = defaultdict(set)

# CONFIG (important)
TIME_WINDOW = 10  # seconds
ATTEMPT_THRESHOLD = 50
IP_THRESHOLD = 10

print("Monitoring logs with time-window detection...")

with open(log_file, "r") as f:
    f.seek(0, 2)

    while True:
        line = f.readline()

        if not line:
            time.sleep(0.1)
            continue

        if "Failed password" in line:
            parts = line.split()
            user = parts[8]
            ip = parts[10]

            current_time = time.time()

            # Track attempts
            user_attempts[user].append(current_time)
            user_ips[user].add(ip)

            # Remove old attempts outside window
            while user_attempts[user] and current_time - user_attempts[user][0] > TIME_WINDOW:
                user_attempts[user].popleft()

            # Detection condition
            if (
                len(user_attempts[user]) > ATTEMPT_THRESHOLD and
                len(user_ips[user]) > IP_THRESHOLD
            ):
                send_alert(
                    user,
                    len(user_ips[user]),
                    len(user_attempts[user])
                )

                # Reset after alert
                user_attempts[user].clear()
                user_ips[user].clear()