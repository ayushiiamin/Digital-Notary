#References:
#1. https://www.thepythoncode.com/article/send-receive-files-using-sockets-python - for establishing communication using TCP sockets

#import necesarry libraries

import socket               
#import base64

try:
	s = socket.socket()         	 # Creating an object of socket
	host = socket.gethostname() 
	port = 1235
	s.connect((host,port))               # allocating socket to address

	print("Connecting to server", host)

	#isConnected = False


	while True:  #Receive messages from server and respond accordingly
		print("From server: "+s.recv(1024).decode()) 
		inp = input("Your input: ")		
		s.send(inp.encode())


	s.close()

#Ctrl c for closing connection
except KeyboardInterrupt:
	print("Closing connection at client end")
	s.close()

