import os
from multiprocessing.context import Process


# 通过继承Process类开启进程
class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(os.getpid())
        print('%s 正在和女主播聊天' % self.name)


if __name__ == '__main__':
    p1 = MyProcess('光头强')
    p2 = MyProcess('喜羊羊')
    p3 = MyProcess('张三')

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
