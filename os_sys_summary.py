#!/usr/bin/env python3
########################################################################
#
#
#
#
########################################################################

import os
import sys
import time
import subprocess
import platform
#import psutils


########################################################################
try:
	import netifaces
except:
	print("No NetIfaces module found")
	print("Trying to install netifaces")
	#pip3 install netifaces

########################################################################

##vars ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#misc
line="=================================================================="
#messages
error_msg = "Something went wrong - try running in debug mode"
note_msg  = "Notification "
start_msg = "Start OF Script"
end_msg   = "End Of Script"
hw_msg    = "List Of HardWare"
sys_msg   = "List Of System Parameters"
users_msg = "List Of System Users"
service_msg = "List Of Services"
app_msg   = "List Of Installed Apps"
net_msg   = "List Of Interfaces With Attributes"
stor_msg  = "List Of Mount Points"
mod_msg   = "List of Kernel Modules"
permission_msg = "Please Get Root Access"


#system vars
arch = [platform.processor(),platform.architecture()]
distro = platform.dist()
host_name = platform.node()
uname = platform.platform()
sys = platform.system()
#net_ifaces = psutils.net_if_addrs()
md_ver = os.getenv('MD_Ver')
md_prod = os.getenv('MD_Prod')
path = os.getenv('PATH')
#misc vars 
sleep_time=2


##Funcs /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

def get_inet_info():
	data=[]
	try:
		import netifaces
		for inet in netifaces.interfaces():
			data.append(netifaces.ifaddresses(inet))
		return data
	except ModuleNotFoundError:
		print("no module found --> trying to by pass:")
		inet_list = subprocess.Popen(['ip','addr','show'],stdout = subprocess.PIPE,stderr = subprocess.PIPE)
		inet_list_filter = subprocess.Popen(['grep','inet'],stdin = inet_list.stdout ,stdout = subprocess.PIPE)
		data = inet_list_filter.communicate()
		return data


def write_to_csv():
	open

###
#Main - _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _

if __name__ == "__main__":
	if os.getuid() !=  0:
		print(permission_msg)
	else:
		print(line)
		print(start_msg)
		print(line)
		time.sleep(sleep_time)
		
		
		print(line)
		print(sys_msg)
		print(line)


		print(line)
		print(net_msg)
		print(line)
		net=get_inet_info()
		print(net)

		print(line)
		print()
		print(line)
