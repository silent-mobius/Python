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
    os.mkdir('./.arp_watcher')
    arp_watcher_db_file = "./.arp_watcher/arp_watcher.db"


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


