\# APC Network Management Card Firmware Upgrade



This repository contains scripts and batch files to automate upgrading firmware on APC Network Management Cards (NMCs). It supports AOS and SUMX firmware upgrades, handling the upload, reboot detection, and logging.

\# APC Network Management Card Firmware Upgrade



This repository contains scripts and batch files to automate upgrading firmware on APC Network Management Cards (NMCs). It supports AOS and SUMX firmware upgrades, handling the upload, reboot detection, and logging.



---



\## 📂 Directory Structure



```text

C:\\Temp\\Script

├── apc\_hw05\_aos720\_sumx720\_bootmon109/    # Firmware bins folder

│   └── Bins/

│       ├── apc\_hw05\_aos\_720.bin

│       ├── apc\_hw05\_bootmon\_109.bin

│       └── apc\_hw05\_sumx\_720.bin

├── Log/                                     # Upload logs (auto-created)

├── credentials.json                         # FTP \& WinSCP settings

├── device\_list.csv                          # List of target IPs

├── update\_firmware.py                       # Main Python orchestrator

├── aos\_bat.bat                              # WinSCP script for AOS

└── sumx\_bat.bat                             # WinSCP script for SUMX

```



---



\## 🔧 Prerequisites



1\. \*\*Operating System:\*\* Windows 10 or higher

2\. \*\*Python:\*\* Version 3.x installed and on `%PATH%`

3\. \*\*WinSCP:\*\* WinSCP CLI (`winscp.com`) installed (\[http://winscp.net](http://winscp.net)) and binary path available



---



\## ⚙️ Configuration



\### 1. `credentials.json`



Store your FTP credentials and WinSCP path here:



```json

{

&nbsp; "ftp\_username": "YOUR\_FTP\_USERNAME",

&nbsp; "ftp\_password": "YOUR\_FTP\_PASSWORD",

&nbsp; "winscp\_com": "C:/Program Files/WinSCP/winscp.com"

}

```



\### 2. `device\_list.csv`



A simple CSV listing one IP per line:



```csv

IP

192.168.1.100

192.168.1.101

\# ...

```



---



\## 🚀 Usage



1\. Open PowerShell or Command Prompt:



&nbsp;  ```powershell

&nbsp;  cd C:\\Temp\\Script

&nbsp;  ```

2\. Run the upgrade script:



&nbsp;  ```powershell

&nbsp;  python update\_firmware.py

&nbsp;  ```



The script will:



\* Read each IP from `device\_list.csv`.

\* Call `aos\_bat.bat` to upload the AOS firmware.

\* Wait for the card to reboot (offline → online).

\* Call `sumx\_bat.bat` to upload the SUMX firmware.

\* Write WinSCP output logs to `Log/{IP}\_{TAG}.txt`.



---



\## 📄 Batch Files



Both batch files accept the same parameters:



```text

Usage: <batch\_file> <ip> <ftp\_user> <ftp\_pass> <winscp\_com> <firmware\_file> <log\_file>

```



\* \*\*`aos\_bat.bat`\*\* — Uploads the AOS firmware image.

\* \*\*`sumx\_bat.bat`\*\* — Uploads the SUMX firmware image.



They execute WinSCP in scripting mode, using `option batch abort` and `option confirm off`.



---



\## 📜 Logging



All WinSCP session output is captured in the `Log` directory. Files are named:



```

{IP}\_AOS.txt

{IP}\_SUMX.txt

```



---



\## ⚖️ License



This project is released under the MIT License. See `LICENSE` for details.



---



\## 📂 Directory Structure



```text

C:\\Temp\\Script

├── apc\_hw05\_aos720\_sumx720\_bootmon109/    # Firmware bins folder

│   └── Bins/

│       ├── apc\_hw05\_aos\_720.bin

│       ├── apc\_hw05\_bootmon\_109.bin

│       └── apc\_hw05\_sumx\_720.bin

├── Log/                                     # Upload logs (auto-created)

├── credentials.json                         # FTP \& WinSCP settings

├── device\_list.csv                          # List of target IPs

├── update\_firmware.py                       # Main Python orchestrator

├── aos\_bat.bat                              # WinSCP script for AOS

└── sumx\_bat.bat                             # WinSCP script for SUMX

```



---



\## 🔧 Prerequisites



1\. \*\*Operating System:\*\* Windows 10 or higher

2\. \*\*Python:\*\* Version 3.x installed and on `%PATH%`

3\. \*\*WinSCP:\*\* WinSCP CLI (`winscp.com`) installed (\[http://winscp.net](http://winscp.net)) and binary path available



---



\## ⚙️ Configuration



\### 1. `credentials.json`



Store your FTP credentials and WinSCP path here:



```json

{

&nbsp; "ftp\_username": "YOUR\_FTP\_USERNAME",

&nbsp; "ftp\_password": "YOUR\_FTP\_PASSWORD",

&nbsp; "winscp\_com": "C:/Program Files/WinSCP/winscp.com"

}

```



\### 2. `device\_list.csv`



A simple CSV listing one IP per line:



```csv

IP

192.168.1.100

192.168.1.101

\# ...

```



---



\## 🚀 Usage



1\. Open PowerShell or Command Prompt:



&nbsp;  ```powershell

&nbsp;  cd C:\\Temp\\Script

&nbsp;  ```

2\. Run the upgrade script:



&nbsp;  ```powershell

&nbsp;  python update\_firmware.py

&nbsp;  ```



The script will:



\* Read each IP from `device\_list.csv`.

\* Call `aos\_bat.bat` to upload the AOS firmware.

\* Wait for the card to reboot (offline → online).

\* Call `sumx\_bat.bat` to upload the SUMX firmware.

\* Write WinSCP output logs to `Log/{IP}\_{TAG}.txt`.



---



\## 📄 Batch Files



Both batch files accept the same parameters:



```text

Usage: <batch\_file> <ip> <ftp\_user> <ftp\_pass> <winscp\_com> <firmware\_file> <log\_file>

```



\* \*\*`aos\_bat.bat`\*\* — Uploads the AOS firmware image.

\* \*\*`sumx\_bat.bat`\*\* — Uploads the SUMX firmware image.



They execute WinSCP in scripting mode, using `option batch abort` and `option confirm off`.



---



\## 📜 Logging



All WinSCP session output is captured in the `Log` directory. Files are named:



```

{IP}\_AOS.txt

{IP}\_SUMX.txt

```



---



\## ⚖️ License



This project is released under the MIT License. See `LICENSE` for details.



