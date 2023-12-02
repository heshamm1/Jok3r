#!/bin/bash

# Install necessary dependencies
sudo apt-get update
sudo apt-get install -y nmap

# Set up a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate

# Install required Python packages
pip install -r requirements.txt

# Provide executable permissions to the script
chmod +x jok3r.py

echo "Setup completed successfully. You can now run the tool using ./jok3r.py."
