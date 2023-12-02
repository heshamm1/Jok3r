
<img src="https://media.giphy.com/media/mvyByQFywcRaw/giphy.gif" alt="Funny GIF" width="1050" height="550">

<div align="center">

[![ProtonMail](https://img.shields.io/badge/ProtonMail-Email%20Me-red)](mailto:0xsh1vv@proton.me)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/heshamm1/)
[![Telegram](https://img.shields.io/badge/Telegram-Chat-blue)](https://t.me/sh1vv1)
[![Discord](https://img.shields.io/badge/Discord-Chat-green)](https://discord.gg/SxHbbCBP)

</div>

<div align="center">
  
# **Welcome to The Joker's World!!**
### Your favorite host discovery/scanner tool.

</div>

## Features

- **Host Discovery:** Quickly discover hosts in a specified subnet.
- **Port Scanning:** Perform stealth or aggressive port scans on specified hosts.
- **Technology Detection:** Identify technologies running on open ports.
- **Output Saving:** Save scan results and discovered hosts to a text file.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)
- [Sample Usage](#sample-usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

Ensure you have Python 3.x installed. Use `pip` to install the required dependencies:

```bash
git clone https://github.com/heshamm1/Jok3r && cd Jok3r
```
```bash
pip install -r requirements.txt
```
> or 
```bash
chmod +x setup.sh && ./setup.sh
```
```bash
python jok3r.py -h
```

## Usage
### Host Discovery:
```bash
python3 jok3r.py -s 192.168.1.0 -m 24
```
### Port Scanning:
```bash
python3 jok3r.py -i 192.168.1.3 -Ps -a 
```
### Output Saving:
```bash
python3 jok3r.py -s 192.168.1.0 -m 24 -So output.txt
```

## Options
*  `-s SUBNET`:    Subnet you want to discover, e.g., 192.168.1.0
*  `-m MASK`:      Subnet Mask you want to discover, e.g., 24
*  `-i IP`:        Specify target IP for port scanning
*  `-So FILE`:     Save output to a text file
*  `-Ps`:          Perform port scan
*  `-a`:           Scan all 65535 ports
*  `-h`:           Show help message

## Sample Usage
```bash
python3 jok3r.py -s 192.168.1.0 -m 24 -i 192.168.1.2 -Ps
```

## Contributing
Contributions are welcome! If you have suggestions, bug reports, or want to contribute code, feel free to open an issue or submit a pull request.

Please make sure to update tests as appropriate.

## License 
This project is licensed under the MIT License.

## Get in Touch

