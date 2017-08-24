# coding:utf-8
import socket

HOST, PORT, BUFSIZ = '', 8899, 1024
# 地址绑定的时候使用
ADDR = (HOST, PORT)

# 创建套解字
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 绑定
listen_socket.bind(ADDR)
# 监听
listen_socket.listen(1)
print "Servering HTTP on port %s..." % PORT
# 服务器循环处理
while True:
    # 接受TCP连接, 并返回新的套接字和端口
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(BUFSIZ)
    # split()切分request内容 返回list
    print request
    # print "...connected from :", client_address
    http_response = """\
    HTTP/1.1 200 OK
    
    Hello World!
    """
    client_connection.sendall(http_response)
    client_connection.close()