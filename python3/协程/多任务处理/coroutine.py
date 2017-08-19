# coding:utf-8
import queue
import time


class Task(object):
    tid = 0

    def __init__(self, target):
        Task.tid += 1
        self.tid = Task.tid
        self.target = target
        self.sendval = None

    def run(self):
        # 这里为什么是return
        # send的时候会接受到yield过来的值
        # 第一次send需要None
        return self.target.send(self.sendval)


class Scheduler(object):

    def __init__(self):
        self.task_map = {}
        self.ready = queue.Queue()

    def new(self, target):
        task = Task(target)
        self.task_map[task.tid] = task
        self.schedule(task)

    # 用来存储已准备好的task
    def schedule(self, task):
        self.ready.put(task)

    def exit(self, tid):
        # 删除一个键值
        del self.task_map[tid]

    def main_loop(self):

        while True:
            # if len(self.ready.queue) !=0:
            #     task = self.ready.get()

            if self.ready.queue.__len__() == 0:
                print("空的")
                # task = self.ready.get()
                # task.run()
                # print("空的也能运行")

                # run起来就break不出了
                break
            task = self.ready.get()
            try:
                result = task.run()
                # print(type(result))
                # print("main")
                # print(result)

                # 这里是与外界联系的交接处
                if isinstance(result, SystemCall):
                    result.task = task
                    result.scheduler = self
                    result.handler()
                    # 系统函数进入队列
                else:
                    print("send(None)")
            except StopIteration:
                self.exit(task.tid)
                continue
            self.schedule(task)
            print(self.ready.queue.__len__())
            time.sleep(1)


# 目前传的都是结果
# 系统调用的时候需要传过来的是系统函数
def first():
    for i in range(5):
        print("before yield")
        response = yield i
        print(i, " first : ", response)
        print("I am first")


def second():
    for i in range(10):
        print("before yield")
        response = yield i
        print(i, " second : ", response)
        print("I am second")


def third():
    while True:
        # 传递一个类对象
        tid = yield GetTid()
        print('this is third , my tid is %s' % tid)


def forth():
    while True:
        tid = yield GetTid()
        print('this is forth , my tid is %s' % tid)


# 需要实现系统调用
# 需要实现什么功能
class SystemCall(object):
    def __init__(self):
        self.task = None
        self.scheduler = None

    def handler(self):
        pass


class GetTid(SystemCall):
    def __init__(self):
        super().__init__()

    def handler(self):
        self.task.sendval = self.task.tid
        # 这一句相当于把当前任务放进队列 所以 我选择注释
        # self.scheduler.ready.put(self.task)


if __name__ == '__main__':
    # f = first()
    # for i in f:
    #     print(i)
    s = Scheduler()
    # s.new(third())
    # s.new(forth())
    s.new(first())
    s.new(second())
    s.main_loop()


# 实现了多任务yield并发 和系统应用的调用
# 熟悉send与yield之间的关系
# send(None)具体都发生了什么 None其实并没有赋值给yield的左边 而只是传递了yield的右边给send的左边
# 目前存在的问题 队列里面的任务越来越多
