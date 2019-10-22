#!/usr/bin/env python3

# Python Network Programming Cookbook -- Chapter - 4
# This program is optimized for Python 3.6 or above.
# It may run on any other version with/without modifications.
import os
import sys
import argparse

try:
	import http
except Exception:
	print('No Module found: trying to install --> ')
	os.system('pip3 install http')


REMOTE_SERVER_HOST = 'www.python.org'
REMOTE_SERVER_PATH = '/'


class HTTPClient:
	def __init__(self, host):
		self.host = host
	def fetch(self, path):
		ht = http.HTTP(self.host)
		# Prepare header
		ht.putrequest("GET", path)
		ht.putheader("User-Agent", __file__)
		ht.putheader("Host", self.host)
		ht.putheader("Accept", "*/*")
		ht.endheaders()

		try:
			errcode, errmsg, headers = ht.getreply()
		except Exception:
			print(f'Client failed error code: {errcode} message:{errmsg} headers:{headers}')
		else:
			print(f"Got homepage from {self.host}")
			file = ht.getfile()
			return file.read()	


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='HTTP Client Example')
	parser.add_argument('--host', action="store", dest="host", default=REMOTE_SERVER_HOST)
	parser.add_argument('--path', action="store", dest="path", default=REMOTE_SERVER_PATH)
	given_args = parser.parse_args()
	host, path = given_args.host, given_args.path
	client = HTTPClient(host)
	print(client.fetch(path))
