import time
import sys

# msg = '{.2f}s'
msg = '{:.2f}s'
print(msg.format(2.003))
for i in range(5):
    # print(i)
    print('haha', end=' '),
    sys.stdout.flush()
    # 加这么一句才能实现定时刷新
    time.sleep(1)