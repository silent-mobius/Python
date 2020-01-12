#!/usr/bin/env python3

######################################################
# created by : Pushtakio
# purpose : arp watcher tool
# date :
# version: 1.0.0
#######################################################
import os
import sys
from signal import signal
from signal import SIGINT

try:
    from scapy.all import sniff
    from scapy.all import ARP

except ModuleNotFoundError:
    print("scapy library missing")
    sys.exit()

ip_mac = {}

if os.path.exists('/var/cache'):
    arp_watcher_db_file = "/var/cache/arp_watcher.db"
else:
    os.mkdir('.arp_watcher')
    arp_watcher_db_file = ".arp_watcher/arp_watcher.db"


def sig_int_handler(signum,frame):
    try:
        f = open(arp_watcher_db_file,'w')

        for (ip, mac) in ip_mac.items():
            f.write(ip, mac, "\n")
        
        f.close()
        print('[+]Done')
    except IOError:
        print("Can Not Write to file: ",arp_watcher_db_file)
        sys.exit(1)


def watch_arp(pkt):
    if pkt[ARP].op == 2:
        print(pkt[ARP].hwsrc," ",pkt[ARP].psrc)

        if ip_mac.get(pkt[ARP].psrc) == None:
            print("[+] New Device:",pkt[ARP].hwsrc, pkt[ARP].psrc)
            ip_mac[pkt[ARP].psrc] = pkt[ARP].hwsrc

        elif ip_mac.get(pkt[ARP].psrc) and ip_mac[pkt[ARP].psrc] != pkt[ARP].hwsrc:
            print(pkt[ARP].hwsrc," has new ip:",pkt[ARP].psrc,"(old :",ip_mac[pkt[ARP].psrc],")")

            ip_mac[pkt[ARP].psrc] = pkt[ARP].hwsrc

signal(SIGINT,sig_int_handler)

if len(sys.argv) < 2 :
    print("Not enough paramenters are given: ")
    print(sys.argv[0], " <iface>")
    sys.exit(0)

try:
    f = open(arp_watcher_db_file, "r")
except IOError:
    print("Cannot read the ",arp_watcher_db_file)
    sys.exit(1)

for line in f:
    line.chomp()
    (ip,mac) = line.split(" ")
    ip_mac[ip] = mac


sniff(prn = watch_arp, filter="arp", iface= sys.argv[1], store = 0)