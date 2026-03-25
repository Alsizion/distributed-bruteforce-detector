from pathlib import Path
import random
import time

BASE_DIR = Path(__file__).resolve().parent.parent
log_path = BASE_DIR / "dataset" / "simulated_attack.log"

users = ["admin"]
ips = [f"192.168.1.{i}" for i in range(10,60)]

log_path.parent.mkdir(exist_ok=True)

# 🔥 CONTROL SETTINGS
RUN_FOREVER = False        # True = infinite attack
TOTAL_LOGS = 2000          # used if RUN_FOREVER = False
DELAY = 0.05               # speed of attack (seconds)

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