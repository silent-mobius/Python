#!/usr/bin/env python3

######################################################
#
#
#
#
#
#######################################################

import http.client

data = input("Please provide the web site: ")

h = http.client.HTTPConnection(data)
h.request("GET", '/')
d = h.getresponse()
print(d.code)
print(d.headers)
t = d.readlines()
for i in t:
    print(i.decode('utf-8'))