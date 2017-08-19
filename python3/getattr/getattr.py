class A:
    def __init__(self):
        self.a = 'a'

    def b(self):
        print('b')

a = A()
print(getattr(a, 'a', 'None'))
# getattr里面是空的啊
