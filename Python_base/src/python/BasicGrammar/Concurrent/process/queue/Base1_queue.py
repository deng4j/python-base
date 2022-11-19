from multiprocessing import Queue

"""
multiprocess.Queue([maxsize])创建共享的进程队列：
    maxsize是队列中允许的最大项数。如果省略此参数，则无大小限制。
    底层队列使用管道和锁定实现。
    
方法：
    q.get([ block[ ,timeout]] )：返回q中的一个项目。如果q为空，此方法将阻塞，直到队列中有项目可用为止。
        block用于控制阻塞行为，默认为True. 如果设置为False，将引发Queue.Empty异常（定义在Queue模块中）。
        timeout是可选超时时间，用在阻塞模式中。如果在制定的时间间隔内没有项目变为可用，将引发Queue.Empty异常。
    q.get_nowait() ：同q.get(False)方法,如果队列满了不会阻塞，但是会因为队列满了而报错。
    q.put(item [, block [,timeout ] ] ) ：将item放入队列。如果队列已满，此方法将阻塞至有空间可用为止。
        block控制阻塞行为，默认为True。如果设置为False，将引发Queue.Empty异常（定义在Queue库模块中）。
        timeout指定在阻塞模式中等待可用空间的时间长短。超时后将引发Queue.Full异常。
    q.qsize() ：返回队列中目前项目的正确数量。此函数的结果并不可靠，因为在返回结果和在稍后程序中使用结果之间，
        队列中可能添加或删除了项目。在某些系统上，此方法可能引发NotImplementedError异常。
    q.empty() ：如果调用此方法时 q为空，返回True。如果其他进程或线程正在往队列中添加项目，结果是不可靠的。
        也就是说，在返回和使用结果之间，队列中可能已经加入新的项目。
    q.full() ：如果q已满，返回为True. 由于线程的存在，结果也可能是不可靠的。
    q.close() ：关闭队列，防止队列中加入更多数据。调用此方法时，后台线程将继续写入那些已入队列但尚未写入的数据，
        但将在此方法完成时马上关闭。如果q被垃圾收集，将自动调用此方法。关闭队列不会在队列使用者中生成任何类型的数据结束信号或异常。
        例如，如果某个使用者正被阻塞在get()操作上，关闭生产者中的队列不会导致get()方法返回错误。
    q.cancel_join_thread() ：不会再进程退出时自动连接后台线程。这可以防止join_thread()方法阻塞。
    q.join_thread() ：连接队列的后台线程。此方法用于在调用q.close()方法后，等待所有队列项被消耗。默认情况下，
        此方法由不是q的原始创建者的所有进程调用。调用q.cancel_join_thread()方法可以禁止这种行为。
"""

q = Queue(3)
q.put('first')
q.put('second')
q.put('third')

try:
    q.put_nowait(3)  # 可以使用put_nowait，如果队列满了不会阻塞，但是会因为队列满了而报错。
except:
    print('队列已经满了')

print("是否队满：", q.full())

print(q.get())
print(q.get())
print(q.get())