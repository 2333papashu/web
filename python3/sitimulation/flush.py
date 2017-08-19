import itertools
import sys
import time


def spin(msg, signal):  # 这个函数会在单独的线程中运行，signal 参数是前边定义的Signal类的实例
    write, flush = sys.stdout.write, sys.stdout.flush
    # 转义
    for char in itertools.cycle('|/-\\'):  # itertools.cycle 函数从指定的序列中反复不断地生成元素
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))  # 使用退格符把光标移回行首
        time.sleep(.1)  # 每 0.1 秒刷新一次
        if not signal:  # 如果 go属性不是 True，退出循环
            break

    # write(' ' * len(status) + '\x08' * len(status))  # 使用空格清除状态消息，把光标移回开头

if __name__ == '__main__':
    spin('haha', True)