# coding:utf-8
# 实现最简单的服务器 迭代式服务器
import socket
import time
import os
SERVER_ADDRESS = (HOST, PORT) = '', 8899


# 处理请求
def handle_request(connection):
    response = connection.recv(1024)
    print response
    http_response = b"""\
    HTTP/1.1 200 ok
    
    Hello,World!
    """
    connection.sendall(http_response)
    time.sleep(30)


# 开启服务器
def serve_forver():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 重启服务器后, 服务器继续使用相同的地址?? 设置部分套接字
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(1)
    print 'Serving HTTP on port {port}...'.format(port=PORT)
    while True:
        client_connection, client_address = listen_socket.accept()
        print "...connected on address {address}".format(address=client_address)
        handle_request(client_connection)
        client_connection.close()


if __name__ == '__main__':
    print '子进程:',os.getpid()
    print '父进程:',os.getppid()
    serve_forver()