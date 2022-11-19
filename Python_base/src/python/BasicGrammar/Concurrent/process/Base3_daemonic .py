import os
import time
from multiprocessing import Process

"""

守护进程：会随着主进程的结束而结束。
    守护进程会在主进程代码执行结束后就终止
    守护进程内无法再开启子进程,否则抛出异常
"""


class Myprocess(Process):
    def __init__(self, person):
        super().__init__()
        self.person = person

    def run(self):
        print(os.getpid(), self.name)
        print("父进程id：", os.getppid())
        print('%s正在和女主播聊天' % self.person)


if __name__ == '__main__':
    p = Myprocess('光头强')
    p.daemon = True  # 一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
    p.start()
    time.sleep(3)  # 在sleep时查看进程id对应的进程ps -ef|grep id
    print('主进程结束')
