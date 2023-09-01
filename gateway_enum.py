# gateway_enum.py
import scapy.all as scapy

def get_gateways():
    arp_request = scapy.ARP(pdst="192.168.1.1/24")
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    gateways = []
    for element in answered_list:
        gateways.append(element[1].psrc)
    return gateways

if __name__ == "__main__":
    gateways = get_gateways()
    print("Discovered Gateways:")
    for gw in gateways:
        print(gw)
