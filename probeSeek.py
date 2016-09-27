#!/usr/bin/env python

###Lib import ////////////////////////////////////////////////////////////////////
import os,sys
from netaddr import *
import argparse
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from subprocess import *
import datetime
import time


###Vars ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# set date-time parameters                                                          
now = datetime.date.today()                 
d=now.strftime("%d, %b %Y")
tf=time.strftime(" %H:%M")
t=time.strftime(" %H:%M:%S")

db = []                          
uni = 0
mach = []
manu =[]
maco=[]


###Funcs :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

call(["clear"])

def pktHandle(pkt):
	global uni
	if pkt.haslayer(Dot11ProbeReq):
		if pkt.haslayer(Dot11Elt):
			if pkt.ID == 0:
				 if pkt.addr2 not in db:
					 db.append(pkt.addr2)
					 print "MAC : %s | Name : %s" %(pkt.addr2, pkt.info)

def autoIfStart(iface):
    if os.system('systemctl status NetworkManager.service') != 0:
        os.system('systemctl stop NetworkManager.service')
        os.sys


####
#Main - _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _
####
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='PyProbe Help')
    parser.add_argument('interface', action="store", help="specify interface (ex. wlan0mon)", default=False)
    parser.add_argument("-l","--log", dest="log",action="store_true", help="print log file")
    args = parser.parse_args()

    if args.log:
        L = open("ProbeLog"+str(now)+str(tf)+".txt","w")    
        sniff(iface=args.interface,prn=pktHandle)                    
        print ("\n")
        print "Unique MACs: ",uni
        L.write ("\nUnique MACs: "+str(uni))
        L.write ("\nScan performed on: "+str(d)+" at"+str(t))  
        L.close()                                                 
        print "Log successfully written. Exiting!"
    else:
        sniff(iface=args.interface,prn=pktHandle, store=0)
        print "\nSuccessfully Exited! No log file written."




