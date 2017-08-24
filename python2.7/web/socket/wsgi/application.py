# coding:utf-8
# environ 包含了wsgi、CGI等环境变量


def app(environ, strat_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text-plain')]
    strat_response(status, response_headers)
    return ['I am app hello world...']