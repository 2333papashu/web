# coding:utf-8
import time
import requests
import os
import sys

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()

BASE_URL = 'http://flupy.org/data/flags'
DEST_DIR = 'images/'


def get_pic(url):
    response = requests.get(url)
    # 返回的是一个对象
    return response.content


def save_pic(image, name):
    path = os.path.join(DEST_DIR, name)
    # 二进制文件
    with open(path, 'wb') as f:
        f.write(image)


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


def download_pic(POP20_CC):
    # TODO 捕捉下载图片发生异常的情况
    for cc in POP20_CC:
        # 拼接url
        url = '{}\{cc}\{cc}.gif'.format(BASE_URL, cc=cc.lower())
        # +
        image = get_pic(url)
        save_pic(image, cc.lower()+'.gif')
        show(cc)
    return len(POP20_CC)


def main():
    start = time.time()
    count = download_pic(POP20_CC)
    end = time.time()
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, end-start))


# 20 flags downloaded in16.32s
# 总结：
# a. format,'+',os.path.join 灵活运用拼接字符串--目录开头没有'/'
#   eg:'images/' os.path.join函数的第一个参数
# b. sys.stdout.flush() 实现类似进度条的功能...
# 其他都是一些比较基本的程序结构设计
if __name__ == '__main__':
    main()

