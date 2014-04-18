# from: http://www.binarytides.com/python-socket-programming-tutorial/
# cn: http://www.oschina.net/question/12_76126

# =========================
# 1. Create a socket
# 2. Connect to remote server
# 3. Send some data
# 4. Receive a reply
#===========================

import socket
import sys

HOST = ""
PORT = 8888

try:
	# AF_INET--> IP4;  SOCK_STREAM-->TCP
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
	print 'Failed to create socket. Error code: %s , Error message: %s' % (str(msg[0]), msg[1])
	sys.exit()
print "Socket create"


try:
	remote_ip = socket.gethostbyname(HOST)
except socket.gaierror:
	print "Hostname could not be resolved. Exiting"
	sys.exit()


s.connect((remote_ip, PORT))
print "Socket connect to %s:%s"  % (remote_ip, PORT)

while 1:
	# send
	message = raw_input('client ask -->:')
	try:
		s.sendall(message)
	except socket.error:
		print "Send Failed"
		sys.exit()
	# print "Message send successfully"


	#recive
	reply = s.recv(4096)
	if not reply:
		break
	print reply

# s.close()






