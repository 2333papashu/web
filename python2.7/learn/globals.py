def xxx(urls):
    for pattern, name in urls:
        print name
        print globals()[name]

urls = [
    ('/', 'GET_index'),
    ('/hello/', 'GET_hello')
]


def GET_index():
    pass


def GET_hello():
    pass


if __name__ == "__main__":
    xxx(urls)