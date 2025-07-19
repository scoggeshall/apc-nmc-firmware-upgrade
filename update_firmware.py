import csv
import subprocess
import time
import socket
import json
import sys
from pathlib import Path

# ─── Configuration ─────────────────────────────────────────
BASE_DIR   = Path(__file__).parent.resolve()
DEVICE_CSV = BASE_DIR / "device_list.csv"
CRED_FILE  = BASE_DIR / "credentials.json"
LOG_DIR    = BASE_DIR / "Log"
FW_DIR     = BASE_DIR / "apc_hw05_aos720_sumx720_bootmon109" / "Bins"

DOWN_TIMEOUT, UP_TIMEOUT, POLL_INTERVAL = 300, 600, 5

FIRMWARE_FILES = {
    "AOS":  "apc_hw05_aos_720.bin",
    "SUMX": "apc_hw05_sumx_720.bin"
}
# ────────────────────────────────────────────────────────────

# ensure we have a place for logs
LOG_DIR.mkdir(exist_ok=True)

# load creds
try:
    creds = json.loads(CRED_FILE.read_text())
except Exception as e:
    print(f"ERROR: Cannot read {CRED_FILE.name}: {e}", file=sys.stderr)
    sys.exit(1)
for key in ("ftp_username", "ftp_password", "winscp_com"):
    if key not in creds:
        print(f"ERROR: Missing '{key}' in {CRED_FILE.name}", file=sys.stderr)
        sys.exit(1)

# pre‑flight firmware files exist?
missing = [t for t, fn in FIRMWARE_FILES.items() if not (FW_DIR / fn).is_file()]
if missing:
    print("ERROR: Missing firmware for:", ", ".join(missing), file=sys.stderr)
    sys.exit(1)

def is_online(ip, port=23, timeout=3):
    try:
        s = socket.create_connection((ip, port), timeout=timeout)
        s.close()
        return True
    except:
        return False

def wait_for_reboot(ip):
    print(f"…{ip} reboot: waiting offline", end="", flush=True)
    end = time.time() + DOWN_TIMEOUT
    while time.time() < end:
        if not is_online(ip):
            print(" ✓"); break
        time.sleep(POLL_INTERVAL)
    else:
        print(" ✗ timed out"); return False

    print(f"…{ip} reboot: waiting online", end="", flush=True)
    end = time.time() + UP_TIMEOUT
    while time.time() < end:
        if is_online(ip):
            print(" ✓"); return True
        time.sleep(POLL_INTERVAL)
    print(" ✗ timed out")
    return False

def upload_firmware(ip, tag):
    bin_path = FW_DIR / FIRMWARE_FILES[tag]
    log_file = LOG_DIR / f"{ip}_{tag}.txt"
    bat_file = BASE_DIR / ("aos_bat.bat" if tag=="AOS" else "sumx_bat.bat")

    print(f"[→] {tag} → {ip}", end="", flush=True)
    # call the .bat with all dynamic args
    args = [
        "cmd.exe", "/c", str(bat_file),
        ip,
        creds["ftp_username"],
        creds["ftp_password"],
        creds["winscp_com"],
        str(bin_path),
        str(log_file)
    ]
    result = subprocess.run(args, shell=False)
    if result.returncode == 0:
        print(" ✓"); return True
    else:
        print(" ✗"); return False

def main():
    try:
        devices = [r["IP"].strip() for r in csv.DictReader(open(DEVICE_CSV)) if r.get("IP")]
    except Exception as e:
        print(f"ERROR: Cannot read {DEVICE_CSV.name}: {e}", file=sys.stderr)
        sys.exit(1)

    for ip in devices:
        print(f"\n=== {ip} ===")
        if upload_firmware(ip, "AOS") and wait_for_reboot(ip):
            upload_firmware(ip, "SUMX")

if __name__ == "__main__":
    main()
