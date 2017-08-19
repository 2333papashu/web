# coding:utf-8
import socket

# TODO 这个还解析不了外网的域名?
# target_ip = 'localhost'
target_ip = 'www.baidu.com'
# target_ip = 'http://www.baidu.com'
# 检查ip是否合法
try:
    target_ip = socket.gethostbyname(target_ip)
except socket.gaierror as e:
    print e
print target_ip
tgtName = socket.gethostbyaddr(target_ip)
print tgtName
