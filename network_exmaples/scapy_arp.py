#!/usr/bin/env python3

#######################################################################################
# created by :www.thepythoncode.com
# edited: pushtakio
# purpose: scany local network for clients 
# date: 18/11/2019
# version: 1.0.0
########################################################################################

### Lib import

import os
import sys
import time
import platform

try:
    import netifaces
    from scapy.all import ARP, Ether, srp
except ModuleNotFoundError:
    print('The libs are missing: trying to install ')
    time.sleep(1)
    os.system('pip3 install netifaces')
    os.system('pip3 install scapy')
    print('try running the script again.')
    sys.exit(1)

## Variables :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

clients = []
try:
    target_ip = str(sys.argv[1])

except IndexError:
    target_ip = input('Please provide the target ip: ')


## Functions /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

def clean():
    if platform.platform() == 'Linux':
        os.system('clear')
    
    if platform.platform() == 'Windows':
        os.system('cls')
    



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