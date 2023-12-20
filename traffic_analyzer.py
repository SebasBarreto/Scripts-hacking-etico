# traffic_analyzer.py
from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

if __name__ == "__main__":
    interface = input("Enter the network interface to monitor (e.g., eth0): ")
    print(f"Starting packet capture on {interface}...")
    sniff(iface=interface, prn=packet_callback, store=0)
