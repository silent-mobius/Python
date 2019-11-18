#!/usr/bin/env python3
###########################################
#created by: Pushtakio
#purpose: send an ICMP echo request packet and display the completely dissected return packet
#date: 18/11/2019
#version: 1.0.0
###########################################

import os
import sys
from scapy.all import sr1,IP,ICMP


p = sr1(IP(dst=sys.argv[1])/ICMP())

if p:
    p.show()