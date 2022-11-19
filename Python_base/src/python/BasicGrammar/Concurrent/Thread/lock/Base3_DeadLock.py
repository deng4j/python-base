from threading import Thread, Lock
import time

"""
死锁：两个或两个以上的进程或线程在执行过程中，因争夺资源而造成的一种互相等待的现象，若无外力作用，它们都将无法推进下去。
"""

print("------------- 死锁 -------------")

mutexA = Lock()
mutexA.acquire()
mutexA.acquire()
print(123)
mutexA.release()
mutexA.release()
