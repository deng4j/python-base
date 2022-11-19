from threading import RLock

"""
递归锁：在Python中为了支持在同一线程中多次请求同一资源，python提供了可重入锁RLock。

RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，从而使得资源
可以被多次require。直到一个线程所有的acquire都被release，其他的线程才能获得资源。
"""

print("------------- 递归锁 -------------")

mutexA = RLock()
mutexA.acquire()
mutexA.acquire()
print(123)
mutexA.release()
mutexA.release()
