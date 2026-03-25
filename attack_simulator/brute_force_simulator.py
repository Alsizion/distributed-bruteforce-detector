from pathlib import Path
import random
import time

BASE_DIR = Path(__file__).resolve().parent.parent

log_path = BASE_DIR / "dataset" / "simulated_attack.log"
alert_path = BASE_DIR / "alerting" / "alerts.log"

# 👤 Users
users = ["admin", "root", "user1", "guest", "test"]

# 🌍 IP pools
attacker_ips = [f"192.168.1.{i}" for i in range(10, 60)]
normal_ips = [f"10.0.0.{i}" for i in range(1, 20)]

# ⚙️ CONTROL
RESET_LOGS = True
TOTAL_LOGS = 1500
DELAY = 0.02

# 🧹 Reset logs
if RESET_LOGS:
    open(log_path, "w").close()
    open(alert_path, "w").close()
    print("Logs reset.")

print("Starting realistic attack simulation...")

with open(log_path, "a") as f:

    for i in range(TOTAL_LOGS):

        # 🎯 Choose scenario
        scenario = random.choice([
            "distributed_attack",
            "normal_activity",
            "mixed_noise"
        ])

        # -------------------------------
        # 🔴 DISTRIBUTED ATTACK
        # -------------------------------
        if scenario == "distributed_attack":
            user = "admin"
            ip = random.choice(attacker_ips)

            log = f"Jan 10 10:01:11 server sshd[123]: Failed password for {user} from {ip} port 22 ssh2\n"

        # -------------------------------
        # 🟢 NORMAL USER ACTIVITY
        # -------------------------------
        elif scenario == "normal_activity":
            user = random.choice(users)
            ip = random.choice(normal_ips)

            success = random.choice([True, False, False])

            if success:
                log = f"Jan 10 10:01:11 server sshd[123]: Accepted password for {user} from {ip} port 22 ssh2\n"
            else:
                log = f"Jan 10 10:01:11 server sshd[123]: Failed password for {user} from {ip} port 22 ssh2\n"

        # -------------------------------
        # 🟡 NOISE TRAFFIC
        # -------------------------------
        else:
            user = random.choice(users)
            ip = random.choice(attacker_ips + normal_ips)

            log = f"Jan 10 10:01:11 server sshd[123]: Failed password for {user} from {ip} port 22 ssh2\n"

        f.write(log)
        f.flush()

        time.sleep(DELAY)

print("Simulation complete.")