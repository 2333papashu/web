# coding:utf-8

import re


class WSGIapp:
    headers = []

    def __init__(self, urls):
        self.urls = urls
        self.status = '200 ok'

    def __call__(self, environ, start_response):
        response = self.mapping_urls(environ)
        start_response(self.status, self.headers)
        return response

    def mapping_urls(self, environ):
        # print environ['PATH_INFO']
        path = environ['PATH_INFO']
        # path = '/hello/'

        for pattern, name in self.urls:
            m = re.match('^'+pattern+'$', path)
            print pattern
            print path
            if m:
                args = m.groups()
                print 'args:', args
                print m.group()
                print '\n'
                func = globals()[name]
                return func(*args)
        return no_fund(self)

    @classmethod
    def set_headers(cls, name, value):
        cls.headers = []
        cls.headers.append((name, value))


def no_fund(self):
    self.status = '404 NOT Found'
    WSGIapp.set_headers('Content-Type', 'text/plain')
    return '404 Not Found\n'


def GET_index(*args):
    WSGIapp.set_headers('Content-Type', 'text/plain')
    return 'Hello, Lin!\n'


def GET_hello(*args):
    WSGIapp.set_headers('Content-Type', 'text/plain')
    return 'Hey Lin!\n'
urls = [
    ('/', 'GET_index'),
    ('/hello/(.*)', 'GET_hello')
]
app = WSGIapp(urls)
