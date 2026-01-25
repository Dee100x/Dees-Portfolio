from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    answered, _ = srp(packet, timeout=2, verbose=False)

    devices = []
    for _, received in answered:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc.lower()
        })

    return devices
