from pathlib import Path
import random
import time

BASE_DIR = Path(__file__).resolve().parent.parent

log_path = BASE_DIR / "dataset" / "simulated_attack.log"
alert_path = BASE_DIR / "alerting" / "alerts.log"

users = ["admin"]
ips = [f"192.168.1.{i}" for i in range(10,60)]

# 🔥 CONTROL SETTINGS
RESET_LOGS = True        # delete old logs before starting
RUN_FOREVER = False
TOTAL_LOGS = 250
DELAY = 0.05

# 🧹 RESET FILES
if RESET_LOGS:
    log_path.parent.mkdir(exist_ok=True)
    alert_path.parent.mkdir(exist_ok=True)

    open(log_path, "w").close()      # clear simulated logs
    open(alert_path, "w").close()    # clear alerts

    print("Old logs cleared.")

print("Starting distributed attack simulation...")

with open(log_path, "a") as f:

    if RUN_FOREVER:
        while True:
            ip = random.choice(ips)
            user = random.choice(users)

            log = f"Jan 10 10:01:11 server sshd[123]: Failed password for {user} from {ip} port 22 ssh2\n"
            f.write(log)
            f.flush()

            time.sleep(DELAY)

    else:
        for _ in range(TOTAL_LOGS):
            ip = random.choice(ips)
            user = random.choice(users)

            log = f"Jan 10 10:01:11 server sshd[123]: Failed password for {user} from {ip} port 22 ssh2\n"
            f.write(log)
            f.flush()

            time.sleep(DELAY)

print("Simulation complete.")