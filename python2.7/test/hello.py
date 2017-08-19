li = [1,2]
it = iter(li)
print li
print it
print it.next
print it.next()
print it.next()
print '----'
x = range(2, 10)
print x[0]


class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __len__(self):
        return self.end - self.start

    def __getitem__(self, index):
        if index < 0 or index > len(self):
            raise IndexError
        return index+self.start

myrange = MyRange(1, 3)
print myrange[0]

print type(myrange)


def MyGenerator():
    value = (yield 'hello')
    print value
    value = (yield value)
    print value
    value = (yield value)


gen = MyGenerator()
print gen.next()
print gen.send('yes')
print gen.send('1')

print [0]*2
empty = 'fa'
default = empty
required = default is empty and not 'read_only'
print required
assert not ('1' and '2'), 'error'
assert 1==3