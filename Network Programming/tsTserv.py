from socket import *
from time import ctime

HOST = '192.168.2.101'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)
tcpSerSocket = socket(AF_INET,SOCK_STREAM)
tcpSerSocket.bind(ADDR)
tcpSerSocket.listen(5)

while True:
	print('waiting for connection')
	tcpCliSock,addr = tcpSerSocket.accept()
	print('...connected from:',addr)
	while True:
		data = tcpCliSock.recv(BUFSIZ)
		print(data.decode('utf-8'))
		if not data:
			break;
		tcpCliSock.send(bytes(('[%s] %s' % (ctime(),data)),'utf-8')) #use ascii
	tcpCliSock.close()
tcpSerSocket.close()
