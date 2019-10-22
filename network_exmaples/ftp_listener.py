#!/usr/bin/env python3
# Python Network Programming Cookbook -- Chapter - 5
# This program is optimized for Python 3.6 or newer.
# It may run on any other version with/without modifications.

import ftplib

FTP_SERVER_URL = 'test.rebex.net'

def test_ftp_connection(path, username, email): #Open ftp connection
	print(f'connecting to {path}')
	ftp = ftplib.FTP(path, username, email) #List the files in the /pub directory
	ftp.cwd("/pub")
	print(f"File list at {path}")
	files = ftp.dir()
	print(files)
	ftp.quit()




if __name__ == '__main__':
	test_ftp_connection(path=FTP_SERVER_URL, username='anonymous', email='nobody@nourl.com', )
