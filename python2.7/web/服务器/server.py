# coding:utf-8
import socket

HOST = ''
PORT = 8889
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind(ADDR)
tcp_server_socket.listen(1)

print "Servering HTTP on port %s..." % PORT

while True:
    # TODO 了解accept时候的细节
    try:
        client_connection, client_address = tcp_server_socket.accept()
    except KeyboardInterrupt as e:
        break
    request = client_connection.recv(BUFSIZ)
    # handle_request 返回内容
    print request
    # response的格式有什么标准吗
    # response = """HTTP/1.1 200 OK
    # Hello World!
    # """
    response = "haha"
    client_connection.sendall(response)
    client_connection.close()
print "服务器打烊了"
# TODO 改服务器代码后需要重新启动才能生效