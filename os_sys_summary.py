#!/usr/bin/env python
########################################################################
#created by : br0k3ngl255
#date		: 12/12/2018
#purpose	: get system info from all possible varieties of linux
#version	: 0.2.38
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
	os.system('pip3 install netifaces')

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
	data={}
	try:
		import netifaces
		for inet in netifaces.interfaces():
			data[inet]=netifaces.ifaddresses(inet)
			#print(type(data))
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
		print(arch)
		print(distro)
		print(uname)
		print(sys)
		print(path)


		print(line)
		print(net_msg)
		print(line)
		inets=get_inet_info()
		#print(type(inets))
		for inet,inet_val in inets.items():
			#print(type(inet))
			#print(inet,inet_val)
			for i in inet_val.values():
			#	print(i)
			#	print(type(i))
				for j in i:
					#print(type(j))
					print(inet,j.get('addr'))

		print(line)
		print()
		print(line)
