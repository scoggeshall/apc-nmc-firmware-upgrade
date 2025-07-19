# APC Network Management Card Firmware Upgrade

This project automates firmware upgrades for APC Network Management Cards using Python and WinSCP. It uploads AOS and SUMX binaries, monitors reboots, and saves logs.

## Directory Structure

```
C:\Temp\Script
├── apc_hw05_aos720_sumx720_bootmon109\   # Firmware directory (not in repo)
│   └── Bins\
├── Log\                                  # Upload logs
├── aos_bat.bat                           # Upload AOS via WinSCP
├── sumx_bat.bat                          # Upload SUMX via WinSCP
├── credentials.json                      # FTP/Winscp config (ignored)
├── credentials.example.json              # Public-safe config example
├── device_list.csv                       # List of device IPs
├── update_firmware.py                    # Main script
├── README.md                             # Documentation
└── .gitignore                            # Excludes sensitive files
```

## Setup

### Requirements

- Python 3.x
- WinSCP installed with access to `winscp.com`

### Configure credentials

Create `credentials.json`:

```json
{
  "ftp_username": "username",
  "ftp_password": "password",
  "winscp_com": "C:\\Program Files (x86)\\WinSCP\\winscp.com"
}
```

This file is excluded from GitHub. An example is included as `credentials.example.json`.

### Add devices

Add IP addresses to `device_list.csv`:

```csv
IP
192.168.1.100
192.168.1.101
```

## Usage

From PowerShell or CMD:

```
cd C:\Temp\Script
python update_firmware.py
```

The script will:

1. Upload AOS firmware using `aos_bat.bat`
2. Wait for the device to reboot
3. Upload SUMX firmware using `sumx_bat.bat`
4. Save logs to the `Log\` directory

## Batch File Parameters

Both batch files are called by Python and accept:

```
<ip> <ftp_user> <ftp_pass> <winscp_com_path> <firmware_file_path> <log_file_path>
```

## Tested Environment

- Windows 11
- Python 3.11+
- WinSCP 6.x
- APC NMC AP9630 / AP9631 (v7.2.0 firmware)

## License

MIT License
