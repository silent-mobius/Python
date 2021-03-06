#!/usr/bin/env python3
####################################################################
# Python Network Programming Cookbook -- Chapter - 5
# This program is optimized for Python 3.6 or newer.
# It may run on any other version with/without modifications
#http://file.allitebooks.com/20150514/Python%20Network%20Programming%20Cookbook.pdf
########################################################################
# created by: Pushtakio
# purpose: practice cgi scripting
# date: unknow
# version: unknow
########################################################################

import os
import cgi
import argparse
import http.server
from http.server import CGIHTTPRequestHandler
import cgitb
cgitb.enable() ## enable CGI error reporting


def web_server(port):
	server = http.server.HTTPServer
	handler = CGIHTTPRequestHandler #RequestsHandler
	server_address = ("", port)
	handler.cgi_directories = ["/cgi-bin", ]
	httpd = server(server_address, handler)
	print(f'Starting web server with CGI support on port: {port}')
	httpd.serve_forever()


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='CGI Server Example')
	parser.add_argument('--port', action="store", dest="port",type=int, required=True)
	given_args = parser.parse_args()
	web_server(given_args.port)
