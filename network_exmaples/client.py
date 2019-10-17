#!/usr/bin/env python
########################################################################
# created by: Pushtakio
# purpose: network server client practice
# date: unknow
# version: 2.7.91
########################################################################

import socket
'''
def getInput():
    ans = input("enter your message: ")
    return ans

# This is the method that creates the challenge. In this case it's the sum of ascii values of all characters in the message
def createChallenge(message):
    return sum(map(ord, message))

# The method to add a challenge to a message. The return message will be as follows: <num_of_characters_in_original_message>_<original_message>_<challenge>
def challengeEncode(message):
    # create the challenge
    challenge = createChallenge(message)
    # create the encoded message in the format of <num_of_characters_in_original_message>_<original_message>_<challenge>
    return '%d_%s_%d' % (len(message), message, challenge)

# The method to decode a message encoded with a challenges
def challengeDecode(message):
    try:
        # first get the number of characters in original message
        num_of_chars = int(message.split('_')[0])
        # calcualte the number of digits in number of characters
        num_of_digits = len(str(num_of_chars))
        # extract the original message from the encoded message
        orig_message = message[num_of_digits+1:num_of_digits+1+num_of_chars]
        # extract the challenge from the encoded message
        challenge = int(message[num_of_digits+1+num_of_chars+1::])
        # calculate the challenge for the original message and compare is to the challenge we got in the message
        return (challenge == createChallenge(orig_message))
    # if an excpetion is thrown it means the encoded message structure was invalid
    except:
        print ("Could not decode encoded message: message structure is invalid")
        return False


def echoClient():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)
    print('connecting to %s port %s' % server_address)
    sock.connect(server_address)

    # a varaible to remember if we already sent the username
    username_sent = False
    # a varaible to remember if we already sent the password
    password_sent = False

    try:
        while True:
            message = getInput()
            if message.lower() == "bye":
                print("[!] Disconnecting: Bye")
                sock.sendall(str.encode("bye"))
                break

            # make sure username if sent first
            if not username_sent:
                username_sent = True
                print('[+]sending username "%s"' % str.encode(message))
                sock.sendall(str.encode(message))
                # Look for the response
                data = sock.recv(50)
                if data:
                    print('[-]received "%s"' % data.decode("utf-8"))
                continue

            # now send the password
            if not password_sent:
                password_sent = True
                print('[+]sending password')
                # make sure to encode the password message before sending it
                message = challengeEncode(message)
                sock.sendall(str.encode(message))
                # Look for the response
                data = sock.recv(50)
                if data:
                    print('[-]received "%s"' % data.decode("utf-8"))
                continue

            # for any other message - just send it
            else:
                print('[+]sending message "%s"' % str.encode(message))
                sock.sendall(str.encode(message))
                # Look for the response
                data = sock.recv(50)
                if data:
                    print('[-]received "%s"' % data.decode("utf-8"))

    finally:
        print('[!]closing socket')
        sock.close()

if __name__ == "__main__":
	echoClient()
'''


import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_address = ('', 10000)
sock.bind(server_address)
print >>sys.stderr, 'starting up on %s port %s' % sock.getsockname()
sock.listen(1)

while True:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'client connected:', client_address
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()
