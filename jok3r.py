#!/usr/bin/env python3

import ipaddress
import socket
import random
import sys
import re
import threading
import subprocess
import os
import time

def generate_banner():
    colors = [
        "\033[91m", "\033[92m", "\033[94m",
        "\033[93m",
        "\033[95m", "\033[96m", "\033[31m"   
    ]
    banner = """
     ██╗ ██████╗ ██╗  ██╗██████╗ ██████╗ 
     ██║██╔═══██╗██║ ██╔╝╚════██╗██╔══██╗
     ██║██║   ██║█████╔╝  █████╔╝██████╔╝
██   ██║██║   ██║██╔═██╗  ╚═══██╗██╔══██╗
╚█████╔╝╚██████╔╝██║  ██╗██████╔╝██║  ██║
 ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ By Sh1vV..
             Never Forget GAZA!
               +17000 Martyr 

"""
    return random.choice(colors) + banner + "\033[0m"

# New function to read targets from a file
def read_targets_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            targets = file.read().splitlines()
        return targets
    except Exception as e:
        print_colored(f"[-] An error occurred while reading targets from file: {e}", "\033[91m")
        return []

def discover_hosts(targets):
    discovered_hosts = []

    def worker(ip):
        ip_str = str(ip)
        try:
            with socket.create_connection((ip_str, 80), timeout=1) as sock:
                discovered_hosts.append(ip_str)
        except (socket.error, socket.timeout) as e:
            pass
        except Exception as e:
            print_colored(f"[-] An error occurred for {ip_str}: {e}", "\033[91m")

    threads = []
    for target in targets:
        for ip in ipaddress.IPv4Network(f"{target}", strict=False).hosts():
            thread = threading.Thread(target=worker, args=(ip,))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    return discovered_hosts

def nmap_scan(target_host, all_ports=False):
    try:
        temp_file_name = "nmap_output.txt"
        print_colored("[+] Scanning in progress. Please wait...", "\033[94m")
        time.sleep(2)
        print_colored("[+] This may take a while depending on the target and selected options.", "\033[94m")
        time.sleep(2)
        print_colored("[+] Scanning in progress. Please wait...", "\033[94m")
        command = f"nmap -A {'-p1-65535' if all_ports else '-p1-1024'} {target_host} > {temp_file_name}"
        subprocess.run(command, shell=True)

        with open(temp_file_name, "rb") as temp_file:
            output = temp_file.read()

        open_ports, port_services = parse_nmap_output(output)

        print_colored("[?] Nmap scan completed. Do you want to delete the temporary file? (y/n)", "\033[94m")
        user_input = input().lower()
        if user_input == "n":
            new_file_name = f"nmap_output_{target_host.replace('.', '_')}.txt"
            os.rename(temp_file_name, new_file_name)
            print_colored(f"[+] Results saved to {new_file_name}", "\033[92m")
        elif user_input == "y":
            os.remove(temp_file_name)
            print_colored("[+] Temporary file deleted.", "\033[92m")
        else:
            print_colored("[-] Invalid input. Temporary file kept.", "\033[91m")

        return open_ports, port_services
    except Exception as e:
        print_colored(f"[-] An error occurred during nmap scan: {e}", "\033[91m")
        return [], {}

def parse_nmap_output(nmap_output):
    open_ports = []
    port_services = {}

    lines = nmap_output.decode("utf-8").splitlines()
    for line in lines:
        if "open" in line.lower() and "tcp" in line.lower():
            match = re.match(r"(\d+)/tcp\s+open\s+(\w+)(?:\s+(\w+))?", line)
            if match:
                port = match.group(1)
                service = match.group(2)
                version = match.group(3) if match.group(3) else "Unknown Version"
                open_ports.append(port)
                port_services[port] = {"service": service, "version": version}

    return open_ports, port_services

def print_colored(message, color):
    print(f"{color}{message}\033[0m")

