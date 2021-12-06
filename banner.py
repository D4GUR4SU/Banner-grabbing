#!/usr/bin/python
import socket

target = raw_input('Enter the IP/Domain: ')
port = input('Enter the Port: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target,port))
banner = client.recv(1024)
print banner
