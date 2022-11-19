from threading import Thread, Lock
import time

"""
互斥锁和join的区别：start后立即join:任务内的所有代码都是串行执行的,而加锁,只是加锁的部分即修改共享数据的部分是串行的
"""

# 多个线程抢占资源，互斥锁的引用

def work():
    global n
    lock.acquire()
    strN = str(n) + "\n"
    print(strN)
    n -= 1
    time.sleep(0.2)
    lock.release()


# 结果可能不为1
if __name__ == '__main__':
    lock = Lock()
    n = 10
    lists = []
    for i in range(10):
        p = Thread(target=work)
        lists.append(p)
        p.start()
    for p in lists:
        p.join()
