# Network Scanner (CLI)

ARP-based network scanner built using Scapy.


## Features
- Discovers devices on local subnet
- MAC address vendor identification
- Flags unknown devices
- CLI output for SOC-style workflows

## Usage
```bash
sudo python3 cli_scanner.py

## Example output
=== Network Device Scanner ===

Using interface: eth0
Scanning network: 192.168.1.10/24

Discovering devices...

Scan complete!

Connected Network Devices
----------------------------------------------------------------------
IP Address      MAC Address        Manufacturer         Status
----------------------------------------------------------------------
192.168.1.5     aa:bb:cc:dd:ee:01  Intel Corporate      KNOWN
192.168.1.1     aa:bb:cc:dd:ee:02  Commscope            KNOWN
192.168.1.20    aa:bb:cc:dd:ee:03  Unknown              UNKNOWN
192.168.1.30    aa:bb:cc:dd:ee:04  Unknown              UNKNOWN

Press Enter to return to portfolio...
