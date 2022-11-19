import os, time
from multiprocessing import Pool

"""
Pool([numprocess  [,initializer [, initargs]]])：
    参数：
        numprocess：要创建的进程数，如果省略，将默认使用cpu_count()的值
        initializer：是每个工作进程启动时要执行的可调用对象，默认为None
        initargs：是要传给initializer的参数组
    方法：
        p.apply(func [, args [, kwargs]])：在一个池工作进程中执行func(*args,**kwargs),然后返回结果。
            需要强调的是：此操作并不会在所有池工作进程中并执行func函数。如果要通过不同参数并发地执行func函数，
            必须从不同线程调用p.apply()函数或者使用p.apply_async()
        p.apply_async(func [, args [, kwargs]])：在一个池工作进程中执行func(*args,**kwargs),然后返回结果。
            此方法的结果是AsyncResult类的实例，callback是可调用对象，接收输入参数。当func的结果变为可用时，
            将理解传递给callback。callback禁止执行任何阻塞操作，否则将接收其他异步操作中的结果。
        p.close()：关闭进程池，防止进一步操作。如果所有操作持续挂起，它们将在工作进程终止前完成。
        P.join()：等待所有工作进程退出。此方法只能在close()或teminate()之后调用。

    apply_async()和map_async()的返回值是AsyncResul的实例obj：
        obj.get()：返回结果，如果有必要则等待结果到达。timeout是可选的。如果在指定时间内还没有到达，将引发一场。
            如果远程操作中引发了异常，它将在调用此方法时再次被引发。
        obj.ready()：如果调用完成，返回True。
        obj.successful()：如果调用完成且没有引发异常，返回True，如果在结果就绪之前调用此方法，引发异常。
        obj.wait([timeout])：等待结果变为可用。
        obj.terminate()：立即终止所有工作进程，同时不执行任何清理或结束任何挂起工作。如果p被垃圾回收，将自动调用此函数。
"""


def work(n, res):
    print('%s run' % os.getpid())
    res.append(n)
    print(res)
    time.sleep(3)
    return n ** 2


# 同步
if __name__ == '__main__':
    p = Pool(3)
    res_l = []
    for i in range(5):
        # 同步调用，直到本次任务执行完毕拿到res，等待任务work执行的过程中可能有阻塞也可能没有阻塞
        res = p.apply(work, args=(i, res_l))
        res_l.append(res)
    print(res_l)
