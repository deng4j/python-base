from multiprocessing import Process, JoinableQueue
import time, random, os

"""
JoinableQueue([maxsize])：创建可连接的共享进程队列。这就像是一个Queue对象，但队列允许项目的使用者
    通知生产者项目已经被成功处理。通知进程是使用共享的信号和条件变量来实现的。
    
    q.task_done() ：使用者使用此方法发出信号，表示q.get()返回的项目已经被处理。
        如果调用此方法的次数大于从队列中删除的项目数量，将引发ValueError异常。

    q.join() ：生产者将使用此方法进行阻塞，直到队列中所有项目均被处理。阻塞将持续到为队列中的每个项目均调用q.task_done()方法为止。
"""


def consumer(q):
    while True:
        res = q.get()
        time.sleep(random.randint(1, 3))
        print('%s 吃 %s' % (os.getpid(), res))
        q.task_done()  # 向q.join()发送一次信号,证明一个数据已经被取走了


def producer(name, q):
    for i in range(10):
        time.sleep(random.randint(1, 3))
        res = '%s%s' % (name, i)
        q.put(res)
        print('生产了 %s ：%s' % (os.getpid(), res))
    q.join()  # 生产完毕，使用此方法进行阻塞，直到队列中所有项目均被处理。


if __name__ == "__main__":
    q = JoinableQueue()
    # 生产者们:即厨师们
    p1 = Process(target=producer, args=('包子', q))
    p2 = Process(target=producer, args=('骨头', q))
    p3 = Process(target=producer, args=('泔水', q))

    # 消费者们:即吃货们
    c1 = Process(target=consumer, args=(q,))
    c2 = Process(target=consumer, args=(q,))
    c1.daemon = True
    c2.daemon = True

    # 开始
    p_l = [p1, p2, p3, c1, c2]
    for p in p_l:
        p.start()

    for p in p_l:
        p.join()

    print('结束！！！')
