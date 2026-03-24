from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
alert_file = BASE_DIR / "alerting" / "alerts.log"

def send_alert(user, unique_ips, attempts):

    alert_file.parent.mkdir(exist_ok=True)

    alert_message = (
        f"{datetime.now()} | ALERT | Distributed Brute Force "
        f"| User: {user} | Unique IPs: {unique_ips} | Attempts: {attempts}\n"
    )

    print(alert_message)

    with open(alert_file, "a") as f:
        f.write(alert_message)