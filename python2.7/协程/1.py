def func():
    n = 10
    while 1:
        n = yield n

f = func()
print f.send(None)
print f.send(1)