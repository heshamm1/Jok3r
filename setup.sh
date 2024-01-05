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
    sleep 2
    echo ""
    echo "[+] Installing python3..."
    sleep 3
    echo ""
    sudo apt-get update
    sudo apt-get install -y python3
fi

if ! command -v pip &> /dev/null; then
    echo "[!] Error: pip is not installed."
    sleep 1
    echo ""
    echo "[+] Installing Pip3..."
    sleep 2
    echo ""
    sudo apt-get update
    sudo apt-get install -y python3-pip 
fi

echo "[+] Updating system and installing nmap..."
echo ""
sleep 3
sudo apt-get update
sudo apt-get install -y nmap

echo "[+] Installing Findomain, Subfinder, AssetFinder..."
GOlang() {
	printf "                                \r"
	sys=$(uname -m)
	#LATEST=$(curl -s 'https://go.dev/VERSION?m=text') # https://golang.org/dl/$LATEST.linux-amd64.tar.gz
	[ $sys == "x86_64" ] && wget https://go.dev/dl/go1.17.13.linux-amd64.tar.gz -O golang.tar.gz &>/dev/null || wget https://golang.org/dl/go1.17.13.linux-386.tar.gz -O golang.tar.gz &>/dev/null
	sudo tar -C /usr/local -xzf golang.tar.gz
	export GOROOT=/usr/local/go
	export GOPATH=$HOME/go
	export PATH=$PATH:$GOROOT/bin:$GOPATH/bin
	echo "[!] Add The Following Lines To Your ~/.${SHELL##*/}rc file:"
 	echo 'export GOROOT=/usr/local/go'
  	echo 'export GOPATH=$HOME/go'
   	echo 'export PATH=$PATH:$GOROOT/bin:$GOPATH/bin'
	
	printf "[+] Golang Installed !.\n"
	
curl -LO https://github.com/findomain/findomain/releases/latest/download/findomain-linux-i386.zip
unzip findomain-linux-i386.zip
chmod +x findomain
sudo mv findomain /usr/bin/findomain
sudo apt install subfinder
go install github.com/tomnomnom/assetfinder@latest &>/dev/null

echo "[+] Installing Python dependencies..."
echo ""
sleep 3
pip install -r requirements.txt

chmod +x jok3r.py
sleep 5
echo "" 
echo ""
echo "[+] Setup completed successfully. You can now run the tool using ./jok3r.py -h or python3 jok3r.py -h "

