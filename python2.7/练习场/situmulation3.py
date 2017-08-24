# coding:utf-8

import socket


def main():

    HOST = ''
    PORT = 8899
    MAX_LISTENS = 5
    ADDRESS = (HOST, PORT)
    BUFSIZ = 1024

    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind(ADDRESS)
    tcp_server.listen(MAX_LISTENS)
    # 函数式编程 传递参数这里有坑
    # 考虑需要传什么值，需要返回什么值
    # 说到底 就是编程之前心里有谱,就和做菜一样
    connect(tcp_server, BUFSIZ)
    tcp_server.close()


def connect(server, BUFSIZ):
    while True:
        print "Waiting for connection..."
        tcp_client, addr = server.accept()
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
        Context-Length:

        Hello World!
        '''
        tcp_client.sendall(respone)
        tcp_client.close()

if __name__ == "__main__":
    main()