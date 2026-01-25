# Dee's Cybersecurity Portfolio (CLI)

This repository contains a collection of command-line cybersecurity tools built in Python.
Each tool is modular and can be executed independently or launched via a central CLI menu.

## Projects Included

### 🔍 Network Scanner (CLI)
- ARP-based network discovery using Scapy
- Identifies connected devices
- Performs MAC address manufacturer lookups (OUI)
- Flags unknown devices
- Designed for internal network visibility

### 🔐 Password Policy Analyser (CLI)
- Audits organisational password policies
- Benchmarked against NIST SP 800-63B guidelines
- Identifies weak or outdated requirements
- Provides remediation recommendations

## Technologies Used
- Python 3
- Scapy
- Linux
- CLI-based UX design

## How to Run

```bash
git clone https://github.com/YOUR_USERNAME/dees_portfolio.git
cd dees_portfolio
python3 main_menu.py
