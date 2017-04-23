#!/usr/bin/python3

import socket
def scanPort(ip, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex((ip, int(port)))
	if result == 0:
   		print(ip + ':' + str(port) + ' is open')
	else:
   		print(ip + ':' + str(port) + ' is closed')


def scanAllPorts(ip):
	for i in range(0, 65535):
		scanPort(ip, i)

def menu():
	ip = input('Enter IP To Scan: ')
	port = input('Enter Port To Scan (Enter Nothing For All): ')
	if port == '':
		scanAllPorts(ip)
		menu()
	else:
		scanPort(ip, int(port))
		menu()
menu()
