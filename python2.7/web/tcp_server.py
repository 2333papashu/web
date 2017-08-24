# coding:utf-8
from socket import *
from time import ctime

HOST = ''
PORT = 8899
BUFSIZ = 1024
ADDR = (HOST, PORT)


tcpSerSock = socket(AF_INET, SOCK_STREAM)
# print tcpSerSock
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print 'Waiting for connection...'
    tcpCliSock, addr = tcpSerSock.accept()
    print '...connected from:', addr
    # tcpCliSock.send('tcp_server...')
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print data
        tcpCliSock.send('[%s] %s' % (ctime(), data))

    tcpCliSock.close()
tcpSerSock.close()