#!/usr/bin/env python3
##################################################################
# created by Pushtakio  
# purpose: knocking on ports with python
# date: 22/10/2019
# version: 1.0.1
##################################################################
import os
import sys
import socket

s = socket.socket()
s.settimeout(2)

trgt = input('Please provide server to test ->> ')
s.connect((trgt,80))

req = 'HEAD / HTTP/1.1\r\nHost: '+ trgt +'\r\n\r\n'

print('Sending: ',req)
s.sendall(bytes(req))

print('Recieved: ',s.recv(1024))

s.close