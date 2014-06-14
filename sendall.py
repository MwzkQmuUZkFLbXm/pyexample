#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sendall.py 

# for sockes
import socket
# for exit
import sys

try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' Error message: ' + msg[1]
    sys.exit()

print 'Socket Created'
host = 'www.google.com'
port = 80
try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print 'Hostname could not be resolved. Existing'
    sys.exit()

print 'Ip address of ' + host + ' is ' + remote_ip

# Connect to remore server
s.connect((remote_ip, port))

print 'Socket Connected to ' + host + ' on ip ' + remote_ip

# Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"

try:
    # Set the whole string
    s.sendall(message)
except socket.error:
    #Send failed
    print 'Send failed'
    sys.exit()

print 'Message send successfully'
s.close()
