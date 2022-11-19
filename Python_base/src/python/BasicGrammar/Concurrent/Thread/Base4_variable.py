import threading
import time

"""
在⼀个进程内的所有线程共享全局变量，很⽅便在多个线程间共享数据。那就有并发修改问题。
"""

num = 0


def work1():
    global num

    for i in range(100):
        time.sleep(0.01)
        num += 1

    print("work1：", num)


def work2():
    global num

    for i in range(100):
        time.sleep(0.02)
        num += 1

    print("work2：", num)


if __name__ == '__main__':
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)
    t1.start()
    t2.start()
