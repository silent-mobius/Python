#!/usr/bin/env python3
# Python Network Programming Cookbook -- Chapter – 4
# This program is optimized for Python 3.6 or newer.
# It may run on any other version with/without modifications.

import urllib.request

BROWSER = 'Mozilla/5.0 (Windows NT 5.1; rv:20.0) Gecko/20100101Firefox/60.0'

URL = 'http://www.python.org'

def spoof_firefox():
	opener = urllib.request.build_opener()
	opener.addheaders = [('User-agent', BROWSER)]
	result = opener.open(URL)
	print("Response headers:")
	for header in result.headers.headers:
		print(header)




if __name__ == '__main__':
	spoof_firefox()
