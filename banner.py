#!/usr/bin/python
import socket

target = raw_input('Enter the IP/Domain: ')
door = input('Enter the Door: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target,door))
banner = client.recv(1024)
print banner
