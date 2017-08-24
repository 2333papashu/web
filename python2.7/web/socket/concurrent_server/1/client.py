# coding:utf-8

import socket

ADDRESS = (HOST, PORT) = '127.0.0.1', 8899
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDRESS)
print '连接成功'
data = "hello I am Client"
client_socket.sendall(data)
data = client_socket.recv(1024)
print data
client_socket.close()