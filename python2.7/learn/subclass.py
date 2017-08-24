# coding:utf-8
class A(object):
    # 新式类
    def go(self):
        print "go A go!"

    def stop(self):
        print "stop A stop!"

    def pause(self):
        raise Exception("Not Implemented")


class B(A):
    def go(self):
        super(B, self).go()
        print "go B go!"


class C(A):
    def go(self):
        super(C, self).go()
        print "go C go!"

    def stop(self):
        super(C, self).stop()
        print "stop C stop!"


class H(A):
    def go(self):
        super(H, self).go()
        print "go H go!"


class D(B, C, H):
    def go(self):
        super(D, self).go()
        print "go D go!"

    def stop(self):
        super(D, self).stop()
        print "stop D stop!"

    def pause(self):
        print "wait D wait!"


class E(B, C):
    pass


class F(B, C):

    def go(self):
        print "go F go!"
a = A()
b = B()
c = C()
d = D()
e = E()
f = F()

a.go()
print "go A go"
print "---"
b.go()
print "go A go"
print "go B go"
print "---"
c.go()
print "go A go"
print "go C go"
print "---"
d.go()
print "go A go"
print "go H go"
print "go c go"
print "go B go"
print "go D go"
print "----"
e.go()
print "go B go"
print "----"
f.go()
print "go F go"
