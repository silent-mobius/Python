#!/usr/bin/env python3

import socket


userList={'Alex':123, 'ninja':'paradise', 'yoni':'whatever'}
'''
def getInput():
    ans = input("[+]enter your message: ")
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
        print ("[!]Could not decode encoded message: message structure is invalid")
        return False

def echoServer():
    listOfData=[]
    sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    server_address = ('localhost', 10000)
    print ( '[+]starting up on %s port %s' % server_address)
    sock.bind(server_address)
    sock.listen(1)

    # a varaible to remember if we already got the username
    username_received = False
    # a varaible to remember if we already got the right password
    password_received = False

    while True:
        # Wait for a connection
        print ('[!]waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print( '[!]connection from', client_address)

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(50)
                if data:
                    if data.decode("utf-8") == "bye":
                        print("[!]Shutting down")
                        break

                    listOfData.append(data.decode("utf-8"))

                    # if username was not yet received
                    if not username_received:
                        # mark that username was provided
                        username_received = True

                        # send a response to user to send the password
                        response = "[!]got username, please send password"
                        connection.sendall(str.encode(response))
                        print (response)
                        continue

                    # if correct password was not received
                    if not password_received:
                        # extract received message
                        recv_message = '%s' % data.decode("utf-8")
                        print ("[+]encoded message received:", recv_message)
                        # decode the encoded message and check the challenge
                        challenge_passed = hash(challengeDecode(recv_message))
                        print ("[+]got password, challenge passed" if (challenge_passed) else "[-]got password, challenge failed")
                        # return an answer to the client
                        response = "[!]password ok" if (challenge_passed) else "password failed, please send again"
                        connection.sendall(str.encode(response))
                        password_received = challenge_passed
                        continue

                    else:
                        response = "[+]got message '%s'" % str(data.decode("utf-8"))
                        print (response)
                        connection.sendall(str.encode(response))

                else:
                    print( '[!]no more data from', client_address)
                    break

        finally:
            # Clean up the connection
            connection.close()



if __name__ == '__main__':
    echoServer()
'''

import socket
import sys

HOST = ''   # Symbolic name, meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

#Start listening on socket
s.listen(10)
print 'Socket now listening'

#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

s.close()