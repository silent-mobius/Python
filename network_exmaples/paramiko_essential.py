#!/usr/bin/env python3


import os
import sys
import time

try:
	import paramiko

except Exception as e:
	print('lib missing: try installing it manually')
	sys.exit(1)
	
def ssh_connect(dest='', port=22,username='',passwd=''):
	if dest == '':
		dest = input('destination missing. Please insert ip: ') 
	if username == '':
		username = input('connection input missing: username:')	
	if passwd == '':
		passwd = input('password missing : provide password: ')
	if port == 22:
		ans = input('port is 22: change ? y/N')
		if ans == 'y' or ans == 'Y':
			port = int(input('Please provide port: '))
		else:
			port =22
	try:
		ssh =  paramiko.SSHClient()
		ssh.load_system_host_keys()
		ssh.connect(dest,username=username,password=passwd, port=port)
	except SSHException:
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	#except Exception as e:
	#	print('error',e,'occured')
	#	sys.exit(1)

	stdin,stdout,stderr = ssh.exec_command('ls -la')
	output=stdout.readlines()
	return output
	
if __name__ == "__main__":
	var=ssh_connect()
	print(var)
