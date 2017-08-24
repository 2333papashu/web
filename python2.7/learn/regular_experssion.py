import re

path = '/hello'
urls = [
    ('/hello', 'GET_hello'),
    ('/', 'GET_all')
]

# m = re.match('^'+'/hello'+'$', path)
print re.match("([abcd]+)", "babcdabcfffaa").groups()
print re.match("([abcd]+)", "babcdabcfffaa").group()
print re.match("([abcd])([abcd])([abcd])", "abcdabcfffaa").groups()

# a = "123abc456"
a = "123456dg333"
print re.match("([0-9])+([a-z]*)([0-9]*)", a).groups(0)
print re.match("([0-9])+", a).groups(1)