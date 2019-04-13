#!/usr/bin/python

#########################################################
#
#
#
#########################################################

###libs import ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#from socket import socket
import socket
###Variables +++++++++++++++++++++++++++++++++++++++++++++++++++++
HOST,PORT= '',8080
#l_socket stands for "listen_socket"
l_socket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
l_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # number stands for amount of connection that will be served
l_socket.bind((HOST, PORT)) # binding connection to host and port intered before-hands
l_socket.listen(1)

###Functions /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\




###
#Main - _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _
###
print "Serving connection on Port : %s" %PORT
while True:
	c_connection, c_addr = l_socket.accept()
	request = c_connection.recv(1024)
	print request
	http_response=""" HTTP/1.1 200 OK """
	c_connection.sendall(http_response)
	c_connection.close()
