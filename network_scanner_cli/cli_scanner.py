import os
import json
import socket
from scanner import scan_network
from mac_lookup import get_manufacturer

def clear():
    os.system("clear")

def banner():
    print("=== Network Device Scanner ===\n")

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def load_known_devices():
    with open("known_devices.json", encoding="utf-8-sig") as f:
        return json.load(f)

def main():
    clear()
    banner()

    interface = "eth0"
    local_ip = get_local_ip()
    ip_range = "192.168.0.0/24"

    print(f"Using interface: {interface}")
    print(f"Scanning network: {local_ip}/24\n")
    print("Discovering devices...\n")

    known_devices = load_known_devices()
    devices = scan_network(ip_range)

    print("Scan complete!\n")

    print("Connected Network Devices")
    print("-" * 70)
    print(f"{'IP Address':<15} {'MAC Address':<18} {'Manufacturer':<20} Status")
    print("-" * 70)

    for d in devices:
        manufacturer = get_manufacturer(d["mac"])
        status = "KNOWN" if d["mac"] in known_devices else "UNKNOWN"
        print(f"{d['ip']:<15} {d['mac']:<18} {manufacturer:<20} {status}")

    input("\nPress Enter to return to portfolio...")

if __name__ == "__main__":
    main()
