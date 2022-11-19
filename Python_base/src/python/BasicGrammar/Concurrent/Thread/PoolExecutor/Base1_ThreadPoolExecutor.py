from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import os, time, random

"""
基本方法：
    submit(fn, *args, **kwargs)：异步提交任务
    map(func, *iterables, timeout=None, chunksize=1)：取代for循环submit的操作
    shutdown(wait=True)：相当于进程池的pool.close()+pool.join()操作：
        1.wait=True，等待池内所有任务执行完毕回收完资源后才继续
        2.wait=False，立即返回，并不会等待池内的任务执行完毕
        3.但不管wait参数为何值，整个程序都会等到所有任务执行完毕
    result(timeout=None)：取得结果
    add_done_callback(fn)：回调函数
    done()：判断某一个线程是否完成
    cancle()：取消某个任务
"""


def task(taskName):
    strName = "任务：" + str(taskName)
    print(strName)
    time.sleep(0.2)
    return str(os.getpid()) + "：" + str(taskName)


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=3)

    futures = []
    for i in range(10):
        future = executor.submit(task, i)
        futures.append(future)

    executor.shutdown(True)

    for future in futures:
        print(future.result())
