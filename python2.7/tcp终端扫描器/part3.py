# coding:utf-8
import socket
import optparse
import time

# TODO 封装一个类 减少重复代码
# 抓取应用banner信息


def connectScan(address, port):
    try:
        connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 这个函数决定参参数的格式
        # 注意connect的格式
        print '请求连接'
        connect.connect((address, port))
        print '已连接'
        # connect.send('Hello World')
        # print '已发送请求'
        # recv函数需要一个参数 eg:1024
        # result = connect.recv(1024)
        print '[+]%d/tcp open'% port
        # print '[+] '+str(result)
        connect.close()
    except Exception as e:
        print e
        print '[-]%d/tcp close'%port


def portScan(host, startPort, endPort):
    # 确定host有效
    try:
        tgtIp = socket.gethostbyname(host)
    except socket.gaierror as e:
        # e.message 什么都不打印
        # print e.message
        print e
        return
    try:
        tgtName = socket.gethostbyaddr(tgtIp)
        print tgtName
    except socket.herror as e:
        print e
        return
    for each_port in range(startPort, endPort):
        connectScan(host, each_port)
    print 'Done'


def main():
    start_time = time.time()
    parser = optparse.OptionParser('usage: -H <target host> '
                                   '-p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string',
                      help='specify target host')
    parser.add_option('--sp', dest='tgtStartPort', type='int',
                      help='specify tgtget start port')
    parser.add_option('--ep', dest='tgtEndPort', type='int',
                      help='specify tgtget end port')
    parser.add_option('-p', dest='tgtPort', type='int',
                      help='specify tgtget port')
    # 最后parse_args一下
    (options, args) = parser.parse_args()

    tgtHost = options.tgtHost
    startPort = options.tgtStartPort
    endPort = options.tgtEndPort

    if (options.tgtPort!=None):
        port = int(options.tgtPort)
        # try:
        #     connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #     # 这个函数决定参参数的格式
        #     connect.connect((tgtHost, port))
        #     connect.send('ViolentPython\r\n')
        #     result = connect.recv(1024)
        #     print '[+]%d/tcp open' % port
        #     print '[+] ' + str(result)
        #     connect.close()
        # except:
        #     print '[-]%d/tcp close' % port
        connectScan(tgtHost, port)
        exit(0)

    if (tgtHost==None)or(startPort==None)or(endPort==None):
        print 'must specify host and port'
        print parser.usage
        exit(0)

    portScan(tgtHost, startPort, endPort)
    end_time = time.time()
    print "total running time:{}".format(end_time-start_time)

if __name__ == '__main__':
    main()