#!/usr/bin/env python
# -*- coding: utf-8 -*-
# client.py 

# for sockets
import socket
# for exit
import sys

#handling errors in python socket programs
def port_detect(host='localhost'):
    try:

        # create an AF_INET, STREAM socket (TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
    except socket.error, msg:
        print 'Failed to created socket. Error code: ' + str(msg[0]) + 'Error message: ' + msg[1]
        sys.exit();

    print 'Socket Created'

    # get the IP address of the remote host/url
    #host = '74.125.68.34'
    port = 9999

    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        # could not resole
        print 'Hostname could not be resolved. Exiting'
        sys.exit()
 
    print 'Ip address of ' + host + ' is ' + remote_ip

    # Connect to remote server
    s.connect((remote_ip, port))
    print 'Socket Connect to ' + host + ' on ip ' + remote_ip
    s.close()

if __name__ == '__main__':
    port_detect()
