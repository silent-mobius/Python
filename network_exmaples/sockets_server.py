#!/usr/bin/env python3

######################################################
# created by : Pushtakio
# purpose : basic tcp server
# date :
# version: 1.0.0
#######################################################

import socket

host = 'localhost'
port = 8080


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(100)

conn, addr = s.accept()

print('[+]Connected by: ', addr)

while True:
    data = conn.recv(2048)
    if not data:
        break
    conn.send(data)

conn.close()