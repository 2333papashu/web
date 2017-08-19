# coding:utf-8

import socket

ADDRESS = (HOST, PORT) = 'localhost', 8889
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDRESS)
data = "hello I am Client"
client_socket.sendall(data)
data = client_socket.recv(1024)
print data
client_socket.close()