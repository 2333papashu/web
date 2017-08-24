# coding:utf-8
# 编程的顺序 整个框架是怎么出来的
# 符合WSGI标准的应用程序, 有请求进来的时候调用的程序
import sys
import socket
import StringIO


# 先创建最基本的类
class WSGIServer(object):
    # 跟踪目前连接的客户端
    total = 0
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 2

    # create a listeing socket
    def __init__(self, server_address):
        self.listen_socket = listen_socket = socket.socket(
            self.address_family,
            self.socket_type
        )
        listen_socket.bind(server_address)
        listen_socket.listen(self.request_queue_size)
        host, port = self.listen_socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port
        self.headers_set = []

    def set_app(self, application):
        # 这里也提示了application这个属性定义的位置有点问题
        self.application = application

    def serve_forever(self):
        # 定义局部变量 怎么深刻理解这个self
        listen_socket = self.listen_socket
        while True:
            # total不是全局类里面的吗
            # 使用self 有些对象就不用放在函数参数里面了
            self.client_connection, client_address = listen_socket.accept()
            self.total += 1
            print "已有%d个客户端连接" % self.total
            self.handle_one_request()
            print 'finish one request...'

    def handle_one_request(self):
        # 接受客户端的数据
        self.request_data = request_data = self.client_connection.recv(1024)
        print 'handle_one_request:'
        print request_data
        # request_data 这里只是用来设置参数 如果 application需要用呢..
        self.parse_request(request_data) # 设置一些参数用来设置environ参数的
        env = self.get_environ()
        # 开始调用满足WSGI标准的application
        # 处理返回的内容应该也可以独立成一个模块
        # 这里只是传递start_response给自定义的application
        # 至于怎么使用start_response这个是符合WSGI标准的应用程序约定好的
        result = self.application(env, self.start_response)
        print result
        print '---------------'
        # 返回body主体部分
        # 处理应用程序返回的数据
        self.finish_response(result)

    def parse_request(self, request_data):
        request_line = request_data.splitlines()[0]
        print 'parser_request:'
        print request_line
        request_line = request_line.rstrip('\r\n')
        (self.request_method, self.path, self.request_version) = request_line.split()

    def get_environ(self):
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
        """让接口应用程序调用的 用来记录调用程序请求的一些状态 比如调用成功 200 OK"""
        server_headers = [
            ('Date', 'Tue, 31 Mar 2015 12:54:48 GMT'),
            ('Server', 'WSGIServer 0.2'),
        ]
        self.headers_set = [status, response_headers + server_headers]

    # 接受处理接口应用程序传过来的值 这里估计还可以机智点
    # 将收到的数据重新组织发送出去
    def finish_response(self, result):
        try:
            status, response_headers = self.headers_set
            print 'finish_response->response_headers:'
            print response_headers
            print '------------'
            # 这句行头肯定需要
            response = 'HTTP/1.1 {status}\r\n'.format(status=status)
            for header in response_headers:
                response += '{0}:{1}\r\n'.format(*header)
            response += '\r\n'
            for data in result:
                response += data
            print ''.join('> {line}\n'.format(line=line)
                          for line in response.splitlines())
            self.client_connection.sendall(response)
        finally:
            self.client_connection.close()

SERVER_ADDRESS = (HOST, PORT) = '', 8889


# 创建一个函数来创建对象
def make_server(server_address, application):
    server = WSGIServer(server_address)
    server.set_app(application)
    return server

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Provide a WSGI application object as moudle:callable')
    app_path = sys.argv[1]
    moudle, application = app_path.split(':')
    moudle = __import__(moudle) # 导入application的固定套路
    application = getattr(moudle, application)
    httped = make_server(SERVER_ADDRESS, application)
    print 'WSGIServer:Serving HTTP on port {port}....\n'.format(port=PORT)
    httped.serve_forever()