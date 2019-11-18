#!/usr/bin/env python3

#######################################################################################
# created by :www.thepythoncode.com
# edited: pushtakio
# purpose: scany local network for clients 
# date: 18/11/2019
# version: 1.0.0
########################################################################################

### Lib import
import sys
from scapy.all import ARP, Ether, srp

## Variables :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

clients = []
try:
    target_ip = str(sys.argv[1])

except IndexError:
    target_ip = input('Please provide the target ip: ')

# IP Address for the destination
# create ARP packet
arp = ARP(pdst=target_ip)
# create the Ether broadcast packet
# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
# stack them
packet = ether/arp

result = srp(packet, timeout=3, verbose=1)[0]

# a list of clients, we will fill this in the upcoming loop

for sent, received in result:
    # for each response, append ip and mac address to `clients` list
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

# print clients
print("Available devices in the network:")
print("IP" + " "*18+"MAC")
for client in clients:
    print(f"{client['ip']:16}    {client['mac']}")