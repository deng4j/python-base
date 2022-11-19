import threading
import time

"""
threading比thread提供了更高级别、功能更强的线程管理的功能。

避免使用thread模块，因为更高级别的threading模块更为先进，对线程的支持更为完善，而且使用thread模块里的属性
有可能会与threading出现冲突；其次低级别的thread模块的同步原语很少(实际上只有一个)，而threading模块则有很多；
再者，thread模块中当主线程结束时，所有的线程都会被强制结束掉，没有警告也不会有正常的清除工作，
至少threading模块能确保重要的子线程退出后进程才退出。

thread模块不支持守护线程，当主线程退出时，所有的子线程不论它们是否还在工作，都会被强行退出。
而threading模块支持守护线程，守护线程一般是一个等待客户请求的服务器，如果没有客户提出请求它就在那等着，
如果设定一个线程为守护线程，就表示这个线程是不重要的，在进程退出的时候，不用等待这个线程退出。

Thread实例对象的方法：
    run(): 用以表示线程活动的方法。
    start():启动线程活动
    join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
    isAlive()：返回线程是否活动的。
    getName()：返回线程名。
    setName()：设置线程名。
    
    
threading模块提供的一些方法：
    threading.currentThread()：返回当前的线程变量。
    threading.enumerate()：返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
    threading.activeCount()：返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
"""


def run(n):
    print("task：", n, "\n")
    time.sleep(1)

    strs = n + '：2s\n'
    print(strs)
    time.sleep(1)

    strs = n + '：1s\n'
    print(strs)
    time.sleep(1)

    strs = n + '：0s\n'
    print(strs)
    time.sleep(1)


if __name__ == '__main__':
    t1 = threading.Thread(target=run, args=("t1",))
    t2 = threading.Thread(target=run, kwargs={'n': 't2'})
    t1.start()
    t2.start()
