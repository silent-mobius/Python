#!/usr/bin/env python3

######################################################
# created by : Pushtakio
# purpose : basic tcp client
# date :
# version: 1.0.0
#######################################################

import socket

host = 'localhost'
port = 8080

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

while i != 'EOF':
    data = input('my message: ')
    s.send(data)
    d = s.recv(2048)

s.close()