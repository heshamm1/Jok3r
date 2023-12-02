#!/bin/bash

# Banner
banner="
     ██╗ ██████╗ ██╗  ██╗██████╗ ██████╗
     ██║██╔═══██╗██║ ██╔╝╚════██╗██╔══██╗
     ██║██║   ██║█████╔╝  █████╔╝██████╔╝
██   ██║██║   ██║██╔═██╗  ╚═══██╗██╔══██╗
╚█████╔╝╚██████╔╝██║  ██╗██████╔╝██║  ██║
 ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ By Sh1vV..
"

echo -e "\033[92m$banner\033[0m"

if ! command -v python3 &> /dev/null; then
    echo "[!] Error: Python3 is not installed."
    sleep 1
    echo "[+] Installing python3..."
    sleep 2
    sudo apt-get update
    sudo apt-get install -y python3
fi

if ! command -v pip &> /dev/null; then
    echo "[!] Error: pip is not installed."
    sleep 1
    echo "[+] Installing Pip3..."
    sleep 2
    sudo apt-get update
    sudo apt-get install -y python3-pip 
fi

echo "[+] Updating system and installing nmap..."
sleep 3
sudo apt-get update
sudo apt-get install -y nmap


echo "[+] Installing Python dependencies..."
sleep 3
pip install -r requirements.txt

chmod +x jok3r.py
sleep 3
echo "[+] Setup completed successfully. You can now run the tool using ./jok3r.py -h or python3 jok3r.py -h "


