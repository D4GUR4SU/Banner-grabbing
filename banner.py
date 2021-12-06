#!/usr/bin/python
import socket

print "|#################################################################################|"
print "|  ____                                 ____           _     _     _              |"
print "| | __ )  __ _ _ __  _ __   ___ _ __   / ___|_ __ __ _| |__ | |__ (_)_ __   __ _  |"
print "| |  _ \ / _` | '_ \| '_ \ / _ \ '__| | |  _| '__/ _` | '_ \| '_ \| | '_ \ / _` | |"
print "| | |_) | (_| | | | | | | |  __/ |    | |_| | | | (_| | |_) | |_) | | | | | (_| | |"
print "| |____/ \__,_|_| |_|_| |_|\___|_|     \____|_|  \__,_|_.__/|_.__/|_|_| |_|\__, | |"
print "|                                                                          |___/  |"
print "| 				v1.0.0						  |"
print "| ->			by D.4.G.U.R.4.S.U (Douglas Souza)		       <- |"
print "|#################################################################################|\n\n"


target = raw_input('Enter the IP/Domain: ')
port = input('Enter the Port: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target,port))
banner = client.recv(1024)
print banner