def display_help():
    print(generate_banner())
    print_colored("Welcome to The Jok3r World!", "\033[94m")
    print("")
    print("Usage:")
    print("  -s SUBNET    Subnet, e.g., 192.168.1.0")
    print("  -m MASK      Subnet Mask, e.g., 24")
    print("  -i IP        Specify target IP for port scanning")
    print("  -f FILE      Specify a file with a list of targets (e.g., IPs.txt)")
    print("  -So FILE     Save output to a text file")
    print("  -Ps          Perform port scan")
    print("  -a           Scan all 65535 ports")
    print("  -h           Show help message")
    print("\nExample:")
    print("     python3 jok3r.py -s 192.168.1.0 -m 24 -i 192.168.1.2 -Ps")
    print("     python3 jok3r.py -f IPs.txt -Ps")
    print("")
    sys.exit()

def validate_input(subnet, subnet_mask):
    try:
        ipaddress.IPv4Network(f"{subnet}/{subnet_mask}", strict=False)
        return True
    except ValueError:
        return False

def save_to_file(output, file_name):
    with open(file_name, "w") as file:
        file.write(output)

def main():
    try:
        if len(sys.argv) < 2:
            display_help()

        subnet = None
        subnet_mask = None
        target_host = None
        target_hosts = None  # New variable for the list of targets
        save_output_file = None
        perform_port_scan = False
        scan_all_ports = False

        for i in range(1, len(sys.argv), 2):
            if sys.argv[i] == "-f" and i + 1 < len(sys.argv):
                target_file = sys.argv[i + 1]
                target_hosts = read_targets_from_file(target_file)
            elif sys.argv[i] == "-s" and i + 1 < len(sys.argv):
                subnet = sys.argv[i + 1]
            elif sys.argv[i] == "-m" and i + 1 < len(sys.argv):  # Corrected this line
                subnet_mask = sys.argv[i + 1]
            elif sys.argv[i] == "-i" and i + 1 < len(sys.argv):
                target_host = sys.argv[i + 1]
            elif sys.argv[i] == "-So" and i + 1 < len(sys.argv):
                save_output_file = sys.argv[i + 1]
            elif sys.argv[i] == "-Ps":
                perform_port_scan = True
            elif sys.argv[i] == "-a":
                scan_all_ports = True
            elif sys.argv[i] == "-h":
                display_help()

        if target_hosts:
            discovered_hosts = discover_hosts(target_hosts)
            if discovered_hosts:
                output = f"[+] Hosts discovered: {', '.join(discovered_hosts)}"
                print_colored(output, "\033[92m")  # Green
                if save_output_file:
                    save_to_file(output, save_output_file)
            else:
                output = "[-] No hosts found on the specified subnet."
                print_colored(output, "\033[91m")  # Red
                if save_output_file:
                    save_to_file(output, save_output_file)

        if perform_port_scan:
            if target_host is None:
                print_colored("[-] Please specify a target IP for port scanning using the -i option.", "\033[91m")  # Red
                display_help()

            open_ports, port_services = nmap_scan(target_host, all_ports=scan_all_ports)

            if open_ports:
                output = f"[+] Open ports on {target_host}: {', '.join(map(str, open_ports))}"
                print_colored(output, "\033[92m")  # Green

                for port in open_ports:
                    service_info = port_services.get(port, {"service": "Unknown Service", "version": "Unknown Version"})
                    service = service_info["service"]
                    version = service_info["version"]
                    print_colored(f"[+] Port {port} service: {service}, version: {version}", "\033[94m")  # Blue

                if save_output_file:
                    save_to_file(output, save_output_file)
            else:
                output = f"[-] No open ports found on {target_host}."
                print_colored(output, "\033[91m")  # Red
                if save_output_file:
                    save_to_file(output, save_output_file)

        if subnet is not None and subnet_mask is not None:
            discovered_hosts = discover_hosts(subnet, subnet_mask)
            if discovered_hosts:
                output = f"[+] Hosts discovered: {', '.join(discovered_hosts)}"
                print_colored(output, "\033[92m")  # Green
                if save_output_file:
                    save_to_file(output, save_output_file)
            else:
                output = "[-] No hosts found on the specified subnet."
                print_colored(output, "\033[91m")  # Red
                if save_output_file:
                    save_to_file(output, save_output_file)

    except KeyboardInterrupt:
        print_colored("[:)] Good Bye", "\033[0m")  # White
        sys.exit()

if __name__ == "__main__":
    main()
