from multiprocessing import Process, Lock
import time, os, random


# 使用锁维护执行顺序

def work(lock, i):
    time.sleep(random.random())

    print('%s: %s is running' % (i, os.getpid()))


if __name__ == '__main__':
    lock = Lock()
    lists = []
    for i in range(10):
        p = Process(target=work, args=(lock, i,))
        lists.append(p)
        p.start()
    for p in lists:
        p.join()
