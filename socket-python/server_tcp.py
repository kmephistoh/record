# ==================================
# 1. Open a socket
# 2. Bind to a address(and port).
# 3. Listen for incoming connections.
# 4. Accept connections
# 5. Read/Send
# ==================================

import socket 
from thread import * 

HOST = ''
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)
print "Socket now listening , 10 is enough "


def  client_thread(conn):
	# conn.send("Welcome to the server, Type something and hit enter\n")
	while 1:
		data = conn.recv(1024)
		reply = "Server reply: " + data
		if not data:
			break
		conn.sendall(reply)
	conn.close()


while 1:
	conn , addr = s.accept()
	print "Connected with %s:%d" % (addr[0], addr[1])
	start_new_thread(client_thread, (conn, ))

s.close()




