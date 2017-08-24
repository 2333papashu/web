# coding:utf-8
# 最简单的并发服务器
import errno
import socket
import time
import os
import signal

SERVER_ADDRESS = (HOST, PORT) = '', 8899


# handle_request结束才调用它
# 确保所有子进程都被处理
def handle_child_process(signum, frame):
    while True:
        try:
            pid, status = os.waitpid(
                -1,
                os.WNOHANG
            )
        except OSError:
            return
        if pid == 0:
            return


def handle_request(client_connection):
    context = client_connection.recv(1024)
    response = """\
    HTTP/1.1 200 OK
    
    Hello, World!
    """
    client_connection.sendall(response)
    time.sleep(3)


def server_forver():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(3)
    print "Servering HTTP on port {port}...".format(port=PORT)

    # 这里添加发送异步处理信号
    signal.signal(signal.SIGCHLD, handle_child_process)

    while True:
        try:
            client_connection, client_address = listen_socket.accept()
        except IOError as e:
            code, msg = e.args
            if code == errno.EINTR:
                continue
            else:
                raise
        except KeyboardInterrupt:
            break
        pid = os.fork()
        if pid == 0:
            listen_socket.close()
            print 'connected from http://{0}:{1}'.format(client_address[0], client_address[1])
            handle_request(client_connection)
            client_connection.close()
            # 进程退出函数 其实也不懂
            os._exit(0)
        else:
            client_connection.close()

if __name__ == "__main__":
    server_forver()
    print "服务器已打烊"