import subprocess
import time
import webbrowser
import requests

# ⚠️ UPDATE PATHS
ELASTIC_PATH = r"D:\Applications\elasticsearch-9.3.2\bin\elasticsearch.bat"
KIBANA_PATH = r"D:\Applications\kibana-9.3.1\bin\kibana.bat"

processes = []


# ---------------------------
# WAIT FOR ELASTICSEARCH
# ---------------------------
def wait_for_elasticsearch():
    print("Waiting for Elasticsearch...")

    while True:
        try:
            res = requests.get("http://localhost:9200")
            if res.status_code in [200, 401]:
                print("Elasticsearch is ready.")
                return
        except:
            pass

        time.sleep(3)


# ---------------------------
# WAIT FOR KIBANA (SMART)
# ---------------------------
def wait_for_kibana(timeout=120):
    print("Checking if Kibana is ready...")

    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            res = requests.get("http://localhost:5601")

            # Kibana returns HTML when ready
            if res.status_code == 200 and "kibana" in res.text.lower():
                print("Kibana is ready.")
                return True

        except:
            pass

        time.sleep(5)

    print("Kibana not fully ready, continuing anyway...")
    return False


# ---------------------------
# START ELASTICSEARCH
# ---------------------------
def start_elasticsearch():
    print("Starting Elasticsearch...")
    p = subprocess.Popen(ELASTIC_PATH, shell=True)
    processes.append(p)

    wait_for_elasticsearch()


# ---------------------------
# START KIBANA
# ---------------------------
def start_kibana():
    print("Starting Kibana...")
    p = subprocess.Popen(KIBANA_PATH, shell=True)
    processes.append(p)

    # Smart wait (non-blocking)
    wait_for_kibana()


# ---------------------------
# OPEN KIBANA
# ---------------------------
def open_kibana():
    print("Opening Kibana in browser...")
    webbrowser.open("http://localhost:5601")


# ---------------------------
# START SIMULATOR
# ---------------------------
def start_simulator():
    print("Starting Attack Simulator...")
    p = subprocess.Popen(
        ["python", "attack_simulator/brute_force_simulator.py"],
        shell=True
    )
    processes.append(p)


# ---------------------------
# START DETECTOR
# ---------------------------
def start_detector():
    print("Starting Detection Engine...")
    p = subprocess.Popen(
        ["python", "-m", "detection_engine.distributed_detector"],
        shell=True
    )
    processes.append(p)


# ---------------------------
# START ML DETECTOR
# ---------------------------
def start_ml_detector():
    print("Starting ML Detection Engine...")
    p = subprocess.Popen(
        ["python", "-m", "detection_engine.ml_detector"],
        shell=True
    )
    processes.append(p)


# ---------------------------
# START SENDER
# ---------------------------
def start_sender():
    print("Starting Log Sender...")
    p = subprocess.Popen(
        ["python", "log_collection/send_logs_to_elasticsearch.py"],
        shell=True
    )
    processes.append(p)


# ---------------------------
# STOP ALL
# ---------------------------
def stop_all():
    print("Stopping all processes...")
    for p in processes:
        try:
            p.kill()
        except:
            pass
    processes.clear()


# ---------------------------
# FULL SYSTEM
# ---------------------------
def start_full_system():
    start_simulator()
    start_detector()
    start_ml_detector()
    start_sender()


# ---------------------------
# MENU
# ---------------------------
def menu():
    while True:
        print("\n==== BRUTE FORCE DETECTION SYSTEM ====")
        print("1. Start ELK Stack")
        print("2. Start Detection System")
        print("3. Run Full System")
        print("4. Stop All")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            start_elasticsearch()
            start_kibana()
            open_kibana()

        elif choice == "2":
            start_simulator()
            start_detector()
            start_ml_detector()
            start_sender()

        elif choice == "3":
            start_full_system()

        elif choice == "4":
            stop_all()

        elif choice == "5":
            stop_all()
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()