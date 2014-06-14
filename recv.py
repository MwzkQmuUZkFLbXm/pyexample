#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# recv.py 

import socket # for sockets
import sys # for exit

# create an AF_INET, SOCKET_STREAM socket (TCP)
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

print 'Socket Created'

host = 'www.baidu.com'
port = 80

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    # could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

#Connect to remote server
s.connect((remote_ip, port))

print 'Socket Connected to ' + host + ' on ip ' + remote_ip

# Send some date to remote server
messge = 'GET / HTTP/1.1\r\n\r\n'

try:
    # set the whole string
    s.sendall(message)
except socket.error:
    # send Failed
    print 'Send failed'

print 'Message send successfully'

# Now receive data
reply = s.recv(4096)

print reply
s.close()
