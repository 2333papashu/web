import os

temp = 0

pid = os.fork()
if pid == 0:
    print 'child: ', temp
else:
    temp = 1000
    print 'parent:', temp
