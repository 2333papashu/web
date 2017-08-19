# coding:utf-8
class A(object):
    money = None

    def same(self):
        print "I am A"

    def p(self):
        self.c()


class B(object):
    money = 100

    def c(self):
        print '现在在B里面'

    def same(self):
        print "I am B"


class C(A, B):

    def __init__(self):
        A.__init__(self)
        B.__init__(self)

    def CC(self):
        self.p()

    def same(self):
        # 将实例化对象 self传递进去
        B.same(self)


c = C()

c.CC()
c.same()
import cgi
