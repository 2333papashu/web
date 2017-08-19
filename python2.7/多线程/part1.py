# coding:utf-8
import threading
import time


def Myjoin(count):
    print 'hello world!'
    print count
    # time.sleep(10)


for i in range(5):
    t = threading.Thread(target=Myjoin, args=(i,))
    t.start()
    t.join()
print 'hello main'
# 阻塞主线程