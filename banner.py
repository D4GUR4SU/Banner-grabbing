#!/usr/bin/python3
import socket

RED   = "\033[1;31m"

print("\n")
print(RED+"\t                                                                                                                         ")
print(RED+"\t ██████   █████  ███    ██ ███    ██ ███████ ██████       ██████  ██████   █████  ██████  ██████  ██ ███    ██  ██████   ")
print(RED+"\t ██   ██ ██   ██ ████   ██ ████   ██ ██      ██   ██     ██       ██   ██ ██   ██ ██   ██ ██   ██ ██ ████   ██ ██        ")
print(RED+"\t ██████  ███████ ██ ██  ██ ██ ██  ██ █████   ██████      ██   ███ ██████  ███████ ██████  ██████  ██ ██ ██  ██ ██   ███  ")
print(RED+"\t ██   ██ ██   ██ ██  ██ ██ ██  ██ ██ ██      ██   ██     ██    ██ ██   ██ ██   ██ ██   ██ ██   ██ ██ ██  ██ ██ ██    ██  ")
print(RED+"\t ██████  ██   ██ ██   ████ ██   ████ ███████ ██   ██      ██████  ██   ██ ██   ██ ██████  ██████  ██ ██   ████  ██████   ")
print(RED+"\t                                    		    v1.0.0						                  ")
print(RED+"\t                            			by D4GUR4SU		                                          ")
print("\n")

target = input('Enter the IP/Domain: ')
port = int(input('Enter the Port: '))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target,port))
banner = client.recv(1024)
print(banner)
