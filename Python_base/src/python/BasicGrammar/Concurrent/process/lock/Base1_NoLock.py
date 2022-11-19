from multiprocessing import Process
import time, os, random

# 多个进程抢占资源的情况
n = 10


def work(i):
    global n  # 在多进程中，这样是只读的
    strN = "只读：" + str(n)
    print(strN)
    n -= 1

    time.sleep(random.random())

    print('%s: %s is running' % (i, os.getpid()))


if __name__ == '__main__':

    lists = []
    for i in range(10):
        p = Process(target=work, args=(i,))
        lists.append(p)
        p.start()
    for p in lists:
        p.join()
