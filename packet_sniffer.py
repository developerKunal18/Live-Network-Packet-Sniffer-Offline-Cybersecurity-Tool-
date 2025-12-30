from scapy.all import sniff, IP, TCP, UDP, ICMP
from collections import Counter

packet_counter = Counter()

def analyze(packet):
    if IP in packet:
        src = packet[IP].src
        dst = packet[IP].dst
        proto = "OTHER"

        if TCP in packet:
            proto = "TCP"
        elif UDP in packet:
            proto = "UDP"
        elif ICMP in packet:
            proto = "ICMP"

        packet_counter[src] += 1

        print(f"{src:15} → {dst:15} | {proto}")

        # Simple DDoS detection
        if packet_counter[src] > 100:
            print(f"🚨 Possible attack from {src}!")

print("🌐 Network Packet Sniffer")
print("Press CTRL+C to stop.\n")

sniff(prn=analyze, store=False)
