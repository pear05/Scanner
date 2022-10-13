#!/bin/python3
#checking wheather a port is open
import sys
import socket
from datetime import datetime
#define our target
if len(sys.argv) ==2:
	tagret = socket.gethostbyname(sys.argv[1])
#if len(sys.argv) == 2:
	#target = socket.gethostbyname(sys.argv[1]) 
#translating hostname to ipv4
else:
	print("Invalid arguments")
	print("syntax: python3 scanner.py <ip>")

#add a banner
print("-" * 50)
print("Scanning target "+target )
print("Time started: "+str(datetime.now())) 
print("-" * 50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns an error indicator
		if result == 0:
			print("port {} is Open".format(port))
			s.close()
			
except KeboardInterrupt:
	print("\nExiting program,")
	sys.exit()

except socket.gaierror:
	print("Host could not be resolved,")
	sys.exit()
except socket.error:
	print("couldnt connect to server")
	sys.exit()
	

