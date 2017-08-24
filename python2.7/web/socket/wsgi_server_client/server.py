# coding:utf-8
import socket
import StringIO
import sys


class WSGIServer(object):
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 2

    def __init__(self, server_address):
        self.listen_socket = listen_socket = socket.socket(
            self.address_family,
            self.socket_type
        )
        listen_socket.bind(server_address)
        listen_socket.listen(self.request_queue_size)
        # 这些是envrion需要的参数
        host, port = self.listen_socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        print self.server_name
        self.server_port = port
        self.headers_set = []

    def set_app(self, application):
        self.application = application

    def set_environ(self):
        env = {}
        env['wsgi.version'] = (1, 0)
        env['wsgi.url_scheme'] = 'http'
        env['wsgi.input'] = StringIO.StringIO(self.request_data)
        env['wsgi.errors'] = sys.stderr
        env['wsgi.multithread'] = False
        env['wsgi.multprocess'] = False
        env['wsgi.run_once'] = False

        env['RESQUEST_METHOD'] = self.request_method
        env['PATH_INFO'] = self.path
        env['SERVER_NAME'] = self.server_name
        env['SERVER_PORT'] = str(self.server_port)

        return env

    def start_response(self, status, response_headers, exc_info=None):
        server_headers = [
            ('Date', 'Tue, 31 Mar 2015 12:54:48 GMT'),
            ('Server', 'WSGIServer 0.2'),
        ]
        # 列表相加
        self.headers_set = [status, response_headers+server_headers]

    def finish_response(self, result):
        # 将数据打包送走
        # header 与 body
        try:
            status, response_headers = self.headers_set
            response = 'HTTP/1.1 {status}\r\n'.format(status=status)
            # header数据格式是元组
            for header in response_headers:
                response += '{0}:{1}\r\n'.format(*header)
            response += '\r\n'
            for data in result:
                response += data
            # 打印看一下报头
            print ''.join('> {line}'.format(line=line) for line in response.splitlines())
            print '----'
            print response
            self.client_socket.sendall(response)
        finally:
            self.client_socket.close()

    def parse_request(self, request_data):
        # 这里的格式并不是很清楚
        print 'parse_request method'
        request_line = request_data.splitlines()[0]
        request_line = request_line.rstrip('\r\n')
        (self.request_method, self.path, self.request_version)= request_line.split()

    def handle_request(self, client_socket):
        self.request_data = request_data = client_socket.recv(1024)
        # 需要解析下request_data
        # 这里一定有数据？
        print 'handle_request:', request_data
        print '\n'
        self.parse_request(request_data)
        environ = self.set_environ()
        data = self.application(environ, self.start_response)
        self.finish_response(data)


    def server_forver(self):
        # 感觉这里也可以直接用self里面的listen_socket
        listen_socket = self.listen_socket
        while True:
            self.client_socket, client_address = listen_socket.accept()
            # 这个应该是通过body传进来的参数
            self.handle_request(self.client_socket)
            self.client_socket.close()

ADDRESS = (HOST, PORT) = '', 8899


def make_server(address, application):
    wsgi_server = WSGIServer(address)
    wsgi_server.set_app(application)
    return wsgi_server


if __name__=='__main__':
    # 获取application
    if len(sys.argv) < 2:
        sys.exit('Provive a WSGI application as moudle:callable')
    app_path = sys.argv[1]
    o_moudle, application = app_path.split(':')
    # 内建方法
    o_moudle = __import__(o_moudle)
    application = getattr(o_moudle, application)
    httped = make_server(ADDRESS, application)
    print 'WSGIServer:Servering HTTP on port {port}'.format(port=PORT)
    httped.server_forver()