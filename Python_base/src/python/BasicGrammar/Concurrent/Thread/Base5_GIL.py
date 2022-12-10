import time
import threading

"""
在我们的印象中，多线程要比单线程效率要高很多，而在下面的实验中，多线程不但没比单线程快，反而更慢。

这是因为有GIL（全局解释器锁）限制。
"""

print("----------------单线程------------------")
start = time.time()


def CountDown(n):
    while n > 0:
        n -= 1


CountDown(100000)
end = time.time()
print("Time used:", (end - start))

print("----------------两个线程------------------")

start = time.time()


def CountDown(n):
    while n > 0:
        n -= 1


t1 = threading.Thread(target=CountDown, args=[100000 // 2])
t2 = threading.Thread(target=CountDown, args=[100000 // 2])
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print("Time used:", (end - start))
