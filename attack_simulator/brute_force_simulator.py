from pathlib import Path
import random

# Get project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Define log file path safely
log_path = BASE_DIR / "dataset" / "simulated_attack.log"

users = ["admin"]
ips = [f"192.168.1.{i}" for i in range(10,60)]

# Ensure dataset folder exists
log_path.parent.mkdir(exist_ok=True)

with open(log_path, "w") as f:
    for _ in range(200):
        ip = random.choice(ips)
        user = random.choice(users)

        log = f"Jan 10 10:01:11 server sshd[123]: Failed password for {user} from {ip} port 22 ssh2\n"
        f.write(log)

print(f"Attack logs generated at: {log_path}")