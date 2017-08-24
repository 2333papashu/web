# coding:utf-8
request_data = 'fdasfs\r\nvfsd\nffs'
lala = request_data.splitlines()
print ''.join(
    '< {line}\n'.format(line=line) for line in request_data.splitlines()
)
# 还能这么赋值 强！
status, response_headers = ['lala', 'haha']
print response_headers