# 🌐 Live Network Packet Sniffer 

## 💡 Overview
The **Live Network Packet Sniffer** is a Python-based cybersecurity tool that monitors real-time network traffic and displays packet information directly in the terminal.

It captures live packets, extracts protocol details, tracks traffic sources, and detects suspicious behavior such as potential **DDoS attacks** — just like professional network monitoring systems.

---

## 🚀 Features

### 📡 Real-Time Packet Capture
- Monitors live network traffic
- Displays:
  - Source IP
  - Destination IP
  - Protocol (TCP / UDP / ICMP)

### 🧠 Protocol Detection
Automatically identifies:
- TCP
- UDP
- ICMP
- Other IP traffic

### 🚨 Suspicious Activity Detection
- Tracks how many packets come from each IP
- Flags possible DDoS-style behavior

### 🌐 Fully Offline
- No APIs
- No internet connection required
- Works directly with your network interface

---

## 🧠 Concepts & Technologies Used
- Python
- Scapy
- Network protocols (TCP, UDP, ICMP)
- Packet sniffing
- Cybersecurity monitoring
- Traffic analysis

---

## 📦 Installation

### Install dependency:
```bash
pip install scapy
