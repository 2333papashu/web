# coding:utf-8

import socket
import chardet

HOST = '127.0.0.1'
PORT = 8899
MAX_LISTENS = 5
ADDRESS = (HOST, PORT)
BUFSIZ = 1024

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    tcp_server.bind(ADDRESS)
except socket.error as e:
    text = "端口被占用"
    print text
    print type(text)
    print '-'*8
    print e
    # print chardet.detect(e)
    print type(e)
    exit(0)
tcp_server.listen(MAX_LISTENS)
# 函数式编程 传递参数这里有坑
# 考虑需要传什么值，需要返回什么值
# 说到底 就是编程之前心里有谱,就和做菜一样
while True:
    print "starting server http://{}:{}".format(HOST, PORT)
    print "Waiting for connection..."
    tcp_client, addr = tcp_server.accept()
    print "...connected from:http://{}:{} ".format(addr[0], addr[1])
    res = tcp_client.recv(BUFSIZ)
    if res:
        print res
        # tcp_client.sendall(respone)
    else:
        print "空"
        # break
    respone = '''\
    HTTP/1.1 200 OK
    Context-Type: text/html
    Server: Python-slp version 1.0
    Context-Length:100
    Access-Control-Allow-Origin:*

    Hello World!
    '''
    tcp_client.sendall(respone)
    tcp_client.close()


